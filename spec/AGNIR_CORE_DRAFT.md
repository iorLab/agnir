# Agnir Core 0.1 Architecture Draft

**Status:** Architecture transition draft; not a released conformance specification  
**Draft line:** `Agnir Core 0.1`  
**Predecessor:** PPMP v2.0.0 / Persistent Project Memory (PPM) / Sandminni

## 1. Purpose

Agnir is project-owned durable continuity.

Agnir exists so that a Project can preserve the state, decisions, next actions, and evidence required to continue safely even when an Executor, execution environment, storage implementation, or conversational context is replaced or lost.

The stable ownership rule is:

> The Project persists; Executors and execution environments may change.

Agnir Core MUST NOT require Git, GitHub, a repository host, ChatGPT, a conversational interface, any particular AI agent, a local or remote execution model, or a specific storage layout.

## 2. Identity and layer model

**Agnir** is the umbrella project and protocol identity for the new lineage. The new lineage does not preserve the predecessor naming stack of separate PPMP protocol, PPM reference implementation, and Sandminni product identities.

The architecture separates these layers:

1. **Agnir Core** — normative project-memory and continuity semantics.
2. **Agnir Profiles** — optional domain-specific durable-memory semantics.
3. **Implementations** — executable behavior that reads, validates, updates, and checkpoints Agnir state.
4. **Backends** — persistence mechanisms and storage-specific behavior.
5. **Adapters** — integration with execution surfaces, workspace products, IDEs, CLIs, CI systems, or other environments.

An implementation, backend, or adapter MAY use Git, repositories, databases, local files, APIs, cloud stores, ChatGPT Projects, or other technology. Those choices MUST NOT become Agnir Core requirements merely because a reference implementation uses them.

## 3. Core concepts

### 3.1 Project

A **Project** is a continuing body of work with a durable identity and a boundary within which prior knowledge affects future work.

Project identity MUST NOT be defined solely by an Executor session or execution environment.

### 3.2 Principal

A **Principal** is an authority that provides or owns intent, policy, approval, or authorization relevant to the Project.

A Principal MAY be a person, organization, policy system, or composed authority model.

### 3.3 Executor

An **Executor** is an entity that performs Project operations, including reading or writing Agnir state.

An Executor MAY be a human, AI agent, CLI, IDE integration, automation, CI runner, service, or composed system.

Agnir conformance MUST NOT depend on an Executor being an AI model or conversational agent.

### 3.4 Durable Memory

Agnir durable memory MUST be able to represent at least:

- **Current State** — present truth required to continue safely;
- **Next Actions** — actionable outstanding work, priorities, blockers, and deferred work;
- **Decisions** — durable accepted decisions and material rationale;
- **Evidence / Checkpoints** — concise historical evidence needed to support claims, recovery, audit, or resumability.

Current State MUST prefer present truth over chronology. Historical evidence MUST NOT become the only location of a fact required to understand current state.

Raw transcripts, model memory, or private Executor recollection MUST NOT be required for Agnir continuity.

## 4. Authority and truth reconciliation

When durable memory conflicts with other available evidence, a conforming implementation SHOULD reconcile sources in this order unless Project policy declares a stricter domain-specific rule:

1. directly observed current Project or relevant external-system state;
2. explicit current Principal instruction or policy;
3. current durable Agnir state;
4. older checkpoint or historical evidence;
5. Executor-private recollection, conversational context, or model memory.

Material unresolved uncertainty MUST be surfaced rather than guessed.

No execution environment becomes authoritative merely because work occurred there.

## 5. Discovery model

Agnir discovery is defined semantically rather than by a mandatory filename or storage location.

### 5.1 Project Entry Point

A **Project Entry Point** is the durable handle or context from which a compatible Executor begins Project access. Examples include a filesystem project, repository, workspace object, project URL, database-backed project identity, or another adapter-defined handle.

### 5.2 Discovery Record

A **Discovery Record** is the minimum durable information required to identify the applicable Agnir version and resolve the Project's durable-memory locations.

The Discovery Record MAY be colocated with the Project Entry Point or reached through an adapter-defined durable binding.

### 5.3 Locator Chain

A **Locator Chain** is the resolvable sequence from Project Entry Point to Discovery Record to durable Agnir state.

A conforming Locator Chain MUST:

