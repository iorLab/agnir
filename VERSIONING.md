# Agnir Versioning

Status: active versioning policy. Published non-prerelease tag `v1.0.1` is the current latest stable repository/distribution release. It uses the same Core `1.0` + `repository-filesystem/1.0` compatibility line as `v1.0.0`.

Agnir distinguishes **repository release version** from **Core compatibility version** and profile/extension compatibility versions.

## Repository release version

Repository releases use semantic versioning for the Agnir product/distribution as a whole.

- PATCH: backward-compatible fixes, documentation corrections, conformance repairs, packaging fixes, and implementation changes that do not materially expand the supported product contract.
- MINOR: backward-compatible product-contract expansion after 1.0 when new supported capability is materially added without breaking the existing contract.
- MAJOR at/after 1.0: incompatible changes to the stable public contract.

A repository prerelease-to-stable promotion such as `1.0.0-rc.1` → `1.0.0` does not itself change Core/profile compatibility. Compatibility is determined by the declared Core/profile versions, not by the presence or absence of a SemVer prerelease suffix.

## v1.0.1 activation/packaging patch

Repository `1.0.1` is a published PATCH-level distribution evolution over `1.0.0`. Its scope is deliberately narrow:

- introduce root `AGNIR.md` as the canonical Executor-facing Project activation and operation surface;
- keep `AGENTS.md` locator-only and point it directly to `AGNIR.md`;
- retain README `Agnir Project Instructions` as a backward-compatible locator for pre-upgrade `1.0.0` Projects rather than a second procedure copy;
- preserve the legacy `AGENTS.md → README` route long enough to activate an existing `1.0.0` Project safely before compatible upgrade/repair;
- make short repository-context `commit` / `提交` / `提交代码` intent dispatch explicitly pass through checkpoint evaluation before VCS commit;
- keep checkpoint no-op semantics intact: checkpoint evaluation is required, `.agnir/` mutation is not;
- keep Project-defined pre-commit verification separate from Agnir Core checkpoint semantics;
- update Skill/conformance/packaging so fresh install and `1.0.0` → `1.0.1` upgrade converge on the direct `AGENTS.md → AGNIR.md → AGNIR.yaml` route.

This patch **does not** introduce Core `1.1`, `repository-filesystem/1.1`, a new Project identity model, a new Continuity Lineage model, or new checkpoint semantics. Existing Core/profile compatibility declarations do not change merely because the `1.0.1` distribution is installed.

Published stable source: `v1.0.1` -> `f56d25b22997c259c660651e7357334b063093e1`.

## Core compatibility version

The Core compatibility version describes the normative protocol semantics an implementation or Project expects.

Published/supported lines include:

- repository `v0.1.1` exposes Core `0.1`;
- repository `v0.2.0` exposes Core `0.2`;
- repository `v1.0.0` exposes stable Core `1.0` for fresh/promoted 1.0 Projects while retaining support for historical `0.1` and `0.2` Projects;
- repository `v1.0.1` exposes the same Core `1.0` semantics; its changes are distribution/activation packaging only.

Core `1.0` is a deliberate **stability promotion of the behavior proven under Core `0.2`**, not a semantic redesign. The stable normative contract is `spec/AGNIR_CORE_1_0.md`; promotion from an existing Core/profile `0.2` Project is governed by `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

Core version changes are driven by protocol compatibility semantics, not by repository release numbering alone.

## Profile and extension versions

Profiles/extensions version their own contracts independently where appropriate.

- repository `v0.2.0` combines Core `0.2` with `repository-filesystem/0.2`;
- repository `v1.0.0` combines Core `1.0` with stable `repository-filesystem/1.0` for fresh/promoted 1.0 Projects while continuing to ship supported historical compatibility paths;
- repository `v1.0.1` keeps `repository-filesystem/1.0` unchanged.

Other adapters/extensions retain their own identifiers and compatibility rules.

## Multi-version distribution support

A repository/distribution release may support more than one Project compatibility line at once.

For the `1.0.x` distribution:

- existing valid Core/profile `0.1` and `0.2` Projects remain supported according to their published contracts;
- a valid `0.2` Project is dispatched to the `0.2` resolver and is **not** silently interpreted as `1.0`;
- fresh Projects intentionally adopting the stable 1.0 line declare Core `1.0` + `repository-filesystem/1.0`;
- merely installing/running a `1.0.x` distribution does not rewrite a Project's compatibility declaration.

This separates **distribution capability** from **Project compatibility identity**.

## Core/profile 0.2 → 1.0 stability promotion

Changing an existing Project's serialized declaration from Core/profile `0.2` to `1.0` crosses an explicit compatibility-identifier boundary even though the normative behavior is preserved.

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

The accepted `v1.0.0-rc.1` is release evidence and remains immutable prerelease history; it never substitutes for stable resolution.

Publication created the non-prerelease `v1.0.1` tag/Release at exact stable source revision `f56d25b22997c259c660651e7357334b063093e1`; stable resolution now selects `v1.0.1`. Previous stable `v1.0.0` remains immutable history at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. Published release tags are immutable by Project policy.

## Meaning of the 1.0 line

`v1.0.0` is the point at which Agnir committed to stable public compatibility and migration discipline for downstream Projects. Patch releases such as `v1.0.1` may harden implementation, documentation, activation, packaging, and conformance without changing the stable Core/profile contract.

The compatibility alignment remains:

```text
Agnir repository 1.0.x
├── Core 1.0
└── repository-filesystem/1.0
```

Historical Core/profile `0.1` and `0.2` contracts remain immutable compatibility surfaces rather than being rewritten as 1.0 history.
