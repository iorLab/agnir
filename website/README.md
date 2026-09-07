# Agnir website

This directory contains the minimal public Agnir website surface.

## Product role

The website is a **public adoption surface**, not a Core/profile contract and not a second copy of Project continuity.

Canonical positioning remains in `adoption/README.md`. Canonical visual identity remains in `brand/`. The website consumes the approved brand masters through the deterministic production-derivative builder; it does not own or redesign them.

## Current pages

- `index.html` — English landing page;
- `zh-CN.html` — Simplified Chinese landing page;
- `styles.css` — self-contained responsive presentation, with no external font or JavaScript dependency.

The landing page leads with the post-v1 adoption story:

> Your agent forgets. Your project shouldn't.

and demonstrates fresh-session recovery before introducing protocol vocabulary.

## Localization

Public localization should optimize for how the target developer community actually speaks, not for literal sentence-by-sentence equivalence.

For Simplified Chinese developer-facing copy:

- use **Agent** rather than the uncommon literal translation `智能体`;
- keep familiar developer terms such as `API`, `IDE`, `Core`, `profile`, `Skill`, `Checkpoint`, and `prompt` in English where that is more idiomatic;
- translate explanatory prose into natural Simplified Chinese while preserving Agnir's Project Continuity semantics;
- do not let localization redefine Core/profile terms or product category boundaries;
- avoid awkward literal renderings such as “兼容执行器”, “连续性表面”, or “协调回检查点” when a clearer developer-facing phrase preserves the same meaning.

The Chinese public surface may therefore differ structurally from the English sentence while remaining semantically aligned with the approved positioning in `adoption/README.md`.

## Brand assets

Do not duplicate or manually redraw Agnir production geometry under `website/`.

At Pages build time, `.github/workflows/pages.yml` runs `brand/tools/build-production-derivatives.py` against the Principal-approved `brand/masters/agnir-mark.svg` and `brand/masters/agnir-wordmark.svg`. This materializes a self-contained `assets/agnir-horizontal-dark.svg` with:

- the approved particle-A geometry and palette;
- the approved dark-treatment white wordmark;
- a **transparent background**;
- no nested external SVG dependency.

This is intentionally different from the older committed `brand/exports/png/agnir-dark-usage.png`, which is a dark-background usage presentation and therefore carries its own dark rectangular backdrop. It is not appropriate as an inline website-header logo on a differently colored page background.

The Pages artifact also includes:

- generated `assets/agnir-favicon.svg` from the same approved masters;
- `brand/exports/png/agnir-social-card.png` as `assets/agnir-social-card.png`.

If the approved master geometry or the deterministic derivative builder changes, the Pages workflow is in the automatic-deployment path filter so the public site is rebuilt from the new canonical source.

## Feedback surface

The website links directly to GitHub's issue chooser. Repository issue forms provide separate paths for defects, product ideas, and real-world adoption reports. Adoption reports are evidence candidates, not automatic protocol-conformance claims.

## Publication

Default GitHub Pages URL:

`https://iorlab.github.io/agnir/`

Workflow: `.github/workflows/pages.yml`.

The first manual GitHub Pages publication succeeded on authoritative `main` in workflow run `34083599723`; both `build` and `deploy` completed successfully and repository host readback reports `has_pages=true`.

After that verified baseline, Pages publication is automatic for authoritative `main` pushes that modify website source, the canonical brand inputs actually consumed by the site, or the Pages workflow itself. `workflow_dispatch` remains available as a manual recovery/republication path.

The path filter intentionally avoids redeploying the public website for unrelated Core, conformance, release, or Agnir continuity-only commits.

A custom domain is not currently declared. Adding one is a separate repository-host/brand decision and must not be inferred from website source alone.
