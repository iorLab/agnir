# Agnir Current State

Agnir `v0.1.1` remains the latest formally published **stable** repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## v0.2.0-rc.1 final-candidate preparation — 2026-09-03

Temporary branch `release/v0.2.0-rc.1` self-hosts Core `0.2` / `repository-filesystem/0.2` for Project `urn:agnir:project:agnir-core` on logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, separately bound to selector `refs/heads/release/v0.2.0-rc.1`.

The RC normative contracts are `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, and `schemas/agnir-manifest-0.2.schema.json`. The former competing `_DRAFT` Core/profile files are absent from the active RC tree. Both READMEs, root `SKILL.md`, repository structure documentation, and executable conformance describe the same lineage-aware RC model while preserving Core/profile `0.1` regression surfaces.

## Verified RC package and release gates

The RC operational package baseline is immutable revision `bee78b2c9bb8c5ce5916d08691019dcde939b813`. `extensions.agnir/operations` now records repository release `0.2.0-rc.1` with that actual applied revision; this deliberately avoids pretending that a commit can contain its own future SHA.

Verified receipts:

- self-host migration `a72654060c21600e1b7a4345634e09f9222ca4fb` — CI `33654332505` success;
- canonical Skill wording / synchronized RC package `1ccede8d0f31565231dc05495a9c519ef5a45bc2` — CI `33673748474` success;
- executable fresh-install + exact published-v0.1.1 manifest migration fixture `b6fde55e525f4a077a070e1cf181304a3dfd7a9d` — CI `33673869587` success;
- dedicated RC fresh-install / published-v0.1.1 migration gate at package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813` — CI `33673892651` success;
- real-repository migration validation begins from immutable `v0.1.1` tag target `e9712357ab590e5c1e5357b3cf3219d07d789aff`; coherent migration revision `041f540a213c90e55d10e70aebaf14d8c1194a2a` preserves Project identity and published durable receipts, establishes a distinct logical lineage + selector binding, and applies operational baseline `bee78b2...`;
- validation instrumentation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97` — CI `33674731595` success, including fresh validation-root Core `0.2` resume, stable Core `0.1` regression, VCS/lineage/profile/migration pressure, RC fixture, and full suite.

Two earlier validation runs (`33674632504`, `33674669670`) failed only because the validation-only inline Python step did not set `PYTHONPATH=conformance`. The validation workflow was corrected without changing Core/profile contracts, migration truth, or formal release-branch content; run `33674731595` then passed completely.

The exact published `v0.1.1` migration baseline is independently anchored by source manifest blob `0d26a9ffb947f551af335963ef753e7c0758c505`, source root tree `44003ec33d4dbc3606c34a5334027fe7aaf6f0e3`, and source `.agnir` tree `37b152659499c1079c796646dce23a8112660b6f`. Detailed release-gate evidence is recorded in `.agnir/evidence/2026-09-03-v0.2.0-rc.1-release-gates.md`.

## Publication boundary

All substantive RC gates before final-candidate verification are now satisfied. This checkpoint is the formal candidate-construction boundary: it records truthful operational provenance and the completed install/migration evidence, but **does not claim that `v0.2.0-rc.1` is published**.

Next, run the complete conformance workflow on the exact resulting candidate revision. Only if that exact revision passes may immutable tag `v0.2.0-rc.1` and a GitHub **prerelease** be created at that revision. The tag must never move, and the RC must not be presented as `latest stable`; published `v0.1.1` remains latest stable.

After publication, a later checkpoint may record the actual tag target, Release id, and publication verification without changing the immutable tag target. Reconciliation of the RC lineage back into authoritative `main`, and final stable `v0.2.0`, remain separate later decisions.
