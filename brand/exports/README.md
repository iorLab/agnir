# Agnir production exports

These exports are generated only from the Principal-approved Agnir production masters under `brand/masters/`.

## Materialized SVG exports

The branch now includes directly usable package-level SVG exports:

- `agnir-horizontal-light.svg`
- `agnir-horizontal-dark.svg`
- `agnir-horizontal-monochrome.svg`
- `agnir-app-icon.svg`
- `agnir-favicon.svg`

To avoid geometry duplication, these SVGs reference the approved masters by relative path and apply only canvas/color treatment. Keep the `brand/exports/` and `brand/masters/` relative layout intact when using them as a package. The geometry authority remains `brand/masters/`.

`brand/tools/build-production-derivatives.py` remains the deterministic builder for PNG delivery derivatives and the visibility-pruned 32/16px favicon sources.

## Rules

- Do not regenerate or redesign the mark or wordmark.
- Light treatment uses the approved particle A with brand-color wordmark.
- Dark treatment uses the approved particle A with white wordmark.
- Monochrome treatment converts the mark to grayscale and keeps the wordmark black.
- 128px and 64px favicons use the full mark.
- 32px and 16px favicons use deterministic visibility pruning of only the smallest particles; A geometry, major particles, pale inner A, and central anchor remain unchanged.
- PNG exports are delivery derivatives, not replacement vector masters.

The authoritative vector sources for branch-local brand production are:

- `brand/masters/agnir-mark.svg`
- `brand/masters/agnir-wordmark.svg`
- `brand/masters/agnir-horizontal-lockup.svg`
- `brand/masters/agnir-vertical-lockup.svg`
