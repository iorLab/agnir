# Agnir Current State

Agnir `v0.2.0-rc.1` remains published as an immutable prerelease at `50a8cd565954e7e8055b8b628e2d620ac7357bab`. Its accepted Project/package changes are already reconciled into authoritative `main`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Stable v0.2.0 publication candidate — 2026-09-03

Temporary branch `release/v0.2.0` is the stable-release carrier forked from verified authoritative main checkpoint `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`.

Project identity remains `urn:agnir:project:agnir-core`. This branch self-hosts Core `0.2` / `repository-filesystem/0.2` on logical Continuity Lineage `urn:agnir:lineage:v0.2.0`, separately bound to selector `refs/heads/release/v0.2.0`. Selector and revision receipts are not lineage identity.

Repository SemVer is `0.2.0`. This is a promotion from repository prerelease `0.2.0-rc.1`; it does not introduce another Core/profile compatibility change. Core remains `0.2` and the repository/filesystem profile remains `repository-filesystem/0.2`.

## Verified stable package baseline

Stable package baseline revision `f59a83754346982170142a355a01c94050ddf3a5` (tree `2605d39fd355cd98939ac2862dcf56c2764ce29c`) passed exact-head workflow run `33711830312`.

That run passed:

- Core `0.2` repository self-host cold start;
- stable Core/profile `0.1` compatibility regression;
- VCS branch continuity and Core `0.2` VCS mapping;
- non-VCS Core `0.2` parallel continuity;
- repository-filesystem `0.2` discovery and VCS lineage binding;
- semantic and concrete Core/profile `0.1` → `0.2` migration;
- fresh Core `0.2` install plus exact published-`v0.1.1` migration/fresh resume;
- stable `v0.2.0` package gates;
- full conformance suite.

Both prerelease and stable publication jobs were skipped on that baseline because the commit message was not a publication trigger. No `v0.2.0` tag or stable Release was created by the baseline run.

## Operational provenance boundary

`extensions.agnir/operations` now records repository release `0.2.0` with `applied_revision: f59a83754346982170142a355a01c94050ddf3a5`. This is the already verified immutable package baseline actually applied to construct the publication candidate.

The final publication commit must not embed its own future SHA into content that determines that SHA. Its job is to carry the verified package plus publication-armed continuity and, after complete conformance passes, become the immutable `v0.2.0` tag target.

## Publication status

Stable `v0.2.0` is **not yet published** at this checkpoint. Published `v0.1.1` remains GitHub `latest stable` until the publication workflow successfully creates/verifies an immutable `v0.2.0` tag, a non-draft/non-prerelease GitHub Release, and `releases/latest == v0.2.0`.

The accepted RC tag remains immutable and must not move. `.agnir/next-actions.md` is the ordered resume plan.
