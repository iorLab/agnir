# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. Canonical brand integration, public README branding, integrated-branch retirement, the first post-v1 real-project adoption evidence, the Principal-approved launch/adoption strategy, theme-aware README repair, and a bilingual website source are complete or staged for authoritative integration.

1. **Operate in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently redefine the stable public contract.
2. **Finish and integrate the README/website public-surface change.** Verify final staged diff, run synthetic-merge checks, squash the coherent Project + continuity result to authoritative `main`, then run post-merge conformance. Retire `maintenance/readme-website-public-surface` after the material result is canonical.
3. **Enable and verify GitHub Pages publication.** In repository Settings → Pages, set the publishing source to **GitHub Actions**. Then run `Deploy Agnir website` from `.github/workflows/pages.yml`, verify the live default URL `https://iorlab.github.io/agnir/`, verify both English and Simplified Chinese pages plus favicon/social-card asset loading, and only then describe the website as live.
4. **Complete Wave 0 launch hygiene.** Finish the GitHub About administrative surface, confirm license/contribution presentation, provide an obvious external feedback path, and prepare stable public share surfaces. Repository metadata is currently still `description=null` / `topics=[]` because the available GitHub Actions token has metadata read-only permission; use repository-admin UI/API authority for that host-only change. After Pages is live, set the repository homepage URL to the verified site.
5. **Promote the website from manual to automatic deployment only after first live verification.** Once a successful Pages publication exists, consider changing `.github/workflows/pages.yml` to deploy relevant `website/` / canonical brand-export changes on authoritative `main` pushes. Do not enable automatic deployment before the first live surface is verified.
6. **Produce the canonical 30-second fresh-session demo.** Demonstrate the user-visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary; the website already reserves the public narrative slot for this story.
7. **Recruit the first external design users.** Target Projects not controlled by Agnir maintainers; verify public understanding, one-line installation, second-session value, and retention without hidden founding-context coaching.
8. **Collect material post-1.0 adoption evidence.** Svif is the first accepted real-project 0.2→1.0 promotion case. Prioritize genuine external cold-start resumes, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations. Do not reopen satisfied release gates by default.
9. **Keep the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
10. **Keep brand production truth locked.** README, website, adoption/demo and social materials may consume canonical brand assets, but must not aesthetically reinterpret the approved Agnir identity. Material visual changes require new Principal approval.
11. **Run technical launch only after external proof exists.** Use the fresh-session value story first; use independent implementation, lineage/reconciliation, mount/storage relocation, and conformance as credibility layers after the user value is understood.
12. **Shift active product execution back to Svif where appropriate.** Svif's own canonical continuity governs its ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
13. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Intended GitHub About metadata

Description:

`Agnir — project-owned durable continuity, assembled from discoverable Project truth: state, next actions, decisions, and evidence.`

Topics:

- `durable-continuity`
- `project-continuity`
- `state-management`
- `protocol`
- `developer-tools`

Discovery/SEO surfaces may additionally use adjacent terms such as `agent-memory`, `project-memory`, `coding-agents`, or `context-engineering` where useful, but the product category remains **Project Continuity**.

Intended homepage after Pages is live and verified:

`https://iorlab.github.io/agnir/`

## Adoption targets

These are product-learning targets, not release gates:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the v1 release gate.

Canonical strategy: `adoption/README.md`.

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
- Svif adoption evidence: `.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`;
- launch/adoption strategy evidence: `.agnir/evidence/2026-09-07-launch-adoption-strategy.md`;
- README/website public-surface evidence: `.agnir/evidence/2026-09-07-readme-website-public-surface.md`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
- Brand assets are product surfaces, not Core semantic dependencies.
- Adoption strategy, website source and repository-host metadata are not Core semantic dependencies.
- Website source readiness != live website publication.
- Repository-host About/Pages metadata is not canonical Project truth.
