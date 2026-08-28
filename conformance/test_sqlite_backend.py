from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core_reference import DiscoveryFailure
from sqlite_backend_reference import (
    SQLiteContinuityReference,
    SQLiteProjectEntryPoint,
)


PROJECT_ID = "urn:test:agnir-sqlite-project"


class SQLiteBackendConformanceTests(unittest.TestCase):
    def test_cold_start_checkpoint_and_resume_without_repository_layout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            database = root / "continuity.sqlite3"
            entry_point = SQLiteProjectEntryPoint(
                database_path=database,
                project_key="project-a",
            )

            SQLiteContinuityReference.put_project(
                entry_point,
                project_identity=PROJECT_ID,
                state="# State\ninitial durable fact\n",
                next_actions="# Next\nadvance fixture\n",
                decisions="# Decisions\nuse database-backed continuity\n",
            )
            SQLiteContinuityReference.put_evidence(
                entry_point,
                "seed",
                "seed evidence",
            )

            self.assertFalse((root / "AGNIR.yaml").exists())
            self.assertFalse((root / ".agnir").exists())

            first_resolver = SQLiteContinuityReference()
            first = first_resolver.load(
                entry_point,
                expected_project_identity=PROJECT_ID,
            )

            self.assertEqual(first.project_identity, PROJECT_ID)
            self.assertIn("initial durable fact", first.state)
            self.assertIn("advance fixture", first.next_actions)
            self.assertIn("database-backed continuity", first.decisions)
            self.assertEqual(first.evidence["seed"], "seed evidence")

            SQLiteContinuityReference.checkpoint(
                entry_point,
                state="# State\nupdated durable fact\n",
                next_actions="# Next\nresume from database\n",
                decisions="# Decisions\ncheckpoint persisted\n",
                evidence_key="checkpoint-1",
                evidence_value="database checkpoint evidence",
            )

            second_resolver = SQLiteContinuityReference()
            resumed = second_resolver.load(
                entry_point,
                expected_project_identity=PROJECT_ID,
            )

            self.assertIn("updated durable fact", resumed.state)
            self.assertIn("resume from database", resumed.next_actions)
            self.assertIn("checkpoint persisted", resumed.decisions)
            self.assertEqual(
                resumed.evidence["checkpoint-1"],
                "database checkpoint evidence",
            )

    def test_project_key_is_part_of_the_durable_entry_point(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "continuity.sqlite3"
            known = SQLiteProjectEntryPoint(database, "known")
            missing = SQLiteProjectEntryPoint(database, "missing")
            SQLiteContinuityReference.put_project(
                known,
                project_identity=PROJECT_ID,
                state="state",
                next_actions="next",
            )

            with self.assertRaises(DiscoveryFailure) as raised:
                SQLiteContinuityReference().load(missing)

            self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_NOT_FOUND")

    def test_identity_mismatch_is_preserved_without_repository_assumptions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "continuity.sqlite3"
            entry_point = SQLiteProjectEntryPoint(database, "project-a")
            SQLiteContinuityReference.put_project(
                entry_point,
                project_identity=PROJECT_ID,
                state="state",
                next_actions="next",
            )

            with self.assertRaises(DiscoveryFailure) as raised:
                SQLiteContinuityReference().load(
                    entry_point,
                    expected_project_identity="urn:test:other-project",
                )

            self.assertEqual(
                raised.exception.code,
                "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            )


if __name__ == "__main__":
    unittest.main()
