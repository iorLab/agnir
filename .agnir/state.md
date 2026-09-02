# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release. `main` remains authoritative and unchanged by the active experimental work. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Active Core 0.2 line — 2026-09-02

Core `0.2` Parallel Continuity development is active on temporary branch `feature/core-0.2-lineage` in draft PR `#5`, stacked on `feature/multibranch-continuity` / draft PR `#4`.

- Project identity remains `urn:agnir:project:agnir-core` across `main`, the VCS experiment, and the Core `0.2` design branch.
- Stable self-hosting remains Core `0.1` + `repository-filesystem/0.1`; the root Project does **not** yet claim Core `0.2` compatibility.
- Intended next feature release if all remaining gates pass: repository `v0.2.0` with Core compatibility `0.2` and `repository-filesystem/0.2`.
- `v1.0.0` remains a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.

## Core 0.2 model currently passing conformance

Working artifacts:

- `spec/AGNIR_CORE_0_2_DRAFT.md` — normative Core draft;
- `spec/CORE_0_2_DESIGN.md` — design rationale;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md` — compatibility-line migration contract;
- `profiles/REPOSITORY_FILESYSTEM_0_2_DRAFT.md` — concrete repository/filesystem profile draft;
- `schemas/agnir-manifest-0.2.schema.json` — experimental manifest schema;
- `conformance/agnir-0.2-plan.md` — acceptance pressure map.

Current accepted design direction under experiment:

1. One Project may own multiple independently advancing Continuity Lineages.
2. Project identity is distinct from logical lineage identity.
3. Logical lineage identity is distinct from backend selector/locator and revision receipt.
4. A Git ref/worktree is a **selector/binding**, not automatically lineage identity; a Git SHA is a checkpoint receipt/conflict token.
5. Ordinary work resolves exactly one lineage from explicit/context/default selection without sibling scanning.
6. Selected missing/unbound lineage context fails rather than silently falling back.
7. Checkpoints are lineage-local by default.
8. Integration is target reconciliation, not source-continuity copying.
9. Integrated Project state + reconciled target continuity publish coherently.
10. Target or relevant source advancement invalidates a staged integration candidate.
11. Core `0.1` → `0.2` is explicit migration; the existing implicit line becomes exactly one initial/default logical lineage while preserving Project identity and durable truth.

## Backend evidence

### Non-VCS

`conformance/sqlite_lineage_reference.py` implements logical lineage namespaces in SQLite with no repository/branch/ref/worktree/commit concepts. SQLite transactions provide atomic publication; integer generations are receipts/conflict tokens. The suite proves independent lineage advancement, selection/failure behavior, reconciliation, source/target stale-candidate rejection, atomic target publication, and cross-Project rejection.

### VCS mapping

`conformance/core_0_2_vcs_mapping_reference.py` and `test_core_0_2_vcs_mapping.py` prove:

```text
selected ref/worktree     -> backend selector/binding
logical lineage identity  -> separately resolved durable identity
commit/revision SHA       -> checkpoint receipt/conflict token
```

An earlier mapping that equated ref name with lineage identity was rejected because ref rename would silently change identity. The corrected tests prove selector string != identity, unbound selected ref does not fall back, SHA rewrite preserves logical identity, and explicit ref rename/rebinding may preserve logical identity.

`conformance/vcs_lineage_binding_reference.py` further proves that an Agnir-aware branch fork gets a new logical lineage identity while preserving Project identity/inherited baseline; ref rename preserves the lineage ID; external copied/stale bindings require explicit fork-vs-rebind resolution rather than guessing.

### Repository/filesystem 0.2

`repository-filesystem/0.2` now has a concrete draft resolver/schema. A selected Project root must expose one logical `continuity.lineage`; sibling enumeration is not required. Stable `repository-filesystem/0.1` discovery explicitly rejects the Core/profile `0.2` line.

For VCS-aware use, the profile draft separates durable `continuity.lineage` from optional selector binding metadata. External binding mismatch is a repair/classification condition, not automatic lineage creation.

## Migration evidence

The storage-neutral migration reference proves:

- unauthorized Core-line change remains `AGNIR_UPGRADE_MIGRATION_REQUIRED`;
- Project identity, State, Next Actions, Decisions, and Evidence are preserved;
- exactly one initial/default lineage is produced from the Core `0.1` implicit line;
- repeated identical migration is a no-op;
- conflicting second lineage rebinding fails;
- stale source generation blocks migration publication;
- fresh Core `0.2` resume recovers preserved truth.

A concrete repository/filesystem migration implementation should be added only against the now-defined `repository-filesystem/0.2` draft shape.

## CI and self-hosting evidence

Two early stable self-hosting failures were useful regressions rather than reasons to weaken the stable checker:

1. top-level `docs/` violated the repository's established active structure; content was moved into `spec/`, `conformance/`, or root policy files;
2. branch-local state rewrite dropped the still-valid `Durable continuity belongs to the Project` invariant; the state was repaired.

GitHub Actions run `33591706263` completed successfully after selector/identity correction and concrete profile pressure. The job passed:

1. Stable self-hosting cold-start conformance;
2. Experimental VCS branch continuity;
3. Experimental Core `0.2` non-VCS parallel continuity;
4. Experimental Core `0.2` VCS mapping;
5. Experimental `repository-filesystem/0.2` discovery;
6. Experimental VCS lineage binding;
7. Experimental Core `0.1` → `0.2` migration;
8. Full conformance suite.

Detailed evidence is recorded in `.agnir/evidence/2026-09-02-core-0.2-parallel-continuity.md`.

## Remaining release boundary

The synthetic/backend/profile evidence is now strong enough to proceed to a **real Project consumer validation**, but not yet to publish Core `0.2` stable.

Preferred first real consumer: Svif, because it already consumes Agnir Core `0.1` through a defined Continuity Provider boundary. The real validation should cover explicit migration, two genuinely divergent continuity lineages, independent checkpoints, VCS selector binding, staged target reconciliation, and fresh resume.

PR `#4` / `#5` eventual integration into authoritative `main` still must obey the target-publication invariant. Final `main` continuity must already be reconciled in the revision that advances `main`; do not knowingly publish an intermediate `main` revision carrying feature-local continuity truth.

## Published stable release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
