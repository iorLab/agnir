# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release. `main` remains authoritative and unchanged by the active experimental work. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, or Continuity Lineage.

## Active Core 0.2 line — 2026-09-02

Core `0.2` Parallel Continuity development is active on temporary branch `feature/core-0.2-lineage` in draft PR `#5`, stacked on `feature/multibranch-continuity` / draft PR `#4`.

- Project identity remains `urn:agnir:project:agnir-core` across `main`, the VCS experiment, and the Core 0.2 design branch.
- Stable self-hosting remains Core `0.1` + `repository-filesystem/0.1`. The root Project does **not** yet claim Core `0.2` compatibility while the new line is under conformance pressure.
- Intended next feature release, if the new compatibility line passes its gates: repository `v0.2.0` with Core compatibility `0.2`.
- `v1.0.0` is defined as a stability/compatibility commitment milestone rather than a feature-count threshold; criteria are recorded in `V1_RELEASE_CRITERIA.md`.

## Core 0.2 design now under test

The working normative draft is `spec/AGNIR_CORE_0_2_DRAFT.md`, with design rationale in `spec/CORE_0_2_DESIGN.md` and the dual-backend plan in `conformance/agnir-0.2-plan.md`.

Core `0.2` generalizes one implicit Project-global continuity line into multiple independently advancing **Continuity Lineages**.

Current design decisions under conformance:

1. Project identity is independent of lineage identity.
2. Lineage identity is a durable logical semantic within Project scope, not a mandated storage field or serialization.
3. Backend revisions such as Git SHAs, database generations, or snapshot versions are checkpoint receipts, not lineage identity.
4. Ordinary lineage-local work resolves exactly one lineage from explicit input, selected context, or declared default; Core does not require sibling enumeration/heuristic scanning.
5. A specifically selected missing lineage fails rather than falling back to another lineage.
6. Checkpoints are lineage-local unless explicit Project policy defines a broader transaction.
7. Integration is target reconciliation, not source-continuity copying.
8. Target publication must publish integrated Project state and reconciled target continuity coherently.
9. A staged integration candidate becomes stale if its target or relevant source authoritative generation advances before publication.
10. Cross-Project integration still respects the Project identity boundary.

## Non-VCS evidence

A first backend-neutral pressure test is implemented in:

- `conformance/core_0_2_reference.py`
- `conformance/sqlite_lineage_reference.py`
- `conformance/test_core_0_2_parallel_continuity.py`

The SQLite fixture deliberately has no repository, VCS branch, ref, worktree, commit, or merge concept. It models one Project with multiple logical lineage namespaces and uses SQLite transactions plus integer generations for coherent publication and stale-candidate detection.

The focused cases cover:

- explicit/context/default lineage selection and `AGNIR_LINEAGE_REQUIRED`;
- selected-missing-lineage rejection via `AGNIR_LINEAGE_NOT_FOUND`;
- same Project identity with independent lineage checkpoints;
- revision/generation receipt changes without lineage-identity changes;
- staged integration that leaves target authoritative truth unchanged until publication;
- rejection of unreconciled publication;
- target-generation conflict after staging;
- source-generation conflict after staging;
- cross-Project integration rejection.

CI has already exposed two self-hosting regressions in the Core `0.2` workstream before the new experimental test could run: first, an invalid top-level `docs/` directory violated the repository's stable structural contract; second, the branch-local state rewrite omitted the still-true Project ownership invariant required by stable cold-start conformance. The structural content has been moved into the repository's existing `spec/`, `conformance/`, and root policy surfaces, and this state restores the required Project-level invariant rather than weakening the stable checker.

## VCS evidence retained from PR #4

`agnir/vcs-branch-continuity/0.1` remains the Git/VCS evidence source. It already demonstrates branch-local continuity, selected-ref isolation, merge/rebase/cherry-pick reconciliation, history-rewrite receipt changes, and pre-target-advance reconciliation.

For Core `0.2`, those VCS concepts are mapped rather than promoted directly:

```text
selected Git ref/worktree -> selected Continuity Lineage
branch/ref logical name   -> profile-level lineage identity mapping
branch-local checkpoint   -> lineage-local checkpoint
merge/rebase/cherry-pick  -> lineage integration boundary
commit SHA                -> backend checkpoint receipt
ref advancement           -> backend publication boundary
```

PR `#4` and PR `#5` must eventually be integrated with target continuity already reconciled in the revision that advances `main`; ordinary server-side merge that temporarily publishes feature-local `.agnir` truth onto `main` remains unsafe for this repository's branch-local continuity model.

## Published stable release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`

The immutable stable release remains unaffected by the Core `0.2` draft.
