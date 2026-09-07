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

The intended public host remains:

`https://iorlab.github.io/agnir/`

The connected GitHub evidence establishes that Pages is enabled and the Pages artifact deployed successfully. Public browser readback is a separate host observation and should continue to be checked when presentation changes materially.

## Automatic deployment policy

After the successful first manual publication, the Principal approved promotion from manual-only publication to scoped automatic publication.

Candidate workflow behavior:

- automatically run on `push` to authoritative `main` only when one of these public-site inputs changes:
  - `website/**`;
  - `brand/exports/png/agnir-dark-usage.png`;
  - `brand/exports/agnir-favicon.svg`;
  - `brand/exports/png/agnir-social-card.png`;
  - `.github/workflows/pages.yml`;
- retain `workflow_dispatch` as a manual recovery/republication path;
- do not redeploy for unrelated Core, conformance, release, or continuity-only commits.

This is a repository-host/public-adoption change only. It does not change Core/profile semantics, Project identity, logical lineage identity, stable release identity, or approved brand geometry.

## Acceptance gate

Automatic publication is accepted only after:

1. the candidate is current with authoritative `main`;
2. synthetic-merge Agnir conformance succeeds;
3. the candidate is integrated coherently into `main`;
4. authoritative post-merge Agnir conformance succeeds;
5. the Pages workflow is observed to trigger automatically from the authoritative `main` push caused by the workflow change itself;
6. that automatic Pages run completes successfully.

Until all six conditions hold, the manual live baseline remains valid but automatic deployment is only staged.
