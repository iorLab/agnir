# Wave 0 close + browser-language website default — 2026-09-07

## Scope

Reconcile authoritative Agnir continuity after the Principal completed GitHub repository-host hygiene and approved browser-language default behavior for the bilingual public website.

This checkpoint does **not** change Core/profile semantics, release identity, Project identity, logical lineage, or brand geometry.

## Repository-host Wave 0 readback

GitHub repository readback confirmed:

- topics are set to `developer-tools`, `durable-continuity`, `project-continuity`, `protocol`, and `state-management`;
- homepage remains `https://iorlab.github.io/agnir`;
- GitHub Pages remains enabled;
- Apache-2.0 is recognized;
- `delete_branch_on_merge=true` is enabled;
- branch readback after cleanup contains only `main`.

The previously retained release/validation branch refs were retired without moving or deleting published tags. Immutable release tags and accepted evidence receipts remain the release anchors.

## Browser-language website behavior

Principal request: make the public website choose the default Chinese/English surface according to the user's computer/browser language.

Accepted behavior:

- when no explicit language preference has been stored, the root English page reads the browser's first preferred UI language;
- a language beginning with `zh` redirects the root landing page to `zh-CN.html`;
- other first preferred languages remain on the English root page;
- a manual `English` / `中文` selection is persisted in same-origin `localStorage` and takes precedence on later root visits;
- directly opening `zh-CN.html` is respected as an explicit URL choice and is not auto-redirected away;
- both language pages publish `hreflang` alternates for `en`, `zh-CN`, and `x-default`.

This is presentation behavior only and does not affect Project Continuity semantics.

## Acceptance receipts

- website PR: #46 `Website: choose default language from browser preference`;
- accepted PR head: `54bf6f26dac5718f5e63dd87e7ca3c21a7d7ddd0`;
- PR conformance run: `34108478639` — success;
- authoritative squash merge: `3c493644249340290acba12655b1980008aab7fe`;
- authoritative post-merge conformance run: `34108532885` — success;
- automatic Pages run: `34108532928`;
- Pages build job: `101699091357` — success;
- Pages deploy job: `101699125085` — success;
- post-merge branch readback: only `main` remains, confirming automatic merged-head cleanup.

## Result

Repository-host Wave 0 hygiene is closed. The next public-adoption priority is the canonical 30-second fresh-session demo, followed by external design-user evidence.
