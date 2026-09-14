# Install conversation preview publication

Date: 2026-09-14
Status: published; Principal live visual review pending

## Context

The Principal requested that the website's **Install first / 先安装** section gain a compact Agent conversation illustration in the open space to the right of the install prompt, matching the approved dark warm-mineral mockup direction. The Principal also explicitly requested that the dynamic fresh-session demo reuse the same Agent icon.

## Implemented result

PR `#54` publishes the install conversation preview as a native website component rather than as a raster screenshot:

- desktop: install heading / prompt / microcopy remain on the left; the Agent conversation preview occupies the right column;
- narrow/mobile: the preview stacks below the install copy;
- preview copy is localized for English, Simplified Chinese, Japanese, and Korean;
- dark and light themes are supported;
- the conversation window uses the approved warm four-point sparkle treatment for Agent identity;
- the dynamic fresh-session demo Agent avatars now use the same sparkle icon instead of the letter `A`;
- `website/install-chat.css` owns the new presentation styles;
- `.github/workflows/pages.yml` publishes that stylesheet into the Pages artifact.

The website component is a public-presentation surface only. It does not redefine Agnir Core, checkpoint semantics, Project ownership, or the accepted split-screen demo scenario.

## Receipts

- implementation source head: `09c66f9b9aecf452241970bebb670fe9ea44e111`;
- implementation PR: `#54` — merged;
- authoritative merge: `a285c8868ae65ab2759b8f9b88572fd47f359161`;
- PR conformance: run `34824713563` — success;
- post-merge conformance: run `34824764737` — success;
- Pages publication: run `34824764786` — build and deploy success;
- Pages build job: `103914219408` — success;
- Pages deploy job: `103914266875` — success;
- Pages artifact: `10340210569`;
- artifact digest: `sha256:a36d2fc1712a1dac1bd6137ec5d3202b4480933d259f22b2131524390395c761`.

## Published-artifact verification

The actual Pages artifact was downloaded and inspected after deployment.

Observed publication result:

- `install-chat.css` is present in the published site artifact;
- `theme.js` contains the localized install preview injector and Agent sparkle markup;
- `demo.js` uses `demo-avatar agent-spark-icon` for Agent messages;
- published `theme.js` passes `node --check`;
- published `demo.js` passes `node --check`.

## Pending observation

Principal live visual review of the new Install-section preview is still pending. Until that observation is supplied, the implementation is accepted as published/verified but not yet human-visually accepted.

This pending review does **not** reopen the already accepted synchronized split-screen fresh-session demo v3 visual gate.
