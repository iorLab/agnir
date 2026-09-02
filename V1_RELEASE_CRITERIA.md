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
