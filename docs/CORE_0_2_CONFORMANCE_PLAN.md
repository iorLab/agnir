# Agnir Core 0.2 Conformance Plan

Status: design draft

## Purpose

This plan tests whether Parallel Continuity belongs in Agnir Core rather than only in the VCS profile layer.

## Acceptance rule

Core 0.2 may adopt Continuity Lineage only if the same backend-neutral invariants pass in both a VCS-backed implementation and a non-VCS implementation.

## Conformance matrix

| Invariant | VCS-backed case | Non-VCS case |
| --- | --- | --- |
| Same Project identity across lineages | branches/worktrees | namespaces/snapshots |
| Explicit lineage selection | selected ref/worktree | namespace selector |
| Independent checkpoint advancement | branch-local checkpoint | namespace-local checkpoint |
| Fresh resume isolation | checkout/worktree resolve | namespace resolve |
| Integration uses source as input, not truth | merge/rebase/cherry-pick | staged namespace integration |
| Target remains unpublished until reconciliation | ref unchanged during staged integration | transaction/snapshot not committed |
| Coherent target publication | reconciled target commit/ref advance | atomic transaction/snapshot publish |
| Backend revision token is not lineage identity | commit SHA rewrite | revision/snapshot token replacement |
| Cross-Project mismatch remains rejected | different AGNIR Project identity | different store Project identity |

## VCS fixture

Reuse and evolve the existing `agnir/vcs-branch-continuity/0.1` tests. The fixture must continue to prove that the target ref remains unchanged until reconciliation is complete.

## Non-VCS fixture

Implement a deliberately small transactional reference store that contains:

- Project identity
- lineage selector
- per-lineage State / Next Actions / Decisions / Evidence
- opaque revision receipt
- staged integration candidate
- atomic publish operation

The store must not use or emulate Git terminology internally.

## Required non-VCS scenarios

1. Two lineages created from the same Project baseline retain the same Project identity.
2. Each lineage advances independently and fresh-resolves to its own continuity.
3. Updating one lineage cannot mutate the other without an explicit integration operation.
4. Integration stages a candidate while target published state remains unchanged.
5. Source continuity participates as reconciliation input but is not copied as target truth.
6. Publishing the reconciled candidate updates Project result + target continuity atomically.
7. Source lineage remains independently resumable after target integration.
8. Opaque revision receipt changes without changing Project identity or lineage identity.
9. Cross-Project integration is explicitly rejected.
10. Missing lineage selection fails explicitly rather than guessing.

## Decision after conformance

- If both backend classes satisfy the same invariants without backend leakage, promote the generic semantics into Core 0.2 and keep backend mapping in profiles/adapters.
- If the non-VCS model requires materially different semantics, retain the VCS behavior as an extension and revise the Core abstraction before publication.
