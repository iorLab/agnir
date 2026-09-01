# Agnir Current State

Agnir is the active greenfield project-owned durable continuity protocol on `iorLab/agnir` `main`. Core compatibility is `0.1`, the repository/filesystem profile is `repository-filesystem/0.1`, and the intended initial repository release is `0.1.0`. No `v0.1.0` tag or GitHub Release has been created.

## Current pre-publication contract

- Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.
- Agnir Core remains storage-, platform-, VCS-, repository-, agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agent-operable `repository-filesystem/0.1` Projects persist activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory.
- Existing Project-owned `AGENTS.md` content is preserved; Agnir adds only a minimal locator and blocks on material instruction conflicts rather than silently overriding them.

## Transactional checkpoint and repository event baseline

Core `0.1` treats checkpointing as an authoritative continuity transition: reconcile current truth, minimize material writes, no-op when unchanged, build a coherent candidate before publication, prevent fresh readers from accepting mixed generations, reject stale-base publication with `AGNIR_CHECKPOINT_CONFLICT`, and verify fresh discovery after publication.

Repository commit intent is a checkpoint boundary; compatible Project + Agnir changes should share one VCS revision. Commit-and-push adds authoritative-ref verification. Externally observed commits trigger evaluation, not unconditional continuity writes.

## Existing Project upgrade baseline

Agnir defines **upgrade** as a first-class Agent operation distinct from install/initialize.

- Upgrade activates and preserves the existing Project; it does not regenerate `.agnir/` from templates.
- Compatible operational upgrade requires target Core/profile lines `0.1` / `repository-filesystem/0.1`.
- Core/profile changes are migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently rewriting the Project.
- `latest stable` resolves an actually published stable tag/release. Moving `main`, another branch, or an untagged revision is not silently treated as stable; non-stable targets require explicit authorization.
- Projects created before operational provenance existed remain valid compatible-upgrade inputs.
- Compatible upgrade preserves `project.identity`, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
- Optional `extensions.agnir/operations` provenance records distribution, repository release, source, and immutable applied revision without redefining Core/profile compatibility or Project identity.
- Re-applying the same operational baseline with no material drift is a no-op.
- Normal resume does not auto-upgrade or require network access to the Agnir distribution source.

## Verified upgrade publication candidate

Implementation checkpoint `2a0cb7bf2068b11f361e315670b2f2dc497b2588` added the compatible existing-Project upgrade Skill procedure, repository/filesystem operational provenance/stable-target rules, executable upgrade classification, release-gate updates, repository structure updates, and durable Agnir continuity.

Exact-revision GitHub Actions `Agnir conformance` run `33463490510`, job `99718447961`, passed. Both self-hosting cold-start conformance and the full `test_*.py` suite succeeded.

`2a0cb7bf2068b11f361e315670b2f2dc497b2588` is therefore the verified Agnir `0.1.0` **publication candidate**. This later observation checkpoint records that external verification and does not recursively redefine the candidate.

## Release status

Development required for the initial `0.1.0` release, including the existing-Project upgrade contract, is complete and verified. Publication remains a separate explicit Principal action.

Until a stable tag/release is actually published, an old Project request to upgrade to `latest stable` must not silently use `main`. Existing Projects should wait for stable publication unless the Principal explicitly authorizes a pre-release revision.

Real mount-boundary behavior remains explicitly unproven and optional additional evidence.

## Current resume point

1. treat `2a0cb7bf2068b11f361e315670b2f2dc497b2588` as the verified `0.1.0` publication candidate;
2. after explicit Principal authorization, publish `v0.1.0` / GitHub Release on that candidate;
3. after stable publication, existing compatible Agnir Projects may be upgraded using the first-class `upgrade` operation and optional `agnir/operations` provenance;
4. preserve transactional checkpoint, upgrade, commit/push, activation, and safe `AGENTS.md` merge invariants.

## Branch governance

`main` remains the only long-lived authoritative branch. Historical recovery uses immutable commit SHAs and Git history rather than live legacy refs.
