# Agnir Core 0.2 Design — Parallel Continuity

Status: active design / first reference implementation

## Goal

Agnir Core 0.2 generalizes Project continuity from a single implicit continuity line into multiple independently advancing continuity lineages without introducing Git, branch, commit, repository, filesystem, Agent, or execution-surface concepts into Core.

The working normative draft is `spec/AGNIR_CORE_0_2_DRAFT.md`. Core `0.1` remains the published stable contract while this design is under conformance pressure.

## Accepted design direction

A Project may own more than one **Continuity Lineage**. Each selected lineage carries its own Current State, Next Actions, Decisions, and Evidence while retaining the same Project identity.

Core `0.2` now treats **lineage identity as a required logical semantic**, but not as a prescribed storage field or serialization. A lineage identity must be durable and non-empty within Project scope. A backend revision, Git SHA, database generation, snapshot version, or equivalent receipt is not lineage identity.

A backend-specific construct such as a Git branch MAY map to a continuity lineage, but the Core abstraction is not a VCS branch.

## Candidate Core invariants under conformance

1. **Project identity is lineage-independent.** Creating, selecting, advancing, reconciling, or retiring a lineage does not create a new Project identity.
2. **Lineage identity is logical, not revision-derived.** Backend revision receipts may change while Project identity and lineage identity remain stable.
3. **Continuity is lineage-local.** A checkpoint on one lineage MUST NOT implicitly mutate the authoritative continuity of another lineage.
4. **Lineage selection is explicit or deterministically provided by execution/profile/backend context.** Core MUST NOT require sibling-lineage scanning or heuristic selection.
5. **A selected missing lineage fails.** Implementations must not silently fall back to a default after a specifically selected lineage fails to resolve.
6. **Integration is reconciliation, not continuity copying.** Source continuity is evidence/input to a target reconciliation; it does not automatically become target truth.
7. **Target publication is coherent.** An integration that changes Project state and target continuity MUST NOT knowingly publish a target generation in which the Project result and target continuity disagree.
8. **Staged candidates are optimistic over authoritative generations.** If target or relevant source continuity advances after a candidate is staged, publication must fail and be re-resolved/reconciled.
9. **Cross-Project integration remains explicit.** Shared or similar lineage identifiers MUST NOT bypass Project identity checks.

## Core discovery shape

Core `0.2` should resolve **one selected lineage** for ordinary lineage-local work rather than requiring the Discovery Record to enumerate every sibling lineage:

```text
Project Entry Point + selection context
            ↓
Core 0.2 Discovery Record
├── Project identity
├── selected Continuity Lineage identity
└── selected lineage memory locators
    ├── Current State
    ├── Next Actions
    ├── Decisions
    └── Evidence / Checkpoints
```

This is deliberate. Enumeration may be useful to some profiles/adapters, but making it a Core requirement would reintroduce branch/workspace scanning behavior that is neither necessary nor backend-neutral.

## Selection rule

The generic reference order is:

1. explicit Principal/task/adapter lineage;
2. already-selected execution/profile/backend context;
3. explicitly declared default lineage.

If no lineage can be selected, surface `AGNIR_LINEAGE_REQUIRED`.

If an explicitly/contextually selected lineage does not resolve, surface `AGNIR_LINEAGE_NOT_FOUND`; do not silently fall back to another lineage.

## Required conformance evidence before Core 0.2 is accepted

Core 0.2 MUST be validated by at least two materially different backend models:

- **VCS-backed case:** Git branches/worktrees with independent checkpoints and staged target reconciliation.
- **Non-VCS case:** logical namespaces persisted transactionally without Git branch, commit, worktree, ref, or repository semantics.

Both cases must demonstrate the same Core invariants: shared Project identity, durable logical lineage identity, independent advancement, deterministic selection, target reconciliation, coherent publication, stale-candidate rejection, and fresh resume/discovery of each lineage.

## Non-VCS reference implementation

The first non-VCS implementation is `conformance/sqlite_lineage_reference.py`.

It uses:

```text
SQLite Project P
├── logical lineage A
│   └── generation N
└── logical lineage B
    └── generation M
```

There is no repository or branch concept. SQLite transactions provide coherent publication; integer generations provide checkpoint receipts and optimistic integration conflict detection.

The reference sequence is:

1. create one Project and initial lineage;
2. fork a second logical lineage from the same continuity baseline;
3. advance each independently;
4. fresh-resolve both and prove isolation;
5. stage a source→target integration candidate while target remains authoritative at its previous generation;
6. reject publication without reconciliation;
7. reject the candidate if target or relevant source generation changes before publication;
8. atomically publish resulting Project state + reconciled target continuity;
9. fresh-resolve both lineages and prove the source lineage remained independent.

## Relationship to `agnir/vcs-branch-continuity/0.1`

The experimental VCS extension is evidence and a profile/adapter mapping candidate for Core 0.2. It is not copied wholesale into Core.

Mapping:

```text
Git selected ref/worktree  -> selected Continuity Lineage
branch name/ref            -> profile-level lineage identity mapping
branch-local checkpoint    -> lineage-local checkpoint
merge/rebase/cherry-pick   -> lineage integration boundary
Git revision / commit SHA  -> backend checkpoint receipt
ref advancement            -> backend publication boundary
```

Git-specific failure details remain profile/adapter concerns when a more generic Core failure already captures the protocol condition.

## Versioning direction

If these semantics and the migration rules are accepted and dual-backend conformance succeeds, the intended repository release is `v0.2.0` with Core compatibility `0.2`.

Agnir `v1.0.0` is a later stability commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.
