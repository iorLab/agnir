# Persistence Rules

Version: 2.0.0

## 1. Model

iorMemory uses event-driven persistence. A checkpoint SHOULD occur when durable project state changes materially, not after every conversational turn.

## 2. Persist when

Persist when a meaningful milestone is completed or verified; a durable decision is confirmed; project status, deployment, schema, configuration, or release state changes materially; a significant problem or resolution is established; a blocker, risk, dependency, requirement, or next step becomes durable; important evidence changes current understanding; or the user explicitly requests a checkpoint/end-of-session save.

## 3. Do not persist

Do not persist casual discussion, raw transcripts, transient debugging chatter without a durable conclusion, unaccepted speculation, redundant facts, unverified claims presented as verified, or secrets/credentials.

## 4. Routing

Route information to the narrowest canonical semantic destination: Current State, Next Steps, Decisions, Checkpoint History, or a profile-defined durable concept.

## 5. Checkpoint procedure

Before a checkpoint, read the relevant current durable state, reconcile it with observed reality, replace stale statements, preserve useful content, apply the state vocabulary accurately, write the smallest coherent update, and record verification evidence for Verified claims.

## 6. Storage transactions

An implementation SHOULD make a checkpoint atomic when its backend supports atomic writes or transactions. It MUST NOT claim persistence succeeded until the backend confirms the durable write.

Version-control commits, database transactions, document revisions, and API writes are implementation/backend behavior rather than protocol requirements.

## 7. End-of-session behavior

When a user explicitly ends or pauses substantive work, an implementation SHOULD reconcile whether durable state changed since the last checkpoint, persist missing durable knowledge, and ensure active next steps/blockers are current. If nothing durable changed, no write is required.

## 8. Checkpoint-history discipline

Checkpoint History is evidence and chronology, not canonical current state. It SHOULD record only meaningful work, decisions, findings, verification, remaining work, and useful references. It MUST NOT be a raw conversation archive.
