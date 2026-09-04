---
name: agnir
description: Install, initialize, migrate, upgrade, use, checkpoint, resume, integrate, or repair Agnir durable Project continuity. Use when a user asks to install or initialize Agnir, upgrade or migrate an existing Agnir Project, make a Project resumable across Agents or conversations, work with parallel Continuity Lineages, checkpoint progress, commit or push Project changes with continuity reconciliation, or repair Agnir discovery/activation. The user-facing request may be only a short intent statement; this Skill owns the full procedure.
---

# Agnir

Agnir is a project-owned durable continuity protocol. The Project owns the durable truth required to continue safely when Agents, conversations, execution environments, storage implementations, or parallel work contexts change.

Do not require the user to carry Agnir's implementation checklist. A short intent such as `Install and initialize Agnir for this Project` or `Upgrade Agnir to the latest stable release` is sufficient once this Skill is available.

## Determine the operation and target

Classify the request as install/initialize, migration, upgrade, resume/use, checkpoint, commit/push, lineage integration, or repair.

Resolve the target Agnir package before mutating the Project:

1. `latest stable release` means an actually published stable tag/release. Do not silently treat `main`, another moving branch, an RC, or an untagged revision as stable.
2. A prerelease such as `v0.2.0-rc.1` requires explicit Principal authorization.
3. Read the target `RELEASE.md`, Core/profile contract, and migration contract.
4. Record immutable target provenance.

For repository/filesystem targets:

- Core/profile `0.1`: `spec/AGNIR_CORE.md`, `profiles/REPOSITORY_FILESYSTEM.md`, `schemas/agnir-manifest.schema.json`;
- Core/profile `0.2`: `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, `spec/CORE_0_1_TO_0_2_MIGRATION.md`, `schemas/agnir-manifest-0.2.schema.json`;
- Core/profile `0.1` VCS branch/worktree/integration behavior: also apply `profiles/VCS_BRANCH_CONTINUITY.md` as the experimental 0.1 VCS extension;
- Core/profile `0.2` VCS selector/binding/fork/rebind/integration behavior: use the normative VCS semantics in `spec/AGNIR_CORE_0_2.md` and `profiles/REPOSITORY_FILESYSTEM_0_2.md`. Do **not** treat the Core/profile 0.1-only `profiles/VCS_BRANCH_CONTINUITY.md` as the normative 0.2 contract.

## Install or initialize Agnir

Treat the target Project root—not this Skill repository—as the authorized Project Entry Point. Before writing, inspect existing `README.md`, `AGENTS.md`, `AGNIR.yaml`, and `.agnir/`. Preserve unrelated Project content; merge rather than destructively replace.

### Merge existing AGENTS.md safely

1. If `AGENTS.md` is absent, create only a minimal Agnir locator to README `Agnir Project Instructions`.
2. If it exists, preserve its existing unrelated content and add only the locator.
3. If an equivalent Agnir locator already exists, treat the merge as idempotent.
4. Keep `AGENTS.md` locator-only; do not copy durable continuity or the full procedure into it.
5. Detect instruction conflicts before writes.
6. If resolving a conflict would require overriding/reinterpreting existing Project instructions, do not guess and do not overwrite it. Stop and report the exact conflict to the Principal.

### Create the discovery record and durable memory

For Core/profile `0.1`, `AGNIR.yaml` declares `agnir.version: "0.1"`, `repository-filesystem/0.1`, non-empty `project.identity`, and memory locators.

For Core/profile `0.2`, it declares `agnir.version: "0.2"`, `repository-filesystem/0.2`, the same durable `project.identity` concept, a non-empty logical `continuity.lineage`, and memory locators.

For VCS-aware Core `0.2`, keep logical lineage identity separate from selector/binding metadata. A branch/ref/worktree can select/bind a lineage; it is not automatically lineage identity. A commit SHA is a receipt, not lineage identity.

Unless an intentionally compatible layout already exists, use:

- `.agnir/state.md`
- `.agnir/next-actions.md`
- `.agnir/decisions.md`
- `.agnir/evidence/`

Create concise initial truth and at least one initialization Evidence item when Evidence is declared.

### Persist Project activation

In target `README.md`, create/update the exact heading `## Agnir Project Instructions`. Tell future Agents to read `AGNIR.yaml`, validate compatibility/Project identity/selected lineage, load State and Next Actions, load Decisions/Evidence when relevant, prefer durable Project truth over private Agent memory, and checkpoint at save/finish/commit boundaries.

