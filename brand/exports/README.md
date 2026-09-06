# Agnir production exports

These exports derive only from the Principal-approved Agnir production masters under `brand/masters/`.

## Materialized SVG exports

Direct package-level SVG treatments:

- `agnir-horizontal-light.svg`
- `agnir-horizontal-dark.svg`
- `agnir-horizontal-monochrome.svg`
- `agnir-app-icon.svg`
- `agnir-favicon.svg`

These SVGs reference approved masters by relative path so geometry is not forked into a second authority. Keep the `brand/exports/` + `brand/masters/` package relationship intact.

## Materialized PNG delivery package

The complete 13-item PNG delivery set is committed under `brand/exports/png/`:

- `agnir-mark.png`
- `agnir-wordmark.png`
- `agnir-horizontal-lockup.png`
- `agnir-vertical-lockup.png`
- `agnir-light-usage.png`
- `agnir-dark-usage.png`
- `agnir-monochrome-usage.png`
- `agnir-app-icon.png`
- `agnir-favicon-128.png`
- `agnir-favicon-64.png`
- `agnir-favicon-32.png`
- `agnir-favicon-16.png`
- `agnir-social-card.png`

GitHub Actions run `33730501685` verified the handoff archive SHA-256 and every source/destination payload SHA-256 before materialization commit `a858de5c2d12f800ef6d9057f28422320ff5a012`.

## Deterministic rebuild

`brand/tools/build-production-derivatives.py` remains the deterministic builder for PNG derivatives and small-size visibility pruning.

## Rules

- `brand/masters/` remains authoritative vector geometry.
- PNG exports are delivery derivatives, not replacement masters.
- Do not regenerate or redesign the mark or wordmark.
- Light treatment uses the approved particle A with brand-color wordmark.
- Dark treatment uses the approved particle A with white wordmark.
- Monochrome preserves the particle hierarchy in grayscale.
- 128px / 64px favicons use the full mark.
- 32px / 16px may prune only sub-threshold micro-particles; A geometry, major particles, pale inner A and central anchor remain unchanged.
