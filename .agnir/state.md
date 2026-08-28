# Agnir Current State

Agnir is the active project/protocol identity on `main`. PPMP v2.0.0 / Persistent Project Memory / Sandminni is predecessor history preserved on `legacy/ppmp-v2.0.0`.

## Active contract line

- Core: Agnir Core `0.1`.
- Repository/filesystem discovery profile: `repository-filesystem/0.1`.
- Authoritative discovery anchor for this Project: top-level `AGNIR.yaml`.
- Authoritative mutable continuity state: `.agnir/` as resolved by `AGNIR.yaml`.
- No execution-surface-specific bootstrap file is part of the active Project structure.
- Active `spec/` now contains only current Agnir protocol material: `AGNIR_CORE.md` and `AGNIR_DISCOVERY.md`.

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

Both READMEs contain a current Architecture Diagram, Continuity Flow diagram, and compact plain-text repository tree. Localized Mermaid diagrams are comprehension-first rather than literal translations.

`REPOSITORY_TREE.md` is the exhaustive file-level map of the active tracked repository. Architecture/continuity changes update both README language versions; tracked file additions/removals/moves or material responsibility changes update `REPOSITORY_TREE.md` in the same change set, and both compact README trees when affected.

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

## Legacy isolation boundary

`legacy/ppmp-v2.0.0` and predecessor PPMP/PPM/Sandminni material are historical lineage only.

They MUST NOT become:

- Agnir Core `0.1` semantic dependencies;
- active conformance fixtures required for Core correctness;
- release gates for Agnir `0.1`;
- compatibility obligations for new Agnir implementations;
- reasons to reintroduce `.chatgpt/`, ChatGPT-specific adapters, predecessor repository structure, or legacy serialization into active `main`.

Optional PPMP migration guidance now lives at `history/MIGRATION_PPMP_V2.md`, outside active `spec/`. It is historical/reference material for consumers that deliberately choose to migrate old PPMP data. It is not part of Core `0.1`, not a conformance requirement, and not a release gate for greenfield Agnir.

Current `main` is a greenfield protocol line. Historical material MAY inform design review, but a rule is active only when it is independently stated by current Agnir Core/profile decisions.

## Current implementation status / resume point

The active Agnir `main` line has a broad executable Core `0.1` conformance baseline across storage neutrality, authorization, multi-project isolation, failure classes, and repository/filesystem boundaries.

Resume in this order:

1. **Freeze the current Agnir Core `0.1` compatibility and repository release notation** from the present Core/profile contract itself, without using predecessor migration as a prerequisite.
2. **Run a final current-architecture consistency review** across Core, Discovery, repository-filesystem profile, schema, README, conformance, and Svif's Continuity Provider binding.
3. Decide whether the resulting `0.1` line is ready for release-candidate/stable publication based on current architecture and conformance only.
4. Keep real mount-boundary behavior explicitly unproven until a mount-capable environment exists; it is not to be faked as release evidence.
5. Keep legacy branches unchanged as history only.

This remains a working `0.1` development contract until the current-architecture release review is complete.

## Evidence checkpoints

- README/localization: `.agnir/evidence/2026-08-28-readme-diagram-localization-checkpoint.md`.
- Negative discovery fixtures: `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`, run `33143495855` success.
- Non-repository SQLite backend: `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`, run `33143655399` success.
- External-memory authorization: `.agnir/evidence/2026-08-28-external-memory-authorization.md`, run `33143771320` success.
- Multi-project workspace isolation: `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`, run `33143930233` success.
- Locator Chain failures: `.agnir/evidence/2026-08-28-locator-chain-failures.md`, run `33144042330` success.
- Filesystem boundaries: `.agnir/evidence/2026-08-28-filesystem-boundaries.md`; corrected run `33144199717` success.
- Repository documentation baseline: pre-checkpoint head `0ca0982a6807acd4af3bf945601f85a5882b88bc`, conformance run `33146757923` success.

## Branch governance

- `main`: authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0`: immutable predecessor history only.
- Incidental branch cleanup remains deferred until the new version is substantially complete.
