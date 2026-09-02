from __future__ import annotations

from dataclasses import dataclass

from core_0_2_reference import select_lineage
from vcs_branch_continuity_reference import (
    BranchContinuitySnapshot,
    VCSContinuityFailure,
    publish_staged_integration,
    select_working_ref,
    stage_integration_candidate,
)


@dataclass(frozen=True)
class Core02VCSLineageView:
    """Backend-neutral view of one VCS branch continuity snapshot."""

    project_identity: str
    lineage_identity: str
    checkpoint_receipt: str
    state: str
    next_actions: str


def branch_as_lineage(snapshot: BranchContinuitySnapshot) -> Core02VCSLineageView:
    return Core02VCSLineageView(
        project_identity=snapshot.project_identity,
        lineage_identity=snapshot.ref,
        checkpoint_receipt=snapshot.revision,
        state=snapshot.state,
        next_actions=snapshot.next_actions,
    )


def select_vcs_lineage(
    *,
    explicit: str | None = None,
    current_context: str | None = None,
    default: str | None = None,
) -> str:
    """Assert that VCS ref selection implements the generic Core 0.2 precedence."""

    generic = select_lineage(
        explicit=explicit,
        current_context=current_context,
        default=default,
    )
    vcs = select_working_ref(
        requested_ref=explicit,
        current_context_ref=current_context,
        default_ref=default,
    )
    if vcs != generic:
        raise AssertionError(f"VCS selection {vcs!r} diverged from Core lineage selection {generic!r}")
    return vcs


def core_failure_code_for_vcs(code: str) -> str:
    """Map backend-specific VCS failures to Core 0.2 semantic conditions."""

    mapping = {
        "AGNIR_VCS_REF_REQUIRED": "AGNIR_LINEAGE_REQUIRED",
        "AGNIR_VCS_RECONCILIATION_REQUIRED": "AGNIR_LINEAGE_RECONCILIATION_REQUIRED",
        "AGNIR_VCS_INTEGRATION_CONFLICT": "AGNIR_LINEAGE_INTEGRATION_CONFLICT",
        "AGNIR_DISCOVERY_PROJECT_MISMATCH": "AGNIR_DISCOVERY_PROJECT_MISMATCH",
    }
    return mapping.get(code, code)


def stage_and_publish_vcs_lineage_integration(
    *,
    event: str,
    staged_source: BranchContinuitySnapshot,
    staged_target: BranchContinuitySnapshot,
    current_source: BranchContinuitySnapshot,
    current_target: BranchContinuitySnapshot,
    result_revision: str,
    reconciled_state: str | None,
    reconciled_next_actions: str | None,
) -> Core02VCSLineageView:
    candidate = stage_integration_candidate(
        event=event,
        source=staged_source,
        target=staged_target,
        result_revision=result_revision,
    )
    try:
        published = publish_staged_integration(
            candidate=candidate,
            current_source=current_source,
            current_target=current_target,
            reconciled_state=reconciled_state,
            reconciled_next_actions=reconciled_next_actions,
        )
    except VCSContinuityFailure as exc:
        raise VCSContinuityFailure(core_failure_code_for_vcs(exc.code), str(exc)) from exc
    return branch_as_lineage(published)
