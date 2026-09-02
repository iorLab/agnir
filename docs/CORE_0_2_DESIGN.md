# Agnir Core 0.2 Design — Parallel Continuity

Status: design draft

## Goal

Agnir Core 0.2 generalizes Project continuity from a single continuity line into multiple independently advancing continuity lineages without introducing Git, branch, commit, repository, filesystem, Agent, or execution-surface concepts into Core.

## Design hypothesis

A Project may own more than one continuity lineage. Each lineage carries its own Current State, Next Actions, Decisions, and Evidence while retaining the same Project identity.

A backend-specific construct such as a Git branch MAY map to a continuity lineage, but the Core abstraction is not a VCS branch.

## Candidate Core invariants

1. **Project identity is lineage-independent.** Creating, selecting, advancing, reconciling, or retiring a lineage does not create a new Project identity.
2. **Continuity is lineage-local.** A checkpoint on one lineage MUST NOT implicitly mutate the authoritative continuity of another lineage.
3. **Lineage selection is explicit or deterministically provided by the execution/profile context.** Core MUST NOT require sibling-lineage scanning or heuristic selection.
4. **Integration is reconciliation, not continuity copying.** Source continuity is evidence/input to a target reconciliation; it does not automatically become target truth.
5. **Target publication is coherent.** An integration that changes Project state and target continuity MUST NOT publish a target state in which the Project result and target continuity knowingly disagree.
6. **Backend revision identifiers are receipts, not lineage identity.** Git SHAs, database revisions, snapshot IDs, or equivalent backend tokens MAY identify checkpoints but MUST NOT define Project or lineage identity.
7. **Cross-Project integration remains explicit.** Shared or similar lineage identifiers MUST NOT bypass Project identity checks.

## Candidate model

```text
Project
├── identity
└── continuity
    ├── lineage A
    │   ├── Current State
    │   ├── Next Actions
    │   ├── Decisions
    │   └── Evidence / Checkpoints
    └── lineage B
        ├── Current State
        ├── Next Actions
        ├── Decisions
        └── Evidence / Checkpoints
```

The exact durable representation of lineage identity is intentionally unresolved in this first design draft. Core 0.2 should standardize the semantics before standardizing a storage encoding.

## Required conformance evidence before Core 0.2 is accepted

Core 0.2 MUST be validated by at least two materially different backend models:

- **VCS-backed case:** Git branches/worktrees with independent checkpoints and staged target reconciliation.
- **Non-VCS case:** independent namespaces/snapshots in a backend that has no Git branch, commit, worktree, or repository semantics.

Both cases must demonstrate the same Core invariants: shared Project identity, independent lineage advancement, explicit selection, target reconciliation, coherent publication, and fresh resume/discovery of each lineage.

## Non-VCS reference case

The first non-VCS conformance fixture should model a Project with two independently persisted namespaces (for example, SQLite rows or an in-memory transactional store persisted by the test fixture):

```text
Project P
├── lineage A / namespace A
└── lineage B / namespace B
```

Required sequence:

1. Create A and B from the same Project continuity baseline.
2. Advance and checkpoint A independently.
3. Advance and checkpoint B independently.
4. Fresh-resolve A and B and prove isolation.
5. Construct an integration candidate from B into A without publishing A yet.
6. Reconcile the resulting Project state with A continuity plus relevant B continuity/Evidence.
7. Publish the integrated Project state and reconciled A continuity coherently.
8. Fresh-resolve A and B; A reflects the integration, B remains its own continuity line.

## Relationship to `agnir/vcs-branch-continuity/0.1`

The existing experimental VCS extension is treated as evidence and a profile/adapter mapping candidate for Core 0.2. It should not be copied wholesale into Core.

Potential mapping:

```text
Git selected ref/worktree  -> selected continuity lineage
branch-local checkpoint    -> lineage-local checkpoint
merge/rebase/cherry-pick   -> lineage integration boundary
Git revision / commit SHA  -> backend checkpoint receipt
ref advancement            -> backend publication boundary
```

Git-specific failure details remain profile/adapter concerns unless a backend-neutral failure class is proven necessary.

## Versioning direction

If these semantics are accepted and conformance succeeds, the intended repository release is `v0.2.0` with Core compatibility `0.2`.

Agnir `v1.0.0` is not triggered by feature count alone. It should mark the point where the Core contract, compatibility policy, migration guarantees, and reference conformance are mature enough that downstream Projects can depend on them without expecting routine breaking redesign.
