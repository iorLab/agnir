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

## Production derivatives

Approved-board derivative work is now active from the locked masters only:

- light-background horizontal treatment: brand-color wordmark with the approved particle A;
- dark-background horizontal treatment: white wordmark with the approved particle A;
- monochrome treatment: grayscale mark plus black wordmark;
- app-icon treatment derived from the approved mark;
- favicon exports at 128/64/32/16px.

### Small-size rule

Directly shrinking the full particle field to 16px loses the A reading. The approved board itself defines a favicon-size family, so 32px and 16px exports use a deterministic visibility derivative of the same master: only particles below a fixed rendered-visibility threshold are pruned. The A geometry, major particles, pale inner A and central anchor are unchanged. This is a size derivative, not a new logo design.

## QA rules

- Principal-facing review is clean: no blue bounds boxes or debug overlays.
- Engineering diagnostics may show bounds only under explicit diagnostic mode.
- Review/render uses `contain`, never crop/cover.
- No derivative may modify the approved core geometry.

## Binary reference boundary

The byte-exact approved 10:42 AM source board remains locked by SHA-256 and preserved in the reference package. Final byte-exact source-board repository preservation remains a pre-`main` integration gate.

## Next actions

1. Persist the current light/dark/monochrome and app/favicon exports with hashes.
2. Build the approved social-card derivative and repository/avatar package from the production masters.
3. Run final target-size QA across the complete Agnir asset package.
4. Write `brand/brand-handoff.md` with canonical usage rules and file map.
5. Preserve the byte-exact approved board in repository storage before final integration.
6. Re-resolve latest `main`, reconcile Agnir continuity, then integrate the brand package coherently.
