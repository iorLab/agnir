from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from repository_filesystem_0_2_reference import discover_repository_filesystem_0_2
from repository_filesystem_reference import discover_repository_filesystem


class RepositoryFilesystemEvidenceShapeTests(unittest.TestCase):
    def _write_project(self, root: Path) -> None:
        evidence = root / ".agnir" / "evidence"
        evidence.mkdir(parents=True)
        (root / ".agnir" / "state.md").write_text("state", encoding="utf-8")
        (root / ".agnir" / "next-actions.md").write_text("next", encoding="utf-8")
        (root / ".agnir" / "decisions.md").write_text("decision", encoding="utf-8")
        (evidence / "checkpoint.md").write_text("evidence", encoding="utf-8")
        (root / "AGNIR.yaml").write_text(
            '''agnir:\n  version: "0.2"\n  discovery_profile: "repository-filesystem/0.2"\nproject:\n  identity: "urn:agnir:test:evidence-shape"\ncontinuity:\n  lineage: "urn:agnir:lineage:evidence-shape"\nmemory:\n  state: ".agnir/state.md"\n  next_actions: ".agnir/next-actions.md"\n  decisions: ".agnir/decisions.md"\n  evidence: ".agnir/evidence/"\n''',
            encoding="utf-8",
        )

    def _point_evidence_at_file(self, root: Path) -> None:
        evidence_file = root / ".agnir" / "single-evidence.md"
        evidence_file.write_text("single evidence", encoding="utf-8")
        manifest = root / "AGNIR.yaml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8").replace(
                'evidence: ".agnir/evidence/"',
                'evidence: ".agnir/single-evidence.md"',
            ),
            encoding="utf-8",
        )

    def test_0_2_non_null_local_evidence_must_resolve_to_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
            self._point_evidence_at_file(root)
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_0_1_non_null_local_evidence_must_resolve_to_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
            manifest = root / "AGNIR.yaml"
            text = manifest.read_text(encoding="utf-8")
            text = text.replace('version: "0.2"', 'version: "0.1"')
            text = text.replace(
                'discovery_profile: "repository-filesystem/0.2"',
                'discovery_profile: "repository-filesystem/0.1"',
            )
            text = text.replace(
                'continuity:\n  lineage: "urn:agnir:lineage:evidence-shape"\n',
                '',
            )
            manifest.write_text(text, encoding="utf-8")
            self._point_evidence_at_file(root)
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_0_2_baseline_evidence_discovery_is_flat(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
            nested = root / ".agnir" / "evidence" / "nested"
            nested.mkdir()
            (nested / "nested.md").write_text("nested evidence", encoding="utf-8")

            snapshot = discover_repository_filesystem_0_2(root)
            self.assertEqual(snapshot.evidence, {"checkpoint.md": "evidence"})
            self.assertNotIn("nested.md", snapshot.evidence)

    def test_0_2_evidence_child_symlink_may_target_in_root_regular_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
            source = root / ".agnir" / "evidence-source.md"
            source.write_text("linked evidence", encoding="utf-8")
            link = root / ".agnir" / "evidence" / "linked.md"
            link.symlink_to(source)

            snapshot = discover_repository_filesystem_0_2(root)
            self.assertEqual(snapshot.evidence["linked.md"], "linked evidence")

    def test_0_2_evidence_child_symlink_escape_is_unresolvable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "project"
            root.mkdir()
            self._write_project(root)
            outside = base / "outside-evidence.md"
            outside.write_text("outside evidence", encoding="utf-8")
            link = root / ".agnir" / "evidence" / "outside.md"
            link.symlink_to(outside)

            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")


if __name__ == "__main__":
    unittest.main()
