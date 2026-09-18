# Agnir Current State

Durable continuity belongs to the Project.

## Stable v1.0.2 publication

Agnir `v1.0.2` is **published, verified, and the latest stable repository/distribution release**.

Accepted stable publication receipts:

- publication authorization: Principal command `发布v1.0.2` / `那就发布v1.0.2`;
- publication-arm / immutable stable tag revision: `b5626394ec40a5cb7a28c01892acde07cc0adc8e`;
- immutable stable tag: `v1.0.2` -> `b5626394ec40a5cb7a28c01892acde07cc0adc8e`;
- GitHub Release id: `391529372`;
- Release state: non-draft, non-prerelease;
- published at: `2026-09-18T14:14:18Z`;
- publication workflow: `35354941029` — success;
- repository/conformance job: `105631886209` — success;
- stable publication job: `105631955191` — success;
- GitHub `releases/latest`: `v1.0.2`;
- previous stable `v1.0.1` remains exactly `f56d25b22997c259c660651e7357334b063093e1`;
- `v1.0.0` remains exactly `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted `v1.0.0-rc.1` remains exactly `092945289f1a0a9803e4fe0583104aa380ceaadc`.

Repository/distribution `1.0.2` is a PATCH-level execution-surface onboarding/packaging hardening over `1.0.1`. It publishes the Principal-accepted locator-only ChatGPT Project handoff while leaving Core `1.0`, `repository-filesystem/1.0`, Project identity, Continuity Lineage, checkpoint semantics, and historical compatibility lines unchanged.

The accepted persistent ChatGPT Project handoff is:

```text
Canonical Project: <owner/repository> (<ref>)
At the first substantive turn of every new conversation, open it, read root AGENTS.md, and follow it before doing Project work.
```

Continuity remains Project-owned behind `AGENTS.md -> AGNIR.md -> AGNIR.yaml -> selected durable continuity`; the surface instruction is only the durable locator into that route.

`VERSION`, `AGNIR.yaml extensions.agnir/release.repository_version`, and `agnir/operations.release` reconcile to repository/distribution `1.0.2`; `agnir/operations.applied_revision` records the immutable stable source revision `b5626394ec40a5cb7a28c01892acde07cc0adc8e`.

## Previous stable v1.0.1 publication

Agnir `v1.0.1` remains an **immutable previous stable release**. Its publication receipts remain historical evidence for the 1.0 line.

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

## v1.0.2 publication acceptance

The authorized PATCH release cycle is closed.

Release preparation PR `#60` merged to authoritative `main` at `72177afbbe4e36945366faaa9096b6d9bbb04d88`. Post-merge conformance run `35354894720`, repository job `105631729092`, succeeded while the v1.0.2 publication job was correctly skipped.

The separate zero-tree-change publication arm `b5626394ec40a5cb7a28c01892acde07cc0adc8e` used the exact commit message `release: publish v1.0.2 stable`. Workflow `35354941029` re-ran exact-source repository/full conformance, then publication job `105631955191` created and verified tag/Release/latest state.

Host readback confirms `refs/tags/v1.0.2` and Release `391529372` both target the exact arm revision, the Release is non-draft/non-prerelease, and `releases/latest == v1.0.2`. Immutable `v1.0.1`, `v1.0.0`, and `v1.0.0-rc.1` receipts remain unchanged.

The release branch has been retired after merge. Post-publication metadata/document reconciliation may advance authoritative `main`, but it does not change the immutable source published as `v1.0.2`.

## Public product state

The Principal-approved Agnir brand identity remains canonical under `brand/`. The bilingual README/website, scoped GitHub Pages publication, transparent render-self-contained brand surfaces, Apache-2.0 licensing, bilingual contribution guidance, repository topics/homepage, and GitHub Issues feedback intake remain accepted public surfaces on authoritative `main`.

The public product category remains **Project Continuity**. The first-user value remains fresh-session recovery: **the Project persists; Executors come and go**. `adoption/README.md` remains canonical launch/adoption strategy.

The canonical fresh-session recovery demo remains under `adoption/demos/fresh-session/`, with `trace.json` as its deterministic presentation source. The first implementation from PR `#51` was technically valid and successfully published, but the first Principal visual review rejected the presentation because it read as independent slide/card replacement rather than a live Agent conversation. That review is accepted product evidence rather than being treated as cosmetic preference.

PR `#52` then replaced the scene-card player with one persistent Agent-workspace transcript. A subsequent Principal review preferred the stronger visual logic of the original static comparison: keep **Without Agnir** and **With Agnir** visible simultaneously, but make both sides dynamic. That direction is now accepted as the demo's current presentation contract rather than a return to slides.

PR `#53` implemented the synchronized split-screen v3. Desktop now shows two dynamic Agent-workspace windows at once: left **Without Agnir**, right **With Agnir**, driven by one shared playback clock. Both receive the same task, reach the same stopping point, create genuinely fresh Session B instances, and receive only `Continue.` / `继续。`; the left side stalls on missing durable context while the right side discovers Agnir, loads Project truth, completes the pending failure-path tests, and verifies them successfully. Narrow/mobile layouts stack the same two windows in Without-then-With order. The deterministic trace schema is `agnir.demo.split-screen/3`.

The split-screen implementation source head is `a74371b37f044af2837c7de3d4178f26cf299d8d`; PR `#53` merged at `64e61ad1f21d15362cedbfb8376ab1d0adb6343d`. PR conformance run `34819370697`, post-merge conformance run `34819425531`, and Pages build/deploy run `34819425549` all succeeded. Published Pages artifact `10338020626` has digest `sha256:50ae43bdc8d18e5ab05057fee5406fbb6c7f9282eb585109de34a5dbb94501de`. The published artifact was inspected directly: it contains `agnir.demo.split-screen/3`, both `without` / `with` event lanes, the split-lane renderer, two-column desktop CSS, and JavaScript that passes `node --check`.

