from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


CORE_0_2_VERSION = "0.2"


class LineageFailure(RuntimeError):
    """Conformance-only carrier for Core 0.2 lineage semantic failures."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def lineage_failure(code: str, message: str) -> LineageFailure:
    return LineageFailure(code, message)


def _non_empty(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return value or None


def select_lineage(
    *,
    explicit: str | None = None,
    current_context: str | None = None,
    default: str | None = None,
) -> str:
    """Resolve one lineage without sibling enumeration or heuristic guessing."""

    for candidate in (explicit, current_context, default):
        selected = _non_empty(candidate)
        if selected is not None:
            return selected
    raise lineage_failure(
        "AGNIR_LINEAGE_REQUIRED",
        "lineage-local work requires an explicit, contextual, or declared-default lineage",
    )


def validate_project_identity(*identities: str) -> str:
    normalized = {_non_empty(identity) for identity in identities}
    if None in normalized:
        raise lineage_failure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "Project identity must be non-empty across integration inputs",
        )
    if len(normalized) != 1:
        raise lineage_failure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            f"integration inputs belong to different Projects: {sorted(normalized)!r}",
        )
    return next(iter(normalized))  # type: ignore[arg-type]


def require_reconciliation(*, reconciled: bool) -> None:
    if not reconciled:
        raise lineage_failure(
            "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
            "target continuity must be reconciled before integration publication",
        )


@dataclass(frozen=True)
class ContinuityLineageSnapshot:
    project_identity: str
    lineage_identity: str
    project_state: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]
    generation: int

    @property
    def receipt(self) -> str:
        """Backend-like checkpoint receipt deliberately distinct from lineage identity."""

        return f"generation:{self.generation}"


@dataclass(frozen=True)
class IntegrationCandidate:
    project_identity: str
    target_lineage_identity: str
    source_lineage_identities: tuple[str, ...]
    target_generation: int
    source_generations: tuple[tuple[str, int], ...]
    resulting_project_state: str


def make_integration_candidate(
    *,
    target: ContinuityLineageSnapshot,
    sources: Iterable[ContinuityLineageSnapshot],
    resulting_project_state: str,
) -> IntegrationCandidate:
    source_list = tuple(sources)
    validate_project_identity(
        target.project_identity,
        *(source.project_identity for source in source_list),
    )
    if not source_list:
        raise lineage_failure(
            "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
            "lineage integration requires at least one source continuity input",
        )
    return IntegrationCandidate(
        project_identity=target.project_identity,
        target_lineage_identity=target.lineage_identity,
        source_lineage_identities=tuple(source.lineage_identity for source in source_list),
        target_generation=target.generation,
        source_generations=tuple(
            (source.lineage_identity, source.generation) for source in source_list
        ),
        resulting_project_state=resulting_project_state,
    )
