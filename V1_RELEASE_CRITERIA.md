# Agnir v1.0.0 Release Criteria

Status: draft release gate

Agnir `v1.0.0` should mean that downstream Projects can adopt the Agnir Core contract as durable infrastructure without expecting routine breaking redesign. It is a stability commitment, not a feature-count milestone.

## Required gates

### 1. Core semantics are complete enough for the intended product class

The Core must cover the recurring continuity problems Agnir intends to own, including at minimum:

- Project identity
- Current State
- Next Actions
- Decisions
- Evidence / Checkpoints
- discovery / resume semantics
- checkpoint semantics
- failure semantics
- continuity integration semantics if parallel continuity is part of Core

No known essential continuity primitive may still require a foreseeable breaking redesign of the Core model.

### 2. Core compatibility contract is explicit

The repository must document:

- what a Core compatibility version means
- what changes are backward-compatible
- what requires a new Core compatibility line
- how profiles/extensions declare compatibility
- how consumers detect unsupported versions
- how deprecation works

`v1.0.0` must not be published while compatibility behavior still depends on undocumented convention.

### 3. Migration is tested, not merely documented

At least these paths must have conformance coverage:

- fresh Project -> current Core
- previous supported Core/profile -> current compatible release
- previous incompatible Core line -> explicit migration or explicit rejection
- idempotent re-application / upgrade
- preservation of pre-existing Project-owned instructions and unrelated Project content

A migration must either preserve continuity correctly or fail explicitly; silent reinterpretation is unacceptable.

### 4. Multiple independent real Projects have used Agnir successfully

Before `v1.0.0`, Agnir should have production-like evidence from more than its own repository and synthetic fixtures.

Minimum evidence gate:

- at least 3 materially different real Projects
- at least 2 materially different execution surfaces or adapters
- at least 1 Project that has crossed an Agnir upgrade boundary
- if parallel continuity is in Core, at least 1 real Project that has exercised independent lineages plus reconciliation

These are release gates for confidence, not Core concepts.

### 5. Backend/profile independence is demonstrated

Core claims must be supported by more than one storage/execution model where the abstraction requires it.

If Core includes Continuity Lineage, VCS and non-VCS conformance are mandatory before `v1.0.0`.

No Core primitive may secretly depend on Git, GitHub, ChatGPT, a particular Agent, or a particular filesystem layout.

### 6. Conformance suite is normative and release-blocking

A release candidate must pass:

- Core conformance
- repository/filesystem profile conformance
- migration/upgrade conformance
- failure-path conformance
- cold-start / fresh-resume conformance
- lineage conformance if applicable
- self-hosting conformance for `iorLab/agnir`

The release process must make these checks visible and reproducible.

### 7. Failure behavior is stable

Required failures must be machine-distinguishable where interoperability depends on them.

For each normative failure class, the specification must define:

- triggering condition
- required observable behavior
- whether recovery is possible
- whether retry is safe

Unknown or ambiguous state must not be silently treated as success.

### 8. Publication/checkpoint integrity has no known correctness hole

Agnir must have no known path that can publish a Project state and continuity state that knowingly disagree.

For repository/filesystem/VCS profiles this includes crash/retry/idempotence and target-publication boundaries where applicable.

### 9. Documentation is sufficient for an independent implementation

An implementer who did not design Agnir must be able to build a conforming implementation from the published specification and conformance suite without relying on private chat history.

Required documentation includes:

- Core specification
- profile specifications
- lifecycle / state transition semantics
- discovery and activation
- checkpoint and reconciliation rules
- compatibility/versioning policy
- migration guidance
- repository map / examples

### 10. Release operations are repeatable

The project must have a documented, tested release procedure covering:

- release candidate creation
- conformance run
- version updates
- exact source revision
- tag creation
- release notes
- artifact/distribution verification
- rollback or superseding-release procedure

Agnir must be able to identify the exact source revision corresponding to every stable release.

## v1.0.0 evidence threshold

| Area | Gate |
| --- | --- |
| Core compatibility | No unresolved planned breaking Core redesign |
| Real Projects | >= 3 materially different Projects |
| Execution surfaces/adapters | >= 2 materially different surfaces |
| Upgrade evidence | >= 1 real upgrade boundary crossed successfully |
| Parallel continuity, if Core | VCS + non-VCS conformance and >= 1 real Project |
| Release candidates | >= 1 explicit `1.0.0-rc` cycle with no release-blocking Core defect |
| Conformance | All normative suites green from a fresh environment |
| Documentation | Independent-implementation quality |

## Current evidence snapshot — 2026-09-03

This section is a non-normative readiness snapshot. It does not weaken the gates above. A status may move backward if new evidence exposes a defect.

