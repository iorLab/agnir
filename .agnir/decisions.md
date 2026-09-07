# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Checkpoint and reconciliation semantics

- A checkpoint is an authoritative continuity transition, not an activity-log append.
- Reconcile Project truth first; unchanged truth is a checkpoint no-op.
- Material checkpoints construct a coherent candidate before publication and must not expose mixed generations as coherent truth.
- Stale-base writers surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile instead of overwriting newer truth.
- A revision/checkpoint receipt is not Project identity or logical lineage identity.
- Source/staging continuity is reconciliation input, never automatic target truth.

## Compatibility and stable 1.0 policy

- Core/profile compatibility-line changes remain explicit Project-owned migration/promotion operations and must not be silently rewritten as compatible package upgrades.
- Core/profile `0.1` → `0.2` remains a published stable migration contract.
- Core/profile `0.2` → `1.0` is the stable semantics-preserving promotion governed by `spec/CORE_0_2_TO_1_0_PROMOTION.md`.
- Core `1.0` and `repository-filesystem/1.0` stabilize the accepted `0.2` semantics without behavioral redesign.
- Existing valid `0.1` and `0.2` Projects remain supported by the `1.0.x` distribution; installing the distribution is not permission to relabel them as `1.0`.
- Historical `0.1` and `0.2` normative contracts, schemas, and evidence remain immutable history/compatibility surfaces.

## Identity, lineage, and VCS binding

- Project identity and logical Continuity Lineage identity are distinct; selector/binding and revision/checkpoint receipt are separate again.
- A selected Git ref/worktree is not itself logical lineage identity.
- Agnir-aware forks preserve Project identity while establishing a new logical lineage identity and selector binding; explicit selector rename/rebind may preserve lineage identity.
- Checkpoints are lineage-local by default and must not silently mutate sibling lineages.
- Integration is target reconciliation, not source-continuity copying.

## Repository/filesystem compatibility and failure mapping

- `repository-filesystem/0.2` and `repository-filesystem/1.0` each resolve one selected logical lineage plus durable memory locators; sibling enumeration is not required for ordinary cold start.
- A multi-version distribution dispatches according to the compatibility line actually declared. A 1.0 resolver does not silently accept 0.2 as 1.0, and a 0.2 resolver does not silently accept 1.0 as 0.2.
- A string-valued incompatible `agnir.version` declaration is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing, null, or wrong scalar/container Core-version serialization is `AGNIR_DISCOVERY_INCONSISTENT`.
- Local locator escape without an authorized external Locator Chain is `AGNIR_DISCOVERY_UNRESOLVABLE`; distinguishable denied external authorization is `AGNIR_DISCOVERY_UNAUTHORIZED`.
- State/Next Actions/non-null Decisions resolve to regular files; non-null Evidence resolves to a directory; baseline Evidence discovery exposes immediate regular-file children only.

## Stable v1.0.0 publication acceptance

