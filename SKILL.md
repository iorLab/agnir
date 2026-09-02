---
name: agnir
description: Install, initialize, migrate, upgrade, use, checkpoint, resume, integrate, or repair Agnir durable Project continuity. Use when a user asks to install or initialize Agnir, upgrade or migrate an existing Agnir Project, make a Project resumable across Agents or conversations, work with parallel Continuity Lineages, checkpoint progress, commit or push Project changes with continuity reconciliation, or repair Agnir discovery/activation. The user-facing request may be only a short intent statement; this Skill owns the full procedure.
---

# Agnir

Agnir is a project-owned durable continuity protocol. The Project owns the durable truth required to continue safely when Agents, conversations, execution environments, storage implementations, or parallel work contexts change.

**Do not require the user to carry Agnir's implementation checklist** in their prompt. A short request such as `Install and initialize Agnir for this Project` or `Upgrade Agnir to the latest stable release` is sufficient once this Skill has been found. This file is the Agent-facing procedure.

## Determine the operation and target

Classify the request as one of:

- **install / initialize** — the target Project does not yet have a valid Agnir setup;
- **migration** — the target Core or discovery-profile compatibility line differs from the existing Project;
- **upgrade** — the Project is already Agnir-enabled and the target operational package stays within the same Core/profile compatibility lines;
- **resume / use** — the Project is already Agnir-enabled and no Agnir upgrade/migration was requested;
- **checkpoint** — persist material continuity updates;
- **commit / push** — treat repository publication intent as a checkpoint boundary, then perform the requested VCS operation when authorized;
- **lineage integration** — combine work from one or more source Continuity Lineages into a target lineage;
- **repair** — the Project intends to use Agnir but activation, discovery, identity, lineage/binding, or locators are broken.

Resolve the target Agnir package before mutating the Project:

1. `latest stable release` means an actually published stable tag/release. **Do not silently treat `main`**, another moving branch, an RC, or an untagged revision as stable.
2. A prerelease such as `v0.2.0-rc.1` may be used only when the Principal explicitly requests or authorizes that non-stable target.
3. Read the target package's `RELEASE.md`, Core/profile contract, and migration contract before changing compatibility lines.
4. Record enough immutable target provenance to make the operation reproducible.

For repository/filesystem Projects:

- Core/profile `0.1` uses `spec/AGNIR_CORE.md`, `profiles/REPOSITORY_FILESYSTEM.md`, and `schemas/agnir-manifest.schema.json`;
- Core/profile `0.2` uses `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, and `schemas/agnir-manifest-0.2.schema.json`;
- when VCS branches/worktrees, selector bindings, merge/rebase/cherry-pick, or target publication matter, also read `profiles/VCS_BRANCH_CONTINUITY.md` as the VCS adapter/extension mapping.

## Install or initialize Agnir

Treat the target Project root—not this Skill repository—as the authorized Project Entry Point.

Before changing any target-Project file, inspect existing `README.md`, `AGENTS.md`, `AGNIR.yaml`, and `.agnir/` content. Preserve unrelated Project documentation, Agent instructions, and existing files. Merge; do not destructively replace.

### Merge existing AGENTS.md safely

Handle the target Project's root `AGENTS.md` mechanically:

1. If `AGENTS.md` does not exist, create only a minimal Agent-instruction file containing an Agnir locator to README `Agnir Project Instructions`.
2. If `AGENTS.md` already exists, **preserve its existing unrelated content** and add only the minimal Agnir locator. Do not rewrite, reorder, summarize, normalize, or delete unrelated Project instructions merely to install Agnir.
3. If an **equivalent Agnir locator already exists**, treat the merge as idempotent; do not add another copy.
4. Keep `AGENTS.md` locator-only for Agnir. Do not copy durable State, Next Actions, Decisions, Evidence, or the full Agnir procedure into it.
5. Detect material instruction conflicts before writing. Examples include instructions not to read/follow `README.md`, not to read `AGNIR.yaml`, not to use Agnir, or an Agnir locator pointing to a competing canonical location.
6. If resolving a material conflict would require deleting, overriding, or reinterpreting an existing Project instruction, **do not guess and do not overwrite it**. Stop, **report the exact conflict to the Principal**, and do not claim installation complete until the conflict is explicitly resolved.

### Create the target discovery record

Use the compatibility line of the explicitly resolved target package.

For Core/profile `0.1`, create or validate top-level `AGNIR.yaml` with:

- `agnir.version: "0.1"`;
- `agnir.discovery_profile: "repository-filesystem/0.1"`;
- a non-empty durable `project.identity`;
- memory locators for Current State, Next Actions, Decisions, and Evidence.

For Core/profile `0.2`, create or validate top-level `AGNIR.yaml` with:

- `agnir.version: "0.2"`;
- `agnir.discovery_profile: "repository-filesystem/0.2"`;
- the same kind of non-empty durable `project.identity`;
- a non-empty logical `continuity.lineage` for the selected continuity;
- memory locators for Current State, Next Actions, Decisions, and Evidence.

For a VCS-aware Core `0.2` Project, keep logical lineage identity separate from VCS selector/binding metadata. A branch/ref/worktree may select or bind a lineage, but it is **not automatically lineage identity**. A commit SHA is a checkpoint/revision receipt, not lineage identity. Do not derive a logical lineage ID from a commit SHA or silently mint/switch lineage merely because a ref name changed.

Unless the Project already has an intentionally compatible layout, use:

- `.agnir/state.md`;
- `.agnir/next-actions.md`;
- `.agnir/decisions.md`;
- `.agnir/evidence/`.

Create concise initial durable truth and at least one initialization Evidence object when Evidence is declared.

### Persist Agent-operable Project activation

In the target Project's `README.md`, create or update a canonical section headed exactly `## Agnir Project Instructions`. It must tell future Agents to:

