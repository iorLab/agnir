# PPMP Maintenance State

## Purpose

This repository is the historical RPM repository and the current canonical development repository for PPMP v2. It maintains the protocol, the Persistent Project Memory (PPM) reference Skill boundary, persistence backends, platform adapters, profiles, templates, examples, migration rules, and the public presentation layer.

## Current status

- Current protocol version: **PPMP 2.0.0**.
- Public protocol identity: **PPMP — Persistent Project Memory Protocol**.
- Initial reference Skill/implementation: **Persistent Project Memory (PPM)**.
- Public product brand for the reference implementation: **Sandminni**.
- Reference implementation machine identity: `persistent-project-memory`.
- Sandminni's brand metaphor is memory accumulated grain by grain; future visual identity should explore sand/grains, convergence or accumulation, and memory/durable continuity.
- The non-normative public website now presents **Sandminni** as the product brand while keeping **PPM** as the technical implementation identity and **PPMP** as the protocol; the historical `rpm` Worker/domain naming remains infrastructure only.
- RPM (Repository Project Memory) v1.0.0 is the historical repository- and ChatGPT-oriented predecessor.
- The v2 architecture separates protocol semantics, implementation behavior, persistence backends, and platform adapters.
- PPMP is platform-agnostic and storage-agnostic. Persistence is required; Git/repository storage is not.
- The initial PPM stack uses the repository backend and ChatGPT adapter to preserve the practical RPM v1 workflow.
- Normative protocol files live under `spec/`; reusable profiles under `profiles/`; reference serialization under `templates/` and `examples/`.
- Implementation, backend, and adapter contracts live under `implementations/`, `backends/`, and `adapters/`.
- This repository uses PPM with the repository backend and ChatGPT adapter for its own maintenance memory under `docs/project-memory/` and is classified as `software` because recurring work includes specification tooling, website code, build/deployment integration, and implementation/backend maintenance.
- The public website remains a non-normative presentation layer and is deployed through Cloudflare Workers from the repository.
- The first real consuming-project migration has been exercised against `mattamior/tree-hole`: its RPM v1 memory was migrated explicitly to PPMP v2 / PPM while preserving the existing root-level durable files. Repository/build validation succeeded and no executable application source changed during the migration.
- That consuming migration exposed a reusable repository-backend hazard: memory-only commits can trigger unrelated production CI/CD in repositories that deploy every successful main push. The reference repository backend now instructs implementations to minimize those side effects, coalesce logical checkpoints when practical, and keep persistence verification distinct from release verification.
- The repository now has path-scoped GitHub **Site CI** at `.github/workflows/site-ci.yml`. Run `33050210045` on commit `13a8bbce8801a1b9c6201b11284e5081988d8ada` completed successfully, including dependency installation, Astro build, and `wrangler deploy --dry-run`. This verifies site build and Worker packaging, but not live Cloudflare production availability or browser interactions.

## Architectural boundary

1. **PPMP** defines durable Project Memory semantics, lifecycle, classification, checkpoint behavior, profiles, and compatibility.
2. **Persistent Project Memory (PPM)** is the first Skill/reference implementation of PPMP; **Sandminni** is its public product brand.
3. **Persistence backends** provide durable storage. The first backend uses repository files and Git.
4. **Platform adapters** map environment-specific lifecycle/discovery behavior. The first adapter targets ChatGPT Projects.

Repository paths, `.chatgpt/` conventions, Git commits, ChatGPT first-substantive-turn behavior, product branding, repository CI/CD suppression mechanics, and website CI are not PPMP protocol requirements.

## Compatibility posture

PPMP v2.0.0 is an intentional MAJOR transition from RPM v1.0.0. Existing RPM v1 projects require explicit migration and MUST NOT be silently reinterpreted as v2.

The Tree Hole migration confirms that an RPM v1 repository can migrate without forced memory-file relocation: existing durable files may remain in place when the selected backend records valid locators and the migration preserves their knowledge. End-to-end ChatGPT-adapter acceptance still requires updating the consuming Project's external Project Instructions and verifying a fresh-conversation restore.

## Operating model

The repository is authoritative for the standard and its maintenance state. Chat conversations are working context only. Confirmed normative behavior belongs in `spec/`, `profiles/`, `templates/`, `examples/`, and `VERSION`; implementation-specific behavior belongs in its corresponding layer.
