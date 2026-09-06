# Agnir Current State

Agnir `v0.2.0` remains the published latest stable release. This selected continuity is the temporary `v1.0.0-rc.1` release lineage, forked from verified authoritative checkpoint `11148c3063e63dd1ea7450b9d538ac1eccec5639` and intentionally promoted to Core `1.0` + `repository-filesystem/1.0` for exact RC verification.

Durable continuity belongs to the Project. Project identity remains `urn:agnir:project:agnir-core`; this lineage identity is `urn:agnir:lineage:v1.0.0-rc.1`, separately bound to `refs/heads/release/v1.0.0-rc.1`.

## Accepted baseline

- latest stable: `v0.2.0` → `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- independent-implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion candidate: issue #27 / PR #28 accepted;
- final promotion candidate: `dfc1af9203673cfc2aa41633143c4c90e274c976`, run `34020641603` success;
- promotion merge to authoritative main: `0337be5c0ef5ccd74d207135646b30947c275776`, run `34025528147` success;
- canonical promotion checkpoint: `11148c3063e63dd1ea7450b9d538ac1eccec5639`, run `34025693977` success.

## RC lineage state

- repository version: `1.0.0-rc.1`;
- Core compatibility: `1.0`;
- profile: `repository-filesystem/1.0`;
- logical lineage: `urn:agnir:lineage:v1.0.0-rc.1`;
- selector: `refs/heads/release/v1.0.0-rc.1`;
- exact verified candidate revision: `e4d5ad8f7e4013314401ecf3d987edb66f509ce5`;
- exact verified candidate run: `34026056687` success;
- publication status: **candidate-verified, not armed**;
- immutable RC tag/release: **not yet created by this lineage**;
- stable publication: **not authorized by RC existence**.

The first true RC-source runs exposed two brittle self-host marker defects before the full suite could execute: run `34025848630` failed on the literal Core marker `coherent target publication`; run `34025962753` then failed on the promotion marker `logical Continuity Lineage identity`. The first was resolved by a non-behavioral terminology clarification in Core 1.0; the second by making the self-host gate match the contract's actual normative term `logical lineage identity`. Neither failure exposed a resolver, checkpoint, lineage, migration, promotion, or compatibility semantic defect.

Run `34026056687` is the first complete exact `VERSION=1.0.0-rc.1` candidate run to pass repository self-host cold start, Core 0.1 regressions, Core/profile 0.2 regressions and migration, Core/profile 1.0 stability/discovery, explicit 0.2→1.0 promotion, VCS lineage binding, and the full `test_*.py` suite. The version-specific v0.2 stable-package gate correctly skipped on the RC source, and the publication job remained skipped because the arm commit does not yet exist.

The next operation is to verify the checkpointed candidate source itself. Only if that exact checkpoint is also green may publication be armed.
