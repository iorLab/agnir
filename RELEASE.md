# Agnir 0.2.0-rc.1 Release Candidate

**Repository version:** `0.2.0-rc.1`

**Core compatibility line:** `0.2`

**Repository/filesystem profile:** `repository-filesystem/0.2`

## Status

Agnir `v0.2.0-rc.1` is formally published as a **prerelease**. Its immutable lightweight tag resolves directly to exact verified revision `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

GitHub Release:

- id: `381532232`;
- title: `Agnir v0.2.0-rc.1`;
- tag: `v0.2.0-rc.1`;
- `prerelease`: true;
- `draft`: false;
- published at: `2026-09-02T19:50:04Z`;
- publication/conformance workflow: `33675638723`.

The latest published **stable** release remains `v0.1.1`, exact tag target `e9712357ab590e5c1e5357b3cf3219d07d789aff`, GitHub Release id `380414987`. GitHub `releases/latest` remained `v0.1.1` after RC publication, so the RC does not change `latest stable` upgrade resolution.

Authoritative `main` has now accepted and reconciled the published RC Project/package line at exact revision `cd0427d26dddfabae768bcd76b78dc8d042151c7`. This does **not** make the RC a stable release; stable `v0.2.0` remains a separate publication decision.

## Version model

Agnir keeps distinct version layers:

- repository SemVer: `0.2.0-rc.1`;
- Core compatibility: `0.2`;
- repository/filesystem compatibility: `repository-filesystem/0.2`;
- VCS/adapter extension identifiers remain separately versioned where applicable.

Core/profile `0.2` is a compatibility-line change from `0.1`, not a compatible operational patch. A later repository SemVer promotion from `0.2.0-rc.1` to stable `0.2.0` does not itself require another Core/profile compatibility change.

## Core 0.2 contract

Core `0.2` introduces **Continuity Lineages** as an explicit Core abstraction while preserving Project-owned durable continuity:

- one Project may own multiple independently advancing logical lineages;
- Project identity != logical lineage identity;
- logical lineage identity != backend selector/locator or revision receipt;
- ordinary lineage-local work resolves one selected lineage without sibling guessing;
- checkpoints are lineage-local by default;
- integration reconciles target truth rather than copying source continuity;
- an Agnir-controlled target publication publishes integrated Project state + reconciled target continuity coherently;
- stale target or relevant source generations invalidate staged integration candidates.

Normative RC contracts:

- `spec/AGNIR_CORE_0_2.md`;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md`;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- `schemas/agnir-manifest-0.2.schema.json`.

Core/profile `0.1` artifacts remain available as supported compatibility/regression surfaces.

## Compatibility and migration boundary

A Core/profile `0.1` Project must not be silently rewritten as `0.2` during an ordinary compatible upgrade. Explicit `0.1` → `0.2` migration preserves Project identity and material durable truth, establishes exactly one initial logical lineage for the existing implicit continuity line, resolves backend selector binding separately when applicable, and verifies fresh Core/profile `0.2` discovery.

Repeated identical migration is a no-op; silent rebind to a different initial lineage is a conflict. Stale source state must not be overwritten.

## Self-host and operational provenance

The published RC release lineage uses logical lineage `urn:agnir:lineage:v0.2.0-rc.1` bound separately to `refs/heads/release/v0.2.0-rc.1`. During RC construction its applied operational-package baseline was immutable revision `bee78b2c9bb8c5ce5916d08691019dcde939b813`; this avoided impossible self-referential tag-SHA provenance.

Authoritative main now self-hosts Core/profile `0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`, and can truthfully record the already-published immutable operational package `0.2.0-rc.1` at tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

Project identity remains `urn:agnir:project:agnir-core`; declared State/Next/Decisions/Evidence locators remain unchanged.

## Release and main-acceptance evidence

Major successful receipts:

- RC self-host migration `a72654060c21600e1b7a4345634e09f9222ca4fb`, run `33654332505`;
- synchronized RC Skill/contracts `1ccede8d0f31565231dc05495a9c519ef5a45bc2`, run `33673748474`;
- fresh install + exact published-v0.1.1 migration fixture `b6fde55e525f4a077a070e1cf181304a3dfd7a9d`, run `33673869587`;
- operational package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813`, run `33673892651`;
- real repository migration from immutable published `v0.1.1`, validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97`, run `33674731595`;
- final prepublication candidate `79f8eb071d0b29bc4505d3448550c55619bd7cc9`, run `33675222129`;
- exact published tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`, publication/conformance run `33675638723`;
- post-publication release checkpoint `df745e2486b1d3f5ab2b07e701a9a6f91451a056`, run `33676002813`;
- release hygiene checkpoint `866604c4532003538fd6a0b565be9c1ef1c8a034`, run `33676171048`;
- reconciled main candidate `cd0427d26dddfabae768bcd76b78dc8d042151c7`, tree `8c931fe53c09b019fd7bfd964c2ebc5d2b02dcd0`;
- candidate-tree PR run `33705224034`, success;
- authoritative-main run `33705292185`, success.

`conformance/test_rc_release_gates.py` anchors the exact published `v0.1.1` manifest blob `0d26a9ffb947f551af335963ef753e7c0758c505`, proves a genuinely fresh Core `0.2` installation, and proves explicit migration/fresh resume while preserving Project identity and durable memory bytes.

Detailed durable evidence includes:

- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-release-gates.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-mechanism.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-result.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-main-reconciliation.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-main-integration-completed.md`.

## Publication and main acceptance result

**RC publication passed.** Workflow `33675638723` ran complete conformance on exact revision `50a8cd...`; only after success did its dependent publication job create/verify tag `v0.2.0-rc.1` and Release id `381532232` as prerelease/non-draft.

**Authoritative-main acceptance passed.** The staged target-first two-parent candidate `cd0427d...` was validated before main moved. Fresh target/source reads remained unchanged, then main advanced once directly to the exact candidate. Main push run `33705292185` passed the complete Core/profile/VCS/migration/full-suite surface; the prerelease publication job was skipped.

## Known limitations and next boundary

Real mount-boundary behavior remains explicitly unproven because no genuine mount-capable conformance environment has been supplied. Execution-surface persistence/configuration remains adapter behavior outside Core.

No release-blocking defect is currently known from the completed RC publication, real migration, Svif consumer, staged integration, and authoritative-main verification gates. Stable `v0.2.0` readiness must nevertheless be evaluated explicitly against the release/milestone/versioning contracts before constructing a stable candidate; the RC's existence alone does not make stable publication automatic.
