# Agnir Repository / Filesystem Profile 0.1

**Profile identifier:** `repository-filesystem/0.1`

This profile applies when the authorized Project Entry Point is a filesystem-style Project root, including a repository checkout/worktree, synced directory, hosted workspace filesystem, or equivalent hierarchical substrate.

This profile is not Agnir Core. It does not make filesystems, repositories, Git, or GitHub universal Agnir requirements.

## 1. Discovery anchor

The Project root MUST contain top-level:

```text
AGNIR.yaml
```

An Executor entering a Project root under this profile MUST inspect that anchor before relying on predecessor-private context or hidden environment knowledge.

## 2. Reference serialization

The profile uses YAML compatible with `schemas/agnir-manifest.schema.json`.

Required semantic shape:

```yaml
agnir:
  version: "0.1"
  discovery_profile: "repository-filesystem/0.1"
project:
  identity: <durable-project-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

Relative locators resolve from the Project root. Absolute filesystem paths SHOULD be avoided unless the Project intentionally accepts that portability constraint.

## 3. Profile and extension versioning

- `agnir.version` is the Core major.minor line as a string.
- `agnir.discovery_profile` is `<profile-name>/<major.minor>`.
- This profile requires `repository-filesystem/0.1`.
- `extensions` keys use `<owner>/<name>` namespaces.
- `agnir/*` extension namespaces are reserved for Agnir-defined extensions.
- Extensions MUST NOT redefine Core fields while claiming the same Core version.

## 4. Project identity and selected-root authority

`project.identity` MUST be non-empty. URI/URN forms are RECOMMENDED for identities intended to survive backend or host changes. Opaque identifiers MAY be used when the Project boundary makes them unambiguous.

Nested Projects are allowed, but each Project Entry Point MUST select one Project root. Implementations MUST NOT silently walk into an unrelated parent/child Project when the selected boundary already determines authority.

A parent and child directory may each contain their own authoritative `AGNIR.yaml`. Once one of those roots has been selected as the authorized Project Entry Point, the existence of the other does **not** make the selected root ambiguous; discovery remains scoped to the selected root. `AGNIR_DISCOVERY_AMBIGUOUS` applies earlier, when multiple candidate Project roots exist and no authority rule has selected exactly one.

A detected identity mismatch at the selected root MUST surface `AGNIR_DISCOVERY_PROJECT_MISMATCH` rather than searching a parent or child root for a more convenient identity.

## 5. Colocated memory

`.agnir/` is the recommended reference layout for colocated memory, but it is not authoritative by name. `AGNIR.yaml` locators are authoritative.

A Project MAY locate memory elsewhere, including outside the Project root, when the active backend/adapter provides a durable authorized Locator Chain.

## 6. Repository/VCS extension

Repository-aware implementations MAY declare repository metadata under an extension namespace, for example:

```yaml
extensions:
  agnir/repository:
    canonical: "owner/name"
    authoritative_ref: "main"
```

This extension is profile/backend metadata, not Core identity. A non-default authoritative ref MUST be durably discoverable; a fresh Executor cannot be expected to remember it from a prior session.

## 7. Discovery order

1. resolve the selected Project root;
2. read `AGNIR.yaml`;
3. validate Core/profile compatibility;
4. verify Project identity;
5. resolve required memory locators;
6. load Current State and Next Actions;
7. load Decisions/Evidence as required;
8. surface Agnir discovery failure semantics.

Implementations MUST NOT silently search arbitrary sibling repositories, user home directories, or old chat logs when `AGNIR.yaml` is missing.

## 8. Migration fallback

A migration-capable implementation MAY recognize `.chatgpt/project-memory.yaml` only in explicit predecessor/migration mode. Once `AGNIR.yaml` is authoritative, predecessor bootstrap files MUST NOT form a second divergent mutable state root.

## 9. Conformance

A profile conformance case SHOULD begin with only the Project root and profile implementation. It MUST prove discovery of `AGNIR.yaml`, version and identity validation, resolution of Current State and Next Actions, recovery of at least one material durable fact, and correct failure for at least one broken-locator case.

The active reference conformance suite additionally pressure-tests explicit `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, and pre-root-selection `AMBIGUOUS` semantics, plus isolation between explicitly selected nested Project roots.
