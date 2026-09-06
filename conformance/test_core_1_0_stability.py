from __future__ import annotations

import unittest

from checkpoint_reference import CheckpointConflict, CheckpointStoreReference, ContinuityCandidate
from core_1_0_reference import (
    CORE_1_0_VERSION,
    ContinuityLineageSnapshot,
    LineageFailure,
    make_integration_candidate,
    require_reconciliation,
    select_lineage,
)


class Core10StabilityTests(unittest.TestCase):
    def test_version_and_lineage_selection_preserve_core_0_2_behavior(self) -> None:
        self.assertEqual(CORE_1_0_VERSION, "1.0")
        self.assertEqual(
            select_lineage(explicit=None, current_context="urn:lineage:context", default="urn:lineage:default"),
            "urn:lineage:context",
        )
        with self.assertRaises(LineageFailure) as raised:
            select_lineage(explicit=None, current_context=None, default=None)
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_REQUIRED")

    def test_checkpoint_no_op_material_and_stale_conflict_remain_stable(self) -> None:
        initial = ContinuityCandidate(
            state="state-0",
            next_actions="next-0",
            decisions="decision-0",
            evidence=(("checkpoint.md", "evidence-0"),),
        )
        store = CheckpointStoreReference(initial)

        unchanged, changed = store.publish(base_revision=0, candidate=initial)
        self.assertFalse(changed)
        self.assertEqual(unchanged.revision, 0)

        material = ContinuityCandidate(
            state="state-1",
            next_actions="next-1",
            decisions="decision-0",
            evidence=(("checkpoint.md", "evidence-1"),),
        )
        published, changed = store.publish(base_revision=0, candidate=material)
        self.assertTrue(changed)
        self.assertEqual(published.revision, 1)
        self.assertEqual(store.current.continuity, material)

        with self.assertRaises(CheckpointConflict) as raised:
            store.publish(base_revision=0, candidate=initial)
        self.assertEqual(raised.exception.code, "AGNIR_CHECKPOINT_CONFLICT")
        self.assertEqual(store.current, published)

    def test_lineage_integration_requires_reconciliation_without_identity_conflation(self) -> None:
        target = ContinuityLineageSnapshot(
            project_identity="urn:project:p",
            lineage_identity="urn:lineage:target",
            project_state="project-target",
            state="target-state",
            next_actions="target-next",
            decisions=None,
            evidence={},
            generation=5,
        )
        source = ContinuityLineageSnapshot(
            project_identity="urn:project:p",
            lineage_identity="urn:lineage:source",
            project_state="project-source",
            state="source-state",
            next_actions="source-next",
            decisions=None,
            evidence={},
            generation=8,
        )
        candidate = make_integration_candidate(
            target=target,
            sources=[source],
            resulting_project_state="integrated-project",
        )
        self.assertEqual(candidate.target_lineage_identity, "urn:lineage:target")
        self.assertEqual(candidate.source_lineage_identities, ("urn:lineage:source",))
        self.assertEqual(target.receipt, "generation:5")
        self.assertNotEqual(target.receipt, target.lineage_identity)

        with self.assertRaises(LineageFailure) as raised:
            require_reconciliation(reconciled=False)
        self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_RECONCILIATION_REQUIRED")
        require_reconciliation(reconciled=True)


if __name__ == "__main__":
    unittest.main()
