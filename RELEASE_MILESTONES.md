# Agnir Release Milestones

- `v0.1.x`: established and pressure-tested the first stable Core `0.1` + repository/filesystem `0.1` profile.
- `v0.2.0`: stable pre-1.0 feature release line for Continuity Lineages. Its acceptance gates included Core `0.2` design, explicit `0.1` → `0.2` migration, materially different VCS and non-VCS backend conformance, fresh install/resume, real-Project validation, mount-boundary evidence, and an RC cycle. Historical Core/profile `0.2` remains a supported compatibility surface after 1.0 rather than being renamed in place.
- `v1.0.0`: published stability milestone. Core `1.0` + `repository-filesystem/1.0` deliberately promote the independently validated `0.2` behavior into the first long-term stable compatibility identifiers. Existing `0.2` Projects remain supported and are not forcibly rewritten; explicit semantics-preserving `0.2` → `1.0` Project promotion remains separately authorized and conformance-tested.
- `v1.0.1`: published PATCH maintenance milestone for activation/packaging reliability. It introduces dedicated `AGNIR.md` Project instructions, direct `AGENTS.md → AGNIR.md` activation, a backward-compatible README locator for `1.0.0` Projects, and explicit short commit-intent checkpoint dispatch. Core `1.0` + `repository-filesystem/1.0` remain unchanged; checkpoint no-op semantics remain unchanged.

## v1 acceptance receipts

The v1 stability milestone reached publication only after:

- clean independent-implementation `PASS` from issue #26;
- Core/profile `1.0` promotion acceptance through issue #27 / PR #28;
- immutable `v1.0.0-rc.1` at `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC publication/conformance workflow `34026167762` attempt 1 success;
- fresh immutable-source workflow `34026167762` attempt 2 success;
- RC acceptance checkpoint `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- stable staging source `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- authoritative target verification `ab5dcc3341d39631e843499632739864a90bba14`, run `34030974021`;
- publication-precondition checkpoint `b99ea0d37cca852df023ef9071d4102c0376f0fe`, run `34038863673`.

## Current publication status

`v1.0.1` is the current published latest stable repository/distribution release.

- stable tag/revision: `v1.0.1` -> `f56d25b22997c259c660651e7357334b063093e1`;
- GitHub Release id: `385176185`;
- publication workflow: `34301559338` — success;
- repository/conformance job: `102309347343` — success;
- stable publication job: `102309386242` — success;
- `releases/latest == v1.0.1`;
- previous stable `v1.0.0` remains immutable at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## v1.0.1 patch acceptance

The `1.0.1` patch was accepted after all of the following held:

- direct fresh activation succeeds through `AGENTS.md → AGNIR.md → AGNIR.yaml → selected continuity`;
- an existing `1.0.0` README-based activation route remains usable long enough to perform a compatible upgrade/repair;
- successful upgrade converges on the direct `AGNIR.md` route without changing Core/profile compatibility identifiers, Project identity, logical lineage identity, or durable continuity semantics;
- `commit` / `提交` / `提交代码` in repository context dispatches checkpoint evaluation before commit;
- a checkpoint no-op does not require artificial `.agnir/` mutation;
- Project-defined pre-commit verification remains Project policy rather than Agnir Core semantics;
- historical Core/profile `0.1` and `0.2` support remains green;
- full conformance is green on the exact candidate.

Publication of `v1.0.1` was a distinct authoritative-main transaction and did not follow automatically from implementation or PR acceptance.