Persist repository intent semantics there: authorized `commit` / `提交代码` means checkpoint before commit and preferably Project + Agnir changes in one VCS revision; `提交推送` means checkpoint + commit + push + destination-ref verification.

Create/update root `AGENTS.md` according to the safe merge rules so it points to `## Agnir Project Instructions` without duplicating the procedure.

### Verify repository activation

Finish with a fresh repository activation test (the repository-layer fresh activation test):

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared selected durable memory
```

If continuation still depends on the installation conversation or installing Agent's private memory, repository activation is incomplete.

### Complete execution-surface activation

Repository activation and execution-surface activation are separate completion dimensions.

1. If a future context automatically begins from the authorized Project root and reads Project instructions, separate surface configuration is not required.
2. If persistent workspace/Project configuration is required and tools/authority permit, configure the locator.
3. Otherwise provide a copy-ready execution-surface handoff, ask the Principal to append or merge it, preserve unrelated instructions, and report pending user configuration.
4. Do not report full fresh activation as passed while required configuration is pending/unverified.
5. Report repository activation status and execution-surface activation status separately.
6. Verify from a genuinely fresh context when possible.

For a ChatGPT Project that needs a persistent locator, provide a block equivalent to:

```text
Agnir Project bootstrap

Canonical Project: <owner/repository>
Authoritative ref: <ref>

At the first substantive turn of every new conversation, open the canonical Project repository, read root AGENTS.md, and follow its Agnir activation locator before doing Project work.

Load the Project continuity declared by AGNIR.yaml. Treat repository-managed Agnir state as canonical durable Project truth; ChatGPT Project memory and conversation context are working memory only.

When Project work materially changes durable continuity, follow the Project's Agnir checkpoint instructions before finishing, committing, or pushing.
```

Ask the Principal to append or merge the block; do not overwrite unrelated existing Project Instructions. This is an execution-surface adapter, not Core or a second Project memory store.

## Upgrade an existing Agnir Project

Upgrade is **not re-initialization**. Activate the existing Project first. Preserve Project identity, memory locators/content, unrelated README/`AGENTS.md` content, unrelated extensions, and still-valid surface locators unless another authorized operation changes them.

### Classify before mutating

- **no-op** — same operational package and no material drift;
- **compatible operational upgrade** — Core/profile compatibility lines unchanged;
- **migration required** — Core/profile changes. Surface `AGNIR_UPGRADE_MIGRATION_REQUIRED`-class semantics and do not silently rewrite compatibility.

A Project without older operational provenance remains valid; missing provenance does not justify re-initialization.

### Apply a compatible operational upgrade

1. Preserve `project.identity`, memory locators/content, and unrelated extensions.
2. Non-destructively merge the target activation/procedure contract.
3. When supported, record actual applied package provenance:

```yaml
extensions:
  agnir/operations:
    distribution: "agnir-agent-skill"
    release: "<repository release>"
    source: "iorLab/agnir"
    applied_revision: "<immutable source revision>"
