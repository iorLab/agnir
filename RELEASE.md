# Agnir 1.0.x Stable Release Package

**Current repository version:** `1.0.2`

**Latest published stable:** `v1.0.1`

**Core compatibility line:** `1.0`

**Repository/filesystem profile:** `repository-filesystem/1.0`

## Status

Agnir repository source `1.0.2` is the **accepted publication candidate**. The latest published stable remains `v1.0.1` until the separate authoritative publication transaction succeeds.

Accepted stable publication receipts:

- tag: `v1.0.1`;
- exact authoritative source revision: `f56d25b22997c259c660651e7357334b063093e1`;
- GitHub Release id: `385176185`;
- published at: `2026-09-09T02:02:14Z`;
- publication workflow: `34301559338` — success;
- repository/conformance job: `102309347343` — success;
- stable publication job: `102309386242` — success;
- `releases/latest == v1.0.1`;
- previous stable `v1.0.0` remains exactly `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted `v1.0.0-rc.1` remains exactly `092945289f1a0a9803e4fe0583104aa380ceaadc`.

Repository `1.0.2` is a backward-compatible PATCH for execution-surface onboarding/packaging reliability. It **does not change Core `1.0`**, `repository-filesystem/1.0`, the Project identity model, Continuity Lineage semantics, checkpoint semantics, or historical compatibility lines. Published `v1.0.1` remains the current stable release until `v1.0.2` publication succeeds.

`latest stable` is a publication property, not a moving-branch property. During the `1.0.2` candidate stage, stable resolution continues to select the published non-prerelease `v1.0.1` release, not the release branch or untagged `main` commits.

## v1.0.2 patch scope

The `1.0.2` candidate publishes the Principal-accepted **locator-only ChatGPT Project handoff**:

```text
Canonical Project: <owner/repository> (<ref>)
At the first substantive turn of every new conversation, open it, read root AGENTS.md, and follow it before doing Project work.
```

For ChatGPT Projects that need persistent workspace instructions, the execution surface stores only the canonical Project/ref plus the fresh-context locator to root `AGENTS.md`. It must not duplicate `AGNIR.yaml` loading, durable-truth authority, checkpoint semantics, or repository-operation semantics into Project Instructions when those are already reachable through the Project-owned activation route.

Continuity remains:

`AGENTS.md -> AGNIR.md -> AGNIR.yaml -> selected durable continuity`

Accepted implementation receipts before the release cycle:

- implementation PR: `#58`;
- implementation merge: `2c62d026c48405c3e299f0f57d6a674b3f6f9e1c`;
- implementation post-merge conformance: `35353464865` — success;
- acceptance/checkpoint merge: `4fde39128e5edf3fba3d7906a279918b1c38b7c2`;
- acceptance post-merge conformance: `35353700740`, repository job `105627739027` — success.

This patch is distribution/onboarding hardening only. Core/profile remain `1.0` / `repository-filesystem/1.0`.

## v1.0.1 patch scope

The patch moves Project-specific Executor instructions out of the general README into a dedicated root `AGNIR.md` surface:

```text
Project root
→ AGENTS.md
→ AGNIR.md
→ AGNIR.yaml
→ selected durable continuity
```

The packaging responsibilities are:

- `AGENTS.md`: locator-only Project entry to `AGNIR.md`;
- `AGNIR.md`: canonical Executor-facing activation + Project-operation instructions;
- `AGNIR.yaml`: machine-readable Project/compatibility/lineage/discovery declaration;
- `.agnir/`: Project-owned durable continuity;
- `README.md#Agnir-Project-Instructions`: backward-compatible locator only for older `1.0.0` activation paths;
- `SKILL.md`: distribution procedure for install, upgrade, migration/promotion, repair, and generic Agnir operations.

The patch also hardens repository short-intent dispatch:

- `commit` / `提交` / `提交代码` in repository context → checkpoint evaluation → Project-defined pre-commit policy when declared → commit;
- `commit and push` / `提交推送` → checkpoint evaluation → Project-defined pre-commit policy when declared → commit → push → verify destination ref.

Checkpoint evaluation is mandatory at the boundary, but `.agnir/` mutation is not. If durable truth is unchanged, checkpoint evaluation is a valid no-op; the implementation must not fabricate State/Evidence changes merely to make a commit contain Agnir files.

## Backward-compatible v1.0.0 upgrade

An existing `1.0.0` Project that still activates through:

```text
AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
```

remains activatable before upgrade/repair. A compatible `1.0.0` → `1.0.1` operational upgrade then:

