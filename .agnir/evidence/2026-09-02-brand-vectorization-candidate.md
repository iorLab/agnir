# Agnir brand vectorization candidate — 2026-09-02

Status: **branch-local candidate evidence; not canonical until reconciled and merged to authoritative `main`.**

## Locked source

The Principal-approved Today 10:42 AM Agnir board remains the sole Agnir-only visual authority. Its source SHA-256 and corrected extraction coordinates are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Candidate progress

A visual-QA pass discovered that several earlier extraction bounds were too tight and could clip the wordmark/lockup. The manifest was corrected before generating the next vector set.

Current review candidates:

- `brand/masters/candidates/agnir-mark-trace-v0.2.svg` — corrected raster-derived particle A with central anchor;
- `brand/masters/candidates/agnir-wordmark-trace-v0.2.svg` — corrected dense contour trace of the approved black standalone wordmark;
- `brand/masters/candidates/agnir-horizontal-lockup-v0.2.svg` — source-aligned horizontal assembly;
- `brand/masters/candidates/agnir-vertical-lockup-v0.2.svg` — source-aligned vertical assembly.

The superseded v0.1 mark/wordmark traces were removed from the active branch to prevent accidental use.

Local source-vs-render QA for the v0.2 particle mark produced SSIM of approximately `0.894`. This is supporting engineering evidence only; visual fidelity to the approved board remains the promotion criterion.

## Decision boundary

No ribbon-based A, replacement font, palette cleanup, particle-field redesign, or aesthetic reinterpretation is authorized. A technically valid SVG that drifts from the locked reference must be rejected.

The v0.2 lockups intentionally reference the candidate component SVGs. If the mark and wordmark are promoted, the lockups must be flattened/self-contained before production-master status.

## Next acceptable move

Principal review of the v0.2 mark / wordmark / horizontal / vertical set. If accepted, promote and flatten the masters, then reconstruct approved light/dark/monochrome and target-size derivatives.
