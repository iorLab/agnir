from __future__ import annotations

import unittest

from operation_dispatch_reference import classify_repository_intent


class RepositoryOperationDispatchTests(unittest.TestCase):
    def test_short_commit_intents_are_checkpoint_intercepted(self) -> None:
        for intent in ("commit", "提交", "提交代码"):
            plan = classify_repository_intent(intent, repository_context=True)
            self.assertIsNotNone(plan)
            assert plan is not None
            self.assertEqual(plan.steps[0], "checkpoint_evaluation")
            self.assertEqual(plan.steps[-1], "commit")
            self.assertIn("project_precommit_policy_if_declared", plan.steps)

    def test_commit_and_push_verifies_destination_after_push(self) -> None:
        for intent in ("commit and push", "提交推送"):
            plan = classify_repository_intent(intent, repository_context=True)
            self.assertIsNotNone(plan)
            assert plan is not None
            self.assertEqual(
                plan.steps,
                (
                    "checkpoint_evaluation",
                    "project_precommit_policy_if_declared",
                    "commit",
                    "push",
                    "verify_destination_ref",
                ),
            )

    def test_no_global_string_matching(self) -> None:
        self.assertIsNone(
            classify_repository_intent("explain how commit works", repository_context=True)
        )
        self.assertIsNone(classify_repository_intent("提交这个想法供讨论", repository_context=True))

    def test_non_repository_context_does_not_intercept_commit_word(self) -> None:
        self.assertIsNone(classify_repository_intent("commit", repository_context=False))


if __name__ == "__main__":
    unittest.main()
