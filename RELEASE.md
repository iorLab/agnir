# Agnir 0.2.0-rc.1 Release Candidate

**Repository version:** `0.2.0-rc.1`

**Core compatibility line:** `0.2`

**Repository/filesystem profile:** `repository-filesystem/0.2`

## Status

Agnir `v0.2.0-rc.1` is the active release-candidate line on temporary branch `release/v0.2.0-rc.1`. It is **not yet published** at this checkpoint. The final candidate must pass exact-head conformance before an immutable tag and GitHub prerelease may be created.

The latest published **stable** release remains immutable `v0.1.1` at exact revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`, GitHub Release id `380414987`. A prerelease, release branch, moving `main`, or untagged revision must not be silently selected as `latest stable`.

## Version model

Agnir keeps distinct version layers:

- repository SemVer: `0.2.0-rc.1`;
- Core compatibility: `0.2`;
- repository/filesystem compatibility: `repository-filesystem/0.2`;
- VCS/adapter extension identifiers remain separately versioned where applicable.

Core/profile `0.2` is a compatibility-line change from `0.1`, not a compatible operational patch.

## Core 0.2 release-candidate scope

The RC introduces **Continuity Lineages** as an explicit Core abstraction:

- one Project may own multiple independently advancing logical lineages;
- Project identity is distinct from logical lineage identity;
- logical lineage identity is distinct from backend selector/locator and revision receipt;
- ordinary work resolves one selected lineage without sibling guessing;
- checkpoints are lineage-local by default;
- integration reconciles target continuity rather than copying source continuity;
- an Agnir-controlled target publication publishes integrated Project state and reconciled target continuity coherently;
- stale target or relevant source generations invalidate a staged integration candidate;
- an Agnir-controlled lineage fork publishes lineage identity, selector binding, and coherent inherited/reconciled continuity together.

Normative RC contracts:

- `spec/AGNIR_CORE_0_2.md`;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md`;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- `schemas/agnir-manifest-0.2.schema.json`.

The former competing `_DRAFT` Core/profile files are absent from the active RC source tree.

## Compatibility and migration boundary

A Core/profile `0.1` Project must not be silently rewritten as `0.2` during an ordinary compatible upgrade. Explicit `0.1` → `0.2` migration preserves Project identity and material durable truth, establishes exactly one initial logical lineage for the preexisting implicit continuity line, preserves/resolves memory locators, establishes backend selector binding separately when applicable, and verifies fresh Core/profile `0.2` discovery.

Repeating the same migration is a no-op; attempting to silently rebind an already migrated Project to a different initial lineage is a conflict. Stale source state must not be overwritten. Published Core/profile `0.1` specifications, schemas, reference models, and regression tests remain in the repository as supported compatibility surfaces.

## RC self-host identity

The release branch explicitly self-hosts:

- Project: `urn:agnir:project:agnir-core`;
- logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`;
- VCS selector: `refs/heads/release/v0.2.0-rc.1`.

The lineage and selector are intentionally distinct semantic concepts. A commit SHA is a receipt, not identity.

## Verified operational package baseline

The operational Skill/documentation/conformance package applied for final RC validation is immutable revision:

`bee78b2c9bb8c5ce5916d08691019dcde939b813`

`extensions.agnir/operations` records repository release `0.2.0-rc.1` with that actual `applied_revision`. This two-step provenance is deliberate: the final candidate may truthfully record an already-existing immutable package baseline, whereas no commit can contain its own not-yet-known SHA as content.

Exact-head GitHub Actions run `33673892651` passed on `bee78b2...`, including RC self-host, stable `0.1` regressions, Core `0.2` VCS/non-VCS pressure, repository-filesystem `0.2`, lineage binding, semantic/concrete migration, the dedicated RC fresh-install/published-v0.1.1 migration gate, and the full suite.

## Fresh installation and published migration evidence

`conformance/test_rc_release_gates.py` is a release-blocking RC test surface. It proves:

1. a genuinely fresh Core/profile `0.2` Project can initialize one Project identity + one logical lineage, persist the Agent-operable activation route, and cold-start without predecessor-private context;
2. the migration fixture is anchored to the exact published `v0.1.1` `AGNIR.yaml` Git blob `0d26a9ffb947f551af335963ef753e7c0758c505`;
3. explicit migration preserves Project identity and durable memory bytes, fresh-resumes as Core/profile `0.2`, is rejected by the stable `0.1` resolver after migration, and is idempotent for the same initial lineage.

The test landed at `b6fde55e525f4a077a070e1cf181304a3dfd7a9d`; CI `33673869587` succeeded. It became an independent workflow gate at `bee78b2...`; CI `33673892651` succeeded.

## Real repository migration from published v0.1.1

A stronger migration validation used Agnir itself as a real Project and started directly from immutable published tag `v0.1.1`, not moving `main`.

Source receipts:

- tag target `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- root tree `44003ec33d4dbc3606c34a5334027fe7aaf6f0e3`;
- `.agnir` tree `37b152659499c1079c796646dce23a8112660b6f`;
- Decisions blob `eb08f76a703d9d033a8e092d67c837549ade7d46`;
- Evidence tree `ff974443e4e7bd119bd4673d28cd21833cf15a33`.

