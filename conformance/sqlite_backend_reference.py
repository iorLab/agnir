from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from core_reference import CORE_VERSION, DiscoveryFailure, discovery_failure


@dataclass(frozen=True)
class SQLiteProjectEntryPoint:
    database_path: Path
    project_key: str


@dataclass(frozen=True)
class SQLiteContinuitySnapshot:
    project_identity: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]


class SQLiteContinuityReference:
    """Conformance-only durable backend demonstrating non-repository Agnir Core use.

    This is not a normative Agnir profile or production implementation. The
    Project Entry Point is a database locator plus durable project key; no
    `AGNIR.yaml`, repository root, or `.agnir/` layout participates in discovery.
    """

    @staticmethod
    def initialize_database(path: Path) -> None:
        with sqlite3.connect(path) as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS projects (
                    project_key TEXT PRIMARY KEY,
                    agnir_version TEXT NOT NULL,
                    project_identity TEXT NOT NULL,
                    state_key TEXT NOT NULL,
                    next_actions_key TEXT NOT NULL,
                    decisions_key TEXT
                );

                CREATE TABLE IF NOT EXISTS memory (
                    project_key TEXT NOT NULL,
                    memory_key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    PRIMARY KEY (project_key, memory_key)
                );

                CREATE TABLE IF NOT EXISTS evidence (
                    project_key TEXT NOT NULL,
                    evidence_key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    PRIMARY KEY (project_key, evidence_key)
                );
                """
            )

    @staticmethod
    def put_project(
        entry_point: SQLiteProjectEntryPoint,
        *,
        project_identity: str,
        state: str,
        next_actions: str,
        decisions: str | None = None,
        version: str = CORE_VERSION,
    ) -> None:
        SQLiteContinuityReference.initialize_database(entry_point.database_path)
        state_key = "state"
        next_key = "next-actions"
        decisions_key = "decisions" if decisions is not None else None
        with sqlite3.connect(entry_point.database_path) as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO projects (
                    project_key, agnir_version, project_identity,
                    state_key, next_actions_key, decisions_key
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    entry_point.project_key,
                    version,
                    project_identity,
                    state_key,
                    next_key,
                    decisions_key,
                ),
            )
            connection.execute(
                "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, state_key, state),
            )
            connection.execute(
                "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, next_key, next_actions),
            )
            if decisions_key is not None:
                connection.execute(
                    "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                    (entry_point.project_key, decisions_key, decisions),
                )

    @staticmethod
    def put_evidence(
        entry_point: SQLiteProjectEntryPoint,
        key: str,
        value: str,
    ) -> None:
        with sqlite3.connect(entry_point.database_path) as connection:
            connection.execute(
                "INSERT OR REPLACE INTO evidence(project_key, evidence_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, key, value),
            )

    @staticmethod
    def _load_memory(
        connection: sqlite3.Connection,
        *,
        project_key: str,
        memory_key: str | None,
        required: bool,
        label: str,
    ) -> str | None:
        if memory_key is None:
            if required:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    f"required {label} locator is null",
                )
            return None
        row = connection.execute(
            "SELECT value FROM memory WHERE project_key = ? AND memory_key = ?",
            (project_key, memory_key),
        ).fetchone()
        if row is None:
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"{label} locator {memory_key!r} does not resolve",
            )
        return str(row[0])

    def load(
        self,
        entry_point: SQLiteProjectEntryPoint,
        *,
        expected_project_identity: str | None = None,
    ) -> SQLiteContinuitySnapshot:
        if not entry_point.database_path.is_file():
            raise discovery_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "SQLite Project Entry Point database does not exist",
            )

        with sqlite3.connect(entry_point.database_path) as connection:
            row = connection.execute(
                """
                SELECT agnir_version, project_identity, state_key,
                       next_actions_key, decisions_key
                FROM projects
                WHERE project_key = ?
                """,
                (entry_point.project_key,),
            ).fetchone()
            if row is None:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_NOT_FOUND",
                    "SQLite Project Entry Point project key has no Discovery Record",
                )

            version, project_identity, state_key, next_key, decisions_key = row
            if version != CORE_VERSION:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                    f"expected Agnir Core {CORE_VERSION}, discovered {version!r}",
                )
            if expected_project_identity is not None and project_identity != expected_project_identity:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                    f"expected {expected_project_identity!r}, discovered {project_identity!r}",
                )

            state = self._load_memory(
                connection,
                project_key=entry_point.project_key,
                memory_key=state_key,
                required=True,
                label="Current State",
            )
            next_actions = self._load_memory(
                connection,
                project_key=entry_point.project_key,
                memory_key=next_key,
                required=True,
                label="Next Actions",
            )
            decisions = self._load_memory(
                connection,
                project_key=entry_point.project_key,
                memory_key=decisions_key,
                required=False,
                label="Decisions",
            )
            evidence = {
                key: value
                for key, value in connection.execute(
                    "SELECT evidence_key, value FROM evidence WHERE project_key = ? ORDER BY evidence_key",
                    (entry_point.project_key,),
                ).fetchall()
            }

        return SQLiteContinuitySnapshot(
            project_identity=str(project_identity),
            state=state,
            next_actions=next_actions,
            decisions=decisions,
            evidence=evidence,
        )

    @staticmethod
    def checkpoint(
        entry_point: SQLiteProjectEntryPoint,
        *,
        state: str,
        next_actions: str,
        decisions: str | None,
        evidence_key: str,
        evidence_value: str,
    ) -> None:
        with sqlite3.connect(entry_point.database_path) as connection:
            row = connection.execute(
                "SELECT state_key, next_actions_key, decisions_key FROM projects WHERE project_key = ?",
                (entry_point.project_key,),
            ).fetchone()
            if row is None:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_NOT_FOUND",
                    "cannot checkpoint because the SQLite Discovery Record is missing",
                )
            state_key, next_key, decisions_key = row
            connection.execute(
                "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, state_key, state),
            )
            connection.execute(
                "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, next_key, next_actions),
            )
            if decisions is not None:
                if decisions_key is None:
                    decisions_key = "decisions"
                    connection.execute(
                        "UPDATE projects SET decisions_key = ? WHERE project_key = ?",
                        (decisions_key, entry_point.project_key),
                    )
                connection.execute(
                    "INSERT OR REPLACE INTO memory(project_key, memory_key, value) VALUES (?, ?, ?)",
                    (entry_point.project_key, decisions_key, decisions),
                )
            connection.execute(
                "INSERT OR REPLACE INTO evidence(project_key, evidence_key, value) VALUES (?, ?, ?)",
                (entry_point.project_key, evidence_key, evidence_value),
            )
