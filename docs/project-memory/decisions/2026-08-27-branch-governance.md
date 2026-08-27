# Agnir branch-governance decision

Date: 2026-08-27
Status: Accepted

## Decision

During the Agnir architecture rewrite, branch governance is intentionally minimal:

- `main` is the authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0` preserves the final pure PPMP v2.0.0 / PPM / Sandminni predecessor boundary at `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`.
- Temporary, experimental, redundant, or otherwise non-authoritative branches do not require immediate cleanup while the new version is still under active restructuring.
- Branch cleanup is deferred until the new Agnir version is substantially complete, at which point non-authoritative branches should be reviewed and removed deliberately.
- Durable project state, specifications, conformance work, and migration decisions MUST treat `main` and the explicit `legacy/*` predecessor branch as the meaningful branch boundaries. Incidental branches MUST NOT become hidden sources of truth.

## Rationale

The current priority is architectural convergence, not repository housekeeping. Immediate cleanup of incidental branches adds churn without improving protocol correctness, while preserving a clear active line and predecessor line is sufficient for safe development and historical recovery.

## Consequence

Future work may rewrite `main` aggressively toward Agnir without preserving predecessor layout in-place. Historical PPMP v2.0.0 behavior remains recoverable from `legacy/ppmp-v2.0.0`. Non-authoritative branch cleanup is a release-completion task rather than an architecture-transition blocker.
