# Agnir v1.0.0 Release Criteria

Status: **satisfied — v1.0.0 published stable**

Agnir `v1.0.0` means downstream Projects can adopt the Agnir public compatibility contract as durable infrastructure without expecting routine breaking redesign. It is a stability commitment, not a feature-count milestone.

## Required gates

### 1. Core semantics are complete enough for the intended product class

The Core must cover the recurring continuity problems Agnir intends to own, including Project identity, Current State, Next Actions, Decisions, Evidence / Checkpoints, discovery/resume, checkpoint/failure semantics, and continuity integration when parallel continuity is part of Core. No known essential continuity primitive may still require a foreseeable breaking redesign.

### 2. Core compatibility contract is explicit

The repository must document what a Core compatibility version means, what changes are backward-compatible, what requires a new compatibility line, how profiles/extensions declare compatibility, how consumers detect unsupported versions, and how deprecation works. `v1.0.0` must not rely on undocumented convention.

### 3. Migration is tested, not merely documented

Conformance must cover fresh Project → current Core, previous supported Core/profile → current release, previous incompatible Core line → explicit migration or rejection, idempotent re-application/upgrade, and preservation of Project-owned instructions and unrelated content. Migration must preserve continuity correctly or fail explicitly.

### 4. Multiple independent real Projects have used Agnir successfully

Minimum evidence before `v1.0.0`:

- at least 3 materially different real Projects;
- at least 2 materially different execution surfaces or adapters;
- at least 1 Project that crossed an Agnir upgrade boundary;
- if parallel continuity is in Core, at least 1 real Project exercising independent lineages plus reconciliation.

### 5. Backend/profile independence is demonstrated

Core claims must be supported by more than one storage/execution model where the abstraction requires it. If Continuity Lineage is in Core, VCS and non-VCS conformance are mandatory. No Core primitive may secretly depend on Git, GitHub, ChatGPT, a particular Agent, or one filesystem layout.

### 6. Conformance suite is normative and release-blocking

A release candidate must pass Core, repository/filesystem profile, migration/upgrade, failure-path, cold-start/fresh-resume, lineage, and Agnir self-hosting conformance. The release process must make these checks visible and reproducible.

### 7. Failure behavior is stable

Required failures must be machine-distinguishable where interoperability depends on them. Specifications must define triggering condition, required observable behavior, recoverability, and safe retry expectations. Unknown or ambiguous state must not be treated as success.

### 8. Publication/checkpoint integrity has no known correctness hole

Agnir must have no known path that can publish Project state and continuity state that knowingly disagree. For repository/filesystem/VCS profiles this includes stale-base rejection, crash/retry/idempotence, and coherent target-publication boundaries where applicable.

### 9. Documentation is sufficient for an independent implementation

An implementer who did not design Agnir must be able to build a conforming implementation from published specification/conformance material without private chat history. Public material must be sufficient for Core/profile behavior, lifecycle/state transitions, discovery/activation, checkpoint/reconciliation, compatibility/versioning, migration, repository map, and examples.

This gate is **satisfied** by independent challenge issue #26 against exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`, with final verdict `PASS`, no concurrent documentation/conformance/implementation failure class, and preserved Phase A/Phase B freeze receipts.

### 10. Release operations are repeatable

The project must have a documented, tested release procedure covering release-candidate creation, conformance, version updates, exact source revision, tag/release creation, artifact/distribution verification, and rollback/superseding-release behavior. Every stable release must identify its exact source revision.

## v1.0.0 evidence threshold

| Area | Gate |
| --- | --- |
| Core compatibility | No unresolved planned breaking Core redesign |
| Real Projects | >= 3 materially different Projects |
| Execution surfaces/adapters | >= 2 materially different surfaces |
| Upgrade evidence | >= 1 real upgrade boundary crossed successfully |
| Parallel continuity, if Core | VCS + non-VCS conformance and >= 1 real Project |
| Independent implementation | One clean fresh independent `PASS` |
| Release candidates | >= 1 explicit `1.0.0-rc` cycle with no release-blocking Core defect |
| Conformance | All normative suites green from a fresh environment |
| Documentation | Independent-implementation quality |

