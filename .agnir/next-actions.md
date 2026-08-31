# Agnir Next Actions

Agnir `0.1.0` is release-ready again after exact-revision verification of the transactional checkpoint / repository commit-event baseline.

Verified publication candidate:

`05103320afa25085d2cb9b65b249a8ad63e883e9`

Verification:

- GitHub Actions workflow: `Agnir conformance`
- run: `33425996098`
- job: `99599577461`
- self-hosting cold-start conformance: success
- full `test_*.py` suite: success

1. **Publication only:** after explicit Principal authorization, create tag `v0.1.0` on the intended verified candidate `05103320afa25085d2cb9b65b249a8ad63e883e9` and/or create the GitHub Release.
2. After publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines. Any `0.1.x` maintenance must remain non-breaking.
3. Preserve Core substrate neutrality: transactional checkpoint semantics must not become Git-specific. Database transactions, immutable generations/pointer swaps, VCS revisions, or equivalent mechanisms may satisfy the same authoritative-transition invariant.
4. Preserve checkpoint minimality and no-op behavior: do not rewrite state, create Evidence, or produce a checkpoint-only revision when durable Project truth did not materially change.
5. Preserve stale-base safety: a writer that detects the authoritative revision changed since its base was loaded must surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile rather than silently overwriting newer truth.
6. Preserve repository-context intent behavior: `commit` / `提交` / `提交代码` means checkpoint-before-commit when VCS intent is clear; `commit and push` / `提交推送` adds push + authoritative-ref verification; observed commits trigger evaluation rather than unconditional mutation.
7. Keep bare language tokens contextual. In particular, `提交` outside repository/VCS context must not trigger Agnir simply by string matching.
8. Keep `.agnir/evidence/` represented by directory responsibility in repository documentation; do not reintroduce per-evidence filename registration that creates write amplification.
9. Preserve the user-prompt / Skill-procedure / target-Project-activation separation and the non-destructive `AGENTS.md` merge invariant.
10. Existing initialized Projects must not require a recurring Agnir bootstrap prompt. Execution surfaces that ignore Project instructions need one-time surface configuration rather than repeated user procedure.
11. Keep real mount-boundary validation as optional additional evidence when a real mount-capable environment exists; never represent ordinary directories as mount evidence.

## Stable maintenance constraints

- `README.md` and `README.zh-CN.md` must stay semantically synchronized for activation, checkpoint, commit/push, and continuity-flow changes.
- Root `SKILL.md` remains the canonical Agent-facing operational package.
- `RELEASE.md` remains the publication contract.
- `main` remains the only long-lived authoritative branch.
