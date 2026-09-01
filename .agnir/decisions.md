# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded implementation chronology remains available through Git history and `.agnir/evidence/`; it is not repeated here unless still required for current Project truth.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Discovery and repository/filesystem profile

- `AGNIR.yaml` is the top-level discovery anchor for `repository-filesystem/0.1`; that filename/layout is profile behavior, not a Core requirement.
- `.agnir/` is the recommended colocated memory layout in this repository, but `AGNIR.yaml` locators are authoritative.
- Cold-start discovery begins from an authorized Project Entry Point, validates version and Project identity, resolves required continuity, and must not guess through arbitrary sibling repositories, old chats, predecessor paths, or private Executor memory.
- Discovery preserves explicit failure semantics including not-found, ambiguity, unsupported version, Project mismatch, unresolvable, unauthorized, cycle, stale, and inconsistent state.
- Current State and Next Actions from different known checkpoint generations must not be accepted as one coherent Project truth.

## Agent-operable activation and Skill packaging

- Root `SKILL.md` is the canonical Agent-facing Agnir operational package. User-facing install/upgrade requests remain short intent statements plus the canonical distribution location; the user does not carry Agnir's internal procedure.
- An initialized Agent-operable repository Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory, so normal continuation does not depend on the installation conversation or reopening the Skill repository.
- Target `AGENTS.md` remains locator-only for Agnir. Existing unrelated Project-owned instructions are preserved; equivalent locators are idempotent; material instruction conflicts are surfaced to the Principal and block completed installation until explicitly resolved.

## Transactional checkpoint semantics — 2026-09-01

- A checkpoint is an **authoritative continuity transition**, not merely a sequence of related writes.
- Checkpoint evaluation first reconciles Project truth and applies a materiality filter. If authoritative Agnir memory already represents the reconciled truth, the correct result is a **no-op**.
- When material continuity changed, an implementation should construct a coherent candidate before publication and minimize writes to semantic categories that actually changed.
- A completed checkpoint must not expose mixed old/new generations as coherent truth. Backends should use an atomic publication primitive when available; otherwise they must provide durable generation/revision/transaction/pointer semantics sufficient for a fresh resolver to reject mixed generations.
- A stale-base writer must not silently overwrite newer truth; it surfaces `AGNIR_CHECKPOINT_CONFLICT`, then re-resolves and reconciles.
- Checkpoint completion includes post-publication discovery verification.
- A backend-generated revision/transaction/commit identifier may serve as the checkpoint receipt without being embedded inside the content that determines it.

## Repository commit / push event semantics — 2026-09-01

- Repository/VCS intent is integration/profile behavior, not a Core VCS dependency.
- In repository context, an authorized request to `commit`, `提交`, `提交代码`, or equivalent is a checkpoint boundary. Agnir continuity is evaluated/reconciled **before** the VCS commit.
- When Project changes and Agnir continuity changes can be represented in one VCS revision, implementations should publish them together in that one revision instead of creating a follow-up checkpoint-only commit.
- `commit and push`, `提交推送`, or equivalent means checkpoint + commit + push + verification of the declared authoritative remote/ref when available.
- A commit observed after another human, Agent, IDE, CI, web UI, or automation action triggers checkpoint evaluation only; coherent unchanged continuity yields a no-op.
- `提交` is contextual integration vocabulary, not a universal literal trigger.
- Git hooks may capture events but remain optional adapter mechanisms and must never become Agnir discovery/continuity dependencies.

## Existing Project upgrade semantics — 2026-09-01

- `upgrade` is a first-class Agnir Skill operation and is **not re-initialization**.
- A compatible upgrade begins by activating the existing Project and preserves `project.identity`, declared memory locators, durable continuity contents, unrelated README/`AGENTS.md` instructions, and unrelated manifest extensions.
- Core/profile compatibility lines classify the operation. When target Core/profile remain `0.1` / `repository-filesystem/0.1`, operational procedure updates may be applied compatibly. If either compatibility line changes, the operation is migration-required and must surface semantics equivalent to `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently rewriting the Project.
- Projects created before operational provenance existed remain valid. Missing provenance is not a reason to re-initialize or rebuild `.agnir/`.
- Repository/filesystem Projects may record applied operational provenance under optional `extensions.agnir/operations` with `distribution`, repository `release`, `source`, and immutable `applied_revision`. This metadata does not redefine Core/profile compatibility or Project identity.
- `latest stable` means an actually published stable tag/release. Moving `main`, another moving branch, or an untagged revision must not be silently treated as stable. Non-stable targets require explicit Principal authorization.
- Re-applying the same operational provenance with no material activation drift is a no-op.
- Compatible VCS upgrades should merge Agnir-owned procedure/provenance and material continuity into one coherent revision when possible, then pass fresh activation.
- Normal resume does not implicitly check for or install upgrades; a Project must remain resumable without network access to the Agnir distribution source.

## Evidence and repository documentation

- Evidence is retained only when needed for recovery, audit, conformance, or support of material claims; it is not an activity log.
- `REPOSITORY_TREE.md` is a structural responsibility map. `.agnir/evidence/` is represented by directory responsibility rather than enumerating every Evidence filename.
- `README.md` and `README.zh-CN.md` are parallel entry documents. Changes to architecture, activation, durable-memory/checkpoint semantics, Project boundary, or continuity flow update both languages in the same change set.

## Versioning, release, and branch governance

- Core compatibility is `0.1`; repository/filesystem compatibility is `repository-filesystem/0.1`; repository SemVer for the initial publication is `0.1.0`.
- Transactional checkpoint, commit-event, and compatible existing-Project upgrade semantics are incorporated before the first `v0.1.0` publication and therefore belong to the initial operational distribution line.
- `RELEASE.md` is the publication contract. A material pre-publication change must pass the full conformance workflow on its exact revision before that revision is considered the publication candidate.
- `main` is the only long-lived authoritative branch. Historical predecessor/branch recovery uses immutable commit SHAs and Git history rather than live legacy refs.
- Real mount-boundary behavior remains explicitly unproven; ordinary directories are not accepted as substitute mount evidence.
