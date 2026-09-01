# Agnir 0.1.0 Release

**Repository version:** `0.1.0`

**Core compatibility line:** `0.1`

**Repository/filesystem profile:** `repository-filesystem/0.1`

## Status

The current `main` is the Agnir `0.1.0` pre-publication line. This document does not itself create a Git tag or GitHub Release. After any material pre-publication contract/conformance change, the resulting publication commit must pass the full conformance gate before it is treated as the publication candidate.

Agnir `0.1` is a greenfield protocol line. Historical PPMP / PPM / Sandminni material under `history/` is lineage/reference material only and is not part of the active compatibility contract, conformance baseline, or release gate.

## Version model

Agnir separates three version layers:

- `agnir.version: "0.1"` identifies the Core compatibility line in a Discovery Record.
- `repository-filesystem/0.1` identifies the compatibility line of the repository/filesystem discovery profile.
- `VERSION` records the SemVer release of this reference specification/conformance/Skill repository.

Breaking Core semantics require a new Core compatibility line. Breaking repository/filesystem profile semantics require a new profile compatibility line after publication. Patch releases may clarify text, strengthen non-breaking conformance, or fix reference/Skill tooling without changing those compatibility identifiers.

The durable Agent-activation route, transactional checkpoint invariants, repository commit/push event integration, compatible existing-Project upgrade procedure, and root Agent Skill are incorporated before the first `v0.1.0` publication. They are part of the initial operational distribution surface, not post-publication compatibility changes.

## Skill packaging boundary

Root `SKILL.md` is the canonical Agent-facing Agnir Skill entrypoint. It owns the detailed install / initialize / upgrade / resume / checkpoint / commit / push / repair procedure.

The README deliberately exposes only a short user-facing install request:

```text
Install and initialize Agnir for this Project: https://github.com/iorLab/agnir
```

The Skill also accepts a short upgrade intent such as `Upgrade Agnir to the latest stable release`. An upgrade is not re-initialization: compatible upgrades preserve Project identity, memory locators, durable continuity, and unrelated Project instructions.

## Existing-Project upgrade boundary

For `repository-filesystem/0.1`, an operational upgrade is compatible only while Core remains `0.1` and the profile remains `repository-filesystem/0.1`. A Core/profile compatibility-line change is migration-required and must not be silently applied as an upgrade.

A Project may record the applied operational package under optional `extensions.agnir/operations` provenance with distribution, repository release, source, and immutable applied revision. Projects created before this provenance existed remain valid and can be upgraded non-destructively.

`latest stable` means an actually published stable tag/release. A moving `main` branch or untagged revision is not a stable upgrade target unless explicitly authorized as a non-stable target.

## Release scope

The `0.1.0` release includes:

- stable normative Core continuity semantics;
- checkpoint no-op, coherent authoritative transition, mixed-generation prevention, and stale-base `AGNIR_CHECKPOINT_CONFLICT` semantics;
- normative discovery and failure semantics;
- `repository-filesystem/0.1` profile and manifest schema;
- compatible existing-Project upgrade semantics that preserve identity/continuity, distinguish upgrade from migration, reject implicit `main`-as-stable behavior, and support optional operational-package provenance;
- repository/VCS integration semantics where commit intent evaluates/reconciles continuity before commit, commit-and-push verifies the declared authoritative ref, and observed commits trigger evaluation rather than unconditional mutation;
- root `SKILL.md` Agent Skill packaging with YAML frontmatter and complete operational procedure;
- one-line user-facing installation UX separated from the Agent-facing procedure;
- non-destructive existing-`AGENTS.md` merge semantics;
- Agent-operable repository initialization with durable activation via `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml`;
- prompt-free fresh-Agent activation pressure;
- self-hosting cold-start validation;
- executable pressure for checkpoint semantics, compatible upgrade classification/provenance preservation, and all named discovery failure classes;
- durable non-repository SQLite continuity pressure;
- external-memory authorization pressure without plaintext credentials;
- multi-project isolation pressure;
- Locator Chain cycle, stale, and inconsistency pressure;
- symlink and real Git worktree boundary pressure;
- bilingual README architecture/Skill/activation/continuity documentation;
- main-only branch governance and immutable historical indexing.

## Known limitation

Real mount-boundary behavior remains explicitly unproven because the current conformance environment does not provide a real mount-capable test case. Ordinary directories are not accepted as substitute evidence.

Execution surfaces differ in how they discover/install Agent Skills and inspect Project instructions. Agnir publishes a repository-root `SKILL.md` and persists the Project activation route; platform-specific Skill installation/discovery mechanics remain outside Agnir Core.

Repository hooks are optional event-capture mechanisms. Agnir's commit/push integration contract does not require hooks and does not make Git/VCS a Core dependency.

Stable upgrade resolution depends on a stable Agnir release being published. Before the first stable tag/release exists, an instruction to upgrade to the latest stable release must not silently fall back to `main`.

## Publication gate

A publication commit is ready when all of the following hold:

1. `VERSION` is `0.1.0`;
2. `AGNIR.yaml`, schema, Core spec, discovery spec, profile, README files, Skill package, and conformance baseline agree on the Core/profile compatibility lines;
3. root `SKILL.md` has valid Agent Skill frontmatter and owns the detailed install / initialize / upgrade / resume / checkpoint / commit / push / repair procedure;
4. Core checkpoint semantics require no-op evaluation when truth is unchanged, coherent authoritative publication, mixed-generation rejection, and stale-base conflict handling;
5. repository/filesystem upgrade guidance preserves Project identity/memory on compatible upgrades, treats Core/profile changes as migration-required, records optional operational provenance without redefining Core/profile identity, and never silently treats `main` as a stable release;
6. repository/filesystem guidance treats repository commit intent as checkpoint-before-commit, prefers one revision for Project + Agnir changes, treats commit-and-push as publication + verification, and does not turn observed commits into unconditional writes;
7. both READMEs expose the short user-facing install prompt, point Agents to `SKILL.md`, do not duplicate the Agent installation checklist in Quick Start, and persist repository commit-boundary behavior in `Agnir Project Instructions`;
8. the Skill/profile contract preserves pre-existing target `AGENTS.md` instructions, keeps the Agnir addition locator-only and idempotent, and blocks on a material instruction conflict rather than deleting or overriding Project-owned rules;
9. root `AGENTS.md` points to the canonical README `Agnir Project Instructions` section;
10. Agent activation conformance proves Project root → `AGENTS.md` → README instruction → `AGNIR.yaml` → durable memory without a repeated bootstrap prompt;
11. executable merge pressure proves existing `AGENTS.md` content is preserved and an explicit contradictory instruction fails before merge;
12. checkpoint conformance proves no-op evaluation, complete-generation publication, and stale-base conflict rejection;
13. upgrade conformance proves legacy/no-provenance compatible upgrade, identity/memory preservation, no-op on same provenance, explicit opt-in for unstable targets, and migration-required behavior for Core/profile changes;
14. active protocol/profile files contain no dependency on retired predecessor branch refs or predecessor bootstrap layouts;
15. the full self-hosting and executable conformance suite passes on the publication commit;
16. `main` is the only live branch and historical branch tips remain indexed under `history/`;
17. known limitations are stated without being represented as proven.

Tagging `v0.1.0` or creating a GitHub Release is a separate publication action.
