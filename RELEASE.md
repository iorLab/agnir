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

The latest published **stable** release remains `v0.1.1`, exact tag target `e9712357ab590e5c1e5357b3cf3219d07d789aff`, GitHub Release id `380414987`. Post-publication verification of GitHub `releases/latest` still returned `v0.1.1`; the RC therefore does not change `latest stable` upgrade resolution.

This file on the moving release branch records post-publication facts. The immutable RC tag remains at `50a8cd...`; later branch checkpoints do not redefine it.

## Version model

Agnir keeps distinct version layers:

- repository SemVer: `0.2.0-rc.1`;
- Core compatibility: `0.2`;
- repository/filesystem compatibility: `repository-filesystem/0.2`;
- VCS/adapter extension identifiers remain separately versioned where applicable.

Core/profile `0.2` is a compatibility-line change from `0.1`, not a compatible operational patch.

## Core 0.2 RC contract

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

The former competing `_DRAFT` Core/profile files are not active RC contracts.

## Skill and activation boundary

Root `SKILL.md` is the canonical Agent-facing install / migrate / upgrade / resume / checkpoint / commit / push / integration / repair procedure. User-facing install and stable-upgrade requests remain short.

Project activation remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → selected durable continuity. Execution-surface bootstrap remains locator-only adapter behavior outside Agnir Core and outside Project durable memory.

## Compatibility and migration boundary

A Core/profile `0.1` Project must not be silently rewritten as `0.2` during an ordinary compatible upgrade. Explicit `0.1` → `0.2` migration preserves Project identity and material durable truth, establishes exactly one initial logical lineage for the existing implicit continuity line, resolves backend selector binding separately when applicable, and verifies fresh Core/profile `0.2` discovery.

Repeated identical migration is a no-op; silent rebind to a different initial lineage is a conflict. Stale source state must not be overwritten. Core/profile `0.1` specifications, schemas, reference models, and regression tests remain available as compatibility surfaces.

## RC self-host and operational provenance

The release lineage uses:

- Project: `urn:agnir:project:agnir-core`;
- logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`;
- selector: `refs/heads/release/v0.2.0-rc.1`.

The applied operational Skill/documentation/conformance package baseline is immutable revision `bee78b2c9bb8c5ce5916d08691019dcde939b813`. `extensions.agnir/operations` records this actual applied revision. The final tagged candidate later records that baseline; it does not attempt impossible self-referential SHA provenance.

## Release evidence

Major successful verification receipts:

- Core `0.2` self-host migration `a72654060c21600e1b7a4345634e09f9222ca4fb`, run `33654332505`;
- synchronized RC Skill/contracts `1ccede8d0f31565231dc05495a9c519ef5a45bc2`, run `33673748474`;
- fresh install + exact published-v0.1.1 migration fixture `b6fde55e525f4a077a070e1cf181304a3dfd7a9d`, run `33673869587`;
- operational package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813`, run `33673892651`;
- real repository migration from immutable published `v0.1.1`, validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97`, run `33674731595`;
- final prepublication candidate `79f8eb071d0b29bc4505d3448550c55619bd7cc9`, run `33675222129`;
- exact published tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`, publication/conformance run `33675638723`.

`conformance/test_rc_release_gates.py` anchors the exact published `v0.1.1` manifest blob `0d26a9ffb947f551af335963ef753e7c0758c505`, proves a genuinely fresh Core `0.2` installation, and proves explicit migration/fresh resume while preserving Project identity and durable memory bytes.

The stronger real-repository validation starts directly from immutable `v0.1.1` tag target `e9712357...`; coherent migration revision `041f540a213c90e55d10e70aebaf14d8c1194a2a` has that published tag target as direct parent.

Detailed durable evidence:

- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-release-gates.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-mechanism.md`;
- `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-result.md`.

## Publication result

**Passed.** Workflow `33675638723` ran the complete conformance job on exact revision `50a8cd565954e7e8055b8b628e2d620ac7357bab`. Only after that job succeeded did its dependent publication job receive `contents:write`, create/verify lightweight tag `v0.2.0-rc.1`, and create/verify GitHub Release id `381532232` with `prerelease=true` and `draft=false`.

External post-publication reads independently confirmed the tag target and Release metadata. The tag is immutable by Project policy and must never move to a later branch checkpoint.

## Known limitations and next boundary

Real mount-boundary behavior remains explicitly unproven because no genuine mount-capable conformance environment has been supplied. Execution-surface persistence/configuration remains adapter behavior outside Core.

RC publication is not final stable `v0.2.0`. The next engineering phase is RC observation/stabilization and safe reconciliation of accepted release-line changes back into authoritative `main`; final stable publication is a separate decision.
