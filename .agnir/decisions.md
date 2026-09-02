# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Core 0.2 Parallel Continuity — 2026-09-02

- The earlier decision to defer a generic lineage abstraction pending non-VCS evidence is **superseded for active design work**. The Principal authorized Core `0.2` design, and a non-VCS SQLite transactional reference is now part of the conformance workstream.
- Core `0.2` generalizes the Core `0.1` single implicit continuity line into multiple independently advancing **Continuity Lineages** owned by one Project.
- Project identity and lineage identity are distinct. Creating/selecting/advancing/integrating a lineage does not implicitly create a new Project.
- A lineage identity is a durable logical semantic within Project scope. Core does not mandate its serialization, key name, URI form, physical path, database representation, or global uniqueness.
- Backend revision receipts—Git SHAs, database generations, snapshot revisions, object versions, or equivalents—are checkpoint receipts, not lineage identity.
- Ordinary lineage-local work resolves exactly one lineage. Generic selection precedence is explicit Principal/task/adapter input → already-selected execution/profile/backend context → explicitly declared default.
- Core does not require enumerating or scanning sibling lineages. If none can be selected, surface `AGNIR_LINEAGE_REQUIRED`. If a specifically selected lineage does not resolve, surface `AGNIR_LINEAGE_NOT_FOUND` rather than silently falling back.
- Checkpoints are lineage-local by default. A checkpoint on one lineage must not silently mutate another lineage's authoritative continuity.
- Lineage integration is **reconciliation**, not source-continuity copying. The target must reconcile the actual integration candidate, previous target continuity, relevant source continuity/Evidence, and Principal intent/policy.
- Integrated Project state and reconciled target continuity must publish as one coherent authoritative target transition. A known intermediate target whose Project result and continuity disagree is not a conforming completed integration.
- Staged integration candidates are optimistic over authoritative target and relevant source generations. If either advances before publication, the candidate must fail/re-resolve rather than overwrite newer truth.
- Cross-Project integration does not bypass Project identity checks.
- Working normative draft: `spec/AGNIR_CORE_0_2_DRAFT.md`.

## Core 0.2 backend-neutral conformance

- Core `0.2` cannot be accepted from Git/VCS evidence alone.
- Required evidence includes at least one materially VCS-backed model and one materially non-VCS model satisfying the same Core invariants.
- `agnir/vcs-branch-continuity/0.1` remains the VCS evidence/mapping layer; branch/ref/worktree concepts remain outside Core.
- `conformance/sqlite_lineage_reference.py` is the first non-VCS model. Its lineages are logical SQLite namespaces, publication uses SQLite transactions, and generations are backend receipts/conflict tokens.
- Dual-backend conformance must pressure: shared Project identity, durable logical lineage identity, selection, isolation, reconciliation, coherent publication, stale-candidate rejection, cross-Project rejection, and fresh resume.

## Core 0.2 discovery direction

- A Core `0.2` ordinary discovery result identifies one selected lineage plus that lineage's durable memory locators.
- The Core semantic shape is equivalent to Project identity + selected Continuity Lineage identity + Current State / Next Actions / Decisions / Evidence locators.
- Core does not require a Discovery Record to enumerate all sibling lineages. Profiles/backends/adapters may provide enumeration as additional behavior.
- Stable Core `0.1` discovery remains unchanged until Core `0.2` is intentionally accepted and published.

## Core 0.1 → 0.2 migration direction

- Core/profile compatibility-line changes remain migration-required; they are not ordinary compatible upgrades.
- The current migration hypothesis is that a Core `0.1` Project's single continuity line becomes one initial/default Core `0.2` lineage while preserving Project identity and existing Current State / Next Actions / Decisions / Evidence.
- Migration must be explicit, idempotent, cold-start verifiable, and conformance-tested before Core `0.2` publication.

## Transactional checkpoint semantics

