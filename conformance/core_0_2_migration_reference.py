from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass

from core_0_2_reference import LineageFailure, select_lineage
from upgrade_reference import UpgradeMigrationRequired


class MigrationConflict(RuntimeError):
    code = "AGNIR_MIGRATION_CONFLICT"


@dataclass(frozen=True)
class Core01Continuity:
    project_identity: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]
    generation: int = 0


@dataclass(frozen=True)
class MigratedLineage:
    lineage_identity: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]


@dataclass(frozen=True)
class Core02MigratedProject:
    project_identity: str
    default_lineage_identity: str
    lineages: dict[str, MigratedLineage]
    source_generation: int

    def resolve(
        self,
        *,
        explicit_lineage: str | None = None,
        current_context_lineage: str | None = None,
    ) -> MigratedLineage:
        selected = select_lineage(
            explicit=explicit_lineage,
            current_context=current_context_lineage,
            default=self.default_lineage_identity,
        )
        lineage = self.lineages.get(selected)
        if lineage is None:
            raise LineageFailure(
                "AGNIR_LINEAGE_NOT_FOUND",
                f"selected migrated lineage {selected!r} does not resolve",
            )
        return lineage


def migrate_core_0_1_to_0_2(
    source: Core01Continuity | Core02MigratedProject,
    *,
    initial_lineage_identity: str,
    authorized: bool,
    expected_source_generation: int | None = None,
) -> tuple[Core02MigratedProject, bool]:
    """Migrate one implicit Core 0.1 line into one explicit Core 0.2 lineage.

    The reference is storage-neutral. It models semantic preservation and
    idempotence without choosing a repository/filesystem serialization.
    """

    selected = initial_lineage_identity.strip()
    if not selected:
        raise LineageFailure(
            "AGNIR_LINEAGE_REQUIRED",
            "Core 0.1 to 0.2 migration requires a durable initial lineage identity",
        )

    if isinstance(source, Core02MigratedProject):
        if source.default_lineage_identity != selected or selected not in source.lineages:
            raise MigrationConflict(
                f"{MigrationConflict.code}: Project is already migrated with initial lineage "
                f"{source.default_lineage_identity!r}, not {selected!r}"
            )
        return deepcopy(source), False

    if not authorized:
        raise UpgradeMigrationRequired(
            f"{UpgradeMigrationRequired.code}: Core 0.1 -> 0.2 changes the compatibility line"
        )

    if expected_source_generation is not None and source.generation != expected_source_generation:
        raise MigrationConflict(
            f"{MigrationConflict.code}: expected Core 0.1 generation "
            f"{expected_source_generation}, found {source.generation}"
        )

    lineage = MigratedLineage(
        lineage_identity=selected,
        state=source.state,
        next_actions=source.next_actions,
        decisions=source.decisions,
        evidence=deepcopy(source.evidence),
    )
    migrated = Core02MigratedProject(
        project_identity=source.project_identity,
        default_lineage_identity=selected,
        lineages={selected: lineage},
        source_generation=source.generation,
    )
    return migrated, True
