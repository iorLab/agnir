# Agnir brand production candidate — 2026-09-02

Status: **branch-local evidence; not canonical until reconciled and integrated into authoritative `main`.**

## Principal approval

The Principal reviewed the clean Agnir v0.3 source-vs-vector comparison and explicitly stated that the set had no material problem. That approval is the promotion gate for the current branch production masters; it does not authorize later visual reinterpretation.

## Promoted production masters

- `brand/masters/agnir-mark.svg`
- `brand/masters/agnir-wordmark.svg`
- `brand/masters/agnir-horizontal-lockup.svg`
- `brand/masters/agnir-vertical-lockup.svg`

The horizontal and vertical lockups are self-contained. v0.3 candidate files remain provenance/review evidence only; v0.2 and earlier are superseded.

## Materialized package exports

The branch now carries directly usable SVG package exports under `brand/exports/` for light, dark and monochrome horizontal treatments plus app-icon and favicon usage. These files reference `../masters/` so approved geometry is not forked into a second authority.

`brand/tools/build-production-derivatives.py` deterministically builds PNG delivery derivatives and the 32/16px visibility-pruned favicon sources from the approved masters.

## Small-size decision

The full particle field loses the A reading when naively reduced to 16px. The approved board itself shows a favicon-size family. Therefore 32px and 16px are allowed to prune only particles below fixed visibility thresholds; the A geometry, major particles, pale inner A and central anchor remain unchanged. This is a size derivative, not a new identity design.

## QA

Final local target-size QA was run on the three horizontal treatments, app icon and 128/64/32/16 favicon outputs. No material geometry change was introduced after Principal approval.

## Remaining integration boundary

Before canonical `main` integration, preserve the byte-exact approved 10:42 AM Agnir board in repository storage, re-resolve latest `main`, reconcile branch-local continuity, integrate coherently, and verify from authoritative `main`.
