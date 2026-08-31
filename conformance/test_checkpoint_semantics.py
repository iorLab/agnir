from __future__ import annotations

import unittest

from checkpoint_reference import (
    CheckpointConflict,
    CheckpointStoreReference,
    ContinuityCandidate,
)


class CheckpointSemanticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.initial = ContinuityCandidate(
            state="state-v1",
            next_actions="next-v1",
            decisions="decision-v1",
            evidence=(("seed", "evidence-v1"),),
        )
        self.store = CheckpointStoreReference(self.initial)

    def test_noop_evaluation_does_not_publish_new_revision(self) -> None:
        before = self.store.current
        published, changed = self.store.publish(
            base_revision=before.revision,
            candidate=self.initial,
        )
        self.assertFalse(changed)
        self.assertEqual(published, before)
        self.assertEqual(self.store.current.revision, 0)

    def test_publish_replaces_the_complete_checkpoint_as_one_generation(self) -> None:
        before = self.store.current
        candidate = ContinuityCandidate(
            state="state-v2",
            next_actions="next-v2",
            decisions="decision-v2",
            evidence=(("checkpoint", "evidence-v2"),),
        )

        self.assertEqual(self.store.current, before)
        published, changed = self.store.publish(
            base_revision=before.revision,
            candidate=candidate,
        )

        self.assertTrue(changed)
        self.assertEqual(published.revision, 1)
        self.assertEqual(published.checkpoint_id, "checkpoint-1")
        self.assertEqual(published.continuity, candidate)
        self.assertEqual(self.store.current.continuity.state, "state-v2")
        self.assertEqual(self.store.current.continuity.next_actions, "next-v2")
        self.assertEqual(self.store.current.continuity.decisions, "decision-v2")
        self.assertEqual(
            self.store.current.continuity.evidence,
            (("checkpoint", "evidence-v2"),),
        )

    def test_stale_base_revision_cannot_silently_overwrite_new_truth(self) -> None:
        base = self.store.current.revision
        first = ContinuityCandidate(
            state="first-writer",
            next_actions="next-first",
            decisions="decision-first",
        )
        second = ContinuityCandidate(
            state="second-writer",
            next_actions="next-second",
            decisions="decision-second",
        )

        self.store.publish(base_revision=base, candidate=first)

        with self.assertRaises(CheckpointConflict) as raised:
            self.store.publish(base_revision=base, candidate=second)

        self.assertIn("AGNIR_CHECKPOINT_CONFLICT", str(raised.exception))
        self.assertEqual(self.store.current.continuity, first)


if __name__ == "__main__":
    unittest.main()
