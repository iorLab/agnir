# Multi-branch continuity development evidence — 2026-09-02

## Scope

This evidence records the first A+B implementation slice for multi-branch Agnir:

- A: Git-native branch safety / branch-local continuity isolation;
- B: branch-aware repository/VCS selection, publication, and integration semantics;
- C: generic storage-neutral continuity lineage remains deferred.

Work is isolated on temporary branch `feature/multibranch-continuity` and draft PR `#4`. Stable `main`, published `v0.1.1`, Core `0.1`, and `repository-filesystem/0.1` remain unchanged.

## Implemented surfaces

- `profiles/VCS_BRANCH_CONTINUITY.md` — experimental `agnir/vcs-branch-continuity/0.1` extension.
- `conformance/vcs_branch_continuity_reference.py` — branch snapshot, working-ref selection, integration reconciliation, history rewrite, and destination/authority verification model.
- `conformance/test_vcs_branch_continuity.py` — nine focused cases including real worktree divergence and staged safe merge.
- `profiles/REPOSITORY_FILESYSTEM.md` — `authoritative_ref` clarified as publication authority; ordinary push verifies actual destination ref.
- root `SKILL.md` — branch-aware Agent procedure and pointer to the VCS extension for merge/rebase/cherry-pick/ref-specific operations.
- `README.md` + `README.zh-CN.md` — parallel high-level documentation of branch-local continuity.
- `conformance/agnir-0.1.md` + `REPOSITORY_TREE.md` — register experimental pressure without redefining stable Core/profile conformance.
- `.github/workflows/conformance.yml` — stable self-hosting, explicit experimental branch gate, then full suite.
- feature-branch `AGNIR.yaml` — self-hosted `extensions.agnir/vcs` policy declaration.
- feature-branch `.agnir/` — branch-local State / Next Actions / Decisions / Evidence for the same Project identity as `main`.

## Design-review finding: merge-first target contamination

A final PR diff review identified a material hole in the initial design. If source and target store branch-local continuity at the same tracked paths, a normal hosting merge/squash/rebase/fast-forward can advance `main` with feature-branch `.agnir` truth before a follow-up target checkpoint. During that interval, a fresh target resolver may read coherent files that describe the wrong branch.

The initial “merge then reconcile/checkpoint target” wording was therefore tightened.

### Corrected invariant

When Agnir controls the integration operation, **target-ref advancement is the publication boundary**. The implementation must stage/construct the integration result without target-ref advancement, reconcile target truth, construct the target checkpoint, and only then advance the target in a revision/transaction containing both the integrated Project and reconciled target continuity.

External/server-side integration that already advanced an unreconciled target is a recovery case and surfaces `AGNIR_VCS_RECONCILIATION_REQUIRED`; a follow-up repair does not retroactively make the original publication branch-continuity-safe.

## Working-ref selection finding

`authoritative_ref` cannot double as “current working branch” in a multi-branch system. A branch-aware resolver now selects one working ref with precedence:

1. explicit task/adapter ref;
2. current checkout/worktree/ref context;
3. declared default ref.

It never scans sibling branches to guess. Missing branch-specific selection surfaces `AGNIR_VCS_REF_REQUIRED`. This is especially important for hosted/shared execution surfaces such as ChatGPT: default/unscoped work may resolve `main`, while a branch-scoped task must carry its selected ref without changing Project identity or global Project instructions.

## Focused conformance

The branch suite now pressures nine cases:

1. working-ref selection / `AGNIR_VCS_REF_REQUIRED`;
2. real Git `main` + feature worktree with same Project identity but divergent Current State;
3. real Git staged merge where `main` does not advance while branch-local continuity conflicts remain unresolved, followed by one two-parent merge commit containing reconciled target continuity;
4. branch checkpoint snapshot isolation;
5. merge/rebase/cherry-pick explicit reconciliation requirement;
6. reconciled result belongs to target ref;
7. cross-Project integration rejection;
8. rebase/history rewrite preserves Project identity/truth while revision receipt changes;
9. destination-ref vs authoritative-ref publication verification.

## Remote CI evidence

GitHub Actions run `33584167605` executed on head `77567bc89fd54bbd82d6aa61e8542f314b436582` after the safe target-publication rule, working-ref selection model/tests, self-hosted `agnir/vcs` manifest declaration, and conformance documentation were present. Overall conclusion: `success`.

The workflow retains three substantive layers:

1. stable self-hosting cold-start conformance;
2. explicit experimental VCS branch-continuity tests;
3. full repository unittest suite.

Earlier runs also passed incrementally while the branch evolved, including `33584132546` on `bf69307b83ba0da0b6b005b8f3d601cfc83a24de`.

## Self-hosting significance

The feature branch is itself a live demonstration of the intended model: same durable Project identity as `main`, different selected-ref continuity while work diverges, explicit VCS policy, and independent checkpoints.

The next real integration proof should not use a normal server-side PR merge that first publishes feature-local state to `main`. A safe integration must construct a `main`-appropriate continuity checkpoint in the integration candidate before `main` advances.
