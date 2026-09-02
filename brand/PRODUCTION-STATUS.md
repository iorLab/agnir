# Agnir brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Agnir board is the sole Agnir-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Completed

- concept exploration ended;
- approved visual reference locked by exact source SHA-256;
- rejected deterministic v0.1 reconstruction removed from active branch;
- lossless source-board crops prepared for primary mark, wordmark, horizontal/vertical lockups, light/dark/monochrome examples, app-icon example, and social-card example;
- crop coordinates and derived hashes persisted for reproducible trace/QA;
- raster-board limitation recorded: board labels such as `512px` are presentation labels, not proof that a true 512px source asset exists.

## Current production gate

**Faithful vectorization only.**

A vector master may be accepted only when it is traced/reconstructed from the approved crop and visually compared with that crop. No new image generation, ribbon-based A replacement, typography substitution, palette reconciliation, particle-field redesign, or aesthetic cleanup is allowed.

The approved Agnir solo mark is the **particle-built A with central anchor** shown on the board. Until a vector master passes the trace/QA gate, extracted raster crops are reference material rather than final scalable production masters.

## Next actions

1. Faithfully trace the approved particle-built A, preserving particle hierarchy, A negative space, central anchor, and sand/light-sand distribution.
2. Trace the approved `Agnir` wordmark geometry from the board rather than selecting a merely similar font.
3. Reconstruct horizontal and vertical lockups from those traced masters and compare against their approved crop references.
4. Build light/dark/monochrome variants only from the locked master and approved examples.
5. Derive real icon exports from the approved master; do not upscale the small presentation crop and call it a source master.
6. Run visual regression at the actual target sizes.
7. Before final integration, add the byte-exact approved source image to repository storage from a binary-capable Git surface, re-resolve latest `main`, reconcile Agnir continuity, then integrate coherently.
