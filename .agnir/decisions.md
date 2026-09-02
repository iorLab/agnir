# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded implementation chronology remains available through Git history and `.agnir/evidence/`; it is not repeated here unless still required for current Project truth.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Name origin and product meaning — 2026-09-01

- The project name **Agnir** is taken from Icelandic `agnir`, the nominative plural of `ögn`, meaning a tiny bit or particle.
- The name maps to Agnir's product model: durable Project continuity is composed from small, discoverable pieces of Project truth rather than depending on one Executor's private context or one monolithic conversation transcript.
- The canonical conceptual pieces are Current State, Next Actions, Decisions, and Evidence / Checkpoints. Together they let a fresh compatible Executor reconstruct enough Project truth to continue safely.
- This is a naming and product metaphor, not a Core storage-layout requirement. Implementations are not required to persist each semantic category as a physically separate file, row, object, or backend record.

## Discovery and repository/filesystem profile

- `AGNIR.yaml` is the top-level discovery anchor for `repository-filesystem/0.1`; that filename/layout is profile behavior, not a Core requirement.
- `.agnir/` is the recommended colocated memory layout in this repository, but `AGNIR.yaml` locators are authoritative.
- Cold-start discovery begins from an authorized Project Entry Point, validates version and Project identity, resolves required continuity, and must not guess through arbitrary sibling repositories, old chats, predecessor paths, or private Executor memory.
- Discovery preserves explicit failure semantics including not-found, ambiguity, unsupported version, Project mismatch, unresolvable, unauthorized, cycle, stale, and inconsistent state.
- Current State and Next Actions from different known checkpoint generations must not be accepted as one coherent Project truth.

## Agent-operable activation and Skill packaging

- Root `SKILL.md` is the canonical Agent-facing Agnir operational package. User-facing install/upgrade requests remain short intent statements plus the canonical distribution location; the user does not carry Agnir's internal procedure.
- An initialized Agent-operable repository Project persists its Project-owned activation route through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Target `AGENTS.md` remains locator-only for Agnir. Existing unrelated Project-owned instructions are preserved; equivalent locators are idempotent; material instruction conflicts are surfaced to the Principal and block completed repository activation until explicitly resolved.

## Execution-surface activation handoff — 2026-09-01

- **Repository activation and execution-surface activation are separate completion dimensions.** A repository can be correctly self-describing while a surrounding execution surface still lacks the persistent locator needed for a future fresh context to reach that repository.
- Execution-surface configuration is an adapter/integration concern, not Agnir Core and not Project-owned durable memory. It must contain only enough persistent locator/bootstrap information to reach the authorized Project Entry Point and then defer to the Project's canonical activation route.
- When the active surface automatically begins Project work from the authorized Project root and inspects Project instruction files, no separate surface configuration is required.
- When persistent surface configuration is required and the active Agent can modify it with Principal authority, the Agent should configure it. When it cannot, installation/upgrade must produce a copy-ready handoff, preserve unrelated existing surface instructions, and report `pending user configuration` rather than pretending the surface is ready.
- Required surface configuration that is pending or unverified blocks a claim that **full fresh activation passed**. Completion reports distinguish repository activation status from execution-surface activation status.
- ChatGPT Project Instructions are the first concrete execution-surface adapter for this rule. The handoff points to canonical repository/ref, root `AGENTS.md`, and `AGNIR.yaml`; it must not duplicate Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure.
- A fresh-context test is the preferred completion gate after required surface configuration is applied. If the execution surface cannot be genuinely restarted/tested by the current Executor, verification remains explicitly pending.
- This repair shipped in repository release `v0.1.1` as an operational Skill/integration patch within Core `0.1` and `repository-filesystem/0.1`; it does not change either compatibility line.

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
- When Project changes and Agnir continuity changes can be represented in one VCS revision, implementations should publish them together in that one revision instead of creating a follow-up checkpoint-only revision.
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
- `README.md` and `README.zh-CN.md` are parallel entry documents. Changes to architecture, activation, execution-surface handoff, durable-memory/checkpoint semantics, Project boundary, or continuity flow update both languages in the same change set.

