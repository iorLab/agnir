# Migration from RPM v1

Version: 2.0.0

## 1. Relationship

RPM (Repository Project Memory) v1.0.0 is the historical predecessor of iorMemory. iorMemory v2 retains the durable-memory semantics that proved reusable while separating protocol requirements from implementation, persistence backend, and platform adapter behavior.

This is a MAJOR migration, not a cosmetic rename.

## 2. What remains protocol-level

The following concepts carry forward: Current State versus history, Next Steps, durable Decisions, meaningful checkpoints, state vocabulary, conservative classification, composable profiles, lazy expansion, event-driven persistence, authority ordering, and explicit compatibility/versioning.

## 3. What moves out of the protocol

- repository/Git canonical storage and commit behavior → repository backend;
- repository-relative paths → backend serialization;
- `.chatgpt/project-memory.yaml` → ChatGPT + repository convention;
- first-substantive-turn ChatGPT behavior and Project isolation → ChatGPT adapter;
- concrete file names such as `PROJECT_STATE.md` → reference serialization, not protocol semantics.

## 4. RPM v1 project migration

A repository-backed RPM v1 project may migrate by:

1. preserving its existing durable memory files;
2. replacing the `rpm` configuration identity with `iormemory.version: 2.0.0` plus implementation/backend/adapter metadata;
3. treating existing Core files as the repository backend's serialization of iorMemory Core concepts;
4. updating Project Instructions to invoke the PPM ChatGPT adapter rather than claiming repository/Git behavior is required by the protocol;
5. validating that no durable knowledge is lost;
6. recording the migration as a distinct durable change.

Existing v1 history SHOULD be preserved. Implementations MUST NOT silently rewrite v1 manifests as v2 without an explicit migration action.

## 5. Repository identity

The existing `mattamior/rpm` repository preserves development history during the v2 migration. Repository renaming is not required for protocol conformance and may be performed separately without changing iorMemory semantics.
