# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable. This authoritative-main target state preserves logical lineage `urn:agnir:lineage:authoritative` separately bound to `refs/heads/main`; published release lineage continuity is integration input, not main truth.

1. **Verify the exact stable-to-main integration candidate before main advancement.** Require generic Core `0.2` main self-host, Core/profile `0.1` regression, VCS/non-VCS lineage pressure, repository-filesystem `0.2`, lineage binding, both migration layers, fresh stable install/exact published-v0.1.1 migration, stable package gates and full suite.
2. **Stale-check captured refs immediately before publication.** Main must still be `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`; release source must still be `2eb083d2aaa2a0869b2baf9ba46d012913317102`. Any change invalidates the staged candidate.
3. **Advance main exactly once to the verified reconciled candidate.** Do not publish release-line `AGNIR.yaml`/State/Next first and repair afterward; do not use an ordinary PR merge as the publication primitive.
4. **Verify authoritative-main fresh resume and push CI.** Confirm main resolves Core/profile `0.2`, Project `urn:agnir:project:agnir-core`, lineage `urn:agnir:lineage:authoritative`, selector `refs/heads/main`, stable `VERSION=0.2.0`, and complete conformance.
5. **Record a post-integration main checkpoint.** Capture final main revision/run, stable tag/Release receipts and source-release checkpoint; publication jobs must remain skipped on ordinary checkpoint commits.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable `v0.2.0`, `v0.2.0-rc.1`, commits, workflow runs and durable Evidence.
7. **Continue toward `v1.0.0` through evidence rather than another fundamental redesign unless new defects require it.** Priorities include broader real Projects, execution surfaces/adapters, real upgrade experience, mount-boundary evidence where feasible, and the explicit `V1_RELEASE_CRITERIA.md` gates.

## Stable receipts

- stable tag: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- stable Release id: `381710267`;
- publication run: `33711982062` success;
- stable package baseline: `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success;
- release post-publication checkpoint: `2eb083d2aaa2a0869b2baf9ba46d012913317102`, run `33712203988` success;
- captured main target: `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Release/source continuity is reconciliation input, not automatic main truth.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- Core/profile `0.1` → `0.2` remains explicit migration.
