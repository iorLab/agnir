# Agnir brand handoff

Status: **approved and production-materialized on `brand/identity-system`; branch-local until integrated into authoritative `main`.**

Visual authority: the Principal-approved Today 10:42 AM Agnir asset board.

## Brand idea

Agnir is the **Structure Layer / 结构层**: particles, continuity and discoverable pieces of truth. The approved identity is the sand/mineral particle-built `A` with a pale inner A and central anchor.

## Repository-resident visual references

Use these byte-exact references for source comparison:

- `brand/reference/agnir-approved-reference.png`
- `brand/reference/svif-agnir-family-approved-reference.png`

Their SHA-256 locks are recorded in `brand/APPROVED-VISUAL-REFERENCE.md` and `brand/reference/EXTRACTION-MANIFEST.md`.

## Production masters

Use these files as the approved scalable geometry masters:

```text
brand/masters/
├── agnir-mark.svg
├── agnir-wordmark.svg
├── agnir-horizontal-lockup.svg
└── agnir-vertical-lockup.svg
```

Files under `brand/masters/candidates/` are provenance/review history and are not production masters.

## Approved treatments

- Light: approved particle A with brand-color wordmark.
- Dark: approved particle A with white wordmark.
- Monochrome: grayscale mark preserving particle hierarchy and pale inner A, with black wordmark.
- App icon: approved particle mark centered in the approved square treatment.
- Social card: preserve the locked particle A, Agnir wordmark, `结构层 / Structure Layer`, bilingual continuity copy and sand-particle flow composition.

Do not replace the particle A with a solid generic A.

## Small-size rule

- 128px / 64px use the complete mark.
- 32px / 16px may deterministically prune only micro-particles below the configured visibility threshold.
- Main A geometry, major particles, pale inner A and central anchor must not change.

The deterministic rule lives in `brand/tools/build-production-derivatives.py`.

## Repository-resident delivery package

Direct SVG treatments live under `brand/exports/`. The complete 13-item PNG delivery package is committed under `brand/exports/png/`.

PNG exports are delivery derivatives; `brand/masters/` remains the geometry authority.

## Forbidden substitutions

Do not:

- regenerate the logo and substitute the result;
- infer a different font for the wordmark;
- redraw the particle field for aesthetic cleanup;
- collapse the mark to a generic A;
- reconcile Agnir colors with Svif colors;
- promote superseded v0.1/v0.2 candidates.

## Byte-exact materialization receipt

The former large-binary transport blocker is closed. GitHub Actions run `33730501685` verified the uploaded handoff archive and all source/destination SHA-256 values before committing the two approved reference boards and the complete 13-item PNG package at `a858de5c2d12f800ef6d9057f28422320ff5a012`. The transport ZIP and temporary workflow removed themselves in the same publication step.

## Integration gate

Before canonical `main` integration:

1. re-resolve latest `main` and reconcile if it moved;
2. require Draft PR `#11` Core 0.2 conformance to pass on the final head;
3. integrate brand assets/evidence coherently without replacing newer authoritative continuity/release truth;
4. fresh-verify authoritative `main` after publication.
