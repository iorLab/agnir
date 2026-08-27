# Agnir Core 0.1

**Status:** Working normative specification on the active `0.1` line.

## 1. Purpose

Agnir is a project-owned durable continuity protocol. It enables a Project to preserve and recover the state, next actions, decisions, and evidence required to continue safely when Executors, execution environments, storage implementations, or conversational contexts change.

The stable ownership rule is:

> The Project persists; Executors and execution environments may change.

Agnir Core MUST NOT require Git, GitHub, a repository host, a filesystem, ChatGPT, an AI agent, a conversational interface, a local/remote execution distinction, or any single storage layout.

## 2. Conformance vocabulary

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are normative requirements.

Agnir separates five layers:

1. **Core** — project continuity semantics.
2. **Profiles** — optional domain or substrate conventions.
3. **Implementations** — executable readers/writers/validators.
4. **Backends** — persistence mechanisms.
5. **Adapters** — execution-surface and external-system integration.

Implementation popularity does not promote lower-layer behavior into Core.

## 3. Core concepts

### Project

A Project is the continuing body of work that owns durable continuity. Project identity MUST survive replacement of an Executor or execution environment.

### Principal

A Principal provides or owns intent, policy, approval, or authorization relevant to the Project.

### Executor

An Executor performs Project operations. It MAY be a human, AI system, CLI, IDE, automation, CI runner, service, or composition of those forms.

### Project Entry Point

A Project Entry Point is the authorized durable handle from which discovery begins.

### Discovery Record

A Discovery Record identifies the applicable Agnir Core version/compatibility line, the Project identity, and locators for required durable memory.

### Locator Chain

A Locator Chain is the resolvable route from Project Entry Point to Discovery Record and then to required durable memory.

## 4. Required durable memory semantics

A conforming Project MUST make the following semantics durably recoverable:

- **Current State** — present truth required to continue safely;
- **Next Actions** — outstanding actionable work, blockers, priorities, and intentionally deferred work;
- **Decisions** — accepted durable decisions and material rationale;
- **Evidence / Checkpoints** — concise evidence required for recovery, audit, or support of material claims.

Current State MUST prefer current truth over chronology. A fact required to understand current state MUST NOT exist only in historical evidence.

Raw transcripts, model memory, private Executor recollection, or a prior conversation MUST NOT be required for continuity.

## 5. Cold-start discovery invariant

A compatible fresh Executor given only an authorized Project Entry Point and the applicable profile/adapter implementation MUST be able to:

1. resolve the Discovery Record;
2. validate Agnir version compatibility;
3. verify Project identity sufficiently to detect accidental cross-Project resolution;
4. resolve and load Current State and Next Actions;
5. load Decisions and Evidence when required by the current operation;
6. surface material inconsistencies or discovery failures;
7. resume without replaying predecessor-private context.

Agnir continuity MUST NOT be claimed when the Locator Chain is missing, stale, ambiguous, cyclic, unauthorized, or otherwise unresolved.

## 6. Discovery Record semantics

A Discovery Record MUST provide semantics equivalent to:

```yaml
agnir:
  version: "0.1"
project:
  identity: <durable-project-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

`state` and `next_actions` are required. `decisions` and `evidence` MAY be null only when no material durable content in those categories is required for safe continuation.

Core does not mandate YAML, a filename, a URI scheme, or a physical storage location.

## 7. Project identity

Project identity MUST be non-empty and durable within the scope in which the active profile/backend resolves it. Global uniqueness is not required by Core.

URI/URN identity forms are RECOMMENDED when a Project must remain identifiable across backend or host changes. Opaque identifiers MAY be used when the active scope makes them unambiguous.

A detected identity mismatch MUST fail discovery rather than silently adopt another Project's memory.

## 8. Truth reconciliation

Unless stricter Project policy applies, implementations SHOULD reconcile conflicting information in this order:

1. directly observed current Project or relevant external-system state;
2. explicit current Principal instruction or policy;
3. current durable Agnir state;
4. older checkpoint/evidence;
5. Executor-private context.

Material unresolved uncertainty MUST be surfaced rather than guessed.

## 9. Discovery failure classes

Implementations MUST preserve semantics equivalent to these classes when applicable:

- `AGNIR_DISCOVERY_NOT_FOUND`
- `AGNIR_DISCOVERY_AMBIGUOUS`
- `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`
- `AGNIR_DISCOVERY_PROJECT_MISMATCH`
- `AGNIR_DISCOVERY_UNRESOLVABLE`
- `AGNIR_DISCOVERY_UNAUTHORIZED`
- `AGNIR_DISCOVERY_CYCLE`
- `AGNIR_DISCOVERY_STALE`
- `AGNIR_DISCOVERY_INCONSISTENT`

Implementations MAY expose platform-specific error types in addition to these semantic classes.

## 10. Mutation, relocation, and repair

Authorized repair MUST occur at the earliest faulty layer and MUST NOT invent Project state.

If authoritative Agnir memory is relocated, the durable discovery route MUST be updated so a future fresh Executor can resolve the new state without the relocating Executor's private knowledge.

After material discovery repair, cold-start discovery SHOULD be rerun from the Project Entry Point.

## 11. Persistence and confidentiality

Agnir requires durability appropriate to the Project's continuity expectations, not any specific persistence technology.

Discovery Records SHOULD contain authorization or credential references rather than secret values. Implementations MUST respect Project confidentiality and authorization policy.

Agnir Core does not require secrets to be stored in durable memory.

## 12. Checkpoints

A checkpoint is an intentional persistence boundary where material Project truth is reconciled into durable memory.

A checkpoint SHOULD coherently reconcile Current State, Next Actions, Decisions, and necessary Evidence. It MUST NOT claim resumability when the Discovery Record or Locator Chain cannot resolve the resulting authoritative memory.

Checkpoint persistence is independent of deployment, CI, release, or any other consuming workflow.

## 13. Versioning and extensions

Agnir begins a new version namespace at Core `0.1`. PPMP v2.0.0 is predecessor evidence and MUST NOT be silently relabeled as Agnir.

Agnir Core version values are strings. The reference repository/filesystem profile uses `"0.1"` for the Core line and `<profile-name>/<major.minor>` for profile identifiers.

Profiles MAY define serialization-specific extension namespaces. Extensions MUST NOT change Core field meaning while claiming the same Core version.

## 14. Relationship to Svif

Svif is an independent consuming protocol. Svif MAY require a compatible Agnir Core line but MUST NOT require a particular Agnir implementation, backend, adapter, or repository layout when another implementation satisfies the same Core contract.

Dependency direction is `Svif -> Agnir`.
