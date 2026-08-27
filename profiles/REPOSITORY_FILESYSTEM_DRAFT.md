# Agnir Repository / Filesystem Discovery Profile Draft

**Status:** Agnir Core 0.1 profile draft; not released conformance text  
**Depends on:** `spec/AGNIR_CORE_DRAFT.md`, `spec/AGNIR_DISCOVERY_DRAFT.md`

## 1. Purpose

This profile defines a simple cold-start discovery convention for Projects whose authorized Project Entry Point is a filesystem-style Project root, including a source repository checkout/worktree, synced project directory, hosted workspace filesystem, or equivalent hierarchical file substrate.

This profile is **not Agnir Core**. Agnir Core does not require a filesystem, repository, Git, or any particular filename.

## 2. Discovery anchor

The profile standardizes this top-level discovery anchor:

```text
AGNIR.yaml
```

A compatible Executor entering a Project root under this profile MUST look for `AGNIR.yaml` at the declared Project root before relying on predecessor-private context or hidden environment knowledge.

The choice of a top-level anchor is deliberate:

- it is visible and easy to discover during cold start;
- it does not require knowing a hidden-directory convention first;
- it can point either to colocated memory or to external durable memory;
- it separates the **discovery anchor** from the physical storage layout of memory;
- it provides a clear migration target from predecessor `.chatgpt/project-memory.yaml` projects.

## 3. Reference manifest

A minimal reference serialization is:

```yaml
agnir:
  version: 0.1

project:
  identity: <stable-project-identity>

memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

Relative filesystem locators are resolved relative to the Project root unless the manifest declares another profile/backend base.

Absolute paths SHOULD be avoided for portable Project memory unless the Project intentionally binds to that path and the continuity policy accepts the portability cost.

External locators MAY use profile/backend-supported URI or reference forms.

## 4. Optional `.agnir/` memory directory

For Projects that colocate Agnir memory with the filesystem Project root, this profile RECOMMENDS but does not require:

```text
AGNIR.yaml
.agnir/
  state.yaml-or-md
  next.md
  decisions.md
  evidence/
```

The exact filenames under `.agnir/` are not normative. `AGNIR.yaml` locators remain authoritative.

This allows a Project to use, for example:

```text
AGNIR.yaml
.agnir/
  PROJECT_STATE.md
  NEXT_ACTIONS.md
  DECISIONS.md
  evidence/
```

or any other declared filenames without changing profile conformance.

A Project MAY store all memory outside `.agnir/` or outside the Project root entirely.

## 5. Project root

The active adapter/backend MUST determine the Project root from the authorized Project Entry Point.

Examples:

- filesystem path supplied as Project Entry Point;
- repository root resolved by an SCM adapter;
- hosted workspace root supplied by the execution-surface adapter.

If multiple nested `AGNIR.yaml` anchors are present, the adapter MUST use the Project boundary selected by the active Project Entry Point rather than silently walking to an unrelated parent or child Project.

Nested Projects are allowed but MUST have distinguishable Project identities and boundaries.

## 6. Repository/VCS extensions

A repository-backed implementation MAY add extension metadata such as:

```yaml
extensions:
  repository:
    provider: git
    remote: <repository-identity>
    authoritative_ref: <ref-or-null>
```

or an implementation-specific equivalent.

These fields are not Agnir Core requirements and are not required for filesystem-only Projects.

When authoritative Agnir state lives on a non-default VCS ref, the repository/backend extension MUST provide enough durable information to resolve that ref during cold start before the memory locators are loaded.

A fresh Executor MUST NOT be expected to remember the active ref from a predecessor conversation.

## 7. External memory from `AGNIR.yaml`

`AGNIR.yaml` MAY point to external durable state:

```yaml
agnir:
  version: 0.1
project:
  identity: example-project
memory:
  state: agnir+https://memory.example/projects/example/state
  next_actions: agnir+https://memory.example/projects/example/next
  decisions: agnir+https://memory.example/projects/example/decisions
  evidence: agnir+https://memory.example/projects/example/evidence
```

The URI form above is illustrative; supported locator schemes are defined by implementations/backends/profiles.

The manifest MUST NOT embed secret values merely to make an external locator work. It MAY declare authorization requirements or protected credential references as extensions.

## 8. Discovery order

Under this profile, cold-start discovery is:

1. resolve the Project root;
2. read top-level `AGNIR.yaml`;
3. validate the Agnir version/compatibility line;
4. verify Project identity;
5. resolve required memory locators;
6. load Current State and Next Actions;
7. load Decisions/Evidence as required;
8. surface discovery failure classes defined by the Agnir Discovery Contract.

An implementation MUST NOT silently search arbitrary sibling repositories, user home directories, old chat logs, or other unbound locations when `AGNIR.yaml` is missing.

## 9. Legacy PPMP/PPM migration fallback

A migration-capable implementation MAY support this predecessor fallback:

```text
.chatgpt/project-memory.yaml
```

but only in explicit **PPMP v2 / migration mode**.

Recommended behavior when `AGNIR.yaml` is absent and a predecessor manifest is present:

1. identify the Project as predecessor PPMP/PPM rather than Agnir-conforming;
2. load predecessor memory according to its implementation/backend/adapter rules;
3. offer or execute an authorized explicit migration;
4. create `AGNIR.yaml` only after the target Agnir semantics and locators are valid;
5. perform a fresh cold-start test from the Project root;
6. retain predecessor history/evidence and record the migration.

Presence of `.chatgpt/project-memory.yaml` alone MUST NOT be interpreted as Agnir 0.1 conformance.

## 10. Coexistence during migration

During migration, a Project MAY temporarily contain both:

```text
AGNIR.yaml
.chatgpt/project-memory.yaml
```

The Project MUST declare which one is authoritative for the active mode and MUST avoid ambiguous divergent mutable state.

A recommended transition is:

```text
PPMP v2 mode:
  .chatgpt/project-memory.yaml authoritative

Migration mode:
  predecessor state read + Agnir target generated/validated

Agnir mode:
  AGNIR.yaml authoritative discovery anchor
  predecessor files retained only as history/compatibility material if still needed
```

Adapters MUST NOT merge conflicting current state from both systems implicitly.

## 11. Workspace registry interaction

A workspace-level project registry MAY point to the Project root or to the `AGNIR.yaml` anchor.

The registry MUST remain locator-only metadata. Mutable Current State, Next Actions, Decisions, or Evidence MUST remain in the Project's Agnir memory rather than being copied into the workspace registry.

This supports one workspace containing multiple independent Agnir Projects without creating a shared mutable memory store.

## 12. Profile conformance test

A repository/filesystem profile test SHOULD:

1. start a fresh Executor with only the Project root and profile implementation;
2. ensure no predecessor conversation/memory path is supplied;
3. discover top-level `AGNIR.yaml`;
4. validate the Agnir version and Project identity;
5. resolve and load Current State and Next Actions;
6. recover at least one material fact that exists only in durable Agnir memory;
7. demonstrate correct failure for one broken locator case;
8. if a non-default VCS ref is used, prove the active ref is durably resolved without hidden context;
9. if external memory is used, prove authorization failure and success are distinguishable without exposing secret values.

## 13. Open profile details

Before release, decide:

- exact YAML schema and schema-version field rules;
- whether Project identity should have recommended URI/UUID forms;
- standard extension namespace rules;
- standard locator URI schemes, if any;
- whether `.agnir/` should remain merely recommended or become the default reference-implementation layout;
- how symbolic links/mounts/worktrees affect Project-root boundary detection;
- whether case-insensitive filesystems require special handling of `AGNIR.yaml` naming.
