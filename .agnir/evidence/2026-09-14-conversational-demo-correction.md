# Conversational fresh-session demo correction

Date: 2026-09-14 (Project working timezone)

## Trigger

The first human visual review of the live canonical fresh-session demo did **not** accept the presentation.

The Principal's observed problem was specific:

> the expected experience was a dynamic Agent-chat process, but the implementation read as slide/card switching.

This is accepted product/adoption evidence. The v1 implementation had a correct high-level scenario and deterministic trace, but its presentation model did not communicate the intended value strongly enough.

## Diagnosis

The rejected implementation replaced the entire visible scene at timeline boundaries. Although technically animated, the user experienced a sequence of prepared cards rather than a live Agent working through a Project.

That distinction matters for the product claim. Agnir is meant to demonstrate continuation of real work across a fresh execution context, so the primary demo needs to visually preserve the causality of:

work -> tool activity -> checkpoint -> session end -> fresh transcript -> Agnir discovery/load -> continued work -> verification.

## Corrective contract

`adoption/demos/fresh-session/README.md` now explicitly requires the primary website demo to be a **continuous Agent-chat playback**, not a slide deck or independent scene cards.

The corrected implementation uses:

- one persistent generic Agent-workspace window;
- user and Agent messages appearing over time;
- visible streamed/typed Agent output;
- inline Read / Edit / Test / Agnir operations;
- natural transcript scrolling;
- a short without-Agnir cold-open only to establish the pain;
- an explicit Session A closure;
- a Fresh Session B with an empty predecessor-private transcript;
- only `Continue.` / `继续。` supplied by the user in the fresh session;
- visible Agnir discovery and loading of State / Next Actions / Decisions;
- continued implementation into the previously pending tests;
- successful verification before the closing value statement.

Only actual session boundaries and the final value statement use brief overlays.

## Implementation receipts

- correction branch: `adoption/conversational-demo-v2`;
- source commit: `423bc22410d0a225f185d9cc2eabe20c644bd361`;
- PR: `#52` — merged;
- authoritative merge: `e87e3a3eaf24d25ae209659f8764c59041b45f7e`;
- PR conformance: run `34810732745` — success;
- post-merge conformance: run `34810775853` — success;
- Pages publication: run `34810776075` — success;
- Pages build job: `103871507283` — success;
- Pages deploy job: `103871540152` — success;
- Pages artifact: `10335125320`;
- artifact digest: `sha256:1d5c069f64bbbadddc18966b4e477b2e90b2ebb33ca8a94593aa96bcccc24e9f`;
- merged-head cleanup: repository branch readback after merge contains only `main`.

Pre-merge syntax checks also passed for the exact JavaScript and JSON trace content.

## Protocol boundary

This correction is an adoption/public-presentation change only.

It does not change:

- Agnir Core `1.0`;
- `repository-filesystem/1.0`;
- checkpoint semantics;
- Project identity;
- Continuity Lineage semantics;
- compatibility/migration behavior;
- published release identity.

## Remaining observation

The corrected conversational v2 is deployed, but human visual acceptance remains distinct from CI and Pages deployment success.

The next observation is to review the actual live English and Simplified Chinese presentations on desktop/mobile and decide whether the demo now reads as one continuous Agent workflow rather than a slide sequence.
