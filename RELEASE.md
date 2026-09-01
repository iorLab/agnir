# Agnir 0.1.1 Release

**Repository version:** `0.1.1`

**Core compatibility line:** `0.1`

**Repository/filesystem profile:** `repository-filesystem/0.1`

## Status

The current `main` is the Agnir `0.1.1` publication-candidate line. The previously published stable release remains immutable `v0.1.0` until an exact `0.1.1` publication candidate passes the full conformance workflow and is separately tagged/released as `v0.1.1`.

Agnir `0.1.1` is a non-breaking operational patch. It does not change Agnir Core `0.1`, `repository-filesystem/0.1`, Project identity semantics, memory locators, checkpoint semantics, or discovery failure classes.

## Version model

Agnir separates three version layers:

- `agnir.version: "0.1"` identifies the Core compatibility line in a Discovery Record.
- `repository-filesystem/0.1` identifies the compatibility line of the repository/filesystem discovery profile.
- `VERSION` records the SemVer release of this reference specification/conformance/Skill repository.

Breaking Core semantics require a new Core compatibility line. Breaking repository/filesystem profile semantics require a new profile compatibility line. Patch releases may clarify text, strengthen non-breaking conformance, or fix reference/Skill/integration tooling without changing those compatibility identifiers.

## Patch purpose: execution-surface activation handoff

A real ChatGPT web Project initialization of `mattamior/skills-hub` exposed an operational completion bug. The target repository had a valid Project-owned route — `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → durable memory — but the surrounding ChatGPT Project did not yet have the persistent locator needed for a genuinely fresh conversation to reach that repository. The initializer nevertheless reported fresh activation too broadly.

`0.1.1` repairs that boundary:

- repository activation and execution-surface activation are separate completion dimensions;
- when a surface automatically starts from the authorized Project root and reads Project instructions, no extra surface configuration is required;
- when persistent surface configuration is required, the Skill configures it when authorized/capable or emits a copy-ready locator-only handoff;
- pending or unverified required surface configuration blocks a claim that full fresh activation passed;
- execution-surface settings must preserve unrelated instructions and must not duplicate Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure;
- ChatGPT Project Instructions are the first concrete surface adapter for this operational rule, not an Agnir Core dependency;
- completion reports distinguish repository activation from execution-surface activation and prefer a genuinely fresh-context verification after configuration.

The real `skills-hub` regression case was then re-tested after the locator-only ChatGPT Project Instructions were configured. A genuinely new conversation, given only an ordinary Project request, immediately located `mattamior/skills-hub`, followed root `AGENTS.md`, and began loading `AGNIR.yaml` and the declared durable continuity. The Principal supplied screenshot evidence and explicitly reported the regression as passed. Durable Evidence is stored under `.agnir/evidence/2026-09-01-v0.1.1-execution-surface-validation.md`.

## Skill packaging boundary

Root `SKILL.md` is the canonical Agent-facing Agnir Skill entrypoint. It owns the detailed install / initialize / upgrade / resume / checkpoint / commit / push / repair procedure.

The README deliberately exposes only short user-facing intent, for example:

```text
Install and initialize Agnir for this Project: https://github.com/iorLab/agnir
```

An upgrade remains distinct from re-initialization. Compatible upgrades preserve Project identity, declared memory locators/content, unrelated README/`AGENTS.md` instructions, and unrelated extensions.

## Existing-Project upgrade boundary

For `repository-filesystem/0.1`, an operational upgrade is compatible only while Core remains `0.1` and the profile remains `repository-filesystem/0.1`. Therefore upgrading an existing compatible Project from repository release `0.1.0` to `0.1.1` is an operational patch upgrade, not a Core/profile migration.

A Project may record the applied operational package under optional `extensions.agnir/operations` provenance with distribution, repository release, source, and immutable applied revision. Projects created before this provenance existed remain valid and can be upgraded non-destructively.

`latest stable release` means an actually published stable tag/release. A moving `main` branch or untagged publication candidate is not stable and must not be silently selected as an upgrade target.

## Release scope

The `0.1.1` release includes the complete `0.1.0` compatibility surface plus the execution-surface activation repair:

- stable normative Core continuity semantics;
- checkpoint no-op, coherent authoritative transition, mixed-generation prevention, and stale-base `AGNIR_CHECKPOINT_CONFLICT` semantics;
- normative discovery and failure semantics;
- `repository-filesystem/0.1` profile and manifest schema;
- compatible existing-Project upgrade semantics and optional `agnir/operations` provenance;
- repository/VCS checkpoint-before-commit and commit-and-push verification semantics;
- root `SKILL.md` Agent Skill packaging with one-line user installation UX;
- non-destructive existing-`AGENTS.md` merge behavior;
- Project-owned activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory;
- execution-surface activation evaluation, copy-ready handoff, separate status reporting, and no premature full-activation claim;
- real ChatGPT Project fresh-context regression evidence;
- self-hosting cold-start validation and executable regression pressure;
- SQLite non-repository continuity, external-memory authorization, multi-project isolation, Locator Chain failures, symlink boundaries, and real Git worktree pressure;
- bilingual README architecture/activation/handoff documentation;
- main-only long-lived branch governance and immutable release targets.

## Known limitations

Real mount-boundary behavior remains explicitly unproven because the current conformance environment does not provide a genuine mount-capable test case. Ordinary directories are not accepted as substitute evidence.

Execution surfaces differ in how they expose persistent Project/workspace configuration. The reference Skill can define the required handoff semantics and generate a copy-ready locator, but whether a specific surface can be configured automatically depends on that surface's available tools and Principal authority. This remains an integration concern outside Agnir Core.

Repository hooks remain optional event-capture mechanisms; Agnir continuity does not depend on them.

## Publication gate

A `v0.1.1` publication commit is ready only when all of the following hold:

1. `VERSION` is `0.1.1` and the self-hosting checker expects repository release `0.1.1`;
2. `AGNIR.yaml`, schema, Core spec, discovery spec, profile, README files, Skill package, and conformance baseline still agree on Core `0.1` / `repository-filesystem/0.1`;
3. root `SKILL.md` retains valid Agent Skill frontmatter and the full operational procedure;
4. repository activation remains non-destructive and fresh-resumable from the Project root;
5. execution-surface activation is evaluated separately and required persistent configuration is either applied or explicitly reported pending;
6. the ChatGPT Project handoff remains locator-only, preserves unrelated surface instructions, and does not fork Project durable truth;
7. the real `mattamior/skills-hub` fresh-conversation regression gate is recorded as passed;
8. both READMEs preserve the short install/upgrade UX and synchronized execution-surface explanation;
9. Core checkpoint, stale-base conflict, repository commit/push, and compatible upgrade semantics remain unchanged;
10. existing `AGENTS.md` merge behavior remains preservation-first, idempotent, and conflict-blocking;
11. all named discovery/authorization/boundary pressure remains green;
12. active protocol/profile files contain no dependency on retired predecessor layouts or execution-surface-specific Project memory;
13. `main` remains the only intended long-lived authoritative branch;
14. known limitations remain stated without being represented as proven;
15. the full self-hosting and executable conformance workflow passes on the exact publication-candidate revision.

Only that exact verified revision may become the immutable `v0.1.1` tag/release target. Tagging `v0.1.1` and creating the GitHub Release are separate publication actions; they must not silently target a later moving `main` revision.
