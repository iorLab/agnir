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

Core `0.1` now treats checkpointing as an authoritative continuity transition:

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

## Verified publication candidate

The transactional-checkpoint / commit-event implementation was published in checkpoint `7e40da7f4bacf98d58570d93310a4e124b2d927b`. Workflow run `33425797110` exposed one case-sensitive self-host marker mismatch. The repair checkpoint `05103320afa25085d2cb9b65b249a8ad63e883e9` strengthened the Core wording to require that a fresh resolver MUST NOT accept mixed checkpoint generations as a completed checkpoint.

Exact-revision verification for `05103320afa25085d2cb9b65b249a8ad63e883e9` passed GitHub Actions `Agnir conformance` run `33425996098`, job `99599577461`. Both `Self-hosting cold-start conformance` and the full `test_*.py` suite succeeded.

`05103320afa25085d2cb9b65b249a8ad63e883e9` is therefore the currently verified Agnir `0.1.0` **publication candidate**. This later observation checkpoint records the external verification result; it does not redefine the already content-addressed candidate or require recursively treating its own Evidence commit as a new candidate.

## Release status

Development required for the initial `0.1.0` release is again complete. Publication remains a separate explicit action: only after Principal authorization should tag `v0.1.0` and/or the GitHub Release be created for the intended verified candidate.

Real mount-boundary behavior remains explicitly unproven and optional additional evidence; ordinary directories are not accepted as mount evidence.

## Current resume point

1. treat `05103320afa25085d2cb9b65b249a8ad63e883e9` as the verified `0.1.0` publication candidate;
2. after explicit Principal authorization, create tag `v0.1.0` on that intended candidate and/or create the GitHub Release;
3. after publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines and keep `0.1.x` maintenance non-breaking;
4. preserve transactional checkpoint, commit/push intent, activation, and safe `AGENTS.md` merge invariants.

## Branch governance

`main` remains the only long-lived authoritative branch. Historical recovery uses immutable commit SHAs and Git history rather than live legacy refs.
