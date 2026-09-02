# Agnir Current State

Agnir `v0.1.1` remains the latest formally published **stable** repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Active v0.2.0-rc.1 release lineage — 2026-09-03

Temporary branch `release/v0.2.0-rc.1` is the release-candidate evidence carrier forked from verified authoritative-main checkpoint `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.

Project identity remains `urn:agnir:project:agnir-core`. This branch explicitly self-hosts Core `0.2` / `repository-filesystem/0.2` on logical Continuity Lineage `urn:agnir:lineage:v0.2.0-rc.1`, separately bound to selector `refs/heads/release/v0.2.0-rc.1`. Selector and revision receipt are not lineage identity.

The self-host migration preserves the inherited durable truth and existing `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/` locators from the verified main baseline. Migration evidence is recorded in `.agnir/evidence/2026-09-03-v0.2.0-rc.1-self-host-migration.md`.

## RC contract and operational documentation synchronized

The RC normative compatibility candidates are now:

- `spec/AGNIR_CORE_0_2.md` — Core `0.2`;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md` — `repository-filesystem/0.2`;
- `spec/CORE_0_1_TO_0_2_MIGRATION.md` — explicit `0.1`→`0.2` migration;
- `schemas/agnir-manifest-0.2.schema.json` — manifest contract.

`README.md`, `README.zh-CN.md`, root `SKILL.md`, `REPOSITORY_TREE.md`, and durable Decisions have been synchronized to the RC model:

- Core `0.2` Continuity Lineages are no longer described as deferred;
- Project identity, logical lineage identity, VCS selector/binding, and revision receipt are separated consistently;
- stable `latest stable` resolution still points to published `v0.1.1` until final `v0.2.0` publication;
- an explicitly authorized RC target may install/migrate to Core/profile `0.2` through the explicit migration contract;
- user-facing install/upgrade prompts remain short;
- non-destructive `AGENTS.md` / README activation and execution-surface handoff semantics are preserved;
- lineage integration uses staged target reconciliation/coherent publication;
- repository structure now exposes the normative RC contracts and RC self-host checker.

The former `_DRAFT` Core/profile documents are no longer active compatibility contracts and are removed from the RC source tree. Historical Evidence and Git history may still name them because those references describe earlier development checkpoints accurately.

## RC self-host verification baseline

Self-host migration revision `a72654060c21600e1b7a4345634e09f9222ca4fb` passed exact-head release-branch CI run `33654332505`:

- RC Core `0.2` self-host cold start: success;
- stable Core/profile `0.1` regression: success;
- VCS branch continuity: success;
- Core `0.2` non-VCS and VCS mapping: success;
- repository-filesystem `0.2`: success;
- VCS lineage binding: success;
- semantic + concrete `0.1`→`0.2` migration: success;
- full suite: success.

The current documentation/Skill synchronization checkpoint must now pass the same exact-head gate before the RC package is treated as candidate-ready.

## Operational provenance boundary

`extensions.agnir/operations` still records the actually applied published operational package `v0.1.1` at `e9712357...`. This is intentional: an immutable RC `applied_revision` cannot truthfully be recorded until the full RC package has an exact verified candidate revision.

After documentation/Skill conformance is green, the next material boundary is to construct an exact RC candidate, use its immutable revision for fresh-install and real migration/resume validation, then record the actual applied RC provenance coherently before tagging.

## Remaining RC gates

1. pass exact-head CI for the synchronized docs/Skill/draft cleanup checkpoint;
2. construct one exact RC candidate revision with truthful `agnir/operations` provenance;
3. validate a genuinely fresh Project installation against that exact RC candidate;
4. validate at least one explicitly authorized real Project migration from published `v0.1.1` / Core/profile `0.1` to `0.2`, preserving Project identity/durable truth and passing fresh resume;
5. re-run exact-candidate conformance;
6. tag/publish immutable `v0.2.0-rc.1` as a prerelease only after all gates pass.

Do not present the RC as `latest stable`. Do not move the RC tag after publication. `.agnir/next-actions.md` is the ordered resume plan.
