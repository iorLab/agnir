from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from ppmp_v2_migration_reference import (
    PPMPMigrationFailure,
    load_ppmp_v2,
    materialize_agnir_target,
)
from repository_filesystem_reference import discover_repository_filesystem


FIXTURE = Path(__file__).parent / "fixtures" / "ppmp-v2"
TARGET_ID = "urn:agnir:fixture:ppmp-v2-migrated"
LEGACY_PPMP_COMMIT = "3bd3938ea00276eb51ca51c6c7ee1264d862acd4"
LEGACY_PPMP_MANIFEST = """ppmp:
  version: 2.0.0

implementation:
  name: persistent-project-memory

backend:
  name: repository

adapter:
  name: chatgpt

project:
  name: PPMP
  primary_type: generic
  profiles:
    - generic

memory:
  root: docs/project-memory
  state: PROJECT_STATE.md
  next_steps: NEXT_STEPS.md
  decisions: DECISIONS.md
  checkpoints: sessions

policy:
  checkpoint: event-driven
  session_logs: meaningful-only
  raw_transcripts: false
"""


class PPMPV2MigrationConformanceTests(unittest.TestCase):
    def test_fixture_manifest_matches_canonical_legacy_boundary(self) -> None:
        self.assertEqual(
            (FIXTURE / ".chatgpt" / "project-memory.yaml").read_text(encoding="utf-8"),
            LEGACY_PPMP_MANIFEST,
            f"fixture must stay aligned with canonical legacy/ppmp-v2.0.0 boundary {LEGACY_PPMP_COMMIT}",
        )

    def test_exact_ppmp_v2_migrates_and_cold_starts_as_agnir(self) -> None:
        source = load_ppmp_v2(FIXTURE)

        with tempfile.TemporaryDirectory() as tmp:
            target = materialize_agnir_target(source, Path(tmp) / "target", project_identity=TARGET_ID)
            snapshot = discover_repository_filesystem(target, expected_project_identity=TARGET_ID)

            self.assertIn("MATERIAL_STATE_MARKER", snapshot.state)
            self.assertIn("MATERIAL_NEXT_MARKER", snapshot.next_actions)
            self.assertIsNotNone(snapshot.decisions)
            self.assertIn("MATERIAL_DECISION_MARKER", snapshot.decisions or "")
            self.assertIn("2026-08-27.md", snapshot.evidence)
            self.assertIn("MATERIAL_EVIDENCE_MARKER", snapshot.evidence["2026-08-27.md"])
            self.assertIn("migration-ppmp-v2.md", snapshot.evidence)

            self.assertFalse((target / ".chatgpt").exists())
            target_manifest = (target / "AGNIR.yaml").read_text(encoding="utf-8")
            self.assertNotIn("adapter:", target_manifest)
            self.assertNotIn("implementation:", target_manifest)
            self.assertNotIn("backend:", target_manifest)

    def test_v1_rpm_manifest_is_not_silently_promoted_to_ppmp_v2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_root = Path(tmp) / "source"
            shutil.copytree(FIXTURE, source_root)
            manifest = source_root / ".chatgpt" / "project-memory.yaml"
            manifest.write_text(
                manifest.read_text(encoding="utf-8").replace("version: 2.0.0", "version: 1", 1),
                encoding="utf-8",
            )

            with self.assertRaises(PPMPMigrationFailure) as ctx:
                load_ppmp_v2(source_root)

            self.assertEqual(ctx.exception.code, "PPMP_MIGRATION_UNSUPPORTED_PREDECESSOR")


if __name__ == "__main__":
    unittest.main()
