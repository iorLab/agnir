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
- earlier clipped/debug-heavy v0.2 review evidence invalidated after Principal inspection;
- QA-safe crops corrected again, including a wider/cleaner primary-mark crop that excludes neighboring title text while retaining mark safety margin;
- `brand/tools/render-vector-review.py` now has two explicit modes: **clean review by default** and engineering-only `--diagnostic` bounds mode;
- `brand/masters/candidates/agnir-mark-trace-v0.3.svg` is the new particle-A candidate, rebuilt from the approved raster using direct multi-scale circle detection plus source-sampled particle colors;
- `brand/masters/candidates/agnir-wordmark-outline-v0.3.svg` is the new smooth outline candidate. It replaces the pixel-dense contour approach and stores only vector outlines, with no runtime font dependency;
- `agnir-horizontal-lockup-v0.3.svg` and `agnir-vertical-lockup-v0.3.svg` encode source-measured v0.3 component scale/spacing;
- v0.2 remains historical candidate evidence only and is not promoted;
- `brand/tools/derive-raster-assets.py` remains the deterministic interim raster-production path.

## Current production gate

**Agnir v0.3 is the current review candidate. It is not yet a locked master.**

The specific defects identified by the Principal in the previous review have been addressed at the QA/candidate level:

- blue artwork-bound boxes are no longer shown in Principal-facing review output; they exist only in explicit diagnostic mode;
- the wordmark no longer uses the jagged pixel-dense trace that produced black merged blobs at the `g` descender and in lockups;
- the particle A now recovers the broad outer field and discrete circle hierarchy much more faithfully than v0.2;
- horizontal/vertical lockups have been rebuilt from source-measured component bounding boxes rather than the earlier compressed assembly.

Remaining review is visual fidelity only. No candidate may be promoted merely because it renders cleanly.

The quality rule remains: **absence of a locked master is preferable to a visually drifting master.**

## QA validity rule

Principal approval uses a **clean review image** with no debug boxes or engineering overlays. Diagnostic artwork bounds are generated separately with `--diagnostic`. Both modes use `contain`, never crop/cover.

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. Final byte-exact repository preservation remains a pre-`main` integration gate.

## Next actions

1. Run Principal visual review on the clean Agnir v0.3 mark / wordmark / horizontal / vertical comparison.
2. If any shape/spacing mismatch remains, correct only what the locked source demonstrates and repeat clean QA.
3. If accepted, promote the v0.3 mark and wordmark to production masters and flatten the lockups into self-contained SVGs.
4. Rebuild light-background, dark-background and monochrome variants from the promoted masters while matching the approved examples.
5. Produce repository/app/favicon/social derivatives and target-size QA.
6. Preserve the byte-exact approved source in repository storage before final integration.
7. Re-resolve latest `main`, reconcile approved brand continuity, and integrate coherently only after the brand asset gate is complete.
