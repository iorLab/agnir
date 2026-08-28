from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from repository_filesystem_reference import discover_repository_filesystem


PROJECT = "urn:test:agnir-boundary-project"


def write_project(root: Path, *, state_locator: str = ".agnir/state.md") -> None:
    (root / ".agnir/evidence").mkdir(parents=True)
    if state_locator == ".agnir/state.md":
        (root / ".agnir/state.md").write_text("# State\nboundary durable fact\n", encoding="utf-8")
    (root / ".agnir/next-actions.md").write_text("# Next\ncontinue boundary test\n", encoding="utf-8")
    (root / ".agnir/decisions.md").write_text("# Decisions\nboundary fixture\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        "agnir:\n"
        '  version: "0.1"\n'
        '  discovery_profile: "repository-filesystem/0.1"\n\n'
        "project:\n"
        f'  identity: "{PROJECT}"\n\n'
        "memory:\n"
        f'  state: "{state_locator}"\n'
        '  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n'
        '  evidence: ".agnir/evidence/"\n',
        encoding="utf-8",
    )


class RepositoryFilesystemBoundaryTests(unittest.TestCase):
    def test_symlink_project_entry_point_resolves_one_selected_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            project = base / "project"
            project.mkdir()
            write_project(project)
            entry = base / "project-entry"
            entry.symlink_to(project, target_is_directory=True)

            snapshot = discover_repository_filesystem(
                entry,
                expected_project_identity=PROJECT,
            )

            self.assertEqual(snapshot.project_root, project.resolve())
            self.assertIn("boundary durable fact", snapshot.state)

    def test_relative_memory_symlink_escape_requires_explicit_external_chain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            project = base / "project"
            project.mkdir()
            outside = base / "outside-state.md"
            outside.write_text("# State\noutside truth must not be adopted implicitly\n", encoding="utf-8")
            write_project(project, state_locator=".agnir/state-link.md")
            (project / ".agnir/state-link.md").symlink_to(outside)

            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem(
                    project,
                    expected_project_identity=PROJECT,
                )

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    @unittest.skipUnless(shutil.which("git"), "git executable required for worktree conformance")
    def test_git_worktree_root_cold_starts_without_repository_layout_assumption(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source"
            worktree = base / "worktree"
            source.mkdir()

            subprocess.run(["git", "init", "-b", "main"], cwd=source, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Agnir Conformance"], cwd=source, check=True)
            subprocess.run(["git", "config", "user.email", "conformance@example.invalid"], cwd=source, check=True)
            write_project(source)
            subprocess.run(["git", "add", "."], cwd=source, check=True)
            subprocess.run(
                ["git", "commit", "-m", "seed Agnir worktree fixture"],
                cwd=source,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "worktree", "add", "-b", "fixture-worktree", str(worktree)],
                cwd=source,
                check=True,
                capture_output=True,
            )

            self.assertTrue((worktree / ".git").is_file())
            self.assertTrue((worktree / "AGNIR.yaml").is_file())

            snapshot = discover_repository_filesystem(
                worktree,
                expected_project_identity=PROJECT,
            )

            self.assertEqual(snapshot.project_root, worktree.resolve())
            self.assertIn("boundary durable fact", snapshot.state)
            self.assertIn("continue boundary test", snapshot.next_actions)


if __name__ == "__main__":
    unittest.main()
