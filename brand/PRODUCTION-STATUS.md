# Agnir brand production status

Date: 2026-09-02
Branch: `brand/identity-system`
Canonical Project ref remains: `main`

## Locked input

The Principal-approved Today 10:42 AM Agnir board is the sole Agnir-only visual authority. See `APPROVED-VISUAL-REFERENCE.md` and `reference/EXTRACTION-MANIFEST.md`.

## Completed

- concept exploration ended;
- approved visual reference locked by exact source SHA-256;
- rejected deterministic v0.1 reconstruction removed from the active branch;
- lossless source-board crops prepared for primary mark, wordmark, horizontal/vertical lockups, light/dark/monochrome examples, app-icon example, and social-card example;
- crop coordinates and derived hashes persisted for reproducible trace/QA;
- raster-board limitation recorded: board labels such as `512px` are presentation labels, not proof that a true 512px source asset exists;
- `brand/masters/candidates/agnir-wordmark-trace-v0.1.svg` now contains a raster-derived trace candidate of the approved standalone `Agnir` wordmark;
- `brand/masters/candidates/agnir-mark-trace-v0.1.svg` now contains a raster-derived candidate of the approved particle-built A with central anchor.

## Current production gate

**Faithful vectorization only.**

A vector master may be accepted only when it is traced/reconstructed from the approved crop and visually compared with that crop. No new image generation, ribbon-based A replacement, typography substitution, palette reconciliation, particle-field redesign, or aesthetic cleanup is allowed.

### Candidate status

- Particle A trace: **candidate only**. The reconstruction preserves the approved particle hierarchy, pale inner A field, outer particle field, and central-anchor reading closely enough to continue QA, but it is not yet a locked master.
- Wordmark trace: **candidate only**. Geometry is derived from the locked raster reference and has been iteratively tightened; it is not yet promoted to a master.
- Lockups and derivatives: blocked until primary mark and wordmark pass the master gate.

The quality rule is explicit: **absence of a vector master is preferable to a visually drifting vector master.**

## Binary reference boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 and in the locked local reference package. They are not falsely claimed to be repository binaries. The current connector can create Git blobs from supplied base64 text, but there is no direct local-file upload bridge; final binary preservation should be completed on a Git-capable execution surface before `main` integration.

## Next actions

1. Continue visual regression on the particle-A candidate and correct only mismatches demonstrated by the approved crop.
2. Continue visual regression on the `Agnir` wordmark candidate and correct only demonstrated mismatches.
3. Reconstruct horizontal and vertical lockups only after both primary mark and wordmark are accepted masters.
4. Build light/dark/monochrome variants only from locked masters and approved examples.
5. Derive real icon exports from locked masters; do not upscale presentation crops and call them source masters.
6. Run target-size QA for repository, app, favicon, and social surfaces.
7. Before final integration, preserve the byte-exact approved source in repository storage, re-resolve latest `main`, reconcile Agnir continuity, and integrate coherently.
