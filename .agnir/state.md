# Agnir Current State

Agnir `v0.1.1` remains the latest formally published **stable** repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## v0.2.0-rc.1 publication-armed candidate — 2026-09-03

Temporary branch `release/v0.2.0-rc.1` self-hosts Core `0.2` / `repository-filesystem/0.2` for Project `urn:agnir:project:agnir-core` on logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, separately bound to selector `refs/heads/release/v0.2.0-rc.1`.

The RC normative contracts, bilingual READMEs, Skill, migration contract, schema, release-gate fixtures, and real published-v0.1.1 migration evidence are synchronized. Operational provenance truthfully records immutable applied RC package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813`.

Final pre-publication candidate `79f8eb071d0b29bc4505d3448550c55619bd7cc9` passed exact-head GitHub Actions run `33675222129`: RC self-host, stable Core `0.1` regressions, VCS/lineage/profile pressure, semantic/concrete migration, fresh Core `0.2` install, exact published-v0.1.1 migration fixture, and full suite all succeeded.

Real-repository migration from immutable published `v0.1.1` also passed on validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97`, run `33674731595`.

## Publication mechanism

Because the connected GitHub write surface does not expose direct tag/release creation, the repository conformance workflow now contains a narrowly scoped publication job. It has `contents:write` only after the ordinary `repository-filesystem` conformance job succeeds and only when all of these are true:

- event is a push;
- ref is exactly `refs/heads/release/v0.2.0-rc.1`;
- head commit message is exactly `rc: arm v0.2.0-rc.1 publication`.

The publication job is fail-closed and idempotent: an existing tag must already point at the exact workflow SHA or publication fails; a correctly created tag is never moved; an existing Release must match the tag; final verification requires tag SHA = workflow SHA, `prerelease=true`, and `draft=false`.

This checkpoint arms that one publication event but does **not** pre-claim its result. The commit containing this state and publication workflow must first pass the complete conformance job; only then may its dependent job create immutable `v0.2.0-rc.1` and the GitHub prerelease. `v0.1.1` remains latest stable.

After publication succeeds, the release branch must record the actual tag target, Release id, and workflow receipt in a later post-publication checkpoint without changing the tag. `main` is not moved by RC publication.
