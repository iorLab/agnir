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

Svif is a separate Project, currently in `iorLab/zerolocal` until its approved rename to `iorLab/svif`. Dependency direction is `Svif -> Agnir`. Svif consumes the Agnir Core protocol contract, not this repository's storage layout, implementation, backend, or ChatGPT shim.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The first real Agnir main-line structure is active: `AGNIR.yaml`, `.agnir/`, normative Core/Discovery/Profile documents, a manifest JSON Schema, and an executable cold-start structural conformance check exist on `main`.

This is a working `0.1` development contract, not yet a final release. Repository/filesystem conformance is concrete enough for this repository to self-host through Agnir discovery rather than PPMP/PPM maintenance memory.

At the 2026-08-27 checkpoint, the pre-checkpoint `main` head was `6537fe56157d2673c0ddc8b205919c73fdda117e`; Agnir conformance run `33081100118` completed successfully for that head.

## Repository identity transition

The repository/public name is now approved to change from `mattamior/rpm` to `mattamior/agnir` as the immediate next execution step. This rename should happen before the coordinated Svif and Cloudflare starter renames:

1. `mattamior/rpm` -> `mattamior/agnir`
2. `iorLab/zerolocal` -> `iorLab/svif`
3. `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`

The predecessor branch `legacy/ppmp-v2.0.0` remains unchanged because it intentionally preserves predecessor identity.

Until the GitHub rename actually occurs, `mattamior/rpm` remains the resolvable canonical repository location for this checkpoint. Immediately after the rename, update `AGNIR.yaml`, the ChatGPT bootstrap shim, README/documentation, Svif cross-project references, and CI/reference URLs. GitHub redirect behavior is compatibility only and must not substitute for durable canonical identity.

## Known gaps

- Repository rename and durable reference reconciliation are the immediate next work.
- Non-repository persistence conformance fixture is not yet implemented.
- Multi-project workspace isolation fixture is not yet executable.
- External-memory authorization fixture is not yet implemented.
- Nested project, symlink, mount, and worktree edge cases need dedicated repository/filesystem tests.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.
