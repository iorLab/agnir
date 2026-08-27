# PPMP Core Specification

Version: 2.0.0

## 1. Purpose

PPMP defines durable Project Memory for long-running AI-assisted projects. Durable knowledge MUST remain recoverable when conversational context, model memory, or a particular AI session is unavailable.

The keywords MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## 2. Project

A Project is a continuing body of work with an identity, durable state, and a boundary within which prior knowledge affects future work. A Project does not require a Git repository, source-code repository, or any specific AI product feature.

## 3. Project Memory

A conforming Project Memory MUST provide durable representations of:

- **Current State** — the authoritative current summary needed to continue the project;
- **Next Steps** — actionable outstanding work, priorities, blockers, and deferred items;
- **Decisions** — confirmed durable decisions and material rationale;
- **Checkpoint History** — optional concise chronological evidence when meaningful work occurred.

Implementations MAY serialize these concepts as files, records, documents, objects, or another persistent representation.

## 4. Current state versus history

Current State MUST prefer present truth over accumulated chronology. Stale state SHOULD be replaced rather than appended indefinitely.

Checkpoint History MUST NOT become the only location of a fact that is required to understand current state.

Raw conversational transcripts are not Project Memory by default and MUST NOT be required for conformance.

## 5. State vocabulary

PPMP uses these status terms consistently:

- **Completed** — implementation or work has been performed.
- **Verified** — completion has independent evidence such as tests, inspection, deployment evidence, or equivalent validation.
- **In Progress** — work has started but is not complete.
- **Planned** — work is approved and intended but not started.
- **Proposed** — an option or idea under consideration and not yet accepted.
- **Blocked** — work cannot proceed until a stated dependency or condition changes.

A claim MUST NOT be upgraded from Completed to Verified without evidence.

## 6. Authority hierarchy

When sources conflict, an implementation SHOULD reconcile them in this order:

1. directly observed current project or relevant external-system state;
2. explicit current user instruction;
3. current durable Project Memory;
4. older checkpoint or historical records;
5. conversational recollection or model memory.

Unresolved material uncertainty MUST be surfaced rather than guessed.

## 7. Core invariants

A conforming implementation MUST:

- preserve durable project knowledge outside ephemeral conversational context;
- avoid inventing project state;
- distinguish current state from history;
- avoid unnecessary duplication of canonical facts;
- preserve useful existing durable content when updating memory;
- classify inferred facts conservatively;
- keep project-specific state within the project's own durable-memory boundary;
- support intentional checkpoints when durable state changes materially.

## 8. Profiles

Profiles extend the Core with domain-specific durable concepts. Profiles SHOULD be composable and SHOULD be activated only when they represent recurring or structurally important work.

Optional profile artifacts SHOULD be materialized lazily rather than as large empty structures.

## 9. Persistence requirement

Persistence is a protocol requirement; a particular persistence technology is not. A conforming implementation MUST use storage durable enough for the project's continuity expectations and MUST be able to recover the Core semantic state without relying on the original conversation.
