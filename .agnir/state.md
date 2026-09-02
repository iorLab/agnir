# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release. `main` remains authoritative and unchanged by the active experimental work. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Active Core 0.2 line — 2026-09-02

Core `0.2` Parallel Continuity development is active on temporary branch `feature/core-0.2-lineage` in draft PR `#5`, stacked on `feature/multibranch-continuity` / draft PR `#4`.

- Project identity remains `urn:agnir:project:agnir-core` across `main` and both development branches.
- Stable self-hosting remains Core `0.1` + `repository-filesystem/0.1`; this branch does not yet claim stable Core `0.2` compatibility.
- Intended next feature release after remaining validation/integration gates: repository `v0.2.0` with Core compatibility `0.2` and `repository-filesystem/0.2`.
- `v1.0.0` remains a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.

## Core 0.2 model now passing synthetic/backend/profile pressure

The active candidate model is:

1. one Project may own multiple independently advancing Continuity Lineages;
2. Project identity is distinct from logical lineage identity;
3. logical lineage identity is distinct from backend selector/locator and revision receipt;
4. a Git ref/worktree is a selector/binding, not lineage identity; a Git SHA is a checkpoint receipt/conflict token;
5. ordinary work resolves exactly one lineage from explicit/context/default selection without sibling scanning;
6. selected missing/unbound context fails rather than silently falling back;
7. checkpoints are lineage-local by default;
8. integration is target reconciliation, not source-continuity copying;
9. integrated Project state + reconciled target continuity publish coherently;
10. target or relevant source advancement invalidates a staged integration candidate;
11. Core `0.1` → `0.2` is explicit migration: the existing implicit line becomes exactly one initial/default logical lineage while preserving Project identity and durable truth.

Working protocol/profile artifacts include `spec/AGNIR_CORE_0_2_DRAFT.md`, `spec/CORE_0_2_DESIGN.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, `profiles/REPOSITORY_FILESYSTEM_0_2_DRAFT.md`, `schemas/agnir-manifest-0.2.schema.json`, and `conformance/agnir-0.2-plan.md`.

## Evidence layers completed

### Non-VCS

`conformance/sqlite_lineage_reference.py` proves the generic lineage invariants with logical SQLite namespaces and transactions, without Git/repository semantics.

### VCS mapping and binding

`conformance/core_0_2_vcs_mapping_reference.py` and `conformance/vcs_lineage_binding_reference.py` prove selector/binding separation, revision-receipt semantics, Agnir-aware fork with a new lineage identity, rename/rebind preserving logical identity, and explicit failure for unresolved external binding mismatch.

### Repository/filesystem 0.2

`conformance/repository_filesystem_0_2_reference.py` plus `schemas/agnir-manifest-0.2.schema.json` prove selected-root Core/profile `0.2` discovery with required logical `continuity.lineage`. Stable `repository-filesystem/0.1` rejects the `0.2` compatibility line rather than interpreting it silently.

### Concrete Core 0.1 → 0.2 migration

`conformance/repository_filesystem_0_2_migration_reference.py` and `conformance/test_repository_filesystem_0_2_migration.py` now implement and pressure the concrete `AGNIR.yaml` migration path, not only the storage-neutral semantic model.

The concrete path:

- requires explicit migration authorization;
- preserves `project.identity` and existing durable memory locators/content;
- stages a candidate against a digest of the authoritative Core `0.1` manifest;
- inserts one explicit logical lineage and advances compatibility to Core/profile `0.2`;
- rejects stale source mutation before publication;
- publishes the manifest using a temporary file + atomic replace;
- verifies fresh `repository-filesystem/0.2` discovery after publication;
- treats repeated identical migration as a no-op and conflicting lineage rebinding as migration conflict.

## CI checkpoint

GitHub Actions run `33591942902` completed successfully for the Core `0.2` branch after the concrete repository migration gate was added. Its job passed:

1. Stable self-hosting cold-start conformance;
2. Experimental VCS branch continuity;
3. Experimental Core `0.2` non-VCS parallel continuity;
4. Experimental Core `0.2` VCS mapping;
5. Experimental `repository-filesystem/0.2` discovery;
6. Experimental VCS lineage binding;
7. Experimental Core `0.1` → `0.2` migration semantics;
8. Experimental concrete repository-filesystem `0.1` → `0.2` migration;
9. Full conformance suite.

Detailed evidence is recorded in `.agnir/evidence/2026-09-02-core-0.2-parallel-continuity.md`.

## Current release boundary

Synthetic/backend/profile/migration pressure is now green. The next release-blocking evidence is a **real Project consumer validation**, not more synthetic test accumulation.

The preferred first consumer is Svif because it already consumes Agnir Core `0.1` through a defined Continuity Provider boundary. Validation should use a temporary Svif development branch and cover explicit migration, two genuinely divergent logical lineages, independent checkpoints, VCS selector bindings, staged target reconciliation, and fresh resume. Svif `main` must remain unchanged until that experiment is reconciled and explicitly integrated.

PR `#4` / `#5` eventual integration into Agnir `main` still must obey the target-publication invariant: final `main` continuity must already be reconciled in the revision that advances `main`; ordinary merge-first / follow-up-repair is not the intended safe path.

## Published stable release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
