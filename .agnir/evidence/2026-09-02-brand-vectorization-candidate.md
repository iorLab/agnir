# Agnir brand vectorization evidence — 2026-09-02

Status: **branch-local approved brand evidence; not canonical Project truth until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Agnir board remains the sole Agnir-only visual authority. Source SHA-256 and QA-safe crop coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Superseded work

- v0.2 review evidence was invalidated because of clipped/debug-heavy presentation and genuine vector mismatch.
- v0.2 and earlier candidates are not production assets.
- the pixel-dense wordmark trace that created merged black blobs is superseded.

## v0.3 approval

The v0.3 clean review separated Principal-facing review from engineering diagnostics and presented the mark, wordmark, horizontal lockup and vertical lockup without crop/debug artifacts.

The Principal reviewed that clean set and stated that the set had no material problem. This is the approval event for promotion.

Promoted production files:

- `brand/masters/agnir-mark.svg`;
- `brand/masters/agnir-wordmark.svg`;
- `brand/masters/agnir-horizontal-lockup.svg`;
- `brand/masters/agnir-vertical-lockup.svg`.

The horizontal and vertical production lockups are self-contained rather than external component references.

## Derivative rule

All light/dark/monochrome, app-icon, favicon, repository/avatar and social derivatives must be generated from the promoted masters and the applicable approved-board examples. No replacement font, regenerated A, palette cleanup, particle redesign or aesthetic reinterpretation is authorized.

For 32px and 16px favicon targets, low-visibility micro-particles may be pruned deterministically because the approved board defines a small-size family and the complete particle field becomes unreadable at those raster sizes. Major particles, A geometry, pale inner A and central anchor remain unchanged.

## QA-system decision

- clean Principal review contains no blue bounds boxes or diagnostic overlays;
- engineering bounds are explicit diagnostic-only output;
- all review placement uses contain-only scaling;
- a technically valid derivative that drifts from the approved reference must still be rejected.

## Next acceptable move

Complete the derivative/export package, run target-size QA, write the brand handoff, preserve the byte-exact approved board in repository storage, then reconcile this approved branch-local evidence into the latest canonical `main` during integration.
