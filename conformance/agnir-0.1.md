# Agnir 0.1 Conformance

This conformance layer validates stable Agnir Core `0.1`, `repository-filesystem/0.1`, and the repository's Agnir Agent Skill packaging without importing predecessor protocol requirements.

## Stable baseline

The executable suite covers:

- root `SKILL.md` Agent Skill frontmatter and the presence of the complete Agent-facing install / initialize / resume / checkpoint / commit / push / repair procedure;
- separation of the one-line user-facing install request from the detailed Agent-facing procedure;
- bilingual README Quick Starts pointing Agents to `SKILL.md` without embedding the internal installation checklist;
- non-destructive merge of the minimal Agnir locator into an existing `AGENTS.md` while preserving existing Project instructions;
- minimal `AGENTS.md` creation when absent, idempotent handling of an equivalent locator, and explicit conflict failure instead of silent overwrite when existing instructions contradict durable Agnir activation;
- self-hosting Agent activation from Project root through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml`;
- prompt-free fresh-Agent activation for an initialized Agent-operable repository Project;
- failure when the Agent activation locator is missing, does not reference the canonical README instruction, or forks an incomplete/duplicated activation contract;
- self-hosting `AGNIR.yaml` cold start;
- Core/profile version agreement and Project identity validation;
- required Current State / Next Actions resolution and optional Decisions / Evidence resolution;
- checkpoint no-op evaluation without synthetic durable mutation;
- coherent checkpoint publication as one authoritative generation and rejection of stale-base publication through `AGNIR_CHECKPOINT_CONFLICT` semantics;
- repository-context commit intent (`commit`, `提交`, `提交代码`) as checkpoint-before-commit and commit-and-push intent (`提交推送`) as checkpoint + commit + push + verification guidance;
- observed commits triggering evaluation rather than unconditional Agnir mutation;
- all named discovery failure classes: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`;
- selected-root isolation for nested Projects;
- durable non-repository SQLite continuity, checkpoint, and fresh-resolver resume;
- external-memory authorization semantics using authorization references rather than plaintext secrets;
- multi-project workspace isolation with locator-only registry metadata;
- substrate-neutral Locator Chain cycle, stale, and material inconsistency pressure;
- symlinked Project Entry Point behavior and rejection of implicit symlink escape;
- real Git worktree cold start;
- bilingual README/documentation structure and exhaustive repository-tree maintenance.

`SKILL.md` is an Agent-facing distribution/operation surface, not an Agnir Core requirement that every Executor use an Agent Skill mechanism. Repository commit/push wording and hooks are integration semantics rather than Core keywords or VCS dependencies. The `AGENTS.md` merge reference is conformance-only pressure for the repository/filesystem Agent-operable initialization contract, not a production installer. The Agent activation fixture is a repository/filesystem profile pressure case, not a Core requirement that every Executor be an AI Agent or that every backend use `AGENTS.md` / `README.md`.

The reference models under `conformance/` are executable pressure tools, not promoted production implementations or mandatory backends.

## Known unproven boundary

A real mount-boundary case remains unproven because the current environment does not provide a real mount-capable fixture. An ordinary directory MUST NOT be represented as equivalent mount evidence.

## Release interpretation

Passing this suite establishes the reference repository's stable `0.1.0` conformance baseline for Core `0.1`, profile `repository-filesystem/0.1`, and the published Agent Skill packaging boundary. For checkpoint semantics it additionally proves no-op behavior, coherent single-generation publication, and stale-base conflict rejection in a substrate-neutral reference model. For an Agent-operable repository initialized under the reference convention, it additionally proves that existing root Agent instructions are preserved during Agnir locator installation, explicit contradictory instructions are surfaced rather than overwritten, the activation route itself is durable, future Agents do not require the original initialization prompt or conversation, and repository-context commit/push intent remains a durable checkpoint boundary.

It does not imply that every possible backend, adapter, filesystem, authorization system, Agent Skill installer, VCS, repository hook, Agent instruction mechanism, semantic conflict form, or execution environment has been tested.