- Stable `v1.0.0` is accepted as published at exact authoritative arm/tag revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`.
- GitHub Release id `383612171` is the accepted non-draft, non-prerelease stable Release; `releases/latest` resolves to `v1.0.0`.
- Publication workflow `34039014354` succeeded on attempt 1 and on a fresh immutable-source attempt 2.
- Accepted RC `v1.0.0-rc.1` remains exactly `092945289f1a0a9803e4fe0583104aa380ceaadc` and is immutable release evidence.
- The v1.0.0 release gate is closed; ordinary stable maintenance now applies.
- Post-release metadata checkpoints on `main` may advance beyond the immutable `v1.0.0` tag without changing what source was released. Release identity is the tag revision, not the later continuity receipt.

## Brand identity and public presentation

- The Principal-approved Agnir visual identity is canonical Project content on `main` after PR #11.
- Agnir's locked direction is sand/warm-mineral **Structure Layer / 结构层**, with a particle-built A and central anchor. The approved reference/master assets are the visual authority; downstream derivatives are not permission to redesign them.
- Public README variants should surface the canonical Agnir lockup and explain the identity in terms consistent with the approved brand system and the product concept.
- Canonical production geometry remains under `brand/masters/`; public delivery assets remain under `brand/exports/`; approved visual authority remains documented under `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/brand-handoff.md`.
- Brand identity is a product/public surface and **does not redefine Agnir Core/profile semantics**.
- GitHub repository About description/topics are repository-host metadata, not canonical Project truth. Failure to mutate host metadata because an integration lacks metadata-write permission must be surfaced explicitly and must not be treated as a product/brand integration failure.
- GitHub-hosted README and website surfaces must use an approved **render-self-contained** visual artifact at the actual rendered/deployed path. An SVG that depends on nested relative `<image>` references is not accepted for those host surfaces unless the final rendered artifact has first been materialized without those dependencies.
- README variants use a theme-aware `<picture>` selecting the approved self-contained transparent `brand/exports/agnir-horizontal-dark.svg` or `brand/exports/agnir-horizontal-light.svg`. These exports are deterministically materialized from the approved production masters; no background rectangle or external nested `<image>` dependency is accepted on the rendered README surface.
- Website header branding uses the same accepted presentation principle: `.github/workflows/pages.yml` runs the approved deterministic `brand/tools/build-production-derivatives.py` against `brand/masters/agnir-mark.svg` and `brand/masters/agnir-wordmark.svg`, producing a self-contained dark horizontal SVG with the approved particle A, white wordmark, and **transparent background**. Deterministic materialization is not a redesign and does not create a second geometry authority.
- The background-bearing `agnir-dark-usage.png` is a usage presentation and is not the accepted inline website-header asset on a differently colored page background.
- Localized public README and website prose should stay in the language of that surface. Language-switch navigation and exact technical identifiers, filenames, commands, protocol names, or version labels are allowed exceptions; accidental bilingual display labels are not.

## Launch and adoption positioning

- The Principal-approved canonical launch/adoption strategy is `adoption/README.md`.
- Agnir's public category is **Project Continuity**. Generic “AI memory” / “agent memory” language may be used as adjacent discovery vocabulary but must not replace the product category or imply tool-owned memory semantics.
- The primary first-user value is fresh-session recovery: **the Project persists; Executors come and go**.
- Public messaging should lead with pain → outcome → Project ownership → mechanism → protocol credibility; deep protocol vocabulary should not be the first marketing experience for ordinary users.
- The first audience is AI coding power users; later audiences include Agent/IDE/tool builders and infrastructure/interoperability communities.
- Launch sequencing is Wave 0 hygiene → Wave 1 external design-user adoption → Wave 2 technical launch → Wave 3 broader developer launch.
- The adoption north star is successful external cold-start resumes in Projects outside direct maintainer control. Stars, forks and impressions are secondary signals.
- Early numeric adoption targets are product-learning targets, not conformance requirements or release gates.
- `brand/` remains the canonical visual identity authority; `adoption/` owns positioning, launch, demo, community and case-study strategy. Neither adoption copy nor host metadata may silently redefine Core/profile semantics.
- GitHub Issues is the accepted first external feedback surface. Structured bug, product-idea, and adoption-report forms may collect public reports. An adoption-report submission is an evidence candidate and requires review before it becomes accepted Agnir evidence.

## Public website boundary

- `website/` is the canonical source for the minimal Agnir public website. It is a product/adoption surface, not a Core/profile contract and not Project continuity storage.
- The website must materialize approved `adoption/` positioning rather than invent a competing product category or protocol story.
- The website must consume canonical brand truth without duplicating, redrawing, or becoming a second visual authority. Deterministic derivatives generated from approved masters by the approved production builder are allowed website artifacts when the output preserves geometry and only applies an already-approved presentation treatment.
- Website brand assets in the final Pages artifact must be self-contained at the rendered path; nested relative source dependencies must not be assumed to survive artifact construction.
- The default first host is GitHub Pages at `https://iorlab.github.io/agnir/`; this is a repository-host surface, not canonical Project truth.
- Website source readiness, Pages enablement, deployment success, artifact verification, and human visual presentation review are distinct observations.
- The first manual Pages deployment succeeded in workflow run `34083599723`, with both build and deploy successful and repository host readback reporting `has_pages=true`.
- Scoped automatic publication is accepted. `.github/workflows/pages.yml` may automatically deploy authoritative `main` pushes only when actual public-site inputs change: `website/**`, the approved mark/wordmark masters used by the builder, the deterministic builder itself, the social-card export, or the Pages workflow. Unrelated Core, conformance, release, or continuity-only commits must not trigger website publication.
- `workflow_dispatch` remains available as a manual recovery/republication path after automatic deployment is enabled.
- A custom domain is not implied or authorized by the existence of website source; custom-domain selection is a separate repository-host/brand decision.
- The root public website may use the browser's first preferred UI language only as a **default** when no explicit visitor preference is stored: `zh-*` selects `zh-CN.html`; other languages remain on English.
- Manual `English` / `中文` selection is an explicit visitor preference and may be persisted in same-origin `localStorage`; it takes precedence over later automatic root-page language detection. A direct `zh-CN.html` URL must be respected and not auto-redirected away.
- Browser-language routing and `hreflang` publication are presentation/SEO behavior only; they do not redefine Project Continuity, Core/profile semantics, or durable Project truth.