1. preserves Project identity, logical lineage identity, Core/profile compatibility identifiers, selectors/bindings, durable memory locators/content, unrelated extensions, and unrelated Project instructions;
2. creates/updates canonical `AGNIR.md`;
3. upgrades the Agnir locator in `AGENTS.md` to point directly to `AGNIR.md`;
4. reduces the README Agnir section to a compatibility locator rather than a second procedure copy;
5. fresh-validates the direct route;
6. reconciles material upgrade evidence/checkpoint state.

This is a distribution/packaging upgrade, not a Core/profile migration or promotion.

## Stable 1.0 compatibility baseline

Stable normative contracts remain unchanged:

- `spec/AGNIR_CORE_1_0.md`;
- `profiles/REPOSITORY_FILESYSTEM_1_0.md`;
- `schemas/agnir-manifest-1.0.schema.json`;
- `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

The stable 1.0 model preserves:

- Project-owned durable continuity;
- Project identity distinct from logical Continuity Lineage identity;
- selector/binding distinct from lineage identity and revision receipts;
- Current State / Next Actions / Decisions / Evidence semantics;
- exact compatibility-line dispatch;
- lineage-local checkpoints and stale-base rejection;
- source continuity as reconciliation input rather than automatic target truth;
- coherent target publication;
- VCS and non-VCS neutrality at Core level;
- machine-distinguishable discovery/checkpoint/lineage failures.

## Historical compatibility remains supported

The `1.0.x` distribution remains multi-version. Historical published compatibility surfaces remain present and are not rewritten as 1.0 history:

- Core/profile `0.1` + `repository-filesystem/0.1`;
- Core/profile `0.2` + `repository-filesystem/0.2`;
- explicit `0.1` → `0.2` migration under `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- explicit semantics-preserving `0.2` → `1.0` promotion under `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

Installing or upgrading to the `1.0.x` distribution does not itself authorize rewriting an existing valid `0.2` Project to `1.0`. A Project may remain on its supported compatibility line until an explicit Project-owned promotion is authorized.

## v1 baseline evidence

The v1 readiness baseline was closed before the original stable cycle. Accepted evidence includes:

- clean independent-implementation `PASS` from issue #26 against exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`;
- accepted artifact SHA-256 `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`;
- direct boundary matrix `81/81` pass and required semantic receipts `19/19` pass;
- three materially different real Projects: Svif, FishUp, and VocaPort;
- two materially different execution surfaces/adapters;
- accepted VCS and non-VCS lineage evidence;
- accepted real upgrade and real parallel-lineage reconciliation evidence;
- genuine Linux Docker bind-mount fresh-remount/read-only/wrong-root evidence.

The immutable accepted RC for the stable 1.0 compatibility line remains `v1.0.0-rc.1` at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## v1.0.1 acceptance evidence

The exact publication candidate demonstrated:

1. direct fresh activation through `AGENTS.md → AGNIR.md → AGNIR.yaml`;
2. legacy `1.0.0` README-route activation remains usable as compatible upgrade/repair input;
3. non-destructive legacy locator upgrade to `AGNIR.md`;
4. short repository `commit`/`提交` intents enter checkpoint evaluation before VCS mutation;
5. commit-and-push includes destination-ref verification;
6. checkpoint no-op remains legal without `.agnir/` mutation;
7. Core/profile `0.1`, `0.2`, and `1.0` conformance remains green;
8. full repository conformance passed on the exact candidate.

Publication run `34301559338` repeated exact-source verification and the full suite before creating the stable tag/Release.

## Stable publication invariant

Implementation, a green PR, or an authoritative-main merge does **not** by itself publish a stable release.

`v1.0.1` was published only through the separately armed authoritative-main transaction `release: publish v1.0.1 stable`. The publication path verified the exact source candidate, created/validated immutable `refs/tags/v1.0.1`, created/validated a non-draft/non-prerelease GitHub Release, verified `releases/latest == v1.0.1`, and verified the existing `v1.0.0` tag remained exactly at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`.

`v1.0.2` may be published only by the exact authoritative-main trigger `release: publish v1.0.2 stable` after the repository source is `1.0.2` and conformance is green. Published tags are immutable by Project policy.

## Activation and Skill boundary

Root `SKILL.md` remains the canonical Agent-facing distribution procedure. A configured Project persists its own operation policy in root `AGNIR.md`; `AGENTS.md` is only a locator to it. Execution-surface bootstrap/configuration remains locator-only adapter behavior outside Agnir Core and outside Project-owned durable memory.