```

`agnir/operations` does not redefine Core/profile, Project identity, or lineage identity.
4. Reconcile material upgrade evidence.
5. In VCS, prefer one coherent revision for procedure/provenance/continuity changes.
6. Re-run repository and surface activation checks.

If nothing material changes, upgrade evaluation is a no-op.

## Migrate Core/profile compatibility

Migration is separately authorized compatibility work, not a compatible operational upgrade.

For `0.1` → `0.2`:

1. activate existing `0.1` truth and capture Project identity, memory locators/content, relevant decisions/evidence, and backend receipt;
2. preserve Project identity and material durable truth;
3. choose/generate exactly one initial logical Continuity Lineage for the previous implicit continuity line;
4. if VCS-aware, resolve selector/binding separately from logical lineage identity;
5. construct the complete `0.2` candidate before publication;
6. if source generation changes after staging, fail/re-resolve rather than overwrite;
7. publish compatibility declaration + logical lineage + selector binding when applicable + preserved/reconciled continuity coherently;
8. fresh-resolve Core/profile `0.2`, the same Project identity, and intended lineage;
9. identical repeat is no-op; conflicting silent initial-lineage rebind is migration conflict.

Follow `spec/CORE_0_1_TO_0_2_MIGRATION.md`. Do not relocate memory merely because `0.2` adds lineage identity.

## Resume or use an existing Agnir Project

Do not ask for another bootstrap prompt.

1. read root `AGENTS.md`;
2. follow README `Agnir Project Instructions`;
3. read `AGNIR.yaml`;
4. validate Core/profile and Project identity;
5. for Core `0.2`, resolve exactly one selected logical lineage from explicit/context/default selection and validate any selector binding separately;
6. load Current State + Next Actions for that lineage;
7. load Decisions/Evidence when relevant;
8. perform the actual Project task.

Missing required selection surfaces `AGNIR_LINEAGE_REQUIRED`; unresolved selected identity/binding fails instead of scanning siblings. Normal resume does not automatically upgrade/migrate.

## Checkpoint

At an intentional checkpoint/save/finish/commit boundary:

1. reconcile Project truth, not a transcript;
2. classify only material continuity changes;
3. unchanged authoritative truth is no-op;
4. construct the complete candidate checkpoint before publication;
5. scope it to the selected lineage unless explicit Project policy says otherwise;
6. publish atomically when possible, otherwise use durable generation/revision semantics;
7. stale authoritative base surfaces `AGNIR_CHECKPOINT_CONFLICT`, then re-resolve/reconcile;
8. fresh-resolve the same Project identity/lineage after publication;
9. ensure a fresh Executor can resume.

## Commit and push integration

Interpret repository intent by context, not by global string matching.

- `commit`, `提交`, `提交代码` in repository context: checkpoint evaluation → commit.
- `commit and push`, `提交推送`: checkpoint evaluation → commit → push → verify actual destination ref.
- a bare `提交` outside repository context does not automatically mean VCS.

If Project and continuity both changed, prefer one VCS revision. If checkpoint evaluation is no-op, commit only requested Project changes. Revision IDs are receipts, not identity.

### Parallel Continuity Lineages in VCS

- preserve one Project identity across ordinary branches/worktrees;
- lineage identity is separate from ref/worktree selector and revision receipt;
- Agnir-aware fork creates a new logical lineage and publishes lineage identity + selector binding + coherent inherited/reconciled continuity together;
- explicit rename/rebind may preserve lineage identity;
- stale/ambiguous external copies must not be guessed as fork vs rename;
- lineage-local checkpoints do not silently mutate siblings.

## Integrate Continuity Lineages

For merge/rebase/cherry-pick or another lineage integration:

1. validate source/target Project identity;
2. capture target and relevant source receipts/continuity;
3. stage the actual integrated candidate without advancing the target when Agnir controls the path;
4. reconcile target truth from integrated Project result + prior target continuity + relevant source continuity/Evidence + current Principal intent;
5. source continuity is input, not automatic target truth;
6. target/source advancement after staging invalidates the candidate;
7. publish integrated Project + reconciled target continuity together in the exact target-advancing transition;
8. fresh-resolve target and verify source remains independently resumable where applicable.

If target continuity remains unreconciled, surface `AGNIR_LINEAGE_RECONCILIATION_REQUIRED` / adapter-specific reconciliation-required semantics.

## Repair

Repair the earliest broken layer; never invent truth.

1. confirm authorized Project Entry Point;
2. validate `AGENTS.md` → README `Agnir Project Instructions` activation;
3. validate `AGNIR.yaml`, Core/profile, Project identity;
4. for `0.2`, validate selected logical lineage and selector/binding separately;
5. validate memory locators/authorization boundaries;
6. reconcile durable truth only after discovery is trustworthy;
7. if an external mechanism advanced an unreconciled target, treat it as recovery-required and construct a coherent target checkpoint;
8. re-run fresh repository activation and required surface activation verification.

Never repair by guessing a sibling Project/branch/lineage, copying source continuity wholesale into target, rewriting unrelated Project instructions, or treating private chat history as canonical Project truth.
