# Agnir Current State

Durable continuity belongs to the Project.

Agnir `v1.0.0` is **published, independently verified, and the latest stable release**. Ordinary stable-maintenance mode applies.

The immutable stable tag `v1.0.0` still points to exact released revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. GitHub Release id `383612171` is non-draft and non-prerelease, and `releases/latest` resolves to `v1.0.0`. Accepted RC `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## Stable compatibility state

- repository/distribution: `1.0.0`;
- Core: `1.0`;
- repository/filesystem profile: `repository-filesystem/1.0`;
- explicit Core/profile `0.2` -> `1.0` promotion remains Project-owned and separately authorized;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- installing a `1.0.x` distribution does not silently relabel an existing valid `0.2` Project.

## Brand identity integration

The Principal-approved Agnir identity system is now **authoritative on `main`**.

- integration PR: `#11`;
- final branch head before integration: `3ce946741835498d91aad9ab1eba0cfad6188e30`;
- authoritative squash-merge commit: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- post-merge conformance run: `34042053904` — success;
- post-merge repository job: `101510482659` — success;
- publication jobs on the brand merge: skipped as required.

The integrated package includes:

- approved v0.3 vector production masters under `brand/masters/`;
- byte-exact approved Agnir and family reference boards under `brand/reference/`;
- complete 13-item PNG delivery package under `brand/exports/png/`;
- QA, handoff, deterministic tooling, repository-map entries, and durable brand evidence.

The byte-exact approved-reference / PNG preservation gate is closed. The brand merge is non-semantic stable maintenance: Core 1.0, `repository-filesystem/1.0`, historical compatibility contracts, and immutable `v1.0.0` / `v1.0.0-rc.1` release tags were not changed.

The prior `brand/identity-system` branch is no longer an active integration line after PR #11. It may be retired as ordinary temporary-ref housekeeping once this authoritative checkpoint is verified.

## Release evidence chain

- independent implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`, Release id `383536840`;
- RC workflow `34026167762`, attempts 1 and 2: success;
- RC acceptance checkpoint: `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- accepted stable staging source: `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- authoritative target verification: `ab5dcc3341d39631e843499632739864a90bba14`, run `34030974021`;
- publication-precondition checkpoint: `b99ea0d37cca852df023ef9071d4102c0376f0fe`, run `34038863673`;
- stable arm/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable publication workflow: `34039014354`, attempts 1 and 2 success.

## Post-v1 housekeeping

The first safe temporary-ref retirement pass previously retired 17 completed temporary refs. Three evidence-only refs remain intentionally retained until an equally durable replacement exists:

- `release/v1.0.0-rc.1`;
- `release/v1.0.0`;
- `validation/mount-boundary-v0.2.0`.

Published release tags remain immutable. Ongoing work is ordinary stable maintenance and post-1.0 adoption evidence.