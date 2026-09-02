from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from core_0_2_reference import (
    CORE_0_2_VERSION,
    ContinuityLineageSnapshot,
    IntegrationCandidate,
    lineage_failure,
    make_integration_candidate,
    require_reconciliation,
    select_lineage,
    validate_project_identity,
)


@dataclass(frozen=True)
class SQLiteLineageEntryPoint:
    database_path: Path
    project_key: str


class SQLiteLineageReference:
    """Non-VCS Core 0.2 conformance backend.

    The backend intentionally has no repository, branch, ref, worktree, commit,
    or VCS merge concept. Lineages are logical namespaces persisted in SQLite,
    and publication uses SQLite transactions/generations.
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
                    default_lineage_identity TEXT
                );

                CREATE TABLE IF NOT EXISTS lineages (
                    project_key TEXT NOT NULL,
                    lineage_identity TEXT NOT NULL,
                    project_state TEXT NOT NULL,
                    state TEXT NOT NULL,
                    next_actions TEXT NOT NULL,
                    decisions TEXT,
                    generation INTEGER NOT NULL,
                    PRIMARY KEY (project_key, lineage_identity)
                );

                CREATE TABLE IF NOT EXISTS lineage_evidence (
                    project_key TEXT NOT NULL,
                    lineage_identity TEXT NOT NULL,
                    evidence_key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    PRIMARY KEY (project_key, lineage_identity, evidence_key)
                );
                """
            )

    @classmethod
    def create_project(
        cls,
        entry_point: SQLiteLineageEntryPoint,
        *,
        project_identity: str,
        initial_lineage_identity: str,
        project_state: str,
        state: str,
        next_actions: str,
        decisions: str | None = None,
        default_lineage_identity: str | None = None,
        version: str = CORE_0_2_VERSION,
    ) -> None:
        cls.initialize_database(entry_point.database_path)
        with sqlite3.connect(entry_point.database_path) as connection:
            connection.execute(
                """
                INSERT INTO projects(
                    project_key, agnir_version, project_identity, default_lineage_identity
                ) VALUES (?, ?, ?, ?)
                """,
                (
                    entry_point.project_key,
                    version,
                    project_identity,
                    default_lineage_identity,
                ),
            )
            connection.execute(
                """
                INSERT INTO lineages(
                    project_key, lineage_identity, project_state,
                    state, next_actions, decisions, generation
                ) VALUES (?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    entry_point.project_key,
                    initial_lineage_identity,
                    project_state,
                    state,
                    next_actions,
                    decisions,
                ),
            )

    @staticmethod
    def _project_row(
        connection: sqlite3.Connection,
        entry_point: SQLiteLineageEntryPoint,
    ) -> tuple[str, str, str | None]:
        row = connection.execute(
            """
            SELECT agnir_version, project_identity, default_lineage_identity
            FROM projects WHERE project_key = ?
            """,
            (entry_point.project_key,),
        ).fetchone()
        if row is None:
            raise lineage_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "SQLite Project Entry Point has no Core 0.2 Discovery Record",
            )
        version, project_identity, default_lineage_identity = row
        if version != CORE_0_2_VERSION:
            raise lineage_failure(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                f"expected Agnir Core {CORE_0_2_VERSION}, discovered {version!r}",
            )
        return str(version), str(project_identity), (
            str(default_lineage_identity) if default_lineage_identity is not None else None
        )

    @staticmethod
    def _snapshot(
        connection: sqlite3.Connection,
        entry_point: SQLiteLineageEntryPoint,
        *,
        lineage_identity: str,
        project_identity: str,
    ) -> ContinuityLineageSnapshot:
        row = connection.execute(
            """
            SELECT project_state, state, next_actions, decisions, generation
            FROM lineages
            WHERE project_key = ? AND lineage_identity = ?
            """,
            (entry_point.project_key, lineage_identity),
        ).fetchone()
        if row is None:
            raise lineage_failure(
                "AGNIR_LINEAGE_NOT_FOUND",
                f"selected lineage {lineage_identity!r} does not resolve",
            )
        project_state, state, next_actions, decisions, generation = row
        evidence = {
            str(key): str(value)
            for key, value in connection.execute(
                """
                SELECT evidence_key, value FROM lineage_evidence
                WHERE project_key = ? AND lineage_identity = ?
                ORDER BY evidence_key
                """,
                (entry_point.project_key, lineage_identity),
            ).fetchall()
        }
        return ContinuityLineageSnapshot(
            project_identity=project_identity,
            lineage_identity=lineage_identity,
            project_state=str(project_state),
            state=str(state),
            next_actions=str(next_actions),
            decisions=str(decisions) if decisions is not None else None,
            evidence=evidence,
            generation=int(generation),
        )

    def load(
        self,
        entry_point: SQLiteLineageEntryPoint,
        *,
        explicit_lineage: str | None = None,
        current_context_lineage: str | None = None,
        expected_project_identity: str | None = None,
    ) -> ContinuityLineageSnapshot:
        if not entry_point.database_path.is_file():
            raise lineage_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "SQLite Project Entry Point database does not exist",
            )
        with sqlite3.connect(entry_point.database_path) as connection:
            _, project_identity, default_lineage = self._project_row(connection, entry_point)
            if (
                expected_project_identity is not None
                and project_identity != expected_project_identity
            ):
                raise lineage_failure(
                    "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                    f"expected {expected_project_identity!r}, discovered {project_identity!r}",
                )
            lineage_identity = select_lineage(
                explicit=explicit_lineage,
                current_context=current_context_lineage,
                default=default_lineage,
            )
            return self._snapshot(
                connection,
                entry_point,
                lineage_identity=lineage_identity,
                project_identity=project_identity,
            )

    def fork_lineage(
        self,
        entry_point: SQLiteLineageEntryPoint,
        *,
        source_lineage: str,
        new_lineage: str,
    ) -> ContinuityLineageSnapshot:
        with sqlite3.connect(entry_point.database_path) as connection:
            _, project_identity, _ = self._project_row(connection, entry_point)
            source = self._snapshot(
                connection,
                entry_point,
                lineage_identity=source_lineage,
                project_identity=project_identity,
            )
            try:
                connection.execute(
                    """
                    INSERT INTO lineages(
                        project_key, lineage_identity, project_state,
                        state, next_actions, decisions, generation
                    ) VALUES (?, ?, ?, ?, ?, ?, 0)
                    """,
                    (
                        entry_point.project_key,
                        new_lineage,
                        source.project_state,
                        source.state,
                        source.next_actions,
                        source.decisions,
                    ),
                )
            except sqlite3.IntegrityError as exc:
                raise lineage_failure(
                    "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
                    f"lineage {new_lineage!r} already exists",
                ) from exc
            for key, value in source.evidence.items():
                connection.execute(
                    """
                    INSERT INTO lineage_evidence(
                        project_key, lineage_identity, evidence_key, value
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (entry_point.project_key, new_lineage, key, value),
                )
        return self.load(entry_point, explicit_lineage=new_lineage)

    def checkpoint(
        self,
        entry_point: SQLiteLineageEntryPoint,
        *,
        lineage_identity: str,
        project_state: str,
        state: str,
        next_actions: str,
        decisions: str | None,
        evidence_key: str | None = None,
        evidence_value: str | None = None,
        expected_generation: int | None = None,
    ) -> ContinuityLineageSnapshot:
        with sqlite3.connect(entry_point.database_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            _, project_identity, _ = self._project_row(connection, entry_point)
            current = self._snapshot(
                connection,
                entry_point,
                lineage_identity=lineage_identity,
                project_identity=project_identity,
            )
            if expected_generation is not None and current.generation != expected_generation:
                raise lineage_failure(
                    "AGNIR_CHECKPOINT_CONFLICT",
                    f"expected generation {expected_generation}, found {current.generation}",
                )
            connection.execute(
                """
                UPDATE lineages
                SET project_state = ?, state = ?, next_actions = ?, decisions = ?,
                    generation = generation + 1
                WHERE project_key = ? AND lineage_identity = ?
                """,
                (
                    project_state,
                    state,
                    next_actions,
                    decisions,
                    entry_point.project_key,
                    lineage_identity,
                ),
            )
            if evidence_key is not None:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO lineage_evidence(
                        project_key, lineage_identity, evidence_key, value
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (
                        entry_point.project_key,
                        lineage_identity,
                        evidence_key,
                        evidence_value or "",
                    ),
                )
        return self.load(entry_point, explicit_lineage=lineage_identity)

    def stage_integration(
        self,
        *,
        target_entry_point: SQLiteLineageEntryPoint,
        target_lineage: str,
        source_entry_point: SQLiteLineageEntryPoint,
        source_lineage: str,
        resulting_project_state: str,
    ) -> IntegrationCandidate:
        target = self.load(target_entry_point, explicit_lineage=target_lineage)
        source = self.load(source_entry_point, explicit_lineage=source_lineage)
        validate_project_identity(target.project_identity, source.project_identity)
        return make_integration_candidate(
            target=target,
            sources=(source,),
            resulting_project_state=resulting_project_state,
        )

    def publish_integration(
        self,
        *,
        target_entry_point: SQLiteLineageEntryPoint,
        source_entry_point: SQLiteLineageEntryPoint,
        candidate: IntegrationCandidate,
        reconciled: bool,
        state: str,
        next_actions: str,
        decisions: str | None,
        evidence_key: str,
        evidence_value: str,
    ) -> ContinuityLineageSnapshot:
        require_reconciliation(reconciled=reconciled)
        if len(candidate.source_lineage_identities) != 1:
            raise lineage_failure(
                "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
                "SQLite reference publishes one source lineage per integration fixture",
            )
        source_lineage = candidate.source_lineage_identities[0]
        expected_source_generation = dict(candidate.source_generations)[source_lineage]

        if target_entry_point.database_path != source_entry_point.database_path:
            # Cross-database cases can be read for identity validation, but this
            # reference backend cannot atomically publish them as one transaction.
            target = self.load(
                target_entry_point,
                explicit_lineage=candidate.target_lineage_identity,
            )
            source = self.load(source_entry_point, explicit_lineage=source_lineage)
            validate_project_identity(target.project_identity, source.project_identity)
            raise lineage_failure(
                "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
                "reference backend cannot atomically publish across SQLite databases",
            )

        with sqlite3.connect(target_entry_point.database_path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            _, target_project_identity, _ = self._project_row(connection, target_entry_point)
            _, source_project_identity, _ = self._project_row(connection, source_entry_point)
            validate_project_identity(
                candidate.project_identity,
                target_project_identity,
                source_project_identity,
            )
            target = self._snapshot(
                connection,
                target_entry_point,
                lineage_identity=candidate.target_lineage_identity,
                project_identity=target_project_identity,
            )
            source = self._snapshot(
                connection,
                source_entry_point,
                lineage_identity=source_lineage,
                project_identity=source_project_identity,
            )
            if target.generation != candidate.target_generation:
                raise lineage_failure(
                    "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
                    "target lineage advanced after the integration candidate was staged",
                )
            if source.generation != expected_source_generation:
                raise lineage_failure(
                    "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
                    "source lineage advanced after the integration candidate was staged",
                )
            connection.execute(
                """
                UPDATE lineages
                SET project_state = ?, state = ?, next_actions = ?, decisions = ?,
                    generation = generation + 1
                WHERE project_key = ? AND lineage_identity = ?
                """,
                (
                    candidate.resulting_project_state,
                    state,
                    next_actions,
                    decisions,
                    target_entry_point.project_key,
                    candidate.target_lineage_identity,
                ),
            )
            connection.execute(
                """
                INSERT OR REPLACE INTO lineage_evidence(
                    project_key, lineage_identity, evidence_key, value
                ) VALUES (?, ?, ?, ?)
                """,
                (
                    target_entry_point.project_key,
                    candidate.target_lineage_identity,
                    evidence_key,
                    evidence_value,
                ),
            )
        return self.load(
            target_entry_point,
            explicit_lineage=candidate.target_lineage_identity,
        )