- A checkpoint is an **authoritative continuity transition**, not an activity-log append.
- Reconcile Project truth first. If authoritative continuity already represents it, checkpoint evaluation is a no-op.
- Material checkpoints construct a coherent candidate before publication and minimize writes to semantic categories that changed.
- Completed checkpoints must not expose mixed generations as coherent truth. Use atomic publication when available or durable generation/revision/transaction/pointer semantics otherwise.
- Stale-base writers must not silently overwrite newer truth; surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile.
- Checkpoint completion includes post-publication discovery verification.

## Repository/VCS mapping and publication safety

- Repository/VCS intent is profile/adapter behavior, not a Core dependency.
- `authoritative_ref` is repository publication authority, not Project identity, lineage identity, or necessarily the active working ref.
- Feature-branch checkpoints verify their actual destination ref; only an authoritative-publication claim must target/verify declared `authoritative_ref`.
- Existing VCS mapping into Core `0.2` is:
  - selected ref/worktree → selected Continuity Lineage;
  - logical branch/ref name → profile-level lineage-identity mapping;
  - branch-local checkpoint → lineage-local checkpoint;
  - merge/rebase/cherry-pick → lineage integration boundary;
  - commit SHA → backend checkpoint receipt;
  - target-ref advancement → backend publication boundary.
- When Agnir controls VCS integration, target-ref advancement must not occur before target continuity is reconciled. Stage integration → reconcile target → construct checkpoint → advance target with integrated Project + reconciled continuity together → fresh verify.
- A server-side merge/squash/rebase/fast-forward that first publishes feature-local `.agnir` truth as target truth and repairs it afterward is recovery-oriented, not the intended safe integration path.

## Development branch governance — 2026-09-02

- `main` remains the only intended long-lived authoritative branch for `iorLab/agnir`.
- Draft PR `#4` (`feature/multibranch-continuity`) carries the VCS branch-continuity experiment.
- Draft PR `#5` (`feature/core-0.2-lineage`) is stacked on PR `#4` and carries the backend-neutral Core `0.2` design/conformance work.
- Both experimental lines may carry branch-local continuity while active without redefining Project identity or stable publication authority.
- Their eventual integration into `main` must construct final `main` continuity before the revision that advances `main`; do not use an ordinary merge path that knowingly exposes feature-local continuity as authoritative target truth.

## Agent-operable activation and execution surfaces

- Root `SKILL.md` remains the canonical Agent-facing Agnir operational package. Users provide intent; the Skill owns procedure.
- Agent-operable repository activation remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Execution-surface configuration is adapter/integration behavior, not Agnir Core or Project durable memory; it contains locator/bootstrap information only.
- Repository activation and execution-surface activation remain separate completion dimensions.

## Existing Project upgrade semantics

- Compatible upgrade activates an existing Project and preserves Project identity, memory locators/content, unrelated instructions, and unrelated extensions.
- Core/profile compatibility-line changes are migration-required and must not be silently rewritten as compatible upgrades.
- `latest stable` means a published stable tag/release, not moving `main` or another development ref unless explicitly authorized.
- Normal resume does not implicitly require an upgrade/network check.

## Versioning and release direction

- Published stable compatibility remains Core `0.1`, `repository-filesystem/0.1`, repository release `0.1.1`.
- Immutable `v0.1.1` remains anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- If Core `0.2` semantics, migration, dual-backend conformance, and real-Project validation pass, the intended next feature release is **repository `v0.2.0` with Core compatibility `0.2`**.
- This feature set should not be labeled `v0.1.2` merely for conservatism; it changes the protocol's continuity model and compatibility line.
- `v1.0.0` is a stability/compatibility commitment milestone governed by `docs/V1_RELEASE_CRITERIA.md`, not a required count of pre-1.0 minor versions.

## Evidence and documentation

- Evidence is retained for recovery, audit, conformance, migration, or support of material claims; it is not an activity log.
- `REPOSITORY_TREE.md` is the structural responsibility map; `.agnir/evidence/` is represented by directory responsibility rather than per-file registration.
- `README.md` and `README.zh-CN.md` remain parallel entry documents and must preserve equivalent operational meaning when stable architecture/activation/continuity semantics change.
- Real mount-boundary behavior remains explicitly unproven until a genuine mount-capable environment is available.
