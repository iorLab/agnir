# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable and safely reconciled into authoritative `main`. Main self-hosts Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`. Svif has completed a real published `v0.1.1` -> published `v0.2.0` downstream migration, and `V1_RELEASE_CRITERIA.md` now records an explicit current satisfied/open evidence map.

1. **Expand the real-Project set toward the v1 minimum of 3 materially different Projects.** Svif now supplies one qualifying external real Project with both upgrade and lineage/reconciliation evidence; add at least two materially different real Projects and record only material interoperability, migration, reconciliation, recovery or usability findings.
2. **Expand execution-surface / adapter evidence toward the `v1.0.0` gate.** Existing repository/filesystem and ChatGPT Project activation behavior provide a baseline; add another materially distinct execution surface/adapter with fresh activation/resume evidence so the minimum of 2 materially different surfaces/adapters is unambiguous.
3. **Pressure mount-boundary behavior when a genuine mount-capable conformance environment is available.** Keep the limitation explicit until real evidence exists; do not simulate it and then claim the boundary is proven.
4. **Obtain independent-implementation quality evidence.** Have an implementation or rigorous review reconstruct the Core/profile behavior from published specs, migration docs, conformance and repository maps without relying on private design chat history; record ambiguities as documentation/product defects rather than coaching around them.
5. **Prepare a `1.0.0-rc` cycle only after the real-Project/surface/documentation evidence gates are credibly closed.** The RC must run every normative suite from the exact candidate and must not be used as a substitute for missing real-world evidence.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable `v0.2.0`, `v0.2.0-rc.1`, commits, workflow runs and durable Evidence; do not repurpose temporary refs.
7. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and migrated explicitly.

## Current verified receipts

### Agnir stable publication

- stable tag: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- stable Release id: `381710267`;
- publication run: `33711982062` success;
- stable package baseline: `f59a83754346982170142a355a01c94050ddf3a5`, run `33711830312` success;
- release post-publication checkpoint: `2eb083d2aaa2a0869b2baf9ba46d012913317102`, run `33712203988` success;
- stable-to-main candidate: `08804f42262326db49fc573ca8fdf6b71b5e9734`, tree `ccbe549100cc91bd1854950bae34cf4642192ea0`;
- candidate-tree run: `33712370588` success;
- authoritative-main verification run: `33712492531` success.

### Svif real published-to-published migration

- downstream Project: `iorLab/svif`, `urn:svif:project:svif-core`;
- captured source main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- source Agnir: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- target Agnir: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, run `33724859300` success;
- target-reconciled candidate/publication revision: `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`, tree `191db90c0b959254025cb061159044c1b0ddf3d6`;
- candidate run: `33725164044` success;
- authoritative Svif main push run: `33725240001` success;
- Svif post-integration checkpoint: `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648` success.

### Agnir downstream-evidence ingestion

- ingestion commit: `b1d1a8c784839aaf0822d542fdf820341d4699b2`, run `33728196706` success;
- post-evidence checkpoint: `8ca37712b9ddfa0207893ceb82c850e36f4b2fcd`, run `33728480626` success;
- focused Core/profile/lineage/migration/fresh-install/stable-package gates: success;
- full conformance suite: success;
- stable and RC publication jobs: skipped as expected.

## v1 evidence status

- real upgrade boundary crossed successfully: **satisfied** via Svif published `v0.1.1` -> published `v0.2.0`;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **open** — 1 qualifying external Project evidenced, target >=3;
- materially different execution surfaces/adapters: **open** until at least 2 are clearly evidenced;
- real mount-boundary behavior: **open / explicitly unproven**;
- independent-implementation documentation quality: **open**;
- explicit `1.0.0-rc` cycle: **future gate**.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/release continuity is reconciliation input, not automatic target truth.
- Published tags are immutable.
- Target publication is coherent and stale candidates fail.
- Core/profile `0.1` -> `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
