# Transactional checkpoint and repository commit-event baseline — 2026-09-01

## Why this checkpoint exists

A review of Agnir's save/checkpoint behavior found that the semantic model already required coherent reconciliation, while the repository/filesystem path could still expose a sequence of individually updated continuity files. Historical Agnir work also demonstrated write amplification where one logical checkpoint became separate Evidence, Next Actions, Decisions, Current State, and repository-tree commits.

The pre-publication `0.1.0` line therefore tightens checkpoint semantics before the first release.

## Durable decisions implemented

- A checkpoint is an authoritative continuity transition.
- Unchanged reconciled truth produces a no-op rather than synthetic Evidence or a checkpoint-only revision.
- Material changes are assembled as a coherent candidate before authoritative publication.
- A completed checkpoint may not present mixed old/new generations as coherent truth.
- Atomic backend publication is preferred when available; otherwise generation/revision/transaction/pointer semantics must allow fresh discovery to reject mixed generations.
- Detectable stale-base publication fails with `AGNIR_CHECKPOINT_CONFLICT` semantics rather than silently overwriting newer truth.
- Backend revision/transaction/commit identifiers are receipts and need not be embedded into the content whose publication determines them.

## Repository/VCS event behavior

- In clear repository context, `commit`, `提交`, `提交代码`, and equivalent intent trigger checkpoint evaluation/reconciliation before the VCS commit.
- Project changes and Agnir changes should share one VCS revision when possible.
- `commit and push` / `提交推送` adds push and authoritative-ref verification when declared.
- A commit observed from another human/Agent/IDE/CI/web action triggers evaluation, not unconditional mutation.
- Bare `提交` outside repository context is not a literal global keyword.
- Git hooks may capture these events but are optional adapter mechanisms.

## Conformance added

- `conformance/checkpoint_reference.py` models substrate-neutral no-op, single-generation publication, and stale-base conflict behavior.
- `conformance/test_checkpoint_semantics.py` pressure-tests those invariants.
- Skill/package conformance now requires transactional checkpoint markers and repository-context commit/push intent.
- Self-hosting conformance now requires the new Core/profile/reference artifacts.

## Documentation write-amplification change

`REPOSITORY_TREE.md` now records `.agnir/evidence/` by directory responsibility instead of enumerating every Evidence filename. Future Evidence creation therefore does not require a second documentation-only mutation merely to register the filename.

## Publication/verification boundary

This evidence intentionally does **not** contain the Git commit SHA that publishes it. The resulting VCS revision is the backend-produced checkpoint receipt; embedding that SHA inside the content that determines the SHA would create a self-reference cycle.

The exact implementation revision must pass the GitHub `Agnir conformance` workflow before it becomes the `0.1.0` publication candidate. A later observation checkpoint may record that commit SHA and workflow run after the external CI result exists.
