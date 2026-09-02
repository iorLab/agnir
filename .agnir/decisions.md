# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Name origin and product meaning — 2026-09-01

- `Agnir` is taken from Icelandic `agnir`, the nominative plural of `ögn`, meaning a tiny bit or particle.
- The name maps to the product model: durable Project continuity is composed from small, discoverable pieces of Project truth rather than one Executor's private context.
- Current State, Next Actions, Decisions, and Evidence / Checkpoints are semantic categories, not mandatory one-file-per-category physical storage.

## Discovery and repository/filesystem profile

- `AGNIR.yaml` is the top-level discovery anchor for `repository-filesystem/0.1`; this filename/layout is profile behavior, not Core.
- `.agnir/` is the recommended colocated layout in this repository; `AGNIR.yaml` locators are authoritative.
- Cold-start discovery begins from an authorized Project Entry Point, validates version/Project identity, resolves required continuity, and does not guess through arbitrary sibling repositories, old chats, predecessor paths, private Executor memory, or VCS sibling refs.
- Current State and Next Actions from different known checkpoint generations must not be accepted as one coherent Project truth.

## Agent-operable activation and Skill packaging

- Root `SKILL.md` is the canonical Agent-facing Agnir operational package. Users provide short install/upgrade/resume intent; the Skill owns procedure.
- An Agent-operable repository persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- `AGENTS.md` remains locator-only for Agnir; unrelated Project instructions are preserved and material conflicts block completed activation until explicitly resolved.

## Execution-surface activation handoff — 2026-09-01

- Repository activation and execution-surface activation are separate completion dimensions.
- Execution-surface configuration is adapter/integration behavior, not Agnir Core or Project durable memory; it stores only enough locator/bootstrap information to reach the authorized Project Entry Point.
- Required surface configuration that is pending/unverified blocks a claim that full fresh activation passed.
- ChatGPT Project Instructions are the first concrete surface adapter. They point to Project/repository/ref and activation files; they do not duplicate State, Next Actions, Decisions, Evidence, or the full Agnir procedure.

## Transactional checkpoint semantics — 2026-09-01

- A checkpoint is an **authoritative continuity transition**, not an activity-log append.
- Reconcile Project truth first. If authoritative continuity already represents it, checkpoint evaluation is a no-op.
- Material checkpoints construct a coherent candidate before publication and minimize writes to semantic categories that changed.
- Completed checkpoints must not expose mixed generations as coherent truth. Use atomic publication when available or durable generation/revision/transaction/pointer semantics otherwise.
- Stale-base writers must not silently overwrite newer truth; surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile.
- Checkpoint completion includes post-publication discovery verification. Backend revision/transaction/commit IDs may be checkpoint receipts without being embedded in content that determines them.

## Repository commit / push semantics — updated 2026-09-02

- Repository/VCS intent is integration/profile behavior, not a Core dependency.
- Authorized repository `commit`, `提交`, `提交代码`, or equivalent is a checkpoint boundary; reconcile Agnir continuity before the VCS commit.
- Prefer Project changes + material Agnir changes in one VCS revision when possible.
- `commit and push`, `提交推送`, or equivalent means checkpoint + commit + push + verification of the **actual destination ref**.
- `authoritative_ref` is publication authority, not branch identity and not the only ref where branch-local checkpointing is allowed.
- Only a claim of authoritative publication must target/verify the declared `authoritative_ref` when one exists. A feature push verifies its feature destination and must not be reported as publishing `main` merely because `main` is authoritative.
- Observed external commits trigger checkpoint evaluation, not unconditional memory mutation. Git hooks remain optional adapter mechanisms.

## Experimental VCS branch continuity — 2026-09-02

- Multi-branch behavior is experimental extension `agnir/vcs-branch-continuity/0.1` layered on Core `0.1` + `repository-filesystem/0.1`; it is not a Core `0.2` change.
- `iorLab/agnir` opts into the experimental policy on this feature branch through `extensions.agnir/vcs.branch_continuity: branch-local` and `integration_reconciliation: required`.
- Ordinary branch creation/checkout/worktree/rebase/merge/cherry-pick/ref rename/history rewrite does not create a new Project identity unless the Principal explicitly creates a distinct Project.
- After divergence, each selected ref/worktree may hold different branch-local Current State / Next Actions / Decisions / Evidence for the same Project identity. A checkpoint on one branch must not mutate sibling branch continuity.
- Branch/ref names are VCS locators/runtime observations, not Project identity and not a standardized durable generic continuity-line identity. Commit/revision IDs are receipts and may change across rebase/history rewrite.

