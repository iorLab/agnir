# Agnir Core 0.2 — Release Candidate Normative Specification

**Status:** Normative compatibility candidate for repository `v0.2.0-rc.1`. This is the Core `0.2` contract under release-candidate verification; final stable publication remains gated by the RC install/migration/resume evidence.

## 1. Purpose

Agnir is a project-owned durable continuity protocol. Core `0.2` extends the single-line continuity model of Core `0.1` so one Project may own multiple independently advancing **Continuity Lineages** while preserving one Project identity.

The stable ownership rule remains:

> The Project persists; Executors and execution environments may change.

Agnir Core MUST NOT require Git, GitHub, VCS branches, repositories, filesystems, ChatGPT, an AI agent, a conversational interface, or any single storage layout.

## 2. Compatibility

Core `0.2` is a new compatibility line because lineage-aware discovery and publication add required semantics that a Core `0.1` implementation is not required to understand.

A conforming implementation MUST NOT silently interpret a Core `0.2` Discovery Record as Core `0.1`.

Repository release versions and Core compatibility lines remain separate. A repository release such as `v0.2.0` MAY publish Core `0.2` while profiles retain independent compatibility identifiers.

## 3. Core concepts

Core `0.2` retains the Core `0.1` concepts of Project, Principal, Executor, Project Entry Point, Discovery Record, Locator Chain, Current State, Next Actions, Decisions, Evidence / Checkpoints, and authoritative checkpoint transition.

### Continuity Lineage

A **Continuity Lineage** is an independently advancing continuity line owned by one Project.

Each active lineage MUST make its own Current State and Next Actions durably recoverable. Decisions and Evidence remain optional only when no material content in those categories is required for safe continuation.

A lineage is not a Project. Creating, selecting, advancing, integrating, renaming/rebinding at a backend layer, or retiring a lineage MUST NOT implicitly create a new Project identity.

### Lineage identity

A lineage identity MUST be non-empty and durable within the Project scope in which the active backend/profile resolves it. Global uniqueness is not required by Core.

Lineage identity MUST NOT be defined by a backend revision receipt. A Git commit SHA, database transaction number, snapshot version, object generation, or equivalent receipt MAY identify a checkpoint but MUST NOT itself be the lineage identity unless an adapter has separately established that value as a durable logical lineage identity independent of revision changes.

A backend locator or selector is also not automatically lineage identity. A branch name, worktree path, workspace handle, database namespace selector, UI tab, or equivalent MAY be used by a profile/adapter to **select or bind to** a lineage. The backend MAY choose a selector whose value happens to equal the logical lineage identity, but Core does not require this and implementations MUST NOT infer identity equivalence merely from matching strings.

Changing a backend selector, locator, or revision receipt MUST NOT by itself be treated as creating a new Project. If a profile supports renaming/rebinding a selector while preserving one logical lineage, that operation MUST preserve the lineage identity or perform an explicit lineage-identity migration; it MUST NOT silently mint or switch identity merely because a locator changed.

Core does not mandate a string format, URI scheme, YAML key name, database column, UUID scheme, or physical encoding for lineage identity.

## 4. Required durable memory semantics

For the selected lineage, a conforming Project MUST make the following semantics durably recoverable:

- **Current State** — present truth required to continue that lineage safely;
- **Next Actions** — outstanding actionable work, blockers, priorities, and intentionally deferred work for that lineage;
- **Decisions** — accepted durable decisions and material rationale relevant to that lineage or Project;
- **Evidence / Checkpoints** — concise evidence required for recovery, audit, reconciliation, or support of material claims.

Project-wide facts MAY be shared physically across lineages, but an implementation MUST preserve the observable semantics of lineage-local continuity and MUST NOT make a checkpoint on one lineage silently change another lineage's authoritative continuity.

## 5. Lineage selection

A Core `0.2` operation that reads or mutates lineage-local continuity MUST resolve exactly one selected lineage unless the operation explicitly names multiple lineages as integration inputs.

Selection input MAY be either a logical lineage identity or a backend/profile selector that deterministically resolves to one logical lineage identity. Selection context MAY come from:

1. explicit Principal/task/adapter input;
2. an already selected execution/profile/backend context;
3. an explicitly declared default lineage or default selector.

Profiles and adapters MAY define a stricter precedence order. They MUST NOT require heuristic scanning of sibling lineages to guess which lineage the Principal intended.

