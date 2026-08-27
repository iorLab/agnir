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
- RPM (Repository Project Memory) v1.0.0 is the historical repository- and ChatGPT-oriented predecessor.
- The v2 architecture separates protocol semantics, implementation behavior, persistence backends, and platform adapters.
- PPMP is platform-agnostic and storage-agnostic. Persistence is required; Git/repository storage is not.
- The initial PPM stack uses the repository backend and ChatGPT adapter to preserve the practical RPM v1 workflow.
- Normative protocol files live under `spec/`; reusable profiles under `profiles/`; reference serialization under `templates/` and `examples/`.
- Implementation, backend, and adapter contracts live under `implementations/`, `backends/`, and `adapters/`.
- This repository uses PPM with the repository backend and ChatGPT adapter for its own maintenance memory under `docs/project-memory/`.
- The public website remains a non-normative presentation layer and is deployed through Cloudflare Workers from the repository.

## Architectural boundary

1. **PPMP** defines durable Project Memory semantics, lifecycle, classification, checkpoint behavior, profiles, and compatibility.
2. **Persistent Project Memory (PPM)** is the first Skill/reference implementation of PPMP; **Sandminni** is its public product brand.
3. **Persistence backends** provide durable storage. The first backend uses repository files and Git.
4. **Platform adapters** map environment-specific lifecycle/discovery behavior. The first adapter targets ChatGPT Projects.

Repository paths, `.chatgpt/` conventions, Git commits, ChatGPT first-substantive-turn behavior, and product branding are not PPMP protocol requirements.

## Compatibility posture

PPMP v2.0.0 is an intentional MAJOR transition from RPM v1.0.0. Existing RPM v1 projects require explicit migration and MUST NOT be silently reinterpreted as v2.

## Operating model

The repository is authoritative for the standard and its maintenance state. Chat conversations are working context only. Confirmed normative behavior belongs in `spec/`, `profiles/`, `templates/`, `examples/`, and `VERSION`; implementation-specific behavior belongs in its corresponding layer.
