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

Both sides begin from the same Project task and the same stopping point. The comparison is intentionally synchronized so the viewer can see that the user workflow is nearly identical while the fresh-session outcome diverges.

### Without Agnir

1. Session A receives the task and completes the endpoint change.
2. The user says to stop/save at the same point used on the Agnir side.
3. Session A ends without Project-owned continuity.
4. A genuinely fresh Session B receives only `Continue.` / `继续。`.
5. The fresh Agent has no durable Project state describing the previous session and asks the user to reconstruct the context.

### With Agnir

1. Session A receives the same task and completes the same endpoint change.
2. The user expresses the same stop/save-progress intent.
3. Agnir reconciles the durable Project truth at that boundary.
4. Session A ends.
5. A genuinely fresh Session B receives only `Continue.` / `继续。`.
6. The fresh Agent discovers Agnir, loads State / Next Actions / Decisions, recovers the pending failure-path tests, and continues the work.
7. The Agent edits the tests and verifies them successfully.

The value is continuation, not merely reciting memory.

## Canonical trace

`trace.json` is the deterministic presentation trace for this scenario. The public website consumes the same trace at runtime rather than maintaining an unrelated marketing script.

The trace is intentionally a presentation fixture. It does not assert that Agnir Core defines UI timing, chat wording, Agent output formatting, a fixed checkpoint keyword parser, or a specific execution-surface UI.

## Presentation contract

The primary presentation is a **synchronized split-screen comparison**:

- left window: **Without Agnir**;
- right window: **With Agnir**;
- both windows are visible at the same time on desktop;
- both use one shared playback clock and controls;
- both begin with the same task and reach the same stopping point;
- both fresh sessions receive only `Continue.` / `继续。`;
- the difference after that identical prompt must be visually immediate.

Each side is still a continuous Agent-chat playback, not a slide deck.

Required behavior:

- website hero demo;
- approximately 30 seconds;
- two persistent generic Agent-workspace windows on desktop;
- stacked windows on narrow/mobile layouts, preserving Without-then-With order;
- messages appear over time inside each transcript;
- Agent replies visibly stream/type rather than appearing as finished cards;
- file reads, edits, Agnir checkpoint/discovery activity, and verification appear inline as lightweight tool-operation rows;
- the Session A -> Fresh Session B boundary is visually explicit in both windows;
- Fresh Session B begins with an empty predecessor-private transcript on both sides;
- the user provides only `Continue.` / `继续。` to both fresh sessions;
- the Without-Agnir side visibly stalls on missing context;
- the With-Agnir side visibly recovers Project truth and continues into the pending tests;
- the conversation scrolls naturally as new work appears;
- silent autoplay when motion preferences allow;
- shared visible pause/play and replay controls;
- responsive desktop/mobile layout;
- reduced-motion mode does not autoplay;
- if the trace cannot load, the server-rendered static without/with-Agnir comparison remains as a safe fallback.

Do **not** turn either side into independent full-window slides whose contents are replaced merely to explain the story. A transcript reset is allowed only when representing the actual creation of Fresh Session B.

Derived media such as MP4/WebM, GIFs, social clips, screenshots, or README images may be produced from this scenario, but they are not the canonical source.

## Acceptance criteria

A first-time viewer should be able to answer all of these after one playback:

1. Are Without Agnir and With Agnir being compared side by side? — **Yes.**
2. Did both sides receive the same initial Project task? — **Yes.**
3. Did both sides reach the same stopping point? — **Yes.**
4. Were both Session B instances genuinely fresh? — **Yes.** Their private transcripts start empty.
5. What did the user tell each fresh session? — Only `Continue.` / `继续。`.
6. What happened without Agnir? — The Agent needed the human to reconstruct context.
7. What happened with Agnir? — The Agent recovered Project-owned durable truth and continued the pending work.
8. Did the Agnir side merely summarize the old state? — **No.** It continued into the pending test work and verified the result.
9. What is the closing value statement? — **New session. Same Project continuity.**

Do not lead this demo with lineage selectors, mount-boundary behavior, compatibility promotion, conflict semantics, or other protocol-depth material. Those belong in later technical demos.
