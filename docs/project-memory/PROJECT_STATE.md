# RPM Project State

## Purpose

RPM (Repository Project Memory) is the current central, versioned specification repository for repository-backed durable memory in long-running ChatGPT projects. RPM v1.0.0 is now also the design baseline from which a more general protocol and implementation architecture is being extracted.

The repository is the canonical source of truth for current RPM rules and maintenance decisions. ChatGPT Project conversations are working memory only.

## Current status

- Current RPM specification version: 1.0.0.
- A new architecture direction has been confirmed: separate the protocol, reference implementation, persistence backend, and platform adapters.
- The planned protocol name is **PPMP — Persistent Project Memory Protocol**.
- PPMP is intended to be platform-agnostic and storage-agnostic. Persistent/durable project memory is required, but Git or repository storage is not.
- The planned reference implementation / Skill name is **iorMemory**.
- iorMemory may initially use repository-backed persistence because it is currently the preferred implementation strategy.
- ChatGPT-specific bootstrap behavior, `.chatgpt/` conventions, Project isolation behavior, and similar mechanics are intended to move into a ChatGPT adapter rather than remain protocol requirements.
- Existing RPM v1.0.0 is treated as the repository- and ChatGPT-oriented prototype/design baseline; no normative migration to PPMP has yet been performed.
- Core specification files live under `spec/`.
- Domain profiles live under `profiles/`.
- Consumer templates live under `templates/`.
- Example manifests live under `examples/`.
- This repository uses RPM for its own durable maintenance state via `.chatgpt/project-memory.yaml`.
- A dedicated ChatGPT Project is configured as the RPM maintenance workspace and uses Project-only memory.
- A public-facing website implementation lives under `site/`. It is a non-normative presentation layer that reads `VERSION`, `spec/`, `profiles/`, and `templates/` directly at build time.
- The website is configured as a static Astro build for Cloudflare Workers Static Assets, with GitHub-integrated Workers Builds as the deployment path.
- The first production Cloudflare Workers build from `main` completed successfully on 2026-08-26 using `site` as the root directory, `npm run build` as the build command, and `npx wrangler deploy` as the deploy command.
- The production website URL is `https://rpm.mattamior.workers.dev`.
- The non-production GitHub-to-Cloudflare branch workflow was validated on 2026-08-26 using `docs/record-production-url`; Cloudflare completed the branch build/deploy successfully.

## Architecture direction

The intended conceptual layering is:

1. **PPMP** defines durable Project Memory semantics, lifecycle, state/decision/task concepts, checkpoint behavior, profiles, and compatibility without requiring a specific AI platform or storage technology.
2. **iorMemory** implements PPMP and supplies concrete persistence and operational behavior.
3. **Persistence backends** such as repository/Git storage are implementation choices beneath iorMemory rather than PPMP requirements.
4. **Platform adapters** define environment-specific discovery and bootstrap behavior, beginning with ChatGPT and potentially extending to other AI project/agent environments.

The audit of RPM v1.0.0 found that much of Core state semantics, classification, profiles, event-driven checkpoint criteria, and versioning concepts can be retained at protocol level. Repository/Git behavior, repository-relative manifest paths, `.chatgpt/` conventions, and ChatGPT conversation triggers need to be separated into implementation/backend/adapter layers.

## Scope

Until a normative migration is completed, this repository still maintains the RPM v1.0.0 standard itself: Core semantics, project classification, persistence rules, bootstrap behavior, manifests, versioning, profiles, templates, examples, and migration planning.

It also maintains the public presentation layer. The website may improve discoverability, explanation, and copy workflows, but it does not define protocol semantics independently.

## Operating model

- Current normative RPM behavior remains under `spec/`, `profiles/`, `templates/`, `examples/`, and `VERSION` until deliberately migrated.
- The PPMP/iorMemory architecture direction is durable but not yet a replacement normative specification.
- Changes to current normative behavior must follow `spec/VERSIONING.md` and assess migration impact.
- Website content derived from normative or template material should be generated from repository sources rather than maintained as a second semantic copy.
- The dedicated ChatGPT Project is a maintenance workspace, not a second source of truth.
- Historical design conversations may be consulted for rationale or regression analysis, but confirmed durable rules and state must live in the repository.
