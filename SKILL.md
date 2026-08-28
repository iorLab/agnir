---
name: agnir
description: Install, initialize, use, checkpoint, resume, or repair Agnir durable Project continuity. Use when a user asks to install or initialize Agnir, make a Project resumable across Agents or conversations, recover an Agnir-enabled Project, checkpoint progress, or repair Agnir discovery/activation. The user-facing install request may be only a short intent statement; this Skill owns the full procedure.
---

# Agnir

Agnir is a project-owned durable continuity protocol. The Project owns the durable truth required to continue safely when Agents, conversations, execution environments, or storage implementations change.

Do not require the user to carry Agnir's implementation checklist in their prompt. A short request such as `Install and initialize Agnir for this Project` is sufficient once this Skill has been found. This file is the Agent-facing procedure.

## Determine the operation

Classify the request as one of:

- **install / initialize** — the target Project does not yet have a valid Agnir setup;
- **resume / use** — the Project is already Agnir-enabled;
- **checkpoint** — persist material continuity updates;
- **repair** — the Project intends to use Agnir but activation, discovery, identity, or locators are broken.

For repository/filesystem Projects, read `profiles/REPOSITORY_FILESYSTEM.md` when performing installation, activation repair, or discovery repair. Read `spec/AGNIR_CORE.md` and `spec/AGNIR_DISCOVERY.md` when the operation depends on Core semantics or failure classification.

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
   - checkpoint material state, next-action, decision, and evidence changes when saving progress or finishing work.
5. Create or update root `AGENTS.md` according to **Merge existing AGENTS.md safely** above so it points to the README `Agnir Project Instructions` section and does not fork a second copy of the full Agnir contract.
6. Validate every locator and Project identity.
7. Finish with a fresh activation test using only the target Project root:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

The installation is incomplete if future continuation still depends on the installation conversation or the installing Agent's private memory.

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

If the execution surface does not automatically inspect Project instruction files, treat that as one-time execution-surface configuration rather than a reason to make the user repeat Agnir's procedure every session.

## Checkpoint

At an intentional checkpoint, save-progress, handoff, or finish boundary:

1. reconcile current Project truth rather than appending a raw transcript;
2. update Current State with present facts required to continue safely;
3. update Next Actions with outstanding work, blockers, priorities, and intentional deferrals;
4. record accepted durable decisions and material rationale;
5. record only the Evidence needed for recovery, audit, or material claims;
6. verify the Discovery Record and Locator Chain still resolve the resulting authoritative memory;
7. ensure a fresh Executor can resume without private conversation context.

## Repair

Repair the earliest faulty layer without inventing Project state.

- Missing activation locator or canonical README instruction: repair the Project instruction route while preserving unrelated content.
- Existing `AGENTS.md` conflict: preserve the existing instruction, surface the conflict, and require explicit Principal resolution before replacing or overriding it.
- Missing or incompatible `AGNIR.yaml`: surface or repair the repository/filesystem discovery anchor according to the active profile.
- Identity mismatch: do not silently adopt another Project's memory.
- Broken required locator: repair the declared locator or durable object; do not search arbitrary sibling repositories, home directories, old chats, or historical layouts.
- Authorization, cycle, stale, or inconsistency failures: preserve the semantic failure rather than guessing around it.

After material activation or discovery repair, rerun fresh activation/cold start from the Project Entry Point.

## Report completion

For installation, report only the useful result: which Project was initialized, where the Agnir anchor and durable memory live, whether README/`AGENTS.md` activation was installed or merged, whether any existing instruction conflict blocked completion, and whether fresh activation passed. Do not make the user learn or repeat the internal checklist.

For resume/checkpoint/repair, report material continuity changes, remaining blockers, and any failure class that prevents safe resumability.