- treat the Project root as the authorized Project Entry Point;
- read top-level `AGNIR.yaml`;
- validate Core/profile, Project identity, and selected lineage/binding when applicable;
- load Current State and Next Actions, then Decisions/Evidence when relevant;
- prefer durable Project truth over private Agent memory unless superseded by newer Principal instruction or directly observed current Project fact;
- checkpoint material continuity changes at save/finish/commit boundaries;
- treat authorized `commit`, `提交代码`, or equivalent repository intent as a checkpoint boundary, prefer Project + Agnir changes in **one VCS revision**, and treat `提交推送` / commit-and-push as checkpoint + commit + push + destination-ref verification.

Create/update root `AGENTS.md` according to **Merge existing AGENTS.md safely** so it points to `## Agnir Project Instructions` and does not fork a second copy of the procedure.

### Verify repository activation

Validate every locator, Project identity, and selected lineage/binding. Finish with a **fresh repository activation test** using only the Project root:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared selected durable memory
```

This repository-layer check is also the **fresh activation test**. Repository activation is incomplete if continuation still depends on the installation conversation or installing Agent's private memory.

### Complete execution-surface activation

**Repository activation and execution-surface activation are separate completion dimensions.** After repository activation, inspect whether the active execution surface will give a future fresh context enough persistent information to reach the authorized Project Entry Point.

1. If the execution surface automatically starts Project work from the authorized Project root and reads Project instructions, report execution-surface activation as not separately required.
2. If persistent project/workspace configuration is required, configure the locator when tools and Principal authority allow it.
3. If required configuration cannot be modified directly, produce a **copy-ready execution-surface handoff**, ask the Principal to **append or merge** it into persistent Project/workspace instructions, preserve unrelated instructions, and report **pending user configuration**.
4. Keep the handoff locator-only. **Do not report full fresh activation as passed** while required surface configuration is pending or unverified.
5. Report **repository activation status** and **execution-surface activation status** separately.
6. After required configuration is applied, verify from a genuinely fresh execution context when possible; otherwise report verification pending.

For a **ChatGPT Project** backed by a repository declared under `extensions.agnir/repository`, when ChatGPT does not automatically inspect repository Project instructions, generate a block equivalent to:

```text
Agnir Project bootstrap

Canonical Project: <owner/repository>
Authoritative ref: <ref>

At the first substantive turn of every new conversation, open the canonical Project repository, read root AGENTS.md, and follow its Agnir activation locator before doing Project work.

Load the Project continuity declared by AGNIR.yaml. Treat repository-managed Agnir state as canonical durable Project truth; ChatGPT Project memory and conversation context are working memory only.

