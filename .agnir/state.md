# Agnir Current State

Durable continuity belongs to the Project.

## Stable v1.0.1 publication

Agnir `v1.0.1` is now **published, verified, and the latest stable repository/distribution release**.

Accepted stable publication receipts:

- publication authorization: Principal command `发布 v1.0.1`;
- publication-arm / stable tag revision: `f56d25b22997c259c660651e7357334b063093e1`;
- immutable stable tag: `v1.0.1` -> `f56d25b22997c259c660651e7357334b063093e1`;
- GitHub Release id: `385176185`;
- Release state: non-draft, non-prerelease;
- published at: `2026-09-09T02:02:14Z`;
- publication workflow: `34301559338` — success;
- repository/conformance job: `102309347343` — success;
- stable publication job: `102309386242` — success;
- GitHub `releases/latest`: `v1.0.1`;
- previous stable `v1.0.0` remains exactly `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted `v1.0.0-rc.1` remains exactly `092945289f1a0a9803e4fe0583104aa380ceaadc`.

Repository/distribution `1.0.1` is a PATCH-level activation/packaging hardening over `1.0.0`. Core remains `1.0`; repository/filesystem remains `repository-filesystem/1.0`; historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported.

The accepted `1.0.1` packaging/operation result is:

- root `AGNIR.md` is the canonical Executor-facing Project activation + operation surface;
- `AGENTS.md` remains locator-only and points directly to `AGNIR.md`;
- README `Agnir Project Instructions` remains a backward-compatible locator for pre-upgrade `1.0.0` Projects, not a second procedure copy;
- legacy `AGENTS.md -> README` activation remains available only as safe pre-upgrade/repair input for existing `1.0.0` Projects;
- repository-context `commit` / `提交` / `提交代码` dispatches checkpoint evaluation before commit;
- `commit and push` / `提交推送` adds push + destination-ref verification;
- checkpoint evaluation remains distinct from forced `.agnir/` mutation, so unchanged durable truth is still a valid no-op;
- Project-defined pre-commit verification remains Project policy, not Agnir Core semantics.

`VERSION`, `AGNIR.yaml extensions.agnir/release.repository_version`, and `agnir/operations.release` now all reconcile to repository/distribution `1.0.1`; `agnir/operations.applied_revision` records the immutable stable source revision `f56d25b22997c259c660651e7357334b063093e1`.

## Publication metadata observation

The GitHub Release body has one cosmetic omission: the intended literal `` `AGNIR.md` `` was consumed by shell command substitution in the publication workflow's unquoted heredoc, leaving that filename absent from one sentence. Release identity, source/tag revision, latest-stable resolution, draft/prerelease state, package contents, and conformance are unaffected.

This is a repository-host presentation defect, not a package-integrity or protocol defect. It must not be repaired by moving/recreating the published tag. A future authorized host-metadata edit may correct only the Release body while preserving release identity.

## Public product state

The Principal-approved Agnir brand identity remains canonical under `brand/`. The bilingual README/website, scoped GitHub Pages publication, transparent render-self-contained brand surfaces, Apache-2.0 licensing, bilingual contribution guidance, repository topics/homepage, and GitHub Issues feedback intake remain accepted public surfaces on authoritative `main`.

The public product category remains **Project Continuity**. The first-user value remains fresh-session recovery: **the Project persists; Executors come and go**. `adoption/README.md` remains canonical launch/adoption strategy.

Svif remains the first accepted real-project post-1.0 adoption case. External cold-start resumes, external design users, cross-Executor cases, and independently built integrations remain the highest-value next adoption evidence.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical Continuity Lineage identity != selector/binding != revision/checkpoint receipt.
- A checkpoint is reconciliation of durable Project truth, not an activity log.
- Unchanged durable truth is a checkpoint no-op.
- Published tags are immutable.
- `latest stable` is determined by actual publication, not a moving source branch or candidate version.
- Core/profile compatibility identifiers are not silently rewritten by a distribution upgrade.
- `AGNIR.md` is a Project activation/operation packaging surface and does not redefine Agnir Core.
- README, website, brand, adoption strategy, repository-host metadata, and execution-surface configuration are not Core semantic dependencies.
