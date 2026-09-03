# Agnir Next Actions

Agnir stable publication candidate lineage `urn:agnir:lineage:v0.2.0` is separately bound to `refs/heads/release/v0.2.0`. Stable package baseline `f59a83754346982170142a355a01c94050ddf3a5` passed exact-head run `33711830312`; `v0.2.0` has not yet been published and `v0.1.1` remains latest stable.

1. **Publish only from the exact publication candidate after complete conformance succeeds.** The release branch commit must use the exact publication trigger and carry operational provenance pointing to verified package baseline `f59a837...`; the publication job remains downstream of the complete conformance job.
2. **Verify stable publication externally.** Confirm `refs/tags/v0.2.0` resolves directly to the exact publication candidate, the GitHub Release is `draft=false` and `prerelease=false`, and GitHub `releases/latest` resolves to `v0.2.0`. A conflicting pre-existing tag is a hard failure and must never be moved.
3. **Record post-publication facts on the moving release branch without moving the stable tag.** Capture tag target, Release id, publication workflow run, latest-stable verification, and stable package provenance in State/Evidence/RELEASE metadata as new observed facts.
4. **Reconcile the published stable result back into authoritative main.** Capture main/source receipts, stage an integration candidate without advancing main, preserve authoritative lineage `urn:agnir:lineage:authoritative` and selector `refs/heads/main`, reconcile target continuity, run candidate-tree CI, stale-check refs, then advance main once coherently.
5. **Verify authoritative main fresh resume after stable reconciliation.** Require Core/profile `0.2` self-host, stable `0.1` regression, stable install/migration gates and full suite on main.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable release tags, commits, CI runs and durable Evidence.
7. Continue broader real-Project/execution-surface evidence toward `v1.0.0` separately; stable `v0.2.0` does not imply the `v1.0.0` compatibility commitment.

## Verified receipts

- stable package baseline: `f59a83754346982170142a355a01c94050ddf3a5`;
- stable package tree: `2605d39fd355cd98939ac2862dcf56c2764ce29c`;
- stable package workflow: `33711830312` success;
- authoritative-main baseline: `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`;
- immutable accepted RC: `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`, Release id `381532232`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Repository SemVer promotion `0.2.0-rc.1` → `0.2.0` does not change Core/profile compatibility lines.
- Core/profile `0.1` → `0.2` remains explicit migration, not silent upgrade.
- Source continuity is reconciliation input, not target truth.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- Latest stable changes only after an actual stable Release is published and externally verified.
