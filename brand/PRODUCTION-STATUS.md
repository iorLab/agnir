# Agnir brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Agnir board is the sole Agnir-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Completed

- concept exploration ended;
- approved visual reference locked by exact source SHA-256;
- rejected deterministic reconstruction removed from the active branch;
- source-board extraction manifest corrected again after Principal review exposed clipping/misleading bounds in the first v0.2 review sheet;
- QA-safe source crops now retain deliberate white margin around mark, wordmark and both lockups;
- `brand/tools/render-vector-review.py` now enforces contain-only review rendering and explicit artwork bounds;
- `brand/masters/candidates/agnir-mark-trace-v0.2.svg` and `agnir-wordmark-trace-v0.2.svg` remain the current committed component candidates;
- `agnir-horizontal-lockup-v0.2.svg` and `agnir-vertical-lockup-v0.2.svg` remain candidate assemblies only;
- `brand/tools/derive-raster-assets.py` remains the deterministic interim raster-production path.

## Current production gate

**Agnir v0.2 is not approved and is not ready for promotion.**

The earlier master-review sheet is invalid because source/vector panels were clipped or fitted into insufficient display bounds. The Principal correctly identified missing descender/edge content and incomplete lockup rendering.

After rebuilding the review with QA-safe crops, explicit margins and contain-only scaling, real candidate mismatches are easier to see:

- particle A: the current vector construction is narrower/denser than the approved source in several rows and still needs proportion correction;
- wordmark: no longer visually clipped in the corrected review path, but contour fidelity still requires review;
- horizontal lockup: component scale and spacing do not yet match the approved source closely enough for master promotion;
- vertical lockup: the current vector assembly is too narrow/compressed relative to the approved source;
- therefore light/dark/monochrome vector variants remain blocked.

The quality rule remains: **absence of a locked master is preferable to a visually drifting master.**

## QA validity rule

A review image is invalid if approved artwork or rendered vector artwork touches the review panel boundary. Review must use `contain`, never crop/cover. Presentation defects must be fixed before any brand judgment is requested.

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. Final byte-exact repository preservation remains a pre-`main` integration gate.

## Next actions

1. Correct particle-A width, row spacing and outer-particle distribution using the QA-safe primary-mark crop.
2. Re-run the wordmark against the QA-safe source without descender clipping.
3. Rebuild horizontal and vertical lockups from the corrected component candidates using approved source proportions and spacing.
4. Generate a new unclipped source-vs-vector QA sheet using `brand/tools/render-vector-review.py`.
5. Request Principal master review only after every panel passes the no-clipping validity check.
6. If accepted, promote/flatten masters and then build light/dark/monochrome, icon, favicon and social derivatives.
7. Before final integration, preserve the byte-exact approved source, re-resolve latest `main`, reconcile Agnir continuity, and integrate coherently.
