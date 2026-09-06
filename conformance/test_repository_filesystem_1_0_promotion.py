from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_0_2_migration_reference import MigrationConflict
from repository_filesystem_0_2_migration_reference import (
    publish_repository_filesystem_0_2_migration,
    stage_repository_filesystem_0_1_to_0_2,
)
from repository_filesystem_0_2_reference import discover_repository_filesystem_0_2
from repository_filesystem_1_0_promotion_reference import (
    publish_repository_filesystem_1_0_promotion,
    stage_repository_filesystem_0_2_to_1_0,
)
from repository_filesystem_1_0_reference import discover_repository_filesystem_1_0
from upgrade_reference import UpgradeMigrationRequired


PROJECT_ID = "urn:agnir:test:promotion"
LINEAGE_ID = "urn:agnir:lineage:promotion-primary"


def _write_core_0_2_project(root: Path) -> None:
    (root / ".agnir" / "evidence").mkdir(parents=True)
    (root / "KEEP.txt").write_text("unrelated project content\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        f'''agnir:\n  version: "0.2"\n  discovery_profile: "repository-filesystem/0.2"\n\nproject:\n  identity: "{PROJECT_ID}"\n  profiles:\n    - generic\n\ncontinuity:\n  lineage: "{LINEAGE_ID}"\n\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n\npolicy:\n  checkpoint: event-driven\n\nextensions:\n  example/custom:\n    preserve: true\n  agnir/vcs:\n    lineage_binding:\n      kind: "vcs-ref"\n      selector: "refs/heads/main"\n''',
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text("state 0.2\n", encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text("next 0.2\n", encoding="utf-8")
    (root / ".agnir" / "decisions.md").write_text("decision 0.2\n", encoding="utf-8")
    (root / ".agnir" / "evidence" / "checkpoint.md").write_text("evidence 0.2\n", encoding="utf-8")


def _write_core_0_1_project(root: Path) -> None:
    (root / ".agnir" / "evidence").mkdir(parents=True)
    (root / "KEEP.txt").write_text("unrelated project content\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        f'''agnir:\n  version: "0.1"\n  discovery_profile: "repository-filesystem/0.1"\n\nproject:\n  identity: "{PROJECT_ID}"\n  profiles:\n    - generic\n\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n\npolicy:\n  checkpoint: event-driven\n\nextensions:\n  example/custom:\n    preserve: true\n''',
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text("state from 0.1\n", encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text("next from 0.1\n", encoding="utf-8")
    (root / ".agnir" / "decisions.md").write_text("decision from 0.1\n", encoding="utf-8")
    (root / ".agnir" / "evidence" / "checkpoint.md").write_text("evidence from 0.1\n", encoding="utf-8")


class RepositoryFilesystem10PromotionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        _write_core_0_2_project(self.root)

    def test_unauthorized_promotion_is_rejected_without_mutation(self) -> None:
        before = (self.root / "AGNIR.yaml").read_bytes()
        with self.assertRaises(UpgradeMigrationRequired) as raised:
            stage_repository_filesystem_0_2_to_1_0(self.root, authorized=False)
        self.assertEqual(raised.exception.code, "AGNIR_UPGRADE_MIGRATION_REQUIRED")
        self.assertEqual((self.root / "AGNIR.yaml").read_bytes(), before)
        self.assertEqual(discover_repository_filesystem_0_2(self.root).version, "0.2")

    def test_staging_does_not_publish_and_candidate_changes_only_compatibility(self) -> None:
        before = (self.root / "AGNIR.yaml").read_text(encoding="utf-8")
        candidate = stage_repository_filesystem_0_2_to_1_0(
            self.root,
            authorized=True,
            expected_project_identity=PROJECT_ID,
            expected_lineage_identity=LINEAGE_ID,
        )
        self.assertTrue(candidate.changed)
        self.assertEqual((self.root / "AGNIR.yaml").read_text(encoding="utf-8"), before)
        self.assertIn('version: "1.0"', candidate.candidate_manifest_text)
        self.assertIn('discovery_profile: "repository-filesystem/1.0"', candidate.candidate_manifest_text)
        self.assertIn(f'identity: "{PROJECT_ID}"', candidate.candidate_manifest_text)
        self.assertIn(f'lineage: "{LINEAGE_ID}"', candidate.candidate_manifest_text)
        self.assertIn("example/custom:\n    preserve: true", candidate.candidate_manifest_text)
        self.assertIn('selector: "refs/heads/main"', candidate.candidate_manifest_text)

    def test_publish_preserves_identity_lineage_memory_locators_extensions_and_unrelated_content(self) -> None:
        manifest_before = (self.root / "AGNIR.yaml").read_text(encoding="utf-8")
        memory_paths = [
            self.root / ".agnir" / "state.md",
            self.root / ".agnir" / "next-actions.md",
            self.root / ".agnir" / "decisions.md",
            self.root / ".agnir" / "evidence" / "checkpoint.md",
            self.root / "KEEP.txt",
        ]
        before_bytes = {path: path.read_bytes() for path in memory_paths}

        candidate = stage_repository_filesystem_0_2_to_1_0(
            self.root,
            authorized=True,
            expected_project_identity=PROJECT_ID,
            expected_lineage_identity=LINEAGE_ID,
        )
        snapshot, changed = publish_repository_filesystem_1_0_promotion(candidate)

        self.assertTrue(changed)
        self.assertEqual(snapshot.version, "1.0")
        self.assertEqual(snapshot.profile, "repository-filesystem/1.0")
        self.assertEqual(snapshot.project_identity, PROJECT_ID)
        self.assertEqual(snapshot.lineage_identity, LINEAGE_ID)
        self.assertEqual(snapshot.state, "state 0.2\n")
        self.assertEqual(snapshot.next_actions, "next 0.2\n")
        self.assertEqual(snapshot.decisions, "decision 0.2\n")
        self.assertEqual(snapshot.evidence, {"checkpoint.md": "evidence 0.2\n"})
        for path, expected in before_bytes.items():
            self.assertEqual(path.read_bytes(), expected)

        manifest_after = (self.root / "AGNIR.yaml").read_text(encoding="utf-8")
        self.assertEqual(
            manifest_after,
            manifest_before
            .replace('version: "0.2"', 'version: "1.0"')
            .replace('discovery_profile: "repository-filesystem/0.2"', 'discovery_profile: "repository-filesystem/1.0"'),
        )
        with self.assertRaises(Exception):
            discover_repository_filesystem_0_2(self.root)
        self.assertEqual(discover_repository_filesystem_1_0(self.root), snapshot)

    def test_repeating_completed_promotion_is_no_op(self) -> None:
        first = stage_repository_filesystem_0_2_to_1_0(self.root, authorized=True)
        first_snapshot, first_changed = publish_repository_filesystem_1_0_promotion(first)
        manifest_after_first = (self.root / "AGNIR.yaml").read_bytes()

        second = stage_repository_filesystem_0_2_to_1_0(
            self.root,
            authorized=False,
            expected_project_identity=PROJECT_ID,
            expected_lineage_identity=LINEAGE_ID,
        )
        second_snapshot, second_changed = publish_repository_filesystem_1_0_promotion(second)
        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(second_snapshot, first_snapshot)
        self.assertEqual((self.root / "AGNIR.yaml").read_bytes(), manifest_after_first)

    def test_manifest_change_after_staging_rejects_stale_candidate(self) -> None:
        candidate = stage_repository_filesystem_0_2_to_1_0(self.root, authorized=True)
        manifest = self.root / "AGNIR.yaml"
        manifest.write_text(manifest.read_text(encoding="utf-8") + "\n# newer authoritative edit\n", encoding="utf-8")
        newer = manifest.read_bytes()
        with self.assertRaises(MigrationConflict) as raised:
            publish_repository_filesystem_1_0_promotion(candidate)
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")
        self.assertEqual(manifest.read_bytes(), newer)
        self.assertIn('version: "0.2"', manifest.read_text(encoding="utf-8"))

    def test_continuity_change_after_staging_rejects_stale_candidate(self) -> None:
        candidate = stage_repository_filesystem_0_2_to_1_0(self.root, authorized=True)
        state = self.root / ".agnir" / "state.md"
        state.write_text("newer authoritative state\n", encoding="utf-8")
        with self.assertRaises(MigrationConflict) as raised:
            publish_repository_filesystem_1_0_promotion(candidate)
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")
        self.assertIn('version: "0.2"', (self.root / "AGNIR.yaml").read_text(encoding="utf-8"))
        self.assertEqual(state.read_text(encoding="utf-8"), "newer authoritative state\n")

    def test_composed_0_1_to_0_2_to_1_0_preserves_established_lineage_migration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_core_0_1_project(root)
            migration = stage_repository_filesystem_0_1_to_0_2(
                root,
                lineage_identity=f"\u00a0{LINEAGE_ID}\u3000",
                authorized=True,
                expected_project_identity=PROJECT_ID,
            )
            snapshot_02, changed_02 = publish_repository_filesystem_0_2_migration(migration)
            self.assertTrue(changed_02)
            self.assertEqual(snapshot_02.lineage_identity, LINEAGE_ID)

            promotion = stage_repository_filesystem_0_2_to_1_0(
                root,
                authorized=True,
                expected_project_identity=PROJECT_ID,
                expected_lineage_identity=LINEAGE_ID,
            )
            snapshot_10, changed_10 = publish_repository_filesystem_1_0_promotion(promotion)
            self.assertTrue(changed_10)
            self.assertEqual(snapshot_10.project_identity, PROJECT_ID)
            self.assertEqual(snapshot_10.lineage_identity, LINEAGE_ID)
            self.assertEqual(snapshot_10.state, "state from 0.1\n")
            self.assertEqual(snapshot_10.next_actions, "next from 0.1\n")
            self.assertEqual(snapshot_10.decisions, "decision from 0.1\n")
            self.assertEqual(snapshot_10.evidence, {"checkpoint.md": "evidence from 0.1\n"})
            self.assertEqual((root / "KEEP.txt").read_text(encoding="utf-8"), "unrelated project content\n")


if __name__ == "__main__":
    unittest.main()
