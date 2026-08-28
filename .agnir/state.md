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

## Repository/filesystem conformance status

The active conformance path uses `conformance/repository_filesystem_reference.py` as a conformance-only executable reference. It is not a promoted production implementation/backend.

`conformance/check_agnir_0_1.py` self-hosts this repository through that resolver, while `conformance/test_repository_filesystem_failures.py` pressure-tests explicit discovery semantics.

Proven cases include:

- missing top-level Discovery Record -> `AGNIR_DISCOVERY_NOT_FOUND`;
- broken required locator -> `AGNIR_DISCOVERY_UNRESOLVABLE`;
- unsupported Core version -> `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- Project identity mismatch -> `AGNIR_DISCOVERY_PROJECT_MISMATCH`;
- multiple unresolved candidate roots before authority selection -> `AGNIR_DISCOVERY_AMBIGUOUS`;
- nested parent/child Projects remain isolated once one root is explicitly selected.

Selected-root rule: after a Project Entry Point has selected a repository/filesystem root, a mismatch at that root is not repaired by searching a parent or child Project.

## Non-repository storage-neutrality evidence

Agnir Core has an executable durable database-style conformance path under `conformance/sqlite_backend_reference.py` and `conformance/test_sqlite_backend.py`.

The SQLite Project Entry Point is a database locator plus durable project key. The fixture does not use `AGNIR.yaml`, `.agnir/`, repository-root discovery, Git, or GitHub. It proves cold-start Discovery Record resolution, version/identity validation, Current State / Next Actions / Decisions / Evidence recovery, checkpoint persistence, and fresh-resolver resume from the database-backed continuity store.

This fixture is conformance evidence only; it does not define a normative SQLite profile or promote SQLite into Agnir Core.

## External-memory authorization evidence

Agnir Core now has executable external-memory authorization pressure under `conformance/external_memory_reference.py` and `conformance/test_external_memory_authorization.py`.

The fixture preserves three distinct layers:

- external Discovery Record absent -> `AGNIR_DISCOVERY_NOT_FOUND`;
- Discovery Record known but its authorization reference is not granted -> `AGNIR_DISCOVERY_UNAUTHORIZED`;
- authorization granted but a declared required memory object is absent -> `AGNIR_DISCOVERY_UNRESOLVABLE`.

The Discovery Record carries only a durable authorization reference such as `credential-ref://...`; no plaintext credential/token/password/secret value is stored or transported in Agnir continuity.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The active Agnir main line contains normative Core/Discovery/Profile documents, self-hosting repository/filesystem cold-start conformance, executable discovery-failure fixtures, a durable non-repository SQLite fixture, and an external-memory authorization fixture with reference-only authorization semantics.

The former ChatGPT-specific bootstrap shim has been removed from active `main`. Cold start for this repository now begins directly at `AGNIR.yaml`, matching the repository/filesystem profile and keeping execution-surface integration outside the Project structure.

This is a working `0.1` development contract, not yet a final release.

## Known gaps

- Multi-project workspace isolation beyond selected nested roots is not yet executable.
- Symlink, mount, and worktree boundary edge cases need dedicated repository/filesystem tests.
- Cycle, stale-locator, and materially inconsistent-memory failure fixtures remain to be added.
- PPMP v2 -> Agnir external migration validation remains incomplete.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.

## 2026-08-28 README/localization checkpoint

- Simplified Chinese diagram clarification commit: `0f9f9ec3371fa6560d237bf7224adf5430bc0a19`.
- Localization-policy decision commit: `fbcbef93cd17434999e431b3d7af3af4c810c351`.
- Agnir conformance run `33142765236`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.

## 2026-08-28 discovery conformance advance

- Shared conformance resolver: `5a8c79959248f04f9c453afc8bc732b7e55a8af7`.
- Negative fixture suite: `63cec0a2feda44fe6102e176afa5c99b444462e4`.
- Self-hosting checker refactor: `6269ff4f01ad4b57c6406def87d037b2665324fe`.
- CI integration: `02dd1662fadf5451acfcb26370d6f36ff0d4bc8e`.
- Nested-root semantic clarification: `2cbad2ad80e18bb674a88f5d91e1d51cc217cdbd`.
- Agnir Core Svif relationship correction: `3645bce8940e2e4c3d4c811709852eb9f3dcf8fa`.
- Conformance run `33143495855`, job `98759373389`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`.

## 2026-08-28 non-repository backend advance

- Shared Core conformance semantics: `ecad85a8618fa8774f6dd256378e37f97ff6266e`.
- SQLite backend reference: `7c0c5dd82c6f74968c0d65c51c4194ccdaacaa26`.
- SQLite backend tests: `08a0cb3f2707b3b5fcd7fdbf0b24a32f4fd0c7eb`.
- Checker registration: `cf260a1f864a47d2a08902c8c8db069b2cf9003b`.
- Conformance run `33143655399`, job `98759873676`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`.

## 2026-08-28 external-memory authorization advance

- External-memory reference: `60a10aaa10f52ce7ab95bcdc2e5ba7983cc7dd0f`.
- Authorization tests: `82585c5b9d6fd38951392710baf238a55d1b237c`.
- Checker registration: `775c8b0657c445514c52fd70ff5988d92ac8275d`.
- Conformance run `33143771320`, job `98760235526`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-external-memory-authorization.md`.
- Resume point: multi-project workspace isolation, then remaining failure classes and filesystem boundary edge cases.
