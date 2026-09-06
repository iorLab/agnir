from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from repository_filesystem_0_2_reference import discover_repository_filesystem_0_2
from repository_filesystem_1_0_reference import (
    CORE_1_0_VERSION,
    PROFILE_1_0,
    discover_repository_filesystem_1_0,
)


PROJECT_ID = "urn:agnir:test:repository-1.0"
LINEAGE_ID = "urn:agnir:lineage:stable-primary"


def _write_project(root: Path) -> None:
    (root / ".agnir" / "evidence" / "nested").mkdir(parents=True)
    (root / "AGNIR.yaml").write_text(
        f'''agnir:\n  version: "1.0"\n  discovery_profile: "repository-filesystem/1.0"\n\nproject:\n  identity: "{PROJECT_ID}"\n  profiles:\n    - generic\n\ncontinuity:\n  lineage: "{LINEAGE_ID}"\n\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n\npolicy:\n  checkpoint: event-driven\n\nextensions:\n  example/custom:\n    preserved: true\n''',
        encoding="utf-8",
    )
    (root / ".agnir" / "state.md").write_text("stable state\n", encoding="utf-8")
    (root / ".agnir" / "next-actions.md").write_text("stable next\n", encoding="utf-8")
    (root / ".agnir" / "decisions.md").write_text("stable decision\n", encoding="utf-8")
    (root / ".agnir" / "evidence" / "checkpoint.md").write_text("stable evidence\n", encoding="utf-8")
    (root / ".agnir" / "evidence" / "nested" / "ignored.md").write_text("nested\n", encoding="utf-8")


class RepositoryFilesystem10Tests(unittest.TestCase):
    def test_fresh_1_0_cold_start_and_flat_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            snapshot = discover_repository_filesystem_1_0(
                root,
                expected_project_identity=PROJECT_ID,
                expected_lineage_identity=LINEAGE_ID,
            )
            self.assertEqual(snapshot.version, CORE_1_0_VERSION)
            self.assertEqual(snapshot.profile, PROFILE_1_0)
            self.assertEqual(snapshot.project_identity, PROJECT_ID)
            self.assertEqual(snapshot.lineage_identity, LINEAGE_ID)
            self.assertEqual(snapshot.state, "stable state\n")
            self.assertEqual(snapshot.next_actions, "stable next\n")
            self.assertEqual(snapshot.decisions, "stable decision\n")
            self.assertEqual(snapshot.evidence, {"checkpoint.md": "stable evidence\n"})

    def test_schema_invalid_extra_field_is_inconsistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            manifest = root / "AGNIR.yaml"
            manifest.write_text(manifest.read_text(encoding="utf-8") + "\nforbidden: true\n", encoding="utf-8")
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_1_0(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_missing_null_and_wrong_type_version_are_inconsistent(self) -> None:
        mutations = (
            ('  version: "1.0"\n', ""),
            ('version: "1.0"', "version: null"),
            ('  version: "1.0"', '  version:\n    - "1.0"'),
        )
        for old, new in mutations:
            with self.subTest(new=new), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                _write_project(root)
                manifest = root / "AGNIR.yaml"
                manifest.write_text(manifest.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
                with self.assertRaises(DiscoveryFailure) as raised:
                    discover_repository_filesystem_1_0(root)
                self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_declared_other_core_version_is_unsupported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            manifest = root / "AGNIR.yaml"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace('version: "1.0"', 'version: "0.2"'),
                encoding="utf-8",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_1_0(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_profile_mismatch_is_inconsistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            manifest = root / "AGNIR.yaml"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    'discovery_profile: "repository-filesystem/1.0"',
                    'discovery_profile: "repository-filesystem/9.9"',
                ),
                encoding="utf-8",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_1_0(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_INCONSISTENT")

    def test_wrong_evidence_target_shape_is_unresolvable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            (root / ".agnir" / "evidence-file.md").write_text("not a collection\n", encoding="utf-8")
            manifest = root / "AGNIR.yaml"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace(
                    'evidence: ".agnir/evidence/"',
                    'evidence: ".agnir/evidence-file.md"',
                ),
                encoding="utf-8",
            )
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_1_0(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_0_2_and_1_0_resolvers_do_not_silently_cross_accept(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_project(root)
            with self.assertRaises(DiscoveryFailure) as raised_02:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised_02.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

            manifest = root / "AGNIR.yaml"
            manifest.write_text(
                manifest.read_text(encoding="utf-8")
                .replace('version: "1.0"', 'version: "0.2"')
                .replace('discovery_profile: "repository-filesystem/1.0"', 'discovery_profile: "repository-filesystem/0.2"'),
                encoding="utf-8",
            )
            snapshot_02 = discover_repository_filesystem_0_2(root)
            self.assertEqual(snapshot_02.version, "0.2")
            with self.assertRaises(DiscoveryFailure) as raised_10:
                discover_repository_filesystem_1_0(root)
            self.assertEqual(raised_10.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")


if __name__ == "__main__":
    unittest.main()
