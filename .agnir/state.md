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

The Principal-approved Agnir identity system remains authoritative under `brand/`. README rendering/localization and the public website are accepted public surfaces on authoritative `main`.

Current accepted public behavior:

- English README uses approved self-contained `brand/exports/png/agnir-dark-usage.png` and keeps visible product prose English apart from language navigation and exact technical identifiers;
- Simplified Chinese README uses the same README-safe lockup and localized visible prose;
- the website no longer uses the background-bearing `agnir-dark-usage.png` in its navigation header;
- Pages now runs `brand/tools/build-production-derivatives.py` against the approved `brand/masters/agnir-mark.svg` and `brand/masters/agnir-wordmark.svg` to materialize a self-contained dark horizontal lockup with the approved particle A, white wordmark, and transparent background;
- no brand master geometry, Core/profile semantics, Project/lineage identity, stable tag, or release identity changed.

Transparent-logo repair receipts:

- PR #35 head: `361c823257effb524599905020eb94a9f02f8872`;
- PR #35 synthetic-merge conformance: run `34085855448`, repository job `101629640557` — success;
- authoritative squash merge: `16810a514620e8a62660948fb9477ba8106baceb`;
- authoritative post-merge conformance: run `34085888593`, repository job `101629727855` — success;
- automatic Pages run from that authoritative `main` push: `34085888590`;
- Pages build job `101629727838` — success;
- Pages deploy job `101629760644` — success;
- Pages artifact id `10005182999`, digest `sha256:ac4a9f5c653e15f0ba6d8e1edb7fcd22227aedbd950789d7657868378013b034`;
- artifact inspection confirms `assets/agnir-horizontal-dark.svg` contains no `<rect>` background and no external `<image>` dependency, contains the white wordmark treatment, and is self-contained.

## Public website and Pages host state

The bilingual static website source is canonical under `website/` and GitHub Pages publication is **live and automatically maintained**.

First live baseline:

- manual workflow run `34083599723` on authoritative `main` revision `38fbeade7995021f4764762cd11b90c2092f75da` — success;
- build job `101623363101` — success;
- deploy job `101623390599` — success;
- repository host readback: `has_pages=true`.

Scoped automatic publication was accepted through PR #33 and remains active. PR #35 refined the brand inputs so automatic Pages publication now follows the actual canonical site build inputs: `website/**`, `brand/masters/agnir-mark.svg`, `brand/masters/agnir-wordmark.svg`, `brand/tools/build-production-derivatives.py`, `brand/exports/png/agnir-social-card.png`, or `.github/workflows/pages.yml`. Manual `workflow_dispatch` remains available. Unrelated Core/conformance/release/continuity-only commits do not intentionally trigger website deployment.

Default public URL: `https://iorlab.github.io/agnir/`.

## Repository-host Wave 0 state

- description: set correctly;
- GitHub Pages: enabled and automatically deployed for scoped public-site changes;
- homepage metadata: set to `https://iorlab.github.io/agnir`;
- feedback path: live through GitHub Issues, with structured bug, product-idea, and adoption-report forms; both website language variants link to the issue chooser;
- topics: still empty;
- recognized repository license: absent;
- Discussions: disabled; this is not currently a feedback blocker because GitHub Issues is the accepted first external feedback surface.

The only material unfinished Wave 0 repository-host decisions are topic metadata and license/contribution presentation. License selection is a Principal/legal policy choice and must not be inferred by an Executor.

## Post-1.0 adoption evidence

Svif (`iorLab/svif`) remains the first recorded real-project downstream Agnir 1.0 adoption case. Its explicit Principal-authorized Core/profile `0.2` -> `1.0` promotion preserved Project identity, logical lineage, selector, durable memory locators, historical adapter support, product version, brand assets, and immutable distribution boundaries. No Agnir defect was exposed.

The new public adoption-report issue form is an intake surface for external evidence candidates. A submitted issue is not automatically accepted as protocol evidence; material cases still require ordinary evidence review.

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

Agnir remains in stable maintenance + downstream adoption mode. Pages, automatic deployment, transparent website branding, and external feedback intake are closed. Immediate public-adoption work is the remaining topic/license Wave 0 decisions, followed by the canonical fresh-session demo and external design-user evidence.
