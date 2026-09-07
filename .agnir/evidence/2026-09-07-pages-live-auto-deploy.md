# GitHub Pages live baseline and automatic deployment — 2026-09-07

## Principal action

The Principal enabled GitHub Pages with **GitHub Actions** as the publishing source and manually dispatched `Deploy Agnir website` from authoritative `main`.

## Verified live-host baseline

GitHub Actions workflow run `34083599723` completed successfully on `main` revision `38fbeade7995021f4764762cd11b90c2092f75da`.

- workflow: `Deploy Agnir website`;
- event: `workflow_dispatch`;
- run conclusion: `success`;
- build job `101623363101`: `success`;
- deploy job `101623390599`: `success`;
- repository host readback after deployment: `has_pages=true`.

The default public host is:

`https://iorlab.github.io/agnir/`

The connected GitHub evidence establishes that Pages is enabled and the Pages artifact deployed successfully. Public browser readback remains a distinct presentation observation and should be repeated when visible site content changes materially.

## Accepted automatic deployment policy

After the successful first manual publication, the Principal approved promotion from manual-only publication to scoped automatic publication.

Accepted workflow behavior:

- automatically run on `push` to authoritative `main` only when one of these public-site inputs changes:
  - `website/**`;
  - `brand/exports/png/agnir-dark-usage.png`;
  - `brand/exports/agnir-favicon.svg`;
  - `brand/exports/png/agnir-social-card.png`;
  - `.github/workflows/pages.yml`;
- retain `workflow_dispatch` as a manual recovery/republication path;
- do not intentionally redeploy for unrelated Core, conformance, release, or continuity-only commits.

This is a repository-host/public-adoption change only. It does not change Core/profile semantics, Project identity, logical lineage identity, stable release identity, or approved brand geometry.

## Acceptance receipts

All acceptance conditions are satisfied:

1. candidate branch `maintenance/pages-auto-deploy` was current with authoritative `main` before integration (`behind_by=0`);
2. PR #33 synthetic-merge Agnir conformance run `34084048316`, repository job `101624594459` — success;
3. PR #33 was squash-merged coherently to authoritative `main` as `b781782c2c2b97f70a66e52f810d7ad18fb0395e`;
4. authoritative post-merge Agnir conformance run `34084087070`, repository job `101624702082` — success;
5. the same authoritative `main` push automatically triggered `Deploy Agnir website` run `34084087062` with event `push`;
6. automatic build job `101624702365` and deploy job `101624730737` both completed successfully.

Therefore scoped automatic GitHub Pages publication is **accepted**.

## Follow-up boundary

A continuity-only acceptance checkpoint should not match the Pages path filter. If that later checkpoint produces no Pages run while conformance succeeds, that is additional evidence that unrelated continuity maintenance does not redeploy the public website.

Remaining Wave 0 work is repository metadata/license/feedback hygiene and public adoption material, not Pages enablement or deployment automation.
