# Agnir 0.2.0-rc.1 Release Candidate

**Repository version:** `0.2.0-rc.1`

**Core compatibility line:** `0.2`

**Repository/filesystem profile:** `repository-filesystem/0.2`

## Status

Agnir `v0.2.0-rc.1` is the active release-candidate line on temporary branch `release/v0.2.0-rc.1`. It is **not yet published** at this checkpoint, and no RC tag/release should be claimed until an exact candidate revision passes the complete publication gate below.

The latest published **stable** release remains immutable `v0.1.1` at exact revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`, GitHub Release id `380414987`. A prerelease, release branch, or moving `main` must not be silently selected as `latest stable`.

## Version model

Agnir keeps distinct version layers:

- repository SemVer: `0.2.0-rc.1` for this candidate package/spec/conformance repository;
- Core compatibility: `0.2`;
- repository/filesystem compatibility: `repository-filesystem/0.2`;
- VCS/adapter extension identifiers remain separately versioned where applicable.

Core/profile `0.2` is a compatibility-line change from `0.1`, not a compatible operational patch.

## Core 0.2 release-candidate scope

The RC introduces **Continuity Lineages** as an explicit Core abstraction:

- one Project may own multiple independently advancing logical lineages;
- Project identity is distinct from lineage identity;
- logical lineage identity is distinct from backend selector/locator and revision receipt;
- ordinary work resolves one selected lineage without sibling guessing;
- checkpoints are lineage-local by default;
- integration reconciles target continuity rather than copying source continuity;
- an Agnir-controlled target publication must publish integrated Project state and reconciled target continuity coherently;
- stale target or relevant source generations invalidate a staged integration candidate;
- an Agnir-controlled lineage fork publishes the new lineage identity, selector binding, and coherent inherited/reconciled continuity together.

Normative RC contracts:

- `spec/AGNIR_CORE_0_2.md`;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md`;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- `schemas/agnir-manifest-0.2.schema.json`.

## Compatibility and migration boundary

A Core/profile `0.1` Project must not be silently rewritten as `0.2` during an ordinary compatible upgrade.

Explicit `0.1` → `0.2` migration must preserve Project identity and material durable truth, establish exactly one initial/default logical lineage for the preexisting implicit continuity line, preserve/resolve its memory locators, establish backend selector binding separately when applicable, and verify fresh Core/profile `0.2` discovery.

Repeating the same migration is a no-op; attempting to silently rebind an already migrated Project to a different initial lineage is a conflict. Stale source state must not be overwritten.

The published Core/profile `0.1` specifications, schemas, reference models, and regression tests remain in the repository as supported compatibility/history surfaces.

## Evidence before this RC branch

The pre-RC line already passed:

- non-VCS SQLite lineage conformance;
- VCS lineage mapping/binding and branch-aware integration pressure;
- repository-filesystem `0.2` discovery and schema pressure;
- storage-neutral and concrete repository/filesystem `0.1`→`0.2` migration conformance;
- a real Svif consumer migration, two-lineage divergence, staged integration, target reconciliation, coherent publication, and independent source resume;
- safe integration of Core `0.2` into Agnir authoritative `main` with exact-candidate validation before target advancement and successful authoritative-main conformance afterward.

Key Agnir receipts:

- Core `0.2` source checkpoint `68cc443d6c44929f1b71d9d534e9b0f73f9745bf`, CI `33620080730`;
- safe-main candidate `a32c9143687b72426617ddd701b90ffd237a111c`, candidate CI `33653019074`;
- authoritative-main CI `33653087179`;
- post-integration main checkpoint `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`, CI `33653383024`.

## RC self-host boundary

The release branch explicitly migrates Agnir's own Project from Core/profile `0.1` to Core/profile `0.2` while preserving Project identity `urn:agnir:project:agnir-core` and the existing durable memory layout.

RC logical lineage:

`urn:agnir:lineage:v0.2.0-rc.1`

VCS selector binding:

`refs/heads/release/v0.2.0-rc.1`

These values are intentionally distinct. The ref is a backend selector/binding; it is not logical lineage identity. A commit SHA is a receipt, not identity.

## Operational package boundary

The repository's operational Skill/documentation package is being synchronized during this RC cycle. Until that package is complete and an exact verified candidate revision exists, `extensions.agnir/operations` may truthfully continue to record the actually applied published `v0.1.1` package rather than inventing a self-referential RC applied revision.

Before RC publication, the final exact candidate must align `SKILL.md`, both READMEs, release/version metadata, repository maps, self-host compatibility, and applied RC provenance used by installation/migration validation.

## RC publication gate

`v0.2.0-rc.1` may be tagged/released only when all of the following are true on one exact candidate revision:

1. `VERSION` is `0.2.0-rc.1`;
2. root `AGNIR.yaml` fresh-resolves Core `0.2` / `repository-filesystem/0.2`, Project `urn:agnir:project:agnir-core`, and the RC logical lineage;
3. logical lineage identity and VCS selector binding are explicit and distinct semantic concepts;
4. `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, migration spec, and 0.2 schema agree on the compatibility contract;
5. stale draft documents no longer compete with RC normative contracts;
6. both READMEs and root `SKILL.md` describe the Core/profile `0.2` RC model consistently while preserving the rule that `latest stable` is still `v0.1.1`;
7. `REPOSITORY_TREE.md` and release-facing structural maps match the actual repository;
8. RC Core `0.2` self-host cold-start passes;
9. Core/profile `0.1` compatibility regressions remain green;
10. Core `0.2` non-VCS/VCS, repository-filesystem `0.2`, lineage binding, semantic/concrete migration, and full conformance suites pass;
11. a genuinely fresh Project can be initialized with the explicit RC target and cold-start resume without predecessor-private context;
12. at least one explicitly authorized real Project migrates from published `v0.1.1` / Core/profile `0.1` to `0.2`, preserving Project identity/durable truth and passing fresh resume;
13. the final operational package provenance used by the validation points to an actual immutable RC candidate revision;
14. the RC tag/release is created only after exact-candidate verification and is marked prerelease;
15. the RC tag is never moved after publication and the RC is never presented as `latest stable`.

## Known limitations

Real mount-boundary behavior remains explicitly unproven because the current conformance environment has not supplied a genuine mount-capable case. Ordinary directories are not accepted as substitute evidence.

Execution-surface persistence/configuration remains adapter behavior outside Agnir Core. The Skill may define locator-only handoff semantics, but automatic configuration depends on the active surface's tools and Principal authority.

The optional VCS extension serialization may evolve independently so long as the normative Core/profile distinction between logical lineage identity, selector/binding, and revision receipt is preserved.

## Publication result

Pending. This section must be updated only after an exact verified RC candidate is immutably tagged and a prerelease is actually created. Until then, do not claim `v0.2.0-rc.1` has been published.