| Gate | Current status | Evidence / remaining work |
| --- | --- | --- |
| 1. Core semantics | **Provisionally satisfied** | Core `0.2` covers Project identity, durable semantic categories, discovery/resume, checkpoint/failure semantics and Continuity Lineage integration. No planned breaking Core redesign is currently recorded; reopen if real downstream evidence exposes one. |
| 2. Compatibility contract | **Satisfied for current published lines** | Core/profile `0.1` and `0.2`, migration semantics, unsupported-version behavior and operational-vs-compatibility versioning are explicit. Future compatibility lines must preserve this discipline. |
| 3. Migration testing | **Satisfied for current published lines** | Fresh Core `0.2` install, Core/profile `0.1` -> `0.2` semantic/concrete migration, idempotence/conflict behavior, stable `0.1` regressions, authoritative Svif published `v0.1.1` -> `v0.2.0` migration, and FishUp's real 0.1 -> 0.2 migration-line validation through the immutable published reference implementation are green. FishUp additionally proved byte-exact State/Next/Decisions/AGENTS/README preservation and product build success. |
| 4. Real Projects | **Partial** | Svif provides authoritative downstream Core/profile `0.2` adoption and upgrade/reconciliation evidence. FishUp is a second materially different external Project with verified published `v0.2.0` migration-line behavior; its authoritative main remains intentionally on `0.1` because every main push has production Cloudflare/D1 side effects outside the validation authorization. At least **1 additional materially different real Project** is still desired under this readiness map, with VocaPort the preferred fresh-install candidate. A clearly distinct second execution surface/adapter is also still required. |
| 5. Backend/profile independence | **Partial / strong conformance evidence** | VCS and non-VCS lineage conformance are green, and Core is not defined by a VCS selector. Genuine mount-boundary behavior remains explicitly unproven and should be pressured in a real mount-capable environment. |
| 6. Normative conformance | **Infrastructure satisfied; v1 final run future** | The release-blocking suite is visible and reproducible and passed stable `v0.2.0` plus subsequent main checkpoints. A fresh exact `1.0.0-rc` candidate must rerun every normative layer. |
| 7. Failure behavior | **Provisionally satisfied** | Normative discovery/checkpoint/lineage/migration failures are machine-distinguishable in specs and conformance. FishUp independently re-exercised the required unauthorized-migration rejection using the published reference implementation. Keep open to correction if independent consumers expose ambiguous recovery/retry semantics. |
| 8. Publication/checkpoint integrity | **Provisionally satisfied** | Agnir stable-to-main and Svif published-to-published migration used staged target reconciliation, exact-tree CI, stale checks, one coherent target advancement and fresh verification. FishUp additionally demonstrated a correctly bounded validation path that did not confuse a validated migration branch with authoritative target publication when target push would have extra production side effects. Broader crash/mount evidence remains useful. |
| 9. Independent-implementation documentation | **Open** | Specs, profiles, migration docs, activation guidance and repository map exist, but independent-implementation quality has not yet been proven by an implementation/review from someone not relying on design chat history. |
| 10. Repeatable release operations | **Satisfied for 0.2; v1 cycle future** | `v0.2.0-rc.1` -> `v0.2.0` exercised exact candidate verification, immutable tags/releases, package provenance and safe main reconciliation. A separate `1.0.0-rc` cycle remains a v1 threshold. |

### Threshold summary

- **Upgrade evidence:** satisfied by real Svif authoritative published `v0.1.1` -> published `v0.2.0` migration.
- **Parallel continuity real Project:** satisfied by Svif; VCS and non-VCS conformance are also green.
- **Real Projects:** partial with two external real Projects carrying direct Core/profile `0.2` evidence — Svif authoritative adoption and FishUp validated migration line. At least one additional materially different Project is still desired; FishUp main publication remains a separate production-affecting action.
- **Execution surfaces/adapters:** open until a second materially distinct surface/adapter has fresh activation/resume evidence.
- **Mount-boundary evidence:** open and explicitly unproven.
- **Independent implementation:** open.
- **`1.0.0-rc` cycle:** future gate.

Canonical downstream receipt detail:

- Svif authoritative published migration: `.agnir/evidence/2026-09-03-svif-published-v0.1.1-to-v0.2.0-upgrade.md`;
- FishUp real migration-line validation: `.agnir/evidence/2026-09-03-fishup-v0.2.0-migration-validation.md`.

## Non-gates

The following alone do **not** justify `v1.0.0`:

- a large number of features
- a large number of commits
- broad platform support
- repository age
- README polish
- one successful self-hosting repository
- one successful Git integration test

Conversely, Agnir does not need every conceivable backend, platform, or convenience feature before `v1.0.0`. The release should happen once the Core contract is stable, interoperable, migratable, independently implementable, and supported by enough real evidence to make that stability commitment credible.
