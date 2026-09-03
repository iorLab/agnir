# Agnir brand production status

Date: 2026-09-03
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked visual authority

The Principal-approved Today 10:42 AM Agnir board remains the sole Agnir-only visual authority. Its byte-exact repository copy is now `brand/reference/agnir-approved-reference.png`, locked to SHA-256 `24b418a975369ea022db229aaa45e1a4993e982f8d4baec16c918a1a0a4b99ac`.

The byte-exact family board is committed at `brand/reference/svif-agnir-family-approved-reference.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Approved production masters

The Principal reviewed Agnir v0.3 and explicitly accepted the set as having no material visual problem. Branch-approved scalable masters remain:

- `brand/masters/agnir-mark.svg`
- `brand/masters/agnir-wordmark.svg`
- `brand/masters/agnir-horizontal-lockup.svg`
- `brand/masters/agnir-vertical-lockup.svg`

Candidate files remain provenance only; v0.2 and earlier are superseded.

## Materialized exports

Direct SVG treatment exports remain under `brand/exports/`:

- `agnir-horizontal-light.svg`
- `agnir-horizontal-dark.svg`
- `agnir-horizontal-monochrome.svg`
- `agnir-app-icon.svg`
- `agnir-favicon.svg`

The complete 13-item PNG delivery package is now committed under `brand/exports/png/`:

- mark;
- wordmark;
- horizontal and vertical lockups;
- light / dark / monochrome usage;
- app icon;
- favicon 128 / 64 / 32 / 16;
- social card.

`brand/masters/` remains the vector geometry authority. PNG files are delivery derivatives, not replacement masters.

`brand/tools/build-production-derivatives.py` remains the deterministic builder. The approved 32/16px favicon rule may prune only sub-threshold micro-particles; the A geometry, major particles, pale inner A and central anchor remain unchanged.

## Complete QA

Final QA is symmetric with Svif and covers 13/13 items. Complete QA sheet SHA-256: `145ab94e4458cdd9165bd61ceed71e4a12302b7cb71077443414ee8683302cfa`.

The approved production masters were unchanged by the derivative/materialization work.

## Byte-exact materialization

The former large-binary gate is **closed**.

The Principal uploaded the prepared handoff archive directly to the branch. The archive was observed as the same Git blob in both repositories and was verified as:

- size `7,925,506` bytes;
- SHA-256 `52e8cee3c03f0762fc47d579505122dc452e5de97dafb462a3b470ed5457f72d`;
- Git blob `3f49c176a5c5680620de6f4de09beb6297f99bf0`.

GitHub Actions run `33730501685` then verified the archive SHA, verified each Agnir source payload SHA, copied all 15 Agnir targets to final repository paths, re-verified every destination SHA, committed the package, and removed both the transport ZIP and temporary workflow.

Final materialization commit: `a858de5c2d12f800ef6d9057f28422320ff5a012`.

## Latest main reconciliation

The branch has been reconciled repeatedly because authoritative `main` continued moving during brand work.

The latest pre-materialization check found:

- authoritative `main`: `3564a4dd1485d3be29052f9698356202685ab31d`;
- pre-reconcile brand head after browser upload: `042de482059df030e4c462c9ee3c517137d2db0c`;
- relation: brand behind main by 9 commits.

Reverse-sync PR `#13` was used as a conflict probe and was not resolved by selecting stale branch-side canonical files. Instead a latest-main-wins two-parent reconciliation was constructed:

- latest-main base tree: `e883044b6263dd56ae894eb5c1dee871262014c6`;
- reconciled tree: `66ad3603c081e4dc214099758544ef21264bd78a`;
- reconciliation commit: `e8dd3662cb2d12bc6ae49b2bd0fc1d8c8f2a0f9d`.

Only the brand tree, six brand-specific evidence files and the uploaded transport archive were overlaid onto latest main. Current Core/release/state/next-actions/decisions truth came from latest authoritative main. GitHub subsequently recognized PR `#13` as merged through ancestry at the exact reconciliation commit.

The materialization workflow then reapplied only the brand entries to current README/repository-map documents.

## Repository documentation

The `brand/` surface is represented in `README.md`, `README.zh-CN.md`, and `REPOSITORY_TREE.md`, based on latest-main documentation with brand-only entries added.

## QA and integration rules

- Principal-facing review is clean; no diagnostic bounds are brand artwork.
- Review uses `contain`, never crop/cover.
- No derivative may modify approved core geometry.
- No regenerated A, substitute font, particle cleanup or palette reconciliation is authorized.

## Integration readiness

Visual design, production masters, 13/13 QA, documentation, reconciliation and byte-exact binary preservation are complete on the brand branch.

Remaining publication gates are only:

1. re-resolve latest `main` immediately before publication and reconcile again if it moved;
2. require Draft PR `#11` Core 0.2 synthetic-merge conformance to be green on the final branch head;
3. integrate the brand package without replacing newer authoritative Core/release continuity truth;
4. fresh-verify authoritative `main` after publication.
