# Agnir Discovery Contract Draft

**Status:** Agnir Core 0.1 supporting draft; not released conformance text  
**Parent:** `spec/AGNIR_CORE_DRAFT.md`

## 1. Purpose

This document makes the Agnir cold-start discovery invariant testable without requiring a particular filesystem path, VCS, repository host, storage backend, or execution surface.

A compatible fresh Executor starts with an authorized **Project Entry Point** and no predecessor-private context. Discovery succeeds only when the Executor can resolve an applicable **Discovery Record** and then resolve the Project's required durable Agnir memory.

## 2. Required discovery semantics

A Discovery Record MUST identify semantics equivalent to:

```yaml
agnir:
  version: <agnir-core-version-or-compatible-line>
project:
  identity: <durable-project-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

The serialization, field names, path, transport, and storage format MAY differ by profile/backend/adapter as long as the semantics are preserved.

### 2.1 `agnir.version`

The Discovery Record MUST identify the Agnir Core version or declared compatibility line used to interpret the memory semantics.

An Executor MUST NOT silently reinterpret an unsupported incompatible version.

### 2.2 `project.identity`

The Discovery Record MUST identify the Project strongly enough to detect accidental resolution into the durable memory of a different Project.

Project identity MAY be an opaque stable identifier, URI, namespace-qualified name, repository identity, workspace identity, or another profile-defined durable identifier.

Global uniqueness is not required by Core if the active adapter/backend scope makes the identity unambiguous.

### 2.3 required memory locators

`state` and `next_actions` are required locators.

`decisions` and `evidence` MAY be null when the Project legitimately has no material durable content in those categories, but an implementation MUST NOT use null merely to hide content that is required for safe continuation.

## 3. Project Entry Point

A Project Entry Point is the minimum authorized handle from which discovery begins.

Examples include:

- a filesystem directory;
- a repository or repository ref;
- a workspace/project object;
- a project URL;
- a database-backed project identifier;
- an API resource;
- an adapter-defined project binding.

Core does not define one universal entry-point type.

A conforming adapter/profile MUST document how its Project Entry Point resolves or exposes the first Discovery Record hop.

## 4. Locator Chain

A Locator Chain is the ordered resolution path from Project Entry Point to Discovery Record to required memory objects.

Each hop MUST be one of:

- directly resolvable by the active backend/adapter;
- resolvable through an explicitly declared next locator;
- resolvable through a stable environment binding that is part of the Project's configured execution surface.

A Locator Chain MUST NOT depend on:

- a previous conversation being remembered;
- private model memory;
- an unstated path known only to a predecessor Executor;
- a secret value embedded only in a prior prompt;
- a mutable workspace note that is not durably bound to the Project.

## 5. External memory

Agnir memory MAY reside outside the immediate Project substrate.

External memory is conforming only when:

1. the Project Entry Point durably resolves the external location;
2. the Project identity can be checked at or after resolution;
3. the required authorization mechanism can be invoked by the active adapter/backend without predecessor-private context;
4. missing authorization is reported as an explicit discovery/authority failure;
5. the external location can be changed without leaving future Executors dependent on a stale hidden pointer.

Core does not standardize OAuth, API keys, service identities, filesystem permissions, or other authorization technologies.

The Discovery Record SHOULD contain credential or authorization **references/requirements**, not secret values, when such metadata is required for resolution.

## 6. Resolution algorithm

A fresh Executor SHOULD perform discovery in this order:

1. accept or resolve the authorized Project Entry Point;
2. determine the active discovery profile/adapter convention;
3. resolve the Discovery Record;
4. detect cycles and conflicting candidate Discovery Records;
5. validate `agnir.version` compatibility;
6. validate `project.identity` against the active Project boundary;
7. resolve Current State and Next Actions;
8. resolve Decisions and Evidence when needed for the current operation;
9. validate internal consistency sufficient for safe continuation;
10. surface any material unresolved discovery problem instead of fabricating continuity.

The exact I/O mechanism is implementation-specific.

## 7. Discovery failure taxonomy

Agnir Core 0.1 should standardize semantic failure classes even if implementations expose different error types.

### `AGNIR_DISCOVERY_NOT_FOUND`

No Discovery Record can be resolved from the authorized Project Entry Point under the active profile/adapter conventions.

### `AGNIR_DISCOVERY_AMBIGUOUS`

Multiple candidate Discovery Records or memory roots resolve and the implementation cannot determine which is authoritative.

### `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`

The Discovery Record declares an Agnir version/compatibility line the implementation cannot safely interpret.

### `AGNIR_DISCOVERY_PROJECT_MISMATCH`

The resolved memory identifies a different Project than the active Project boundary.

### `AGNIR_DISCOVERY_UNRESOLVABLE`

A required locator exists but cannot be resolved to durable state.

### `AGNIR_DISCOVERY_UNAUTHORIZED`

The locator is known but required authorization is unavailable or denied.

This MUST be distinguished from "not found" when the implementation can determine the difference without leaking protected information.

### `AGNIR_DISCOVERY_CYCLE`

The Locator Chain contains a cycle and does not terminate in required durable state.

### `AGNIR_DISCOVERY_STALE`

A durable locator resolves only to state known to be superseded, deleted, moved, or otherwise non-authoritative.

### `AGNIR_DISCOVERY_INCONSISTENT`

Required memory objects resolve but materially contradict the Discovery Record or one another such that safe continuation cannot be established.

## 8. Repair requirements

An implementation MAY repair discovery when authorized, but MUST NOT invent Project state.

Repair SHOULD occur at the earliest faulty layer:

- missing repository/filesystem anchor -> discovery profile repair;
- moved external store -> locator repair;
- unsupported version -> explicit migration/compatible implementation;
- authorization failure -> authority/adapter action;
- Project mismatch -> boundary correction, never silent adoption;
- stale memory -> reconcile against authoritative current evidence;
- inconsistent memory -> surface and reconcile material conflicts.

After repair, cold-start discovery SHOULD be re-run from the Project Entry Point rather than trusted solely because the repairing Executor already knows the answer.

## 9. Mutation and relocation

When authoritative Agnir memory is relocated, the Project's durable discovery route MUST be updated so a future fresh Executor does not require the relocating Executor's private knowledge.

An implementation SHOULD update a Discovery Record and its referenced memory in a way that avoids a long-lived state where neither old nor new locators are safely resolvable.

Temporary redirects/aliases MAY be used by a profile/backend when they are durable, bounded, and do not create ambiguous authority.

## 10. Discovery Record confidentiality

A Discovery Record is often more widely discoverable than the memory it locates.

Therefore:

- secret values SHOULD NOT be embedded in a Discovery Record;
- authorization requirements or secret-store references MAY be declared;
- locator metadata SHOULD reveal no more sensitive information than is necessary for resolution;
- a backend/adapter MAY protect the Discovery Record itself when the Project's access model requires it, provided an authorized fresh Executor can still resolve it.

## 11. Reference repository/filesystem profile — unresolved choice

A future repository/filesystem profile may standardize a conventional anchor such as:

```text
AGNIR.yaml
```

or:

```text
.agnir/
  manifest.yaml
```

or another equivalent convention.

This draft intentionally does not choose one yet. The profile choice should optimize cold-start discoverability, tooling simplicity, coexistence with existing Project layouts, and migration from predecessor `.chatgpt/project-memory.yaml` projects.

The chosen profile convention MUST remain a profile rule rather than an Agnir Core requirement.

## 12. Cold-start conformance procedure

A discovery conformance case SHOULD begin with a fresh Executor/environment that receives only the Project Entry Point and the adapter/profile implementation required to interpret that entry-point type.

The test passes only if the Executor can:

1. locate the Discovery Record;
2. identify the Agnir version line;
3. verify Project identity;
4. load Current State and Next Actions;
5. load relevant Decisions/Evidence without predecessor-chat replay;
6. identify any declared blockers/uncertainty;
7. demonstrate that a material current fact was recovered from durable Agnir state rather than hidden test harness context.

A test that pre-supplies the memory path or current state outside the Project's normal discovery mechanism does not prove the cold-start invariant.