On 2026-09-14, the Principal completed human visual review of the live split-screen v3 and explicitly accepted the result: **“看过了，这个版本我觉得可以。”** The canonical fresh-session demo visual-review gate is therefore closed. The split-screen v3 is now the accepted primary first-contact demo surface for Agnir adoption work.

PR `#54` added a native install-conversation illustration to the website's **Install first / 先安装** section, following the Principal-approved mockup direction. The install copy remains on the left while a compact Agent chat surface appears on the right on desktop; narrow/mobile layouts stack the preview below the install copy. The preview is HTML/CSS rather than a raster screenshot, is localized for English / Simplified Chinese / Japanese / Korean, supports dark/light themes, and uses the same warm four-point Agent sparkle icon as the dynamic fresh-session demo Agent avatars. This is a public-presentation surface only and does not redefine Core or checkpoint semantics.

The initial install-preview source head was `09c66f9b9aecf452241970bebb670fe9ea44e111`; PR `#54` merged at `a285c8868ae65ab2759b8f9b88572fd47f359161`. PR conformance run `34824713563`, post-merge conformance run `34824764737`, and Pages run `34824764786` succeeded; Pages build job `103914219408` and deploy job `103914266875` both succeeded. Published artifact `10340210569` has digest `sha256:a36d2fc1712a1dac1bd6137ec5d3202b4480933d259f22b2131524390395c761`. That first single-window install preview was then refined before visual acceptance.

PR `#55` now makes the Install-section session boundary explicit. The right-side illustration is two separate stacked Agent windows: Session A installs Agnir and tells the user that a fresh session only needs `Continue.` / `继续。`; Fresh Session B is a separate lower window that receives only that prompt and then shows the Agent loading Project state and continuing. A compact localized “open a fresh session” divider sits between the two windows. The hero comparison copy is also strengthened in Simplified Chinese to **“两个新会话都只收到一句：‘继续。’ 但大有不同。”** with equivalent English contrast wording and Japanese/Korean static-fallback copy.

The PR `#55` source head is `3c073e80ad87db9a11d2beb89f9e90d4d92f6482`; it merged at `06749842054d612a64af46f5509f9baffe99da03`. PR conformance run `34826216679`, post-merge conformance run `34826272500`, and Pages build/deploy run `34826272497` all succeeded. Pages build job `103919066599` and deploy job `103919099750` succeeded. Published artifact `10340342962` has digest `sha256:1c48ae65668aa4f9f0ce81d706e91c964def43656367290b7025971dd051c0e0`. Direct artifact inspection confirmed the two-window CSS, localized Session A / Fresh Session B copy, the contrast addendum, and successful `node --check` for published `theme.js` and `demo.js`. Human visual review of this refined Install-section presentation remains pending and does not reopen the already accepted canonical split-screen demo gate.

PR `#62` refined the public Install prompt interaction by moving the copy icon from the trailing/right side of the prompt block to the leading/left side. The DOM order now also places the copy button before the prompt `pre`, so the semantic/tab order matches the visual order rather than relying on CSS-only positioning. English, Simplified Chinese, Japanese, and Korean pages were updated together; desktop and mobile prompt padding were mirrored accordingly. Copy/check behavior and labels remain unchanged.

The implementation source head was `4ac47b0bd89af2d4cbe29fb381e255e10c8bf1ce`; PR `#62` merged to authoritative `main` at `e038f4f8c6aded44b2b513d98ebb04564326dcfd`. PR conformance run `35382160261` succeeded. Post-merge conformance run `35382206608` succeeded. GitHub Pages run `35382206627` succeeded with build job `105720772360` and deploy job `105720824525`; published artifact `10562442305` has digest `sha256:549a7e018baa0633c37b6fa928abdcf350bf9ba393fff1fb0cf2d14490173367`. This is public-surface polish only and does not change Agnir Core/profile or durable-continuity semantics.

Svif remains the first accepted real-project post-1.0 adoption case. External cold-start resumes, external design users, cross-Executor cases, and independently built integrations are now the highest-value next adoption evidence.

## ChatGPT Project locator simplification accepted

On 2026-09-18, a real ChatGPT web initialization trial exposed that Agnir could repeatedly propose overly verbose persistent Project Instructions. Review found a packaging inconsistency: the README already required execution-surface bootstrap to append **Project locator only**, while the `SKILL.md` ChatGPT example duplicated `AGNIR.yaml` loading, durable-truth authority, and checkpoint semantics.

The accepted ChatGPT Project handoff is now intentionally locator-only:

```text
Canonical Project: <owner/repository> (<ref>)
At the first substantive turn of every new conversation, open it, read root AGENTS.md, and follow it before doing Project work.
```

The Principal explicitly accepted these two lines for permanent Agnir use provided continuity is preserved. Continuity remains repository-owned because the surface instruction only locates the Project; the durable activation chain remains `AGENTS.md -> AGNIR.md -> AGNIR.yaml -> selected durable continuity`. The shorter surface handoff removes duplicated semantics rather than removing continuity semantics.

Implementation PR `#58` merged to authoritative `main` at `2c62d026c48405c3e299f0f57d6a674b3f6f9e1c`. PR conformance run `35334360203` and authoritative post-merge conformance run `35353464865` both succeeded. Core `1.0` and `repository-filesystem/1.0` remain unchanged.

A future genuinely fresh ChatGPT Project initialization remains useful adoption observation: it should surface the accepted short locator without user simplification. Failure to do so is a packaging/integration regression, not a reason to duplicate Agnir semantics back into Project Instructions.

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
