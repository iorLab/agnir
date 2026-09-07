# Transparent website logo and Wave 0 feedback surface — 2026-09-07

## Principal observation

The Principal observed that the Agnir lockup in the live website header appeared on a rectangular background whose color differed from the surrounding website surface. The intended inline header presentation is a transparent lockup.

## Root cause

The website was using `brand/exports/png/agnir-dark-usage.png`. That asset is a dark-background usage presentation and therefore carries its own rectangular backdrop.

The committed `brand/exports/agnir-horizontal-dark.svg` was also unsuitable as a direct public-host replacement because it contained both:

- an explicit `#17202A` background `<rect>`; and
- relative `<image>` references to `../masters/agnir-mark.svg` and `../masters/agnir-wordmark.svg`.

The existing deterministic builder `brand/tools/build-production-derivatives.py` already defined the desired approved dark treatment from canonical masters: the approved particle A, a white wordmark, no background rectangle, and self-contained inline vector geometry.

## Accepted repair

PR #35 changed the website deployment boundary rather than redesigning the identity:

- website header references `assets/agnir-horizontal-dark.svg`;
- Pages runs `brand/tools/build-production-derivatives.py` against the approved `brand/masters/agnir-mark.svg` and `brand/masters/agnir-wordmark.svg` at build time;
- the resulting Pages artifact contains the transparent, self-contained dark horizontal treatment;
- automatic Pages path filters now follow the actual canonical inputs used to build the site;
- both website language variants expose an explicit GitHub feedback entry;
- structured GitHub issue forms were added for bugs, product ideas, and adoption reports.

No approved mark/wordmark geometry, Core/profile semantics, Project identity, logical lineage identity, release tag, or stable release identity changed.

## Acceptance receipts

PR #35:

- final head: `361c823257effb524599905020eb94a9f02f8872`;
- synthetic-merge conformance: run `34085855448`, repository job `101629640557` — success;
- authoritative squash merge: `16810a514620e8a62660948fb9477ba8106baceb`;
- authoritative post-merge conformance: run `34085888593`, repository job `101629727855` — success.

Automatic Pages publication from that authoritative `main` push:

- workflow run `34085888590` — success;
- build job `101629727838` — success;
- deploy job `101629760644` — success;
- Pages artifact id `10005182999`;
- artifact digest: `sha256:ac4a9f5c653e15f0ba6d8e1edb7fcd22227aedbd950789d7657868378013b034`.

## Artifact verification

The downloaded deployed artifact was inspected directly. `assets/agnir-horizontal-dark.svg` satisfied all of the required render conditions:

- no `<rect>` background element;
- no external `<image>` dependency;
- approved white dark-treatment wordmark present;
- black default wordmark treatment absent;
- geometry is materialized self-contained from the approved masters by the deterministic production builder.

This closes the observed website-header background defect at the artifact/deployment level. Human browser presentation remains a distinct observation and may be rechecked after cache refresh when necessary.

## Wave 0 feedback surface

The same accepted change added GitHub issue-chooser intake:

- bug report form;
- product idea form;
- adoption report form;
- documentation and public-site contact links.

Both English and Simplified Chinese website variants now link to the issue chooser.

An adoption report is an **evidence candidate**, not automatic accepted evidence. Material claims still require ordinary review and receipts before they are added to canonical Agnir evidence.

## Repository-host readback after repair

Fresh repository metadata after the accepted merge reports:

- description: set correctly;
- Pages: enabled;
- homepage: `https://iorlab.github.io/agnir`;
- topics: empty;
- recognized license: absent;
- Discussions: disabled.

GitHub Issues is accepted as the first external feedback path, so Discussions is not a Wave 0 blocker. The remaining material Wave 0 decisions are repository topics and explicit Principal selection of a repository license/contribution-licensing policy.
