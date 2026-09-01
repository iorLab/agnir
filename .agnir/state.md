# Agnir Current State

Agnir `v0.1.0` is formally published.

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
- durable continuity remains Project-owned and storage/VCS/execution-surface neutral at Core level.

## Stable upgrade status

`latest stable` now has a real published stable target. Existing compatible Agnir Projects may use the first-class upgrade operation against `v0.1.0`.

Compatible upgrade preserves Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions. Projects without historical `agnir/operations` provenance remain valid upgrade inputs. Core/profile compatibility changes remain migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.

## Checkpoint and repository invariants

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free activation, and safe non-destructive `AGENTS.md` merge remain active.

## Remaining release cleanup

A temporary branch `release-v0.1.0-candidate` was created only to let the GitHub web Release UI target the verified candidate. It is not a long-lived branch and should be deleted now that `v0.1.0` exists. The current connected GitHub tool does not expose branch deletion.

README/RELEASE pre-publication wording also needs post-release synchronization on `main`; this is documentation maintenance and does not affect the already-published tag.

## Branch governance

`main` remains the only intended long-lived authoritative branch. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
