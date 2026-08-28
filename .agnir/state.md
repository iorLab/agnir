# Agnir Current State

Agnir is the active project/protocol identity on `main`. PPMP v2.0.0 / Persistent Project Memory / Sandminni remains predecessor history on `legacy/ppmp-v2.0.0`.

## Release state

- Core compatibility line: **Agnir Core `0.1`**.
- Repository release line: **`0.1.0-rc.1`**.
- Current repository/filesystem profile: **`repository-filesystem/0.1`**.
- `main` is now a **release-candidate line**, not yet a published stable GitHub Release/tag.
- The first stable repository release for this Core line is intended to be `0.1.0` after RC verification and final release-boundary review.

Compatibility semantics are frozen for the RC:

- Discovery Records serialize Core compatibility as `agnir.version: "0.1"`;
- consumers bind to the Core line, not to a specific repository patch release;
- `0.1.x` repository releases may clarify/fix/strengthen conformance but MUST NOT redefine existing Core `0.1` semantics;
- a breaking Core semantic change requires a new line such as Core `0.2` / repository `0.2.0`.

## Core invariants

- Durable continuity belongs to the Project, not an Executor, execution environment, VCS, repository host, or conversation.
- A fresh Executor given only an authorized Project Entry Point must be able to resolve the Discovery Record and required durable state without predecessor-private context.
- Required durable memory semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Agnir Core is storage-, platform-, VCS-, repository-, agent-, and execution-surface-neutral.
- All named Core discovery failure classes have executable conformance pressure: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`.

## Relationship to Svif

Svif is a separate **Project orchestration product** at `iorLab/svif`. Svif consumes the Agnir Core `0.1` compatibility line through a Continuity Provider adapter; it must not depend on the Agnir repository layout or a particular backend/adapter when another implementation satisfies the same Core semantics.

## Conformance baseline

The active suite now covers:

- self-hosting `repository-filesystem/0.1` cold start;
- all explicit discovery failure classes;
- durable non-repository SQLite continuity with checkpoint + fresh-resolver resume;
- external-memory authorization without plaintext credentials;
- multi-project workspace isolation with locator-only registry metadata;
- generic Locator Chain `CYCLE`, `STALE`, and material `INCONSISTENT` semantics;
- symlinked Project Entry Point behavior, rejection of implicit symlink escape, and real Git worktree cold start;
- **exact PPMP v2 -> Agnir migration conformance**.

The exact PPMP fixture is aligned with the canonical predecessor manifest from `legacy/ppmp-v2.0.0` at boundary commit `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`. It preserves material state, next actions, decisions, and checkpoint evidence, materializes a target Agnir Project, and cold-starts that target through the current `repository-filesystem/0.1` resolver. A v1/RPM manifest is explicitly rejected rather than silently promoted to PPMP v2.

The first full conformance run including this fixture passed in run `33150059494` (job `98779726021`).

## Predecessor migration evidence

A real non-fixture predecessor audit is complete using `iorLab/svif@legacy/zerolocal-v0.1` at commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`.

That Project is genuine predecessor evidence but uses an earlier v1/RPM-era `.chatgpt/project-memory.yaml`, not PPMP v2. The audit compares material durable knowledge rather than only file/locator presence and found one real regression: the durable `installable-plugin` product target had been lost during the Svif rewrite. Svif repaired that regression.

Evidence classification is explicit:

- real external predecessor migration: **PASS, v1/RPM-era**;
- exact PPMP v2 historical source: **available on canonical legacy branch, not external**;
- exact PPMP v2 executable migration fixture: **PASS**;
- target Agnir Core `0.1` conformance baseline: **PASS on RC line**.

A second independently hosted historical PPMP v2 Project is **not** a Core `0.1` release prerequisite. Historical availability is accidental; reproducible exact PPMP v2 conformance plus real non-fixture predecessor migration pressure is the release requirement.

Durable evidence:

- `.agnir/evidence/2026-08-28-real-predecessor-migration-and-ppmp-boundary.md`;
- Svif counterpart: `.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md` in `iorLab/svif`.

## Repository documentation

`README.md` and `README.zh-CN.md` are parallel entry points with synchronized architecture and continuity diagrams. The README repository tree is compact navigation; `REPOSITORY_TREE.md` is the exhaustive tracked-file map and must move with repository structure changes.

The READMEs now state the RC versioning model and exact PPMP v2 migration coverage.

## Remaining release boundary

1. Record the Core `0.1` compatibility/release freeze in durable decisions and a final RC evidence record.
2. Run final RC verification on the latest canonical head after that synchronization.
3. Review normative/user-facing prose for stale `development` wording or contradictions with the frozen RC compatibility model.
4. Keep the real mount-boundary case explicitly **unproven** until a mount-capable environment is available; it does not block RC solely because no fake substitute is accepted.
5. Do not create a public GitHub Release/tag until explicitly authorized.

## Branch governance

- `main`: authoritative Agnir Core `0.1` RC line;
- `legacy/ppmp-v2.0.0`: authoritative predecessor boundary;
- incidental branch cleanup remains deferred until the new version is substantially complete.