If a lineage-local operation requires a lineage and no identity/selector can be selected deterministically, the implementation MUST fail with semantics equivalent to `AGNIR_LINEAGE_REQUIRED`.

If a selected identity or selector is known but does not resolve to one valid lineage, the implementation MUST fail with semantics equivalent to `AGNIR_LINEAGE_NOT_FOUND` rather than silently selecting another lineage. Profiles MAY expose a more specific binding/selector failure in addition to the Core semantic class.

Selection is not enumeration. Core does not require an implementation to list all sibling lineages before resolving one selected lineage.

## 6. Discovery Record semantics

After any profile/backend selector has been resolved, a Core `0.2` Discovery Record MUST provide semantics equivalent to:

```yaml
agnir:
  version: "0.2"
project:
  identity: <durable-project-identity>
continuity:
  lineage: <selected-durable-logical-lineage-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

The representation is semantic, not serialization-specific. A backend MAY resolve the selector before materializing a Discovery Record, provided a fresh compatible Executor can determine which logical lineage was selected and load the corresponding continuity without private predecessor context.

A profile MAY retain selector/binding metadata outside the Core semantic record when needed to resolve backend context to the logical lineage identity.

Core does not require a Discovery Record to enumerate sibling lineages.

## 7. Cold-start discovery invariant

A compatible fresh Executor given only an authorized Project Entry Point, the required lineage-selection context, and the applicable profile/adapter implementation MUST be able to:

1. resolve the Core `0.2` Discovery Record;
2. validate Core compatibility;
3. verify Project identity sufficiently to detect accidental cross-Project resolution;
4. resolve exactly one selected lineage for ordinary lineage-local work;
5. resolve any backend selector/binding to the logical lineage identity and verify that identity;
6. resolve and load that lineage's Current State and Next Actions;
7. load Decisions and Evidence when required by the current operation;
8. surface material inconsistencies or discovery/binding failures;
9. resume without replaying predecessor-private context.

## 8. Lineage-local checkpoints

A checkpoint remains an intentional persistence boundary where material Project truth is reconciled into durable continuity.

In Core `0.2`, checkpoint authority is scoped to the selected lineage unless Project policy explicitly defines a broader Project-wide transaction.

A completed checkpoint on lineage `A` MUST NOT implicitly mutate the authoritative continuity of lineage `B`.

The Core `0.1` coherent-checkpoint rules remain in force per lineage:

- construct a coherent candidate before authoritative mutation when material continuity changes exist;
- do not expose mixed checkpoint generations as completed truth;
- use atomic backend publication where available, or generation/revision/pointer metadata sufficient to reject mixed generations;
- detect stale authoritative bases and surface `AGNIR_CHECKPOINT_CONFLICT` rather than silently overwriting newer truth;
- verify that fresh discovery resolves the resulting authoritative continuity.

## 9. Lineage integration and reconciliation

A **Lineage Integration** combines relevant work from one or more source lineages into a target lineage.

Integration is a reconciliation operation, not a continuity-copy operation.

A conforming integration MUST consider, as applicable:

1. the actual resulting Project state represented by the integration candidate;
2. target-lineage continuity before integration;
3. relevant source-lineage continuity and Evidence;
4. current Principal intent and Project policy;
5. backend-specific integration results or receipts.

Source Current State, Next Actions, Decisions, or Evidence MUST NOT automatically become target truth merely because source Project changes were incorporated.

If an operation has produced or selected an integration candidate but target continuity has not yet been reconciled sufficiently for safe publication, the implementation MUST NOT claim the target integration is complete. It SHOULD surface semantics equivalent to `AGNIR_LINEAGE_RECONCILIATION_REQUIRED` when that state is externally observable.

Cross-Project integration MUST NOT bypass Project identity validation. Accidental source/target Project identity mismatch remains `AGNIR_DISCOVERY_PROJECT_MISMATCH` unless an explicit higher-level cross-Project protocol governs the operation.

## 10. Coherent target publication

Advancing authoritative target Project state across a lineage integration is a publication boundary.

When an integration changes both Project state and target continuity, a conforming Agnir-controlled path MUST NOT knowingly publish a target generation in which the integrated Project result and target continuity disagree.

The safe abstract sequence is:

1. capture the authoritative target generation and target continuity;
2. construct or stage the integration candidate without publishing the target;
3. reconcile target continuity against the candidate and relevant source/target evidence;
4. construct the new target checkpoint;
5. publish integrated Project state and reconciled target continuity as one coherent authoritative transition;
6. verify fresh target discovery.

If the backend supports an atomic transaction, implementations SHOULD use it. If it does not, they MUST use generation/revision/pointer semantics that prevent a fresh compatible resolver from accepting an intermediate incoherent target as completed truth.

If the target authoritative generation changes after the integration candidate was based but before publication, the implementation MUST fail rather than overwrite the newer target. The failure MUST preserve semantics equivalent to `AGNIR_LINEAGE_INTEGRATION_CONFLICT` or the more general `AGNIR_CHECKPOINT_CONFLICT` when the implementation does not expose a distinct integration class.

If a relevant source lineage is part of the staged candidate and its authoritative generation changes before publication, the implementation MUST re-resolve/reconcile or fail rather than knowingly publish against stale source evidence.

An external mechanism MAY advance a target outside Agnir's control. If that produces a target whose Project state and continuity are known to be unreconciled, the state is recovery-required, not a conforming completed integration.

## 11. Truth reconciliation

Unless stricter Project policy applies, conflicting information SHOULD be reconciled in this order:

1. directly observed current Project or relevant external-system state;
2. explicit current Principal instruction or policy;
3. current durable target-lineage continuity;
4. relevant source-lineage continuity and Evidence;
5. older checkpoint/evidence;
6. Executor-private context.

Material unresolved uncertainty MUST be surfaced rather than guessed.

## 12. Failure classes

Core `0.2` retains the Core `0.1` discovery and checkpoint failure semantics and adds lineage-aware classes when applicable:

- `AGNIR_LINEAGE_REQUIRED`
- `AGNIR_LINEAGE_NOT_FOUND`
- `AGNIR_LINEAGE_RECONCILIATION_REQUIRED`
- `AGNIR_LINEAGE_INTEGRATION_CONFLICT`

Existing classes including `AGNIR_DISCOVERY_PROJECT_MISMATCH`, `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`, `AGNIR_DISCOVERY_UNRESOLVABLE`, and `AGNIR_CHECKPOINT_CONFLICT` remain valid.

Profiles and adapters MAY expose more specific backend selector/binding/integration failures in addition to these semantic classes.

## 13. Backend neutrality

Core `0.2` conformance requires evidence from materially different backend models. At minimum before final stable publication:

- one VCS-backed model MUST demonstrate branches/workspaces selecting/binding logical lineages without making VCS concepts Core requirements;
- one non-VCS transactional model MUST demonstrate the same lineage invariants without Git branches, commits, worktrees, refs, or repository semantics.

Passing only a Git/VCS implementation is insufficient evidence for accepting Continuity Lineage as a Core abstraction.

## 14. VCS mapping

A VCS profile/adapter MAY map concepts approximately as follows:

```text
selected branch/ref/worktree -> backend selector/binding for one Continuity Lineage
logical lineage identity     -> durable identity resolved by the VCS profile/adapter
branch-local checkpoint      -> lineage-local checkpoint
merge/rebase/cherry-pick     -> lineage integration boundary
commit/revision SHA          -> backend checkpoint receipt
ref advancement              -> backend publication boundary
```

A branch/ref name MUST NOT be assumed by Core to equal the logical lineage identity. A VCS profile MAY deliberately make them equal only if it also defines safe behavior for branch creation, rename/rebinding, deletion/recreation, and ambiguity without silently conflating locator changes with lineage identity changes.

The mapping is informative for adapters/profiles. None of these VCS terms is required by Core.

## 15. Relationship to Core 0.1

Core `0.2` preserves the project-owned continuity principles, required memory semantics, cold-start recoverability, Project identity checks, truth reconciliation, confidentiality, checkpoint consistency, and backend independence established by Core `0.1`.

The breaking addition is that continuity is no longer assumed to have exactly one implicit Project-global line. Lineage selection, logical identity, selector/binding resolution, isolation, integration, and coherent target publication become explicit protocol semantics.

Migration from Core `0.1` to `0.2` is specified in `spec/CORE_0_1_TO_0_2_MIGRATION.md` and executable conformance. An existing single continuity line becomes exactly one initial/default logical lineage while preserving Project identity and durable truth.