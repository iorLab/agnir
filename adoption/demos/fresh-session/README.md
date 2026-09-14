# Fresh-session recovery demo

Status: canonical adoption demo scenario

This directory defines Agnir's primary 30-second fresh-session recovery demo. It is an adoption/product surface, not Agnir Core and not Project continuity storage.

## Product claim being demonstrated

> A fresh compatible Executor can recover the durable Project truth needed to continue without predecessor-private conversational context.

The demo should make one contrast obvious before it explains any protocol vocabulary:

- without Agnir, a fresh session has to reconstruct what happened;
- with Agnir, the Project supplies Current State, Next Actions, Decisions, and Evidence/Checkpoint context so work can continue.

Close with:

> **New session. Same Project continuity.**

## Scenario

Use one small, developer-readable task:

> Add a `version` field to `/api/health`, preserve the existing `status` field for compatibility, then add failure-path tests.

The first session completes the implementation and leaves the failure-path tests unfinished.

### Without Agnir

1. Session A receives the task and completes the implementation portion.
2. Session A ends.
3. A genuinely fresh Session B receives only `Continue.` / `继续。`.
4. Session B cannot know what work was in progress from predecessor-private context and asks what it was working on.

### With Agnir

1. Session A receives the same task and completes the same implementation portion.
2. The user reaches a meaningful stopping point and checkpoints the Project.
3. Session A ends.
4. A genuinely fresh Session B receives only `Continue.` / `继续。`.
5. Session B recovers the Project-owned durable truth:
   - Current State: `/api/health` now includes `version` and still returns `status`;
   - Next Action: add failure-path tests;
   - Decision: preserve backward compatibility for `status`.
6. Session B continues with the tests.

The value is continuation, not merely reciting memory.

## Canonical trace

`trace.json` is the deterministic presentation trace for this scenario. The public website consumes the same trace at build/runtime rather than maintaining an unrelated marketing script.

The trace is intentionally a presentation fixture. It does not assert that Agnir Core defines UI timing, chat wording, Agent output formatting, or a fixed `checkpoint` keyword parser.

## Presentation contract

Primary presentation:

- website hero demo;
- approximately 30 seconds;
- silent autoplay when motion preferences allow;
- visible pause/play and replay controls;
- responsive layout;
- reduced-motion mode does not autoplay;
- if the trace cannot load, the existing static without/with-Agnir comparison remains as a safe fallback.

Derived media such as MP4/WebM, GIFs, social clips, screenshots, or README images may be produced from this scenario, but they are not the canonical source.

## Acceptance criteria

A first-time viewer should be able to answer all of these after one playback:

1. What goes wrong in a fresh session without durable Project continuity?
2. What is different after Agnir is installed and checkpointed?
3. Does the new session receive a long human re-prompt? — **No.** It receives only `Continue.` / `继续。`.
4. Does Agnir merely remember chat? — **No.** The Project supplies durable state needed to continue the work.
5. What is the closing value statement? — **New session. Same Project continuity.**

Do not lead this demo with lineage selectors, mount-boundary behavior, compatibility promotion, conflict semantics, or other protocol-depth material. Those belong in later technical demos.