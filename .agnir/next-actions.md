# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. Canonical brand integration, the Principal-approved launch/adoption strategy, the bilingual website source, and the render-safe/localized README + website repair are accepted on authoritative `main`.

1. **Operate in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently redefine the stable public contract.
2. **Enable and verify GitHub Pages publication.** Fresh host readback still reports `has_pages=false`. The current connected GitHub tool surface does not expose a Pages-settings mutation or workflow-dispatch action, and official `actions/configure-pages` enablement requires separate repository-administration/pages-write authority rather than the ordinary workflow token. Select **GitHub Actions** as the Pages publishing source using an authority that can change the repository Pages setting, then run `Deploy Agnir website`, verify `https://iorlab.github.io/agnir/`, and verify English/Chinese pages plus favicon/social-card/logo loading before calling the site live.
3. **Complete the remaining Wave 0 repository-host surface.** The repository description is correct. Add the intended topics, confirm license/contribution presentation, provide an obvious external feedback path, and prepare stable public share surfaces. After Pages is live, set the repository homepage URL to the verified site.
4. **Promote the website from manual to automatic deployment only after first live verification.** Once a successful Pages publication exists, consider deploying relevant `website/` / canonical brand-export changes automatically from authoritative `main`. Do not enable automatic deployment before a live baseline is verified.
5. **Produce the canonical 30-second fresh-session demo.** Demonstrate the visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary.
6. **Recruit the first external design users.** Target Projects not controlled by Agnir maintainers; verify public understanding, one-line installation, second-session value, and retention without hidden founding-context coaching.
7. **Collect material post-1.0 adoption evidence.** Svif is the first accepted real-project 0.2→1.0 promotion case. Prioritize genuine external cold-start resumes, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations. Do not reopen satisfied release gates by default.
8. **Keep the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
9. **Retire completed temporary public-surface branches when branch-deletion authority is available.** `maintenance/readme-website-public-surface`, `maintenance/readme-render-language-cleanup`, and `maintenance/post-render-repair-checkpoint` are not product lines; their material results are or will be represented on `main` and in Evidence.
10. **Keep brand production truth locked.** README, website, adoption/demo and social materials may consume canonical brand assets, but must not aesthetically reinterpret the approved Agnir identity. Material visual changes require new Principal approval.
11. **Run technical launch only after external proof exists.** Use the fresh-session value story first; use independent implementation, lineage/reconciliation, mount/storage relocation, and conformance as credibility layers after the user value is understood.
12. **Shift active product execution back to Svif where appropriate.** Svif's own canonical continuity governs its ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
13. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Intended GitHub About metadata

Description — **currently set**:

`Agnir — project-owned durable continuity, assembled from discoverable Project truth: state, next actions, decisions, and evidence.`

Topics — **still pending**:

- `durable-continuity`
- `project-continuity`
- `state-management`
- `protocol`
- `developer-tools`

Discovery/SEO surfaces may additionally use adjacent terms such as `agent-memory`, `project-memory`, `coding-agents`, or `context-engineering` where useful, but the product category remains **Project Continuity**.

Intended homepage after Pages is live and verified:

`https://iorlab.github.io/agnir/`

Current host readback after PR #31: homepage empty; `has_pages=false`; topics empty; recognized license absent.

## Adoption targets

These are product-learning targets, not release gates:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the v1 release gate.

Canonical strategy: `adoption/README.md`.

## Recent public-surface receipts

- PR #30 public website/source merge: `4b29fb8becc0b155a2598c09b8199342e40a9e65`;
- PR #31 final head: `b7f6aac0d778a7c3082da11bb74e4da863b7215d`;
- PR #31 final synthetic-merge conformance: run `34082518956`, job `101620379344` — success;
- render-safe/localized authoritative merge: `357dccff0044a262e2bfe5a3e002fc53a49ec6ad`;
- authoritative post-merge conformance: run `34082581320`, job `101620553239` — success;
- evidence: `.agnir/evidence/2026-09-07-render-safe-public-surface.md`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
- Brand assets are product surfaces, not Core semantic dependencies.
- Adoption strategy, website source and repository-host metadata are not Core semantic dependencies.
- GitHub-hosted public visual assets must be render-self-contained at the referenced/deployed path.
- Localized public prose should not accidentally mix display languages; exact technical identifiers/navigation remain allowed exceptions.
- Website source readiness != live website publication.
- Repository-host About/Pages metadata is not canonical Project truth.
