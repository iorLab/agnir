from __future__ import annotations

import unittest

from vcs_branch_continuity_reference import BranchContinuitySnapshot, VCSContinuityFailure
from vcs_lineage_binding_reference import (
    bind_snapshot,
    fork_lineage_binding,
    rebind_lineage_selector,
    validate_selected_binding,
)


class VCSLineageBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_snapshot = BranchContinuitySnapshot(
            "urn:p",
            "refs/heads/main",
            "sha-base",
            "baseline state",
            "baseline next",
        )
        self.source = bind_snapshot(
            self.source_snapshot,
            lineage_identity="urn:agnir:lineage:main",
        )

    def test_branch_fork_gets_new_lineage_identity_and_preserves_project(self) -> None:
        feature = fork_lineage_binding(
            self.source,
            new_ref="refs/heads/feature/a",
            new_lineage_identity="urn:agnir:lineage:feature-a",
            new_revision="sha-base",
        )
        self.assertEqual(feature.project_identity, self.source.project_identity)
        self.assertNotEqual(feature.lineage_identity, self.source.lineage_identity)
        self.assertNotEqual(feature.selector_ref, self.source.selector_ref)
        self.assertEqual(feature.checkpoint_receipt, self.source.checkpoint_receipt)
        self.assertEqual(feature.state, self.source.state)
        self.assertEqual(feature.next_actions, self.source.next_actions)

    def test_ref_rename_rebind_preserves_logical_lineage_identity(self) -> None:
        renamed = rebind_lineage_selector(
            self.source,
            new_ref="refs/heads/trunk",
            current_revision="sha-base",
        )
        self.assertEqual(renamed.project_identity, self.source.project_identity)
        self.assertEqual(renamed.lineage_identity, self.source.lineage_identity)
        self.assertNotEqual(renamed.selector_ref, self.source.selector_ref)
        self.assertEqual(renamed.state, self.source.state)

    def test_external_branch_copy_with_source_binding_is_not_auto_forked(self) -> None:
        with self.assertRaises(VCSContinuityFailure) as raised:
            validate_selected_binding(
                self.source,
                selected_ref="refs/heads/feature/copied-outside-agnir",
            )
        self.assertEqual(raised.exception.code, "AGNIR_VCS_LINEAGE_BINDING_MISMATCH")
        self.assertEqual(self.source.lineage_identity, "urn:agnir:lineage:main")

    def test_missing_binding_is_explicit_failure(self) -> None:
        with self.assertRaises(VCSContinuityFailure) as raised:
            validate_selected_binding(None, selected_ref="refs/heads/feature/a")
        self.assertEqual(raised.exception.code, "AGNIR_VCS_LINEAGE_BINDING_REQUIRED")

    def test_matching_binding_resolves_without_sibling_scan(self) -> None:
        resolved = validate_selected_binding(
            self.source,
            selected_ref="refs/heads/main",
        )
        self.assertEqual(resolved, self.source)

    def test_fork_cannot_reuse_source_logical_lineage_identity(self) -> None:
        with self.assertRaises(VCSContinuityFailure) as raised:
            fork_lineage_binding(
                self.source,
                new_ref="refs/heads/feature/a",
                new_lineage_identity=self.source.lineage_identity,
                new_revision="sha-base",
            )
        self.assertEqual(raised.exception.code, "AGNIR_VCS_LINEAGE_BINDING_MISMATCH")


if __name__ == "__main__":
    unittest.main()