- be durable for the continuity expectations of the Project;
- terminate in resolvable Agnir state;
- identify the applicable Agnir protocol version or compatibility line;
- avoid dependence on predecessor-private conversational or model context;
- not require a particular filesystem path, VCS, repository host, or execution surface;
- expose missing, stale, unauthorized, cyclic, or ambiguous resolution as a discovery failure rather than fabricating state.

Externally stored Agnir state is conforming only when the Project has a durable, authorized route to resolve that external state from its Project Entry Point.

## 6. Cold-start / fresh-executor invariant

A compatible fresh Executor that has no predecessor-private context and is given only an authorized Project Entry Point MUST be able to:

1. identify the Project boundary;
2. resolve the Discovery Record;
3. validate the Agnir version or compatibility line;
4. resolve and load Current State and Next Actions;
5. load Decisions and Evidence as required by the current task;
6. identify material inconsistencies or missing memory;
7. resume work without requiring replay of a predecessor conversation or private Executor memory.

Agnir calls this the **cold-start discovery invariant**. `Fresh-executor recovery` is the recovery case in which the invariant is exercised after an Executor or context replacement.

An implementation MUST NOT claim cold-start resumability when the Locator Chain is missing, stale, unauthorized, or unresolved.

## 7. Configuration semantics

Agnir Core defines semantic configuration, not a mandatory serialization.

A conforming Discovery Record MUST provide semantics equivalent to:

```yaml
agnir:
  version: 0.1
project:
  identity: <durable project identity>
memory:
  state: <durable locator>
  next_actions: <durable locator>
  decisions: <durable locator or null>
  evidence: <durable locator or null>
policy:
  checkpoint: <project policy>
```

Implementations MAY extend this with backend, adapter, namespace, repository, database, credential-reference, or profile configuration.

No top-level filename such as `AGNIR.yaml` is required by Core. A filename MAY be standardized by a filesystem/repository profile if conformance evidence later justifies doing so.

## 8. Persistence and confidentiality

Agnir requires durability, not a specific persistence technology.

A conforming implementation MUST use persistence sufficient for the Project's declared continuity expectations and MUST recover required Core state without relying on the original Executor context.

Agnir Core does not require secret values to be stored in Project Memory. Implementations MUST respect the Project's confidentiality and authorization policy. A profile or consuming protocol MAY impose stricter requirements, including prohibiting plaintext secret values in Agnir memory.

## 9. Checkpoint semantics

A checkpoint is an intentional persistence boundary at which material Project truth is reconciled into durable memory.

A conforming checkpoint SHOULD update current state, next actions, decisions, and necessary evidence coherently. It MUST NOT claim resumability if the Discovery Record or Locator Chain cannot resolve the resulting authoritative memory.

Checkpoint persistence is independent from application deployment, CI, or release behavior. Backends SHOULD avoid unintended side effects when persisting memory.

## 10. Versioning and predecessor compatibility

Agnir starts a new explicit version namespace. The first target line is **Agnir Core 0.1**.

PPMP v2.0.0 remains a released predecessor specification and historical evidence base. PPMP v2 conformance MUST NOT be silently relabeled as Agnir conformance.

Compatibility with a PPMP v2 project requires an explicit migration or compatibility adapter that maps predecessor configuration and semantics into an Agnir version and demonstrates the Agnir discovery invariant.

The repository MAY continue to use PPMP v2 / PPM to maintain itself during the transition. Self-hosting through a predecessor implementation does not make predecessor implementation details Agnir Core requirements.

## 11. Relationship to Svif

Svif is an independent consuming protocol.

- Agnir MUST remain useful without Svif.
- Svif MAY require conformance to a specified Agnir Core version line.
- Svif MUST NOT require a particular Agnir implementation, backend, or adapter when an alternative implementation conforms to the required Agnir Core contract.
- Svif lifecycle, verification, delivery, provider, and trust-boundary semantics MUST NOT be added to Agnir Core unless they are independently justified as general durable-continuity semantics.

The intended dependency direction is `Svif -> Agnir`.

## 12. Migration targets

The architecture transition should next define:

1. the final normative wording and version identifier for Agnir Core 0.1;
2. a migration mapping from PPMP v2 configuration and concepts to Agnir;
3. a reference discovery serialization/profile for repository/filesystem projects without making that layout Core;
4. conformance cases for cold-start discovery across at least two materially different execution/storage surfaces;
5. a multi-project workspace isolation case proving that one execution workspace can operate multiple Projects without durable context bleed;
6. the exact Agnir Core compatibility line consumed by Svif.
