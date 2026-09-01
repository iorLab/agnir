# 2026-09-01 — README audience split and entry-point information architecture

The Principal approved a README information-architecture simplification for Agnir and later extended the pre-architecture guide with a concrete view of the initialized Project surface.

Durable documentation rule:

- Before `## Architecture Diagram`, README content remains concise and operational rather than becoming a full implementation manual.
- `## Start Here` is the user-facing entry point and contains only the minimal install, upgrade, and normal-use actions.
- `## Agnir Project Instructions` remains the canonical Agent-facing activation heading required by `AGENTS.md`; it is explicitly marked as Agent-only guidance for human readers.
- `## What Agnir Adds to a Project` / `## Agnir 会给 Project 增加什么` follows the Agent section and gives users a compact filesystem map of what the reference Skill creates, merges, or validates: `AGENTS.md`, `AGNIR.yaml`, the README instruction section, and the declared `.agnir/` State / Next Actions / Decisions / Evidence surface.
- The Project-surface section explains each file/directory responsibility and explicitly states that existing files are merged non-destructively, `AGNIR.yaml` locators are authoritative, and the reference `.agnir/` layout is profile behavior rather than a universal Agnir Core requirement.
- Packaging rationale, compatibility explanation, release detail, repository structure, and deeper implementation/conformance material belong after the architecture entry point or in dedicated documents.
- The user-facing install and upgrade intents remain one sentence each; users do not carry the Agent implementation checklist.
- English and Simplified Chinese READMEs follow the same information architecture.
- Conformance enforces `Start Here -> Agnir Project Instructions -> installed Project surface -> Architecture`, canonical user prompts, and the required Project-surface markers.

This is a documentation/operational-entry refactor only. It does not change Agnir Core `0.1`, `repository-filesystem/0.1`, Project identity, durable memory locators, or the published `v0.1.0` release target.
