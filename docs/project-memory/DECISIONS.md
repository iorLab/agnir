# RPM Decisions

## D-001 — Repository-backed canonical memory

RPM treats the repository as the canonical source of truth for durable project knowledge. Chat conversations are working memory and are not authoritative durable storage.

## D-002 — Unified Core plus composable profiles

Every RPM project uses the shared Core memory layer. Domain profiles extend Core and are selected conservatively based on recurring or structurally important project work.

## D-003 — Per-project manifest

Initialized consuming projects declare RPM configuration in `.chatgpt/project-memory.yaml` and normally keep Core memory under `docs/project-memory/`.

## D-004 — Project isolation

ChatGPT Projects may use Project-only memory. RPM must not rely on implicit cross-project memory for durable continuity; repositories and RPM artifacts provide the durable bridge.

## D-005 — RPM self-hosting

The `mattamior/rpm` specification repository uses RPM to track its own project state. Self-hosted project-memory artifacts describe maintenance state only and do not duplicate or supersede normative specification files under `spec/`, `profiles/`, or `templates/`.

## D-006 — Conservative self-classification

The RPM specification repository initially uses the `generic` profile. A specialized profile should be added only if recurring maintenance work clearly benefits from it.
