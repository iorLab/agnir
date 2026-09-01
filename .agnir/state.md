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

Core `0.1` treats checkpointing as an authoritative continuity transition: reconcile current truth, minimize material writes, no-op when unchanged, build a coherent candidate before publication, prevent fresh readers from accepting mixed generations, reject stale-base publication with `AGNIR_CHECKPOINT_CONFLICT`, and verify fresh discovery after publication.

A backend-generated commit/revision/transaction identifier may be the checkpoint receipt and does not need to be embedded inside the content whose publication creates that identifier.

## Repository commit and push integration

- In repository context, `commit`, `提交`, `提交代码`, and equivalent intent are checkpoint boundaries: reconcile Agnir before commit and prefer Project changes plus Agnir changes in one VCS revision.
- `commit and push`, `提交推送`, and equivalent intent mean checkpoint + commit + push + verification of the declared authoritative remote/ref when available.
- A bare `提交` outside repository context is contextual, not a universal keyword.
- An externally observed commit triggers checkpoint evaluation only; unchanged coherent continuity yields a no-op.

## Existing Project upgrade baseline

Agnir now defines **upgrade** as a first-class Agent operation distinct from install/initialize.

- Upgrade starts by activating and preserving the existing Project; it does not regenerate `.agnir/` from templates.
- A compatible operational upgrade requires the target Core/profile lines to remain `0.1` / `repository-filesystem/0.1`.
- A Core/profile compatibility-line change is migration-required and must surface semantics equivalent to `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently rewriting the Project.
- `latest stable` resolves an actually published stable release/tag. Moving `main`, another branch, or an untagged revision is not silently treated as stable; non-stable targets require explicit authorization.
- Projects created before operational provenance existed remain valid compatible-upgrade inputs.
- A compatible repository/filesystem upgrade preserves `project.identity`, all memory locators and durable memory contents, unrelated README/`AGENTS.md` content, and unrelated extensions.
- Optional `extensions.agnir/operations` provenance records distribution, repository release, source, and immutable applied revision without redefining Core/profile compatibility or Project identity.
- Re-applying the same operational baseline with no material drift is a no-op.
- Compatible VCS upgrades should publish Agnir-owned procedure/provenance changes and continuity evidence in one coherent revision and finish with fresh activation.
- Normal resume does not auto-upgrade Agnir or require network access to the Agnir distribution source.

## Executable pressure

The suite includes checkpoint no-op/coherent-publication/conflict pressure and a new substrate-light upgrade reference covering legacy Projects without provenance, compatible provenance application, same-baseline no-op, rejection of implicit unstable targets, and migration-required behavior for Core/profile changes.

Existing discovery, activation, safe `AGENTS.md` merge, SQLite continuity, external authorization, multi-project isolation, Locator Chain failure, symlink, and real Git worktree pressure remains in place.

## Repository documentation behavior

`REPOSITORY_TREE.md` is a structural responsibility map. `.agnir/evidence/` is represented by directory responsibility rather than duplicating every evidence filename.

## Release status

The previously verified publication candidate `05103320afa25085d2cb9b65b249a8ad63e883e9` predates the newly accepted existing-Project upgrade contract. The pre-publication baseline is therefore reopened: the upgrade implementation must be published as one coherent revision and pass the full exact-revision conformance workflow before a new `0.1.0` publication candidate is established.

Real mount-boundary behavior remains explicitly unproven and optional additional evidence; ordinary directories are not accepted as mount evidence.

## Current resume point

1. publish the upgrade Skill/profile/conformance/release documentation and this durable continuity update as one coherent revision;
2. verify the full `Agnir conformance` workflow on that exact revision;
3. if it passes, record that revision as the new verified `0.1.0` publication candidate without recursively promoting a later observation-only checkpoint;
4. only after explicit Principal publication authorization should `v0.1.0` / GitHub Release be created;
5. after stable publication, existing Agnir Projects may use the new `upgrade` operation to move to the published stable operational baseline.

## Branch governance

`main` remains the only long-lived authoritative branch. Historical recovery uses immutable commit SHAs and Git history rather than live legacy refs.
