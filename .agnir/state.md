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
- All named Core discovery failure classes now have executable conformance pressure: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`.
- Profiles, implementations, backends, and adapters remain outside Core unless their semantics are independently generalized.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Svif's stable kernel depends on a Continuity Provider interface; the current founding implementation uses Agnir Core `0.1` through an Agnir adapter. Agnir remains independently useful and does not absorb Svif execution, delivery, provider, authority, or distribution semantics.

## README architecture documentation

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`. Both contain current Architecture and Continuity Flow Mermaid diagrams and expose the active conformance commands. Architecture/continuity changes require both languages to be updated in the same change set; localized diagrams are comprehension-first rather than literal translations.

## Conformance coverage

The active suite now spans:

- self-hosting `repository-filesystem/0.1` cold start;
- explicit repository/filesystem negative discovery semantics;
- durable non-repository SQLite continuity, including checkpoint and fresh-resolver resume;
- external-memory authorization (`NOT_FOUND` vs `UNAUTHORIZED` vs authorized-but-`UNRESOLVABLE`) using authorization references only;
- multi-project workspace isolation with locator-only registry metadata;
- generic Locator Chain `CYCLE`, `STALE`, and material `INCONSISTENT` semantics;
- repository/filesystem indirection pressure for symlinked Project Entry Points, rejection of relative-locator symlink escape, and real Git worktree cold start.

### Repository/filesystem boundary rule

An authorized symlink Project Entry Point may canonicalize to one selected Project root. A relative memory locator that escapes that root through a symlink is not implicitly authorized external memory and fails `AGNIR_DISCOVERY_UNRESOLVABLE` unless an explicit external Locator Chain exists.

A Git worktree is a valid Project root when its own top-level `AGNIR.yaml` and declared continuity are present. Discovery does not depend on `.git` being a directory.

The first worktree fixture correctly failed because its declared Evidence directory was empty and therefore not tracked by Git. The fixture was repaired by persisting real Evidence, not by weakening resolver semantics.

Real mount-boundary behavior remains unproven and must not be represented by a fake ordinary-directory test.

## Predecessor migration audit

The migration specification remains explicitly **PPMP v2 -> Agnir 0.1**. Current accessible real predecessor Projects inspected during the migration audit do not provide a second external Project with a clear PPMP v2.0.0 manifest.

`iorLab/svif@legacy/zerolocal-v0.1` is genuine external predecessor evidence relative to Agnir and is suitable for validating predecessor-memory -> Agnir semantic migration. Its `.chatgpt/project-memory.yaml`, however, is an earlier v1/RPM-era serialization rather than PPMP v2.0.0. `mattamior/agent-skills` likewise carries an older `.chatgpt/project-memory.yaml` form.

These older real Projects MUST NOT be relabeled as PPMP v2 fixtures. They MAY validate predecessor fallback semantics and durable-knowledge preservation, but exact external PPMP v2 migration evidence remains unmet unless a qualifying Project is found or an explicitly classified non-historical PPMP v2 fixture is introduced.

The Svif predecessor audit already exposed one material migration regression: ZeroLocal predecessor state explicitly preserved `installable-plugin` as long-term product intent, while the rewritten Svif state had generalized this to `distribution` and lost the exact durable intent. Svif is restoring the Plugin target. This confirms that Agnir migration validation must compare material Project knowledge, not merely verify that target locator files exist.

## Current implementation status

The active Agnir main line has a broad executable Core `0.1` conformance baseline across storage-neutral, authorization, multi-project, failure-class, and repository/filesystem boundary cases. The remaining release-pressure work is primarily migration reconciliation and final compatibility/release notation.

This remains a working `0.1` development contract, not yet a final release.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Negative discovery fixtures: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`, run `33143495855` success.
- Non-repository SQLite backend: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`, run `33143655399` success.
- External-memory authorization: `.agnir/evidence/2026-08-28-external-memory-authorization.md`, run `33143771320` success.
- Multi-project workspace isolation: `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`, run `33143930233` success.
- Locator Chain failures: `.agnir/evidence/2026-08-28-locator-chain-failures.md`, run `33144042330` success.
- Filesystem boundaries: `.agnir/evidence/2026-08-28-filesystem-boundaries.md`; corrected run `33144199717`, job `98761550583`, success.
- Conformance / migration-audit checkpoint: `.agnir/evidence/2026-08-28-conformance-and-migration-audit-checkpoint.md`.
- Pre-checkpoint head `16adfdf69156eda5393f94495f250dccdff27117`; Agnir conformance run `33144314449` success.

Resume point: complete a real predecessor-memory -> Agnir migration evidence envelope using the Svif predecessor while clearly labeling it as pre-PPMP-v2/v1-era evidence; then reconcile whether exact external PPMP v2 evidence is required for Core `0.1` release and freeze compatibility notation accordingly. A real mount-boundary case remains unproven until an appropriate environment is available.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branch cleanup remains deferred until the new version is substantially complete.
