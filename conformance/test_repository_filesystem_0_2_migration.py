from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_0_2_migration_reference import MigrationConflict
from core_reference import DiscoveryFailure
from repository_filesystem_0_2_migration_reference import (
    publish_repository_filesystem_0_2_migration,
    stage_repository_filesystem_0_1_to_0_2,
)
from repository_filesystem_reference import discover_repository_filesystem
from upgrade_reference import UpgradeMigrationRequired


PROJECT_ID = "urn:agnir:test:repository-migration"
LINEAGE_ID = "urn:agnir:lineage:migrated-primary"


def _write_core_0_1_project(root: Path) -> None:
    (root / ".agnir" / "evidence").mkdir(parents=True)
    (root / "AGNIR.yaml").write_text(
        f'''agnir:\n  version: "0.1"\n  discovery_profile: "repository-filesystem/0.1"\n\nproject:\n  identity: "{PROJECT_ID}"\n  profiles:\n    - generic\n\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n\npolicy:\n  checkpoint: event-driven\n\nextensions:\n  example/custom:\n    preserve: true\n''',
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text("existing state\n", encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text("existing next\n", encoding="utf-8")
    (root / ".agnir" / "decisions.md").write_text("existing decision\n", encoding="utf-8")
    (root / ".agnir" / "evidence" / "checkpoint.md").write_text(
        "existing evidence\n",
        encoding="utf-8",
    )


class RepositoryFilesystem02MigrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        _write_core_0_1_project(self.root)

    def test_unauthorized_migration_does_not_modify_manifest(self) -> None:
        before = (self.root / "AGNIR.yaml").read_bytes()
        with self.assertRaises(UpgradeMigrationRequired) as raised:
            stage_repository_filesystem_0_1_to_0_2(
                self.root,
                lineage_identity=LINEAGE_ID,
                authorized=False,
            )
        self.assertEqual(raised.exception.code, "AGNIR_UPGRADE_MIGRATION_REQUIRED")
        self.assertEqual((self.root / "AGNIR.yaml").read_bytes(), before)

    def test_staging_does_not_publish_core_0_2(self) -> None:
        before = discover_repository_filesystem(self.root)
        candidate = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
            expected_project_identity=PROJECT_ID,
        )
        self.assertTrue(candidate.changed)
        during = discover_repository_filesystem(self.root)
        self.assertEqual(during, before)
        self.assertNotIn("continuity:", (self.root / "AGNIR.yaml").read_text(encoding="utf-8"))

    def test_publish_preserves_durable_memory_and_unrelated_manifest_content(self) -> None:
        memory_paths = [
            self.root / ".agnir" / "state.md",
            self.root / ".agnir" / "next-actions.md",
            self.root / ".agnir" / "decisions.md",
            self.root / ".agnir" / "evidence" / "checkpoint.md",
        ]
        before_memory = {path: path.read_bytes() for path in memory_paths}

        candidate = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        snapshot, changed = publish_repository_filesystem_0_2_migration(candidate)

        self.assertTrue(changed)
        self.assertEqual(snapshot.project_identity, PROJECT_ID)
        self.assertEqual(snapshot.lineage_identity, LINEAGE_ID)
        self.assertEqual(snapshot.state, "existing state\n")
        self.assertEqual(snapshot.next_actions, "existing next\n")
        self.assertEqual(snapshot.decisions, "existing decision\n")
        self.assertEqual(snapshot.evidence["checkpoint.md"], "existing evidence\n")
        for path, expected in before_memory.items():
            self.assertEqual(path.read_bytes(), expected)

        manifest = (self.root / "AGNIR.yaml").read_text(encoding="utf-8")
        self.assertIn('version: "0.2"', manifest)
        self.assertIn('discovery_profile: "repository-filesystem/0.2"', manifest)
        self.assertIn("continuity:\n", manifest)
        self.assertIn(f'lineage: "{LINEAGE_ID}"', manifest)
        self.assertIn("profiles:\n    - generic", manifest)
        self.assertIn("example/custom:\n    preserve: true", manifest)
        self.assertIn("checkpoint: event-driven", manifest)

    def test_stable_core_0_1_resolver_rejects_published_0_2(self) -> None:
        candidate = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        publish_repository_filesystem_0_2_migration(candidate)
        with self.assertRaises(DiscoveryFailure) as raised:
            discover_repository_filesystem(self.root)
        self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_repeating_identical_migration_is_no_op(self) -> None:
        first = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        first_snapshot, first_changed = publish_repository_filesystem_0_2_migration(first)
        manifest_after_first = (self.root / "AGNIR.yaml").read_bytes()

        second = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        second_snapshot, second_changed = publish_repository_filesystem_0_2_migration(second)

        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(second_snapshot, first_snapshot)
        self.assertEqual((self.root / "AGNIR.yaml").read_bytes(), manifest_after_first)

    def test_repeated_migration_cannot_rebind_lineage(self) -> None:
        first = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        publish_repository_filesystem_0_2_migration(first)
        with self.assertRaises(MigrationConflict) as raised:
            stage_repository_filesystem_0_1_to_0_2(
                self.root,
                lineage_identity="urn:agnir:lineage:different",
                authorized=True,
            )
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")

    def test_manifest_change_after_staging_invalidates_candidate(self) -> None:
        candidate = stage_repository_filesystem_0_1_to_0_2(
            self.root,
            lineage_identity=LINEAGE_ID,
            authorized=True,
        )
        manifest_path = self.root / "AGNIR.yaml"
        manifest_path.write_text(
            manifest_path.read_text(encoding="utf-8") + "\n# newer authoritative edit\n",
            encoding="utf-8",
        )
        newer = manifest_path.read_bytes()

        with self.assertRaises(MigrationConflict) as raised:
            publish_repository_filesystem_0_2_migration(candidate)
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")
        self.assertEqual(manifest_path.read_bytes(), newer)
        self.assertNotIn("continuity:", manifest_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