## README entry-point information architecture — 2026-09-01

- Before the Architecture Diagram, both READMEs are deliberately limited to a concise Project identity/name explanation followed by: **Start Here / 从这里开始** for users; the canonical **Agnir Project Instructions** for Agents; and **What Agnir Adds to a Project / Agnir 会给 Project 增加什么** as a concrete user-facing map of the initialized repository/filesystem Project surface.
- `Start Here` contains only minimal install, upgrade, and normal-use actions. User-facing install and upgrade intents remain one sentence each; users do not carry Agnir's internal implementation checklist.
- `Agnir Project Instructions` remains the canonical heading resolved by `AGENTS.md` and is explicitly marked as Agent guidance for human readers.
- `What Agnir Adds to a Project` shows the reference Skill's non-destructive Project surface: `AGENTS.md`, `AGNIR.yaml`, the README instruction section, and the declared `.agnir/` continuity layout with State, Next Actions, Decisions, and Evidence responsibilities. It must state that `AGNIR.yaml` locators are authoritative and that the file layout is profile/reference behavior rather than a universal Core requirement.
- Execution-surface bootstrap is shown outside the Project-owned surface. If needed, it is labeled as an edit/append-only locator rather than a new canonical memory surface.
- The Architecture Diagram mirrors the Project surface without duplicating the full file tree: `AGENTS.md` and `README.md` are non-destructive **EDIT / add-entry-only** surfaces, while `AGNIR.yaml` and the reference `.agnir/` continuity layout are Agnir **ADD** surfaces feeding discovery and Core continuity semantics.
- The Continuity Flow describes post-install resume/runtime behavior and may begin with resolving a persistent execution-surface Project locator when the surface requires one; it must not turn surface settings into Project truth.
- Packaging rationale, compatibility explanation, release detail, repository structure, and deeper implementation/conformance explanation belong after the architecture entry point or in dedicated documents.
- Bilingual documentation must preserve the same audience split and operational meaning without requiring literal sentence-for-sentence translation.
- Conformance enforces the ordering `Start Here -> Agnir Project Instructions -> installed Project surface -> Architecture`, canonical install/upgrade intents, and the required surface markers so the README front matter remains concrete without drifting back into a full implementation checklist.

## Core 0.2 Parallel Continuity — 2026-09-02

- Core `0.2` generalizes Core `0.1`'s single implicit continuity line into multiple independently advancing **Continuity Lineages** owned by one Project.
- Project identity and lineage identity are distinct. Creating, selecting, advancing, integrating, renaming a selector, or retiring a lineage does not implicitly create a new Project.
- A lineage identity is a durable logical semantic within Project scope. Core does not mandate its serialization, URI form, path, database representation, or global uniqueness.
- Backend selector/locator values and revision receipts are not lineage identity. Git refs/worktrees are selector/binding context; Git SHAs, database generations, and snapshot revisions are checkpoint receipts/conflict tokens.
- Ordinary lineage-local work resolves exactly one lineage using explicit Principal/task/adapter selection, already-selected trusted execution/profile/backend context, or an explicitly declared default. Core does not require sibling enumeration/scanning.
- A selected missing/unbound lineage fails explicitly rather than silently falling back.
- Checkpoints are lineage-local by default.
- Integration is target reconciliation, not source-continuity copying. Target truth is reconciled from the actual integration candidate, previous target continuity, relevant source continuity/Evidence, and Principal intent/policy.
- Integrated Project result + reconciled target continuity must publish as one coherent target transition. Source or target advancement before publication invalidates a stale candidate.
- Cross-Project integration never bypasses Project identity checks.
- Working pre-RC Core document is `spec/AGNIR_CORE_0_2_DRAFT.md` until the release-candidate change deliberately promotes the intended contract.

## VCS selector/binding and lineage fork — 2026-09-02

