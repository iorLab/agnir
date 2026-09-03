# Agnir Current State

Agnir `v0.2.0-rc.1` is formally published as a **prerelease** at immutable tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`. GitHub Release id `381532232` remains `prerelease=true`, `draft=false`; `releases/latest` still resolves to stable `v0.1.1`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Authoritative main RC acceptance completed — 2026-09-03

Accepted RC Project/package changes have been reconciled into authoritative `main` through the Core 0.2 target-publication path.

Exact authoritative-main integration revision: `cd0427d26dddfabae768bcd76b78dc8d042151c7`.

- first parent: previous authoritative main `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`;
- second parent: accepted release-line head `866604c4532003538fd6a0b565be9c1ef1c8a034`;
- exact integrated tree: `8c931fe53c09b019fd7bfd964c2ebc5d2b02dcd0`.

Validation-only Draft PR #9 produced synthetic merge `406236beb1b8de212c218d899914b5cfd89f82c0`; its tree was exactly the same `8c931fe5...` as the staged candidate. Candidate-tree conformance run `33705224034` passed Core 0.2 self-host, stable Core/profile 0.1 regression pressure, VCS/lineage/profile/migration gates, RC fresh-install/published-migration gates, and the full suite while main remained unchanged.

Immediately before publication, fresh reads still observed main at `f0b2cbd...`, release source at `866604c...`, and the integration ref at `cd0427d...`. Main then advanced once directly to exact candidate `cd0427d...`; no release-line-continuity-first or follow-up-repair interval occurred.

Authoritative-main push run `33705292185` passed the same complete conformance surface. The prerelease publication job was correctly skipped on main.

PR #9 was automatically recognized by GitHub as merged through ancestry when main advanced to the exact candidate. No GitHub PR merge action created a different publication revision.

## Authoritative main Core 0.2 self-host

Project identity remains `urn:agnir:project:agnir-core` and declared durable memory locators remain unchanged.

Authoritative main now self-hosts Core `0.2` / `repository-filesystem/0.2` on logical Continuity Lineage `urn:agnir:lineage:authoritative`, separately bound to selector `refs/heads/main`. The logical lineage identity is not derived from the ref or commit receipt.

This is the explicit migration of main's former Core/profile `0.1` implicit line into one Core/profile `0.2` logical lineage. `extensions.agnir/operations` records the accepted immutable published RC package `0.2.0-rc.1` at revision `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

## Release boundary

- repository source line on main: `0.2.0-rc.1`;
- Core compatibility: `0.2`;
- profile: `repository-filesystem/0.2`;
- immutable prerelease: `v0.2.0-rc.1` at `50a8cd...`;
- latest stable remains `v0.1.1` until an actual stable `v0.2.0` publication;
- no release-blocking defect is known from the RC publication/main-acceptance gates completed so far;
- final stable `v0.2.0` remains a separate exact-candidate decision and publication.

Detailed reconciliation evidence is in `.agnir/evidence/2026-09-03-v0.2.0-rc.1-main-reconciliation.md`; completion receipts are in `.agnir/evidence/2026-09-03-v0.2.0-rc.1-main-integration-completed.md`. `.agnir/next-actions.md` is the canonical resume order.
