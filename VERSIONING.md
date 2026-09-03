# Agnir Versioning

Status: active pre-1.0 versioning policy

Agnir distinguishes **repository release version** from **Core compatibility version** and profile/extension compatibility versions.

## Repository release version

Repository releases use semantic versioning for the Agnir product/distribution as a whole.

- PATCH: backward-compatible fixes, documentation corrections, conformance repairs, packaging fixes, and implementation changes that do not materially expand the supported product contract.
- MINOR before 1.0: backward-compatible or intentionally pre-1.0 contract evolution, including substantial new capabilities. Repository `v0.2.0` publishes Continuity Lineages through Core `0.2` after explicit migration, dual-backend conformance, real-Project validation, and an RC cycle.
- MAJOR at/after 1.0: incompatible changes to the stable public contract.

Because releases below `1.0.0` signal that the public contract is still stabilizing, Agnir may introduce Core compatibility changes in a new pre-1.0 repository minor release when clearly documented and migration behavior is explicit.

A repository prerelease-to-stable promotion such as `0.2.0-rc.1` → `0.2.0` does not itself change Core/profile compatibility. Compatibility is determined by the declared Core/profile versions, not by the presence or absence of a SemVer prerelease suffix.

## Core compatibility version

The Core compatibility version describes the normative protocol semantics an implementation or Project expects.

Examples:

- repository `v0.1.1` exposes Core `0.1`;
- repository `v0.2.0` exposes Core `0.2`;
- a future repository patch/minor release may update packaging, profiles, adapters, documentation, or conformance while remaining compatible with the same Core line.

Core version changes are driven by protocol semantics, not by repository release numbering alone.

## Profile and extension versions

Profiles/extensions version their own contracts independently where appropriate. Repository `v0.2.0` combines Core `0.2` with `repository-filesystem/0.2`; other adapters/extensions retain their own identifiers and compatibility rules.

## Stable and prerelease resolution

`latest stable` means an actually published non-prerelease tag/release. A moving `main`, temporary release branch, RC, or untagged commit is not silently substituted for a stable release.

A prerelease target requires explicit Principal authorization. After a stable release is published successfully, upgrade resolution may advance to that stable tag according to the distribution adapter's release-resolution rules.

Published release tags are immutable by Project policy.

## Meaning of v1.0.0

`v1.0.0` is the point at which Agnir commits to stable public compatibility and migration discipline for downstream Projects. It does not mean feature-complete in the sense of supporting every backend or platform.

The release gate is defined in `V1_RELEASE_CRITERIA.md`.
