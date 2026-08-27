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
- Architecture draft: `spec/AGNIR_CORE_DRAFT.md`.
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
- A fresh Executor with no predecessor-private context must be able to resolve the Locator Chain, validate the Agnir version line, load required current memory, surface inconsistencies, and resume safely. This is the **cold-start discovery invariant**.
- Agnir Core does not universally prohibit secrets from durable storage; confidentiality is governed by Project policy and consuming profiles/protocols. Svif may impose a stricter protected-secret rule.

## Relationship to Svif

- **Svif** is a separate project evolving from ZeroLocal in `iorLab/zerolocal`.
- Dependency direction remains **Svif -> Agnir**.
- Svif should normatively depend on a **compatible Agnir Core protocol version**, not on a specific Agnir implementation/backend/adapter.
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

Turn `spec/AGNIR_CORE_DRAFT.md` from an architecture draft into a testable Core contract without collapsing implementation/backend/adapter behavior back into Core. In parallel, define an explicit PPMP v2 -> Agnir 0.1 migration mapping and a first repository/filesystem discovery profile, then freeze the exact Svif compatibility declaration.

## Remaining open questions

- What exact normative fields and error semantics belong in the Agnir 0.1 Discovery Record.
- Whether the first repository/filesystem discovery profile standardizes a top-level `AGNIR.yaml`, `.agnir/` layout, or another locator convention.
- How external-memory Locator Chains authenticate/authorize resolution without making a particular identity system normative.
- What migration guarantees are required when converting PPMP v2 Current State / Next Steps / Decisions / checkpoints into Agnir 0.1 semantics.
- What exact release version identifier and compatibility range Svif should declare once Agnir Core 0.1 is frozen.
- Which conformance fixtures best demonstrate storage/execution neutrality rather than merely restating it.

## Deferred predecessor tasks

The previous PPMP v2 maintenance tasks remain valid evidence/work items but are secondary during the architecture transition:

- fresh-conversation acceptance of the current PPMP/PPM ChatGPT adapter;
- synchronizing and testing the Tree Hole external ChatGPT Project Instructions;
- optional release-quality browser acceptance for the predecessor Sandminni site;
- public repository/domain naming cleanup, license, and site lockfile improvements.

These should be resumed only when it is clear whether their acceptance target is predecessor PPMP/PPM behavior or the Agnir line.

## Latest architecture progress

- Added `spec/AGNIR_CORE_DRAFT.md` defining the Agnir 0.1 target architecture, neutral roles, discovery model, cold-start invariant, new version namespace, and Svif dependency boundary.
- Updated `.chatgpt/project-memory.yaml` so the self-hosted maintenance project identifies itself as Agnir while explicitly declaring that PPMP v2 / PPM remains the current predecessor persistence implementation during migration.

## Checkpoint

- Last full checkpoint: **2026-08-27T17:58:00+08:00**.
- Architecture work has advanced since that checkpoint; the next explicit checkpoint should capture the new Agnir Core draft and corresponding Svif transition draft after any review/refinement.
