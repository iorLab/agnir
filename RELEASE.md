# Agnir 0.2.0 Stable Release

**Repository version:** `0.2.0`

**Core compatibility line:** `0.2`

**Repository/filesystem profile:** `repository-filesystem/0.2`

## Status

This source tree is the stable `v0.2.0` release line. Publication is complete only when an immutable `v0.2.0` tag resolves to the exact verified publication candidate and a non-draft, non-prerelease GitHub Release exists for that tag.

Before that publication succeeds, the latest published stable release remains `v0.1.1` at `e9712357ab590e5c1e5357b3cf3219d07d789aff`. After successful stable publication, `v0.2.0` must become GitHub `releases/latest` and the tag must remain immutable.

Repository SemVer promotion from `0.2.0-rc.1` to `0.2.0` does not introduce another Core/profile compatibility change. Core remains `0.2`; the profile remains `repository-filesystem/0.2`.

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

A conforming `0.1` → `0.2` migration:

1. activates and captures the existing Project identity, durable continuity, memory locators, and relevant backend receipt;
2. preserves Project identity and material State / Next Actions / Decisions / Evidence;
3. establishes exactly one initial logical Continuity Lineage for the former implicit continuity line;
4. resolves VCS/backend selector binding separately from logical lineage identity where applicable;
5. publishes the full Core/profile `0.2` candidate coherently;
6. rejects stale source state rather than overwriting newer truth;
7. fresh-resolves Core/profile `0.2`, the same Project identity, and intended lineage;
8. is idempotent for the same resulting lineage and fails conflicting silent rebinds.

The concrete release gates anchor the exact published `v0.1.1` manifest blob `0d26a9ffb947f551af335963ef753e7c0758c505` and preserve durable memory bytes across migration.

## Activation and Skill boundary

Root `SKILL.md` is the canonical Agent-facing install / initialize / migrate / upgrade / resume / checkpoint / commit / push / lineage-integration / repair procedure. User-facing install and stable-upgrade requests remain short.

An initialized repository Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → selected durable continuity. Execution-surface bootstrap remains locator-only adapter behavior outside Agnir Core and outside Project-owned durable memory.

`latest stable` resolution must use an actually published stable release. A moving branch, RC, or untagged commit must not be silently substituted.

## Release evidence

The `v0.2.0` milestone requires Core `0.2` design, migration, dual-backend conformance, and real-Project validation. The accepted evidence includes:

- Core `0.2` design and executable lineage-selection/integration semantics;
- non-VCS transactional SQLite lineage conformance;
- VCS selector/binding, fork/rebind and staged-integration conformance;
- semantic and repository/filesystem concrete `0.1` → `0.2` migration;
- genuinely fresh Core `0.2` installation and cold start;
- exact published-v0.1.1 manifest-shape migration/fresh resume;
- a real repository migration starting directly from immutable `v0.1.1`;
- real consumer/Project evidence from Svif during Core `0.2` validation;
- immutable `v0.2.0-rc.1` publication at `50a8cd565954e7e8055b8b628e2d620ac7357bab`, Release id `381532232`;
- safe target-first reconciliation of the accepted RC into authoritative main at `cd0427d26dddfabae768bcd76b78dc8d042151c7`;
- authoritative-main Core `0.2` verification and post-acceptance checkpoint run `33705538455`.

Detailed durable release-readiness evidence is recorded under `.agnir/evidence/`, including `2026-09-03-v0.2.0-stable-candidate.md`.

## Stable publication gate

Stable publication must use an exact verified candidate and must not be triggered by an ordinary branch push.

Required publication checks:

1. exact release ref is `refs/heads/release/v0.2.0`;
2. repository `VERSION` is `0.2.0`;
3. Core/profile declarations are `0.2` / `repository-filesystem/0.2`;
4. stable normative contract/status markers are present;
5. fresh install and exact published-v0.1.1 migration/fresh-resume gates pass;
6. complete conformance suite passes on the exact publication candidate;
7. tag `v0.2.0` is created only if absent, or must already point to the same exact SHA;
8. GitHub Release is created/verified with `prerelease=false` and `draft=false`;
9. GitHub `releases/latest` resolves to `v0.2.0` after publication.

The final publication candidate may record an already verified immutable stable operational-package baseline as `extensions.agnir/operations.applied_revision`. It must not attempt impossible self-referential provenance by embedding its own future SHA into the content that determines that SHA.

## Known limitations

Real mount-boundary behavior remains explicitly unproven because no genuine mount-capable conformance environment has been supplied. Execution-surface persistence/configuration remains adapter behavior outside Core.

These limitations remain documented; neither is a declared `v0.2.0` milestone blocker. Broader backend/surface evidence and long-term compatibility commitments continue toward `v1.0.0` under `V1_RELEASE_CRITERIA.md`.
