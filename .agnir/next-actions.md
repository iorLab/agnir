# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable and safely reconciled into authoritative `main`. Main self-hosts Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`.

1. **Stabilize through broader real-Project evidence rather than another fundamental redesign unless a real defect demands it.** Run Core/profile `0.2` on additional Projects and record only material interoperability, migration, reconciliation, or recovery findings.
2. **Expand execution-surface / adapter evidence toward the `v1.0.0` gate.** Existing repository/filesystem and ChatGPT Project activation behavior provide a baseline; add another materially distinct execution surface/adapter with fresh activation/resume evidence.
3. **Obtain another real upgrade/migration experience from a downstream Project.** Exercise published stable `v0.2.0` install or explicit `v0.1.1`/Core `0.1` → `v0.2.0`/Core `0.2` migration outside Agnir's own repository and record observed usability/failure semantics.
4. **Pressure mount-boundary behavior when a genuine mount-capable conformance environment is available.** Keep the limitation explicit until real evidence exists; do not simulate it and then claim the boundary is proven.
5. **Review `V1_RELEASE_CRITERIA.md` against current receipts and turn remaining gaps into concrete evidence tasks.** The v1 milestone requires stronger downstream compatibility confidence, not merely another version bump.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable `v0.2.0`, `v0.2.0-rc.1`, commits, workflow runs and durable Evidence; do not repurpose temporary refs.
7. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and migrated explicitly.

## Current verified receipts

- stable tag: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- stable Release id: `381710267`;
- publication run: `33711982062` success;
- stable package baseline: `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success;
- release post-publication checkpoint: `2eb083d2aaa2a0869b2baf9ba46d012913317102`, run `33712203988` success;
- stable-to-main candidate: `08804f42262326db49fc573ca8fdf6b71b5e9734`, tree `ccbe549100cc91bd1854950bae34cf4642192ea0`;
- candidate-tree run: `33712370588` success;
- authoritative-main verification run: `33712492531` success;
- validation PR #12 auto-recognized closed/merged through exact ancestry after direct main advancement.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/release continuity is reconciliation input, not automatic target truth.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- Core/profile `0.1` → `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
