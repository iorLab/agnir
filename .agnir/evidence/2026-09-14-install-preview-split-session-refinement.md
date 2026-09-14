# Install preview split-session refinement — 2026-09-14

## Status

Accepted publication evidence; Principal visual review of the refined presentation remains pending.

## Principal direction

After reviewing the first Install-section conversation preview, the Principal requested two presentation refinements:

1. replace the single long chat window with two vertically stacked windows so it is visually obvious that a new session was opened;
2. strengthen the Simplified Chinese hero comparison caption from `两个新会话都只收到一句：“继续。”` to `两个新会话都只收到一句：“继续。” 但大有不同。`.

The equivalent contrast wording was also supplied for English and for Japanese/Korean static fallback presentation.

## Implemented result

PR `#55` implements the refinement as a public website presentation change only.

Install section:

- upper window: `Session A` / localized equivalent;
- lower window: `Fresh Session B` / localized equivalent;
- a localized “open a fresh session” divider separates the windows;
- Session A shows install/initialize intent and the Agent explaining that a fresh session only needs `Continue.` / `继续。`;
- Fresh Session B receives only that continuation prompt and shows the Agent loading Project state and continuing;
- both windows reuse the approved warm four-point Agent sparkle icon;
- the layout remains responsive and theme-aware;
- preview copy remains localized for English, Simplified Chinese, Japanese, and Korean.

Hero comparison:

- Simplified Chinese presentation adds `但大有不同。` after the existing fresh-session-prompt statement;
- English receives the equivalent contrast addendum;
- Japanese and Korean static fallbacks receive localized equivalent contrast copy;
- the canonical split-screen demo scenario semantics and deterministic trace remain unchanged.

## Receipts

- implementation PR: `#55`;
- implementation source head: `3c073e80ad87db9a11d2beb89f9e90d4d92f6482`;
- authoritative merge: `06749842054d612a64af46f5509f9baffe99da03`;
- PR conformance: run `34826216679` — success;
- post-merge conformance: run `34826272500` — success;
- Pages publication: run `34826272497` — build and deploy success;
- Pages build job: `103919066599` — success;
- Pages deploy job: `103919099750` — success;
- Pages artifact: `10340342962`;
- artifact digest: `sha256:1c48ae65668aa4f9f0ce81d706e91c964def43656367290b7025971dd051c0e0`.

## Direct artifact verification

The published Pages artifact was downloaded and inspected directly.

Confirmed:

- `theme.js` contains localized Session A / Fresh Session B labels for EN / zh-CN / JA / KO;
- `theme.js` contains the requested Simplified Chinese `但大有不同。` addendum and equivalent English/Japanese/Korean copy;
- published `install-chat.css` contains the split-window and new-session-divider rules;
- `install-chat-sessions.css` is present in the artifact;
- published `theme.js` passes `node --check`;
- published `demo.js` passes `node --check`.

## Boundary

This change is website/public-surface presentation only. It does not modify Agnir Core, repository/filesystem profile semantics, checkpoint behavior, Project identity, logical lineage, or the already accepted canonical split-screen demo gate.

## Next observation

Principal live visual review of the refined Install-section two-window presentation remains pending. If accepted, close only this public-surface polish item and continue external design-user adoption work.
