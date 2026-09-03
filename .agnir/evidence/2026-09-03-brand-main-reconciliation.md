# Brand branch reconciliation with authoritative main — 2026-09-03

Status: **branch-local integration evidence; not canonical until brand integration reaches authoritative `main`.**

## First reconciliation during brand QA

During final brand QA, `brand/identity-system` was observed diverged from authoritative `main`: the branch carried the approved identity work but was behind by 88 commits because Core 0.2 Parallel Continuity work had advanced concurrently.

A reverse-sync PR (`#8`, `head=main`, `base=brand/identity-system`) absorbed authoritative `main` into the temporary brand branch without changing `main`.

- main observed: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`;
- pre-sync brand head: `c45cd4c4c4fe7bd2cffb0789e3be1c5fa1908843`;
- branch merge commit: `b00e0d7c544e74d4b0245569450ecebb271461d5`;
- post-sync result: **behind `main` = 0**.

This prevented the brand branch from shadowing newer canonical `AGNIR.yaml`, Current State, Next Actions, Decisions, release metadata and Core/profile work.

## Second reconciliation after authoritative RC acceptance

While brand integration gates were being closed, authoritative `main` advanced again by 15 commits and completed RC acceptance / Core 0.2 authoritative-main integration. A fresh comparison found:

- latest main: `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`;
- pre-reconcile brand head: `6ac35732ca58301b2fa8e9759a0ed8e7d4042dcd`;
- relation: brand ahead 84, **behind 15**;
- merge base: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.

A second reverse-sync PR (`#10`) was opened only as a conflict probe. GitHub reported it non-mergeable because both lines had touched repository documentation / continuity surfaces. The PR was closed unmerged; no conflict-side selection was allowed to overwrite newer main truth.

### Explicit tree reconciliation

The branch was reconciled with a Git-native two-parent commit instead:

- first parent: pre-reconcile brand `6ac35732ca58301b2fa8e9759a0ed8e7d4042dcd`;
- second parent: authoritative main `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`;
- base tree: exact latest-main tree `5bedbf190a49e01689280fdbd0a812a0d1b60347`;
- reconciled tree: `5e09b705519a36183859f8abc64870a39dc60ee7`;
- reconciliation commit: `714da79d7338e6d2c35d691da6003aa134ed902c`.

The reconciled tree deliberately started from latest `main` and overlaid only:

- the branch-local `brand/` tree;
- the six brand-specific evidence files under `.agnir/evidence/`.

It deliberately did **not** reuse stale branch copies of `AGNIR.yaml`, state, next actions, decisions, release/Core/profile contracts, README files or `REPOSITORY_TREE.md`.

### Documentation reapplication

Because the latest-main tree correctly won repository documentation conflicts, the brand-only repository-map entries then had to be reapplied minimally to that newer documentation.

A temporary one-off workflow inserted only:

- one `brand/` line into the compact repository tree in `README.md`;
- one `brand/` line into the compact repository tree in `README.zh-CN.md`;
- the `brand/` responsibility block into the current `REPOSITORY_TREE.md`.

The first workflow definition had invalid YAML indentation and created no job or repository mutation. The corrected run `33705830326` succeeded; bot commit `99d10f611577eff534594888e2b55be3b38005ce` applied the documentation-only patch. The temporary workflow was then removed.

## Current result

Post-reconciliation comparison reports `brand/identity-system` **ahead of latest `main` and behind by 0**, with merge base equal to `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`.

The remaining diff is brand-local: approved visual references, production masters/exports/tools, QA/handoff material, repository-map entries, and brand candidate evidence. Current authoritative Core 0.2 / RC-acceptance truth remains inherited from `main` rather than redefined by brand work.

Before brand publication, the branch must still re-resolve latest `main` once more because concurrent main development may continue. Large byte-exact binary preservation remains the other open integration gate.
