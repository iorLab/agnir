# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. Canonical brand integration, the Principal-approved launch/adoption strategy, the bilingual website source, render-safe/localized public surfaces, GitHub Pages enablement, scoped automatic deployment, transparent website branding, and external GitHub Issues feedback intake are accepted on authoritative `main`.

1. **Operate in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently redefine the stable public contract.
2. **Close the last Wave 0 host/legal decisions.** GitHub description, Pages, homepage, and feedback intake are in place. Add the intended repository topics when host metadata authority is available. Make an explicit Principal decision on repository license before adding a license file or contribution-licensing language; do not infer a license from predecessor projects or general open-source convention.
3. **Produce the canonical 30-second fresh-session demo.** Demonstrate the visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary.
4. **Recruit the first external design users.** Target Projects not controlled by Agnir maintainers; verify public understanding, one-line installation, second-session value, and retention without hidden founding-context coaching.
5. **Collect material post-1.0 adoption evidence.** Svif is the first accepted real-project 0.2→1.0 promotion case. Use the public adoption-report issue form as an intake surface, then review material reports before accepting them as evidence. Prioritize genuine external cold-start resumes, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations.
6. **Keep the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
7. **Retire completed temporary public-surface branches when branch-deletion authority is available.** Completed maintenance branches are not product lines; their material results must first be represented on `main` and in Evidence.
8. **Keep brand production truth locked.** README, website, adoption/demo and social materials may consume approved brand assets or deterministic derivatives from approved masters, but must not aesthetically reinterpret the Agnir identity. Material visual changes require new Principal approval.
9. **Run technical launch only after external proof exists.** Use the fresh-session value story first; use independent implementation, lineage/reconciliation, mount/storage relocation, and conformance as credibility layers after the user value is understood.
10. **Shift active product execution back to Svif where appropriate.** Svif's own canonical continuity governs its ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
11. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## GitHub Pages accepted state

First successful manual deployment:

- run `34083599723` — success;
- build job `101623363101` — success;
- deploy job `101623390599` — success;
- source revision `38fbeade7995021f4764762cd11b90c2092f75da`;
- host readback: `has_pages=true`.

Accepted automatic deployment:

- PR #33 authoritative merge `b781782c2c2b97f70a66e52f810d7ad18fb0395e`;
- automatic Pages run `34084087062`, build `101624702365`, deploy `101624730737` — success;
- transparent-logo/Wave 0 feedback merge `16810a514620e8a62660948fb9477ba8106baceb`;
- post-merge conformance run `34085888593`, job `101629727855` — success;
- automatic Pages run `34085888590`, build `101629727838`, deploy `101629760644` — success.

Default public URL:

`https://iorlab.github.io/agnir/`

Automatic publication triggers only on authoritative `main` changes to:

- `website/**`;
- `brand/masters/agnir-mark.svg`;
- `brand/masters/agnir-wordmark.svg`;
- `brand/tools/build-production-derivatives.py`;
- `brand/exports/png/agnir-social-card.png`;
- `.github/workflows/pages.yml`.

The Pages build materializes `assets/agnir-horizontal-dark.svg` from approved masters using the deterministic production-derivative builder. The accepted artifact is self-contained, uses the approved white dark-treatment wordmark, has no `<rect>` background, and has no external `<image>` dependency. Manual `workflow_dispatch` remains enabled.

## GitHub About / feedback state

Description — **set**:

`Agnir — project-owned durable continuity, assembled from discoverable Project truth: state, next actions, decisions, and evidence.`

Homepage — **set**:

`https://iorlab.github.io/agnir`

Topics — **still pending**:

- `durable-continuity`
- `project-continuity`
- `state-management`
- `protocol`
- `developer-tools`

Discovery/SEO surfaces may additionally use adjacent terms such as `agent-memory`, `project-memory`, `coding-agents`, or `context-engineering` where useful, but the product category remains **Project Continuity**.

Feedback — **live**:

- GitHub issue chooser is linked from both website language variants;
- structured issue forms exist for bug reports, product ideas, and adoption reports;
- Discussions remain disabled and are not required for the current first-feedback path.

License — **Principal decision required**:

- no repository license is currently recognized;
- do not add or infer a license without explicit Principal authorization.

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

- automatic Pages acceptance checkpoint: `0ef44f9a66b26e4ab80f83dbf347d14a41d7e5ba`;
- PR #35 synthetic conformance: run `34085855448`, job `101629640557` — success;
- transparent-logo/Wave 0 feedback merge: `16810a514620e8a62660948fb9477ba8106baceb`;
- post-merge conformance: run `34085888593`, job `101629727855` — success;
- automatic Pages run: `34085888590`, build `101629727838`, deploy `101629760644` — success;
- deployed Pages artifact: id `10005182999`, digest `sha256:ac4a9f5c653e15f0ba6d8e1edb7fcd22227aedbd950789d7657868378013b034`;
- evidence: `.agnir/evidence/2026-09-07-transparent-website-logo-wave0-feedback.md`.

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
- Automatic Pages deployment must be scoped to actual public-site inputs and authoritative `main`; unrelated Project changes must not trigger publication.
- Repository-host About/Pages metadata is not canonical Project truth.
- A public adoption report is an evidence candidate, not automatic evidence acceptance.
