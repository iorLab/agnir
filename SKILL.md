---
name: agnir
description: Install, initialize, upgrade, use, checkpoint, resume, or repair Agnir durable Project continuity. Use when a user asks to install or initialize Agnir, upgrade an existing Agnir Project to a newer operational release, make a Project resumable across Agents or conversations, recover an Agnir-enabled Project, checkpoint progress, commit or push Project changes with continuity reconciliation, or repair Agnir discovery/activation. The user-facing install or upgrade request may be only a short intent statement; this Skill owns the full procedure.
---

# Agnir

Agnir is a project-owned durable continuity protocol. The Project owns the durable truth required to continue safely when Agents, conversations, execution environments, or storage implementations change.

Do not require the user to carry Agnir's implementation checklist in their prompt. A short request such as `Install and initialize Agnir for this Project` or `Upgrade Agnir to the latest stable release` is sufficient once this Skill has been found. This file is the Agent-facing procedure.

## Determine the operation

Classify the request as one of:

- **install / initialize** — the target Project does not yet have a valid Agnir setup;
- **upgrade** — the Project is already Agnir-enabled and the Principal wants a newer Agnir operational package or compatibility line;
- **resume / use** — the Project is already Agnir-enabled and no Agnir upgrade was requested;
- **checkpoint** — persist material continuity updates;
- **commit / push** — treat repository publication intent as a checkpoint boundary, then perform the requested VCS operation when authorized;
- **repair** — the Project intends to use Agnir but activation, discovery, identity, or locators are broken.

For repository/filesystem Projects, read `profiles/REPOSITORY_FILESYSTEM.md` when performing installation, upgrade, activation repair, discovery repair, or repository commit/push integration. Read `spec/AGNIR_CORE.md` and `spec/AGNIR_DISCOVERY.md` when the operation depends on Core semantics or failure classification.

## Install or initialize Agnir

Treat the target Project root—not this Skill repository—as the authorized Project Entry Point.

Before changing any target-Project file, inspect the existing `README.md`, `AGENTS.md`, `AGNIR.yaml`, and any `.agnir/` content. Preserve unrelated Project documentation and Agent instructions. Merge; do not destructively replace.

### Merge existing AGENTS.md safely

Handle the target Project's root `AGENTS.md` mechanically:

1. If `AGENTS.md` does not exist, create only a minimal Agent-instruction file containing an Agnir locator to README `Agnir Project Instructions`.
2. If `AGENTS.md` already exists, preserve its existing unrelated content and add only the minimal Agnir locator. Do not rewrite, reorder, summarize, normalize, or delete existing Project instructions merely to install Agnir.
3. If an equivalent Agnir locator already exists, treat the merge as idempotent; do not add another copy.
4. Keep `AGENTS.md` locator-only for Agnir. Do not copy Current State, Next Actions, Decisions, Evidence, checkpoint procedure, or the full activation contract into `AGENTS.md`.
5. Before writing, detect material instruction conflicts. Examples include an existing instruction not to read/follow `README.md`, not to read `AGNIR.yaml`, not to use Agnir, or an existing Agnir instruction that points to a competing canonical location.
6. If a material conflict exists and resolving it would require deleting, overriding, or reinterpreting an existing Project instruction, **do not guess and do not overwrite it**. Stop the Agnir activation rewrite, report the exact conflict to the Principal, and do not claim installation complete until the conflict is explicitly resolved.

Prefer detecting conflicts during this preflight before making any Agnir installation writes. A partial setup must never be reported as a completed installation, and fresh activation must remain the completion gate.

For the reference `repository-filesystem/0.1` setup:

1. Create or validate top-level `AGNIR.yaml` with:
   - `agnir.version: "0.1"`;
   - `agnir.discovery_profile: "repository-filesystem/0.1"`;
   - a non-empty durable `project.identity`;
   - locators for Current State, Next Actions, Decisions, and Evidence.
2. Unless the Project already has an intentionally compatible layout, use:
   - `.agnir/state.md`;
   - `.agnir/next-actions.md`;
   - `.agnir/decisions.md`;
   - `.agnir/evidence/`.
