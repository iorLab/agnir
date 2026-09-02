# Agnir Current State

Agnir `v0.2.0-rc.1` is now formally published as a **prerelease**. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Published RC — 2026-09-03

- tag: `v0.2.0-rc.1`
- immutable tag target: `50a8cd565954e7e8055b8b628e2d620ac7357bab`
- tag object type: commit
- GitHub Release id: `381532232`
- Release title: `Agnir v0.2.0-rc.1`
- `prerelease`: true
- `draft`: false
- published at: `2026-09-02T19:50:04Z`
- publication/conformance workflow: `33675638723`

The workflow first passed the complete `repository-filesystem` conformance job on the exact tag target, then its dependent publication job created and verified the tag/release. External post-publication reads confirmed `refs/tags/v0.2.0-rc.1` resolves directly to `50a8cd...` and the Release metadata is prerelease/non-draft.

GitHub `releases/latest` still resolves to stable `v0.1.1` Release id `380414987`; therefore RC publication did not replace stable upgrade resolution.

## RC compatibility contract

- repository SemVer: `0.2.0-rc.1`
- Core: `0.2`
- profile: `repository-filesystem/0.2`
- Project: `urn:agnir:project:agnir-core`
- release-line logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`
- release-line selector: `refs/heads/release/v0.2.0-rc.1`
- applied operational-package baseline: `bee78b2c9bb8c5ce5916d08691019dcde939b813`

Normative RC contracts are `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, and `schemas/agnir-manifest-0.2.schema.json`.

## Verification evidence

Prepublication gates included RC self-host, stable Core `0.1` regression, Core `0.2` VCS/non-VCS/profile/binding/migration pressure, a genuinely fresh Core `0.2` install, exact published-v0.1.1 manifest migration, and a stronger real-repository migration starting directly from immutable published `v0.1.1`. The real validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97` passed run `33674731595`.

Final prepublication candidate `79f8eb071d0b29bc4505d3448550c55619bd7cc9` passed run `33675222129`. Publication-armed exact tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab` then passed the complete conformance job in run `33675638723` before its dependent publication job succeeded.

Durable receipts are recorded under `.agnir/evidence/2026-09-03-v0.2.0-rc.1-release-gates.md`, `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-mechanism.md`, and `.agnir/evidence/2026-09-03-v0.2.0-rc.1-publication-result.md`.

## Current boundary

The RC tag is immutable and must not be moved to this or any later checkpoint. This post-publication branch checkpoint records facts that only became knowable after publication; it does not redefine the release target.

`main` has not moved as part of RC publication. The next major engineering boundary is an RC observation/stabilization cycle followed by safe reconciliation of accepted RC changes back into authoritative `main`. Final stable `v0.2.0` is a separate publication decision and must not be inferred merely from RC success.
