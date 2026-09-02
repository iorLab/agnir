# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Core 0.2 Parallel Continuity — 2026-09-02

- The earlier decision to defer a generic lineage abstraction pending non-VCS evidence is superseded. Core `0.2` Continuity Lineage now has VCS, non-VCS, concrete profile/migration, and real-Project consumer evidence.
- Core `0.2` generalizes Core `0.1`'s single implicit continuity line into multiple independently advancing **Continuity Lineages** owned by one Project.
- Project identity and lineage identity are distinct. Creating, selecting, advancing, integrating, renaming a selector, or retiring a lineage does not implicitly create a new Project.
- A lineage identity is a durable logical semantic within Project scope. Core does not mandate its serialization, URI form, path, database representation, or global uniqueness.
- Backend selector/locator values and revision receipts are not lineage identity. Git refs/worktrees are selector/binding context; Git SHAs, database generations, and snapshot revisions are checkpoint receipts/conflict tokens.
- Ordinary lineage-local work resolves exactly one lineage. Generic selection precedence is explicit Principal/task/adapter input → already-selected execution/profile/backend context → explicitly declared default.
- Core does not require enumerating or scanning sibling lineages. Missing deterministic selection surfaces `AGNIR_LINEAGE_REQUIRED`; selected missing/unbound lineage semantics fail rather than silently falling back.
- Checkpoints are lineage-local by default. A checkpoint on one lineage must not silently mutate another lineage's authoritative continuity.
- Lineage integration is reconciliation, not source-continuity copying. Target continuity is reconciled from actual integration candidate, previous target truth, relevant source continuity/Evidence, and Principal intent/policy.
- Integrated Project state and reconciled target continuity must publish as one coherent authoritative target transition.
- Staged integration candidates are optimistic over authoritative target and relevant source generations. If either advances before publication, the candidate must fail/re-resolve rather than overwrite newer truth.
- Cross-Project integration does not bypass Project identity checks.
- Working normative draft: `spec/AGNIR_CORE_0_2_DRAFT.md`.

## Selector/binding semantics for VCS-backed lineages

- A selected Git ref/worktree is not itself the logical lineage identity.
- Agnir-aware branch fork preserves Project identity and inherited baseline but establishes a new logical lineage identity and a new selector→lineage binding.
- A conforming Agnir-controlled lineage fork must publish the new logical lineage identity, selector binding, and coherent inherited/reconciled continuity together. Sequential ref-visible writes that temporarily expose a copied source binding under the new selector are not the intended safe fork path.
- Explicit branch/ref rename or rebind may preserve logical lineage identity while changing the selector string.
- External branch copy/rename that carries stale or ambiguous binding metadata must not be guessed as either fork or rename. It is an explicit classification/repair condition.
- Commit/revision rewrite may change checkpoint receipt without changing Project identity, lineage identity, or otherwise coherent lineage truth.
- `authoritative_ref` remains repository publication authority/default only when policy says so; it is not Project identity, lineage identity, or necessarily the active selector.

## Core 0.2 discovery and repository/filesystem profile

- Core `0.2` ordinary discovery resolves one selected lineage plus that lineage's durable memory locators; Core does not require sibling-lineage enumeration.
- `repository-filesystem/0.2` is the concrete draft profile in `profiles/REPOSITORY_FILESYSTEM_0_2_DRAFT.md`.
- Its manifest semantics require Core/profile `0.2`, one durable `project.identity`, one selected logical `continuity.lineage`, and Current State / Next Actions / Decisions / Evidence locators.
- `schemas/agnir-manifest-0.2.schema.json` is the experimental schema. Published `schemas/agnir-manifest.schema.json` remains the Core/profile `0.1` schema.
- Stable `repository-filesystem/0.1` discovery must reject Core/profile `0.2` rather than silently reinterpret it.
- A VCS-aware profile/adapter may persist selector binding separately from logical `continuity.lineage`; mismatch is not automatic lineage creation.

## Core 0.1 → 0.2 migration

- Core/profile compatibility-line changes remain migration-required, not compatible upgrades.
- A Core `0.1` Project's single implicit continuity line becomes exactly one initial/default Core `0.2` logical lineage while preserving Project identity and existing Current State / Next Actions / Decisions / Evidence.
- Migration must be explicit, idempotent, cold-start verifiable, and conflict-safe.
- Storage-neutral migration conformance and concrete repository/filesystem migration conformance both pass on the current development branch.
- Concrete `AGNIR.yaml` migration stages against the authoritative source manifest, rejects stale source mutation, writes the Core/profile `0.2` candidate through atomic replace, then verifies fresh `repository-filesystem/0.2` discovery.
- Repeating the same migration is a no-op; attempting to silently rebind an already migrated Project to a different initial lineage is a migration conflict.

