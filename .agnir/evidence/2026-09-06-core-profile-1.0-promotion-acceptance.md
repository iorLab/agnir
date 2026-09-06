# Core/Profile 1.0 Promotion Acceptance — 2026-09-06

## Scope

This evidence records acceptance of the deliberate semantics-preserving promotion machinery from accepted Core/profile `0.2` behavior to Core `1.0` + `repository-filesystem/1.0`. It does **not** record publication of repository `v1.0.0`, and it does not relabel the authoritative `main` Project from Core/profile `0.2`.

## Tracking

- issue: #27 `v1: promote Core/profile 0.2 semantics to stable 1.0`
- pull request: #28 `v1: begin Core/profile 1.0 stability promotion`
- working branch: `promotion/core-profile-1.0`
- authoritative target: `main`

## Accepted contract surfaces

- `spec/AGNIR_CORE_1_0.md`
- `profiles/REPOSITORY_FILESYSTEM_1_0.md`
- `schemas/agnir-manifest-1.0.schema.json`
- `spec/CORE_0_2_TO_1_0_PROMOTION.md`
- `conformance/core_1_0_reference.py`
- `conformance/repository_filesystem_1_0_reference.py`
- `conformance/repository_filesystem_1_0_promotion_reference.py`
- `conformance/check_agnir_1_0.py`
- direct Core/profile 1.0 and 0.2→1.0 promotion tests
- composed 0.1→0.2→1.0 coverage
- README/Skill/versioning/repository-map/package/CI surfaces required to expose and verify the multi-version model.

## Promotion invariants verified by the candidate

- Core/profile 1.0 are a stability promotion of accepted 0.2 semantics, not a semantic redesign.
- Existing valid Core/profile 0.2 Projects remain supported and are not forcibly rewritten by a 1.0 distribution.
- A Project compatibility declaration changes 0.2→1.0 only through explicit authorization.
- Promotion preserves Project identity, logical lineage identity, durable memory semantics/content/locators, policy, unrelated extensions, and unrelated Project content unless separately authorized.
- Same-target repeat is a no-op.
- Stale/conflicting promotion fails rather than overwriting newer truth.
- Fresh exact 1.0 resolve is required after promotion publication.
- Historical Core/profile 0.1 and 0.2 normative contracts remain unchanged.
- 0.1→1.0 composition preserves the explicit 0.1→0.2 migration boundary before 0.2→1.0 promotion.

## Exact receipts

- final promotion candidate revision: `dfc1af9203673cfc2aa41633143c4c90e274c976`
- exact-head PR conformance run: `34020641603` — success
- squash merge revision on authoritative `main`: `0337be5c0ef5ccd74d207135646b30947c275776`
- authoritative-main push conformance run: `34025528147` — success
- authoritative-main lineage at acceptance: `urn:agnir:lineage:authoritative`
- authoritative selector: `refs/heads/main`

The main verification run executed repository self-host cold start, Core 0.1 regressions, Core 0.2 continuity/discovery/migration, Core 1.0 stability semantics, repository-filesystem 1.0 discovery, explicit 0.2→1.0 promotion, VCS lineage binding, stable v0.2 package gates, and the full conformance suite successfully.

## Release boundary after acceptance

The authoritative Project remains:

- repository version: `0.2.0`
- Core compatibility: `0.2`
- discovery profile: `repository-filesystem/0.2`
- lineage: `urn:agnir:lineage:authoritative`

The next distinct release stage is an explicit `release/v1.0.0-rc.1` lineage. That lineage will intentionally promote its own self-host declaration to Core/profile `1.0`, set repository RC metadata, run exact-source RC gates, and only then arm immutable prerelease publication. Stable `v1.0.0` remains blocked on a clean RC evidence cycle.
