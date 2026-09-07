# Agnir Current State

Durable continuity belongs to the Project.

Agnir `v1.0.0` is **published, independently verified, and the latest stable release**. Ordinary stable-maintenance mode applies.

The immutable stable tag `v1.0.0` points to exact released revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. GitHub Release id `383612171` is non-draft and non-prerelease, and `releases/latest` resolves to `v1.0.0`. Accepted RC `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## Stable compatibility state

- repository/distribution: `1.0.0`;
- Core: `1.0`;
- repository/filesystem profile: `repository-filesystem/1.0`;
- explicit Core/profile `0.2` -> `1.0` promotion remains Project-owned and separately authorized;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- installing a `1.0.x` distribution does not silently relabel an existing valid `0.2` Project.

## Brand identity and public repository surface

The Principal-approved Agnir identity system is authoritative on `main` and is surfaced directly in both public README variants.

- brand integration PR: `#11`, merged completed;
- authoritative squash merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- brand acceptance checkpoint: `e5305ab0474c4c8c562dbfbfaca54185b84d07f1`;
- README/brand public-surface + first adoption evidence commit: `75dde01da2123e731a6de461fb2f3269fd6bbbbb`;
- public-surface conformance run/job: `34077491299` / `101606358819` — success;
- canonical production masters remain under `brand/masters/`; delivery PNG/app-icon/favicon surfaces remain under `brand/exports/png/`.

The first post-v1 README repair (PR #30) correctly diagnosed the original dark-wordmark PNG issue but its replacement was not actually GitHub-render-safe. The selected `brand/exports/agnir-horizontal-dark.svg` and `agnir-horizontal-light.svg` exports contain nested relative `<image>` references to master SVG files. GitHub README sanitization did not resolve that dependency, producing the blank logo area observed by the Principal. The same dependency would also be broken by the flattened Pages artifact because the referenced masters were not copied.

A second public-surface repair is now staged on `maintenance/readme-render-language-cleanup`:

- both README variants use approved self-contained `brand/exports/png/agnir-dark-usage.png`;
- English public prose removes accidental Chinese display text while retaining the language-switch link;
- Simplified Chinese README prose has been localized substantially, retaining exact protocol identifiers, filenames, commands and version names only where needed;
- both website language variants use the same render-safe approved PNG lockup;
- the Simplified Chinese website surface is localized instead of mixing English product-copy fragments throughout;
- `.github/workflows/pages.yml` copies the PNG lockup into the deployment artifact instead of the nested-reference SVG.

No brand master geometry, wordmark path, particle field, palette, Core/profile semantics, stable tag, or release identity changes in this repair.

Previous PR #30 receipts remain valid for the source/website introduction itself:

- PR: `#30`;
- final staging head: `aa9be855a4d8eca55ffc927d6fe22de2cf70b6f7`;
- PR synthetic-merge conformance: run `34079325656` — success;
- authoritative squash merge: `4b29fb8becc0b155a2598c09b8199342e40a9e65`;
- authoritative post-merge conformance: run `34079406444` / repository job `101611700144` — success.

GitHub repository About metadata is **partially complete** by current host readback. The description is set to the intended Agnir description. Topics remain empty, homepage remains empty, GitHub reports `has_pages=false`, and no recognized repository license is present. These are repository-host/public-adoption surfaces, not Core or release state.

## Public website source

A minimal bilingual public website source is canonical on `main` under `website/`; the render-safe asset/localization repair described above is currently staged.

- English landing page: `website/index.html`;
- Simplified Chinese landing page: `website/zh-CN.html`;
- responsive presentation: `website/styles.css`;
- responsibility/publication boundary: `website/README.md`;
- deployment workflow: `.github/workflows/pages.yml`.

The website materializes the approved adoption strategy: it leads with **Project Continuity**, fresh-session recovery, Project-owned truth, one-line installation, and then protocol credibility. It consumes canonical approved brand exports rather than duplicating/redrawing brand masters.

The intended default host is `https://iorlab.github.io/agnir/`, but **the website is not live yet**. Current GitHub host readback reports `has_pages=false`. The available GitHub connector in this session exposes repository/ref/PR/content operations but no Pages-settings mutation or workflow-dispatch action. `actions/configure-pages` cannot solve this with the ordinary `GITHUB_TOKEN`: its documented enablement mode requires a separate token with repository administration/pages write authority. Therefore the repository must still enable Pages with **GitHub Actions** as the publishing source through an authority that can mutate the Pages setting; then `Deploy Agnir website` must run and the public URL/assets must be verified. Source readiness and live host publication remain separate states.

## Post-1.0 adoption evidence

Svif (`iorLab/svif`) is the first recorded real-project downstream adoption case for Agnir 1.0.

Svif completed an explicit, Principal-authorized Core/profile `0.2` -> `1.0` promotion while preserving Project identity, logical lineage, selector, durable memory locators, historical 0.1/0.2 adapter support, product version, brand assets, and the immutable Preview.1 distribution boundary. Agnir records this at `.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`.

Key Svif receipts:

- captured source: `a00ad6ed9f18abddbed1979a619f932350cefe54`;
- candidate: `5a88eee4bc214b8da3b4c5f48640067b167248b8`;
- staging/full run: `34076031454` success;
- PR #9 synthetic-merge checks: `34076166897` success;
- authoritative promotion merge: `5da0eb76e38e817ba0f5111ce2b08750afa3b9c3`;
- Svif post-promotion checkpoint: `6c2c33da68e88a221ba36289d895f0423d64063a`.

No Agnir defect was exposed by the Svif adoption case. Previously satisfied v1 gates remain closed.

## Launch and adoption strategy

The Principal-approved post-v1 launch/adoption strategy is canonical at `adoption/README.md`.

- category: **Project Continuity**;
- positioning: project-owned durable continuity, not tool-owned generic AI memory;
- primary first audience: AI coding power users with fresh-session / cross-surface continuity pain;
- first proof experience: a canonical fresh-session recovery demo;
- launch sequence: hygiene → design-user adoption → technical launch → broader developer launch;
- north-star evidence: successful external cold-start resumes in Projects outside direct maintainer control;
- early adoption targets are product-learning targets, not conformance/release gates.

`brand/` remains the visual identity authority; `adoption/` owns launch, positioning, demos, community and case-study strategy; `website/` materializes approved public messaging. None of these surfaces redefines Core/profile semantics.

## Release evidence chain

- independent implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`, Release id `383536840`;
- stable arm/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable publication workflow: `34039014354`, attempts 1 and 2 success.

Agnir is now in stable maintenance + downstream adoption mode. The immediate repository change is a non-semantic public rendering/localization repair. After it is integrated and verified, the remaining host-side follow-up is Pages enablement/live verification plus the rest of Wave 0 repository metadata/feedback/license work; these are not protocol/release gates.
