from __future__ import annotations

import unittest

from core_0_2_vcs_mapping_reference import (
    branch_as_lineage,
    core_failure_code_for_vcs,
    select_vcs_lineage,
    stage_and_publish_vcs_lineage_integration,
)
from vcs_branch_continuity_reference import (
    BranchContinuitySnapshot,
    VCSContinuityFailure,
    rewrite_revision,
)


class Core02VCSMappingTests(unittest.TestCase):
    def test_vcs_selection_implements_core_lineage_precedence(self) -> None:
        self.assertEqual(
            select_vcs_lineage(
                explicit="feature/a",
                current_context="main",
                default="fallback",
            ),
            "feature/a",
        )
        self.assertEqual(
            select_vcs_lineage(current_context="feature/context", default="main"),
            "feature/context",
        )
        self.assertEqual(select_vcs_lineage(default="main"), "main")

    def test_ref_maps_to_logical_lineage_while_sha_maps_to_receipt(self) -> None:
        before = BranchContinuitySnapshot(
            "urn:p",
            "feature/a",
            "sha-old",
            "feature ready",
            "review",
        )
        after = rewrite_revision(before, revision="sha-rewritten")
        before_view = branch_as_lineage(before)
        after_view = branch_as_lineage(after)

        self.assertEqual(before_view.project_identity, after_view.project_identity)
        self.assertEqual(before_view.lineage_identity, "feature/a")
        self.assertEqual(after_view.lineage_identity, before_view.lineage_identity)
        self.assertNotEqual(after_view.checkpoint_receipt, before_view.checkpoint_receipt)
        self.assertEqual(after_view.state, before_view.state)

    def test_vcs_failure_codes_have_core_lineage_semantics(self) -> None:
        self.assertEqual(
            core_failure_code_for_vcs("AGNIR_VCS_REF_REQUIRED"),
            "AGNIR_LINEAGE_REQUIRED",
        )
        self.assertEqual(
            core_failure_code_for_vcs("AGNIR_VCS_RECONCILIATION_REQUIRED"),
            "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
        )
        self.assertEqual(
            core_failure_code_for_vcs("AGNIR_VCS_INTEGRATION_CONFLICT"),
            "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
        )
        self.assertEqual(
            core_failure_code_for_vcs("AGNIR_DISCOVERY_PROJECT_MISMATCH"),
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
        )

    def test_unreconciled_vcs_integration_maps_to_core_reconciliation_failure(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f1", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m1", "main", "ship")
        with self.assertRaises(VCSContinuityFailure) as raised:
            stage_and_publish_vcs_lineage_integration(
                event="merge",
                staged_source=source,
                staged_target=target,
                current_source=source,
                current_target=target,
                result_revision="merge-result",
                reconciled_state=None,
                reconciled_next_actions=None,
            )
        self.assertEqual(
            raised.exception.code,
            "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
        )

    def test_target_advancement_invalidates_staged_vcs_candidate(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f1", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m1", "main", "ship")
        newer_target = BranchContinuitySnapshot("urn:p", "main", "m2", "newer main", "re-stage")
        with self.assertRaises(VCSContinuityFailure) as raised:
            stage_and_publish_vcs_lineage_integration(
                event="merge",
                staged_source=source,
                staged_target=target,
                current_source=source,
                current_target=newer_target,
                result_revision="merge-result",
                reconciled_state="combined",
                reconciled_next_actions="verify",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_INTEGRATION_CONFLICT")

    def test_source_advancement_invalidates_staged_vcs_candidate(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f1", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m1", "main", "ship")
        newer_source = BranchContinuitySnapshot("urn:p", "feature/a", "f2", "new feature", "re-stage")
        with self.assertRaises(VCSContinuityFailure) as raised:
            stage_and_publish_vcs_lineage_integration(
                event="cherry-pick",
                staged_source=source,
                staged_target=target,
                current_source=newer_source,
                current_target=target,
                result_revision="pick-result",
                reconciled_state="combined",
                reconciled_next_actions="verify",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_INTEGRATION_CONFLICT")

    def test_reconciled_vcs_publication_stays_on_target_lineage(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f1", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m1", "main", "ship")
        published = stage_and_publish_vcs_lineage_integration(
            event="merge",
            staged_source=source,
            staged_target=target,
            current_source=source,
            current_target=target,
            result_revision="merge-result",
            reconciled_state="feature integrated into main",
            reconciled_next_actions="verify target",
        )
        self.assertEqual(published.project_identity, "urn:p")
        self.assertEqual(published.lineage_identity, "main")
        self.assertEqual(published.checkpoint_receipt, "merge-result")
        self.assertEqual(published.state, "feature integrated into main")
        self.assertNotEqual(published.state, source.state)


if __name__ == "__main__":
    unittest.main()
