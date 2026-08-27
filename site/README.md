# Sandminni / PPMP website

This directory contains the non-normative public presentation layer for **Sandminni**, the public product brand of **Persistent Project Memory (PPM)**, together with **PPMP — Persistent Project Memory Protocol** reference material. The layer identities remain distinct: Sandminni is the product brand, PPM is the reference Skill implementation, and PPMP is the protocol.

The site reads `../VERSION`, `../spec/`, `../profiles/`, `../implementations/`, `../backends/`, `../adapters/`, and `../templates/` directly during the Astro build so the repository remains the single source of truth.

Production: `https://rpm.mattamior.workers.dev`

The existing Worker/domain name is historical infrastructure and does not define protocol or product identity.

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
