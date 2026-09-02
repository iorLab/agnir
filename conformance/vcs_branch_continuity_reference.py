from __future__ import annotations

from dataclasses import dataclass, replace


INTEGRATION_EVENTS = frozenset({"merge", "rebase", "cherry-pick"})


class VCSContinuityFailure(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


@dataclass(frozen=True)
class BranchContinuitySnapshot:
    project_identity: str
    ref: str
    revision: str
    state: str
    next_actions: str


def branch_from(base: BranchContinuitySnapshot, *, ref: str, revision: str) -> BranchContinuitySnapshot:
    """Start a branch-local continuity line from an already coherent base checkpoint."""
    if not ref or not revision:
        raise ValueError("ref and revision must be non-empty")
    return replace(base, ref=ref, revision=revision)


def checkpoint_branch(
    current: BranchContinuitySnapshot,
    *,
    revision: str,
    state: str,
    next_actions: str,
) -> BranchContinuitySnapshot:
    """Publish a checkpoint on one ref without mutating sibling branch snapshots."""
    if not revision:
        raise ValueError("revision must be non-empty")
    return replace(current, revision=revision, state=state, next_actions=next_actions)


def rewrite_revision(current: BranchContinuitySnapshot, *, revision: str) -> BranchContinuitySnapshot:
    """Model rebase/force-rewrite receipts without redefining Project identity or branch truth."""
    if not revision:
        raise ValueError("revision must be non-empty")
    return replace(current, revision=revision)


def integration_requires_reconciliation(event: str) -> bool:
    return event in INTEGRATION_EVENTS


def reconcile_integration(
    *,
    event: str,
    source: BranchContinuitySnapshot,
    target: BranchContinuitySnapshot,
    result_revision: str,
    reconciled_state: str | None,
    reconciled_next_actions: str | None,
) -> BranchContinuitySnapshot:
    """Construct target truth after a VCS integration event.

    Source continuity is an input to reconciliation, never an implicit replacement
    for target continuity. The caller must provide explicit reconciled target truth.
    """
    if event not in INTEGRATION_EVENTS:
        raise ValueError(f"unsupported integration event: {event}")
    if source.project_identity != target.project_identity:
        raise VCSContinuityFailure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "VCS integration attempted to reconcile continuity from different Projects",
        )
    if reconciled_state is None or reconciled_next_actions is None:
        raise VCSContinuityFailure(
            "AGNIR_VCS_RECONCILIATION_REQUIRED",
            f"{event} requires explicit target-branch continuity reconciliation",
        )
    if not result_revision:
        raise ValueError("result_revision must be non-empty")
    return BranchContinuitySnapshot(
        project_identity=target.project_identity,
        ref=target.ref,
        revision=result_revision,
        state=reconciled_state,
        next_actions=reconciled_next_actions,
    )


def verification_ref(*, destination_ref: str, authoritative_ref: str | None, claims_authoritative: bool) -> str:
    """Resolve the ref that must be verified after publication/push."""
    if not destination_ref:
        raise ValueError("destination_ref must be non-empty")
    if claims_authoritative:
        if not authoritative_ref:
            raise VCSContinuityFailure(
                "AGNIR_VCS_AUTHORITY_UNRESOLVED",
                "authoritative publication was claimed but no authoritative ref is declared",
            )
        if destination_ref != authoritative_ref:
            raise VCSContinuityFailure(
                "AGNIR_VCS_AUTHORITY_MISMATCH",
                "authoritative publication must target the declared authoritative ref",
            )
    return destination_ref
