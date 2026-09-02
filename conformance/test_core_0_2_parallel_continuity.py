from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_0_2_reference import LineageFailure, select_lineage
from sqlite_lineage_reference import SQLiteLineageEntryPoint, SQLiteLineageReference


PROJECT_ID = "urn:agnir:test:parallel-project"


class Core02ParallelContinuityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.database = Path(self.temp_dir.name) / "continuity.sqlite3"
        self.entry = SQLiteLineageEntryPoint(self.database, "project-p")
        self.backend = SQLiteLineageReference()
        self.backend.create_project(
            self.entry,
            project_identity=PROJECT_ID,
            initial_lineage_identity="main",
            default_lineage_identity="main",
            project_state="project baseline",
            state="main baseline",
            next_actions="main baseline next",
            decisions="shared baseline decision",
        )

    def test_lineage_selection_is_explicit_contextual_then_default(self) -> None:
        self.assertEqual(
            select_lineage(explicit="feature", current_context="main", default="fallback"),
            "feature",
        )
        self.assertEqual(
            select_lineage(current_context="work-context", default="fallback"),
            "work-context",
        )
        self.assertEqual(select_lineage(default="main"), "main")
        with self.assertRaises(LineageFailure) as raised:
            select_lineage()
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_REQUIRED")

    def test_selected_missing_lineage_does_not_fall_back_to_default(self) -> None:
        with self.assertRaises(LineageFailure) as raised:
            self.backend.load(self.entry, explicit_lineage="does-not-exist")
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_NOT_FOUND")

    def test_forked_lineages_keep_project_identity_and_checkpoint_independently(self) -> None:
        feature = self.backend.fork_lineage(
            self.entry,
            source_lineage="main",
            new_lineage="feature",
        )
        self.assertEqual(feature.project_identity, PROJECT_ID)
        self.assertEqual(feature.lineage_identity, "feature")

        feature = self.backend.checkpoint(
            self.entry,
            lineage_identity="feature",
            project_state="project with feature experiment",
            state="feature implementation active",
            next_actions="validate feature",
            decisions="feature-only decision",
            evidence_key="feature-checkpoint",
            evidence_value="feature advanced",
            expected_generation=feature.generation,
        )
        main = self.backend.load(self.entry, explicit_lineage="main")

        self.assertEqual(main.project_identity, feature.project_identity)
        self.assertEqual(main.state, "main baseline")
        self.assertEqual(main.project_state, "project baseline")
        self.assertNotIn("feature-checkpoint", main.evidence)
        self.assertEqual(feature.state, "feature implementation active")
        self.assertEqual(feature.generation, 1)

    def test_backend_receipt_changes_without_changing_lineage_identity(self) -> None:
        before = self.backend.load(self.entry, explicit_lineage="main")
        after = self.backend.checkpoint(
            self.entry,
            lineage_identity="main",
            project_state="project baseline plus note",
            state="main advanced",
            next_actions="continue",
            decisions=before.decisions,
            expected_generation=before.generation,
        )
        self.assertEqual(before.lineage_identity, after.lineage_identity)
        self.assertNotEqual(before.receipt, after.receipt)
        self.assertEqual(after.receipt, "generation:1")

    def test_staged_integration_keeps_target_authoritative_until_coherent_publish(self) -> None:
        feature = self.backend.fork_lineage(
            self.entry,
            source_lineage="main",
            new_lineage="feature",
        )
        self.backend.checkpoint(
            self.entry,
            lineage_identity="feature",
            project_state="project feature result",
            state="feature complete",
            next_actions="integrate feature",
            decisions="feature implementation decision",
            evidence_key="feature-result",
            evidence_value="validated source result",
            expected_generation=feature.generation,
        )

        main_before = self.backend.load(self.entry, explicit_lineage="main")
        feature_before = self.backend.load(self.entry, explicit_lineage="feature")
        candidate = self.backend.stage_integration(
            target_entry_point=self.entry,
            target_lineage="main",
            source_entry_point=self.entry,
            source_lineage="feature",
            resulting_project_state="project integrated result",
        )

        # Staging is not publication: fresh target discovery must still see old truth.
        main_during_stage = self.backend.load(self.entry, explicit_lineage="main")
        self.assertEqual(main_during_stage, main_before)

        with self.assertRaises(LineageFailure) as raised:
            self.backend.publish_integration(
                target_entry_point=self.entry,
                source_entry_point=self.entry,
                candidate=candidate,
                reconciled=False,
                state="should not publish",
                next_actions="should not publish",
                decisions=None,
                evidence_key="invalid",
                evidence_value="invalid",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_RECONCILIATION_REQUIRED")
        self.assertEqual(
            self.backend.load(self.entry, explicit_lineage="main"),
            main_before,
        )

        published = self.backend.publish_integration(
            target_entry_point=self.entry,
            source_entry_point=self.entry,
            candidate=candidate,
            reconciled=True,
            state="main contains reconciled feature result",
            next_actions="continue from integrated main",
            decisions="target decision incorporates relevant source rationale",
            evidence_key="integration",
            evidence_value="feature reconciled into main",
        )
        source_after = self.backend.load(self.entry, explicit_lineage="feature")

        self.assertEqual(published.project_state, "project integrated result")
        self.assertEqual(published.state, "main contains reconciled feature result")
        self.assertEqual(published.generation, main_before.generation + 1)
        self.assertEqual(source_after, feature_before)
        self.assertIn("integration", published.evidence)

    def test_target_advancement_after_staging_causes_integration_conflict(self) -> None:
        self.backend.fork_lineage(
            self.entry,
            source_lineage="main",
            new_lineage="feature",
        )
        candidate = self.backend.stage_integration(
            target_entry_point=self.entry,
            target_lineage="main",
            source_entry_point=self.entry,
            source_lineage="feature",
            resulting_project_state="candidate result",
        )
        main = self.backend.load(self.entry, explicit_lineage="main")
        self.backend.checkpoint(
            self.entry,
            lineage_identity="main",
            project_state="newer target state",
            state="target advanced independently",
            next_actions="re-stage integration",
            decisions=main.decisions,
            expected_generation=main.generation,
        )

        with self.assertRaises(LineageFailure) as raised:
            self.backend.publish_integration(
                target_entry_point=self.entry,
                source_entry_point=self.entry,
                candidate=candidate,
                reconciled=True,
                state="stale integration",
                next_actions="invalid",
                decisions=None,
                evidence_key="stale",
                evidence_value="must not publish",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_INTEGRATION_CONFLICT")
        fresh_main = self.backend.load(self.entry, explicit_lineage="main")
        self.assertEqual(fresh_main.state, "target advanced independently")

    def test_source_advancement_after_staging_causes_integration_conflict(self) -> None:
        feature = self.backend.fork_lineage(
            self.entry,
            source_lineage="main",
            new_lineage="feature",
        )
        candidate = self.backend.stage_integration(
            target_entry_point=self.entry,
            target_lineage="main",
            source_entry_point=self.entry,
            source_lineage="feature",
            resulting_project_state="candidate result",
        )
        self.backend.checkpoint(
            self.entry,
            lineage_identity="feature",
            project_state="source changed after staging",
            state="feature moved",
            next_actions="re-stage",
            decisions=feature.decisions,
            expected_generation=feature.generation,
        )
        with self.assertRaises(LineageFailure) as raised:
            self.backend.publish_integration(
                target_entry_point=self.entry,
                source_entry_point=self.entry,
                candidate=candidate,
                reconciled=True,
                state="stale source integration",
                next_actions="invalid",
                decisions=None,
                evidence_key="stale-source",
                evidence_value="must not publish",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_INTEGRATION_CONFLICT")

    def test_cross_project_integration_is_rejected(self) -> None:
        other_entry = SQLiteLineageEntryPoint(self.database, "project-q")
        self.backend.create_project(
            other_entry,
            project_identity="urn:agnir:test:other-project",
            initial_lineage_identity="other",
            default_lineage_identity="other",
            project_state="other project",
            state="other state",
            next_actions="other next",
        )
        with self.assertRaises(LineageFailure) as raised:
            self.backend.stage_integration(
                target_entry_point=self.entry,
                target_lineage="main",
                source_entry_point=other_entry,
                source_lineage="other",
                resulting_project_state="must not integrate",
            )
        self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_PROJECT_MISMATCH")


if __name__ == "__main__":
    unittest.main()
