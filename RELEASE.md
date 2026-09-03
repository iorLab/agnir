# Agnir 0.2.0 Stable Release

**Repository version:** `0.2.0`

**Core compatibility line:** `0.2`

**Repository/filesystem profile:** `repository-filesystem/0.2`

## Status

Agnir `v0.2.0` is published as the current **latest stable** repository release.

Publication receipts:

- immutable lightweight tag: `v0.2.0`;
- exact tag target: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id: `381710267`;
- Release `draft=false`;
- Release `prerelease=false` (non-prerelease stable release);
- publication/conformance workflow: `33711982062`;
- independent post-publication verification: GitHub `releases/latest` resolves to `v0.2.0`.

Published tags are immutable by Project policy. Later moving-branch checkpoints do not redefine the stable tag target.

Repository SemVer promotion from `0.2.0-rc.1` to `0.2.0` did not introduce another Core/profile compatibility change. Core remains `0.2`; the profile remains `repository-filesystem/0.2`.

## What v0.2.0 stabilizes

Repository `v0.2.0` publishes Continuity Lineages as the accepted Core `0.2` abstraction:

- one Project may own multiple independently advancing logical Continuity Lineages;
- Project identity and logical lineage identity are distinct;
- logical lineage identity is distinct from backend selector/locator and revision/checkpoint receipt;
- ordinary lineage-local work resolves exactly one selected lineage without sibling guessing;
- checkpoints are lineage-local by default;
- source continuity is integration input, not automatic target truth;
- Agnir-controlled integration stages without target advancement, reconciles target continuity, and publishes integrated Project state + reconciled target continuity coherently;
- stale source or target generations invalidate staged candidates;
- Core remains storage-, platform-, VCS-, Agent-, Skill-, and execution-surface-neutral.

Stable normative contracts:

- `spec/AGNIR_CORE_0_2.md`;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md`;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- `schemas/agnir-manifest-0.2.schema.json`.

Core/profile `0.1` artifacts remain present as supported compatibility/regression surfaces for existing published `v0.1.1` Projects and explicit migration testing.

## Migration from v0.1.1 / Core 0.1

A Core/profile `0.1` Project must not be silently rewritten to `0.2` by an ordinary compatible operational upgrade. The compatibility change requires explicit migration.

A conforming `0.1` → `0.2` migration preserves Project identity and material State / Next Actions / Decisions / Evidence, establishes exactly one initial logical Continuity Lineage for the former implicit continuity line, resolves selector/binding separately where applicable, rejects stale-source overwrite, and verifies a fresh Core/profile `0.2` resume.

Release conformance anchors the exact published `v0.1.1` manifest blob `0d26a9ffb947f551af335963ef753e7c0758c505` and verifies preserved durable memory bytes across migration.

## Activation and Skill boundary

Root `SKILL.md` is the canonical Agent-facing install / initialize / migrate / upgrade / resume / checkpoint / commit / push / lineage-integration / repair procedure. User-facing install and stable-upgrade requests remain short.

An initialized repository Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → selected durable continuity. Execution-surface bootstrap remains locator-only adapter behavior outside Agnir Core and outside Project-owned durable memory.

`latest stable` resolution uses an actually published stable release. A moving branch, RC, or untagged commit must not be silently substituted.

## Release evidence

The `v0.2.0` milestone required Core `0.2` design, explicit migration, materially different VCS and non-VCS backend conformance, fresh install/resume, and real-Project validation. Accepted evidence includes:

- non-VCS transactional SQLite lineage conformance;
- VCS selector/binding, fork/rebind and staged-integration conformance;
- semantic and repository/filesystem concrete `0.1` → `0.2` migration;
- genuinely fresh Core `0.2` installation and exact published-v0.1.1 migration/fresh resume;
- a real repository migration starting directly from immutable `v0.1.1`;
- real consumer/Project evidence from Svif;
- immutable `v0.2.0-rc.1` publication at `50a8cd565954e7e8055b8b628e2d620ac7357bab`, Release id `381532232`;
- safe RC acceptance into authoritative main and main verification;
- stable package baseline `f59a83754346982170142a355a01c94050ddf3a5`, workflow `33711830312` success;
- exact stable publication target `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, workflow `33711982062` success.

Detailed durable Evidence is under `.agnir/evidence/`, including `2026-09-03-v0.2.0-stable-candidate.md`, `2026-09-03-v0.2.0-stable-package-publication-candidate.md`, and `2026-09-03-v0.2.0-stable-publication-result.md`.

## Operational provenance

The stable operational-package baseline actually applied before the final publication transition is immutable revision `f59a83754346982170142a355a01c94050ddf3a5`. `extensions.agnir/operations.applied_revision` records that baseline.

The final stable tag target `fc84095...` is the publication receipt and exact released source tree. The package baseline and final tag target are deliberately distinct so provenance never requires an impossible self-referential SHA.

## Known limitations and next boundary

Real mount-boundary behavior remains explicitly unproven because no genuine mount-capable conformance environment has been supplied. Execution-surface persistence/configuration remains adapter behavior outside Core. Neither was a declared `v0.2.0` milestone blocker.

The next engineering boundary is safe reconciliation of the published stable result back into authoritative `main`, then broader real-Project/execution-surface evidence toward `v1.0.0` under `V1_RELEASE_CRITERIA.md`.