When Project work materially changes durable continuity, follow the Project's Agnir checkpoint instructions before finishing, committing, or pushing.
```

Ask the Principal to **append or merge** this block and **do not overwrite unrelated existing Project Instructions**. The block is an execution-surface adapter, not Agnir Core and not a second canonical Project memory store.

## Upgrade an existing Agnir Project

**Upgrade is not re-initialization**. Start by activating the existing Project and loading authoritative continuity. Preserve Project identity, memory locators/content, unrelated README content, unrelated `AGENTS.md` instructions, unrelated extensions, and execution-surface locators unless a separately authorized operation changes them.

### Classify before mutating

Compare existing `agnir.version` / `agnir.discovery_profile` with the target:

- **no-op** — the same operational package provenance is applied and no material activation/procedure drift exists;
- **compatible operational upgrade** — Core/profile compatibility lines are unchanged but the operational package is newer or provenance is missing;
- **migration required** — Core or profile compatibility changes. Surface semantics equivalent to `AGNIR_UPGRADE_MIGRATION_REQUIRED`; do not silently rewrite the Project.

A Project created before operational provenance existed is still valid. Missing provenance is not a reason to re-initialize.

### Apply a compatible operational upgrade

1. **Preserve `project.identity`**, all declared memory locators/content, and unrelated extensions.
2. Non-destructively merge the target activation/procedure contract into README `Agnir Project Instructions` and preserve locator-only `AGENTS.md` behavior.
3. Record applied operational provenance when the target package supplies it:

```yaml
extensions:
  agnir/operations:
    distribution: "agnir-agent-skill"
    release: "<repository release>"
    source: "iorLab/agnir"
    applied_revision: "<immutable source revision>"
