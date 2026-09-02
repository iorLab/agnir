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
class Core02VCSSelection:
    selector_ref: str
    lineage_identity: str


@dataclass(frozen=True)
class Core02VCSLineageView:
    """Backend-neutral view of one VCS-selected logical lineage."""

    project_identity: str
    lineage_identity: str
    selector_ref: str
    checkpoint_receipt: str
    state: str
    next_actions: str


def branch_as_lineage(
    snapshot: BranchContinuitySnapshot,
    *,
    lineage_identity: str,
) -> Core02VCSLineageView:
    logical_identity = lineage_identity.strip()
    if not logical_identity:
        raise VCSContinuityFailure(
            "AGNIR_LINEAGE_REQUIRED",
            "VCS selector must resolve to a non-empty logical lineage identity",
        )
    return Core02VCSLineageView(
        project_identity=snapshot.project_identity,
        lineage_identity=logical_identity,
        selector_ref=snapshot.ref,
        checkpoint_receipt=snapshot.revision,
        state=snapshot.state,
        next_actions=snapshot.next_actions,
    )


def select_vcs_lineage(
    *,
    bindings: dict[str, str],
    explicit_ref: str | None = None,
    current_context_ref: str | None = None,
    default_ref: str | None = None,
) -> Core02VCSSelection:
    """Select one VCS ref, then resolve it to one logical Core 0.2 lineage.

    The generic selection helper is used only to pressure the same precedence.
    The selected ref is a backend selector; it is not assumed to be identity.
    """

    generic_selector = select_lineage(
        explicit=explicit_ref,
        current_context=current_context_ref,
        default=default_ref,
    )
    selected_ref = select_working_ref(
        requested_ref=explicit_ref,
        current_context_ref=current_context_ref,
        default_ref=default_ref,
    )
    if selected_ref != generic_selector:
        raise AssertionError(
            f"VCS selector {selected_ref!r} diverged from Core selection precedence {generic_selector!r}"
        )
    lineage_identity = bindings.get(selected_ref)
    if lineage_identity is None or not lineage_identity.strip():
        raise VCSContinuityFailure(
            "AGNIR_LINEAGE_NOT_FOUND",
            f"selected VCS ref {selected_ref!r} has no valid logical lineage binding",
        )
    return Core02VCSSelection(
        selector_ref=selected_ref,
        lineage_identity=lineage_identity.strip(),
    )


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
    source_lineage_identity: str,
    target_lineage_identity: str,
    result_revision: str,
    reconciled_state: str | None,
    reconciled_next_actions: str | None,
) -> Core02VCSLineageView:
    if not source_lineage_identity.strip() or not target_lineage_identity.strip():
        raise VCSContinuityFailure(
            "AGNIR_LINEAGE_REQUIRED",
            "source and target VCS selectors must resolve to logical lineage identities",
        )
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
    return branch_as_lineage(
        published,
        lineage_identity=target_lineage_identity,
    )
