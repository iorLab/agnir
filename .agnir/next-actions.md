# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Multi-branch work is isolated on `feature/multibranch-continuity` / draft PR `#4`; current head behavior has passed stable + experimental + full PR conformance, while `main` remains authoritative and unchanged.

## Active branch work

1. Pressure-test one additional **explicitly authorized real Project** using a genuine parallel branch workflow beyond this self-hosting branch and the synthetic worktree fixture. Prefer: branch selection → divergence → independent checkpoint → target advancement → staged merge/rebase/cherry-pick → target continuity reconciliation. Do not mutate an unrelated Project merely to manufacture evidence.
2. Keep working-ref selection explicit: task/adapter ref > current checkout/worktree ref > declared default. Do not infer a feature branch by scanning sibling refs; surface `AGNIR_VCS_REF_REQUIRED` when branch-specific work has no selected ref.
3. Keep `authoritative_ref` as publication authority/default only when policy says so; do not treat it as active branch identity or the only legal checkpoint destination.
4. Preserve the target-ref publication invariant. An Agnir-aware merge/cherry-pick must stage the integration while the target ref is unchanged, reconcile target continuity, then publish integrated Project + target checkpoint together. Treat merge-first/follow-up-repair as recovery, not the normal safe path.
5. Before PR `#4` is integrated, perform one final diff/CI review and choose an integration mechanism that can construct a reconciled target revision **before** advancing `main`. Do not use an ordinary server-side merge that would first publish feature-branch `.agnir` state onto `main`.
6. If PR `#4` is integrated, the final target revision must contain `main`-appropriate Current State / Next Actions / Decisions from the integration candidate itself. Verify `main` fresh discovery after the ref advances; there should be no intermediate published `main` revision whose continuity is knowingly feature-local.
7. After a safe integration, decide whether the experimental extension is mature enough for a repository patch release or should remain development-only pending more real Project evidence. Do not promote it into Core `0.2` solely because Git evidence passes.
8. Gather a non-VCS parallel-continuity case before considering any generic durable `lineage.id` or Core continuity-lineage semantics.

## Stable maintenance work still open

1. Use additional real Projects/execution surfaces to broaden evidence for the execution-surface handoff rule and compatible upgrade behavior without making any platform-specific adapter part of Agnir Core.
2. When useful, add a second compatible-upgrade case with different existing Project instructions or operational provenance to pressure preservation/idempotence beyond `skills-hub`.
3. Keep real mount-boundary validation optional until a genuine mount-capable environment exists.

## Current stable release

- repository release: `0.1.1`
- tag: `v0.1.1`
- exact target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- Required execution-surface settings are adapters/locators, not Project memory or Agnir Core.
- `.agnir/evidence/` is represented by directory responsibility rather than per-evidence filename registration in repository maps.
- `main` is the only intended long-lived authoritative branch; temporary development branches may carry branch-local continuity while active.
