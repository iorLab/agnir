from __future__ import annotations

"""Conformance reference surface for Agnir Core 1.0.

Core 1.0 is a stability promotion of the accepted Core 0.2 semantics.  The
reference intentionally re-exports the proven lineage/integration machinery
rather than forking a second implementation that could drift semantically.
"""

from core_0_2_reference import (
    ContinuityLineageSnapshot,
    IntegrationCandidate,
    LineageFailure,
    lineage_failure,
    make_integration_candidate,
    require_reconciliation,
    select_lineage,
    validate_project_identity,
)


CORE_1_0_VERSION = "1.0"


__all__ = [
    "CORE_1_0_VERSION",
    "ContinuityLineageSnapshot",
    "IntegrationCandidate",
    "LineageFailure",
    "lineage_failure",
    "make_integration_candidate",
    "require_reconciliation",
    "select_lineage",
    "validate_project_identity",
]
