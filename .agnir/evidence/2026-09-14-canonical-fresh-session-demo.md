# Canonical fresh-session demo acceptance

Date: 2026-09-14 (Project working timezone)

## Intent

The Principal approved implementation of Agnir's primary 30-second fresh-session recovery demo as a website autoplay experience backed by a real, repository-owned reproducible scenario rather than an unrelated marketing video.

The accepted presentation architecture is:

```text
canonical scenario + deterministic trace
                ↓
        website demo player
          ↓             ↓
       README         derived media
```

Derived video/GIF/social assets may be produced later, but they are not the canonical source.

## Canonical scenario

The durable adoption source is:

- `adoption/demos/fresh-session/README.md`;
- `adoption/demos/fresh-session/trace.json`.

The scenario uses a small developer-readable task: add a `version` field to `/api/health`, preserve `status` compatibility, then add failure-path tests. The first session completes the implementation portion and leaves the tests pending.

Without Agnir, a genuinely fresh second session receives only `Continue.` / `继续。` and cannot recover predecessor-private context. With Agnir, Session A checkpoints the Project; the fresh Session B receives the same minimal continue intent, recovers Current State / Next Action / Decision truth from the Project, and continues with the tests.

The closing message is:

> **New session. Same Project continuity.**

## Implementation

PR `#51` implemented the demo on branch `adoption/fresh-session-demo`.

Accepted PR head:

`71026db59f1a83f27dac3f73d21f4c226421da54`

PR conformance:

- run: `34808633866`;
- conclusion: **success**.

The PR was squash-merged to authoritative `main` as:

`226ac6f502e4fefc1a3bbb10472802d83ef51c03`

The implementation adds:

- `website/demo.js` — trace-driven autoplay/pause/replay player;
- `website/demo.css` — responsive presentation;
- dynamic loading from `website/theme.js` so the existing server-rendered static comparison remains a safe fallback;
- reduced-motion behavior that does not autoplay;
- English and Simplified Chinese trace copy;
- Pages packaging of the canonical trace as `fresh-session-demo.json`.

This is an adoption/public-surface implementation and does not modify Agnir Core/profile semantics.

## Post-merge conformance

Authoritative-main conformance after merge:

- run: `34808679959`;
- conclusion: **success**.

## Pages publication

Pages workflow:

- run: `34808679937`;
- head: `226ac6f502e4fefc1a3bbb10472802d83ef51c03`;
- build job: `103865504185` — **success**;
- deploy job: `103865531573` — **success**.

Published Pages artifact:

- artifact id: `10333823384`;
- name: `github-pages`;
- digest: `sha256:15bd2907feec1ab772f7484fe040f42fb0b717db0e6c91c45240f013050b1fab`.

## Artifact verification

The actual workflow artifact was downloaded and inspected after deployment.

It contains the required public files, including:

- `demo.js`;
- `demo.css`;
- `fresh-session-demo.json`;
- `index.html`;
- `zh-CN.html`;
- the existing language/theme and brand assets.

The published trace was parsed successfully and verified as:

- schema: `agnir.demo.fresh-session/1`;
- duration: `30000` ms;
- 8 contiguous timeline scenes;
- first scene: `without-work`;
- final scene: `close`;
- localized copy present for `en` and `zh-CN`.

`node --check` succeeded for the published `demo.js` and `theme.js`.

## Observation boundary

The following are now accepted:

- canonical scenario source exists;
- deterministic trace exists;
- PR and post-merge conformance are green;
- Pages build and deployment succeeded;
- the actual published artifact contains the required demo resources;
- trace structure and JavaScript syntax were independently rechecked from the publication artifact.

Human visual presentation review remains a separate observation. It should verify the live English and Simplified Chinese experience on desktop/mobile, playback controls, responsive behavior, and reduced-motion/fallback presentation. A visual defect would be a public-surface defect to repair; it would not by itself reopen Agnir Core/profile release gates.

## Accepted result

The canonical 30-second fresh-session demo is implemented and published. The previous next action to "produce the canonical 30-second fresh-session demo" is therefore satisfied at the implementation/publication level.

The adoption sequence now advances to live visual QA followed by external design-user recruitment and genuine external cold-start evidence.
