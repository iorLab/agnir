# Core 0.2 Work Status

Branch: `feature/core-0.2-lineage`

## Current objective

Validate whether Parallel Continuity / Continuity Lineage is a backend-neutral Agnir Core concept rather than only a VCS extension.

## Immediate next actions

1. Translate the candidate invariants in `CORE_0_2_DESIGN.md` into executable backend-neutral conformance cases.
2. Reuse the existing VCS branch-continuity fixture as one implementation of those invariants.
3. Add a deliberately non-VCS transactional namespace/snapshot reference implementation.
4. Compare failure semantics and identify which failures belong in Core versus profiles/adapters.
5. If both backend classes satisfy the same model without backend leakage, draft the normative Core 0.2 spec and migration path from Core 0.1.
6. Only after the normative draft exists, validate Core 0.2 in Svif as a real consumer Project.

## Release direction

If accepted, target repository release: `v0.2.0`; target Core compatibility: `0.2`.

Agnir `v1.0.0` remains gated by the separate stability criteria in `V1_RELEASE_CRITERIA.md`.
