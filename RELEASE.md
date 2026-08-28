# Agnir 0.1.0 Release

**Repository version:** `0.1.0`

**Core compatibility line:** `0.1`

**Repository/filesystem profile:** `repository-filesystem/0.1`

## Status

The current `main` is the Agnir `0.1.0` publication candidate. This document does not itself create a Git tag or GitHub Release.

Agnir `0.1` is a greenfield protocol line. Historical PPMP / PPM / Sandminni material under `history/` is lineage/reference material only and is not part of the active compatibility contract, conformance baseline, or release gate.

## Version model

Agnir separates three version layers:

- `agnir.version: "0.1"` identifies the Core compatibility line in a Discovery Record.
- `repository-filesystem/0.1` identifies the compatibility line of the repository/filesystem discovery profile.
- `VERSION` records the SemVer release of this reference specification/conformance/Skill repository.

Breaking Core semantics require a new Core compatibility line. Breaking repository/filesystem profile semantics require a new profile compatibility line after publication. Patch releases may clarify text, strengthen non-breaking conformance, or fix reference/Skill tooling without changing those compatibility identifiers.

The durable Agent-activation route and the root Agent Skill were incorporated before the first `v0.1.0` publication. They are part of the initial operational distribution surface, not post-publication Core compatibility changes.

## Skill packaging boundary

Root `SKILL.md` is the canonical Agent-facing Agnir Skill entrypoint. It owns the detailed install / initialize / resume / checkpoint / repair procedure.

The README deliberately exposes only a short user-facing install request:

```text
Install and initialize Agnir for this Project: https://github.com/iorLab/agnir
```

The user is not required to carry Agnir's implementation checklist. After locating this repository, an Agent reads `SKILL.md` and executes the procedure. After initialization, the target Project persists its own activation route and should not require the installation prompt again for normal work.

## Release scope

The `0.1.0` release includes:

- stable normative Core continuity semantics;
- normative discovery and failure semantics;
- `repository-filesystem/0.1` profile and manifest schema;
- root `SKILL.md` Agent Skill packaging with YAML frontmatter and complete operational procedure;
- one-line user-facing installation UX separated from the Agent-facing procedure;
- non-destructive existing-`AGENTS.md` merge semantics: preserve Project-owned instructions, add only the minimal Agnir locator, stay idempotent, and surface material conflicts instead of silently overwriting them;
- Agent-operable repository initialization with durable activation via `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml`;
- prompt-free fresh-Agent activation pressure proving that an initialized Project does not depend on the initialization conversation;
- self-hosting cold-start validation;
- executable pressure for all named discovery failure classes;
- durable non-repository SQLite continuity pressure;
- external-memory authorization pressure without plaintext credentials;
- multi-project isolation pressure;
- Locator Chain cycle, stale, and inconsistency pressure;
- symlink and real Git worktree boundary pressure;
- bilingual README architecture/Skill/activation/continuity documentation;
- main-only branch governance and immutable historical indexing.

## Known limitation

Real mount-boundary behavior remains explicitly unproven because the current conformance environment does not provide a real mount-capable test case. Ordinary directories are not accepted as substitute evidence. This limitation does not alter the published Core `0.1` semantics.

Execution surfaces differ in how they discover or install Agent Skills and whether they automatically inspect `AGENTS.md` or Project documentation. Agnir publishes a repository-root `SKILL.md` and persists the Project activation route; platform-specific Skill installation/discovery mechanics remain outside Agnir Core. A surface that ignores Project instruction files may require one-time configuration. Repeating Agnir's internal procedure in every user prompt is not the intended workflow.

## Publication gate

A publication commit is ready when all of the following hold:

1. `VERSION` is `0.1.0`;
2. `AGNIR.yaml`, schema, Core spec, discovery spec, profile, README files, Skill package, and conformance baseline agree on the Core/profile compatibility lines;
3. root `SKILL.md` has valid Agent Skill frontmatter and owns the detailed install / initialize / resume / checkpoint / repair procedure;
4. both READMEs expose the short user-facing install prompt, point Agents to `SKILL.md`, and do not duplicate the Agent installation checklist in Quick Start;
5. the Skill/profile contract preserves pre-existing target `AGENTS.md` instructions, keeps the Agnir addition locator-only and idempotent, and blocks on a material instruction conflict rather than deleting or overriding Project-owned rules;
6. root `AGENTS.md` points to the canonical README `Agnir Project Instructions` section, and that section contains the durable activation instructions required by the repository/filesystem profile;
7. Agent activation conformance proves Project root → `AGENTS.md` → README instruction → `AGNIR.yaml` → durable memory without relying on a repeated user bootstrap prompt;
8. executable merge pressure proves existing `AGENTS.md` content is preserved and an explicit contradictory instruction fails before merge;
9. active protocol/profile files contain no dependency on retired predecessor branch refs or predecessor bootstrap layouts;
10. the full self-hosting and executable conformance suite passes on the publication commit;
11. `main` is the only live branch and historical branch tips remain indexed under `history/`;
12. known limitations are stated without being represented as proven.

Tagging `v0.1.0` or creating a GitHub Release is a separate publication action.
