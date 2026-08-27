# Agnir Core 0.1 Transition Decisions — 2026-08-27

**Status:** Active architecture decisions during the Agnir transition.  
**Historical consolidated decisions:** `docs/project-memory/DECISIONS.md`

This record captures decisions made after the 2026-08-27 17:58 +08:00 full checkpoint without rewriting predecessor PPMP decision history.

## Agnir identity and versioning

- **Agnir** is the umbrella identity for the new project/protocol lineage.
- The new lineage does not require the predecessor PPMP protocol / PPM implementation / Sandminni brand naming stack.
- Agnir starts a new explicit version namespace with target line **Agnir Core 0.1**.
- PPMP v2.0.0 remains released predecessor evidence and MUST NOT be silently relabeled as Agnir conformance.

## Layer model

The target layer separation is:

`Agnir Core -> Profiles -> Implementations -> Backends -> Adapters`

Technology used by a reference implementation or adapter MUST NOT become Core merely because it is convenient or historically present.

## Project ownership and roles

- Durable memory belongs to the **Project**.
- **Principal** is the neutral authority/intent/policy role.
- **Executor** is the neutral entity performing operations.
- Agnir conformance does not depend on AI, conversation, ChatGPT, Git, GitHub, a repository host, local/remote execution, or a particular storage layout.

## Durable-memory semantics

Agnir Core durable memory covers at least:

- Current State;
- Next Actions;
- Decisions;
- Evidence / Checkpoints.

Current State represents present truth rather than chronology. Executor-private context and raw conversation history are not required continuity mechanisms.

## Cold-start discovery

Cold-start discovery is a Core invariant rather than an adapter-specific fresh-conversation convention.

A compatible fresh Executor given an authorized Project Entry Point must be able to resolve:

`Project Entry Point -> Discovery Record -> Locator Chain -> required durable Agnir state`

without predecessor-private context.

The draft portable discovery failure classes include not-found, ambiguity, unsupported version, Project mismatch, unresolvable locator, authorization, cycle, stale locator, and inconsistent memory.

## Repository/filesystem discovery profile

- Agnir Core does **not** require a discovery filename.
- The first repository/filesystem profile standardizes top-level **`AGNIR.yaml`** as its discovery anchor.
- `.agnir/` is an optional recommended colocated memory directory, not a Core requirement and not authoritative without the manifest locators.
- VCS/repository/ref metadata belongs to profile/backend extensions, not Core.
- `.chatgpt/project-memory.yaml` may be recognized only in explicit predecessor/migration mode; its presence alone does not establish Agnir conformance.

## Migration boundary

PPMP v2 -> Agnir migration uses explicit modes:

1. PPMP v2 predecessor mode;
2. migration mode;
3. Agnir 0.1 mode.

Physical rename of files, repositories, or branding does not by itself complete semantic migration. A migrated Project must preserve durable knowledge and pass Agnir cold-start discovery.

## Svif dependency

- Dependency direction is **Svif -> Agnir**.
- Svif should depend on a compatible **Agnir Core protocol version**, not on a particular Agnir implementation/backend/adapter.
- Current draft target is the Agnir Core 0.1 line; exact release compatibility remains unfrozen until the Core/discovery contract is stable.
- Svif-specific delivery/provider lifecycle semantics and stricter protected-secret rules do not belong in Agnir Core unless independently justified as general continuity semantics.

## Self-hosting during transition

`mattamior/rpm` may continue maintaining itself through PPMP v2 / PPM + repository backend + ChatGPT adapter while Agnir 0.1 is still a draft.

That configuration is **migration mode**, not an Agnir conformance claim. The repository should not create an authoritative `AGNIR.yaml` merely to match naming before the schema and cold-start conformance procedure are stable enough to test.
