# Agnir Core 0.2 Conformance Plan

Status: active experimental gate

## Purpose

This plan tests whether Parallel Continuity belongs in Agnir Core rather than only in the VCS profile layer.

## Acceptance rule

Core 0.2 may adopt Continuity Lineage only if the same backend-neutral invariants pass in both a VCS-backed implementation and a non-VCS implementation without confusing backend selectors/locators with logical lineage identity.

## Conformance matrix

| Invariant | VCS-backed case | Non-VCS case |
| --- | --- | --- |
| Same Project identity across lineages | branches/worktrees | logical namespaces |
| Durable logical lineage identity distinct from revision | logical lineage ID vs SHA | lineage key vs generation |
| Selector/binding distinct from identity when backend requires it | ref/worktree -> logical lineage binding | namespace may equal identity by backend design |
| Explicit deterministic selection | selected ref/worktree | namespace selector |
| Selected unbound/missing value does not fall back | unbound ref | missing namespace |
| Selector rename can preserve logical identity | explicit ref rebind/rename | namespace alias/rebind where supported |
| Independent checkpoint advancement | branch-local checkpoint | namespace-local checkpoint |
| Fresh resume isolation | ref/worktree binding resolve | namespace resolve |
| Integration uses source as input, not truth | merge/rebase/cherry-pick | staged namespace integration |
| Target remains unpublished until reconciliation | ref unchanged during staged integration | transaction not committed |
| Coherent target publication | reconciled target commit/ref advance | atomic transaction publish |
| Stale target/source candidate rejection | ref/revision conflict semantics | generation conflict |
| Cross-Project mismatch remains rejected | different Agnir Project identity | different store Project identity |

## VCS fixture

Reuse and evolve `agnir/vcs-branch-continuity/0.1` and `conformance/test_vcs_branch_continuity.py`. The real Git fixture must continue to prove that the target ref remains unchanged until reconciliation is complete.

`conformance/core_0_2_vcs_mapping_reference.py` is the Core mapping pressure layer. It MUST treat:

```text
ref/worktree             = backend selector/binding
logical lineage identity = separately resolved durable identity
commit SHA               = checkpoint receipt/conflict token
```

The mapping layer must prove that a selected ref can resolve to a logical identity that is not equal to the ref string, that an unbound selected ref fails rather than falling back, and that an explicit ref rename/rebinding can preserve the same logical lineage identity.

This prevents branch/ref, commit SHA, and merge/rebase/cherry-pick from leaking into Core semantics.

## Non-VCS fixture

`conformance/sqlite_lineage_reference.py` is the first reference backend. It deliberately contains no repository, branch, ref, worktree, commit, or VCS merge concept.

It persists:

- Project identity;
- optional default lineage identity;
- per-lineage Project result + State / Next Actions / Decisions / Evidence;
- integer generation receipts;
- staged integration candidates;
- atomic target publication through SQLite transactions.

In this fixture the namespace key intentionally serves as both selector and logical lineage identity. This is a backend choice, not a Core requirement.

## Required non-VCS scenarios

1. Two lineages created from the same Project baseline retain the same Project identity.
2. Each lineage advances independently and fresh-resolves to its own continuity.
3. Updating one lineage cannot mutate the other without an explicit integration operation.
4. Missing lineage selection fails explicitly rather than guessing.
5. Explicitly selected missing lineage fails instead of falling back to default.
6. Revision/generation receipt changes without changing Project identity or lineage identity.
7. Integration stages a candidate while target published state remains unchanged.
8. Publication without target reconciliation is rejected.
9. Publishing the reconciled candidate updates Project result + target continuity atomically.
10. Source lineage remains independently resumable after target integration.
11. Target advancement after staging invalidates the candidate.
12. Relevant source advancement after staging invalidates the candidate.
13. Cross-Project integration is explicitly rejected.

## Migration gate

Before Core `0.2` can be published stable, conformance must cover Core `0.1` → `0.2` migration:

- preserve Project identity;
- preserve existing durable continuity content;
- map the existing single continuity line into exactly one initial/default logical lineage;
- obtain that initial lineage identity explicitly or from deterministic profile/backend policy;
- make migration explicit rather than silently treating `0.2` as compatible with `0.1`;
- make repeated identical migration a no-op;
- reject an attempt to silently rebind an already migrated Project to another initial lineage identity;
- reject stale-source migration publication;
- cold-start the migrated Project as Core `0.2` from authorized selector/identity context or default.

## Current acceptance status

The first dual-backend + migration run passed all focused gates and the full conformance suite before the selector/identity distinction was tightened. The tightened VCS mapping adds explicit unbound-ref and rename-preserves-identity cases; CI must remain green after this refinement before the abstraction is considered accepted for the next profile-design step.

## Decision after conformance

- If both backend classes satisfy the same invariants without backend leakage, accept the generic lineage semantics into Core `0.2` and keep backend selector/binding mapping in profiles/adapters.
- If materially different backend semantics are required, revise the Core abstraction before publication instead of weakening tests or claiming premature compatibility.
