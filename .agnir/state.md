# Agnir Current State

Agnir is the active project/protocol identity on `main`. PPMP v2.0.0 / Persistent Project Memory / Sandminni remains predecessor history on `legacy/ppmp-v2.0.0`.

## Release state

- Core compatibility line: **Agnir Core `0.1`**.
- Repository release line: **`0.1.0-rc.1`**.
- Current repository/filesystem profile: **`repository-filesystem/0.1`**.
- Core `0.1` compatibility semantics are frozen for RC.
- `main` is a **release-candidate line**, not a published stable GitHub Release/tag.
- The intended first stable repository release for this Core line is `0.1.0`.

Compatibility rules:

- Discovery Records serialize Core compatibility as `agnir.version: "0.1"`;
- consumers bind to the Core line, not to a particular repository patch/RC;
- `0.1.x` repository releases may clarify/fix/strengthen conformance but MUST NOT redefine existing Core `0.1` semantics;
- a breaking semantic change requires a new line such as Core `0.2` / repository `0.2.0`.

The compatibility freeze is durably recorded in `.agnir/decisions.md` and `.agnir/evidence/2026-08-28-core-0.1-rc1-freeze.md`.

## Core invariants

- Durable continuity belongs to the Project, not an Executor, execution environment, VCS, repository host, or conversation.
- A fresh Executor given only an authorized Project Entry Point must resolve the Discovery Record and required durable state without predecessor-private context.
- Required durable memory semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agnir Core is storage-, platform-, VCS-, repository-, agent-, and execution-surface-neutral.
- All named Core discovery failure classes have executable conformance pressure: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Svif consumes Agnir through the Core `"0.1"` compatibility line. It must not bind to the Agnir repository RC/patch number, repository layout, backend, or adapter when another implementation satisfies the same Core semantics.

## Conformance baseline

The active suite covers:

- self-hosting `repository-filesystem/0.1` cold start;
- all explicit discovery failure classes;
- durable non-repository SQLite continuity with checkpoint + fresh-resolver resume;
- external-memory authorization without plaintext credentials;
- multi-project workspace isolation with locator-only registry metadata;
- generic Locator Chain `CYCLE`, `STALE`, and material `INCONSISTENT` semantics;
- symlinked Project Entry Point behavior, rejection of implicit symlink escape, and real Git worktree cold start;
- exact PPMP v2 -> Agnir migration conformance.

The exact PPMP fixture is aligned with canonical `legacy/ppmp-v2.0.0` at boundary commit `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`. It preserves material state, next actions, decisions, and checkpoint evidence, materializes a target Agnir Project, and cold-starts that target through the current resolver. A v1/RPM manifest is explicitly rejected rather than silently promoted to PPMP v2.

Migration fixture baseline passed run `33150059494`, job `98779726021`.

The frozen RC checker head `967292d95ba2ed7f3c5315d0f9e0540e0e84c263` passed full Agnir conformance run `33150494178`.

## Predecessor migration evidence

A real non-fixture predecessor audit is complete using `iorLab/svif@legacy/zerolocal-v0.1` at commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`.

That Project is genuine predecessor evidence but uses earlier v1/RPM-era `.chatgpt/project-memory.yaml`, not PPMP v2. The audit compares material durable knowledge rather than only locator/file presence and found one real regression: the durable `installable-plugin` product target had been lost during the Svif rewrite. Svif repaired that regression.

Evidence classification:

- real non-fixture predecessor migration: **PASS, v1/RPM-era**;
- exact PPMP v2 historical source: **available on canonical legacy branch, not an external independent Project**;
- exact PPMP v2 executable migration fixture: **PASS**;
- target Agnir Core `0.1` RC conformance: **PASS**.

A second independently hosted historical PPMP v2 Project is not a Core `0.1` release prerequisite. Reproducible exact PPMP v2 conformance plus real non-fixture predecessor migration pressure is the release requirement.

## Repository documentation

`README.md` and `README.zh-CN.md` are parallel entry points with synchronized Architecture and Continuity Flow diagrams. They state the RC versioning model and exact PPMP v2 migration coverage.

README repository trees are compact navigation. `REPOSITORY_TREE.md` is the exhaustive tracked-file map and must be updated with repository structure/responsibility changes.

## Remaining stable-release boundary

The technical Core `0.1` RC freeze and migration/conformance prerequisites are complete. Remaining work before a stable `0.1.0` publication is deliberately narrow:

1. perform a final release-boundary review for contradictory/stale normative or user-facing wording and release metadata;
2. verify the latest final release-candidate head after any such cleanup;
3. preserve the real mount-boundary case as explicitly **unproven** until an appropriate environment exists; no fake substitute is accepted and its absence alone does not invalidate the current RC baseline;
4. create a public GitHub tag/Release only if explicitly authorized.

No public Agnir `0.1.0` release/tag currently exists as a result of this work.

## Branch governance

- `main`: authoritative Agnir Core `0.1` RC line;
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary;
- incidental branch cleanup remains deferred until the new version is substantially complete.
