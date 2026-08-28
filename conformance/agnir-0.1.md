# Agnir 0.1 Conformance — executable development baseline

This main-line conformance layer validates Agnir Core `0.1`, the current `repository-filesystem/0.1` profile, storage-neutral continuity semantics, explicit discovery failures, authorization/isolation boundaries, and predecessor-migration pressure without relabeling predecessor evidence.

Current executable checks cover:

- self-hosting cold start from top-level `AGNIR.yaml`;
- Core/profile version and Project identity validation;
- Current State, Next Actions, Decisions, and Evidence resolution;
- all named discovery failure classes: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`;
- durable non-repository SQLite continuity with checkpoint + fresh-resolver resume;
- external-memory authorization using authorization references rather than plaintext credentials;
- multi-project workspace isolation with locator-only registry metadata;
- symlinked Project Entry Point behavior, rejection of implicit symlink escape, and real Git worktree cold start;
- exact PPMP v2 predecessor-format migration fixture derived from canonical `legacy/ppmp-v2.0.0`, including preservation of material state / next actions / decisions / checkpoint evidence and fresh target Agnir cold start;
- explicit rejection of v1/RPM predecessor serialization as PPMP v2.

The exact PPMP v2 migration fixture is reproducible conformance evidence, not a claim that a second independently hosted historical PPMP v2 Project exists. Real non-fixture migration pressure is separately supplied by the Svif/ZeroLocal predecessor audit.

A real mount-boundary case remains intentionally unproven until a mount-capable environment is available. Final release work is now primarily compatibility/version notation and release-boundary documentation rather than basic discovery/conformance coverage.