### Working-ref selection

- Before loading branch-local continuity, resolve exactly one working ref/worktree.
- Precedence is: explicit Principal/task/adapter ref → already selected checkout/worktree/current-ref → explicitly declared default ref.
- `authoritative_ref` may act as an unscoped default only when policy says so; it never overrides an explicit feature ref.
- Implementations must not scan sibling branches to guess which branch a fresh Executor meant. Missing selection surfaces extension semantics equivalent to `AGNIR_VCS_REF_REQUIRED`.
- This keeps one shared execution surface capable of serving multiple branch-scoped tasks without changing Project identity or globally rebinding durable Project truth.

### Integration reconciliation and target publication

- Merge, rebase, and cherry-pick are continuity-integration boundaries. Source continuity is input only and must not be promoted automatically to target truth.
- **Target-ref advancement is a publication boundary.** When Agnir controls integration, it must not advance the target ref until the target continuity for the staged integrated Project has been reconciled.
- Preferred sequence: capture target revision/continuity → stage integration without ref advancement → reconcile staged Project + target continuity + relevant source continuity/Evidence + Principal intent → construct target checkpoint → publish integrated Project + reconciled target continuity in the same ref-advancing revision/transaction → verify target ref + fresh discovery.
- “Merge first, repair Agnir in a follow-up commit” is not the normal branch-continuity-safe path when the merge would expose source branch-local continuity as target truth.
- Ordinary server-side merge/squash/rebase-and-merge/fast-forward is not branch-continuity-safe if it cannot preserve/reconcile target continuity before advancing the target ref. It requires an Agnir-aware hook/adapter or another staged integration mechanism.
- If an external mechanism already advanced an unreconciled target, surface `AGNIR_VCS_RECONCILIATION_REQUIRED`; repair is recovery after an unmanaged integration, not the preferred publication sequence.
- Cross-Project integration continues to fail the Project-identity boundary rather than adopting source continuity.

### Scope boundary

- A generic storage-neutral `lineage.id` remains deliberately deferred. Promotion into Core requires non-VCS evidence that parallel continuity lineage is a substrate-neutral invariant.
- Stable Core self-hosting and experimental branch-continuity tests remain separate CI gates; extension success does not redefine stable compatibility lines.
- For `iorLab/agnir`, `main` remains the only intended long-lived authoritative branch; temporary development branches may carry branch-local continuity while active.
- PR `#4` itself must not be integrated by a normal server-side operation that first publishes feature-local `.agnir` truth to `main`; its final target integration must contain reconciled `main` continuity before `main` advances.

## Existing Project upgrade semantics — 2026-09-01

- `upgrade` is first-class and is not re-initialization.
- Compatible upgrade activates the existing Project and preserves `project.identity`, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
- Core/profile line changes are migration-required and must surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently rewriting the Project.
- `latest stable` means a published stable tag/release, never moving `main` or another untagged branch unless explicitly authorized as non-stable.
- Re-applying identical operational provenance with no material activation drift is a no-op.
- Normal resume does not implicitly check/install upgrades; Project resume must not require network access to the Agnir distribution source.

## Evidence and documentation

- Evidence is retained only for recovery, audit, conformance, or support of material claims; it is not an activity log.
- `REPOSITORY_TREE.md` is the structural responsibility map; `.agnir/evidence/` is represented by directory responsibility rather than per-file registration.
- `README.md` and `README.zh-CN.md` are parallel entry documents and must preserve equivalent operational meaning for architecture/activation/continuity changes.
- README front matter remains ordered: Start Here → Agnir Project Instructions → What Agnir Adds to a Project → Architecture.

## Versioning, release, and branch governance

- Stable compatibility remains Core `0.1`, `repository-filesystem/0.1`, repository release `0.1.1`.
- Immutable release `v0.1.1` remains anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- `main` is the only long-lived authoritative branch. Temporary development branches may exist and carry branch-local continuity without redefining publication authority.
- Historical predecessor/branch recovery uses immutable SHAs/Git history rather than live legacy refs.
- Real mount-boundary behavior remains explicitly unproven.
