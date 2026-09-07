# Brand integration note

The brand identity work originally diverged while authoritative `main` continued to advance through Core 0.2, Core/profile 1.0 promotion, and the stable v1 release. Integration therefore used latest-main-wins reconciliation: brand-local continuity and stale release/Core/profile snapshots were never allowed to overwrite newer authoritative Project truth.

## Agnir v1.0.x integration reconciliation — 2026-09-06

The brand package was reconciled onto the published Agnir v1 stable-maintenance line. The reconciliation deliberately started from authoritative `main` and overlaid only the approved `brand/` surface plus brand-specific Evidence.

- authoritative main at reconciliation: `8b1dbe7cc1025bc500f1058b193f9bfff54bfb1b`;
- authoritative main tree: `14c36a245c5de87babeb9c057273fd1b26242514`;
- latest-main-wins two-parent reconciliation commit: `03098462d90000e387635399b73c442e589ac4ee`;
- Core/profile inherited from target: **Core 1.0 + repository-filesystem/1.0**;
- stable distribution remains **v1.0.0**; published tags are untouched;
- byte-exact reference and PNG preservation gate is **closed**.

## Final canonical integration

PR #11 is merged and the brand system is now canonical on authoritative `main`.

- final branch head: `3ce946741835498d91aad9ab1eba0cfad6188e30`;
- authoritative squash merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- post-merge conformance run: `34042053904` — success;
- repository job: `101510482659` — success;
- post-integration canonical checkpoint: `e5305ab0474c4c8c562dbfbfaca54185b84d07f1`.

No brand asset changes the stable Core/profile contract, compatibility behavior, release identity, or published `v1.0.0` / `v1.0.0-rc.1` tags. The former `brand/identity-system` branch is no longer an active product line and may be retired after this canonical result is durably recorded.