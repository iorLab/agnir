# iorMemory

iorMemory is a platform-agnostic protocol for durable project memory in AI-assisted work.

Its core principle is simple: important project knowledge MUST survive the loss of conversational context. The protocol defines what durable project memory means, how it is classified, when it is checkpointed, and how compatible implementations identify the version they support. It does not require Git, a repository, ChatGPT, or any particular storage layout.

## Status

Current protocol version: **iorMemory v2.0.0**.

RPM (Repository Project Memory) v1.0.0 is the historical repository- and ChatGPT-oriented predecessor. The v2 transition deliberately separates protocol semantics from implementation, storage backend, and platform integration.

## Architecture

- **iorMemory protocol** — normative semantics under `spec/`, reusable profiles under `profiles/`, and conformance/versioning rules.
- **Persistent Project Memory (PPM)** — the initial reference Skill/implementation described under `implementations/`.
- **Persistence backends** — concrete durable-storage strategies such as repository/Git persistence, described under `backends/`.
- **Platform adapters** — environment-specific discovery and bootstrap behavior, beginning with ChatGPT under `adapters/`.

## Core model

Every conforming project has durable representations for:

- current project state;
- actionable next steps and blockers;
- confirmed durable decisions;
- optional meaningful checkpoint history;
- profile-specific durable knowledge when useful.

The representation MAY be files, database records, documents, API objects, or another durable medium. Implementations MUST preserve the semantic distinction between current state and history.

## Repository layout

```text
spec/              normative iorMemory protocol
profiles/          composable domain profiles
templates/         reference serialization/templates
examples/          example configurations
implementations/   reference implementation behavior
backends/          persistence backend behavior
adapters/          platform-specific integration behavior
site/              non-normative public presentation layer
docs/project-memory/ maintenance state for this repository
```

## Reference implementation

**Persistent Project Memory (PPM)** is the first reference implementation. Its initial ChatGPT adapter and repository backend preserve the practical workflow proven by RPM v1 while keeping those mechanics outside protocol requirements.

## Migration from RPM v1

RPM v1 projects are not silently reinterpreted as iorMemory v2 projects. Migration is explicit because v2 removes repository paths and ChatGPT-specific bootstrap behavior from protocol-level requirements. See `spec/MIGRATION.md`.

## Design goals

iorMemory is designed to be durable, explicit, lightweight, composable, storage-agnostic, platform-agnostic, auditable, and conservative about what becomes persistent state.

It is not a transcript archive. Persist durable project knowledge, not raw conversations.
