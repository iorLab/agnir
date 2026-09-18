# Website install-prompt copy icon refinement

Date: 2026-09-19

## Principal direction

Move the Agnir website install-prompt copy icon so it appears **before the prompt** rather than after it.

## Implemented result

The copy control now appears on the leading/left side of the prompt block on all localized website pages:

- English;
- Simplified Chinese;
- Japanese;
- Korean.

The DOM order also places the copy button before the prompt `pre`, so semantic/tab order matches the visual order rather than using CSS-only re-positioning.

Responsive layout was mirrored accordingly:

- desktop prompt padding reserves space on the left;
- mobile prompt padding reserves space on the left;
- copy-button positioning uses `left` rather than `right`;
- existing copy-to-checkmark behavior, labels, and clipboard fallback remain unchanged.

## Receipts

- implementation branch: `website/copy-icon-before-prompt`;
- implementation source head: `4ac47b0bd89af2d4cbe29fb381e255e10c8bf1ce`;
- implementation PR: `#62`;
- authoritative merge: `e038f4f8c6aded44b2b513d98ebb04564326dcfd`;
- PR conformance run: `35382160261` — success;
- post-merge conformance run: `35382206608` — success;
- Pages publication run: `35382206627` — success;
- Pages build job: `105720772360` — success;
- Pages deploy job: `105720824525` — success;
- Pages artifact: `10562442305`;
- Pages artifact digest: `sha256:549a7e018baa0633c37b6fa928abdcf350bf9ba393fff1fb0cf2d14490173367`.

## Semantic boundary

This is website/public-surface polish only.

Unchanged:

- Agnir Core `1.0`;
- `repository-filesystem/1.0`;
- Project identity;
- Continuity Lineage;
- checkpoint/reconciliation semantics;
- published stable release identity `v1.0.2`.
