from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from sqlite_backend_reference import SQLiteContinuityReference
from workspace_registry_reference import WorkspaceRegistryReference


ALPHA = "urn:test:agnir-alpha"
BETA = "urn:test:agnir-beta"


def write_registry(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "projects": {
                    ALPHA: {
                        "backend": "sqlite-conformance",
                        "database": "alpha.sqlite3",
                        "project_key": "alpha",
                    },
                    BETA: {
                        "backend": "sqlite-conformance",
                        "database": "beta.sqlite3",
                        "project_key": "beta",
                    },
                }
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


class WorkspaceIsolationTests(unittest.TestCase):
    def test_workspace_registry_locates_but_does_not_share_project_truth(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            registry_path = workspace / "workspace.json"
            write_registry(registry_path)

            alpha_entry = WorkspaceRegistryReference(registry_path).resolve(ALPHA).entry_point
            beta_entry = WorkspaceRegistryReference(registry_path).resolve(BETA).entry_point

            SQLiteContinuityReference.put_project(
                alpha_entry,
                project_identity=ALPHA,
                state="# State\nalpha-state\n",
                next_actions="# Next\nalpha-next\n",
                decisions="# Decisions\nalpha-decision\n",
            )
            SQLiteContinuityReference.put_evidence(alpha_entry, "alpha-seed", "alpha-evidence")
            SQLiteContinuityReference.put_project(
                beta_entry,
                project_identity=BETA,
                state="# State\nbeta-state\n",
                next_actions="# Next\nbeta-next\n",
                decisions="# Decisions\nbeta-decision\n",
            )
            SQLiteContinuityReference.put_evidence(beta_entry, "beta-seed", "beta-evidence")

            registry_before = registry_path.read_bytes()
            resolver = SQLiteContinuityReference()
            alpha_before = resolver.load(alpha_entry, expected_project_identity=ALPHA)
            beta_before = resolver.load(beta_entry, expected_project_identity=BETA)

            self.assertIn("alpha-state", alpha_before.state)
            self.assertNotIn("beta-state", alpha_before.state)
            self.assertIn("beta-state", beta_before.state)
            self.assertNotIn("alpha-state", beta_before.state)

            SQLiteContinuityReference.checkpoint(
                alpha_entry,
                state="# State\nalpha-state-updated\n",
                next_actions="# Next\nalpha-next-updated\n",
                decisions="# Decisions\nalpha-decision-updated\n",
                evidence_key="alpha-checkpoint",
                evidence_value="alpha-checkpoint-evidence",
            )

            fresh_registry = WorkspaceRegistryReference(registry_path)
            fresh_resolver = SQLiteContinuityReference()
            alpha_after = fresh_resolver.load(
                fresh_registry.resolve(ALPHA).entry_point,
                expected_project_identity=ALPHA,
            )
            beta_after = fresh_resolver.load(
                fresh_registry.resolve(BETA).entry_point,
                expected_project_identity=BETA,
            )

            self.assertIn("alpha-state-updated", alpha_after.state)
            self.assertIn("alpha-next-updated", alpha_after.next_actions)
            self.assertIn("alpha-decision-updated", alpha_after.decisions)
            self.assertEqual(
                alpha_after.evidence["alpha-checkpoint"],
                "alpha-checkpoint-evidence",
            )

            self.assertEqual(beta_after.state, beta_before.state)
            self.assertEqual(beta_after.next_actions, beta_before.next_actions)
            self.assertEqual(beta_after.decisions, beta_before.decisions)
            self.assertEqual(beta_after.evidence, beta_before.evidence)

            self.assertEqual(registry_path.read_bytes(), registry_before)

            registry_payload = json.loads(registry_path.read_text(encoding="utf-8"))
            forbidden = {"state", "next_actions", "decisions", "evidence", "memory", "continuity"}
            for entry in registry_payload["projects"].values():
                self.assertTrue(forbidden.isdisjoint(entry))
            registry_text = registry_path.read_text(encoding="utf-8")
            for continuity_text in (
                "alpha-state",
                "alpha-next",
                "alpha-decision",
                "alpha-evidence",
                "beta-state",
                "beta-next",
                "beta-decision",
                "beta-evidence",
            ):
                self.assertNotIn(continuity_text, registry_text)

    def test_registry_rejects_embedded_project_continuity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            registry_path = workspace / "workspace.json"
            registry_path.write_text(
                json.dumps(
                    {
                        "projects": {
                            ALPHA: {
                                "backend": "sqlite-conformance",
                                "database": "alpha.sqlite3",
                                "project_key": "alpha",
                                "state": "shared mutable truth must not live here",
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaises(DiscoveryFailure) as raised:
                WorkspaceRegistryReference(registry_path)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_missing_project_locator_is_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            registry_path = Path(directory) / "workspace.json"
            write_registry(registry_path)
            registry = WorkspaceRegistryReference(registry_path)

            with self.assertRaises(DiscoveryFailure) as raised:
                registry.resolve("urn:test:agnir-missing")

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_NOT_FOUND")

    def test_registry_locator_cannot_bypass_project_identity_check(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            registry_path = workspace / "workspace.json"
            write_registry(registry_path)
            alpha_entry = WorkspaceRegistryReference(registry_path).resolve(ALPHA).entry_point
            SQLiteContinuityReference.put_project(
                alpha_entry,
                project_identity=ALPHA,
                state="alpha",
                next_actions="alpha-next",
            )

            with self.assertRaises(DiscoveryFailure) as raised:
                SQLiteContinuityReference().load(
                    alpha_entry,
                    expected_project_identity=BETA,
                )

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_PROJECT_MISMATCH")


if __name__ == "__main__":
    unittest.main()
