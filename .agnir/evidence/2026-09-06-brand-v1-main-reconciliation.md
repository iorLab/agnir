# Brand identity reconciliation onto Agnir v1 main — 2026-09-06

Status: **branch-local integration evidence; candidate until integrated into authoritative `main`.**

Agnir `v1.0.0` was already published and verified before this brand integration resumed. The old brand branch had diverged from current authoritative `main` by 40 commits and therefore was not eligible for direct merge.

## Reconciliation rule

The target authoritative Project truth wins. A Git-native two-parent reconciliation was constructed from exact current `main` and the prior brand head.

- prior brand head: `57bc3ffdfb2d96406ecf768bae1fce39e180ae83`;
- authoritative main: `8b1dbe7cc1025bc500f1058b193f9bfff54bfb1b`;
- authoritative main tree: `14c36a245c5de87babeb9c057273fd1b26242514`;
- resulting reconciliation commit: `03098462d90000e387635399b73c442e589ac4ee`.

The resulting tree starts from exact latest `main` and overlays only:

- the approved `brand/` tree;
- seven brand-specific Evidence records under `.agnir/evidence/`.

It deliberately does **not** reuse stale branch copies of `AGNIR.yaml`, Current State, Next Actions, Decisions, Core/profile contracts, release metadata, Skill/package surfaces, or repository documentation. Those are inherited from Agnir v1 authoritative `main`.

## v1 compatibility boundary

Brand integration is a non-semantic stable-maintenance change. It does not alter Core 1.0, `repository-filesystem/1.0`, historical 0.1/0.2 compatibility, the explicit 0.2 -> 1.0 promotion contract, or any immutable published release tag.

The byte-exact approved reference boards and complete 13-item PNG delivery package were already materialized and SHA-verified on the brand branch; that gate remains closed.

## Final gate

Before authoritative integration, require:

1. PR #11 synthetic-merge conformance green on the final brand head;
2. final comparison reports `behind main = 0`;
3. PR is mergeable against current `main`;
4. post-merge authoritative-main verification.

Documentation patch workflow run: `34041880077`.
