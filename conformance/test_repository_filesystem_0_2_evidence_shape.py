from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from repository_filesystem_0_2_reference import discover_repository_filesystem_0_2


class RepositoryFilesystem02EvidenceShapeTests(unittest.TestCase):
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

    def test_non_null_local_evidence_must_resolve_to_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
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
            with self.assertRaises(DiscoveryFailure) as raised:
                discover_repository_filesystem_0_2(root)
            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")

    def test_baseline_evidence_discovery_is_flat(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_project(root)
            nested = root / ".agnir" / "evidence" / "nested"
            nested.mkdir()
            (nested / "nested.md").write_text("nested evidence", encoding="utf-8")

            snapshot = discover_repository_filesystem_0_2(root)
            self.assertEqual(snapshot.evidence, {"checkpoint.md": "evidence"})
            self.assertNotIn("nested.md", snapshot.evidence)


if __name__ == "__main__":
    unittest.main()
