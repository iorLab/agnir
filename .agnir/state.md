# Agnir Current State

Agnir is the active greenfield project-owned durable continuity protocol on `iorLab/agnir` `main`. Core compatibility is `0.1`, the repository/filesystem profile is `repository-filesystem/0.1`, and the intended initial repository release is `0.1.0`. No `v0.1.0` tag or GitHub Release has been created.

## Current pre-publication contract

- Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.
- Agnir Core remains storage-, platform-, VCS-, repository-, agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Cold-start discovery must resolve the correct Project identity and coherent authoritative memory without predecessor-private context.
- Agent-operable `repository-filesystem/0.1` Projects persist activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Existing Project-owned `AGENTS.md` content is preserved; Agnir adds only a minimal locator and blocks on material instruction conflicts rather than silently overriding them.

## Transactional checkpoint baseline

The pre-publication Core treats checkpointing as an authoritative continuity transition rather than an arbitrary sequence of writes:

1. reconcile current Project truth;
2. minimize writes to semantic categories that materially changed;
3. treat unchanged durable truth as a no-op;
4. construct a coherent candidate before authoritative publication;
5. use an atomic backend publication primitive when available, or durable generation/revision/transaction semantics that prevent a fresh resolver from accepting mixed generations;
6. reject stale-base publication with semantics equivalent to `AGNIR_CHECKPOINT_CONFLICT` instead of silently overwriting newer truth;
7. verify fresh discovery after publication.

A backend-generated commit/revision/transaction identifier may be the checkpoint receipt and does not need to be embedded inside the content whose publication creates that identifier.

## Repository commit and push integration

Repository/VCS integration is profile/Skill behavior, not a Core VCS dependency.

- In repository context, `commit`, `提交`, `提交代码`, and equivalent intent are checkpoint boundaries: reconcile Agnir before commit and prefer Project changes plus Agnir changes in one VCS revision.
- `commit and push`, `提交推送`, and equivalent intent mean checkpoint + commit + push + verification of the declared authoritative remote/ref when available.
- A bare `提交` outside repository context is not a universal keyword; integrations interpret intent and context rather than literal string matching.
- A commit observed after another human/Agent/IDE/CI/web action triggers checkpoint evaluation only. If durable continuity remains coherent, the result is a no-op rather than another checkpoint-only commit.
- Git hooks may capture events but are optional implementation mechanisms and are not continuity dependencies.

## Executable pressure

The conformance suite includes a substrate-neutral checkpoint reference and tests for no-op evaluation, complete-generation publication, stale-base conflict rejection, Skill commit/push intent, and bilingual durable Project instructions.

Existing discovery, activation, safe `AGENTS.md` merge, SQLite continuity, external authorization, multi-project isolation, Locator Chain failure, symlink, and real Git worktree pressure remains in place.

## Repository documentation behavior

`REPOSITORY_TREE.md` is a structural responsibility map. `.agnir/evidence/` is represented by directory responsibility rather than duplicating every evidence filename. Adding an Evidence object therefore does not itself require a second documentation mutation merely to register that filename.

## Exact-revision CI observation

Implementation checkpoint `7e40da7f4bacf98d58570d93310a4e124b2d927b` triggered `Agnir conformance` workflow run `33425797110` and failed in the self-hosting step. The failure was a case-sensitive marker mismatch: the checker required lowercase `mixed checkpoint generations` while the Core sentence began `Mixed checkpoint generations` with an uppercase initial letter.

The repair strengthens the normative sentence instead of weakening conformance: `A fresh compatible resolver MUST NOT accept mixed checkpoint generations as a completed checkpoint.` A new coherent checkpoint must be published from the exact current base and verified by a new workflow run.

## Release status

The transactional-checkpoint / commit-event delta is implemented but is **not yet release-ready** until the repaired exact revision passes the full GitHub conformance workflow. `RELEASE.md` contains the updated publication gate.

Real mount-boundary behavior remains explicitly unproven and optional additional evidence; ordinary directories are not accepted as mount evidence.

## Current resume point

1. publish the CI-marker repair as a coherent checkpoint based on `7e40da7f4bacf98d58570d93310a4e124b2d927b`;
2. verify the GitHub `Agnir conformance` workflow for the repaired exact revision;
3. if CI passes, record the successful revision/run as release-readiness evidence in a later observation checkpoint when useful;
4. only after a passing publication candidate and explicit Principal authorization, create tag `v0.1.0` and/or the GitHub Release.

## Branch governance

`main` remains the only long-lived authoritative branch. Historical recovery uses immutable commit SHAs and Git history rather than live legacy refs.
