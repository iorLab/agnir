# Agnir brand production status

Date: 2026-09-03
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

Directly usable package-level SVG exports exist under `brand/exports/`:

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

Directly shrinking the full particle field to 16px loses the A reading. The approved board itself defines a favicon-size family, so 32px and 16px exports use a deterministic visibility derivative of the same master: only particles below a fixed visibility threshold are pruned. The A geometry, major particles, pale inner A and central anchor are unchanged. This is a size derivative, not a new logo design.

## Complete QA status

The earlier final-QA sheet was incomplete because it covered only derivative exports. It is superseded by the complete symmetric 13-item QA recorded in `brand/qa/FINAL-QA.md`.

The completed QA scope is:

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

Complete QA sheet SHA-256: `145ab94e4458cdd9165bd61ceed71e4a12302b7cb71077443414ee8683302cfa`.

The current cross-brand production delivery ZIP SHA-256 is `171b974b62fabc9eb286104d6bc090563e381ac4fd4fb8d2157b6b3cceaad2c7`.

The approved production masters remain unchanged through this derivative/QA pass.

## Main reconciliation status

The brand branch has now been reconciled twice as authoritative `main` advanced concurrently.

### First reconciliation

- main observed: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`;
- reverse-sync PR `#8` (`main` → `brand/identity-system`);
- branch merge commit: `b00e0d7c544e74d4b0245569450ecebb271461d5`;
- result at that point: **behind `main` = 0**.

### Second reconciliation after RC acceptance reached main

A later stale-base check found `main` at `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d` and the brand branch behind by 15 commits. Conflict-probe PR `#10` was intentionally closed unmerged.

The branch was reconciled with an explicit latest-main-wins two-parent commit:

- pre-reconcile brand: `6ac35732ca58301b2fa8e9759a0ed8e7d4042dcd`;
- authoritative main: `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`;
- latest-main base tree: `5bedbf190a49e01689280fdbd0a812a0d1b60347`;
- reconciled tree: `5e09b705519a36183859f8abc64870a39dc60ee7`;
- reconciliation commit: `714da79d7338e6d2c35d691da6003aa134ed902c`.

Only `brand/` plus brand-specific Evidence were overlaid onto latest main. Stale copies of `AGNIR.yaml`, state, next actions, decisions, release/Core/profile contracts and repository docs were deliberately not reused.

A minimal post-reconcile documentation patch then restored only the brand entries to the current README / repository maps; corrected workflow run `33705830326` succeeded. Current comparison after this reconciliation reports **behind `main` = 0**. See `.agnir/evidence/2026-09-03-brand-main-reconciliation.md`.

## Repository-documentation status

The new top-level `brand/` surface is synchronized into:

- `REPOSITORY_TREE.md`;
- `README.md` compact repository tree;
- `README.zh-CN.md` compact repository tree.

The documents are based on current authoritative-main content with only the brand-specific map entries added.

## Integration validation

Earlier branch-local one-off validation passed before the second main reconciliation. After the second reconciliation, Draft PR `#11` (`brand/identity-system` → `main`) became the canonical non-publishing integration validation surface.

The repository's actual Core 0.2 pull-request workflow runs against GitHub's synthetic merge tree and covers:

- Core 0.2 repository self-host cold-start;
- stable Core 0.1 compatibility regression;
- VCS branch continuity and lineage binding;
- Core 0.2 non-VCS/VCS mapping;
- repository-filesystem 0.2 discovery;
- Core/profile migration semantics;
- RC fresh-install and published-v0.1.1 migration gates;
- full conformance suite.

The Draft PR is explicitly blocked from merge while the byte-exact large-binary preservation gate remains open. The **latest** PR-head run, not an older receipt embedded in this file, is the final conformance authority before merge.

## QA rules

- Principal-facing review is clean: no blue bounds boxes or debug overlays.
- Engineering diagnostics may show bounds only under explicit diagnostic mode.
- Review/render uses `contain`, never crop/cover.
- No derivative may modify the approved core geometry.

## Binary reference boundary

The byte-exact approved 10:42 AM source board remains locked by SHA-256 and preserved in the external reference/delivery package. The complete 13-item PNG package exists and is hash-recorded, but large binary payloads still cannot be attached safely through the current execution bridge without truncation risk.

Final byte-exact source-board and selected large-PNG repository preservation therefore remains a pre-`main` integration gate.

## Remaining integration gates

1. Preserve the byte-exact approved Agnir board and desired large PNG delivery files through a binary-safe repository path; verify hashes after storage.
2. Re-check latest `main` immediately before publication and reconcile again if it moved.
3. Require the latest Draft PR `#11` synthetic-merge conformance run to be green on the final head.
4. Integrate the approved brand package coherently without replacing newer Core 0.2 continuity/release truth.
5. Verify authoritative `main` after publication.

Visual design, production masters, 13/13 QA, repository documentation and reconciliation mechanics are complete. **Large byte-exact binary preservation is the only non-reconciliation integration blocker still open.**
