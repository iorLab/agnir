# Multi-branch continuity development evidence — 2026-09-02

## Scope

This evidence records the first A+B implementation slice for multi-branch Agnir:

- A: Git-native branch safety / branch-local continuity isolation;
- B: branch-aware repository/VCS integration semantics;
- C: generic storage-neutral continuity lineage remains deferred.

The work is isolated on temporary branch `feature/multibranch-continuity` and draft PR `#4`. Stable `main`, published `v0.1.1`, Core `0.1`, and `repository-filesystem/0.1` remain unchanged.

## Implemented artifacts

- `profiles/VCS_BRANCH_CONTINUITY.md` — experimental `agnir/vcs-branch-continuity/0.1` extension.
- `conformance/vcs_branch_continuity_reference.py` — branch snapshot, integration reconciliation, history-rewrite, and publication-ref reference model.
- `conformance/test_vcs_branch_continuity.py` — seven focused cases including a real Git worktree divergence fixture.
- `profiles/REPOSITORY_FILESYSTEM.md` — clarified that `authoritative_ref` is publication authority, while ordinary push verification follows the actual destination ref.
- root `SKILL.md` — branch-aware Agent procedure for branch-local checkpointing and merge/rebase/cherry-pick reconciliation.
- `README.md` + `README.zh-CN.md` — parallel user/Agent documentation of experimental branch continuity.
- `conformance/agnir-0.1.md` + `REPOSITORY_TREE.md` — registered experimental pressure without redefining the stable baseline.
- `.github/workflows/conformance.yml` — stable self-hosting gate remains separate from an explicit experimental VCS branch-continuity gate, followed by full unittest discovery.
- `.agnir/state.md`, `.agnir/next-actions.md`, and `.agnir/decisions.md` on the feature branch — self-hosted branch-local continuity for the same Project identity used by `main`.

## Key semantic decisions proven/pressured

1. `project.identity` survives ordinary VCS branch/worktree operations.
2. Branch/ref name is a VCS locator/runtime observation, not Project identity.
3. Commit/revision ID is a checkpoint receipt and may change across rebase/history rewrite.
4. Diverged branches may carry different branch-local Agnir Current State while remaining the same Project.
5. Merge, rebase, and cherry-pick require explicit target continuity reconciliation; source continuity is input, not automatic target truth.
6. Unreconciled integration surfaces `AGNIR_VCS_RECONCILIATION_REQUIRED` at the extension layer.
7. Ordinary push verifies the actual destination ref; only an authoritative-publication claim additionally enforces the declared `authoritative_ref`.
8. A generic storage-neutral `lineage.id` is not introduced from Git evidence alone.

## Focused test evidence

A locally reconstructed isolated execution of the seven new `VCSBranchContinuityTests` completed successfully:

- real Git main/feature worktree resolves same Project identity with different branch-local state;
- branch checkpoint snapshot isolation;
- merge/rebase/cherry-pick explicit reconciliation requirement;
- reconciled result belongs to target ref;
- cross-Project integration rejected;
- rebase revision rewrite preserves Project identity/truth;
- destination-ref vs authoritative-ref verification behavior.

Result: `Ran 7 tests ... OK`.

## Remote CI evidence

GitHub Actions run `33583654296` executed on feature-branch checkpoint head `1acb38a81a9661cd42efc8a69b2bc42b8e0cd16d` and completed with overall conclusion `success`.

The `repository-filesystem` job reported all substantive gates successful:

1. `Stable self-hosting cold-start conformance` — success;
2. `Experimental VCS branch continuity` — success;
3. `Full conformance suite` — success.

This establishes remote repository-level conformance for the implemented A+B branch slice at that checkpoint. A later continuity-only checkpoint does not change the extension implementation, but its own PR head should still remain green before merge.

## Self-hosting significance

This feature branch is the first Project-level demonstration of the intended isolation rule: it retains the same Agnir Project identity as `main` but carries branch-local Current State / Next Actions / Decisions describing work that is not yet true on `main`.

If PR `#4` is eventually merged, the target `main` branch must observe the actual merge result and reconcile a fresh main checkpoint. The feature branch's memory is not valid as a wholesale textual replacement for target truth.
