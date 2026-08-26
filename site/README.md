# RPM website

This directory contains the public presentation layer for RPM. It is intentionally non-normative: the site reads `../VERSION`, `../spec/`, `../profiles/`, and `../templates/` directly during the Astro build so the repository remains the single source of truth.

Production: `https://rpm.mattamior.workers.dev`

## Local development

```bash
cd site
npm install
npm run dev
```

## Validate a production build

```bash
npm run build
npm run check:deploy
```

## Cloudflare Workers Builds

Import `mattamior/rpm` as a Worker and configure:

- Production branch: `main`
- Root directory: `site`
- Build command: `npm run build`
- Deploy command: `npx wrangler deploy`

Cloudflare's default non-production deploy command (`npx wrangler versions upload`) can be used for preview builds.

The Worker is static-assets-only; no Worker script or runtime bindings are required.
