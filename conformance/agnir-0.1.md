# Agnir 0.1 Conformance

This conformance layer validates the stable Agnir Core `0.1` and `repository-filesystem/0.1` contracts without importing predecessor protocol requirements.

## Stable baseline

The executable suite covers:

- self-hosting `AGNIR.yaml` cold start;
- Core/profile version agreement and Project identity validation;
- required Current State / Next Actions resolution and optional Decisions / Evidence resolution;
- all named discovery failure classes: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`;
- selected-root isolation for nested Projects;
- durable non-repository SQLite continuity, checkpoint, and fresh-resolver resume;
- external-memory authorization semantics using authorization references rather than plaintext secrets;
- multi-project workspace isolation with locator-only registry metadata;
- substrate-neutral Locator Chain cycle, stale, and material inconsistency pressure;
- symlinked Project Entry Point behavior and rejection of implicit symlink escape;
- real Git worktree cold start;
- bilingual README/documentation structure and exhaustive repository-tree maintenance.

The reference models under `conformance/` are executable pressure tools, not promoted production implementations or mandatory backends.

## Known unproven boundary

A real mount-boundary case remains unproven because the current environment does not provide a real mount-capable fixture. An ordinary directory MUST NOT be represented as equivalent mount evidence.

## Release interpretation

Passing this suite establishes the reference repository's stable `0.1.0` conformance baseline for Core `0.1` and profile `repository-filesystem/0.1`. It does not imply that every possible backend, adapter, filesystem, authorization system, or execution environment has been tested.
