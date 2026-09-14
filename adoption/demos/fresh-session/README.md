# Fresh-session recovery demo

Status: canonical adoption demo scenario

This directory defines Agnir's primary approximately-30-second fresh-session recovery demo. It is an adoption/product surface, not Agnir Core and not Project continuity storage.

## Product claim being demonstrated

> A fresh compatible Executor can recover the durable Project truth needed to continue without predecessor-private conversational context.

The demo must make one contrast obvious before it explains protocol vocabulary:

- without Agnir, a fresh session has to reconstruct what happened;
- with Agnir, the Project supplies Current State, Next Actions, Decisions, and Evidence/Checkpoint context so work can continue.

Close with:

> **New session. Same Project continuity.**

## Scenario

Use one small, developer-readable task:

> Add a `version` field to `/api/health`, preserve the existing `status` field for compatibility, then add failure-path tests.

The first session completes the implementation and leaves the failure-path tests unfinished.

### Without Agnir

A short cold-open is sufficient:

1. a genuinely fresh session receives only `Continue.` / `继续。`;
2. it has no predecessor-private context;
3. it asks what the user was working on.

This section establishes the pain but must not consume most of the demo.

### With Agnir

The main demo shows the full working handoff as one continuous Agent conversation:

1. Session A receives the real task.
2. The Agent visibly reads/edits Project files.
3. The implementation reaches a meaningful stopping point.
4. The user expresses checkpoint/save-progress intent.
5. Agnir visibly reconciles the durable Project truth.
6. Session A ends.
7. A genuinely fresh Session B starts with no predecessor-private chat history.
8. The user provides only `Continue.` / `继续。`.
9. The fresh Agent discovers Agnir, loads State / Next Actions / Decisions, explains what it recovered, then continues the unfinished work.
10. The Agent visibly edits the pending tests and verifies them successfully.

The value is continuation, not merely reciting memory.

## Canonical trace

`trace.json` is the deterministic presentation trace for this scenario. The public website consumes the same trace at runtime rather than maintaining an unrelated marketing script.

The trace is intentionally a presentation fixture. It does not assert that Agnir Core defines UI timing, chat wording, Agent output formatting, a fixed checkpoint keyword parser, or a specific execution-surface UI.

## Presentation contract

The primary presentation is a **continuous Agent-chat playback**, not a slide deck and not a sequence of scene cards.

Required behavior:

- website hero demo;
- approximately 30 seconds;
- one persistent generic Agent-workspace window;
- messages appear over time inside the same transcript;
- Agent replies visibly stream/type rather than appearing as finished cards;
- file reads, edits, Agnir discovery/checkpoint activity, and verification appear inline as lightweight tool-operation rows;
- the Session A -> Fresh Session B boundary is visually explicit;
- Fresh Session B begins with an empty private-chat transcript and receives only `Continue.` / `继续。`;
- the conversation scrolls naturally as new work appears;
- silent autoplay when motion preferences allow;
- visible pause/play and replay controls;
- responsive desktop/mobile layout;
- reduced-motion mode does not autoplay;
- if the trace cannot load, the server-rendered static without/with-Agnir comparison remains as a safe fallback.

Do **not** implement the primary demo as independent slides whose whole contents are replaced at scene boundaries. Session transitions may briefly use an overlay, but the actual work must read visually as a live conversation unfolding in a persistent Agent workspace.

Derived media such as MP4/WebM, GIFs, social clips, screenshots, or README images may be produced from this scenario, but they are not the canonical source.

## Acceptance criteria

A first-time viewer should be able to answer all of these after one playback:

1. What goes wrong in a fresh session without durable Project continuity?
2. What actual work did Session A complete?
3. What remained unfinished at the checkpoint?
4. Was Session B genuinely fresh? — **Yes.** Its private transcript starts empty.
5. What did the user tell Session B? — Only `Continue.` / `继续。`.
6. What did the fresh Agent recover from the Project?
7. Did it merely summarize the old state? — **No.** It continued into the pending test work and verified the result.
8. What is the closing value statement? — **New session. Same Project continuity.**

Do not lead this demo with lineage selectors, mount-boundary behavior, compatibility promotion, conflict semantics, or other protocol-depth material. Those belong in later technical demos.
