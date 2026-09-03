# Agnir Current State

Agnir `v0.2.0` is the published latest stable repository release and its accepted stable Project/package result is now safely reconciled into authoritative `main`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Stable release

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id `381710267`;
- `draft=false`, `prerelease=false`;
- publication/conformance run `33711982062` success;
- GitHub `releases/latest` -> `v0.2.0`;
- stable package provenance baseline `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success.

The accepted RC remains immutable at `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

## Authoritative-main stable reconciliation — verified 2026-09-03

Captured target main was `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`. Captured release source was post-publication checkpoint `2eb083d2aaa2a0869b2baf9ba46d012913317102`.

A reconciled two-parent candidate was constructed before main advancement:

- candidate revision: `08804f42262326db49fc573ca8fdf6b71b5e9734`;
- candidate tree: `ccbe549100cc91bd1854950bae34cf4642192ea0`;
- first parent: captured main `1af33e0...`;
- second parent: release checkpoint `2eb083d2...`.

The candidate kept Project identity `urn:agnir:project:agnir-core`, authoritative logical lineage `urn:agnir:lineage:authoritative`, and selector `refs/heads/main`; release-line lineage/binding/State/Next remained reconciliation input rather than target truth.

Draft PR #12 existed only to run candidate-tree CI. Candidate run `33712370588` passed every focused gate and the full suite. GitHub's synthetic merge commit used the exact same tree `ccbe549100cc91bd1854950bae34cf4642192ea0`.

Immediately before publication, main, release and integration refs were re-read and still matched the captured receipts. Main then advanced exactly once from `1af33e0...` directly to `08804f...`; no ordinary PR merge was used as the publication primitive.

Authoritative-main push run `33712492531` passed Core `0.2` self-host, Core/profile `0.1` regression, VCS/non-VCS lineage pressure, both migration layers, fresh install/published-v0.1.1 migration, stable package gates and the full suite. Both release publication jobs were skipped. PR #12 was subsequently auto-recognized closed/merged by exact ancestry.

## Active compatibility and product state

Repository version is `0.2.0`. Stable Core `0.2` and stable `repository-filesystem/0.2` are active. Core/profile `0.1` artifacts remain compatibility/regression and explicit migration surfaces for existing `v0.1.1` Projects.

Authoritative main self-hosts logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`. `extensions.agnir/operations` records stable package release `0.2.0` applied from immutable verified baseline `f59a837...`.

Real mount-boundary behavior remains explicitly unproven, and execution-surface persistence remains adapter-specific. Neither blocked `v0.2.0`; they remain relevant evidence toward `v1.0.0`.

`.agnir/next-actions.md` is the ordered resume plan.
