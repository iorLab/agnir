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
- All named Core discovery failure classes have executable conformance pressure: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`.
- Profiles, implementations, backends, and adapters remain outside Core unless their semantics are independently generalized.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Svif's stable kernel depends on a Continuity Provider interface; the current founding implementation uses Agnir Core `0.1` through an Agnir adapter. Agnir remains independently useful and does not absorb Svif execution, delivery, provider, authority, or distribution semantics.

## Repository documentation baseline

The repository has parallel English and Simplified Chinese entry points: `README.md` and `README.zh-CN.md`.

Both READMEs contain:

- a current Architecture Diagram;
- a current Continuity Flow diagram;
- a compact plain-text repository tree explaining the main directories, key files, and responsibilities.

Localized Mermaid diagrams are comprehension-first rather than literal translations. Simplified Chinese nodes explain both what an object is and what responsibility it has in Agnir.

A separate `REPOSITORY_TREE.md` is the exhaustive file-level map of the active tracked repository. It expands every tracked file and annotates its role in Core, profiles, schemas, conformance, Project continuity, history, CI, or documentation.

Maintenance invariant:

- architecture/continuity changes update both README language versions in the same change set;
- tracked file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set;
- if a change affects the compact README tree, both README language versions update together.

The self-hosting conformance checker enforces the README tree anchors, `REPOSITORY_TREE.md` presence/linkage, and representative deep-file coverage without byte-for-byte locking the documentation prose.

The pre-checkpoint repository-documentation head `0ca0982a6807acd4af3bf945601f85a5882b88bc` passed Agnir conformance run `33146757923`.

## Conformance coverage

The active suite spans:

- self-hosting `repository-filesystem/0.1` cold start;
- explicit repository/filesystem negative discovery semantics;
- durable non-repository SQLite continuity, including checkpoint and fresh-resolver resume;
- external-memory authorization (`NOT_FOUND` vs `UNAUTHORIZED` vs authorized-but-`UNRESOLVABLE`) using authorization references only;
- multi-project workspace isolation with locator-only registry metadata;
- generic Locator Chain `CYCLE`, `STALE`, and material `INCONSISTENT` semantics;
- repository/filesystem indirection pressure for symlinked Project Entry Points, rejection of relative-locator symlink escape, and real Git worktree cold start.

An authorized symlink Project Entry Point may canonicalize to one selected Project root. A relative memory locator that escapes that root through a symlink is not implicitly authorized external memory and fails `AGNIR_DISCOVERY_UNRESOLVABLE` unless an explicit external Locator Chain exists.

A Git worktree is a valid Project root when its own top-level `AGNIR.yaml` and declared continuity are present. Discovery does not depend on `.git` being a directory.

Real mount-boundary behavior remains unproven and must not be represented by a fake ordinary-directory test.

## Predecessor migration audit

The migration specification remains explicitly **PPMP v2 -> Agnir 0.1**. Current accessible real predecessor Projects inspected during the migration audit do not provide a second external Project with a clear PPMP v2.0.0 manifest.

`iorLab/svif@legacy/zerolocal-v0.1` is genuine external predecessor evidence relative to Agnir and is suitable for validating predecessor-memory -> Agnir semantic migration. Its `.chatgpt/project-memory.yaml`, however, is an earlier v1/RPM-era serialization rather than PPMP v2.0.0. Older real Projects MUST NOT be relabeled as PPMP v2 fixtures.

These older real Projects MAY validate predecessor fallback semantics and durable-knowledge preservation, but exact external PPMP v2 migration evidence remains unmet unless a qualifying Project is found or an explicitly classified PPMP v2 fixture is introduced.

The Svif predecessor audit exposed one material migration regression: ZeroLocal predecessor state explicitly preserved `installable-plugin` as long-term product intent, while rewritten Svif state had generalized this to `distribution` and lost the exact durable intent. Svif has restored that target. This confirms that Agnir migration validation must compare material Project knowledge, not merely target locator/file presence.

## Current implementation status / resume point

The active Agnir main line has a broad executable Core `0.1` conformance baseline across storage-neutral, authorization, multi-project, failure-class, and repository/filesystem boundary cases. Remaining release-pressure work is primarily migration reconciliation and final compatibility/release notation.

Resume in this order:

1. complete a real predecessor-memory -> Agnir migration evidence envelope using the Svif predecessor, clearly labeled as pre-PPMP-v2/v1-era evidence;
2. decide whether exact external PPMP v2 evidence is a hard Core `0.1` release requirement or whether an explicitly classified PPMP v2 conformance fixture plus real older-predecessor evidence is sufficient;
3. freeze Agnir Core `0.1` compatibility/release notation after that decision;
4. keep real mount-boundary behavior explicitly unproven until a mount-capable environment exists.

This remains a working `0.1` development contract, not yet a final release.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Negative discovery fixtures: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`, run `33143495855` success.
- Non-repository SQLite backend: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`, run `33143655399` success.
- External-memory authorization: `.agnir/evidence/2026-08-28-external-memory-authorization.md`, run `33143771320` success.
- Multi-project workspace isolation: `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`, run `33143930233` success.
- Locator Chain failures: `.agnir/evidence/2026-08-28-locator-chain-failures.md`, run `33144042330` success.
- Filesystem boundaries: `.agnir/evidence/2026-08-28-filesystem-boundaries.md`; corrected run `33144199717` success.
- Conformance / migration-audit checkpoint: `.agnir/evidence/2026-08-28-conformance-and-migration-audit-checkpoint.md`.
- Repository documentation baseline: pre-checkpoint head `0ca0982a6807acd4af3bf945601f85a5882b88bc`, conformance run `33146757923` success.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary.
- Incidental branch cleanup remains deferred until the new version is substantially complete.
