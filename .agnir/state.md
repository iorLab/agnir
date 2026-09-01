# Agnir Current State

Agnir is the active greenfield project-owned durable continuity protocol on `iorLab/agnir` `main`. Core compatibility is `0.1`, the repository/filesystem profile is `repository-filesystem/0.1`, and the intended initial repository release is `0.1.0`.

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

## Verified publication candidate

Implementation checkpoint `2a0cb7bf2068b11f361e315670b2f2dc497b2588` added the compatible existing-Project upgrade contract and passed exact-revision GitHub Actions `Agnir conformance` run `33463490510`, job `99718447961`. Both self-hosting cold-start conformance and the full `test_*.py` suite succeeded.

`2a0cb7bf2068b11f361e315670b2f2dc497b2588` remains the verified Agnir `0.1.0` **publication candidate**. Observation checkpoint `e0ee44f7e156c6b5c81023b3e9da655d120106a0` recorded that verification and also passed conformance.

## Publication authorization and current blocker

On 2026-09-01 the Principal explicitly authorized formal publication of Agnir `v0.1.0`.

Publication target remains the verified candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`, not the later observation-only `main` checkpoint.

Pre-publication verification confirmed that neither the `v0.1.0` Git tag nor a GitHub Release for `v0.1.0` currently exists.

The current execution surface's connected GitHub capability exposes repository commit/ref operations but does not expose a mutation for creating Git tags or GitHub Releases. It is therefore not safe to represent publication as complete, and a branch named `v0.1.0` must not be substituted for a tag.

The release is **authorized but not yet published**. The next capable Executor should create the real `v0.1.0` tag on `2a0cb7bf2068b11f361e315670b2f2dc497b2588`, create the GitHub Release from that tag, and verify both exist before marking publication complete.

## Release status

Development required for the initial `0.1.0` release, including the existing-Project upgrade contract, is complete and verified. Principal publication authorization has been granted; only execution of the actual Git tag + GitHub Release remains blocked by the current tool surface.

Until the stable tag/release is actually published, an old Project request to upgrade to `latest stable` must not silently use `main`.

Real mount-boundary behavior remains explicitly unproven and optional additional evidence.

## Current resume point

1. publication authorization is already granted; do not ask the Principal to authorize `v0.1.0` again;
2. create real Git tag `v0.1.0` on verified candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588` using an execution surface with tag-write capability;
3. create the GitHub Release for `v0.1.0` from that tag and verify the tag resolves to the intended candidate;
4. only after that verification, mark `0.1.0` published and allow existing compatible Projects to use `latest stable` upgrade;
5. preserve transactional checkpoint, upgrade, commit/push, activation, and safe `AGENTS.md` merge invariants.

## Branch governance

`main` remains the only long-lived authoritative branch. Historical recovery uses immutable commit SHAs and Git history rather than live legacy refs.
