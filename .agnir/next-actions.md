# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Core `0.2` Parallel Continuity work is active on `feature/core-0.2-lineage` / draft PR `#5`, stacked on `feature/multibranch-continuity` / draft PR `#4`.

## Core 0.2 active work

1. **Perform a final combined review of PR `#4` and PR `#5`.** Inspect the effective diff from stable `main`, the Core/profile/migration contracts, CI gates, and all branch-local continuity that must not become authoritative `main` truth unchanged.
2. **Construct an Agnir-aware integration revision for `main`.** Stage the combined Project result without advancing `main`; reconcile final `main` Current State / Next Actions / Decisions from actual integrated Project truth, current `main` continuity, relevant feature evidence, and Principal intent; then publish the integrated Project + reconciled `main` continuity together in the target-advancing revision.
3. **Do not ordinary-merge PR `#4` or PR `#5`.** A server-side merge that first publishes feature-local `.agnir` truth and repairs it afterward violates the intended normal publication path.
4. **Run authoritative-main conformance after safe integration.** Require stable Core `0.1` regression coverage plus Core `0.2`, VCS lineage/binding, repository-filesystem `0.2`, migration, full suite, and self-host cold-start verification against the actual integrated revision.
5. **Prepare repository `v0.2.0-rc.1` if integrated main remains green.** Update release/version/docs deliberately, bind the RC to an exact revision, and exercise fresh install plus explicit `v0.1.1` → Core/profile `0.2` migration/resume before final `v0.2.0` publication.
6. **Use more real consumers rather than more synthetic lineage models by default.** Add new synthetic cases only when integration/RC/consumer evidence exposes a missing invariant or failure class.
7. **Keep Svif authoritative `main` unchanged for now.** Its temporary validation target has completed the consumer experiment, but Svif adoption of published Agnir Core `0.2` should be a separate post-publication decision.
8. Keep `v1.0.0` gated by `V1_RELEASE_CRITERIA.md`: stable Core architecture, compatibility/migration discipline, conformance/failure/publication integrity, multiple real Projects/execution surfaces, real upgrade evidence, independent implementability, repeatable release engineering, and an RC with no release-blocking Core defect.

## Completed Core 0.2 real-consumer evidence

- Svif Project: `urn:svif:project:svif-core`.
- Common baseline: `329984f94483a7cbbb21a6faa42b9cf9ed84fed2`.
- Target pre-integration: `79c5b7c7ee2ed545492702bea43d0f7135602f35`, CI `33619053159` success.
- Source: `d2d0c1bf25526b54490cce14c5aa8797c85c4d54`, CI `33618885830` success.
- Staged candidate: `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`, never target truth.
- Reconciled target: `1cd25539c75f8a2a32c84b822c0db80b176fd319`.
- Semantic self-host repair: `e48ae07faa6a716f7e2cd83cdcefdce6d02d8c7e`, CI `33619491154` success.
- Final Svif validation checkpoint: `d42489f72cc8985d353ccbf2f9b6ae7249fe6480`, CI `33619807614` 3/3 success.
- Source remained independently resumable after target integration.

## Invariants to preserve

- Durable continuity belongs to the Project.
- Project identity is not lineage identity.
- Lineage identity is logical and durable within Project scope.
- Backend selectors/bindings and revision receipts are not lineage identity.
- Lineage selection is explicit/contextual/default and never guessed by scanning siblings.
- A selected missing or mismatched binding does not silently fall back.
- Agnir-aware fork creates a new logical lineage and must publish lineage identity + selector binding + coherent inherited/reconciled continuity together.
- Explicit selector rename/rebind may preserve an existing logical lineage.
- Checkpoints are lineage-local by default.
- Source continuity is integration input, not automatic target truth.
- Integrated Project state and reconciled target continuity publish coherently.
- Stale target/source integration candidates fail rather than overwrite newer truth.
- Core `0.1` → `0.2` is explicit migration; repeated identical migration is a no-op and conflicting rebinding fails.
- Cross-Project identity mismatch remains a hard boundary.
- Stable Core `0.1` and repository `v0.1.1` remain unchanged until Core `0.2` is accepted and intentionally published.

## Current stable release

- repository release: `0.1.1`
- tag: `v0.1.1`
- exact target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
