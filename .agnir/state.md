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

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branches are non-authoritative until explicitly promoted; cleanup remains deferred until the new version is substantially complete.

## Current implementation status

The active Agnir main line contains `AGNIR.yaml`, `.agnir/`, normative Core/Discovery/Profile documents, a manifest JSON Schema, and an executable cold-start structural conformance check.

The former ChatGPT-specific bootstrap shim has been removed from active `main`. Cold start for this repository now begins directly at `AGNIR.yaml`, matching the repository/filesystem profile and keeping execution-surface integration outside the Project structure.

This is a working `0.1` development contract, not yet a final release. Repository/filesystem conformance is concrete enough for this repository to self-host through Agnir discovery rather than PPMP/PPM maintenance memory.

At the 2026-08-27 checkpoint, the pre-checkpoint `main` head was `6537fe56157d2673c0ddc8b205919c73fdda117e`; Agnir conformance run `33081100118` completed successfully for that head.

## Repository identity transition

The coordinated repository identity transition is complete.

- Agnir: `iorLab/agnir` (renamed from `mattamior/rpm` and transferred into the `iorLab` organization).
- Svif: `iorLab/svif`.
- Provider-specific Svif Cloudflare behavior now belongs inside `iorLab/svif`; no standalone Cloudflare project is part of the active canonical topology.

The predecessor branch `legacy/ppmp-v2.0.0` remains unchanged because it intentionally preserves predecessor identity. Repository redirects from predecessor names are compatibility behavior only.

## Known gaps

- Non-repository persistence conformance fixture is not yet implemented.
- Multi-project workspace isolation fixture is not yet executable.
- External-memory authorization fixture is not yet implemented.
- Nested project, symlink, mount, and worktree edge cases need dedicated repository/filesystem tests.
- Release compatibility notation consumed by Svif remains provisional until Agnir `0.1` release criteria are complete.

## 2026-08-28 checkpoint

README architecture documentation and localization policy are now durable Project state.

- Simplified Chinese diagram clarification commit: `0f9f9ec3371fa6560d237bf7224adf5430bc0a19`.
- Localization-policy decision commit: `fbcbef93cd17434999e431b3d7af3af4c810c351`.
- Agnir conformance run `33142765236`: success.
- Durable evidence: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Resume point remains Agnir Core `0.1` conformance hardening: negative discovery fixtures, storage-neutral evidence, external-memory authorization, and multi-project isolation.
