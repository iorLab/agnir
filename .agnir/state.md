# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release. `main` remains authoritative and unchanged by the active experimental work. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Active Core 0.2 line — 2026-09-02

Core `0.2` Parallel Continuity development is active on temporary branch `feature/core-0.2-lineage` in draft PR `#5`, stacked on `feature/multibranch-continuity` / draft PR `#4`.

- Project identity remains `urn:agnir:project:agnir-core` across `main` and both development branches.
- Stable self-hosting remains Core `0.1` + `repository-filesystem/0.1`; this branch does not claim published Core `0.2` compatibility.
- Intended next feature release after safe integration/release-candidate gates: repository `v0.2.0` with Core compatibility `0.2` and `repository-filesystem/0.2`.
- `v1.0.0` remains a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.

## Core 0.2 candidate model

The candidate now has synthetic, non-VCS, VCS, concrete profile/migration, and real-Project consumer evidence for these semantics:

1. one Project may own multiple independently advancing Continuity Lineages;
2. Project identity is distinct from logical lineage identity;
3. logical lineage identity is distinct from backend selector/locator and revision receipt;
4. a Git ref/worktree is selector/binding context, not lineage identity; a Git SHA is a checkpoint receipt/conflict token;
5. ordinary work resolves one lineage from explicit/context/default selection without sibling scanning;
6. selected missing/unbound context fails rather than silently falling back;
7. checkpoints are lineage-local by default;
8. lineage fork must publish new lineage identity + selector binding + inherited/reconciled continuity coherently;
9. integration is target reconciliation, not source-continuity copying;
10. integrated Project state + reconciled target continuity publish coherently;
11. target or relevant source advancement invalidates a staged integration candidate;
12. Core `0.1` → `0.2` is explicit migration preserving Project identity and durable truth while establishing one initial/default lineage.

Working artifacts remain `spec/AGNIR_CORE_0_2_DRAFT.md`, `spec/CORE_0_2_DESIGN.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, `profiles/REPOSITORY_FILESYSTEM_0_2_DRAFT.md`, `schemas/agnir-manifest-0.2.schema.json`, and `conformance/agnir-0.2-plan.md`.

## Evidence layers completed

### Backend/profile/migration

- `conformance/sqlite_lineage_reference.py` proves the generic model without VCS/repository concepts.
- VCS mapping/binding conformance proves selector != lineage identity, branch fork with a new logical lineage, rebind/rename preserving identity, revision receipts, isolation, reconciliation, and stale-candidate rejection.
- `repository-filesystem/0.2` resolver/schema pressure is green.
- storage-neutral and concrete repository/filesystem Core `0.1` → `0.2` migration pressure is green.
- Agnir branch CI run `33591942902` passed stable Core `0.1` self-hosting, all experimental Core `0.2`/VCS/profile/migration gates, and the full suite.

### Real Svif consumer validation — completed

Svif `urn:svif:project:svif-core` completed the first real Core `0.2` consumer exercise on temporary branches while Svif `main` remained unchanged.

Receipts:

- common coherent baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`;
- target lineage `urn:svif:lineage:agnir-core-0.2-validation`, pre-integration revision `79c5b7c7ee2ed545492702bea43d0f7135602f35`, CI `33619053159` success;
- source lineage `urn:svif:lineage:agnir-core-0.2-parallel`, revision `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`, CI `33618885830` success;
- staged two-parent candidate `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3` created while the target ref remained unchanged;
- reconciled two-parent target revision `1cd25539c75f8a2a32c84b822c0db80b176fd319`;
- target ref advanced once from the pre-integration target directly to the reconciled revision; the staged candidate was never target truth;
- semantic self-host repair `e48ae07faa6a716f7e2cd83cdcefdce6d02d8c7e`, CI `33619491154` 3/3 success;
- Svif completion checkpoint `d42489f72cc8985d353ccbf2f9b6ae7249fe6480`, CI `33619807614` 3/3 success;
- source ref remained at `d2d0c1bf...` after target integration and fresh source discovery still resolved the source lineage/selector and source-local State.

The experiment also produced negative evidence: a preliminary source fork implemented as a sequence of ref-visible file writes briefly created an incoherent source branch state. That attempt was discarded before the accepted fork, and the coherent source fork was republished in one tree/commit. This confirms fork publication needs the same coherence discipline as target integration publication.

Detailed evidence is recorded in `.agnir/evidence/2026-09-02-svif-core-0.2-real-consumer-validation.md`.

## Current release boundary

The planned real-Project validation gate is now satisfied. The next release-blocking work is **safe Agnir integration and release-candidate preparation**, not additional synthetic lineage modeling by default.

Before Agnir `main` advances, review PR `#4` / `#5` together and construct an Agnir-aware target revision whose final `main` State / Next Actions / Decisions are already reconciled. Do not use ordinary server-side merge-first/follow-up-repair.

If integration review and authoritative-main conformance remain green, prepare `v0.2.0-rc.1`; then exercise fresh installation/migration/resume from published `v0.1.1` before final `v0.2.0` publication.

## Published stable release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
