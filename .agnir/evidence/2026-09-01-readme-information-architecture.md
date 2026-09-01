# 2026-09-01 — README audience split and entry-point information architecture

The Principal approved a README information-architecture simplification for Agnir.

Durable documentation rule:

- Before `## Architecture Diagram`, README content is limited to two operational audiences.
- `## Start Here` is the user-facing entry point and contains only the minimal install, upgrade, and normal-use actions.
- `## Agnir Project Instructions` remains the canonical Agent-facing activation heading required by `AGENTS.md`; it is explicitly marked as Agent-only guidance for human readers.
- Packaging rationale, compatibility explanation, release detail, repository structure, and implementation/conformance material belong after the architecture entry point or in dedicated documents.
- The user-facing install and upgrade intents remain one sentence each; users do not carry the Agent implementation checklist.
- English and Simplified Chinese READMEs follow the same audience split.
- Conformance now enforces `Start Here -> Agnir Project Instructions -> Architecture` ordering and the canonical user prompts.

This is a documentation/operational-entry refactor only. It does not change Agnir Core `0.1`, `repository-filesystem/0.1`, Project identity, durable memory locators, or the published `v0.1.0` release target.