Coherent migration revision `041f540a213c90e55d10e70aebaf14d8c1194a2a` has the published tag target as its direct parent, preserves Project identity and durable source receipts, applies operational baseline `bee78b2...`, and establishes logical lineage `urn:agnir:lineage:validation:v0.2.0-rc.1-from-v0.1.1` separately from its VCS selector.

Validation instrumentation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97` passed GitHub Actions run `33674731595`. The run includes validation-root fresh Core `0.2` resume, stable Core `0.1` regressions, Core `0.2` VCS/non-VCS/profile/binding/migration gates, the RC release-gate fixture, and the full suite.

Earlier runs `33674632504` and `33674669670` failed because the validation-only inline Python harness omitted `PYTHONPATH=conformance`; the harness was fixed without changing Core/profile contracts or migration continuity, after which `33674731595` passed completely.

Detailed receipts are stored in `.agnir/evidence/2026-09-03-v0.2.0-rc.1-release-gates.md`.

## RC publication gate

`v0.2.0-rc.1` may be tagged/released only when all of the following are true:

1. `VERSION` is `0.2.0-rc.1`;
2. root `AGNIR.yaml` fresh-resolves Core `0.2` / `repository-filesystem/0.2`, Project `urn:agnir:project:agnir-core`, and the RC logical lineage;
3. logical lineage identity and VCS selector binding are explicit and distinct;
4. Core/profile/migration/schema contracts agree;
5. stale draft contracts do not compete with RC normative contracts;
6. both READMEs and root `SKILL.md` describe the RC model consistently while `latest stable` remains `v0.1.1`;
7. `REPOSITORY_TREE.md` matches the actual active source tree;
8. RC Core `0.2` self-host cold-start passes;
9. Core/profile `0.1` regressions remain green;
10. Core `0.2` non-VCS/VCS, profile, lineage binding, semantic/concrete migration, and full suite pass;
11. genuinely fresh Core `0.2` installation passes;
12. migration from the exact published `v0.1.1` shape passes, and a real repository Project migration from immutable `v0.1.1` passes fresh resume;
13. operational provenance points to actual immutable RC package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813`;
14. the **final candidate revision containing the completed provenance/evidence checkpoint** passes the complete exact-head workflow;
15. the RC tag is created directly at that exact green candidate, the GitHub Release is `prerelease=true` / `draft=false`, the tag is never moved, and the RC is never presented as `latest stable`.

Items 1–13 are satisfied before final-candidate publication. Item 14 is the immediate next gate. Item 15 happens only after item 14 succeeds.

## Known limitations

Real mount-boundary behavior remains explicitly unproven because the current conformance environment has not supplied a genuine mount-capable case. Ordinary directories are not accepted as substitute evidence.

Execution-surface persistence/configuration remains adapter behavior outside Agnir Core. Automatic configuration depends on the active surface's tools and Principal authority.

The optional VCS extension serialization may evolve independently so long as the normative distinction between logical lineage identity, selector/binding, and revision receipt is preserved.

## Publication result

**Pending.** This section must be changed only after the exact final candidate is green and immutable `v0.2.0-rc.1` plus its GitHub prerelease actually exist. Until then, do not claim the RC has been published.