## Final v1.0.0 evidence snapshot — 2026-09-06

| Gate | Final status | Evidence |
| --- | --- | --- |
| 1. Core semantics | **Satisfied** | Core `1.0` stabilizes the accepted Core `0.2` durable continuity semantics without behavioral redesign. |
| 2. Compatibility contract | **Satisfied** | Core/profile `0.1`, `0.2`, and `1.0`, migration/promotion contracts, failure mapping, and versioning discipline are public and conformance-tested. |
| 3. Migration testing | **Satisfied** | Fresh install, `0.1`→`0.2`, `0.2`→`1.0`, composed migration/promotion, idempotence/conflict/stale handling, and real Project evidence are accepted. |
| 4. Real Projects and execution surfaces | **Satisfied** | Svif + FishUp + VocaPort satisfy the 3-Project threshold; materially different execution surfaces satisfy the 2-surface threshold. |
| 5. Backend/profile independence | **Satisfied** | VCS and non-VCS lineage conformance plus genuine Docker bind-mount evidence are accepted. |
| 6. Normative conformance | **Satisfied** | Core/profile 1.0, historical regressions, promotion, migration, self-host, stable package gates, and full suite passed the accepted RC and stable publication cycles. |
| 7. Failure behavior | **Satisfied** | Required discovery/checkpoint/lineage/migration failures are machine-distinguishable in published contract/conformance. |
| 8. Publication/checkpoint integrity | **Satisfied** | Staged reconciliation, stale checks, coherent target publication, exact-main validation, immutable tag verification, and fresh idempotent publication verification all passed. |
| 9. Independent-implementation documentation | **Satisfied** | Issue #26 clean independent `PASS`; exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`; artifact SHA-256 `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`; matrix/test/semantic/edge receipts 81/81, 10/10, 19/19, 10/10. |
| 10. Repeatable release operations | **Satisfied** | `v1.0.0-rc.1` and `v1.0.0` both completed exact-source publication cycles with fresh immutable-source reruns and idempotent verification. |

### Final release receipts

- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- accepted RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC Release id `383536840`;
- RC workflow `34026167762`, attempts 1 and 2: success;
- stable tag: `v1.0.0` -> `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable Release id `383612171`;
- stable workflow `34039014354`, attempt 1 and fresh immutable-source attempt 2: success;
- `releases/latest == v1.0.0`;
- issue #29 closed completed.

### Threshold summary

- **Real Projects:** satisfied.
- **Execution surfaces/adapters:** satisfied.
- **Upgrade evidence:** satisfied by Svif and migration/promotion conformance.
- **Parallel continuity real Project:** satisfied by Svif; VCS and non-VCS conformance are green.
- **Mount-boundary evidence:** satisfied by accepted Docker bind-mount validation.
- **Independent implementation:** satisfied by issue #26 clean `PASS`.
- **Core/profile 1.0 promotion:** satisfied.
- **`1.0.0-rc` cycle:** satisfied by immutable `v1.0.0-rc.1` plus fresh rerun.
- **Stable publication:** satisfied by immutable `v1.0.0` plus fresh rerun.

Canonical receipt detail for independent acceptance: `.agnir/evidence/2026-09-06-independent-implementation-challenge-acceptance.md`.
Canonical receipt detail for stable publication: `.agnir/evidence/v1.0.0-stable-publication-acceptance.md`.

## Non-gates

The following alone do not justify `v1.0.0`: feature count, commit count, broad platform support, repository age, README polish, one self-hosting repository, or one Git integration test. Conversely, Agnir does not need every conceivable backend/platform/mount substrate before `v1.0.0`; it needs a stable, interoperable, migratable, independently implementable public contract plus enough real evidence to make that commitment credible.
