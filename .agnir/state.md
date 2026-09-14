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

This is a repository-host presentation defect, not a package-integrity or protocol defect. It must not be repaired by moving/recreating the published tag. A future authorized metadata repair may update only the Release body while preserving release identity.

## Public product state

The Principal-approved Agnir brand identity remains canonical under `brand/`. The bilingual README/website, scoped GitHub Pages publication, transparent render-self-contained brand surfaces, Apache-2.0 licensing, bilingual contribution guidance, repository topics/homepage, and GitHub Issues feedback intake remain accepted public surfaces on authoritative `main`.

The public product category remains **Project Continuity**. The first-user value remains fresh-session recovery: **the Project persists; Executors come and go**. `adoption/README.md` remains canonical launch/adoption strategy.

The canonical fresh-session recovery demo remains under `adoption/demos/fresh-session/`, with `trace.json` as its deterministic presentation source. The first implementation from PR `#51` was technically valid and successfully published, but the first Principal visual review rejected the presentation because it read as independent slide/card replacement rather than a live Agent conversation. That review is accepted product evidence rather than being treated as cosmetic preference.

PR `#52` then replaced the scene-card player with one persistent Agent-workspace transcript. A subsequent Principal review preferred the stronger visual logic of the original static comparison: keep **Without Agnir** and **With Agnir** visible simultaneously, but make both sides dynamic. That direction is now accepted as the demo's current presentation contract rather than a return to slides.

PR `#53` implemented the synchronized split-screen v3. Desktop now shows two dynamic Agent-workspace windows at once: left **Without Agnir**, right **With Agnir**, driven by one shared playback clock. Both receive the same task, reach the same stopping point, create genuinely fresh Session B instances, and receive only `Continue.` / `继续。`; the left side stalls on missing durable context while the right side discovers Agnir, loads Project truth, completes the pending failure-path tests, and verifies them successfully. Narrow/mobile layouts stack the same two windows in Without-then-With order. The deterministic trace schema is `agnir.demo.split-screen/3`.

The split-screen implementation source head is `a74371b37f044af2837c7de3d4178f26cf299d8d`; PR `#53` merged at `64e61ad1f21d15362cedbfb8376ab1d0adb6343d`. PR conformance run `34819370697`, post-merge conformance run `34819425531`, and Pages build/deploy run `34819425549` all succeeded. Published Pages artifact `10338020626` has digest `sha256:50ae43bdc8d18e5ab05057fee5406fbb6c7f9282eb585109de34a5dbb94501de`. The published artifact was inspected directly: it contains `agnir.demo.split-screen/3`, both `without` / `with` event lanes, the split-lane renderer, two-column desktop CSS, and JavaScript that passes `node --check`. Human visual acceptance of this split-screen v3 remains the next observation.

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
