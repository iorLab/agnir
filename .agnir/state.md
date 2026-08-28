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

Both READMEs MUST contain:

- an **Architecture Diagram** showing Agnir Core, discovery/profile realization, and durable continuity components;
- a **Continuity Flow** diagram showing cold-start discovery, load, external Project work, checkpoint, and future resume.

Changes to the layer model, discovery path, durable-memory semantics, Project boundary, or continuity flow require the affected diagrams in both language versions to be updated in the same change set. Conformance checks enforce the README/diagram structure without freezing prose wording.

Localized diagrams are **comprehension-first, not literal translations**. In the Simplified Chinese README, important diagram nodes must be understandable to a Chinese reader without requiring prior knowledge of the English technical term: nodes should explain both the role and its responsibility, while English terminology may remain as a secondary label.

## Conformance coverage

The active conformance suite now pressure-tests Agnir Core across multiple realizations rather than only the self-hosting repository/filesystem path.

### Repository/filesystem

`conformance/repository_filesystem_reference.py` is a conformance-only executable reference. Proven cases include:

- missing top-level Discovery Record -> `AGNIR_DISCOVERY_NOT_FOUND`;
- broken required locator -> `AGNIR_DISCOVERY_UNRESOLVABLE`;
- unsupported Core version -> `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- Project identity mismatch -> `AGNIR_DISCOVERY_PROJECT_MISMATCH`;
- multiple unresolved candidate roots before authority selection -> `AGNIR_DISCOVERY_AMBIGUOUS`;
- nested parent/child Projects remain isolated once one root is explicitly selected.

Selected-root rule: after a Project Entry Point has selected a repository/filesystem root, a mismatch at that root is not repaired by searching a parent or child Project.

### Non-repository storage neutrality

`conformance/sqlite_backend_reference.py` and `conformance/test_sqlite_backend.py` provide a durable database-style path whose Project Entry Point is a database locator plus durable project key. It does not use `AGNIR.yaml`, `.agnir/`, repository-root discovery, Git, or GitHub, and proves cold start, checkpoint, and fresh-resolver resume.

### External-memory authorization

`conformance/external_memory_reference.py` and its tests distinguish:

- absent external Discovery Record -> `AGNIR_DISCOVERY_NOT_FOUND`;
- known record but denied authorization reference -> `AGNIR_DISCOVERY_UNAUTHORIZED`;
- authorization granted but required memory missing -> `AGNIR_DISCOVERY_UNRESOLVABLE`.

Only authorization references are durable; plaintext credential values remain outside Agnir continuity.

### Multi-project workspace isolation

`conformance/workspace_registry_reference.py` and `conformance/test_workspace_isolation.py` prove that a shared workspace registry may locate multiple independent Projects without becoming a shared truth root.

The registry carries only locator metadata. Alpha and Beta use separate durable continuity stores. Checkpointing Alpha leaves Beta's State / Next Actions / Decisions / Evidence unchanged and leaves the registry file byte-for-byte unchanged. Registry entries that embed continuity payloads are rejected as `AGNIR_DISCOVERY_INCONSISTENT`.

The registry is convenience metadata only and is not a required Agnir Core component.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The active Agnir main line contains normative Core/Discovery/Profile documents, self-hosting repository/filesystem cold-start conformance, executable discovery-failure fixtures, a durable non-repository SQLite fixture, external-memory authorization pressure, and multi-project workspace isolation.

The former ChatGPT-specific bootstrap shim has been removed from active `main`. Cold start for this repository now begins directly at `AGNIR.yaml`, matching the repository/filesystem profile and keeping execution-surface integration outside the Project structure.

This is a working `0.1` development contract, not yet a final release.

## Known gaps

- Cycle, stale-locator, and materially inconsistent-memory failure fixtures remain to be added.
- Symlink, mount, and worktree boundary edge cases need dedicated repository/filesystem tests.
- PPMP v2 -> Agnir external migration validation remains incomplete.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.

## 2026-08-28 evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Negative discovery fixtures: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`, run `33143495855` success.
- Non-repository SQLite backend: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`, run `33143655399` success.
- External-memory authorization: `.agnir/evidence/2026-08-28-external-memory-authorization.md`, run `33143771320` success.
- Multi-project workspace isolation: `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`, run `33143930233`, job `98760729955`, success.

Resume point: add explicit `CYCLE`, `STALE`, and materially `INCONSISTENT` discovery fixtures, then filesystem boundary edge cases and migration validation.
