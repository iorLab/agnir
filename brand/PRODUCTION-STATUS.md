# Agnir brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Agnir board is the sole Agnir-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Approved production master

The Principal reviewed the clean Agnir v0.3 source-vs-vector sheet and explicitly accepted the set as having no material visual problem.

The following files are therefore the **branch-approved production masters**:

- `brand/masters/agnir-mark.svg` — particle-built A with central anchor;
- `brand/masters/agnir-wordmark.svg` — smooth outline wordmark, no runtime font dependency;
- `brand/masters/agnir-horizontal-lockup.svg` — self-contained horizontal composition;
- `brand/masters/agnir-vertical-lockup.svg` — self-contained vertical composition.

The v0.3 candidate files remain provenance/review evidence only. v0.2 and earlier work are superseded and must not be used as production masters.

## Materialized production exports

Directly usable package-level SVG exports now exist under `brand/exports/`:

- `agnir-horizontal-light.svg`;
- `agnir-horizontal-dark.svg`;
- `agnir-horizontal-monochrome.svg`;
- `agnir-app-icon.svg`;
- `agnir-favicon.svg`.

These exports deliberately reference `../masters/` instead of duplicating the approved geometry. Their job is treatment/canvas packaging only; `brand/masters/` remains the single geometry authority. Keep the relative `brand/exports/` + `brand/masters/` package layout intact when using these files.

`brand/tools/build-production-derivatives.py` remains the deterministic builder for PNG delivery exports and for the visibility-pruned 32/16px favicon sources.

### Approved derivative rules

- light-background horizontal treatment: brand-color wordmark with the approved particle A;
- dark-background horizontal treatment: white wordmark with the approved particle A;
- monochrome treatment: grayscale mark plus black wordmark;
- app-icon treatment derived from the approved mark;
- favicon exports at 128/64/32/16px.

### Small-size rule

Directly shrinking the full particle field to 16px loses the A reading. The approved board itself defines a favicon-size family, so 32px and 16px exports use a deterministic visibility derivative of the same master: only particles below a fixed rendered-visibility threshold are pruned. The A geometry, major particles, pale inner A and central anchor are unchanged. This is a size derivative, not a new logo design.

## QA status

Final local target-size QA has been completed across:

- light / dark / monochrome horizontal treatments;
- app icon;
- 128 / 64 / 32 / 16 favicon targets.

The approved production masters remain unchanged through this derivative pass. The complete local delivery package includes manifests/hashes and the clean QA sheet.

## QA rules

- Principal-facing review is clean: no blue bounds boxes or debug overlays.
- Engineering diagnostics may show bounds only under explicit diagnostic mode.
- Review/render uses `contain`, never crop/cover.
- No derivative may modify the approved core geometry.

## Binary reference boundary

The byte-exact approved 10:42 AM source board remains locked by SHA-256 and preserved in the reference package. Final byte-exact source-board repository preservation remains a pre-`main` integration gate.

## Remaining integration gates

1. Preserve the byte-exact approved Agnir board in repository storage.
2. Materialize any desired PNG delivery exports/social/repository-avatar derivatives through a byte-preserving path and verify hashes; the SVG package is already directly usable.
3. Re-resolve latest `main` and reconcile branch-local Agnir continuity.
4. Integrate the approved brand package coherently.
5. Verify authoritative `main` after publication.
