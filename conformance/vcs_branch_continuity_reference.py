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


@dataclass(frozen=True)
class VCSIntegrationCandidate:
    """Staged VCS integration receipt before target-ref publication."""

    event: str
    project_identity: str
    source_ref: str
    source_revision: str
    target_ref: str
    target_revision: str
    result_revision: str


def select_working_ref(
    *,
    requested_ref: str | None = None,
    current_context_ref: str | None = None,
    default_ref: str | None = None,
) -> str:
    """Select one VCS working ref without guessing among sibling branches.

    Explicit task/adapter scope wins, then an already selected checkout/worktree ref,
    then an explicitly declared default. The helper never searches branch names.
    """
    for candidate in (requested_ref, current_context_ref, default_ref):
        if candidate:
            return candidate
    raise VCSContinuityFailure(
        "AGNIR_VCS_REF_REQUIRED",
        "branch-local continuity requires an explicit selected ref/worktree or declared default ref",
    )


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


def stage_integration_candidate(
    *,
    event: str,
    source: BranchContinuitySnapshot,
    target: BranchContinuitySnapshot,
    result_revision: str,
) -> VCSIntegrationCandidate:
    """Capture optimistic source/target receipts without advancing the target ref."""

    if event not in INTEGRATION_EVENTS:
        raise ValueError(f"unsupported integration event: {event}")
    if source.project_identity != target.project_identity:
        raise VCSContinuityFailure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "VCS integration attempted to stage continuity from different Projects",
        )
    if not result_revision:
        raise ValueError("result_revision must be non-empty")
    return VCSIntegrationCandidate(
        event=event,
        project_identity=target.project_identity,
        source_ref=source.ref,
        source_revision=source.revision,
        target_ref=target.ref,
        target_revision=target.revision,
        result_revision=result_revision,
    )


def reconcile_integration(
    *,
    event: str,
    source: BranchContinuitySnapshot,
    target: BranchContinuitySnapshot,
    result_revision: str,
    reconciled_state: str | None,
    reconciled_next_actions: str | None,
) -> BranchContinuitySnapshot:
    """Construct target truth for a staged VCS integration candidate.

    Source continuity is an input to reconciliation, never an implicit replacement
    for target continuity. The caller must provide explicit reconciled target truth
    before the target ref is advanced to ``result_revision``.
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
            f"{event} requires explicit target-branch continuity reconciliation before target publication",
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


def publish_staged_integration(
    *,
    candidate: VCSIntegrationCandidate,
    current_source: BranchContinuitySnapshot,
    current_target: BranchContinuitySnapshot,
    reconciled_state: str | None,
    reconciled_next_actions: str | None,
) -> BranchContinuitySnapshot:
    """Validate staged receipts, then construct publishable target continuity.

    This helper models the VCS adapter/profile boundary. It does not move a ref;
    the caller may advance the target only after this returns reconciled truth.
    """

    if current_source.project_identity != candidate.project_identity or current_target.project_identity != candidate.project_identity:
        raise VCSContinuityFailure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            "staged VCS integration inputs no longer resolve to the staged Project",
        )
    if current_target.ref != candidate.target_ref or current_source.ref != candidate.source_ref:
        raise VCSContinuityFailure(
            "AGNIR_VCS_INTEGRATION_CONFLICT",
            "staged integration source/target logical refs changed before publication",
        )
    if current_target.revision != candidate.target_revision:
        raise VCSContinuityFailure(
            "AGNIR_VCS_INTEGRATION_CONFLICT",
            "target ref advanced after the integration candidate was staged",
        )
    if current_source.revision != candidate.source_revision:
        raise VCSContinuityFailure(
            "AGNIR_VCS_INTEGRATION_CONFLICT",
            "source ref advanced after the integration candidate was staged",
        )
    return reconcile_integration(
        event=candidate.event,
        source=current_source,
        target=current_target,
        result_revision=candidate.result_revision,
        reconciled_state=reconciled_state,
        reconciled_next_actions=reconciled_next_actions,
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
