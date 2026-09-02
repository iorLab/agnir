# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release on immutable target `e9712357ab590e5c1e5357b3cf3219d07d789aff`. Current development is isolated on temporary branch `feature/multibranch-continuity` and draft PR `#4`; it does not redefine stable `main` truth or compatibility lines.

The first full remote branch conformance has passed: GitHub Actions run `33583654296` succeeded on checkpoint head `1acb38a81a9661cd42efc8a69b2bc42b8e0cd16d`, including stable self-hosting, the explicit experimental branch-continuity gate, and the full unittest suite.

## Active branch work

1. Review the final PR diff and ensure the experimental/stable boundary remains explicit in profile, Skill, READMEs, repository map, CI, and durable Agnir state.
2. Pressure-test at least one additional real multi-branch Project workflow beyond the synthetic worktree fixture and this self-hosting branch, ideally including branch divergence → independent checkpoint → target advancement → merge or rebase → explicit target reconciliation. Do not mutate an unrelated Project merely to manufacture this evidence; use an explicitly authorized real case.
3. Keep `project.identity` stable across ordinary branches/worktrees; keep branch/ref names as VCS locators/runtime observations and commit SHAs as revision/checkpoint receipts.
4. Keep `authoritative_ref` as publication authority rather than the only legal Agnir branch. Verify actual destination refs for ordinary pushes; enforce the authoritative ref only when authoritative publication is claimed.
5. Do not introduce a generic durable `lineage.id` or Core `0.2` solely from Git evidence. Gather a non-VCS parallel-continuity case first if promotion into Core is later considered.
6. Once the PR diff is reviewed and the current head's conformance remains green, move PR `#4` out of draft if no new blocker appears. Merging remains a separate decision because target/main continuity must be reconciled from the actual merge result.
7. If PR `#4` is merged, perform **target/main reconciliation** after observing the actual merge result: remove feature-only blockers/next actions, preserve only decisions that remain true on `main`, record merge evidence as needed, and publish a new `main` Agnir checkpoint. Do not carry this feature-branch state wholesale into `main`.

## Stable maintenance work still open

1. Use additional real Projects/execution surfaces to broaden evidence for the execution-surface handoff rule and compatible upgrade behavior without making any platform-specific adapter part of Agnir Core.
2. When useful, add a second upgrade case with different existing Project instructions or operational provenance to pressure preservation/idempotence beyond `skills-hub`.
3. Preserve transactional checkpoint no-op/coherent publication semantics, stale-base safety, repository commit/push integration, prompt-free Project activation, non-destructive `AGENTS.md` merge, and the README `Start Here -> Agnir Project Instructions -> Project surface -> Architecture` audience split.
4. Keep `latest stable release` resolution pinned to actual published tags/releases; never silently substitute moving `main`.
5. Keep real mount-boundary validation optional until a genuine mount-capable environment exists.

## Current stable release

- repository release: `0.1.1`
- tag: `v0.1.1`
- exact target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- exact-candidate conformance run: `33499092957`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`

## Real compatible-upgrade evidence

- Project: `mattamior/skills-hub`
- upgrade revision: `f8ec9fbb429df6a8eaa0aa837906a5897ffbb210`
- target repository validation run: `33500075237`
- conclusion: `success`
- applied operational release: `0.1.1`
- applied Agnir revision: `e9712357ab590e5c1e5357b3cf3219d07d789aff`

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- Required execution-surface settings are adapters/locators, not Project memory or Agnir Core.
- `.agnir/evidence/` is represented by directory responsibility rather than per-evidence filename registration in repository maps.
- `main` is the only intended long-lived authoritative branch; temporary development branches may carry branch-local continuity while active.
