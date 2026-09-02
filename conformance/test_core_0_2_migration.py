from __future__ import annotations

import unittest

from core_0_2_migration_reference import (
    Core01Continuity,
    MigrationConflict,
    migrate_core_0_1_to_0_2,
)
from core_0_2_reference import LineageFailure
from upgrade_reference import UpgradeMigrationRequired


class Core02MigrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = Core01Continuity(
            project_identity="urn:agnir:test:migration",
            state="existing current truth",
            next_actions="existing next action",
            decisions="existing durable decision",
            evidence={"checkpoint-a": "existing evidence"},
            generation=7,
        )

    def test_core_line_change_requires_explicit_migration_authorization(self) -> None:
        with self.assertRaises(UpgradeMigrationRequired) as raised:
            migrate_core_0_1_to_0_2(
                self.source,
                initial_lineage_identity="primary",
                authorized=False,
                expected_source_generation=7,
            )
        self.assertEqual(raised.exception.code, "AGNIR_UPGRADE_MIGRATION_REQUIRED")

    def test_authorized_migration_preserves_project_and_continuity(self) -> None:
        migrated, changed = migrate_core_0_1_to_0_2(
            self.source,
            initial_lineage_identity="primary",
            authorized=True,
            expected_source_generation=7,
        )
        self.assertTrue(changed)
        self.assertEqual(migrated.project_identity, self.source.project_identity)
        self.assertEqual(migrated.default_lineage_identity, "primary")
        self.assertEqual(set(migrated.lineages), {"primary"})

        resumed = migrated.resolve()
        self.assertEqual(resumed.lineage_identity, "primary")
        self.assertEqual(resumed.state, self.source.state)
        self.assertEqual(resumed.next_actions, self.source.next_actions)
        self.assertEqual(resumed.decisions, self.source.decisions)
        self.assertEqual(resumed.evidence, self.source.evidence)

    def test_migration_does_not_alias_mutable_source_evidence(self) -> None:
        migrated, _ = migrate_core_0_1_to_0_2(
            self.source,
            initial_lineage_identity="primary",
            authorized=True,
        )
        self.source.evidence["late"] = "source-side mutation"
        self.assertNotIn("late", migrated.resolve().evidence)

    def test_repeating_same_migration_is_no_op(self) -> None:
        migrated, first_changed = migrate_core_0_1_to_0_2(
            self.source,
            initial_lineage_identity="primary",
            authorized=True,
        )
        repeated, second_changed = migrate_core_0_1_to_0_2(
            migrated,
            initial_lineage_identity="primary",
            authorized=True,
        )
        self.assertTrue(first_changed)
        self.assertFalse(second_changed)
        self.assertEqual(repeated, migrated)
        self.assertEqual(set(repeated.lineages), {"primary"})

    def test_repeated_migration_cannot_silently_rebind_initial_lineage(self) -> None:
        migrated, _ = migrate_core_0_1_to_0_2(
            self.source,
            initial_lineage_identity="primary",
            authorized=True,
        )
        with self.assertRaises(MigrationConflict) as raised:
            migrate_core_0_1_to_0_2(
                migrated,
                initial_lineage_identity="different",
                authorized=True,
            )
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")

    def test_missing_initial_lineage_identity_is_rejected(self) -> None:
        with self.assertRaises(LineageFailure) as raised:
            migrate_core_0_1_to_0_2(
                self.source,
                initial_lineage_identity="  ",
                authorized=True,
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_REQUIRED")

    def test_fresh_resume_of_selected_missing_lineage_does_not_fall_back(self) -> None:
        migrated, _ = migrate_core_0_1_to_0_2(
            self.source,
            initial_lineage_identity="primary",
            authorized=True,
        )
        with self.assertRaises(LineageFailure) as raised:
            migrated.resolve(explicit_lineage="missing")
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_NOT_FOUND")

    def test_stale_source_generation_blocks_migration_publication(self) -> None:
        newer_source = Core01Continuity(
            project_identity=self.source.project_identity,
            state="newer current truth",
            next_actions="newer next action",
            decisions=self.source.decisions,
            evidence=self.source.evidence,
            generation=8,
        )
        with self.assertRaises(MigrationConflict) as raised:
            migrate_core_0_1_to_0_2(
                newer_source,
                initial_lineage_identity="primary",
                authorized=True,
                expected_source_generation=7,
            )
        self.assertEqual(raised.exception.code, "AGNIR_MIGRATION_CONFLICT")


if __name__ == "__main__":
    unittest.main()