- A selected Git ref/worktree is not itself logical lineage identity.
- Agnir-aware branch fork preserves Project identity and inherited baseline while establishing a new logical lineage identity and selector→lineage binding.
- When Agnir controls the fork, new lineage identity, selector binding, and coherent inherited/reconciled continuity must publish together. A sequence of independently visible ref writes that temporarily exposes copied source binding under the new selector is not the intended safe path.
- Explicit ref rename/rebind may preserve logical lineage identity while changing selector string.
- External branch copy/rename with stale or ambiguous binding metadata is a classification/repair condition; Agnir must not guess fork vs rename.
- Commit/history rewrite may change receipt without changing Project identity or logical lineage identity.
- `authoritative_ref` is repository publication authority/default only when policy says so; it is not Project identity, lineage identity, or necessarily the active selector.

## Repository/filesystem 0.2 and migration — 2026-09-02

- `repository-filesystem/0.2` is the pre-RC concrete profile candidate. Ordinary discovery resolves one selected logical `continuity.lineage` plus its durable memory locators; sibling-lineage enumeration is not required.
- Stable `repository-filesystem/0.1` discovery rejects Core/profile `0.2` instead of silently reinterpreting it.
- Core/profile compatibility-line changes are migration-required, not compatible upgrades.
- A Core `0.1` Project's single implicit line becomes exactly one initial/default Core `0.2` lineage while preserving Project identity and existing Current State / Next Actions / Decisions / Evidence.
- Migration is explicit, idempotent, cold-start verifiable, and conflict-safe. Concrete `AGNIR.yaml` migration rejects stale source mutation and verifies fresh `repository-filesystem/0.2` discovery after publication.

## Branch-aware VCS integration publication — 2026-09-02

- Feature-branch checkpoints verify their actual destination ref; `authoritative_ref` does not silently redirect ordinary feature work to `main`.
- For Agnir-controlled lineage integration, target-ref advancement is a publication boundary: stage the candidate while target stays unchanged → reconcile target continuity → construct the final target checkpoint → publish integrated Project + reconciled target continuity together → fresh verify.
- A known merge-first/follow-up-continuity-repair sequence is recovery-oriented, not the intended conforming normal path.
- The same preservation rule applies to unrelated still-valid target obligations: target reconciliation must not erase stable release, activation, upgrade, or distribution truth merely because the feature line focused on another subsystem.

## Real Svif Core 0.2 validation — 2026-09-02

- Svif completed the first real Core `0.2` consumer validation without changing Svif authoritative `main`.
- One Svif Project identity survived explicit `0.1`→`0.2` migration and two genuinely divergent logical lineages with different selector bindings and branch-local continuity.
- Both lineages made distinct real Project changes and passed independent CI/fresh-discovery pressure.
- A two-parent integration candidate existed while target/source refs remained unchanged; its tree retained target lineage/binding truth while incorporating both Project changes.
- Final target continuity was reconciled before publication. The target ref advanced once directly to the reconciled two-parent revision; the staged candidate never became target truth.
- Source continuity remained independently resumable after target publication.
- Real workflow pressure also showed that continuity reconciliation must preserve still-valid unrelated Project obligations and that conformance should test stable semantics rather than transient workflow headings.
- Exact receipts are retained in `.agnir/evidence/2026-09-02-svif-core-0.2-real-consumer-validation.md`.

## Versioning, release, and branch governance

- Published Core compatibility remains `0.1`; published repository/filesystem compatibility remains `repository-filesystem/0.1`; published repository SemVer remains `0.1.1` until an explicit new release.
- The execution-surface activation handoff repair remains the immutable `v0.1.1` operational patch anchored to exact verified revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- Repository release SemVer, Core compatibility, and profile/extension versions are distinct version layers. The intended next feature release is repository `v0.2.0` with Core compatibility `0.2` if the pre-RC main integration and RC gates pass.
- `v0.2.0-rc.1` should precede final `v0.2.0` and must exercise fresh installation plus explicit migration/resume from published `v0.1.1`.
- `v1.0.0` is a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a required count of pre-1.0 minor versions.
- `latest stable release` remains published `v0.1.1` until a newer stable tag/release is actually published; moving `main` or an RC is not silently treated as stable.
- `main` remains the only intended long-lived authoritative branch. Temporary feature/integration refs are evidence carriers and are not second continuity authorities.
- Real mount-boundary behavior remains explicitly unproven; ordinary directories are not accepted as substitute mount evidence.
