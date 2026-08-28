# Agnir README Agent Quick Start Checkpoint — 2026-08-28

## Scope

This checkpoint records the user-operability improvement added to the stable Agnir `0.1.0` release-ready line.

The English and Simplified Chinese README entry points now put an operational Quick Start before architecture explanation. A user who has an Agent with Project-directory read/write access can begin without first understanding Core/Profile terminology.

## Operational entry path

Both READMEs now provide two directly usable paths:

1. **Existing Agnir Project** — a copyable Agent prompt instructs the Agent to treat the Project root as the authorized Project Entry Point, read top-level `AGNIR.yaml`, resolve Current State / Next Actions and other durable memory as needed, prefer durable Agnir memory over private conversational context, and checkpoint changed Project truth when requested.
2. **New Project initialization** — a copyable Agent prompt instructs the Agent to initialize Core `0.1` with `repository-filesystem/0.1`, create `AGNIR.yaml`, create `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, `.agnir/evidence/`, persist initialization evidence, and verify a fresh cold start from the Project root.

The Quick Start also shows a minimal `AGNIR.yaml` and minimal `.agnir/` layout.

## Product boundary

This is documentation/usability hardening only. It does not change:

- Core compatibility line `0.1`;
- profile compatibility line `repository-filesystem/0.1`;
- repository SemVer `0.1.0`;
- any Core discovery or continuity semantics.

The README still explains that the repository/filesystem profile does not require GitHub, ChatGPT, a daemon, or an account when an Agent already has access to the Project filesystem.

## Durable documentation rule

The operational Quick Start is a required README entry-point surface:

- it must appear before the Architecture Diagram in both language versions;
- it must preserve both existing-Project and initialization paths;
- it must retain enough minimal configuration detail for an Agent to act without external setup documentation.

The self-hosting checker enforces these structural requirements without byte-for-byte locking prompt wording.

## Verification

Operational Quick Start enforcement commit: `820d8847bba4bc825740972bda19d3cc22378ad0`.

Agnir conformance run `33162899443` completed successfully on that commit.

This evidence is part of the stable `0.1.0` release-ready documentation baseline. Publication remains a separate explicit action.
