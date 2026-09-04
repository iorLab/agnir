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

The branch carries directly usable SVG package exports under `brand/exports/` for light, dark and monochrome horizontal treatments plus app-icon and favicon usage. These files reference `../masters/` so approved geometry is not forked into a second authority.

`brand/tools/build-production-derivatives.py` deterministically builds PNG delivery derivatives and the 32/16px visibility-pruned favicon sources from the approved masters.

## Small-size decision

The full particle field loses the A reading when naively reduced to 16px. The approved board itself shows a favicon-size family. Therefore 32px and 16px are allowed to prune only particles below fixed visibility thresholds; the A geometry, major particles, pale inner A and central anchor remain unchanged. This is a size derivative, not a new identity design.

## Complete QA

The earlier derivative-only final QA was incomplete and is superseded. The branch now uses the same 13-item final QA contract as Svif:

1. mark;
2. wordmark;
3. horizontal lockup;
4. vertical lockup;
5. light usage;
6. dark usage;
7. monochrome usage;
8. app icon;
9. favicon 128;
10. favicon 64;
11. favicon 32;
12. favicon 16;
13. social card.

`brand/qa/FINAL-QA.md` records the complete branch-local QA scope and hashes. No approved master geometry changed during this QA completion pass.

## Repository-documentation synchronization

The new top-level `brand/` product surface is represented in both repository documentation layers:

- `REPOSITORY_TREE.md` includes the brand directory and responsibilities;
- `README.md` and `README.zh-CN.md` compact repository trees both include `brand/`.

The compact-tree update was applied by a one-off GitHub Actions workflow; run `33704897307` completed successfully, and the temporary workflow file was removed afterward.

## Integration validation

A one-off workflow validated the actual brand branch with the repository's canonical conformance commands:

- `python conformance/check_agnir_0_1.py`;
- `python -m unittest discover -s conformance -p 'test_*.py' -v`.

Run `33705053591` completed successfully. The temporary validation workflow was removed afterward.

## Main reconciliation

During final QA the branch was reconciled with the newer authoritative Core 0.2 / Parallel Continuity mainline before integration work continued. The newer canonical `AGNIR.yaml`, state, next actions, decisions and Core/release truth must remain authoritative; brand evidence remains branch-local until final publication.

## Remaining integration boundary

Before canonical `main` integration:

1. preserve the byte-exact approved 10:42 AM Agnir board and desired large PNG delivery derivatives through a byte-preserving repository path;
2. re-resolve latest `main` immediately before publication and reconcile again if it moved;
3. integrate coherently without replacing newer Core 0.2 continuity/release truth;
4. verify authoritative `main` after publication.

Visual design, approved production masters, 13/13 QA, repository documentation and branch validation are complete. The remaining blocker is large byte-exact binary preservation plus the final latest-main reconciliation.
