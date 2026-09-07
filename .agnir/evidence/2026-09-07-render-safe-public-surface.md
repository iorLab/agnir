# Render-safe public surface repair — 2026-09-07

## Principal observation

The Principal supplied a fresh GitHub README screenshot after the first theme-aware repair. The centered logo area rendered as an empty dark rectangle, and the English README still displayed accidental Chinese product-copy text (`结构层`) inside the English identity paragraph.

The Principal requested direct execution where possible and identified both the image-rendering defect and mixed-language presentation as public-surface issues.

## Root cause

The first repair switched README rendering to:

- `brand/exports/agnir-horizontal-dark.svg`;
- `brand/exports/agnir-horizontal-light.svg`.

Those approved export files are not render-self-contained. For example, the dark export contains nested relative SVG image dependencies:

```xml
<image href="../masters/agnir-mark.svg" .../>
<image href="../masters/agnir-wordmark.svg" .../>
```

GitHub README sanitization/rendering did not resolve those nested references, so the export background rendered while the actual mark/wordmark did not. The same dependency would also fail in the current Pages artifact because `.github/workflows/pages.yml` flattened the export into `_site/assets/` without copying `brand/masters/` into the relative path expected by the SVG.

The defect is therefore a public delivery/rendering defect, not a brand geometry defect.

## Staged repair

Branch: `maintenance/readme-render-language-cleanup`

Base authoritative revision: `6927ce7cd910f97bbc2c36e990cb8e4a42728567`.

Changes:

1. `README.md`
   - replaces theme-aware nested-reference SVG rendering with approved self-contained `brand/exports/png/agnir-dark-usage.png`;
   - removes accidental Chinese display text from English identity copy;
   - removes Chinese command aliases from English Agent instructions while retaining the Simplified Chinese language-navigation link.
2. `README.zh-CN.md`
   - uses the same render-safe approved PNG lockup;
   - localizes public prose into Simplified Chinese while retaining exact technical identifiers, filenames, commands and version labels where required.
3. `website/index.html` / `website/zh-CN.html`
   - use `assets/agnir-dark-usage.png` for the header lockup;
   - Simplified Chinese product copy is localized instead of mixing English marketing fragments throughout.
4. `.github/workflows/pages.yml`
   - copies `brand/exports/png/agnir-dark-usage.png` into the deployment artifact;
   - stops copying the nested-reference horizontal dark SVG for site-header use.
5. `website/README.md`
   - records the render-self-contained asset requirement and why the PNG is the accepted host-safe delivery derivative.
6. `.agnir/decisions.md`
   - records render-self-contained public-asset and localized-prose invariants.

No visual master, Core/profile contract, Project/lineage identity, stable release tag or release identity changes.

## Pages execution boundary

Current repository host readback reports `has_pages=false`.

The GitHub connector available in this session supports repository/ref/PR/content operations but does not expose:

- a Pages-settings mutation; or
- a workflow-dispatch action.

The official `actions/configure-pages` action documents an `enablement` mode, but it explicitly requires a token other than the ordinary `GITHUB_TOKEN`; for a GitHub App it requires both `administration:write` and `pages:write`. The repository workflow currently has only the ordinary workflow token available. Therefore no unsupported or misleading self-enable attempt is being claimed.

Pages live publication remains pending until an authority capable of changing repository Pages settings selects GitHub Actions as the publishing source, after which `Deploy Agnir website` can run and the public URL can be verified.

## Acceptance gate

Final acceptance requires:

1. branch behind authoritative `main` = 0 before integration;
2. synthetic-merge conformance success;
3. coherent integration of Project changes plus reconciled target continuity;
4. authoritative post-merge conformance success;
5. public README readback showing the PNG asset reference and language-clean identity copy.
