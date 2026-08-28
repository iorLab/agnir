# Agnir main-only branch cleanup checkpoint

Date: 2026-08-28

## Result

`iorLab/agnir` now uses **main-only branch governance**. GitHub branch enumeration after cleanup returned only `main`.

Verified pre-checkpoint baseline:

- `main`: `de10811149889cce5c3525e7b690c5e04d10d2e2`;
- conformance run `33157427784`: success;
- all former legacy, website, feature, temporary, release-pointer, and branch-capability-probe refs were deleted;
- retired RPM website PR #3 was closed without merge before its source branch was deleted;
- the one-shot cleanup workflow used to remove refs was deleted from `main` after use.

## Historical preservation

Before branch deletion, retired branch names and final tip SHAs were recorded in `history/BRANCH_ARCHIVE.md`. PPMP / PPM / Sandminni predecessor lineage is therefore recoverable by immutable commit SHA and Git history without retaining a live `legacy/*` branch.

Historical commits and `history/MIGRATION_PPMP_V2.md` are reference material only. They are not Agnir Core `0.1` semantics, compatibility obligations, conformance requirements, or release gates.

## Resume point

Continue from the current greenfield Agnir Core `0.1` line:

1. freeze Core compatibility and repository release notation from current contracts;
2. run the final current-architecture consistency review;
3. reconcile Svif's Continuity Provider binding to the current Core compatibility line;
4. decide release-candidate/stable readiness from the current architecture and conformance baseline.

Real mount-boundary behavior remains explicitly unproven.