# RPM Core Specification

Version: 1.0.0

## 1. Purpose

RPM defines a durable memory layer for long-running projects that use conversational AI. The repository is the canonical source of truth for durable project knowledge. Chat conversations are working memory and MUST NOT be the only location of information whose loss would materially impair project continuity.

The keywords MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## 2. Core memory layer

Every initialized RPM project MUST have a memory root. The default is:

```text
docs/project-memory/
```

The Core consists of:

```text
PROJECT_STATE.md
NEXT_STEPS.md
DECISIONS.md
sessions/
```

### PROJECT_STATE.md

`PROJECT_STATE.md` is the current authoritative summary of the project. It SHOULD answer: "What would a competent agent need to know to continue this project if all chat history disappeared?"

It MUST prefer current truth over history. Stale state SHOULD be replaced rather than appended indefinitely.

### NEXT_STEPS.md

`NEXT_STEPS.md` contains actionable outstanding work, priorities, blockers, and deferred items. Completed items SHOULD be removed or moved to a historical record rather than left as active tasks.

### DECISIONS.md

`DECISIONS.md` records confirmed durable decisions, their rationale, and material rejected alternatives when useful. Speculative ideas MUST NOT be recorded as accepted decisions.

### sessions/

Session logs are concise checkpoint records. They MUST NOT be raw chat transcripts. A session file SHOULD be created only when meaningful work occurred. The recommended naming convention is `YYYY-MM-DD.md`; multiple same-day checkpoints MAY be appended to the same file.

## 3. State vocabulary

RPM uses the following status terms consistently:

- **Completed** — implementation or work has been performed.
- **Verified** — completion has been independently checked by tests, inspection, deployment evidence, or equivalent validation.
- **In Progress** — work has started but is not complete.
- **Planned** — work is approved and intended, but not started.
- **Proposed** — an option or idea under consideration and not yet accepted.
- **Blocked** — work cannot proceed until a stated dependency or condition changes.

A claim MUST NOT be upgraded from Completed to Verified without evidence.

## 4. Authority hierarchy

When sources conflict, RPM SHOULD reconcile them using this order:

1. Directly observed current repository state and current external system state relevant to the task.
2. Explicit, current user instruction.
3. Current RPM memory documents.
4. Older session logs and historical documents.
5. Conversational recollection or model memory.

If a conflict cannot be resolved safely, the uncertainty MUST be recorded instead of guessed.

## 5. Core invariants

An RPM implementation MUST:

- preserve durable project knowledge outside chat;
- avoid inventing implementation state;
- distinguish current state from history;
- avoid duplicating the same canonical fact across multiple files unless cross-reference is useful;
- load only the minimum additional profile material needed for the current task;
- preserve useful existing repository content when updating memory;
- keep project-specific facts in the consuming repository, not in the central RPM specification repository.

## 6. Lazy expansion

Profiles extend the Core. Optional profile files and directories SHOULD be created lazily, only when the information has durable value that is not well represented by the Core files.

Initialization MUST NOT create large trees of empty placeholder documentation.

## 7. Source-of-truth rule

Repository content is durable state. Chat is ephemeral state.

If an important fact exists only in chat and meets the persistence criteria in `PERSISTENCE.md`, it is not considered safely preserved until it has been written to the repository.
