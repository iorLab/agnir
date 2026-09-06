# Agnir Versioning

Status: active versioning policy; repository `v0.2.0` remains latest published stable while the `1.0.0` promotion/RC line is prepared.

Agnir distinguishes **repository release version** from **Core compatibility version** and profile/extension compatibility versions.

## Repository release version

Repository releases use semantic versioning for the Agnir product/distribution as a whole.

- PATCH: backward-compatible fixes, documentation corrections, conformance repairs, packaging fixes, and implementation changes that do not materially expand the supported product contract.
- MINOR before 1.0: backward-compatible or intentionally pre-1.0 contract evolution, including substantial new capabilities. Repository `v0.2.0` publishes Continuity Lineages through Core `0.2` after explicit migration, dual-backend conformance, real-Project validation, and an RC cycle.
- MAJOR at/after 1.0: incompatible changes to the stable public contract.

Because releases below `1.0.0` signal that the public contract is still stabilizing, Agnir may introduce Core compatibility changes in a new pre-1.0 repository minor release when clearly documented and migration behavior is explicit.

A repository prerelease-to-stable promotion such as `0.2.0-rc.1` → `0.2.0` or `1.0.0-rc.1` → `1.0.0` does not itself change Core/profile compatibility. Compatibility is determined by the declared Core/profile versions, not by the presence or absence of a SemVer prerelease suffix.

## Core compatibility version

The Core compatibility version describes the normative protocol semantics an implementation or Project expects.

Published/historical examples:

- repository `v0.1.1` exposes Core `0.1`;
- repository `v0.2.0` exposes Core `0.2`;
- a repository patch/minor release may update packaging, profiles, adapters, documentation, or conformance while remaining compatible with the same Core line.

The intended repository `v1.0.0` line exposes Core `1.0`. Core `1.0` is a deliberate **stability promotion of the behavior proven under Core `0.2`**, not a semantic redesign. The normative candidate is `spec/AGNIR_CORE_1_0.md`; promotion from an existing Core/profile `0.2` Project is governed by `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

Core version changes are driven by protocol compatibility semantics, not by repository release numbering alone.

## Profile and extension versions

Profiles/extensions version their own contracts independently where appropriate.

- repository `v0.2.0` combines Core `0.2` with `repository-filesystem/0.2`;
- the intended repository `v1.0.0` line combines Core `1.0` with `repository-filesystem/1.0` for fresh 1.0 Projects while continuing to ship supported historical compatibility paths.

Other adapters/extensions retain their own identifiers and compatibility rules.

## Multi-version distribution support

A repository/distribution release may support more than one Project compatibility line at once.

For the intended `1.0.x` distribution:

- existing valid Core/profile `0.1` and `0.2` Projects remain supported according to their published contracts;
- a valid `0.2` Project is dispatched to the `0.2` resolver and is **not** silently interpreted as `1.0`;
- fresh Projects intentionally adopting the stable 1.0 line declare Core `1.0` + `repository-filesystem/1.0`;
- merely installing/running a `1.0.x` distribution does not rewrite a Project's compatibility declaration.

This separates **distribution capability** from **Project compatibility identity**.

## Core/profile 0.2 → 1.0 stability promotion

Changing an existing Project's serialized declaration from Core/profile `0.2` to `1.0` crosses an explicit compatibility-identifier boundary even though the intended normative behavior is preserved.

Therefore the Project-owned promotion:

1. requires explicit Principal/policy authorization;
2. changes only the compatibility declarations unless another Project change is separately authorized;
3. preserves Project identity, logical Continuity Lineage identity, durable memory semantics/content/locators, policy, unrelated extensions, selector/binding semantics, and unrelated Project content;
4. stages and validates the complete 1.0 candidate before publication;
5. rejects stale source state instead of overwriting newer truth;
6. fresh-resolves exact Core/profile `1.0` after publication;
7. is a no-op when the same valid 1.0 target is already authoritative.

A Core/profile `0.1` Project reaches `1.0` through the existing explicit `0.1` → `0.2` migration followed by this `0.2` → `1.0` promotion; a higher-level operation must not bypass the established 0.1→0.2 lineage-migration semantics.

## Stable and prerelease resolution

`latest stable` means an actually published non-prerelease tag/release. A moving `main`, temporary promotion/release branch, RC, or untagged commit is not silently substituted for a stable release.

A prerelease target requires explicit Principal authorization. After a stable release is published successfully, upgrade resolution may advance to that stable tag according to the distribution adapter's release-resolution rules.

Published release tags are immutable by Project policy.

At the current promotion-candidate stage, `v0.2.0` remains the latest stable release. Core/profile `1.0` files present on a development/promotion branch do not make `v1.0.0` published or stable.

## Meaning of v1.0.0

`v1.0.0` is the point at which Agnir commits to stable public compatibility and migration discipline for downstream Projects. It does not mean feature-complete in the sense of supporting every backend or platform.

The intended stable version alignment is:

```text
Agnir repository v1.0.0
├── Core 1.0
└── repository-filesystem/1.0
```

Historical Core/profile `0.1` and `0.2` contracts remain immutable compatibility surfaces rather than being rewritten as 1.0 history.

The release gate is defined in `V1_RELEASE_CRITERIA.md`. An exact `1.0.0-rc` cycle remains required before stable `v1.0.0` publication.
