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

The Principal-approved Agnir identity system remains authoritative under `brand/`. The render-safe/localized README + website repair is accepted on authoritative `main`.

Accepted repair receipts:

- PR #31 final synthetic-merge conformance: run `34082518956`, repository job `101620379344` — success;
- authoritative repair merge: `357dccff0044a262e2bfe5a3e002fc53a49ec6ad`;
- authoritative repair post-merge conformance: run `34082581320`, repository job `101620553239` — success;
- final repair checkpoint: `38fbeade7995021f4764762cd11b90c2092f75da`;
- checkpoint conformance: run `34082772747` — success.

Current accepted public behavior:

- English README uses approved self-contained `brand/exports/png/agnir-dark-usage.png` and keeps visible product prose English apart from navigation/exact identifiers;
- Simplified Chinese README uses the same lockup and localized visible prose;
- website pages use the same render-safe approved PNG lockup;
- no brand master geometry, Core/profile semantics, Project/lineage identity, stable tag, or release identity changed.

## Public website and Pages host state

The bilingual static website source is canonical under `website/` and GitHub Pages publication is **live and automatically maintained**.

First live baseline:

- manual workflow run `34083599723` on authoritative `main` revision `38fbeade7995021f4764762cd11b90c2092f75da` — success;
- build job `101623363101` — success;
- deploy job `101623390599` — success;
- repository host readback after enablement: `has_pages=true`.

Scoped automatic publication was then accepted through PR #33:

- PR #33 final head: `17d26109567dd3e242854651079422a0fb858632`;
- PR synthetic-merge conformance: run `34084048316`, repository job `101624594459` — success;
- authoritative squash merge: `b781782c2c2b97f70a66e52f810d7ad18fb0395e`;
- authoritative post-merge conformance: run `34084087070`, repository job `101624702082` — success;
- automatic Pages run triggered by that same authoritative `main` push: `34084087062`;
- automatic Pages build job `101624702365` — success;
- automatic Pages deploy job `101624730737` — success.

The default public URL is `https://iorlab.github.io/agnir/`.

`.github/workflows/pages.yml` now deploys automatically on authoritative `main` only when public-site inputs change: `website/**`, the exact canonical brand exports consumed by the site, or the Pages workflow itself. Manual `workflow_dispatch` remains available. Unrelated Core/conformance/release/continuity-only commits do not intentionally trigger website deployment.

Evidence: `.agnir/evidence/2026-09-07-pages-live-auto-deploy.md`.

## Repository-host Wave 0 state

- description: set correctly;
- GitHub Pages: enabled and automatically deployed for scoped public-site changes;
- homepage metadata: still empty;
- topics: still empty;
- recognized repository license: absent;
- Discussions: disabled.

These are repository-host/adoption surfaces, not Core or release state.

## Post-1.0 adoption evidence

Svif (`iorLab/svif`) remains the first recorded real-project downstream Agnir 1.0 adoption case. Its explicit Principal-authorized Core/profile `0.2` -> `1.0` promotion preserved Project identity, logical lineage, selector, durable memory locators, historical adapter support, product version, brand assets, and immutable distribution boundaries. No Agnir defect was exposed.

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

Agnir remains in stable maintenance + downstream adoption mode. Pages enablement and scoped automatic deployment are closed. Immediate public-adoption work is the remaining Wave 0 metadata/license/feedback hygiene plus the canonical fresh-session demo and external design-user evidence.
