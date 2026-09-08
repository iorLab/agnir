from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from activation_reference import ActivationFailure, resolve_agent_activation
from repository_filesystem_reference import discover_repository_filesystem


AGNIR_INSTRUCTIONS = """# Agnir Project Instructions

## Activation
Treat this Project root as the authorized Project Entry Point. Read `AGNIR.yaml`, then load Current State and Next Actions. Load Decisions and Evidence when relevant.

## Checkpoint
At a checkpoint or commit boundary, reconcile durable Project truth. A checkpoint evaluation may be a no-op.

## Repository operations
`commit`, `提交`, or `提交代码` means checkpoint evaluation before commit.
"""

README_SHIM = """# Example Project

## Agnir Project Instructions

Canonical Agnir activation and Project-operation instructions live in [`AGNIR.md`](AGNIR.md). This heading is retained as a backward-compatible locator for older Agnir 1.0.0 activation paths.
"""

LEGACY_README_SECTION = """# Example Project

## Agnir Project Instructions

This Project uses Agnir for durable continuity.

Before Project work, treat this Project root as the authorized Project Entry Point. Read the top-level `AGNIR.yaml`, then load Current State and Next Actions. Load Decisions and Evidence when relevant. Durable Agnir memory is authoritative over chat history or private Agent memory unless a newer Principal instruction or directly observed Project fact supersedes it.

When checkpointing, saving progress, or finishing work, reconcile material changes into the declared Agnir memory and verify the Project can cold-start again from the same Project Entry Point.
"""

AGENTS_LOCATOR = """# Agent Instructions

Before Project work, read and follow `AGNIR.md`.

This file is a locator only; AGNIR.md is canonical.
"""

LEGACY_AGENTS_LOCATOR = """# Agent Instructions

Before Project work, read and follow the **Agnir Project Instructions** section in `README.md`.

This file is a locator only; the README section is canonical.
"""

MANIFEST = """agnir:
  version: \"0.1\"
  discovery_profile: \"repository-filesystem/0.1\"
project:
  identity: \"urn:example:activation-fixture\"
memory:
  state: \".agnir/state.md\"
  next_actions: \".agnir/next-actions.md\"
  decisions: \".agnir/decisions.md\"
  evidence: \".agnir/evidence/\"
"""


class AgentActivationTests(unittest.TestCase):
    def _make_project(self, root: Path) -> None:
        (root / "README.md").write_text(README_SHIM, encoding="utf-8")
        (root / "AGENTS.md").write_text(AGENTS_LOCATOR, encoding="utf-8")
        (root / "AGNIR.md").write_text(AGNIR_INSTRUCTIONS, encoding="utf-8")
        (root / "AGNIR.yaml").write_text(MANIFEST, encoding="utf-8")
        memory = root / ".agnir"
        (memory / "evidence").mkdir(parents=True)
        (memory / "state.md").write_text("Current State: initialized\n", encoding="utf-8")
        (memory / "next-actions.md").write_text("Next Actions: continue\n", encoding="utf-8")
        (memory / "decisions.md").write_text("Decisions: use Agnir\n", encoding="utf-8")
        (memory / "evidence" / "initialization.md").write_text(
            "Evidence: activation route persisted\n", encoding="utf-8"
        )

    def test_fresh_agent_activation_then_agnir_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)

            activation = resolve_agent_activation(root)
            self.assertEqual(activation.route, "agnir-md")
            self.assertEqual(activation.instructions_path.name, "AGNIR.md")
            self.assertIn("checkpoint evaluation", activation.instructions)

            snapshot = discover_repository_filesystem(
                root,
                expected_project_identity="urn:example:activation-fixture",
            )
            self.assertIn("initialized", snapshot.state)
            self.assertIn("continue", snapshot.next_actions)

    def test_legacy_v1_0_0_readme_route_remains_activatable_for_upgrade(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGNIR.md").unlink()
            (root / "AGENTS.md").write_text(LEGACY_AGENTS_LOCATOR, encoding="utf-8")
            (root / "README.md").write_text(LEGACY_README_SECTION, encoding="utf-8")

            activation = resolve_agent_activation(root)
            self.assertEqual(activation.route, "legacy-readme")
            self.assertIn("AGNIR.yaml", activation.instructions)

    def test_missing_agents_locator_fails_activation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGENTS.md").unlink()
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_NOT_FOUND"):
                resolve_agent_activation(root)

    def test_direct_locator_requires_agnir_md(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGNIR.md").unlink()
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_NOT_FOUND"):
                resolve_agent_activation(root)

    def test_agents_must_reference_supported_activation_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGENTS.md").write_text("# Agent Instructions\nUse Agnir.\n", encoding="utf-8")
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_UNRESOLVABLE"):
                resolve_agent_activation(root)

    def test_agnir_md_activation_instructions_must_be_complete(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGNIR.md").write_text("# Agnir\nRead AGNIR.yaml.\n", encoding="utf-8")
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_INCOMPLETE"):
                resolve_agent_activation(root)

    def test_readme_compatibility_section_must_point_to_agnir_md(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "README.md").write_text(
                "# Example\n\n## Agnir Project Instructions\nAgnir is enabled.\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_UNRESOLVABLE"):
                resolve_agent_activation(root)

    def test_agents_must_not_fork_the_full_activation_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._make_project(root)
            (root / "AGENTS.md").write_text(
                "# Agent Instructions\nRead AGNIR.md.\n"
                "Load Current State, Next Actions, Decisions, Evidence and checkpoint changes.\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ActivationFailure, "AGNIR_ACTIVATION_INCONSISTENT"):
                resolve_agent_activation(root)


if __name__ == "__main__":
    unittest.main()