```

`agnir/operations` records the operational package; it does not replace Core/profile compatibility, lineage identity, or Project identity.
4. Reconcile material upgrade facts into continuity/Evidence.
5. In VCS, publish the operational upgrade and checkpoint coherently, preferably in one revision.
6. Finish with repository activation and execution-surface activation evaluation.

If nothing material changed, **upgrade evaluation is a no-op**: do not rewrite Project files merely to record that evaluation occurred.

## Migrate Core/profile compatibility

Migration is separately authorized compatibility work, not a compatible operational upgrade.

For Core/profile `0.1` → `0.2`:

1. activate the existing `0.1` Project and capture authoritative Project identity, memory locators/content, relevant decisions/evidence, and backend generation/revision receipt;
2. preserve Project identity and all material durable truth;
3. choose/generate exactly one initial logical Continuity Lineage for the existing implicit continuity line according to explicit Project/profile policy;
4. if VCS-aware, resolve the selected ref/worktree as backend selector/binding separately from that logical lineage identity;
5. construct the complete Core/profile `0.2` candidate before authoritative publication;
6. if the source generation changed after staging, fail/re-resolve rather than overwrite newer truth;
7. publish compatibility declaration + lineage identity + selector binding (when applicable) + preserved/reconciled continuity coherently;
8. fresh-resolve Core/profile `0.2`, the same Project identity, and the intended logical lineage;
9. repeat of the identical migration is a no-op; conflicting silent lineage rebind is a migration conflict.

Follow `spec/CORE_0_1_TO_0_2_MIGRATION.md` and the selected profile's migration rules. Do not move memory solely because Core `0.2` introduces lineage identity.

## Resume or use an existing Agnir Project

Do not ask the user for another Agnir bootstrap prompt.

1. read root `AGENTS.md`;
2. follow it to README `Agnir Project Instructions`;
3. read `AGNIR.yaml`;
4. validate Core/profile compatibility and Project identity;
5. for Core `0.2`, resolve exactly one selected logical lineage from explicit/context/default selection; if a backend selector is used, validate its binding separately;
6. load Current State and Next Actions for that lineage;
7. load Decisions/Evidence when relevant;
8. perform the user's actual Project task.

If required lineage selection is missing, fail with `AGNIR_LINEAGE_REQUIRED` semantics. If a selected identity/binding cannot safely resolve, fail instead of scanning sibling branches/workspaces to guess.

Normal resume does not automatically upgrade or migrate Agnir. Upgrade/migration occurs only by explicit Principal intent or durable Project policy, keeping Projects resumable without network access to the distribution source.

## Checkpoint

At an intentional checkpoint, save-progress, handoff, finish boundary, or repository commit boundary:

1. reconcile current Project truth rather than appending a transcript;
2. classify material changes into State, Next Actions, Decisions, and only necessary Evidence;
3. if authoritative durable truth already matches, checkpoint evaluation is a **no-op**;
4. when material continuity changed, construct the complete **candidate checkpoint** before publication;
5. scope the checkpoint to the selected lineage unless explicit Project policy defines a wider transaction;
6. publish atomically when possible, or use durable generation/revision/pointer semantics that prevent mixed generations from appearing coherent;
7. if the authoritative base changed, surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile again;
8. verify fresh discovery of the same Project identity and selected lineage;
9. ensure a fresh Executor can resume without private conversation context.

Do not require every checkpoint to modify every semantic category.

## Commit and push integration

Interpret repository commit/push requests by intent and context, **not by global string matching**.

- In repository/VCS context, `commit`, `提交`, `提交代码`, and equivalent wording normally mean: **checkpoint evaluation → reconcile if material → create the requested commit**.
- `commit and push`, `提交推送`, and equivalents mean: **checkpoint evaluation → commit → push → verify the actual destination remote/ref**.
- A bare `提交` outside repository context may mean submitting a form/document/job; do not trigger VCS procedure solely on the literal word.

For an authorized commit:

1. load current selected continuity;
2. reconcile material updates;
3. if Project and Agnir continuity both changed, prefer **one VCS revision** containing both;
4. do not create a follow-up checkpoint-only commit unless a later independent material truth change requires it;
5. if checkpoint evaluation is a no-op, commit only requested Project changes;
6. use commit/revision identifiers as receipts when useful; do not embed a commit SHA into content whose hash would determine that SHA.

After push, verify the actual destination ref. An `authoritative_ref` is a publication-authority boundary, not the only permitted feature-branch checkpoint target.

### Parallel Continuity Lineages in VCS

For Core `0.2` VCS-backed work:

- preserve one Project identity across ordinary branches/worktrees;
- logical lineage identity is separate from branch/ref/worktree selector and revision receipt;
- an Agnir-aware lineage fork creates a new logical lineage and must publish lineage identity + selector binding + coherent inherited/reconciled continuity together;
- explicit ref rename/rebind may preserve logical lineage identity;
- external branch copies with stale/ambiguous binding must not be guessed as fork vs rename;
- branch-local checkpoints do not silently mutate sibling lineages.

## Integrate Continuity Lineages

For merge/rebase/cherry-pick or another lineage integration:

1. validate source/target Project identity; cross-Project mismatch remains a hard failure;
2. capture target and relevant source generation/revision receipts plus continuity;
3. construct/stage the actual integrated Project candidate **without advancing the target** when Agnir controls the path;
4. reconcile target State/Next Actions/Decisions/Evidence from actual integrated Project truth, prior target continuity, relevant source continuity/Evidence, and current Principal intent;
5. source continuity is input, never automatic target truth;
6. if target or relevant source advances after staging, discard/re-resolve the stale candidate;
7. publish integrated Project + reconciled target continuity together in the exact target-advancing transition;
8. fresh-resolve target and verify source remains independently resumable when applicable.

If integration has happened but target continuity remains unreconciled, surface `AGNIR_LINEAGE_RECONCILIATION_REQUIRED` / adapter-specific reconciliation-required semantics rather than claiming completion.

## Repair

Repair the earliest broken layer; do not invent truth.

1. Confirm the authorized Project Entry Point.
2. Validate `AGENTS.md` → README `Agnir Project Instructions` activation.
3. Validate `AGNIR.yaml` Core/profile compatibility and Project identity.
4. For Core `0.2`, validate selected logical lineage and any backend selector/binding separately.
5. Validate memory locators and reject traversal/symlink/authorization violations according to the profile.
6. Reconcile material durable truth only after discovery/selection is trustworthy.
7. If an external mechanism advanced a target with unreconciled continuity, classify it as recovery-required; reconcile target truth and create a coherent checkpoint rather than pretending the earlier publication was conforming.
8. Re-run fresh repository activation and, when required, execution-surface activation verification.

Never repair by silently choosing a sibling repository/branch/lineage, copying source continuity wholesale into target, rewriting unrelated Project instructions, or treating private chat history as canonical Project truth.
