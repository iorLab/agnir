# Persistence Rules

Version: 1.0.0

## 1. Persistence model

RPM uses event-driven persistence, not message-driven persistence. A repository checkpoint SHOULD occur when durable project state changes materially, not after every conversational turn.

## 2. Persist when

Persist information when one or more of the following occurs:

- a meaningful implementation or work milestone is completed;
- a completed item becomes verified;
- an architectural, product, editorial, research, or planning decision is confirmed;
- project status changes materially;
- a significant problem, root cause, or resolution is established;
- deployment, CI, infrastructure, schema, migration, configuration, or release state changes;
- a blocker, risk, dependency, or new next step is established;
- durable constraints or requirements become clear;
- important evidence changes the current understanding of the project;
- the user explicitly requests a checkpoint or indicates the work session is ending.

Typical explicit checkpoint phrases include "收尾", "结束", "先到这里", "checkpoint", "save progress", and equivalents.

## 3. Do not persist

Do not persist:

- casual discussion;
- raw chat transcripts;
- transient debugging chatter that has no durable conclusion;
- speculative ideas that remain unaccepted;
- abandoned intermediate approaches unless the rejection itself is important;
- duplicate facts already accurately represented in a canonical file;
- unverified claims presented as verified facts;
- secrets, credentials, tokens, private keys, or sensitive transient values.

## 4. Routing durable knowledge

Route information to the narrowest canonical location that fits:

| Information | Canonical destination |
| --- | --- |
| Current overall state | `PROJECT_STATE.md` |
| Outstanding work, priorities, blockers | `NEXT_STEPS.md` |
| Confirmed decision and rationale | `DECISIONS.md` |
| Important chronological checkpoint | `sessions/YYYY-MM-DD.md` |
| Domain-specific durable knowledge | Profile-defined artifact |

A session log MAY reference changes made to canonical files but SHOULD NOT become the only copy of current state.

## 5. Checkpoint procedure

Before writing a checkpoint:

1. Read the existing relevant canonical documents.
2. Reconcile new information with repository and external state.
3. Remove or replace stale statements when appropriate.
4. Preserve useful existing content.
5. Distinguish status using the RPM state vocabulary.
6. Write the smallest coherent set of updates.
7. Avoid creating redundant documents.
8. Record verification evidence when a claim is marked Verified.

## 6. Git behavior

Documentation-only RPM persistence MAY be committed directly when the project instructions authorize it.

Recommended commit messages include:

```text
docs: checkpoint project state
docs: record project decision
docs: update next steps
docs: record research findings
```

RPM persistence MUST NOT modify production code merely to create a documentation checkpoint. Code changes follow the normal development and validation workflow.

## 7. End-of-session behavior

When the user explicitly ends or pauses a substantive work session, the assistant SHOULD perform a final reconciliation:

- confirm whether durable state changed since the last checkpoint;
- persist missing durable knowledge if needed;
- ensure active next steps and blockers are current;
- report briefly which files changed and, if applicable, the commit SHA.

If no durable state changed, no repository write is required.

## 8. Session-log discipline

Session logs are evidence and chronology, not canonical current state.

A session log SHOULD contain only meaningful items such as:

- work completed;
- decisions made;
- findings or root causes;
- verification performed;
- remaining work;
- links or references to relevant commits, issues, PRs, or external evidence.

Multiple trivial session files SHOULD NOT be created merely because a conversation occurred.
