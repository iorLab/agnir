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
- This repository now uses RPM for its own durable project state via `.chatgpt/project-memory.yaml`.

## Scope

This repository maintains the RPM standard itself: Core semantics, project classification, persistence rules, bootstrap behavior, manifests, versioning, profiles, templates, examples, and future migration rules.

It does not store durable state for consuming projects such as application repositories. Each consuming repository owns its own `.chatgpt/project-memory.yaml` and project-memory artifacts.

## Operating model

- Normative RPM behavior belongs in this repository.
- Changes to RPM rules should be reflected in the relevant specification or template files and versioned according to `spec/VERSIONING.md`.
- The ChatGPT Project used to maintain RPM should preferably use Project-only memory so unrelated project conversations do not become implicit context.
- Consumer projects may use Project-only memory independently; cross-project continuity should come from repositories and RPM artifacts, not implicit ChatGPT memory sharing.
