# RPM Project State

## Purpose

RPM (Repository Project Memory) is the central, versioned specification repository for repository-backed durable memory in long-running ChatGPT projects.

The repository is the canonical source of truth for RPM rules. ChatGPT Project conversations are working memory only.

## Current status

- Current RPM specification version: 1.0.0.
- Core specification files live under `spec/`.
- Domain profiles live under `profiles/`.
- Consumer templates live under `templates/`.
- Example manifests live under `examples/`.
- This repository uses RPM for its own durable maintenance state via `.chatgpt/project-memory.yaml`.
- A dedicated ChatGPT Project is now configured as the RPM maintenance workspace.
- The RPM maintenance Project uses Project-only memory.
- Maintainer-focused Project Instructions identify `mattamior/rpm` as the authoritative specification repository and require repository bootstrap at the first substantive turn.
- A public-facing website implementation lives under `site/`. It is a non-normative presentation layer that reads `VERSION`, `spec/`, `profiles/`, and `templates/` directly at build time.
- The website is configured as a static Astro build for Cloudflare Workers Static Assets, with GitHub-integrated Workers Builds as the intended deployment path.
- The original RPM design conversation has been moved into the RPM maintenance Project for design provenance only; it is not an authoritative state source.

## Scope

This repository maintains the RPM standard itself: Core semantics, project classification, persistence rules, bootstrap behavior, manifests, versioning, profiles, templates, examples, and future migration rules.

It also maintains the public presentation layer for those materials. The website may improve discoverability, explanation, and copy workflows, but it does not define RPM semantics independently.

It does not store durable state for consuming projects such as application repositories. Each consuming repository owns its own `.chatgpt/project-memory.yaml` and project-memory artifacts.

## Operating model

- Normative RPM behavior belongs in this repository.
- Changes to RPM rules should be reflected in the relevant specification or template files and versioned according to `spec/VERSIONING.md`.
- Website content derived from normative or template material should be generated from repository sources rather than maintained as a second semantic copy.
- The dedicated ChatGPT Project is a maintenance workspace, not a second source of truth.
- Consumer projects may use Project-only memory independently; cross-project continuity should come from repositories and RPM artifacts, not implicit ChatGPT memory sharing.
- Historical design conversations may be consulted for rationale or regression analysis, but confirmed durable rules and state must live in the repository.
