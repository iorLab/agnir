# Agnir Current State

Agnir `v0.1.0` is formally published.

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
- repository release: `0.1.0`
- Agnir Core remains storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.

## Stable upgrade status

`latest stable` has a real published stable target. Existing compatible Agnir Projects may use the first-class upgrade operation against `v0.1.0`.

Compatible upgrade preserves Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions. Projects without historical `agnir/operations` provenance remain valid upgrade inputs. Core/profile compatibility changes remain migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.

## README entry architecture

The repository entry documentation is now intentionally split by audience before architecture material:

1. `Start Here` / `从这里开始` — minimal user actions for install, upgrade, and normal continuation;
2. `Agnir Project Instructions` — canonical Agent activation/operation guidance;
3. `Architecture Diagram` / `架构图` — beginning of explanatory architecture, packaging, compatibility, release, and implementation material.

The user-facing install/upgrade prompts remain one sentence each. Root `SKILL.md` owns the detailed Agent operational procedure. Conformance enforces the entry ordering so implementation detail does not drift back into the user-facing front section. Durable rationale is recorded in `.agnir/evidence/2026-09-01-readme-information-architecture.md` and `.agnir/decisions.md`.

## Checkpoint and repository invariants

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free activation, and safe non-destructive `AGENTS.md` merge remain active.

## Post-release maintenance

The temporary branch `release-v0.1.0-candidate` has been deleted; `main` remains the only intended long-lived branch. `README.md` and `README.zh-CN.md` now describe the published `v0.1.0` state. `RELEASE.md` still contains pre-publication wording and remains a documentation-maintenance item; this does not affect the immutable published tag.

## Branch governance

`main` remains the only intended long-lived authoritative branch. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
