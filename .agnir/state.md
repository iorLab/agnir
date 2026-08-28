# Agnir Current State

Agnir is the active project/protocol identity on `main`. Repository branch governance is main-only: PPMP/PPM/Sandminni and other predecessor history are preserved by immutable commit SHA and `history/`, not by live legacy branch refs.

## Stable release line

Agnir is **release-ready at repository version `0.1.0`**.

The version layers are deliberately distinct:

- Core compatibility line: `0.1`;
- repository/filesystem discovery profile: `repository-filesystem/0.1`;
- repository release SemVer: `0.1.0`.

The top-level `VERSION` records repository SemVer. Discovery Records continue to declare `agnir.version: "0.1"`; repository SemVer does not replace the Core compatibility identifier.

Breaking Core field meaning, required continuity semantics, identity rules, or discovery invariants requires a new Core line such as `0.2`. Breaking repository/filesystem discovery-anchor, serialization, locator, or selected-root semantics requires a new profile line. Repository `0.1.x` patch releases may make non-breaking clarifications, compatible conformance additions, or reference-tooling fixes without changing the Core/profile compatibility identifiers.

`RELEASE.md` is the current publication contract for `0.1.0`.

## Active contract line

- Stable Core: Agnir Core `0.1`.
- Stable repository/filesystem profile: `repository-filesystem/0.1`.
- Repository release: `0.1.0`.
- Authoritative discovery anchor for this Project: top-level `AGNIR.yaml`.
- Authoritative mutable continuity state: `.agnir/` as resolved by `AGNIR.yaml`.
- No execution-surface-specific or predecessor bootstrap file is part of the active Project structure.
- Active `spec/` contains only current Agnir protocol material: `AGNIR_CORE.md` and `AGNIR_DISCOVERY.md`.

## Core invariants

- Durable continuity belongs to the Project, not an Executor, execution environment, VCS, repository host, or conversation.
- A fresh Executor given only an authorized Project Entry Point must be able to resolve the Discovery Record and required durable state without predecessor-private context.
- Required durable memory semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agnir Core is storage-, platform-, VCS-, repository-, agent-, and execution-surface-neutral.
- All named Core discovery failure classes have executable conformance pressure: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`.
- Profiles, implementations, backends, and adapters remain outside Core unless their semantics are independently generalized.

## Release-readiness review

The stable review reconciled Core, Discovery, repository/filesystem profile, manifest schema, bilingual READMEs, conformance baseline, self-hosting checker, `AGNIR.yaml`, repository version metadata, and Svif's current Core `0.1` Continuity Provider binding.

Release cleanup removed the final active predecessor couplings:

- stale `predecessor_ref` was removed from `AGNIR.yaml`;
- predecessor `.chatgpt/project-memory.yaml` fallback was removed from the active repository/filesystem profile.

Stable publication candidate `846d794384e24f4d0431bb72b0f1036c60503bdd` passed Agnir conformance run `33161463275`.

Durable evidence: `.agnir/evidence/2026-08-28-agnir-0.1.0-release-readiness.md`.

## User-operability baseline

The bilingual README entry points now begin with an operational Quick Start before architecture explanation.

For `repository-filesystem/0.1`, the first-screen path is intentionally minimal:

- an Agent that already has Project-directory read/write access can use an existing Agnir Project by reading top-level `AGNIR.yaml` and following its durable memory locators;
- a new Project can be initialized by an Agent from a copyable prompt that creates the minimal `AGNIR.yaml` and `.agnir/` continuity layout, persists initialization evidence, and verifies a fresh cold start;
- the Quick Start shows the minimal manifest and the four durable continuity categories directly, without requiring the user to understand Core/Profile architecture first.

This is a documentation/usability contract, not a new Core semantic dependency. The self-hosting checker requires the operational Quick Start to remain before the Architecture Diagram in both language versions and requires both existing-Project and initialization paths.

Quick Start enforcement commit `820d8847bba4bc825740972bda19d3cc22378ad0` passed conformance run `33162899443`.

Durable evidence: `.agnir/evidence/2026-08-28-readme-agent-quick-start-checkpoint.md`.

## Bilingual README navigation

The current language-navigation model remains intentionally simple:

- `README.md` is the standalone English entry point;
- `README.zh-CN.md` is the standalone Simplified Chinese entry point;
- each document links to the other as a separate GitHub Markdown page.

Same-page language switching was considered but explicitly deferred. No anchor-based or collapsible bilingual single-page treatment is part of the current `0.1.0` publication surface, and this is not a release blocker.

Durable evidence: `.agnir/evidence/2026-08-28-readme-language-navigation-deferred-checkpoint.md`.

## Conformance coverage

The stable suite spans:

- self-hosting `repository-filesystem/0.1` cold start;
- all nine named discovery failure classes;
- durable non-repository SQLite continuity, checkpoint, and fresh-resolver resume;
- external-memory authorization using authorization references rather than plaintext secrets;
- multi-project workspace isolation with locator-only registry metadata;
- Locator Chain cycle, stale, and material inconsistency semantics;
- symlinked Project Entry Point and symlink-escape boundaries;
- real Git worktree cold start.

Real mount-boundary behavior remains explicitly unproven. Ordinary directories are not accepted as fake mount evidence. This is documented in `RELEASE.md` and is not a Core `0.1` publication blocker.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Its current `AgnirFilesystemContinuityProvider` binds to Core `0.1` and profile `repository-filesystem/0.1`. Svif consumes the Agnir continuity contract, not this repository's historical lineage or a universal Git/GitHub requirement.

## Repository documentation baseline

`README.md` and `README.zh-CN.md` are parallel standalone entry points. Each begins with an operational Quick Start before the Architecture Diagram, then retains synchronized Architecture and Continuity Flow diagrams plus compact annotated repository trees. `REPOSITORY_TREE.md` is the exhaustive tracked-file map and must be updated with tracked file additions/removals/moves or material responsibility changes.

## Historical isolation boundary

PPMP/PPM/Sandminni and other retired work remain lineage/reference material only under `history/` and Git history. They are not Core semantic dependencies, profile compatibility obligations, conformance requirements, or release gates.

Optional historical PPMP migration guidance remains at `history/MIGRATION_PPMP_V2.md`; it is outside active `spec/`.

## Current resume point

Agnir development work required for the initial stable release is complete.

The next operation is **publication only**:

1. after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release;
2. after publication, treat Core `0.1` and profile `repository-filesystem/0.1` as frozen compatibility lines and keep `0.1.x` maintenance non-breaking;
3. keep real mount-boundary validation as optional additional evidence when a real mount-capable environment becomes available;
4. do not alter bilingual README navigation unless the Project explicitly revisits same-page language UX.

## Branch governance

- `main` is the only long-lived branch and the only authoritative Agnir line.
- Retired branch tips are recorded in `history/BRANCH_ARCHIVE.md`.
- Historical recovery uses commit SHAs and Git history, not live branch refs.
