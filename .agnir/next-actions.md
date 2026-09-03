# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable and safely reconciled into authoritative `main`. Main self-hosts Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`. Svif has completed a real published `v0.1.1` -> published `v0.2.0` downstream migration, and `V1_RELEASE_CRITERIA.md` records the current satisfied/open evidence map.

Read-only candidate reconnaissance on 2026-09-03 identified a concrete next evidence sequence. No candidate repository has been mutated by this reconnaissance; real-Project installation/migration requires explicit Principal authorization naming that Project.

1. **Use `iorLab/fishup` as the next real published-to-published migration candidate after explicit authorization.** It is already an Agnir Project on Core `0.1` / `repository-filesystem/0.1`, operational release `0.1.1@e9712357...`, Project identity `urn:agnir:project:fishup`, canonical `main`, and Project-owned `.agnir/` continuity. Captured read-only main was `a57b5ec7b679874af08da094fef3e8e7bdee90e3`. Its product is materially different from Agnir/Svif: a Vite/TypeScript/three.js/Rapier game deployed through Cloudflare Workers + D1 with automatic main deployment. A migration must preserve FishUp product state, existing `AGENTS.md` locator and Project instructions, deployment configuration, durable locators and unrelated decisions; use a temporary migration lineage and target-owned main reconciliation rather than mutating main first.
2. **Use `iorLab/VocaPort` as the preferred third materially different real Project after explicit authorization.** It currently has no `AGNIR.yaml`; its existing `AGENTS.md` contains independent Project rules that MUST be preserved. VocaPort is a Rust/WASM/native multi-surface application spanning Web, Desktop and Android, with durable application-session snapshots and GitHub Release automation. A fresh Agnir `v0.2.0` install should therefore pressure non-destructive bootstrap into a substantial pre-existing repository instead of another toy fixture. Do not overwrite/restructure its existing bilingual Agent/README documentation merely to add Agnir activation.
3. **Treat DSH as a separate execution-surface/adapter experiment, not as a shortcut for the real-Project count.** `iorLab/dsh-web-search-custom` is a DSH WebSearchProvider plugin and `iorLab/dsh-ui-settings-yaml` is a DSH configuration UI whose README explicitly states there is no model-visible surface. Neither repository, by itself, proves that Agnir can resume across a second Agent execution surface. To close the surface gate, run an authorized real Agnir Project through DSH (or another materially distinct Agent environment) and demonstrate fresh activation/resume/checkpoint without predecessor-private context. The DSH plugin repos currently have no `AGNIR.yaml` and were not modified during reconnaissance.
4. **Keep low-value candidates out of the v1 count.** `iorLab/imixTV` and `iorLab/novo` currently report repository size `0`; do not use empty repositories merely to inflate the real-Project metric.
5. **Pressure mount-boundary behavior when a genuine mount-capable conformance environment is available.** Keep the limitation explicit until real evidence exists; do not simulate it and then claim the boundary is proven.
6. **Obtain independent-implementation quality evidence.** Have an implementation or rigorous review reconstruct the Core/profile behavior from published specs, migration docs, conformance and repository maps without relying on private design chat history; record ambiguities as documentation/product defects rather than coaching around them.
7. **Prepare a `1.0.0-rc` cycle only after the real-Project/surface/documentation evidence gates are credibly closed.** The RC must run every normative suite from the exact candidate and must not substitute for missing real-world evidence.
8. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable `v0.2.0`, `v0.2.0-rc.1`, commits, workflow runs and durable Evidence; do not repurpose temporary refs.
9. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and migrated explicitly.

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

### Agnir downstream-evidence ingestion and gate mapping

- ingestion commit: `b1d1a8c784839aaf0822d542fdf820341d4699b2`, run `33728196706` success;
- post-evidence checkpoint: `8ca37712b9ddfa0207893ceb82c850e36f4b2fcd`, run `33728480626` success;
- v1 evidence-gap map commit: `667a4c733eddc9471d6f93d3deb2f2ea0365ebc3`, run `33728736089` success;
- all focused Core/profile/lineage/migration/fresh-install/stable-package gates and the full conformance suite remain green.

## v1 evidence status

- real upgrade boundary crossed successfully: **satisfied** via Svif published `v0.1.1` -> published `v0.2.0`;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **open** — 1 qualifying external Project evidenced; FishUp and VocaPort are the preferred next candidates, pending explicit authorization and successful evidence;
- materially different execution surfaces/adapters: **open** — DSH is a plausible next surface only if it actually operates/resumes an Agnir Project;
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
- Real evidence must come from real behavior; repository labels, empty repositories, or provider/plugin affiliation do not substitute for actual Project or execution-surface use.
