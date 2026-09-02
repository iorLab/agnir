# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release. Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, storage implementation, or VCS branch.

## Active experimental multi-branch line — 2026-09-02

Development is isolated on temporary branch `feature/multibranch-continuity` and draft PR `#4` while `main` remains the only long-lived authoritative branch for `iorLab/agnir`.

- Project identity remains `urn:agnir:project:agnir-core` on `main` and the feature branch.
- Experimental extension: `agnir/vcs-branch-continuity/0.1` in `profiles/VCS_BRANCH_CONTINUITY.md`.
- The feature branch self-declares the policy under `extensions.agnir/vcs` in `AGNIR.yaml`:
  - `branch_continuity: branch-local`;
  - `integration_reconciliation: required`.
- Stable compatibility is unchanged: Agnir Core `0.1` + `repository-filesystem/0.1` + repository release `0.1.1`.
- A generic storage-neutral `lineage.id` remains deliberately deferred; current evidence is VCS-specific.

### Working-ref selection

Branch-local continuity requires one selected working ref/worktree. The experimental rule is:

1. explicit task/adapter ref;
2. already selected checkout/worktree/current-ref context;
3. explicitly declared default ref.

`authoritative_ref` may be used as an unscoped default only when adapter/Project policy says so. It does not override an explicitly selected feature branch and is not Project identity. Implementations must not scan sibling branches and guess which feature branch a fresh Executor meant; missing selection surfaces `AGNIR_VCS_REF_REQUIRED`.

This keeps shared execution surfaces safe: unscoped work can continue on a declared default such as `main`, while a branch-specific ChatGPT/API task must carry the selected ref as task/adapter context rather than changing Project identity or globally rebinding the shared Project.

### Branch-local checkpoint isolation

After divergence, each selected branch/worktree may carry different Current State, Next Actions, Decisions, and Evidence while retaining the same Project identity. A checkpoint on one ref must not silently mutate sibling branch continuity.

This feature branch is now itself a self-hosting example: its Agnir continuity describes experimental work that is not yet true on stable `main`.

### Integration safety: reconcile before target-ref advancement

Final diff review exposed and closed a material design gap: ordinary server-side merge/squash/rebase/fast-forward can copy feature-branch `.agnir` continuity into `main` before a later repair checkpoint, creating a window where target discovery exposes the wrong branch truth.

The extension now treats **target-ref advancement as a publication boundary**. When Agnir controls merge/cherry-pick/integration, the safe sequence is:

1. capture coherent target continuity and target revision;
2. stage/construct the integration result without advancing the target ref;
3. reconcile the staged Project result against target continuity, relevant source continuity/Evidence, and Principal intent;
4. construct the target checkpoint;
5. publish integrated Project + reconciled target continuity together in the revision/transaction that advances the target;
6. verify destination ref and fresh target discovery.

A normal Agnir-aware path must not rely on “merge first, repair Agnir afterward” when that merge would expose source continuity as target truth. If an external mechanism already advanced an unreconciled target, the Project is in recovery state and must surface `AGNIR_VCS_RECONCILIATION_REQUIRED` until repaired.

For PR `#4` itself, an ordinary GitHub server-side merge that first places this feature branch's `.agnir` State / Next Actions / Decisions onto `main` is explicitly not the intended safe integration path.

### Verification

The experimental suite now contains nine focused branch-continuity cases, including:

- working-ref selection without sibling-branch guessing;
- real Git worktree divergence with the same Project identity and different branch-local state;
- branch checkpoint isolation;
- merge/rebase/cherry-pick reconciliation requirement;
- real Git `merge --no-commit` pressure showing `main` stays at the old revision while continuity conflicts are unresolved, followed by one two-parent merge revision containing reconciled target continuity;
- cross-Project integration rejection;
- history-rewrite identity preservation;
- destination-ref vs authoritative-ref publication verification.

GitHub Actions run `33584167605` completed successfully on head `77567bc89fd54bbd82d6aa61e8542f314b436582` after these rules and tests were in place. The workflow's stable self-hosting gate, explicit experimental VCS branch-continuity gate, and full conformance suite all passed.

Evidence: `.agnir/evidence/2026-09-02-multibranch-continuity-development.md`.

## Published release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- published at: `2026-09-01T10:47:58Z`
- exact-candidate conformance run: `33499092957`
- publication workflow run: `33499228486`

The immutable `v0.1.1` release is unaffected by this development branch.

## Existing stable validations

The execution-surface activation handoff regression and the real compatible upgrade of `mattamior/skills-hub` remain passed evidence for the published `v0.1.1` line. Existing Projects on Core `0.1` / `repository-filesystem/0.1` may continue to resolve `latest stable` to `v0.1.1`; compatibility-line changes remain migration-required.

## Repository invariants

- Root `SKILL.md` remains the canonical Agent-facing operational package.
- Project activation remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Execution-surface configuration remains locator-only and outside Project durable truth.
- Transactional checkpoint no-op/coherent publication, stale-base `AGNIR_CHECKPOINT_CONFLICT`, prompt-free activation, non-destructive `AGENTS.md` merge, and actual-destination push verification remain active.
- On the experimental branch, selected-ref isolation and pre-target-advance integration reconciliation are additional extension-level invariants under pressure.

## Branch governance

`main` remains the only intended long-lived authoritative branch. `feature/multibranch-continuity` is temporary and carries branch-local continuity only for its active development lifetime. Historical recovery/releases continue to use immutable SHAs/tags rather than live legacy refs.
