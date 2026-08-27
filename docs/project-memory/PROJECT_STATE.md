# Agnir Maintenance State

## Purpose

This repository is the historical RPM repository, the released PPMP v2 / PPM / Sandminni predecessor repository, and the canonical project evolving into **Agnir**.

Agnir is project-owned durable memory/continuity. Its normative semantics are independent of Git, GitHub, repository hosting, ChatGPT, conversational interfaces, any particular AI agent, local-vs-remote execution, and any single storage layout or backend.

## Current status

- Current released predecessor protocol lineage: **PPMP v2.0.0**.
- Current predecessor reference implementation lineage: **Persistent Project Memory (PPM)**.
- Current predecessor public product brand: **Sandminni**.
- New project/protocol identity: **Agnir**.
- Target architecture line: **Agnir Core 0.1**.
- Core architecture draft: `spec/AGNIR_CORE_DRAFT.md`.
- Discovery contract draft: `spec/AGNIR_DISCOVERY_DRAFT.md`.
- PPMP v2 -> Agnir migration draft: `spec/AGNIR_MIGRATION_DRAFT.md`.
- Repository: `mattamior/rpm` (repository rename remains deferred).
- The repository's own maintenance memory still runs through PPMP v2 / PPM with the repository backend and ChatGPT adapter during migration. This is intentional predecessor self-hosting and is not an Agnir conformance claim.

## Architecture decisions now established

- **Agnir is the umbrella identity** for the new project/protocol lineage. The new architecture does not preserve a required PPMP-protocol / PPM-implementation / Sandminni-brand naming stack.
- Agnir begins a **new explicit version namespace** with the target line `Agnir Core 0.1`; PPMP v2.0.0 remains historical predecessor evidence rather than being silently renumbered or relabeled.
- The layer model is: **Agnir Core -> Profiles -> Implementations -> Backends -> Adapters**.
- Durable memory belongs to the **Project**, not to an Executor, execution environment, repository host, VCS, or chat.
- The neutral authority/execution vocabulary is **Principal** and **Executor**.
- Core durable-memory semantics include **Current State**, **Next Actions**, **Decisions**, and **Evidence / Checkpoints**.
- Discovery is modeled through a **Project Entry Point**, **Discovery Record**, and resolvable **Locator Chain**.
- No top-level filename such as `AGNIR.yaml` is currently required by Core. A filesystem/repository discovery profile may standardize one later if conformance evidence justifies it.
- Externally stored Agnir state is allowed only when the Project has a durable, authorized route from its Project Entry Point to that state.
- A fresh Executor with no predecessor-private context must be able to resolve the Locator Chain, validate the Agnir version line, verify Project identity, load required current memory, surface inconsistencies, and resume safely. This is the **cold-start discovery invariant**.
- Discovery failure semantics now have draft portable classes covering not-found, ambiguity, unsupported version, Project mismatch, unresolvable locator, authorization, cycle, stale locator, and inconsistent memory.
- Agnir Core does not universally prohibit secrets from durable storage; confidentiality is governed by Project policy and consuming profiles/protocols. Discovery Records should use authorization/credential references rather than embedded secret values.
- PPMP v2 -> Agnir migration has three explicit states: predecessor PPMP v2 mode, migration mode, and Agnir 0.1 mode. A Project must not be silently promoted between them.

## Relationship to Svif

- **Svif** is a separate project evolving from ZeroLocal in `iorLab/zerolocal`.
- Dependency direction remains **Svif -> Agnir**.
- Svif normatively depends on a **compatible Agnir Core protocol version**, not on a specific Agnir implementation/backend/adapter.
- The current draft dependency target is the **Agnir Core 0.1 line**; the exact release compatibility expression is intentionally not frozen until the Core draft stabilizes.
- Agnir remains independently useful outside software delivery, provider workflows, CI/CD, or Svif.

## Multi-project workspace model

- One ChatGPT Project or other execution workspace may coordinate multiple Projects.
- The workspace is not a Project identity and is not an authoritative shared mutable memory store.
- Each Project owns independent Agnir state.
- Cross-project decisions are persisted separately in each affected Project according to their local meaning.
- Workspace-level configuration should remain locator/registry metadata only.
- This Svif/Agnir workspace is a candidate future multi-project conformance case for proving isolated continuity without durable context bleed.

