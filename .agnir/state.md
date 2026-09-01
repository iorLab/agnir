# Agnir Current State

Agnir `v0.1.0` is formally published. A patch-line `v0.1.1` repair is now in preparation for execution-surface activation handoff.

Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.

## Published release

- repository release: `0.1.0`
- Git tag: `v0.1.0`
- tag target: `2a0cb7bf2068b11f361e315670b2f2dc497b2588`
- GitHub Release id: `380187574`
- Release title: `Agnir v0.1.0`
- published at: `2026-09-01T03:09:36Z`
- draft: false
- prerelease: false

The published tag resolves directly to the exact verified publication candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`. That candidate passed GitHub Actions `Agnir conformance` run `33463490510`, job `99718447961`, including self-hosting cold-start conformance and the full executable test suite.

Later `main` checkpoints are post-candidate operational observations and do not redefine the immutable `v0.1.0` release target.

## Active compatibility contract

- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
- published repository release: `0.1.0`
- next intended repository release: `0.1.1` after real execution-surface validation and exact-candidate conformance
- Agnir Core remains storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.

## Execution-surface activation repair

A real ChatGPT Project initialization of `mattamior/skills-hub` exposed an operational gap: repository activation was installed successfully, but the initializer did not hand the Principal the persistent ChatGPT Project Instructions needed for a genuinely fresh ChatGPT conversation to locate the canonical repository. The initializer then reported fresh activation too broadly.

The repair is implemented on `main` through `b46656793a5e1ea7a94e39f2da1506fc73db177e`:

- `SKILL.md` now treats repository activation and execution-surface activation as separate completion dimensions;
- a surface that needs persistent workspace/Project configuration must be configured when possible or receive a copy-ready locator-only handoff;
- pending or unverified surface configuration blocks a claim that full fresh activation passed;
- ChatGPT Project handoff is explicitly an execution-surface adapter and does not duplicate Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure;
- README documentation and architecture/continuity diagrams describe the one-time handoff without making it part of Agnir Core;
- regression conformance checks the handoff contract and protects the canonical Project/surface boundary.

GitHub Actions `Agnir conformance` run `33497764549` passed on exact revision `b46656793a5e1ea7a94e39f2da1506fc73db177e`, including self-hosting cold-start conformance and all executable unit/conformance tests.

Repository-level repair is therefore green. Real ChatGPT execution-surface validation remains pending: the `skills-hub` Project must receive the generated locator-only Project Instructions and then be exercised from a genuinely fresh conversation before `v0.1.1` publication is finalized.

## Stable upgrade status

`latest stable` currently resolves to published `v0.1.0`. Existing compatible Agnir Projects may use the first-class upgrade operation against that release until `v0.1.1` is actually published.

Compatible upgrade preserves Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions. Projects without historical `agnir/operations` provenance remain valid upgrade inputs. Core/profile compatibility changes remain migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.

## README entry architecture

The repository entry documentation is intentionally layered before architecture material:

1. `Start Here` / `从这里开始` — minimal user actions for install, upgrade, and normal continuation;
2. `Agnir Project Instructions` — canonical Agent activation/operation guidance;
3. `What Agnir Adds to a Project` / `Agnir 会给 Project 增加什么` — concrete user-facing map of the files/directories the reference Skill creates, merges, or validates and the responsibility of each;
4. `Architecture Diagram` / `架构图` — beginning of explanatory architecture, packaging, compatibility, release, and implementation material.

The Project-surface section documents `AGENTS.md`, `AGNIR.yaml`, the README instruction section, and the reference `.agnir/` State / Next Actions / Decisions / Evidence layout while explicitly preserving the distinction between profile-specific filesystem conventions and Agnir Core. Execution-surface configuration is shown outside the Project-owned tree and remains locator-only. The user-facing install/upgrade prompts remain one sentence each. Root `SKILL.md` owns the detailed Agent operational procedure.

## Checkpoint and repository invariants

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free Project activation, safe non-destructive `AGENTS.md` merge, and explicit execution-surface activation handoff remain active.

## Post-release maintenance

The temporary branch `release-v0.1.0-candidate` has been deleted; `main` remains the only intended long-lived branch. `RELEASE.md` still contains `v0.1.0` pre-publication wording and should be synchronized as part of the `v0.1.1` release-preparation change set rather than treated as evidence about the already immutable `v0.1.0` tag.

## Branch governance

`main` remains the only intended long-lived authoritative branch. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
