# Agnir Current State

Agnir is the active project/protocol identity on `main`. PPMP v2.0.0 / Persistent Project Memory / Sandminni is predecessor history preserved on `legacy/ppmp-v2.0.0`.

## Active contract line

- Core: Agnir Core `0.1`.
- Repository/filesystem discovery profile: `repository-filesystem/0.1`.
- Authoritative discovery anchor for this Project: top-level `AGNIR.yaml`.
- Authoritative mutable continuity state: `.agnir/` as resolved by `AGNIR.yaml`.
- `.chatgpt/project-memory.yaml` is a ChatGPT bootstrap compatibility shim only; it is not Agnir Core and is not authoritative over `AGNIR.yaml`.

## Core invariants

- Durable continuity belongs to the Project, not an Executor, execution environment, VCS, repository host, or conversation.
- A fresh Executor given only an authorized Project Entry Point must be able to resolve the Discovery Record and required durable state without predecessor-private context.
- Required durable memory semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agnir Core is storage-, platform-, VCS-, repository-, and execution-surface-neutral.
- Project identity mismatch, broken locators, unsupported versions, authorization failures, cycles, ambiguity, stale locators, and materially inconsistent memory are explicit discovery failures.
- Profiles, implementations, backends, and adapters remain outside Core unless their semantics are independently generalized.

## Relationship to Svif

Svif is a separate Project in `iorLab/zerolocal`. Dependency direction is `Svif -> Agnir`. Svif consumes the Agnir Core protocol contract, not this repository's storage layout, implementation, backend, or ChatGPT shim.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The first real Agnir main-line structure is active: `AGNIR.yaml`, `.agnir/`, normative Core/Discovery/Profile documents, a manifest JSON Schema, and an executable cold-start structural conformance check exist on `main`.

This is a working `0.1` development contract, not yet a final release. Repository/filesystem conformance is now concrete enough for this repository to self-host through Agnir discovery rather than PPMP/PPM maintenance memory.

## Known gaps

- Non-repository persistence conformance fixture is not yet implemented.
- Multi-project workspace isolation fixture is not yet executable.
- External-memory authorization fixture is not yet implemented.
- Nested project, symlink, mount, and worktree edge cases need dedicated repository/filesystem tests.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.
