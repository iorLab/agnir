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
- publication status: **candidate-unarmed**;
- immutable RC tag/release: **not yet created by this lineage**;
- stable publication: **not authorized by RC existence**.

The branch now exercises the exact 1.0 serialized identifiers while preserving the same Project identity and durable continuity model. The next operation is candidate verification. Publication must not be armed until the exact branch head is green across self-host and full conformance.
