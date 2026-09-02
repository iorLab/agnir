# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Core `0.2` Parallel Continuity work is active on `feature/core-0.2-lineage` / draft PR `#5`, stacked on the VCS evidence branch `feature/multibranch-continuity` / draft PR `#4`.

## Core 0.2 active work

1. Use Svif as the first explicitly authorized real Core `0.2` consumer validation on a temporary Svif branch; do not mutate Svif `main` during the experiment.
2. Migrate the selected Svif branch from Core/profile `0.1` to `0.2` explicitly, preserving `urn:svif:project:svif-core`, all material durable truth, existing project instructions, and unrelated repository content. Verify fresh Core `0.2` discovery after migration.
3. Establish a second Svif logical lineage through an Agnir-aware VCS selector binding. Prove selector != lineage identity, independent checkpoint advancement, and fresh resume isolation after genuine divergence.
4. Exercise a real staged source→target integration in Svif. Keep the target ref unchanged while the candidate is unreconciled; reconcile target continuity from actual Project result + target truth + relevant source Evidence; publish integrated Project + target checkpoint coherently; fresh-resolve both source and target afterward.
5. Record the real-Project evidence in both Svif durable continuity and this Agnir Core `0.2` evidence line. If the real workflow exposes a model defect, fix the earliest protocol/profile layer rather than weakening conformance.
6. After Svif validation, perform a final PR `#4` / `#5` diff and CI review and build an Agnir-aware integration revision for `main`. Final `main` State / Next Actions / Decisions must be reconciled before `main` advances; do not use ordinary server-side merge-first/follow-up-repair.
7. If Core `0.2`, concrete migration, dual-backend, repository profile, and Svif real-consumer gates remain green after integration review, prepare repository `v0.2.0-rc.1`, then `v0.2.0` after release-candidate verification.
8. Keep `v1.0.0` gated by `V1_RELEASE_CRITERIA.md`: stable Core architecture, explicit compatibility/migration discipline, conformance/failure/publication integrity, multiple real Projects/execution surfaces, real upgrade evidence, independent implementability, repeatable release engineering, and an RC with no release-blocking Core defect.

## Invariants to preserve

- Durable continuity belongs to the Project.
- Project identity is not lineage identity.
- Lineage identity is logical and durable within Project scope.
- Backend selectors/bindings and revision receipts are not lineage identity.
- Lineage selection is explicit/contextual/default and never guessed by scanning siblings.
- A selected missing or mismatched binding does not silently fall back.
- Agnir-aware fork creates a new logical lineage; explicit selector rename/rebind may preserve an existing logical lineage.
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