## Repository-host Wave 0 policy

- Repository description, homepage URL, topics, Pages settings, and Discussions availability are repository-host metadata, not canonical Project truth.
- The current accepted public homepage is `https://iorlab.github.io/agnir/`; host readback may omit the trailing slash while referring to the same site.
- GitHub Issues is sufficient as the first external feedback path; Discussions is optional and may remain disabled unless a later community need justifies it.
- The Principal explicitly selected **Apache License 2.0** for Agnir on 2026-09-07. Root `LICENSE` is the canonical repository license surface, and GitHub host recognition must resolve to SPDX `Apache-2.0`.
- Contributions intentionally submitted for inclusion are handled under the repository's Apache-2.0 terms unless explicitly stated otherwise; bilingual contribution guidance lives in `CONTRIBUTING.md` and `CONTRIBUTING.zh-CN.md`.
- Apache-2.0 licensing does not authorize redesign or misuse of Agnir branding; `brand/` remains the visual/trademark-usage authority.

## Post-release branch-ref retirement policy

- `main` is the sole intended long-lived authoritative branch; temporary refs should be retired after their work is completed and their material result is durably represented.
- A branch used by an open PR is not housekeeping garbage and must not be deleted merely to reduce branch count.
- A diverged evidence-only ref is retained by default when deleting it would remove the clearest durable reachability anchor for an accepted external or release checkpoint. It may be retired only after an equally durable replacement exists.
- Branch retirement must never move or delete a published release tag.
- Safe retirement may rely on merged PR history, authoritative ancestry, immutable release tags, and canonical `.agnir/evidence/` receipts to establish that the branch ref itself is no longer required.
- The completed `brand/identity-system` branch was retired after PR #11, canonical brand acceptance, README publication, exact tag verification, and a dedicated successful retirement workflow.
- As of 2026-09-07, completed non-authoritative release/validation/checkpoint/public branches were retired and repository branch readback contains only `main`. Immutable release tags plus accepted `.agnir/evidence/` receipts remain the durable release/evidence anchors.
- GitHub `delete_branch_on_merge=true` is enabled so ordinary merged head branches are retired automatically. A future branch may still be retained only when an explicit unresolved evidence need justifies it.

## Post-1.0 adoption evidence policy

- Successful downstream adoption should be recorded as evidence when it materially demonstrates compatibility/promotion behavior beyond the release test matrix.
- A downstream adoption case does not reopen satisfied v1 gates unless it exposes a real product/conformance defect.
- Svif's explicit Project-owned Agnir `0.2` → `1.0` promotion is accepted as the first recorded real-project post-v1 adoption case.
- That Svif case preserved Project identity, logical lineage, selector, memory locators, historical adapter compatibility, Svif product version, brand assets, and the immutable Preview.1 distribution boundary; no Agnir defect was exposed.

## Release and repository governance

- `v1.0.0` is a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.
- Repository `1.0.0`, Core `1.0`, and profile `repository-filesystem/1.0` align at the first stable 1.0 release while remaining distinct version axes in the architecture.
- `main` is the only intended long-lived authoritative branch. Release/validation/repair branches are temporary staging/evidence carriers and require explicit reconciliation before authoritative-main advancement.
- Published tags are immutable.
