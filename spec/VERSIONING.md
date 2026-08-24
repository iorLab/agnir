# Versioning

Version: 1.0.0

RPM follows Semantic Versioning for the specification.

## 1. Version format

```text
MAJOR.MINOR.PATCH
```

- **MAJOR** — incompatible changes to manifest semantics, Core requirements, or normative behavior.
- **MINOR** — backward-compatible new profiles, optional fields, templates, or capabilities.
- **PATCH** — clarifications, typo fixes, and backward-compatible corrections that do not change intended behavior materially.

The repository root `VERSION` file declares the current specification version.

## 2. Consuming-project version

Every initialized consuming project MUST record the RPM version it was initialized against in `.chatgpt/project-memory.yaml`.

An implementation MUST NOT silently reinterpret a project using a newer incompatible major specification.

## 3. Compatibility behavior

When loading a manifest:

- same supported MAJOR and equal/older MINOR: proceed using compatible behavior;
- newer MINOR not understood by the implementation: proceed only when unknown fields can be safely ignored; otherwise surface the incompatibility;
- different MAJOR: require an explicit migration before applying the new semantics.

## 4. Upgrades

RPM upgrades are intentional project changes.

Before upgrading a consuming project:

1. read the target version's migration notes when available;
2. compare manifest and Core requirements;
3. preserve existing durable knowledge;
4. update the manifest version only after the repository conforms to the new version;
5. commit the migration as a distinct change.

## 5. Profile evolution

Profiles may add optional domain artifacts in MINOR releases. Existing projects are not required to create newly introduced optional artifacts unless they become useful.

Removal or semantic redefinition of required profile behavior requires a MAJOR release.

## 6. Central specification source

A manifest SHOULD declare the specification repository. The declared version is authoritative for intended semantics.

If the specification repository's root `VERSION` does not match the manifest's requested version, the implementation SHOULD surface the mismatch rather than silently applying unknown rules.

For RPM v1, the reference implementation source is:

```text
mattamior/rpm
```

## 7. Version history

Version history SHOULD be recorded in repository Git history and may additionally be summarized in a changelog in future releases.
