# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. Canonical brand integration, public README branding, integrated-branch retirement, and the first post-v1 real-project adoption evidence are complete.

1. **Operate in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently redefine the stable public contract.
2. **Complete the GitHub About administrative surface.** Repository metadata is currently still `description=null` / `topics=[]` because the available GitHub Actions token has metadata read-only permission. Use a repository-admin UI/API credential to set the intended description and topics; this is host metadata only and does not alter Project truth.
3. **Continue collecting post-1.0 adoption evidence.** Svif is the first accepted real-project 0.2→1.0 promotion case. Add further adoption evidence only when it materially expands confidence; do not reopen satisfied release gates by default.
4. **Keep the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
5. **Keep brand production truth locked.** README/public derivatives may use the canonical masters, but must not aesthetically reinterpret the approved Agnir identity. Material visual changes require new Principal approval.
6. **Shift active product execution back to Svif where appropriate.** Svif's own canonical continuity governs its ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
7. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Intended GitHub About metadata

Description:

`Agnir — project-owned durable continuity, assembled from discoverable Project truth: state, next actions, decisions, and evidence.`

Topics:

- `durable-continuity`
- `project-continuity`
- `state-management`
- `protocol`
- `developer-tools`

## Recent maintenance receipts

- brand PR #11 merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- brand acceptance checkpoint: `e5305ab0474c4c8c562dbfbfaca54185b84d07f1`;
- README + brand-surface + Svif adoption commit: `75dde01da2123e731a6de461fb2f3269fd6bbbbb`;
- corresponding conformance: `34077491299` / `101606358819` success;
- About-write attempt: workflow `34077611205` / job `101606699693` failed with GitHub HTTP 403 before branch deletion because Actions had `Metadata: read` only;
- brand-branch retirement arm: `77eaada2b200b2fb3dd73309eddd259623540666`;
- retirement workflow/job: `34077763678` / `101607125525` success;
- retirement conformance: `34077763682` / `101607125572` success;
- one-shot workflow removal: `222d60c0467c0368b1aefe68b55cc01ef43cda56`;
- post-removal conformance: `34077835425` / `101607318275` success;
- Svif adoption evidence: `.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
- Brand assets are product surfaces, not Core semantic dependencies.
- Repository-host About metadata is not canonical Project truth.