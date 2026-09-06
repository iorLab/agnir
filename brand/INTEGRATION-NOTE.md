# Brand integration note

The brand branch diverged after authoritative `main` integrated Core 0.2 Parallel Continuity. Before any brand-to-main integration, this branch must first absorb the latest `main` and then reconcile brand-local continuity under the current branch-local / integration-reconciliation semantics.

Brand assets and approved visual evidence remain valid branch-local work. Old branch snapshots of `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `AGNIR.yaml`, release metadata, or repository maps must not overwrite newer authoritative `main` truth.

## Agnir v1.0.x integration reconciliation — 2026-09-06

The brand package is now reconciled onto the published Agnir v1 stable-maintenance line. The reconciliation deliberately starts from authoritative `main` and overlays only the approved `brand/` surface plus brand-specific Evidence.

- authoritative main at reconciliation: `8b1dbe7cc1025bc500f1058b193f9bfff54bfb1b`;
- authoritative main tree: `14c36a245c5de87babeb9c057273fd1b26242514`;
- latest-main-wins two-parent reconciliation commit: `03098462d90000e387635399b73c442e589ac4ee`;
- Core/profile inherited from target: **Core 1.0 + repository-filesystem/1.0**;
- stable distribution remains **v1.0.0**; published tags are untouched;
- byte-exact reference and PNG preservation gate remains **closed**.

No brand asset changes the stable Core/profile contract, compatibility behavior, release identity, or published `v1.0.0` tag. Final integration requires current PR synthetic-merge conformance on the final head and a last `behind main = 0` check.