## Historical PPMP v2 architecture retained as evidence

The repository still preserves the predecessor architecture and evidence:

- `spec/` PPMP v2 normative documents;
- `profiles/` composable predecessor profiles;
- `templates/` and `examples/` predecessor serialization/examples;
- `implementations/` PPM reference implementation behavior;
- `backends/` persistence behavior, including repository/Git;
- `adapters/` platform integrations, including ChatGPT;
- `site/` predecessor public presentation;
- `docs/project-memory/` current self-hosted maintenance state.

The earlier `mattamior/tree-hole` migration, repository-backend CI/CD side-effect finding, site CI evidence, and ChatGPT adapter Project Instructions drift findings remain useful implementation evidence and must not be discarded.

## Current focus

Convert the three Agnir 0.1 drafts into a coherent normative set. The next concrete architecture pressure point is the first repository/filesystem discovery profile: it must provide a simple cold-start anchor and migration path from `.chatgpt/project-memory.yaml` without turning a filename or Git repository into Core. After that, define executable discovery conformance cases and freeze the exact Svif compatibility declaration.

## Resolved transition questions

- Agnir uses one umbrella project/protocol identity rather than preserving a mandatory three-name protocol/implementation/brand stack.
- Agnir starts a new `0.1` version line instead of inheriting PPMP's `2.x` number.
- Principal and Executor are the neutral authority/execution roles.
- Cold-start discovery is Core, not merely ChatGPT-adapter bootstrap behavior.
- PPMP v2 projects require explicit migration; physical renames alone do not establish Agnir conformance.
- Repository-backed self-hosting may remain in migration mode until Agnir discovery and conformance are concrete.

## Remaining open questions

- Whether the first repository/filesystem discovery profile standardizes top-level `AGNIR.yaml`, `.agnir/manifest.yaml`, or another anchor convention.
- How that profile represents an authoritative ref/version when Project memory is on a non-default VCS ref without making VCS a Core concept.
- How external-memory Locator Chains authenticate/authorize resolution while keeping identity technology adapter-specific.
- Exact schema/versioning for Discovery Record extensions and profile declarations.
- What release-quality conformance fixture demonstrates a materially non-repository backend.
- What exact release version identifier and compatibility range Svif should declare once Agnir Core 0.1 is frozen.

## Deferred predecessor tasks

The previous PPMP v2 maintenance tasks remain valid evidence/work items but are secondary during the architecture transition:

- fresh-conversation acceptance of the current PPMP/PPM ChatGPT adapter;
- synchronizing and testing the Tree Hole external ChatGPT Project Instructions;
- optional release-quality browser acceptance for the predecessor Sandminni site;
- public repository/domain naming cleanup, license, and site lockfile improvements.

These should be resumed only when it is clear whether their acceptance target is predecessor PPMP/PPM behavior or the Agnir line.

## Latest architecture progress

- Added `spec/AGNIR_CORE_DRAFT.md` defining the Agnir 0.1 target architecture, neutral roles, project-owned continuity, and Svif dependency boundary.
- Added `spec/AGNIR_DISCOVERY_DRAFT.md` defining Discovery Record semantics, Locator Chain resolution, portable discovery failure classes, repair rules, and a cold-start conformance procedure.
- Added `spec/AGNIR_MIGRATION_DRAFT.md` mapping PPMP v2 semantics/configuration into Agnir 0.1 and defining explicit predecessor / migration / Agnir modes.
- Updated `.chatgpt/project-memory.yaml` so the self-hosted maintenance project identifies itself as Agnir while explicitly declaring that PPMP v2 / PPM remains the current predecessor persistence implementation during migration.

## Checkpoint

- Last full checkpoint: **2026-08-27T17:58:00+08:00**.
- Architecture work has advanced since that checkpoint; the next explicit checkpoint should capture the new Core, Discovery, and migration drafts together with the corresponding Svif transition artifacts.
