# README theme repair and website public surface — 2026-09-07

## Principal instruction

The Principal identified that the Agnir logo rendered as visually skewed in the GitHub README and requested both:

1. repair the README logo presentation; and
2. create the Agnir website public surface.

## README diagnosis

The approved logo geometry was not redrawn.

The public README used:

`brand/exports/png/agnir-horizontal-lockup.png`

That fixed treatment contains a dark wordmark. On GitHub dark theme, the wordmark becomes visually suppressed against the host background while the particle mark remains visible, making the centered full lockup appear horizontally displaced/skewed.

The repair replaces the fixed PNG with GitHub theme-aware `<picture>` markup selecting the already approved exports:

- dark viewer theme → `brand/exports/agnir-horizontal-dark.svg`;
- light viewer theme → `brand/exports/agnir-horizontal-light.svg`;
- fallback → `brand/exports/agnir-horizontal-light.svg`.

The same repair is authoritative in `README.md` and `README.zh-CN.md`. No master geometry, wordmark path, particle field, palette, or approved brand authority was modified.

## Website source

A minimal bilingual static website source is authoritative on `main`:

- `website/index.html` — English landing page;
- `website/zh-CN.html` — Simplified Chinese landing page;
- `website/styles.css` — responsive self-contained presentation;
- `website/README.md` — website responsibility and publication boundary;
- `.github/workflows/pages.yml` — GitHub Pages artifact/deployment workflow.

The website implements the Principal-approved `adoption/README.md` positioning:

- category: **Project Continuity**;
- first message: **Your agent forgets. Your project shouldn't.**;
- first proof: fresh-session recovery;
- Project-owned truth: State / Next Actions / Decisions / Evidence;
- one-line install intent;
- protocol/release credibility after the value story.

The Pages build copies canonical brand exports into the deploy artifact rather than storing duplicate visual masters under `website/`.

## Integration acceptance

Staging branch:

`maintenance/readme-website-public-surface`

Captured authoritative base:

`1b74b5361104b15297c389eec0721af00c436179`

Final staging head:

`aa9be855a4d8eca55ffc927d6fe22de2cf70b6f7`

PR:

`#30` — `Public surface: fix README lockup and add Agnir website`

Validation and integration receipts:

- final branch was 12 commits ahead / 0 behind captured `main` before integration;
- PR synthetic-merge conformance: run `34079325656` — **success**;
- authoritative squash merge: `4b29fb8becc0b155a2598c09b8199342e40a9e65`;
- authoritative post-merge conformance: run `34079406444` — **success**;
- repository-filesystem job: `101611700144` — **success**;
- stable/prerelease publication jobs skipped on the ordinary maintenance change as required.

The accepted change is non-semantic stable maintenance: Core/profile 1.0, historical compatibility contracts, Project identity, continuity lineage identity, stable tags, and release identity were not changed.

The staging branch now carries no unique material product truth and may be retired under normal temporary-ref housekeeping.

## Publication boundary

Intended default Pages URL:

`https://iorlab.github.io/agnir/`

Live publication is **not yet accepted**. Current repository-host readback after integration reports:

- intended repository description: set;
- topics: empty;
- homepage: empty;
- `has_pages=false`;
- recognized repository license: absent.

GitHub Pages must first be configured to use **GitHub Actions** as its publishing source. After that, the manual `Deploy Agnir website` workflow must succeed and the public English/Chinese pages plus favicon/social-card assets must be read back successfully before the site is called live.

Source readiness and live host publication are separate completion states.
