# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. Canonical brand integration, the Principal-approved launch/adoption strategy, the bilingual website source, and the render-safe/localized README + website repair are accepted on authoritative `main`. GitHub Pages is enabled and the first manual deployment succeeded; scoped automatic deployment is now staged.

1. **Operate in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently redefine the stable public contract.
2. **Accept scoped automatic Pages deployment.** Validate `maintenance/pages-auto-deploy` against latest `main`, require synthetic-merge conformance success, integrate coherently, require authoritative post-merge conformance success, and verify that `Deploy Agnir website` triggers automatically from the resulting authoritative `main` push and completes successfully. Retain `workflow_dispatch` as the manual recovery path.
3. **Complete the remaining Wave 0 repository-host surface.** The repository description is correct and Pages is enabled. Add the intended topics, confirm license/contribution presentation, provide an obvious external feedback path, prepare stable public share surfaces, and set the repository homepage URL to the verified Pages site when host/public readback is accepted.
4. **Produce the canonical 30-second fresh-session demo.** Demonstrate the visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary.
5. **Recruit the first external design users.** Target Projects not controlled by Agnir maintainers; verify public understanding, one-line installation, second-session value, and retention without hidden founding-context coaching.
6. **Collect material post-1.0 adoption evidence.** Svif is the first accepted real-project 0.2→1.0 promotion case. Prioritize genuine external cold-start resumes, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations. Do not reopen satisfied release gates by default.
7. **Keep the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
8. **Retire completed temporary public-surface branches when branch-deletion authority is available.** Completed maintenance branches are not product lines; their material results must first be represented on `main` and in Evidence.
9. **Keep brand production truth locked.** README, website, adoption/demo and social materials may consume canonical brand assets, but must not aesthetically reinterpret the approved Agnir identity. Material visual changes require new Principal approval.
10. **Run technical launch only after external proof exists.** Use the fresh-session value story first; use independent implementation, lineage/reconciliation, mount/storage relocation, and conformance as credibility layers after the user value is understood.
11. **Shift active product execution back to Svif where appropriate.** Svif's own canonical continuity governs its ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
12. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## GitHub Pages state

First successful manual deployment:

- run `34083599723` — success;
- build job `101623363101` — success;
- deploy job `101623390599` — success;
- source revision `38fbeade7995021f4764762cd11b90c2092f75da`;
- host readback: `has_pages=true`.

Default public URL:

`https://iorlab.github.io/agnir/`

Automatic deployment candidate triggers only on authoritative `main` changes to:

- `website/**`;
- `brand/exports/png/agnir-dark-usage.png`;
- `brand/exports/agnir-favicon.svg`;
- `brand/exports/png/agnir-social-card.png`;
- `.github/workflows/pages.yml`.

Manual `workflow_dispatch` remains enabled.

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

Intended homepage:

`https://iorlab.github.io/agnir/`

Current host state: Pages enabled; description set; homepage empty; topics empty; recognized license absent; Discussions disabled.

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

- PR #31 authoritative render-safe/localized merge: `357dccff0044a262e2bfe5a3e002fc53a49ec6ad`;
- render-safe acceptance checkpoint: `38fbeade7995021f4764762cd11b90c2092f75da`;
- checkpoint conformance: run `34082772747` — success;
- first Pages manual deployment: run `34083599723`, build `101623363101`, deploy `101623390599` — success;
- Pages/auto-deploy evidence: `.agnir/evidence/2026-09-07-pages-live-auto-deploy.md`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
- Brand assets are product surfaces, not Core semantic dependencies.
- Adoption strategy, website source and repository-host metadata are not Core semantic dependencies.
- GitHub-hosted public visual assets must be render-self-contained at the referenced/deployed path.
- Localized public prose should not accidentally mix display languages; exact technical identifiers/navigation remain allowed exceptions.
- Website source readiness, Pages enablement, deployment success, and public presentation verification are distinct observations.
- Automatic Pages deployment must be scoped to public-site inputs and authoritative `main`; unrelated Project changes must not trigger publication.
- Repository-host About/Pages metadata is not canonical Project truth.
