# iorMemory Decisions

## D-001 — Repository-backed canonical memory

RPM v1 treated the repository as canonical durable memory.

**Status:** Historical for RPM v1; retained by the PPM repository backend, not by the iorMemory protocol.

## D-002 — Unified Core plus composable profiles

Every iorMemory project uses the shared Core semantic layer. Domain profiles extend Core and are selected conservatively based on recurring or structurally important work.

## D-003 — Per-project manifest

RPM v1 required `.chatgpt/project-memory.yaml`.

**Status:** Superseded at protocol level. iorMemory v2 requires configuration semantics but not a file path or serialization. The path remains a PPM ChatGPT + repository convention.

## D-004 — Project isolation

Durable continuity MUST NOT depend on implicit model memory. ChatGPT Project-only memory is adapter-specific behavior.

## D-005 — Self-hosting

This specification repository uses the repository-backed PPM workflow to maintain its own durable maintenance state. Self-hosted maintenance files do not duplicate or override normative specification files.

## D-006 — Conservative classification

The maintenance project uses `generic` unless recurring maintenance work justifies a specialized profile.

## D-007 — Website is non-normative

The public website may explain and render iorMemory material but MUST NOT become an independent source of protocol semantics.

## D-008 — Static Cloudflare deployment

The public site uses Astro static generation and Cloudflare Workers Static Assets with GitHub-integrated builds.

## D-009 — Separate protocol, implementation, backends, and adapters

The architecture separates platform/storage-neutral protocol semantics from implementation behavior, persistence technology, and platform integration.

## D-010 — iorMemory is the protocol identity

The public standard/protocol identity is **iorMemory**. The earlier proposed name **PPMP — Persistent Project Memory Protocol** is retired before normative release and MUST NOT be used as the current protocol name.

Rationale: iorMemory is more distinctive and avoids acronym friction while still allowing the specification to define project-memory semantics clearly.

## D-011 — Persistent Project Memory is the reference Skill

The initial reference Skill/implementation is **Persistent Project Memory (PPM)**. It implements iorMemory and may initially use repository-backed persistence plus a ChatGPT adapter.

## D-012 — iorMemory v2.0.0 is a major migration from RPM v1

The shift from repository/ChatGPT-bound RPM semantics to platform- and storage-agnostic iorMemory semantics is incompatible at the protocol/configuration level. The first normative iorMemory release in this lineage is therefore version **2.0.0**, and RPM v1 projects require explicit migration.
