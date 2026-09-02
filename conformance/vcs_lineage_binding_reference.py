from __future__ import annotations

from dataclasses import dataclass

from vcs_branch_continuity_reference import BranchContinuitySnapshot, VCSContinuityFailure


@dataclass(frozen=True)
class VCSLineageBinding:
    project_identity: str
    lineage_identity: str
    selector_ref: str
    checkpoint_receipt: str
    state: str
    next_actions: str


def bind_snapshot(
    snapshot: BranchContinuitySnapshot,
    *,
    lineage_identity: str,
) -> VCSLineageBinding:
    logical = lineage_identity.strip()
    if not logical:
        raise VCSContinuityFailure(
            "AGNIR_VCS_LINEAGE_BINDING_REQUIRED",
            "selected VCS ref has no logical lineage identity to bind",
        )
    return VCSLineageBinding(
        project_identity=snapshot.project_identity,
        lineage_identity=logical,
        selector_ref=snapshot.ref,
        checkpoint_receipt=snapshot.revision,
        state=snapshot.state,
        next_actions=snapshot.next_actions,
    )


def validate_selected_binding(
    binding: VCSLineageBinding | None,
    *,
    selected_ref: str,
) -> VCSLineageBinding:
    if binding is None:
        raise VCSContinuityFailure(
            "AGNIR_VCS_LINEAGE_BINDING_REQUIRED",
            f"selected ref {selected_ref!r} has no durable lineage binding",
        )
    if binding.selector_ref != selected_ref:
        raise VCSContinuityFailure(
            "AGNIR_VCS_LINEAGE_BINDING_MISMATCH",
            f"selected ref {selected_ref!r} conflicts with persisted binding {binding.selector_ref!r}",
        )
    return binding


def fork_lineage_binding(
    source: VCSLineageBinding,
    *,
    new_ref: str,
    new_lineage_identity: str,
    new_revision: str,
) -> VCSLineageBinding:
    """Establish an independent logical lineage from an inherited branch baseline."""

    logical = new_lineage_identity.strip()
    if not new_ref or not new_revision or not logical:
        raise ValueError("new_ref, new_lineage_identity, and new_revision must be non-empty")
    if new_ref == source.selector_ref:
        raise VCSContinuityFailure(
            "AGNIR_VCS_LINEAGE_BINDING_MISMATCH",
            "lineage fork requires a distinct backend selector from the source binding",
        )
    if logical == source.lineage_identity:
        raise VCSContinuityFailure(
            "AGNIR_VCS_LINEAGE_BINDING_MISMATCH",
            "independent branch lineage fork must establish a new logical lineage identity",
        )
    return VCSLineageBinding(
        project_identity=source.project_identity,
        lineage_identity=logical,
        selector_ref=new_ref,
        checkpoint_receipt=new_revision,
        state=source.state,
        next_actions=source.next_actions,
    )


def rebind_lineage_selector(
    current: VCSLineageBinding,
    *,
    new_ref: str,
    current_revision: str,
) -> VCSLineageBinding:
    """Rename/rebind a backend selector while preserving logical lineage identity."""

    if not new_ref or not current_revision:
        raise ValueError("new_ref and current_revision must be non-empty")
    return VCSLineageBinding(
        project_identity=current.project_identity,
        lineage_identity=current.lineage_identity,
        selector_ref=new_ref,
        checkpoint_receipt=current_revision,
        state=current.state,
        next_actions=current.next_actions,
    )
