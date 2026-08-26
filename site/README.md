# iorMemory website

This directory contains the non-normative public presentation layer for iorMemory. The site reads canonical protocol, profile, implementation, backend, adapter, and template files directly during the Astro build so the repository remains the single source of truth.

Production currently remains at `https://rpm.mattamior.workers.dev`; the legacy Worker/repository deployment name is operational infrastructure and does not define the protocol identity.

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
