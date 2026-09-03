# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable at immutable tag target `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, GitHub Release id `381710267`. Release lineage `urn:agnir:lineage:v0.2.0` remains separately bound to `refs/heads/release/v0.2.0`; authoritative main is a different logical lineage.

1. **Reconcile published stable `v0.2.0` back into authoritative main.** Capture exact main and release-line receipts, use the post-publication release tree as Project/package input, preserve main logical lineage `urn:agnir:lineage:authoritative` and selector `refs/heads/main`, and treat release continuity as reconciliation input rather than target truth.
2. **Stage the main integration candidate without advancing main.** Construct the exact integrated Project tree plus reconciled main State/Next/Evidence, then verify candidate-tree Core/profile `0.2` self-host, Core/profile `0.1` regression, VCS/non-VCS lineage pressure, stable install/migration gates and full suite.
3. **Stale-check main and release receipts immediately before publication.** Any advancement invalidates the candidate and requires re-resolution/reconciliation.
4. **Advance main exactly once to the verified reconciled candidate.** Do not use an ordinary PR merge that would publish release-line continuity first and repair later.
5. **Verify authoritative-main fresh resume and CI.** Confirm main resolves `urn:agnir:lineage:authoritative` bound to `refs/heads/main`, stable release metadata remains `v0.2.0`, and the stable tag remains at `fc84095...`.
6. **Record a post-integration main checkpoint.** Capture authoritative-main integration revision/run and retain stable publication receipts.
7. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Never move/delete published stable or RC tags.
8. Continue broader real-Project/execution-surface evidence toward `v1.0.0`; `v0.2.0` is a stable pre-1.0 feature release, not the v1 compatibility commitment.

## Verified stable receipts

- stable package baseline: `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success;
- immutable stable tag: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- stable Release id: `381710267`;
- publication/conformance run: `33711982062` success;
- post-publication `releases/latest`: `v0.2.0`;
- immutable accepted RC: `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/release continuity is reconciliation input, not automatic main truth.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- Core/profile `0.1` → `0.2` remains explicit migration.