## Transactional checkpoint and integration publication

- A checkpoint is an authoritative continuity transition, not an activity-log append.
- Reconcile Project truth first. If authoritative continuity already represents it, checkpoint evaluation is a no-op.
- Material checkpoints construct a coherent candidate before publication and minimize writes to semantic categories that changed.
- Completed checkpoints must not expose mixed generations as coherent truth. Use atomic publication where available or durable generation/revision/transaction/pointer semantics otherwise.
- Stale-base writers must not silently overwrite newer truth; surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile.
- Checkpoint completion includes post-publication discovery verification.
- For lineage integration, target advancement is a publication boundary: stage candidate without publishing target → reconcile target → construct checkpoint → publish integrated Project + reconciled target continuity together → fresh verify.
- Merge-first/follow-up-repair is recovery-oriented, not the intended Agnir-controlled normal path when it knowingly exposes wrong target continuity.

## Development branch governance — 2026-09-02

- `main` remains the only intended long-lived authoritative branch for `iorLab/agnir`.
- Draft PR `#4` (`feature/multibranch-continuity`) carries the VCS branch-continuity evidence line.
- Draft PR `#5` (`feature/core-0.2-lineage`) is stacked on PR `#4` and carries the backend-neutral Core `0.2`, profile, binding, migration, and real-consumer evidence.
- Temporary development branches may carry branch-local continuity without redefining Project identity or stable publication authority.
- PR `#4` / `#5` eventual integration into `main` must construct final `main` continuity before the revision that advances `main`; ordinary server-side merge-first/follow-up-repair is not the intended safe integration path.

## Real-Project validation result — 2026-09-02

- The first required real Core `0.2` consumer validation is complete in Svif on temporary branches; Svif authoritative `main` remained unchanged.
- Svif preserved one Project identity across two genuinely divergent logical lineages with distinct VCS selector bindings and branch-local continuity.
- Both lineages advanced real Project content independently and passed their own product CI/fresh-discovery pressure.
- A two-parent integration candidate was constructed without advancing the target ref. Fresh ref reads proved the unpublished candidate coexisted with the unchanged target/source refs.
- The candidate retained target lineage/binding metadata while incorporating both Project changes; source lineage/selector metadata was reconciliation input, not target truth.
- Final target continuity was reconciled before publication. The target ref advanced once from the pre-integration target directly to the reconciled two-parent revision; the staged candidate never became target truth.
- The source ref and source-local continuity remained independently resumable after target publication.
- Post-publication verification exposed one brittle workflow-heading assertion, not a continuity defect. The test was corrected to assert stable binding-driven semantics and the full Svif product suite passed afterward.
- A later Svif completion checkpoint initially dropped still-valid Preview/Codex release obligations; an existing product test caught the omission. The durable Next Actions were repaired rather than weakening the test. This confirms branch-local continuity reconciliation must preserve unrelated still-valid Project obligations.
- Exact receipts are recorded in `.agnir/evidence/2026-09-02-svif-core-0.2-real-consumer-validation.md`.

## Agent-operable activation and execution surfaces

- Root `SKILL.md` remains the canonical Agent-facing Agnir operational package. Users provide intent; the Skill owns procedure.
- Agent-operable repository activation remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Execution-surface configuration is adapter/integration behavior, not Agnir Core or Project durable memory; it contains locator/bootstrap information only.
- Repository activation and execution-surface activation remain separate completion dimensions.

## Versioning and release direction

- Published stable compatibility remains Core `0.1`, `repository-filesystem/0.1`, repository release `0.1.1`.
- Immutable `v0.1.1` remains anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- Core `0.2` semantics, concrete migration, dual-backend/profile conformance, and the first Svif real-Project validation are now green. The remaining pre-RC protocol gate is safe integration into Agnir authoritative `main` plus authoritative-main conformance.
- If that integration remains green, prepare repository `v0.2.0-rc.1`, then final `v0.2.0` after release-candidate migration/install/resume verification.
- `v1.0.0` is a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a required count of pre-1.0 minor versions.

## Evidence and documentation

- Evidence is retained for recovery, audit, conformance, migration, or support of material claims; it is not an activity log.
- `REPOSITORY_TREE.md` is the structural responsibility map; `.agnir/evidence/` is represented by directory responsibility rather than per-file registration.
- `README.md` and `README.zh-CN.md` remain parallel entry documents and must preserve equivalent operational meaning when stable architecture/activation/continuity semantics change.
- Conformance tests should prefer stable protocol/profile/Project semantics over transient workflow-stage wording. Tests that intentionally preserve still-valid Project/release obligations remain valuable and should not be weakened merely because a feature workflow completes.
- Real mount-boundary behavior remains explicitly unproven until a genuine mount-capable environment is available.
