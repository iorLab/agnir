# Agnir 1.0.0-rc.1 Release Candidate

**Repository version:** `1.0.0-rc.1`

**Core compatibility line:** `1.0`

**Repository/filesystem profile:** `repository-filesystem/1.0`

## Status

This source tree is the explicit `v1.0.0-rc.1` **release candidate lineage**. It is not a published stable release and is not publication-armed merely because the branch exists.

The current **latest stable** release remains immutable `v0.2.0` at `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`.

RC source origin:

- verified authoritative checkpoint: `11148c3063e63dd1ea7450b9d538ac1eccec5639`;
- checkpoint conformance run: `34025693977` success;
- release lineage: `urn:agnir:lineage:v1.0.0-rc.1`;
- selector binding: `refs/heads/release/v1.0.0-rc.1`.

## What this RC verifies

Core/profile `1.0` are a semantics-preserving stability promotion of the independently accepted Core/profile `0.2` behavior. This RC verifies the stable identifiers and release mechanics rather than introducing a new continuity model.

Normative contracts:

- `spec/AGNIR_CORE_1_0.md`;
- `profiles/REPOSITORY_FILESYSTEM_1_0.md`;
- `schemas/agnir-manifest-1.0.schema.json`;
- `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

Historical Core/profile `0.1` and `0.2` contracts remain supported compatibility/migration surfaces. A valid `0.2` Project is not silently rewritten to `1.0` by this distribution.

## Promotion boundary

The release lineage intentionally promotes its own self-host declaration from Core/profile `0.2` to `1.0` under the accepted promotion contract. The transition preserves Project identity, durable continuity semantics and locators, unrelated Project content, and the distinction between logical lineage identity and VCS selector.

This does not relabel authoritative `main`. The RC lineage has its own logical identity and selector binding.

## Activation and Skill boundary

Root `SKILL.md` remains the canonical Agent-facing install / initialize / migrate / compatibility-promotion / upgrade / resume / checkpoint / commit / push / lineage-integration / repair procedure.

An initialized repository Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → selected durable continuity. `latest stable` resolution still means an actually published non-prerelease release; this RC must not replace `v0.2.0` in ordinary stable-upgrade resolution.

## Candidate verification gate

Before publication can be armed, the exact RC candidate revision must pass:

- `python conformance/check_agnir_1_0.py`;
- Core 0.1 compatibility regression;
- Core/profile 0.2 compatibility and migration regression;
- Core/profile 1.0 stability/discovery/checkpoint/lineage coverage;
- explicit `0.2` → `1.0` promotion conformance;
- composed `0.1` → `0.2` → `1.0` coverage;
- VCS and non-VCS lineage/integration pressure;
- package/release gates;
- the full `test_*.py` suite.

Any release-blocking failure keeps the RC unarmed.

## Publication contract

Only a push to exact branch `release/v1.0.0-rc.1` whose head commit message is exactly:

`rc: arm v1.0.0-rc.1 publication`

may enter the publication job.

That job must verify exact source, exact Core/profile/lineage/selector metadata, and `check_agnir_1_0.py` before creating or validating immutable tag/release `v1.0.0-rc.1`.

After publication:

- tag target must equal the exact armed revision;
- Release must be `prerelease=true`, `draft=false`;
- GitHub `releases/latest` must still resolve to `v0.2.0`;
- the immutable RC source must receive a fresh evidence cycle before stable `v1.0.0` is considered.

## Promotion acceptance receipts

- issue #26 independent implementation: clean `PASS` against `eabc599d589f2c3dfe6b3d9508a093d120f33c95`;
- issue #27 / PR #28 promotion candidate: `dfc1af9203673cfc2aa41633143c4c90e274c976`;
- promotion candidate run: `34020641603` success;
- promotion merge to main: `0337be5c0ef5ccd74d207135646b30947c275776`;
- authoritative main verification: `34025528147` success;
- canonical promotion-acceptance checkpoint: `11148c3063e63dd1ea7450b9d538ac1eccec5639`, run `34025693977` success.
