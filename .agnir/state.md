# Agnir Current State

Agnir `v0.2.0` is the published latest stable repository release. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Authoritative main stable acceptance — 2026-09-03

This authoritative-main target state accepts the published stable `v0.2.0` Project/package result while preserving main's own logical Continuity Lineage `urn:agnir:lineage:authoritative`, separately bound to selector `refs/heads/main`.

Stable publication receipts are:

- immutable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id `381710267`;
- `draft=false`, `prerelease=false`;
- publication/conformance run `33711982062` success;
- GitHub `releases/latest` -> `v0.2.0`;
- stable package provenance baseline `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success.

The accepted RC remains immutable at `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

## Target reconciliation basis

Captured target main checkpoint: `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`.

Captured source release checkpoint: `2eb083d2aaa2a0869b2baf9ba46d012913317102`.

The source release lineage contributes the stable product/spec/profile/conformance/docs tree and publication Evidence. Its logical lineage `urn:agnir:lineage:v0.2.0`, selector `refs/heads/release/v0.2.0`, release-line State and release-line Next Actions are reconciliation inputs only; they are not copied as authoritative-main truth.

Main keeps Project identity `urn:agnir:project:agnir-core`, Core `0.2`, `repository-filesystem/0.2`, logical lineage `urn:agnir:lineage:authoritative`, and selector `refs/heads/main`.

## Stable product state

Repository version is `0.2.0`. Stable Core `0.2` and stable `repository-filesystem/0.2` are the active 0.2 contracts. Core/profile `0.1` artifacts remain supported compatibility/regression and explicit migration surfaces for existing `v0.1.1` Projects.

`extensions.agnir/operations` records stable package release `0.2.0` applied from immutable verified baseline `f59a837...`; the final stable tag target remains a separate publication receipt.

Real mount-boundary behavior remains explicitly unproven and execution-surface persistence remains adapter-specific. Neither is a `v0.2.0` blocker; both remain relevant to broader `v1.0.0` evidence.

`.agnir/next-actions.md` is the ordered resume plan.
