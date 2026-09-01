# Agnir Current State

Agnir `v0.1.0` remains the formally published stable release. Repository release `0.1.1` is now in publication-candidate preparation after the execution-surface activation repair passed both repository conformance and the real ChatGPT `skills-hub` fresh-context regression.

Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.

## Published stable release

- repository release: `0.1.0`
- Git tag: `v0.1.0`
- tag target: `2a0cb7bf2068b11f361e315670b2f2dc497b2588`
- GitHub Release id: `380187574`
- Release title: `Agnir v0.1.0`
- published at: `2026-09-01T03:09:36Z`
- draft: false
- prerelease: false

The published tag resolves directly to the exact verified publication candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`. Later `main` work does not redefine that immutable release target.

## Active compatibility contract

- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
- latest published stable repository release: `0.1.0`
- repository release candidate line on `main`: `0.1.1`
- Agnir Core remains storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.

## Execution-surface activation repair

A real ChatGPT Project initialization of `mattamior/skills-hub` exposed an operational gap: repository activation was installed successfully, but the initializer did not hand the Principal the persistent ChatGPT Project Instructions needed for a genuinely fresh ChatGPT conversation to locate the canonical repository. The initializer then reported fresh activation too broadly.

The repair on `main` establishes these invariants:

- repository activation and execution-surface activation are separate completion dimensions;
- a surface that needs persistent workspace/Project configuration must be configured when possible or receive a copy-ready locator-only handoff;
- pending or unverified surface configuration blocks a claim that full fresh activation passed;
- ChatGPT Project handoff is an execution-surface adapter and does not duplicate Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure;
- README documentation and architecture/continuity diagrams describe the one-time handoff without making it part of Agnir Core;
- regression conformance protects the canonical Project/surface boundary.

Repository implementation/conformance was green before the real-surface test, including GitHub Actions `Agnir conformance` run `33497764549` on exact revision `b46656793a5e1ea7a94e39f2da1506fc73db177e`.

## Real ChatGPT execution-surface validation

The Principal appended/merged the generated locator-only bootstrap into the real ChatGPT web `skills-hub` Project Instructions and opened a genuinely fresh conversation. The first substantive request was an ordinary Project-status request with no repeated Agnir bootstrap prompt and no repository address supplied in the conversation.

The fresh conversation immediately identified `mattamior/skills-hub`, stated that repository-managed Agnir durable state was authoritative, and began fetching root `AGENTS.md`, `AGNIR.yaml`, and the declared continuity. The Principal supplied a screenshot and explicitly reported the regression test as **passed**.

Durable Evidence: `.agnir/evidence/2026-09-01-v0.1.1-execution-surface-validation.md`.

The real execution-surface gate that previously blocked `v0.1.1` release preparation is therefore closed.

## 0.1.1 publication-candidate preparation

`main` is being synchronized for repository SemVer `0.1.1` without changing Core/profile compatibility:

- `VERSION` is `0.1.1`;
- the self-hosting checker expects repository release `0.1.1`;
- `README.md` and `README.zh-CN.md` describe the `0.1.1` candidate while keeping `v0.1.0` as the published stable release until publication actually occurs;
- `RELEASE.md` defines the `0.1.1` patch scope and exact-candidate gate;
- the real ChatGPT regression Evidence is persisted.

The next publication gate is a full GitHub Actions conformance pass on the exact final candidate revision. Only that exact verified revision may be used as the immutable `v0.1.1` tag/release target.

## Stable upgrade status

`latest stable` still resolves to published `v0.1.0` until `v0.1.1` is actually tagged/released. Existing compatible Agnir Projects must not silently upgrade from moving `main`.

After `v0.1.1` publication, upgrading an existing compatible Project from repository release `0.1.0` to `0.1.1` remains a compatible operational upgrade because Core/profile stay `0.1` / `repository-filesystem/0.1`. Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions remain preserved.

## README entry architecture

The repository entry documentation remains intentionally layered before architecture material:

1. `Start Here` / `从这里开始` — minimal user actions for install, upgrade, and normal continuation;
2. `Agnir Project Instructions` — canonical Agent activation/operation guidance;
3. `What Agnir Adds to a Project` / `Agnir 会给 Project 增加什么` — concrete user-facing map of Project-owned files/directories created, merged, or validated;
4. `Architecture Diagram` / `架构图` — architecture, packaging, compatibility, release, and implementation material.

Execution-surface configuration is shown outside the Project-owned tree and remains locator-only. Root `SKILL.md` owns the detailed Agent operational procedure.

## Checkpoint and repository invariants

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free Project activation, safe non-destructive `AGENTS.md` merge, and explicit execution-surface activation handoff remain active.

## Branch governance

`main` remains the only intended long-lived authoritative branch. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
