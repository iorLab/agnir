from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from repository_filesystem_reference import discover_repository_filesystem
from vcs_branch_continuity_reference import (
    BranchContinuitySnapshot,
    VCSContinuityFailure,
    branch_from,
    checkpoint_branch,
    integration_requires_reconciliation,
    reconcile_integration,
    rewrite_revision,
    select_working_ref,
    verification_ref,
)


def _git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def _write_project(root: Path, state: str, next_actions: str) -> None:
    (root / ".agnir").mkdir(parents=True, exist_ok=True)
    (root / "AGNIR.yaml").write_text(
        """agnir:\n  version: \"0.1\"\n  discovery_profile: \"repository-filesystem/0.1\"\nproject:\n  identity: \"urn:agnir:test:parallel\"\nmemory:\n  state: \".agnir/state.md\"\n  next_actions: \".agnir/next-actions.md\"\n  decisions: null\n  evidence: null\n""",
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text(state, encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text(next_actions, encoding="utf-8")


class VCSBranchContinuityTests(unittest.TestCase):
    def test_working_ref_selection_never_guesses_sibling_branch(self) -> None:
        self.assertEqual(
            select_working_ref(
                requested_ref="feature/a",
                current_context_ref="main",
                default_ref="main",
            ),
            "feature/a",
        )
        self.assertEqual(
            select_working_ref(current_context_ref="feature/worktree", default_ref="main"),
            "feature/worktree",
        )
        self.assertEqual(select_working_ref(default_ref="main"), "main")
        with self.assertRaises(VCSContinuityFailure) as ctx:
            select_working_ref()
        self.assertEqual(ctx.exception.code, "AGNIR_VCS_REF_REQUIRED")

    def test_real_git_worktree_resolves_branch_local_truth(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "project"
            feature_worktree = Path(tmp) / "feature-worktree"
            repo.mkdir()
            subprocess.run(["git", "init", "-b", "main", str(repo)], check=True, capture_output=True)
            _git(repo, "config", "user.name", "Agnir Conformance")
            _git(repo, "config", "user.email", "agnir@example.invalid")
            _write_project(repo, "base state\n", "base next\n")
            _git(repo, "add", ".")
            _git(repo, "commit", "-m", "base")
            _git(repo, "branch", "feature/parallel")

            (repo / ".agnir" / "state.md").write_text("main state\n", encoding="utf-8")
            _git(repo, "add", ".agnir/state.md")
            _git(repo, "commit", "-m", "main continuity")

            _git(repo, "worktree", "add", str(feature_worktree), "feature/parallel")
            (feature_worktree / ".agnir" / "state.md").write_text("feature state\n", encoding="utf-8")
            _git(feature_worktree, "add", ".agnir/state.md")
            _git(feature_worktree, "commit", "-m", "feature continuity")

            main = discover_repository_filesystem(repo)
            feature = discover_repository_filesystem(feature_worktree)
            self.assertEqual(main.project_identity, feature.project_identity)
            self.assertEqual(main.state, "main state\n")
            self.assertEqual(feature.state, "feature state\n")

    def test_real_git_merge_reconciles_before_target_ref_advances(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "project"
            repo.mkdir()
            subprocess.run(["git", "init", "-b", "main", str(repo)], check=True, capture_output=True)
            _git(repo, "config", "user.name", "Agnir Conformance")
            _git(repo, "config", "user.email", "agnir@example.invalid")
            _write_project(repo, "base state\n", "base next\n")
            (repo / "project.txt").write_text("base\n", encoding="utf-8")
            _git(repo, "add", ".")
            _git(repo, "commit", "-m", "base")
            _git(repo, "branch", "feature/parallel")

            (repo / ".agnir" / "state.md").write_text("main state\n", encoding="utf-8")
            (repo / ".agnir" / "next-actions.md").write_text("main next\n", encoding="utf-8")
            (repo / "main.txt").write_text("main work\n", encoding="utf-8")
            _git(repo, "add", ".")
            _git(repo, "commit", "-m", "main advances")
            main_before_merge = _git(repo, "rev-parse", "HEAD")

            _git(repo, "checkout", "feature/parallel")
            (repo / ".agnir" / "state.md").write_text("feature state\n", encoding="utf-8")
            (repo / ".agnir" / "next-actions.md").write_text("feature next\n", encoding="utf-8")
            (repo / "feature.txt").write_text("feature work\n", encoding="utf-8")
            _git(repo, "add", ".")
            _git(repo, "commit", "-m", "feature advances")
            _git(repo, "checkout", "main")

            merge = subprocess.run(
                ["git", "-C", str(repo), "merge", "--no-commit", "--no-ff", "feature/parallel"],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(merge.returncode, 0, "divergent continuity should require explicit conflict resolution")
            self.assertEqual(
                _git(repo, "rev-parse", "HEAD"),
                main_before_merge,
                "target ref must not advance while the integration candidate is unreconciled",
            )

            (repo / ".agnir" / "state.md").write_text(
                "feature integrated; main work preserved\n",
                encoding="utf-8",
            )
            (repo / ".agnir" / "next-actions.md").write_text(
                "verify integrated target\n",
                encoding="utf-8",
            )
            _git(repo, "add", ".")
            _git(repo, "commit", "-m", "merge feature with reconciled target continuity")

            merge_head = _git(repo, "rev-parse", "HEAD")
            self.assertNotEqual(merge_head, main_before_merge)
            parents = _git(repo, "rev-list", "--parents", "-n", "1", "HEAD").split()
            self.assertEqual(len(parents), 3, "final target publication should be one two-parent merge revision")

            target = discover_repository_filesystem(repo)
            self.assertEqual(target.project_identity, "urn:agnir:test:parallel")
            self.assertEqual(target.state, "feature integrated; main work preserved\n")
            self.assertEqual(target.next_actions, "verify integrated target\n")

    def test_branch_checkpoint_is_isolated_from_sibling_snapshot(self) -> None:
        main = BranchContinuitySnapshot("urn:p", "main", "a", "base", "ship")
        feature = branch_from(main, ref="feature/a", revision="b")
        feature2 = checkpoint_branch(feature, revision="c", state="feature ready", next_actions="review")
        self.assertEqual(main.state, "base")
        self.assertEqual(main.ref, "main")
        self.assertEqual(feature2.state, "feature ready")

    def test_integration_events_require_explicit_reconciliation(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m", "main", "deploy")
        for event in ("merge", "rebase", "cherry-pick"):
            self.assertTrue(integration_requires_reconciliation(event))
            with self.assertRaises(VCSContinuityFailure) as ctx:
                reconcile_integration(
                    event=event,
                    source=source,
                    target=target,
                    result_revision="r",
                    reconciled_state=None,
                    reconciled_next_actions=None,
                )
            self.assertEqual(ctx.exception.code, "AGNIR_VCS_RECONCILIATION_REQUIRED")

    def test_reconciled_result_belongs_to_target_ref(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m", "main", "deploy")
        result = reconcile_integration(
            event="merge",
            source=source,
            target=target,
            result_revision="z",
            reconciled_state="feature integrated and main deployment preserved",
            reconciled_next_actions="deploy combined result",
        )
        self.assertEqual(result.ref, "main")
        self.assertEqual(result.project_identity, "urn:p")
        self.assertNotEqual(result.state, source.state)

    def test_cross_project_integration_is_rejected(self) -> None:
        source = BranchContinuitySnapshot("urn:source", "feature/a", "f", "feature", "review")
        target = BranchContinuitySnapshot("urn:target", "main", "m", "main", "deploy")
        with self.assertRaises(VCSContinuityFailure) as ctx:
            reconcile_integration(
                event="merge",
                source=source,
                target=target,
                result_revision="z",
                reconciled_state="x",
                reconciled_next_actions="y",
            )
        self.assertEqual(ctx.exception.code, "AGNIR_DISCOVERY_PROJECT_MISMATCH")

    def test_rebase_revision_rewrite_preserves_project_and_truth(self) -> None:
        before = BranchContinuitySnapshot("urn:p", "feature/a", "old", "ready", "review")
        after = rewrite_revision(before, revision="new")
        self.assertEqual(after.project_identity, before.project_identity)
        self.assertEqual(after.ref, before.ref)
        self.assertEqual(after.state, before.state)
        self.assertEqual(after.next_actions, before.next_actions)
        self.assertNotEqual(after.revision, before.revision)

    def test_push_verifies_destination_ref(self) -> None:
        self.assertEqual(
            verification_ref(destination_ref="feature/a", authoritative_ref="main", claims_authoritative=False),
            "feature/a",
        )
        self.assertEqual(
            verification_ref(destination_ref="main", authoritative_ref="main", claims_authoritative=True),
            "main",
        )
        with self.assertRaises(VCSContinuityFailure) as ctx:
            verification_ref(destination_ref="feature/a", authoritative_ref="main", claims_authoritative=True)
        self.assertEqual(ctx.exception.code, "AGNIR_VCS_AUTHORITY_MISMATCH")


if __name__ == "__main__":
    unittest.main()
