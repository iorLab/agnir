# Agnir Current State

Agnir is the active project/protocol identity on `main`. PPMP v2.0.0 / Persistent Project Memory / Sandminni is predecessor history preserved on `legacy/ppmp-v2.0.0`.

## Active contract line

- Core: Agnir Core `0.1`.
- Repository/filesystem discovery profile: `repository-filesystem/0.1`.
- Authoritative discovery anchor for this Project: top-level `AGNIR.yaml`.
- Authoritative mutable continuity state: `.agnir/` as resolved by `AGNIR.yaml`.
- No execution-surface-specific bootstrap file is part of the active Project structure.

## Core invariants

- Durable continuity belongs to the Project, not an Executor, execution environment, VCS, repository host, or conversation.
- A fresh Executor given only an authorized Project Entry Point must be able to resolve the Discovery Record and required durable state without predecessor-private context.
- Required durable memory semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agnir Core is storage-, platform-, VCS-, repository-, agent-, and execution-surface-neutral.
- Project identity mismatch, broken locators, unsupported versions, authorization failures, cycles, ambiguity, stale locators, and materially inconsistent memory are explicit discovery failures.
- Profiles, implementations, backends, and adapters remain outside Core unless their semantics are independently generalized.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Svif's stable kernel depends on a Continuity Provider interface; the current founding implementation uses Agnir Core `0.1` through an Agnir adapter. Agnir remains independently useful and does not absorb Svif execution, delivery, provider, or authority semantics.

The canonical projects relevant to this workspace are now `iorLab/agnir` and `iorLab/svif`. The former standalone Svif Cloudflare reference has been retired from active architecture and is not an Agnir dependency.

## README architecture documentation

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs MUST contain an **Architecture Diagram** and **Continuity Flow** diagram. Architecture/continuity changes require both languages to be updated in the same change set. Localized diagrams are comprehension-first, not literal translations.

## Conformance coverage

The active suite now pressure-tests every named Core discovery failure class through executable conformance references while keeping substrate-specific fixtures outside Core.

### Repository/filesystem

`conformance/repository_filesystem_reference.py` proves self-hosting cold start plus `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.

### Non-repository storage neutrality

`conformance/sqlite_backend_reference.py` proves durable continuity without `AGNIR.yaml`, `.agnir/`, repository-root discovery, Git, or GitHub, including checkpoint and fresh-resolver resume.

### External-memory authorization

`conformance/external_memory_reference.py` distinguishes missing external Discovery Record (`NOT_FOUND`), known-but-denied authorization reference (`UNAUTHORIZED`), and authorized-but-missing required memory (`UNRESOLVABLE`) without transporting plaintext credentials.

### Multi-project isolation

`conformance/workspace_registry_reference.py` proves a locator-only shared workspace registry can locate independent Projects without becoming a second continuity root. Checkpointing one Project leaves another Project and the registry unchanged.

### Generic Locator Chain failures

`conformance/locator_chain_reference.py` now proves:

- a revisited locator -> `AGNIR_DISCOVERY_CYCLE`;
- a known superseded/non-authoritative record -> `AGNIR_DISCOVERY_STALE`;
- contradictory chain structure or mixed checkpoint generations -> `AGNIR_DISCOVERY_INCONSISTENT`;
- a coherent multi-hop chain with matching checkpoint generation resolves successfully.

This closes the executable baseline across the complete discovery failure vocabulary named by Core `0.1`.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The active Agnir main line contains normative Core/Discovery/Profile documents and conformance pressure across repository/filesystem, non-repository SQLite, external-memory authorization, multi-project isolation, and generic Locator Chain failure semantics.

This is still a working `0.1` development contract, not yet a final release.

## Known gaps

- Symlink and Git worktree boundary cases are not yet executable in the repository/filesystem suite.
- A real mount-boundary case is not yet proven and should not be simulated as if it were a real mount.
- PPMP v2 -> Agnir external migration validation remains incomplete.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.

## 2026-08-28 evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Negative discovery fixtures: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`, run `33143495855` success.
- Non-repository SQLite backend: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`, run `33143655399` success.
- External-memory authorization: `.agnir/evidence/2026-08-28-external-memory-authorization.md`, run `33143771320` success.
- Multi-project workspace isolation: `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`, run `33143930233` success.
- Locator Chain failures: `.agnir/evidence/2026-08-28-locator-chain-failures.md`, run `33144042330`, job `98761070215`, success.

Resume point: add real repository/filesystem symlink and Git worktree boundary pressure, then external PPMP v2 migration validation and release-compatibility freeze.
