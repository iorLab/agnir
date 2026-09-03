# Agnir Next Actions

Agnir `v0.2.0` is published as latest stable and safely reconciled into authoritative `main`. Main self-hosts Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`. Svif has completed an authoritative published `v0.1.1` -> published `v0.2.0` downstream migration. FishUp has now completed a second real Project migration-line validation against published `v0.2.0`, while its authoritative `main` remains intentionally unchanged because every main push performs remote D1/Cloudflare deployment.

1. **Use `iorLab/VocaPort` as the preferred next materially different real Project after explicit authorization.** It currently has no `AGNIR.yaml`; its existing `AGENTS.md` contains independent Project rules that MUST be preserved. VocaPort is a Rust/WASM/native multi-surface application spanning Web, Desktop and Android, with durable application-session snapshots and GitHub Release automation. A fresh Agnir `v0.2.0` install should pressure non-destructive bootstrap into a substantial pre-existing repository instead of another migration case. Do not overwrite/restructure its existing bilingual Agent/README documentation merely to add Agnir activation.
2. **Keep FishUp authoritative-main publication separate from the completed validation.** Validated branch head is `bea8c4e6e52347e1a0164596a5a9132b17de9631`; runs `33737783270` and `33737919224` are green. Do not advance FishUp `main` under migration-validation authority alone: `.github/workflows/deploy.yml` runs remote D1 migration attempts and Cloudflare Workers deployment on every main push. If a later Principal instruction explicitly authorizes that production-affecting publication, construct a target-owned main lineage/binding candidate, re-check source/target staleness, and publish coherently rather than merging migration-line continuity directly.
3. **Treat DSH as a separate execution-surface/adapter experiment, not as a shortcut for the real-Project count.** `iorLab/dsh-web-search-custom` is a DSH WebSearchProvider plugin and `iorLab/dsh-ui-settings-yaml` is a DSH configuration UI whose README explicitly states there is no model-visible surface. To close the surface gate, run an authorized real Agnir Project through DSH (or another materially distinct Agent environment) and demonstrate fresh activation/resume/checkpoint without predecessor-private context.
4. **Pressure mount-boundary behavior when a genuine mount-capable conformance environment is available.** Keep the limitation explicit until real evidence exists; do not simulate it and then claim the boundary is proven.
5. **Obtain independent-implementation quality evidence.** Have an implementation or rigorous review reconstruct the Core/profile behavior from published specs, migration docs, conformance and repository maps without relying on private design chat history; record ambiguities as documentation/product defects rather than coaching around them.
6. **Prepare a `1.0.0-rc` cycle only after the real-Project/surface/documentation evidence gates are credibly closed.** The RC must run every normative suite from the exact candidate and must not substitute for missing real-world evidence.
7. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable releases, commits, workflow runs and durable Evidence; do not repurpose temporary refs.
8. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and migrated explicitly.

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

### Svif real published-to-published authoritative migration

- downstream Project: `iorLab/svif`, `urn:svif:project:svif-core`;
- captured source main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- source Agnir: `v0.1.1` -> `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- target Agnir: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- validated migration source: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, run `33724859300` success;
- target-reconciled publication revision: `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`, tree `191db90c0b959254025cb061159044c1b0ddf3d6`;
- candidate run: `33725164044` success;
- authoritative Svif main push run: `33725240001` success;
- Svif post-integration checkpoint: `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648` success.

### FishUp real migration-line validation

- downstream Project: `iorLab/fishup`, `urn:agnir:project:fishup`;
- captured authoritative main: `a57b5ec7b679874af08da094fef3e8e7bdee90e3`;
- source Agnir: `v0.1.1` / Core-profile `0.1`;
- validated target Agnir: `v0.2.0` / Core-profile `0.2` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- migration line first commit: `c9673cf3c20a0fa92db54c9d54413efe7fefc7ee`, tree `b2bd12f9f64e6f26abfb804b65692fa45217ca97`;
- verified checkpoint/head: `bea8c4e6e52347e1a0164596a5a9132b17de9631`, tree `1bd27517a2c663e5303bd22190129f65806426e6`;
- first run `33737783270` success; exact checkpoint run `33737919224` success;
- official published `iorLab/agnir@v0.2.0` migration/reference resolver was exercised on the actual FishUp 0.1 baseline;
- unauthorized migration rejection, authorized migration, byte-exact continuity preservation, idempotent re-apply, fresh 0.2 discovery, typecheck and build all passed;
- Draft PR FishUp #1 is validation-only and explicitly `DO NOT MERGE`;
- FishUp authoritative `main` remains on Core/profile `0.1` because production deployment was not part of the validation authorization.

### Agnir downstream-evidence ingestion and gate mapping

- Svif ingestion commit: `b1d1a8c784839aaf0822d542fdf820341d4699b2`, run `33728196706` success;
- post-Svif-evidence checkpoint: `8ca37712b9ddfa0207893ceb82c850e36f4b2fcd`, run `33728480626` success;
- v1 evidence-gap map commit: `667a4c733eddc9471d6f93d3deb2f2ea0365ebc3`, run `33728736089` success;
- candidate-shortlist checkpoint: `3564a4dd1485d3be29052f9698356202685ab31d`, run `33729266283` success.

## v1 evidence status

- real upgrade boundary crossed successfully: **satisfied** via Svif published `v0.1.1` -> published `v0.2.0` authoritative migration;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **partial** — Svif provides authoritative 0.2 downstream evidence and FishUp provides a second external real Project with verified 0.2 migration-line behavior; FishUp main acceptance is intentionally pending, and at least one additional materially different real Project remains desirable under the current readiness gate;
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
- A validated migration branch is not the same claim as authoritative target publication when a target push has additional production side effects.
