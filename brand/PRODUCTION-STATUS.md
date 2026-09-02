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
- source-board extraction manifest corrected after QA found several earlier crop bounds were too tight;
- corrected primary-mark / wordmark / horizontal-lockup regions now preserve the approved content without clipping;
- `brand/masters/candidates/agnir-mark-trace-v0.2.svg` is the current particle-A review candidate, derived from the corrected approved primary-mark crop;
- `brand/masters/candidates/agnir-wordmark-trace-v0.2.svg` is the current black standalone wordmark review candidate, derived from the corrected approved wordmark crop;
- `brand/masters/candidates/agnir-horizontal-lockup-v0.2.svg` and `agnir-vertical-lockup-v0.2.svg` encode the current source-aligned candidate assemblies;
- superseded v0.1 mark/wordmark traces were removed from the active branch to prevent accidental use;
- `brand/tools/derive-raster-assets.py` provides the deterministic interim white-matte → transparent PNG / target-size raster path;
- raster derivation continues to preserve the approved Agnir appearance without pretending raster upscales are native masters.

## Current production gate

**v0.2 is ready for master-review, not yet a locked master.**

A vector master may be promoted only after visual comparison against the corrected approved crop. No new image generation, ribbon-based A replacement, typography substitution, palette reconciliation, particle-field redesign, or aesthetic cleanup is allowed.

### Current v0.2 review status

- Particle A: **best current vector candidate**. It preserves the approved discrete-particle hierarchy, pale inner A, outer field and central anchor. Automated source-vs-render SSIM during local QA is approximately `0.894`; that metric is supporting evidence only, not the approval criterion.
- Wordmark: **best current vector candidate**. It is a corrected dense contour trace of the actual approved black wordmark, not a substituted font.
- Horizontal lockup: **review candidate assembled and visually aligned** to the corrected approved horizontal region.
- Vertical lockup: **review candidate assembled and visually aligned** to the approved vertical region.
- Candidate lockups intentionally reference the candidate component SVGs at this stage; if/when promoted, they must be flattened/self-contained.
- Light/dark/monochrome vector variants remain blocked until the v0.2 primary mark and wordmark are accepted masters.

The quality rule remains: **absence of a locked master is preferable to a visually drifting master.**

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. The current connector does not provide a practical local-file binary upload bridge for the multi-megabyte exact approved PNG, so final byte-exact repository preservation remains a pre-`main` integration gate.

## Next actions

1. Run Principal visual review of Agnir v0.2 mark / wordmark / horizontal / vertical candidates against the locked board.
2. If accepted, promote the mark and wordmark to production masters and flatten the two lockups into self-contained SVGs.
3. Rebuild light-background, dark-background and monochrome variants from those locked masters while matching the approved examples.
4. Produce repository/app/favicon/social derivatives and target-size QA.
5. Preserve the byte-exact approved source in repository storage before final integration.
6. Re-resolve latest `main`, reconcile approved brand continuity, and integrate coherently only after the brand asset gate is complete.
