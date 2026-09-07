# Agnir website

This directory contains the minimal public Agnir website surface.

## Product role

The website is a **public adoption surface**, not a Core/profile contract and not a second copy of Project continuity.

Canonical positioning remains in `adoption/README.md`. Canonical visual identity remains in `brand/`. The website consumes approved brand exports; it does not own or redesign them.

## Current pages

- `index.html` — English landing page;
- `zh-CN.html` — Simplified Chinese landing page;
- `styles.css` — self-contained responsive presentation, with no external font or JavaScript dependency.

The landing page leads with the post-v1 adoption story:

> Your agent forgets. Your project shouldn't.

and demonstrates fresh-session recovery before introducing protocol vocabulary.

## Brand assets

Do not duplicate or manually redraw Agnir production assets under `website/`.

The Pages workflow copies these canonical exports into the deployment artifact:

- `brand/exports/agnir-horizontal-dark.svg`;
- `brand/exports/agnir-favicon.svg`;
- `brand/exports/png/agnir-social-card.png`.

If a public website needs a new visual derivative, produce and approve it through the `brand/` system first.

## Publication

Intended default GitHub Pages URL:

`https://iorlab.github.io/agnir/`

Workflow: `.github/workflows/pages.yml`.

The workflow is intentionally **manual-dispatch only until repository Pages is enabled**. GitHub requires a one-time repository setting selecting GitHub Actions as the Pages publishing source. Site source readiness and live host publication must be reported separately.

After Pages is enabled, dispatch `Deploy Agnir website`. A later maintenance change may add automatic `main` push deployment once the live surface is verified.

A custom domain is not currently declared. Adding one is a separate repository-host/brand decision and must not be inferred from website source alone.
