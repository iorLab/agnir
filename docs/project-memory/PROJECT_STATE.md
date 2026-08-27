# Agnir Maintenance State

## Purpose

This repository is the historical RPM repository, the current PPMP v2 / PPM / Sandminni development repository, and the canonical project that will evolve into **Agnir**.

Agnir is project-owned durable memory/continuity. Its normative semantics must be independent of Git, GitHub, repository hosting, ChatGPT, conversational interfaces, any particular AI agent, local-vs-remote execution, and any single storage layout or backend.

## Current status

- Current released protocol lineage: **PPMP v2.0.0**.
- Current reference implementation lineage: **Persistent Project Memory (PPM)**.
- Current public product brand: **Sandminni**.
- New target project identity: **Agnir**.
- Repository: `mattamior/rpm` (repository rename is pending and is not required for the architecture decision).
- The Agnir transition is an explicit architecture/naming migration, not a silent relabeling of PPMP v2 claims.
- PPMP v2 already separates protocol semantics, implementation behavior, persistence backends, and platform adapters and already states that Git/repository storage and ChatGPT are not protocol requirements. That work is retained as the immediate architectural predecessor.
- The new Agnir definition strengthens the stable ownership model: durable memory belongs to the **project**, not to an agent, chat, IDE, repository host, VCS, or execution environment.
- Any compatible reader/executor may consume Agnir if it can discover and interpret the project's durable memory according to the applicable contract.
- Discovery and resumability must generalize from ChatGPT-specific fresh-conversation behavior to **cold-start/fresh-executor discovery**.
- A fresh executor must not require predecessor-private context to locate and interpret the project's durable state.
- Git, repository files, databases, documents, APIs, local filesystems, cloud workspaces, or other durable media may be used by implementations/backends; no one of them is normative Core.
- ChatGPT Projects, Project Instructions, Skills, local CLIs, IDE integrations, CI runners, and other execution surfaces belong in adapters/integrations rather than Agnir Core.

## Relationship to Svif

- **Svif** is a separate project evolving from ZeroLocal in `iorLab/zerolocal`.
- Svif builds on Agnir-compatible durable project continuity.
- Dependency direction is **Svif -> Agnir**.
- Agnir does not depend on Svif and must remain useful to projects that do not use Svif or software-delivery workflows at all.
- The exact versioned compatibility/dependency contract between Svif and Agnir is not yet frozen and is a priority design task.

## Multi-project workspace model

- One ChatGPT Project or other execution workspace may contain multiple related projects.
- The workspace is not a project identity and is not an authoritative shared memory store.
- Each project owns independent Agnir state.
- Cross-project decisions are persisted separately in each affected project according to their local meaning.
- Workspace-level configuration should be a thin registry/locator only and must not duplicate mutable project state.
- Project-scoped work should load only the target project's Agnir. Explicitly cross-project work may load both/all affected projects.
- This shared-workspace/separate-memory pattern is a candidate future Agnir conformance scenario for testing multi-project operation without durable context bleed.

## Historical PPMP v2 architecture retained as evidence

The current repository still contains and should preserve until the explicit migration is implemented:

- `spec/` — PPMP v2 normative semantics;
- `profiles/` — composable profiles;
- `templates/` and `examples/` — reference serialization/examples;
- `implementations/` — PPM reference implementation behavior;
- `backends/` — persistence backend behavior, including repository/Git;
- `adapters/` — platform-specific integrations, including ChatGPT;
- `site/` — non-normative public presentation layer;
- `docs/project-memory/` — this repository's own maintenance state.

The earlier `mattamior/tree-hole` migration, repository-backend CI/CD side-effect finding, site CI evidence, and ChatGPT adapter Project Instructions drift findings remain useful implementation evidence. They must not be discarded merely because the public/project identity changes.

## Current focus

Design the explicit PPMP/PPM/Sandminni -> Agnir migration while preserving the useful v2 layer separation. Define Agnir's platform/storage/executor-neutral Core, project-owned discovery semantics, vocabulary, versioning/compatibility policy, and the Svif dependency boundary before performing broad repository/file/site renames.

## Open questions

- Whether Agnir becomes the single umbrella name for protocol + reference implementation family, or whether a subordinate technical protocol/implementation identity remains useful under the Agnir project brand.
- What versioning scheme best preserves PPMP v2 lineage while making the Agnir architecture transition explicit rather than cosmetic.
- What exact discovery invariant is normative when Agnir state is external to the project's immediate filesystem/store.
- Whether a top-level discovery anchor such as `AGNIR.yaml` should be a reference serialization convention or a normative profile requirement; Core must not require a particular path unless evidence justifies it.
- What neutral role names should be standardized for readers/executors/authorities without implying AI or conversation.
- What minimum contract Svif should depend on and how Agnir version compatibility should be declared.
- How to model workspace registries without allowing them to become a second mutable project-memory store.

## Deferred predecessor tasks

The previous PPMP v2 maintenance tasks remain valid evidence/work items but are temporarily secondary to the Agnir architecture transition:

- fresh-conversation acceptance of the current PPMP/PPM ChatGPT adapter;
- synchronizing and testing the Tree Hole external ChatGPT Project Instructions;
- optional release-quality browser acceptance for the Sandminni site;
- public repository/domain naming cleanup, license, and site lockfile improvements.

Where useful, these tasks should be resumed only after deciding whether their expected naming/configuration should target the predecessor PPMP/PPM/Sandminni layer or the new Agnir layer.

## Checkpoint

- Saved: **2026-08-27T17:58:00+08:00**.
- Reason: adopt Agnir as the new project identity, clarify project-owned/platform-neutral semantics, establish the independent Svif -> Agnir relationship, and adopt a shared-workspace/separate-durable-memory model.
- Resumability: repository state is persisted. The external ChatGPT workspace bootstrap still needs a later multi-project registry update before fresh-context multi-project resumability can be claimed as fully synchronized.
