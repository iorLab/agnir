# Agnir Versioning

Status: design draft

Agnir distinguishes **repository release version** from **Core compatibility version** and profile/extension compatibility versions.

## Repository release version

Repository releases use semantic versioning for the Agnir product/distribution as a whole.

- PATCH: backward-compatible fixes, documentation corrections, conformance repairs, packaging fixes, and implementation changes that do not materially expand the supported product contract.
- MINOR before 1.0: backward-compatible or intentionally pre-1.0 contract evolution, including substantial new capabilities. Parallel Continuity is intended for `v0.2.0` if its gates pass.
- MAJOR at/after 1.0: incompatible changes to the stable public contract.

Because releases below `1.0.0` signal that the public contract is still stabilizing, Agnir may introduce Core compatibility changes in a new pre-1.0 repository minor release when clearly documented and migration behavior is explicit.

## Core compatibility version

The Core compatibility version describes the normative protocol semantics an implementation or Project expects.

Examples:

- repository `v0.1.1` exposes Core `0.1`;
- intended repository `v0.2.0` may expose Core `0.2` if the new line passes conformance;
- a future repository patch/minor release may update packaging, profiles, adapters, or documentation while remaining compatible with the same Core line.

Core version changes are driven by protocol semantics, not by repository release numbering alone.

## Profile and extension versions

Profiles/extensions version their own contracts independently where appropriate. A repository release may therefore combine a stable Core with newer compatible profile/extension revisions.

## Meaning of v1.0.0

`v1.0.0` is the point at which Agnir commits to stable public compatibility and migration discipline for downstream Projects. It does not mean feature-complete in the sense of supporting every backend or platform.

The release gate is defined in `V1_RELEASE_CRITERIA.md`.
