# Agnir brand vectorization candidate — 2026-09-02

Status: **branch-local candidate evidence; not canonical until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Agnir board remains the sole Agnir-only visual authority. Its source SHA-256 and QA-safe extraction coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Superseded v0.2 review

The first Agnir v0.2 master-review sheet is invalid evidence. Principal inspection identified clipped/incomplete presentation and debug artifacts. A subsequent unclipped diagnostic review also revealed real candidate mismatch: a narrow/dense particle A, jagged wordmark contours, and compressed lockup proportions.

Therefore **v0.2 is not approved and must not be promoted to master**.

## Current v0.3 candidate set

- `brand/masters/candidates/agnir-mark-trace-v0.3.svg` — particle-A candidate rebuilt from the locked raster with direct multi-scale circle detection and source-sampled particle colors. The broader outer particle field and circle hierarchy are recovered instead of approximated by block geometry.
- `brand/masters/candidates/agnir-wordmark-outline-v0.3.svg` — smooth outline reconstruction fitted against the locked raster wordmark. It intentionally avoids the previous pixel-dense trace and has no runtime font dependency.
- `brand/masters/candidates/agnir-horizontal-lockup-v0.3.svg` — source-measured horizontal assembly.
- `brand/masters/candidates/agnir-vertical-lockup-v0.3.svg` — source-measured vertical assembly.

The previous v0.2 candidate files remain branch history / comparison evidence only.

## QA-system decision

Principal-facing review and engineering diagnostics are now separate products:

- normal `brand/tools/render-vector-review.py` output is **clean review** with no blue bounds boxes, crop boxes, or debug overlays;
- `--diagnostic` is engineering-only and may draw detected artwork bounds;
- both modes use contain-only scaling;
- debug information must never obscure or visually compete with the brand artwork being approved.

The primary-mark crop was also widened/cleaned again so review does not include neighboring title text while retaining safe margin.

## Decision boundary

No regenerated A, replacement wordmark design, palette cleanup, particle-field redesign, or aesthetic reinterpretation is authorized. The v0.3 wordmark construction may use a geometric outline template internally, but the approved raster remains the authority and the committed result is outline geometry only; no inferred font identity is canonical.

A technically valid SVG that drifts from the locked reference must still be rejected.

## Next acceptable move

Run Principal clean review of the v0.3 component/lockup set. Correct only mismatches demonstrated by the locked source. If accepted, promote/flatten masters and continue to light/dark/monochrome, icon, favicon and social derivatives.