3. Create the declared durable memory with concise initial Project truth. Persist at least one initialization evidence file when Evidence is declared.
4. In the target Project's `README.md`, create or update a canonical section headed exactly `## Agnir Project Instructions`. It must tell future Agents, before Project work, to:
   - treat the Project root as the authorized Project Entry Point;
   - read top-level `AGNIR.yaml`;
   - load Current State and Next Actions;
   - load Decisions and Evidence when relevant;
   - prefer durable Agnir Project truth over chat history or private Agent memory unless superseded by newer Principal instruction or directly observed current Project fact;
   - checkpoint material state, next-action, decision, and evidence changes when saving progress or finishing work;
   - treat an authorized request to commit Project changes as a checkpoint boundary: reconcile material continuity before the VCS commit, prefer code and Agnir changes in one revision, and treat a commit-and-push request as checkpoint + commit + push + verification when repository context applies.
5. Create or update root `AGENTS.md` according to **Merge existing AGENTS.md safely** above so it points to the README `Agnir Project Instructions` section and does not fork a second copy of the full Agnir contract.
6. Validate every locator and Project identity.
7. Finish with a fresh repository activation test using only the target Project root:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

Repository activation is incomplete if continuation from the Project root still depends on the installation conversation or the installing Agent's private memory. This repository-layer check remains the `fresh activation test`; it does not by itself prove execution-surface activation.

### Complete execution-surface activation

Repository activation and execution-surface activation are separate completion dimensions. After the repository activation test, inspect whether the current execution surface will give a future fresh context enough persistent information to reach the authorized Project Entry Point and its Agnir activation route.

1. If the execution surface automatically starts future Project work from the authorized Project root and inspects the Project instruction route, report execution-surface activation as **not separately required**.
2. If the execution surface requires persistent workspace/project configuration, configure that locator when the available tools and Principal authority allow it.
3. If the execution surface requires such configuration but the Agent cannot modify it directly, produce a **copy-ready execution-surface handoff**, ask the Principal to append or merge it into the surface's persistent Project/workspace instructions, preserve unrelated existing instructions, and report execution-surface activation as **pending user configuration**.
4. Keep the handoff locator-only. Do not copy Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure into execution-surface settings. The surface configuration points to the Project; the Project remains canonical.
5. Do not report full fresh activation as passed while required execution-surface configuration is still pending or unverified. Report repository activation and execution-surface activation separately.
6. After required configuration is applied, verify from a genuinely fresh execution context when possible. If a fresh-context test cannot be performed, report verification as pending rather than claiming success.

For a **ChatGPT Project** backed by a repository declared under `extensions.agnir/repository`, and when ChatGPT does not automatically inspect the repository's Project instructions, generate a block equivalent to the following with the target Project's actual values:

```text
Agnir Project bootstrap

Canonical Project: <owner/repository>
Authoritative ref: <ref>

At the first substantive turn of every new conversation, open the canonical Project repository, read root AGENTS.md, and follow its Agnir activation locator before doing Project work.

Load the Project continuity declared by AGNIR.yaml. Treat repository-managed Agnir state as canonical durable Project truth; ChatGPT Project memory and conversation context are working memory only.

When Project work materially changes durable continuity, follow the Project's Agnir checkpoint instructions before finishing, committing, or pushing.
```

Ask the Principal to **append or merge** this block into the ChatGPT Project's persistent Instructions; do not overwrite unrelated existing Project Instructions. The block is an execution-surface adapter, not Agnir Core and not a second canonical copy of Project memory.

## Upgrade an existing Agnir Project

Upgrade is **not re-initialization**. Start by activating the existing Project and loading its authoritative continuity. Preserve the Project identity, memory locators, durable State / Next Actions / Decisions / Evidence, unrelated README content, unrelated `AGENTS.md` instructions, and unrelated manifest extensions unless a separately authorized migration explicitly changes them.

A short user request such as `Upgrade Agnir to the latest stable release: https://github.com/iorLab/agnir` is sufficient.

### Resolve the upgrade target

