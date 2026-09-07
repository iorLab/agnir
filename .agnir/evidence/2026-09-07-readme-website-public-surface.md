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

The same repair is staged in `README.md` and `README.zh-CN.md`. No master geometry, wordmark path, particle field, palette, or approved brand authority was modified.

## Website source

A minimal bilingual static website source was added:

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

## Publication boundary

Intended default Pages URL:

`https://iorlab.github.io/agnir/`

Live publication is **not yet accepted**. GitHub requires the repository Pages publishing source to be configured for GitHub Actions before the official deployment workflow can publish. The available repository connector in this work session exposes repository content/PR/ref operations but no supported Pages-settings mutation, so the workflow is deliberately manual-dispatch until that host configuration is completed.

Source readiness and live host publication are separate completion states.

## Staging lineage

Staging branch:

`maintenance/readme-website-public-surface`

Base authoritative revision:

`1b74b5361104b15297c389eec0721af00c436179`

The staged change is non-semantic stable maintenance: it does not modify Core/profile 1.0, historical compatibility contracts, Project identity, continuity lineage identity, stable tags, or release identity.

Final acceptance requires synthetic-merge conformance, authoritative squash integration, and post-merge conformance. The temporary staging branch should be retired after the material result is canonical.
