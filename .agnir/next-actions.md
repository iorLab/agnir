# Agnir Next Actions

Agnir stable candidate branch `release/v0.2.0` self-hosts Core `0.2` / `repository-filesystem/0.2` as logical lineage `urn:agnir:lineage:v0.2.0`, separately bound to `refs/heads/release/v0.2.0`. It is based on authoritative main `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`. Published `v0.2.0-rc.1` remains immutable; `v0.1.1` remains latest stable until stable publication actually succeeds.

1. **Complete the stable package promotion.** Promote Core/profile status from RC candidate to stable normative `0.2`; update bilingual README, RELEASE, VERSIONING and repository-tree status; add generic Core `0.2` self-host and stable release gates; keep Core/profile `0.1` compatibility artifacts and regression coverage.
2. **Pass exact-head stable-package CI.** Require Core `0.2` self-host, stable Core/profile `0.1` regression, VCS/lineage/profile/migration pressure, fresh Core `0.2` install, exact published-v0.1.1 migration/fresh resume, stable-package metadata checks, and full suite.
3. **Establish an immutable verified stable operational-package baseline.** After the stable package is green, use that exact revision as `agnir/operations.applied_revision` for repository release `0.2.0`; do not use the final publication commit's self-referential SHA.
4. **Construct the exact publication candidate.** Record stable package provenance and publication-armed continuity without changing Core/profile semantics; run exact-head conformance again.
5. **Publish immutable `v0.2.0` only after the publication candidate is green.** The publication job must be gated on the exact release ref and exact commit message, fail closed if a conflicting tag already exists, create/verify a non-prerelease/non-draft Release, and verify GitHub `releases/latest` resolves to `v0.2.0`.
6. **Record post-publication facts on the moving release branch without moving the stable tag.** Capture tag target, Release id, publication run, and latest-stable verification in State/Evidence.
7. **Reconcile published stable results back into authoritative main.** If the stable release branch tree differs from main, use the same target-first staged reconciliation: capture main/source receipts, stage candidate without main advancement, reconcile authoritative-main continuity, validate exact tree, stale-check refs, then advance main once coherently.
8. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Never delete or move immutable release tags.
9. Continue broader evidence toward `v1.0.0` separately; stable `v0.2.0` does not imply the `v1.0.0` compatibility commitment.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Repository SemVer promotion `0.2.0-rc.1` → `0.2.0` does not change Core/profile compatibility lines.
- Core/profile `0.1` → `0.2` remains explicit migration, not silent upgrade.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- A prerelease is not latest stable; latest stable changes only after an actual stable Release is published.