1. Resolve the requested Agnir distribution source and target release.
2. When the Principal asks for the **latest stable release**, use an actually published stable release/tag. **Do not silently treat `main`, another moving branch, or an untagged revision as stable.**
3. A pre-release branch or explicit revision may be used only when the Principal explicitly requests or authorizes that non-stable target.
4. Record enough target provenance to make the applied operational package reproducible.

### Classify before mutating

Compare the existing Project's `agnir.version` and `agnir.discovery_profile` with the target:

- **no-op** — the same operational package provenance is already applied and no material activation/procedure drift exists;
- **compatible operational upgrade** — Core and profile compatibility lines are unchanged, but the operational package/procedure is newer or the Project has no recorded operational provenance;
- **migration required** — Core or profile compatibility line changes. Do not silently rewrite the Project to the new line. Surface migration-required semantics equivalent to `AGNIR_UPGRADE_MIGRATION_REQUIRED` and follow a separately authorized migration procedure.

A Project created before operational provenance existed is still a valid Agnir Project. Missing provenance does not justify re-initialization; after Core/profile compatibility is validated, it is a compatible-upgrade input.

### Apply a compatible operational upgrade

For `repository-filesystem/0.1`:

1. Preserve `project.identity`, all `memory` locators, existing durable memory content, and unrelated `extensions`.
2. Non-destructively merge the target Agnir activation/procedure contract into README `Agnir Project Instructions` and preserve the locator-only `AGENTS.md` behavior.
3. Record the applied operational package under the optional reference extension:

```yaml
extensions:
  agnir/operations:
    distribution: "agnir-agent-skill"
    release: "<stable repository release>"
    source: "iorLab/agnir"
    applied_revision: "<immutable source revision>"
```

The operational extension records which distribution procedure was applied. It does **not** replace `agnir.version`, `agnir.discovery_profile`, or Project identity and is not an Agnir Core requirement.
4. Reconcile any material upgrade facts into Agnir continuity. Evidence should identify the previous operational baseline when known, the target release/revision, classification, and fresh-activation result.
5. If the Project is in VCS, publish the compatible upgrade and its Agnir checkpoint as one coherent revision when possible; do not create a chain of per-file upgrade commits.
6. Finish with the same repository activation test and execution-surface activation evaluation required after initialization. The upgrade is incomplete for a surface that requires persistent configuration until that configuration is applied or explicitly reported as pending.

If the target procedure is already applied and durable truth did not change, upgrade evaluation is a no-op: do not rewrite README, manifest, memory, Evidence, or create a repository revision just to say the check occurred.

## Resume or use an existing Agnir Project

Do not ask the user for another Agnir bootstrap prompt.

Follow the target Project's durable activation instructions. For the reference repository/filesystem convention:

1. read root `AGENTS.md`;
2. follow it to README `Agnir Project Instructions`;
3. read `AGNIR.yaml`;
4. validate Core/profile compatibility and Project identity;
5. load Current State and Next Actions;
6. load Decisions and Evidence when relevant;
7. then perform the user's actual Project task.

If the execution surface does not automatically inspect Project instruction files, use its one-time persistent Project/workspace configuration to reach the authorized Project Entry Point. If that configuration is missing, treat it as an activation repair/handoff problem; do not make the user repeat Agnir's internal procedure every session.

Normal resume does not automatically upgrade Agnir. Upgrade checks or mutations happen only according to explicit Principal intent or a durable Project upgrade policy. This keeps an initialized Project resumable without requiring network access to the Agnir distribution source.

## Checkpoint

At an intentional checkpoint, save-progress, handoff, finish boundary, or repository commit boundary:

1. reconcile current Project truth rather than appending a raw transcript;
2. classify only material changes: current facts to Current State, outstanding actionable work to Next Actions, accepted durable choices to Decisions, and only recovery/audit/material-claim support to Evidence;
3. if the reconciled durable truth already matches the authoritative Agnir memory, treat the checkpoint as a **no-op**: do not create evidence, rewrite memory, or create a repository revision merely to record that evaluation occurred;
4. when material continuity changed, construct the complete candidate checkpoint before publishing authoritative memory;
5. publish the candidate using the active backend's atomic publication primitive when available; otherwise use durable generation/revision/transaction semantics sufficient to keep a fresh resolver from accepting mixed checkpoint generations;
6. if the authoritative revision changed since the checkpoint base was read, do not silently overwrite it; surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve current Project truth, and reconcile again;
7. verify the Discovery Record and Locator Chain resolve the resulting authoritative memory coherently;
8. ensure a fresh Executor can resume without private conversation context.

