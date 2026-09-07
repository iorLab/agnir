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

GitHub README sanitization/rendering did not resolve those nested references, so the export background rendered while the actual mark/wordmark did not. The same dependency would also fail in the flattened Pages artifact because `.github/workflows/pages.yml` copied the export without the relative master paths it expects.

The defect was therefore a public delivery/rendering defect, not a brand geometry defect.

## Accepted repair

PR: `#31` — **Public surface: render-safe logo and language cleanup**.

Base authoritative revision: `6927ce7cd910f97bbc2c36e990cb8e4a42728567`.

Final accepted changes:

1. `README.md`
   - uses approved self-contained `brand/exports/png/agnir-dark-usage.png`;
   - visible product prose remains English apart from explicit language navigation and exact technical identifiers;
   - historical machine-only cross-language aliases remain only in non-rendering comments where existing self-host compatibility requires them.
2. `README.zh-CN.md`
   - uses the same render-safe approved PNG lockup;
   - visible public prose is substantially localized Simplified Chinese;
   - older literal self-host markers remain only in non-rendering compatibility comments where necessary.
3. `website/index.html` / `website/zh-CN.html`
   - use `assets/agnir-dark-usage.png` for the header lockup;
   - Simplified Chinese marketing copy is localized rather than mixing English product-copy fragments throughout.
4. `.github/workflows/pages.yml`
   - copies `brand/exports/png/agnir-dark-usage.png` into the deployment artifact rather than relying on the nested-reference horizontal SVG.
5. `website/README.md`
   - records the render-self-contained public-asset requirement.
6. `conformance/test_1_0_package_surface.py`
   - validates current localized Chinese package-status/support wording rather than requiring obsolete mixed-language visible text.
7. `.agnir/decisions.md`
   - records render-self-contained public-asset and localized-prose invariants.

No visual master, Core/profile contract, Project/lineage identity, stable release tag, or release identity changed.

## Conformance pressure

PR #31 deliberately ran through the stable self-host/package gates rather than bypassing them.

- initial synthetic run `34082048733` exposed historical literal coupling in the Chinese README self-host marker;
- non-rendering compatibility comments preserved required machine literals without restoring mixed visible UI;
- later run `34082389127` reached the full suite and exposed one package-surface assertion that required obsolete mixed-language visible support wording;
- `conformance/test_1_0_package_surface.py` was updated to validate the actual localized visible Chinese wording;
- final PR head `b7f6aac0d778a7c3082da11bb74e4da863b7215d` passed synthetic-merge conformance run `34082518956`, repository job `101620379344`, including repository self-host, stable package gates, and the full `test_*.py` suite;
- authoritative squash merge `357dccff0044a262e2bfe5a3e002fc53a49ec6ad` then passed post-merge conformance run `34082581320`, repository job `101620553239`, including the same full suite.

This conformance adjustment validates public package presentation only. It does not modify Core/profile semantics or compatibility dispatch.

## Host readback after acceptance

Fresh repository metadata readback after the authoritative merge reports:

- description set to the intended Agnir description;
- `has_pages=false`;
- homepage empty;
- topics empty;
- recognized repository license absent.

The README/website source repair is therefore accepted, while live GitHub Pages publication remains a separate host-side pending state.

## Pages execution boundary

The GitHub connector available in this session supports repository/ref/PR/content operations but does not expose:

- a Pages-settings mutation; or
- a workflow-dispatch action.

The official `actions/configure-pages` action documents an `enablement` mode, but it explicitly requires a token other than the ordinary `GITHUB_TOKEN`; for a GitHub App it requires repository administration/pages-write authority. Therefore no unsupported self-enable attempt is claimed.

Live publication requires an authority capable of changing repository Pages settings to select **GitHub Actions** as the publishing source, after which `Deploy Agnir website` must run and `https://iorlab.github.io/agnir/` plus the English/Chinese pages and public assets must be verified.

## Acceptance result

**PASS — render-safe public surface repair accepted.**

The original screenshot defects are closed at the repository-source level:

- the README no longer depends on nested-reference SVG rendering;
- the accepted public lockup is the approved self-contained PNG derivative;
- visible English/Chinese copy is language-clean except for intentional navigation and exact technical identifiers;
- the website artifact uses the same render-safe asset boundary;
- synthetic-merge and authoritative post-merge conformance both pass.

The remaining blocker is not a source defect: GitHub Pages is not yet enabled on the repository host.
