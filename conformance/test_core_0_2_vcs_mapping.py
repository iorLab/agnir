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


MAIN_LINEAGE = "urn:agnir:lineage:main-logical"
FEATURE_LINEAGE = "urn:agnir:lineage:feature-logical"


class Core02VCSMappingTests(unittest.TestCase):
    def test_vcs_selector_precedence_resolves_to_independent_logical_identity(self) -> None:
        bindings = {
            "main": MAIN_LINEAGE,
            "feature/a": FEATURE_LINEAGE,
            "feature/context": "urn:agnir:lineage:context",
            "fallback": "urn:agnir:lineage:fallback",
        }
        explicit = select_vcs_lineage(
            bindings=bindings,
            explicit_ref="feature/a",
            current_context_ref="main",
            default_ref="fallback",
        )
        self.assertEqual(explicit.selector_ref, "feature/a")
        self.assertEqual(explicit.lineage_identity, FEATURE_LINEAGE)
        self.assertNotEqual(explicit.selector_ref, explicit.lineage_identity)

        contextual = select_vcs_lineage(
            bindings=bindings,
            current_context_ref="feature/context",
            default_ref="main",
        )
        self.assertEqual(contextual.selector_ref, "feature/context")
        self.assertEqual(contextual.lineage_identity, "urn:agnir:lineage:context")

        defaulted = select_vcs_lineage(bindings=bindings, default_ref="main")
        self.assertEqual(defaulted.selector_ref, "main")
        self.assertEqual(defaulted.lineage_identity, MAIN_LINEAGE)

    def test_selected_ref_without_binding_fails_instead_of_guessing_sibling(self) -> None:
        with self.assertRaises(VCSContinuityFailure) as raised:
            select_vcs_lineage(
                bindings={"main": MAIN_LINEAGE},
                explicit_ref="feature/unbound",
                default_ref="main",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_NOT_FOUND")

    def test_sha_rewrite_changes_receipt_not_logical_lineage_identity(self) -> None:
        before = BranchContinuitySnapshot(
            "urn:p",
            "feature/a",
            "sha-old",
            "feature ready",
            "review",
        )
        after = rewrite_revision(before, revision="sha-rewritten")
        before_view = branch_as_lineage(before, lineage_identity=FEATURE_LINEAGE)
        after_view = branch_as_lineage(after, lineage_identity=FEATURE_LINEAGE)

        self.assertEqual(before_view.project_identity, after_view.project_identity)
        self.assertEqual(before_view.lineage_identity, FEATURE_LINEAGE)
        self.assertEqual(after_view.lineage_identity, before_view.lineage_identity)
        self.assertNotEqual(after_view.checkpoint_receipt, before_view.checkpoint_receipt)
        self.assertEqual(after_view.state, before_view.state)

    def test_explicit_ref_rename_can_preserve_logical_lineage_identity(self) -> None:
        before = BranchContinuitySnapshot(
            "urn:p",
            "feature/a",
            "sha-1",
            "feature ready",
            "review",
        )
        renamed = BranchContinuitySnapshot(
            "urn:p",
            "feature/renamed",
            "sha-1",
            "feature ready",
            "review",
        )
        before_view = branch_as_lineage(before, lineage_identity=FEATURE_LINEAGE)
        renamed_view = branch_as_lineage(renamed, lineage_identity=FEATURE_LINEAGE)

        self.assertNotEqual(before_view.selector_ref, renamed_view.selector_ref)
        self.assertEqual(before_view.lineage_identity, renamed_view.lineage_identity)
        self.assertEqual(before_view.checkpoint_receipt, renamed_view.checkpoint_receipt)

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
                source_lineage_identity=FEATURE_LINEAGE,
                target_lineage_identity=MAIN_LINEAGE,
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
                source_lineage_identity=FEATURE_LINEAGE,
                target_lineage_identity=MAIN_LINEAGE,
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
                source_lineage_identity=FEATURE_LINEAGE,
                target_lineage_identity=MAIN_LINEAGE,
                result_revision="pick-result",
                reconciled_state="combined",
                reconciled_next_actions="verify",
            )
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_INTEGRATION_CONFLICT")

    def test_reconciled_vcs_publication_preserves_target_logical_lineage(self) -> None:
        source = BranchContinuitySnapshot("urn:p", "feature/a", "f1", "feature", "review")
        target = BranchContinuitySnapshot("urn:p", "main", "m1", "main", "ship")
        published = stage_and_publish_vcs_lineage_integration(
            event="merge",
            staged_source=source,
            staged_target=target,
            current_source=source,
            current_target=target,
            source_lineage_identity=FEATURE_LINEAGE,
            target_lineage_identity=MAIN_LINEAGE,
            result_revision="merge-result",
            reconciled_state="feature integrated into main",
            reconciled_next_actions="verify target",
        )
        self.assertEqual(published.project_identity, "urn:p")
        self.assertEqual(published.selector_ref, "main")
        self.assertEqual(published.lineage_identity, MAIN_LINEAGE)
        self.assertEqual(published.checkpoint_receipt, "merge-result")
        self.assertEqual(published.state, "feature integrated into main")
        self.assertNotEqual(published.state, source.state)


if __name__ == "__main__":
    unittest.main()