Do not require every checkpoint to modify all four durable semantic categories. Minimize writes to the categories whose durable truth actually changed.

## Commit and push integration

Interpret repository commit/push requests by intent and context, not by global string matching.

- In a repository/VCS context, `commit`, `提交`, `提交代码`, and equivalent wording normally mean: **checkpoint evaluation → reconcile if material → create the requested VCS commit**.
- `commit and push`, `提交推送`, and equivalent wording normally mean: **checkpoint evaluation → commit → push → verify the intended authoritative remote/ref when declared**.
- A bare word such as `提交` outside repository context can mean submitting a form, document, job, or other non-VCS action; do not trigger Agnir merely because the literal word matches.

For an authorized commit request:

1. load and validate current Agnir continuity before building the commit;
2. reconcile material continuity changes;
3. if both Project changes and Agnir memory changed, prefer staging them into **one VCS revision** so the revision itself is a coherent Project snapshot;
4. do not create a second checkpoint-only commit after the Project commit unless a later independent material truth change requires it;
5. if checkpoint evaluation is a no-op, commit only the requested Project changes;
6. treat the resulting VCS revision identifier as a backend receipt when useful; do not try to embed a commit SHA inside the content whose commit would determine that same SHA.

For an authorized push request, perform the commit-boundary procedure first. After push/publication, if the Project declares a canonical repository and authoritative ref, verify that the intended revision reached that ref before reporting completion.

When a commit created elsewhere is merely observed—human CLI, IDE, web UI, CI, another Agent, or automation—trigger **checkpoint evaluation**, not unconditional checkpoint mutation. If the durable Project truth remains coherent, do nothing. If material truth drift is detected, reconcile at the next authorized checkpoint boundary or according to Project policy.

Git hooks such as `pre-commit` or `pre-push` may be used by an implementation to surface these events, but hooks are optional adapter mechanisms. Never make future Agnir discovery or continuity depend on a hook having run.

## Repair

Repair the earliest faulty layer without inventing Project state.

- Missing activation locator or canonical README instruction: repair the Project instruction route while preserving unrelated content.
- Missing required execution-surface Project/workspace locator: configure it when authorized, or produce the copy-ready surface handoff and report `pending user configuration`; do not claim full activation passed.
- Existing `AGENTS.md` conflict: preserve the existing instruction, surface the conflict, and require explicit Principal resolution before replacing or overriding it.
- Missing or incompatible `AGNIR.yaml`: surface or repair the repository/filesystem discovery anchor according to the active profile.
- Identity mismatch: do not silently adopt another Project's memory.
- Broken required locator: repair the declared locator or durable object; do not search arbitrary sibling repositories, home directories, old chats, or historical layouts.
- Authorization, cycle, stale, or inconsistency failures: preserve the semantic failure rather than guessing around it.

After material activation or discovery repair, rerun repository activation/cold start from the Project Entry Point and reevaluate execution-surface activation.

## Report completion

For installation, report only the useful result: which Project was initialized, where the Agnir anchor and durable memory live, whether README/`AGENTS.md` activation was installed or merged, whether any existing instruction conflict blocked completion, **repository activation status**, and **execution-surface activation status**. If surface configuration is pending, include the copy-ready handoff and do not report full fresh activation as passed. Do not make the user learn or repeat the internal checklist.

For upgrade, report the previous operational baseline when known, target release/revision, classification (`no-op`, compatible upgrade, or migration required), which Agnir-owned activation/provenance surfaces changed, whether Project identity/memory locators were preserved, repository activation result, execution-surface activation result when relevant, and repository revision when relevant.

For resume/checkpoint/commit/push/repair, report material continuity changes, whether checkpoint evaluation was a no-op or published transition, the resulting repository revision/remote verification when relevant, remaining blockers, and any failure class that prevents safe resumability.
