from __future__ import annotations

import unittest

from agents_merge_reference import AgentsMergeConflict, merge_agents_locator


class AgentsMergeTests(unittest.TestCase):
    def test_existing_agents_content_is_preserved(self) -> None:
        existing = (
            "# Agent Instructions\n\n"
            "- Run tests before committing.\n"
            "- Follow CONTRIBUTING.md.\n"
            "- Never edit generated files manually.\n"
        )

        merged = merge_agents_locator(existing)

        self.assertTrue(merged.startswith(existing))
        self.assertIn("## Agnir", merged)
        self.assertIn("Agnir Project Instructions", merged)
        self.assertIn("README.md", merged)
        self.assertNotIn("Current State", merged)
        self.assertNotIn("Next Actions", merged)

    def test_missing_agents_gets_minimal_locator(self) -> None:
        merged = merge_agents_locator(None)

        self.assertTrue(merged.startswith("# Agent Instructions\n"))
        self.assertIn("## Agnir", merged)
        self.assertIn("README.md", merged)
        self.assertNotIn("AGNIR.yaml", merged)
        self.assertNotIn("Current State", merged)

    def test_existing_equivalent_locator_is_idempotent(self) -> None:
        existing = (
            "# Agent Instructions\n\n"
            "Before Project work, read the Agnir Project Instructions in README.md.\n"
        )

        self.assertEqual(merge_agents_locator(existing), existing)

    def test_explicit_conflict_fails_before_merge(self) -> None:
        existing = (
            "# Agent Instructions\n\n"
            "Do not read README.md before working on this Project.\n"
        )

        with self.assertRaisesRegex(AgentsMergeConflict, "AGNIR_INSTALL_AGENTS_CONFLICT"):
            merge_agents_locator(existing)

        self.assertEqual(
            existing,
            "# Agent Instructions\n\nDo not read README.md before working on this Project.\n",
        )


if __name__ == "__main__":
    unittest.main()
