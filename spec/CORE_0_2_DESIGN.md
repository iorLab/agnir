# Agnir Core 0.2 Design — Parallel Continuity

Status: active design / dual-backend reference implementation

## Goal

Agnir Core 0.2 generalizes Project continuity from a single implicit continuity line into multiple independently advancing continuity lineages without introducing Git, branch, commit, repository, filesystem, Agent, or execution-surface concepts into Core.

The working normative draft is `spec/AGNIR_CORE_0_2_DRAFT.md`. Core `0.1` remains the published stable contract while this design is under conformance pressure.

## Accepted design direction

A Project may own more than one **Continuity Lineage**. Each selected lineage carries its own Current State, Next Actions, Decisions, and Evidence while retaining the same Project identity.

Core `0.2` treats **lineage identity as a required logical semantic**, but not as a prescribed storage field or serialization. A lineage identity must be durable and non-empty within Project scope.

Two distinctions are now explicit:

```text
Project identity != Continuity Lineage identity
Continuity Lineage identity != backend selector / locator / revision receipt
```

A Git ref/worktree, database namespace handle, workspace selector, or similar backend value may select/bind a lineage. It is not automatically the logical lineage identity. A Git SHA, database generation, snapshot version, or equivalent revision token is a checkpoint receipt/conflict token, not lineage identity.

This distinction was added after the first VCS→Core mapping pass exposed a rename problem: if a branch name were itself the Core identity, renaming a branch would silently change identity. The corrected model lets an explicit backend rebind/rename preserve one logical lineage while its selector changes.

## Candidate Core invariants under conformance

1. **Project identity is lineage-independent.** Creating, selecting, advancing, reconciling, rebinding, or retiring a lineage does not create a new Project identity.
2. **Lineage identity is logical, not locator/revision-derived.** Backend selectors and revision receipts may change while Project identity and lineage identity remain stable.
3. **Selection resolves to identity.** Explicit/context/default input may be a logical identity or backend selector; after resolution, one logical lineage identity must be known.
4. **Continuity is lineage-local.** A checkpoint on one lineage MUST NOT implicitly mutate the authoritative continuity of another lineage.
5. **Selection is deterministic.** Core MUST NOT require sibling-lineage scanning or heuristic selection.
6. **A selected missing/unbound lineage fails.** Implementations must not silently fall back after a specific selector/identity fails to resolve.
7. **Integration is reconciliation, not continuity copying.** Source continuity is evidence/input to a target reconciliation; it does not automatically become target truth.
8. **Target publication is coherent.** An integration that changes Project state and target continuity MUST NOT knowingly publish a target generation in which the Project result and target continuity disagree.
9. **Staged candidates are optimistic over authoritative generations.** If target or relevant source continuity advances after a candidate is staged, publication must fail and be re-resolved/reconciled.
10. **Cross-Project integration remains explicit.** Shared selectors or similar lineage identifiers MUST NOT bypass Project identity checks.

## Core discovery shape

Core `0.2` resolves **one selected logical lineage** for ordinary lineage-local work rather than requiring the Discovery Record to enumerate every sibling lineage:

```text
Project Entry Point + selection context
            ↓
profile/backend selector resolution (when needed)
            ↓
Core 0.2 Discovery Record
├── Project identity
├── selected logical Continuity Lineage identity
└── selected lineage memory locators
    ├── Current State
    ├── Next Actions
    ├── Decisions
    └── Evidence / Checkpoints
```

Enumeration may be useful to some profiles/adapters, but making it a Core requirement would reintroduce branch/workspace scanning behavior that is neither necessary nor backend-neutral.

## Selection rule

Generic precedence remains:

1. explicit Principal/task/adapter input;
2. already-selected execution/profile/backend context;
3. explicitly declared default lineage or default selector.

If no selection can be made, surface `AGNIR_LINEAGE_REQUIRED`.

If an explicitly/contextually selected identity/selector does not resolve to one lineage, surface `AGNIR_LINEAGE_NOT_FOUND`; do not silently fall back to another lineage.

## Required conformance evidence before Core 0.2 is accepted

Core 0.2 MUST be validated by at least two materially different backend models:

- **VCS-backed case:** Git refs/worktrees used as selectors/bindings, with logical lineage identity distinct from SHA receipts and capable of surviving explicit ref rename/rebinding.
- **Non-VCS case:** logical namespaces persisted transactionally without Git branch, commit, worktree, ref, or repository semantics.

Both cases must demonstrate the same Core invariants: shared Project identity, durable logical lineage identity, deterministic selection/binding, independent advancement, target reconciliation, coherent publication, stale-candidate rejection, and fresh resume/discovery of each lineage.

## Non-VCS reference implementation

The non-VCS implementation is `conformance/sqlite_lineage_reference.py`.

It uses:

```text
SQLite Project P
├── logical lineage A
│   └── generation N
└── logical lineage B
    └── generation M
```

There is no repository or branch concept. SQLite transactions provide coherent publication; integer generations provide checkpoint receipts and optimistic integration conflict detection. In this backend the namespace key can serve both as selector and logical identity by explicit backend design; Core does not require other backends to do the same.

## VCS mapping

`conformance/core_0_2_vcs_mapping_reference.py` now models:

```text
Git selected ref/worktree  -> backend selector/binding
logical lineage identity   -> separate durable identity resolved by that binding
branch-local checkpoint    -> lineage-local checkpoint
merge/rebase/cherry-pick   -> lineage integration boundary
Git revision / commit SHA  -> backend checkpoint receipt
ref advancement            -> backend publication boundary
```

The mapping tests explicitly prove:

- selector precedence matches generic Core precedence;
- an unbound selected ref fails instead of falling back to a sibling/default;
- SHA rewrite changes receipt without changing logical lineage identity;
- explicit ref rename/rebinding can preserve logical lineage identity;
- target/source revision movement invalidates a staged candidate;
- reconciled publication remains on the target logical lineage.

The experimental `agnir/vcs-branch-continuity/0.1` extension remains evidence and a source of backend behavior; it is not copied wholesale into Core.

## Migration

`spec/CORE_0_1_TO_0_2_MIGRATION.md` and `conformance/test_core_0_2_migration.py` pressure the compatibility-line transition. The current model preserves Project identity and all existing durable truth, creates exactly one initial/default lineage from the Core `0.1` implicit line, requires explicit migration authorization, makes repeated identical migration a no-op, and rejects conflicting lineage rebinding.

## Versioning direction

If these semantics, migration rules, concrete profile mapping, and real-Project validation are accepted, the intended repository release is `v0.2.0` with Core compatibility `0.2`.

Agnir `v1.0.0` is a later stability commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.
