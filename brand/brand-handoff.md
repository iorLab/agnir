# Agnir brand handoff

Status: **approved on `brand/identity-system`; branch-local until integrated into authoritative `main`.**

Visual authority: the Principal-approved Today 10:42 AM Agnir asset board recorded in `APPROVED-VISUAL-REFERENCE.md`.

## Brand idea

Agnir is the **Structure Layer / 结构层**.

- 微粒、连续性、可发现的真相碎片
- Particles, continuity, discoverable pieces of truth

The Agnir identity is a sand/mineral particle-built `A` with a central anchor. It is distinct from Svif while sharing the family particle-and-geometry language.

## Production masters

Use these files as the branch-approved scalable masters:

```text
brand/masters/
├── agnir-mark.svg
├── agnir-wordmark.svg
├── agnir-horizontal-lockup.svg
└── agnir-vertical-lockup.svg
```

- `agnir-mark.svg`: approved particle A geometry and color distribution.
- `agnir-wordmark.svg`: approved smooth outline wordmark; no runtime font dependency.
- horizontal / vertical lockups: self-contained compositions, not external candidate references.

Files under `brand/masters/candidates/` are provenance/review history and are **not** production masters.

## Approved treatments

### Light background

Use the approved particle A with the Agnir brand-color wordmark. Current production derivative uses `#C2812E` for the wordmark, matching the approved light-background treatment.

### Dark background

Use the approved particle A with a white wordmark on a dark neutral/navy surface.

### Monochrome

Convert mark colors to grayscale while preserving particle hierarchy and the pale inner A; use a black wordmark on a light surface.

Do not replace the particle A with a solid generic `A`.

## Small-size assets

The approved asset board defines favicon sizes down to 16px. The complete micro-particle field is not readable when naively shrunk to that size.

Rules:

- 128px and 64px: use the complete mark.
- 32px: deterministic pruning may remove only particles below the configured visibility threshold.
- 16px: a stronger deterministic visibility threshold may be used.
- never change the main A geometry, major particles, pale inner A, or central anchor for small-size use.
- small-size pruning is a functional derivative, not a new logo design.

The deterministic rule lives in `brand/tools/build-production-derivatives.py`.

## App / repository / avatar usage

- App icon: approved particle mark centered in a white rounded square.
- Repository icon / GitHub avatar: prefer the mark-only treatment with generous clear space; use the app-icon treatment where a square icon surface is required.
- Avoid embedding the full wordmark in very small avatars.

## Social card

The approved board shows a light social-card treatment with:

- particle A on the left;
- black Agnir wordmark;
- `结构层 / Structure Layer`;
- the bilingual continuity/tagline copy;
- a sand-particle flow treatment on the right.

A production social card must preserve that composition rather than invent a new campaign style.

## QA

Principal-facing review must be clean: no blue artwork-bound boxes or diagnostic overlays. Engineering diagnostics are explicit-only and must never be mistaken for brand artwork.

All review placement uses `contain`, never crop/cover.

## Forbidden substitutions

Do not:

- regenerate the logo with image generation and substitute the result;
- infer or substitute a different font for the wordmark;
- redraw the particle field for aesthetic cleanup;
- collapse the mark to a generic `A`;
- reconcile Agnir colors with Svif colors;
- treat superseded v0.1/v0.2 candidate files as masters.

## Rebuilding derivatives

Run from a repository checkout:

```bash
python brand/tools/build-production-derivatives.py --repo . --out brand/exports
```

With CairoSVG installed, add `--png` to render icon PNG exports.

## Integration gate

Before merging this brand work to canonical `main`:

1. preserve the byte-exact approved 10:42 AM source board in repository storage;
2. run final target-size QA for the derivative package;
3. re-resolve latest `main` and reconcile branch-local Agnir evidence/state;
4. integrate assets and continuity coherently;
5. verify from `main` after publication.
