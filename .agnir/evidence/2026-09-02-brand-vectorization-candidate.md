# Agnir brand vectorization candidate — 2026-09-02

Status: **branch-local candidate evidence; not canonical until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Agnir board remains the sole Agnir-only visual authority. Its source SHA-256 and QA-safe extraction coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Candidate progress

Current committed candidates:

- `brand/masters/candidates/agnir-mark-trace-v0.2.svg` — particle-A candidate;
- `brand/masters/candidates/agnir-wordmark-trace-v0.2.svg` — dense contour wordmark candidate;
- `brand/masters/candidates/agnir-horizontal-lockup-v0.2.svg` — horizontal candidate assembly;
- `brand/masters/candidates/agnir-vertical-lockup-v0.2.svg` — vertical candidate assembly.

The superseded v0.1 mark/wordmark traces were removed from the active branch to prevent accidental use.

## Invalidated review evidence

The first Agnir v0.2 master-review sheet is **invalid evidence**. Principal inspection identified clipped/incomplete presentation: the wordmark descender/edge content and lockup output were not fully visible. The issue was in review cropping/viewBox/panel handling, not proof that the approved source itself lacked those parts.

The review system has therefore been corrected before any master decision:

- QA-safe source crops now include deliberate white margin;
- `brand/tools/render-vector-review.py` uses contain-only scaling;
- source and vector artwork bounds are explicitly checked/displayed;
- any artwork touching a review panel boundary invalidates the sheet.

## Current finding after unclipped review

Removing the presentation defects reveals genuine remaining candidate mismatch:

- the particle-A vector is still too narrow/dense relative to the approved source;
- wordmark contour fidelity remains under review, although the descender can now be displayed completely;
- horizontal lockup component scale/spacing still drifts from the approved source;
- vertical lockup is too narrow/compressed.

Therefore **v0.2 is not approved and must not be promoted to master**. The previous approximate SSIM evidence is secondary and cannot override this visual result.

## Decision boundary

No replacement font, redesigned A, palette cleanup, particle-field redesign, or aesthetic reinterpretation is authorized. A technically valid SVG that drifts from the locked reference must be rejected.

## Next acceptable move

Correct the v0.2 geometry/spacing against the QA-safe crops, generate a new unclipped review, and request Principal approval only after the review itself passes the no-clipping validity rule.
