# Agnir Current State

Agnir `v0.2.0-rc.1` is formally published as a **prerelease**. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Published RC — 2026-09-03

- tag: `v0.2.0-rc.1`
- immutable tag target: `50a8cd565954e7e8055b8b628e2d620ac7357bab`
- GitHub Release id: `381532232`
- Release title: `Agnir v0.2.0-rc.1`
- `prerelease`: true
- `draft`: false
- published at: `2026-09-02T19:50:04Z`
- publication/conformance workflow: `33675638723`

The complete conformance job passed on the exact tag target before the dependent publication job created and verified the tag/release. External reads confirmed the tag points directly to `50a8cd...` and GitHub `releases/latest` still resolves to stable `v0.1.1` Release id `380414987`.

Post-publication continuity checkpoint `df745e2486b1d3f5ab2b07e701a9a6f91451a056` recorded the newly knowable publication receipts and passed fresh conformance run `33676002813`. The immutable RC tag remains at the earlier publication target and is not redefined by later checkpoints.

## RC compatibility contract

- repository SemVer: `0.2.0-rc.1`
- Core: `0.2`
- profile: `repository-filesystem/0.2`
- Project: `urn:agnir:project:agnir-core`
- logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`
- selector: `refs/heads/release/v0.2.0-rc.1`
- applied operational-package baseline: `bee78b2c9bb8c5ce5916d08691019dcde939b813`

Normative RC contracts are `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, and `schemas/agnir-manifest-0.2.schema.json`.

## Verification and validation hygiene

Prepublication evidence includes fresh Core `0.2` install, exact published-v0.1.1 manifest migration, and a real-repository migration starting directly from immutable `v0.1.1`. Validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97` passed run `33674731595`.

Draft PR #7, which existed only as a non-merge validation surface, was closed after the real validation receipts were captured. It remains `merged=false`; no validation PR merge changed the release or authoritative branches.

The validation refs themselves remain temporary. The currently connected GitHub mutation surface exposes branch create/update but no delete-ref operation, so they have not been falsely reported as deleted. Their immutable commits/runs remain durable Evidence until a safe retirement path is available.

## Current boundary

The next engineering phase is RC observation/stabilization and later safe reconciliation of accepted RC changes back into authoritative `main`. `main` did not move during RC publication. Final stable `v0.2.0` is a separate publication decision and must not be inferred from RC success.
