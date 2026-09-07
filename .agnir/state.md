# Agnir Current State

Durable continuity belongs to the Project.

Agnir `v1.0.0` is **published, independently verified, and the latest stable release**. Ordinary stable-maintenance mode applies.

The immutable stable tag `v1.0.0` points to exact released revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. GitHub Release id `383612171` is non-draft and non-prerelease. Accepted RC `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## Stable compatibility state

- repository/distribution: `1.0.0`;
- Core: `1.0`;
- repository/filesystem profile: `repository-filesystem/1.0`;
- explicit Core/profile `0.2` -> `1.0` promotion remains Project-owned and separately authorized;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- installing a `1.0.x` distribution does not silently relabel an existing valid `0.2` Project.

## Public repository surface

The Principal-approved Agnir identity system remains authoritative under `brand/`. The public README rendering/localization repair is now accepted on authoritative `main`.

The first post-v1 README repair in PR #30 used approved theme-aware SVG exports, but those exports contain nested relative `<image>` references to master SVG files. GitHub README sanitization did not resolve those dependencies, producing the blank logo rectangle observed by the Principal; the same dependency would have failed in the flattened Pages artifact.

PR `#31` replaced those host-fragile SVG references with the approved self-contained delivery asset `brand/exports/png/agnir-dark-usage.png` and cleaned the localized public copy.

Accepted repair receipts:

- final PR #31 head: `b7f6aac0d778a7c3082da11bb74e4da863b7215d`;
- final synthetic-merge conformance: run `34082518956`, repository job `101620379344` — success;
- authoritative squash merge: `357dccff0044a262e2bfe5a3e002fc53a49ec6ad`;
- authoritative post-merge conformance: run `34082581320`, repository job `101620553239` — success.

Current accepted public behavior:

- English README uses the self-contained PNG lockup and keeps visible product prose English, apart from the explicit language-navigation link and exact technical identifiers;
- Simplified Chinese README uses the same lockup and substantially localized visible prose; historical literal markers required by self-host/package compatibility are retained only in non-rendering comments where necessary;
- `website/index.html` and `website/zh-CN.html` use the same approved render-safe PNG lockup;
- the Pages artifact build copies the self-contained PNG rather than the nested-reference horizontal SVG;
- `conformance/test_1_0_package_surface.py` validates the localized Chinese package presentation rather than requiring obsolete mixed-language visible copy.

No brand master geometry, wordmark path, palette, Core/profile semantics, Project/lineage identity, stable tag, or release identity changed.

## Public website source and host state

The bilingual static website source is canonical on `main` under `website/`:

- English landing page: `website/index.html`;
- Simplified Chinese landing page: `website/zh-CN.html`;
- responsive presentation: `website/styles.css`;
- publication boundary: `website/README.md`;
- manual deployment workflow: `.github/workflows/pages.yml`.

The website materializes the approved **Project Continuity** positioning and consumes canonical brand exports rather than redefining the identity.

The intended first host is `https://iorlab.github.io/agnir/`, but **the website is not live yet**. Fresh repository-host readback after PR #31 still reports:

- `has_pages=false`;
- homepage empty;
- topics empty;
- recognized repository license absent;
- intended repository description is set correctly.

The currently connected GitHub tool surface does not expose a Pages-settings mutation or workflow-dispatch action. Official `actions/configure-pages` enablement requires separate repository-administration/pages-write authority rather than the ordinary workflow token. Therefore live publication still requires a host-side authority to select **GitHub Actions** as the Pages publishing source, followed by a successful `Deploy Agnir website` run and public URL/assets verification. Source readiness and live publication remain separate states.

## Post-1.0 adoption evidence

Svif (`iorLab/svif`) remains the first recorded real-project downstream Agnir 1.0 adoption case. It completed an explicit Principal-authorized Core/profile `0.2` -> `1.0` promotion while preserving Project identity, logical lineage, selector, durable memory locators, historical adapter support, product version, brand assets, and its immutable Preview.1 distribution boundary. No Agnir defect was exposed.

## Launch and adoption strategy

The Principal-approved strategy is canonical at `adoption/README.md`:

- category: **Project Continuity**;
- positioning: project-owned durable continuity, not tool-owned generic AI memory;
- first audience: AI coding power users with fresh-session / cross-surface continuity pain;
- first proof: canonical fresh-session recovery demo;
- sequence: hygiene → external design-user adoption → technical launch → broader developer launch;
- north star: successful external cold-start resumes outside direct maintainer control.

`brand/` remains visual authority; `adoption/` owns positioning/launch strategy; `website/` materializes approved public messaging. None redefines Core/profile semantics.

## Release evidence chain

- independent implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- stable arm/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable publication workflow: `34039014354`, attempts 1 and 2 success.

Agnir remains in stable maintenance + downstream adoption mode. The README/website rendering and localization defect is closed. The immediate remaining public-surface blocker is GitHub Pages host enablement/live verification, followed by the rest of Wave 0 metadata/license/feedback hygiene.
