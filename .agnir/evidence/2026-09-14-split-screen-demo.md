# Synchronized split-screen fresh-session demo

Date: 2026-09-14

## Principal direction

After reviewing the conversational single-window v2, the Principal preferred the visual logic of the earlier static comparison: keep **Without Agnir** and **With Agnir** visible at the same time, but make both sides dynamic.

The accepted implementation direction was therefore:

- left window: Without Agnir;
- right window: With Agnir;
- one shared playback clock and controls;
- both sides receive the same initial Project task;
- both reach the same stopping point;
- both Fresh Session B instances receive only `Continue.` / `继续。`;
- the left side visibly stalls because durable Project continuity is missing;
- the right side discovers Agnir, recovers Project truth, continues the pending tests, and verifies the result.

This is a presentation/adoption decision. It does not redefine Agnir Core, the repository/filesystem profile, checkpoint semantics, Project identity, or Continuity Lineage behavior.

## Implementation

Implementation PR:

- PR: `#53` — `website: compare Agnir side by side`;
- implementation source head: `a74371b37f044af2837c7de3d4178f26cf299d8d`;
- authoritative merge: `64e61ad1f21d15362cedbfb8376ab1d0adb6343d`.

Canonical demo surfaces:

- `adoption/demos/fresh-session/README.md` — synchronized split-screen presentation contract;
- `adoption/demos/fresh-session/trace.json` — deterministic trace, schema `agnir.demo.split-screen/3`;
- `website/demo.js` — two-lane renderer on one shared clock;
- `website/demo.css` — simultaneous two-column desktop layout and stacked mobile layout.

The server-rendered static comparison remains the fallback if the dynamic trace cannot load.

## Verification

PR conformance:

- run: `34819370697` — success.

Post-merge conformance:

- run: `34819425531` — success.

GitHub Pages publication:

- run: `34819425549`;
- build job: `103897304068` — success;
- deploy job: `103897345459` — success.

Published Pages artifact:

- artifact id: `10338020626`;
- digest: `sha256:50ae43bdc8d18e5ab05057fee5406fbb6c7f9282eb585109de34a5dbb94501de`.

The published artifact was downloaded and inspected directly. It contains:

- `fresh-session-demo.json` with schema `agnir.demo.split-screen/3`;
- separate `without` and `with` event lanes;
- `demo.js` containing the split-lane renderer and shared playback clock;
- `demo.css` containing the two-column desktop layout and mobile stacking behavior.

The published `demo.js` also passes `node --check`.

## Accepted durable result

The canonical demo is now implemented and published as a synchronized dynamic comparison rather than a single-window narrative or slide/card sequence.

Human visual acceptance remains intentionally open. The next observation is for the Principal to review the live English and Simplified Chinese presentation and decide whether the side-by-side dynamic comparison now communicates Agnir's fresh-session value correctly.
