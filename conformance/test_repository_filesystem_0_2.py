from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from repository_filesystem_0_2_reference import (
    CORE_0_2_VERSION,
    PROFILE_0_2,
    discover_repository_filesystem_0_2,
)
from repository_filesystem_reference import discover_repository_filesystem


PROJECT_ID = "urn:agnir:test:repository-0.2"


def _write_project(root: Path, *, lineage: str, state: str, next_actions: str) -> None:
    (root / ".agnir" / "evidence").mkdir(parents=True)
    (root / "AGNIR.yaml").write_text(
        f'''agnir:\n  version: "0.2"\n  discovery_profile: "repository-filesystem/0.2"\n\nproject:\n  identity: "{PROJECT_ID}"\n\ncontinuity:\n  lineage: "{lineage}"\n\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n''',
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text(state, encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text(next_actions, encoding="utf-8")
    (root / ".agnir" / "decisions.md").write_text("durable decision", encoding="utf-8")
    (root / ".agnir" / "evidence" / "checkpoint.md").write_text(
        "durable evidence",
        encoding="utf-8",
    )


class RepositoryFilesystem02Tests(unittest.TestCase):
    def test_cold_start_resolves_project_and_logical_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(
                root,
                lineage="urn:agnir:lineage:primary",
                state="primary state",
                next_actions="primary next",
            )
            snapshot = discover_repository_filesystem_0_2(
                root,
                expected_project_identity=PROJECT_ID,
                expected_lineage_identity="urn:agnir:lineage:primary",
            )
            self.assertEqual(snapshot.version, CORE_0_2_VERSION)
            self.assertEqual(snapshot.profile, PROFILE_0_2)
            self.assertEqual(snapshot.project_identity, PROJECT_ID)
            self.assertEqual(snapshot.lineage_identity, "urn:agnir:lineage:primary")
            self.assertEqual(snapshot.state, "primary state")
            self.assertEqual(snapshot.next_actions, "primary next")
            self.assertEqual(snapshot.decisions, "durable decision")
            self.assertIn("checkpoint.md", snapshot.evidence)

    def test_two_selected_roots_can_share_project_identity_but_not_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root_a = base / "lineage-a"
            root_b = base / "lineage-b"
            root_a.mkdir()
            root_b.mkdir()
            _write_project(
                root_a,
                lineage="urn:agnir:lineage:a",
                state="state a",
                next_actions="next a",
            )
            _write_project(
                root_b,
                lineage="urn:agnir:lineage:b",
                state="state b",
                next_actions="next b",
            )
            a = discover_repository_filesystem_0_2(root_a)
            b = discover_repository_filesystem_0_2(root_b)
            self.assertEqual(a.project_identity, b.project_identity)
            self.assertNotEqual(a.lineage_identity, b.lineage_identity)
            self.assertNotEqual(a.state, b.state)

    def test_expected_lineage_mismatch_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(
                root,
                lineage="urn:agnir:lineage:actual",
                state="state",
                next_actions="next",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(
                    root,
                    expected_lineage_identity="urn:agnir:lineage:other",
                )
            self.assertEqual(raised.exception.code, "AGNIR_LINEAGE_NOT_FOUND")

    def test_missing_lineage_in_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".agnir").mkdir()
            (root / "AGNIR.yaml").write_text(
                f'''agnir:\n  version: "0.2"\n  discovery_profile: "repository-filesystem/0.2"\nproject:\n  identity: "{PROJECT_ID}"\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: null\n  evidence: null\n''',
                encoding="utf-8",
            )
            (root / ".agnir" / "state.md").write_text("state", encoding="utf-8")
            (root / ".agnir" / "next-actions.md").write_text("next", encoding="utf-8")
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_profile_mismatch_is_inconsistent_not_unsupported_core_version(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(
                root,
                lineage="urn:agnir:lineage:primary",
                state="state",
                next_actions="next",
            )
            manifest = (root / "AGNIR.yaml").read_text(encoding="utf-8")
            (root / "AGNIR.yaml").write_text(
                manifest.replace(
                    'discovery_profile: "repository-filesystem/0.2"',
                    'discovery_profile: "repository-filesystem/9.9"',
                ),
                encoding="utf-8",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_local_locator_escape_is_unresolvable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "project"
            root.mkdir()
            _write_project(
                root,
                lineage="urn:agnir:lineage:primary",
                state="state",
                next_actions="next",
            )
            outside = base / "outside-state.md"
            outside.write_text("outside", encoding="utf-8")
            manifest = (root / "AGNIR.yaml").read_text(encoding="utf-8")
            (root / "AGNIR.yaml").write_text(
                manifest.replace(
                    'state: ".agnir/state.md"',
                    'state: "../outside-state.md"',
                ),
                encoding="utf-8",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_stable_0_1_resolver_does_not_silently_accept_0_2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(
                root,
                lineage="urn:agnir:lineage:primary",
                state="state",
                next_actions="next",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_stable_schema_declares_core_and_profile_0_2(self) -> None:
        schema_path = Path(__file__).resolve().parents[1] / "schemas" / "agnir-manifest-0.2.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertEqual(
            schema["properties"]["agnir"]["properties"]["version"]["const"],
            "0.2",
        )
        self.assertEqual(
            schema["properties"]["agnir"]["properties"]["discovery_profile"]["const"],
            "repository-filesystem/0.2",
        )
        self.assertIn("continuity", schema["required"])
        self.assertIn("lineage", schema["properties"]["continuity"]["required"])


if __name__ == "__main__":
    unittest.main()
