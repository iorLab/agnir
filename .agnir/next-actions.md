# Agnir Next Actions

Agnir remains on the pre-publication `0.1.0` line. Transactional checkpoint and repository commit/push integration are implemented. Exact-revision CI for implementation checkpoint `7e40da7f4bacf98d58570d93310a4e124b2d927b` failed only on a case-sensitive self-host marker and is being repaired with a stronger normative sentence.

1. **Publish the repair checkpoint:** from base `7e40da7f4bacf98d58570d93310a4e124b2d927b`, publish the Core wording repair together with updated Current State / Next Actions / repair Evidence as one coherent revision.
2. **Verify the repaired exact revision:** inspect the GitHub `Agnir conformance` workflow for that new commit. Do not reuse run `33425797110` as passing evidence; it is durable failure evidence for the predecessor revision.
3. If the new workflow fails, repair the earliest failed invariant and publish another coherent checkpoint rather than patching memory independently from implementation truth.
4. If the workflow passes, record the commit SHA and workflow run/job as release-readiness evidence when that external observation becomes durable Project truth.
5. **Publication remains separately authorized:** only after the current publication candidate passes the full gate may an explicitly authorized operation create tag `v0.1.0` and/or the GitHub Release.
6. Preserve Core `0.1` substrate neutrality: transactional checkpoint semantics must not become Git-specific. Database transactions, immutable generations/pointer swaps, VCS revisions, or equivalent mechanisms may satisfy the same authoritative-transition invariant.
7. Preserve checkpoint minimality and no-op behavior: do not rewrite state, create Evidence, or produce a checkpoint-only revision when durable Project truth did not materially change.
8. Preserve stale-base safety: a writer that detects the authoritative revision changed since its base was loaded must surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile rather than silently overwriting newer truth.
9. Preserve repository-context intent behavior: `commit` / `提交` / `提交代码` means checkpoint-before-commit when VCS intent is clear; `commit and push` / `提交推送` adds push + authoritative-ref verification; observed commits trigger evaluation rather than unconditional mutation.
10. Keep bare language tokens contextual. In particular, `提交` outside repository/VCS context must not trigger Agnir simply by string matching.
11. Keep `.agnir/evidence/` represented by directory responsibility in repository documentation; do not reintroduce per-evidence filename registration that creates write amplification.
12. Preserve the user-prompt / Skill-procedure / target-Project-activation separation and the non-destructive `AGENTS.md` merge invariant.
13. Existing initialized Projects must not require a recurring Agnir bootstrap prompt. Execution surfaces that ignore Project instructions need one-time surface configuration rather than repeated user procedure.
14. Keep real mount-boundary validation as optional additional evidence when a real mount-capable environment exists; never represent ordinary directories as mount evidence.

## Stable maintenance constraints

- `README.md` and `README.zh-CN.md` must stay semantically synchronized for activation, checkpoint, commit/push, and continuity-flow changes.
- Root `SKILL.md` remains the canonical Agent-facing operational package.
- `RELEASE.md` remains the publication contract.
- `main` remains the only long-lived authoritative branch.
