# RPM Decisions

## D-001 — Repository-backed canonical memory

RPM treats the repository as the canonical source of truth for durable project knowledge. Chat conversations are working memory and are not authoritative durable storage.

**Status:** Superseded in scope by D-009. Repository-backed canonical memory remains the current implementation strategy, but is not a requirement of the future platform- and storage-agnostic protocol.

## D-002 — Unified Core plus composable profiles

Every RPM project uses the shared Core memory layer. Domain profiles extend Core and are selected conservatively based on recurring or structurally important project work.

## D-003 — Per-project manifest

Initialized consuming projects declare RPM configuration in `.chatgpt/project-memory.yaml` and normally keep Core memory under `docs/project-memory/`.

**Status:** Superseded in scope by D-009. The `.chatgpt/` path is ChatGPT-specific and repository-relative paths belong to the repository-backed implementation, not the platform-agnostic protocol.

## D-004 — Project isolation

ChatGPT Projects may use Project-only memory. RPM must not rely on implicit cross-project memory for durable continuity; repositories and RPM artifacts provide the durable bridge.

**Status:** Superseded in scope by D-009. Durable continuity remains a protocol concern; ChatGPT Project isolation and its recovery mechanics belong to a ChatGPT adapter.

## D-005 — RPM self-hosting

The `mattamior/rpm` specification repository uses RPM to track its own project state. Self-hosted project-memory artifacts describe maintenance state only and do not duplicate or supersede normative specification files under `spec/`, `profiles/`, or `templates/`.

## D-006 — Conservative self-classification

The RPM specification repository initially uses the `generic` profile. A specialized profile should be added only if recurring maintenance work clearly benefits from it.

## D-007 — Website as a non-normative presentation layer

RPM's public website lives in the specification repository and reads canonical `VERSION`, `spec/`, `profiles/`, and `templates/` files at build time. The website may add navigation, explanation, rendering, and copy controls, but it must not silently become an independent source of RPM semantics.

## D-008 — Static Cloudflare deployment

The initial RPM website uses Astro static generation and Cloudflare Workers Static Assets. GitHub-integrated Workers Builds is the intended deployment path so repository changes can produce preview and production deployments without a separate website content store or application backend.

## D-009 — Separate protocol, implementation, and platform adapters

The next architecture direction separates the current RPM design into three conceptual layers:

1. **PPMP — Persistent Project Memory Protocol**: the platform-agnostic and storage-agnostic protocol for durable AI project memory. Persistence is a protocol requirement, but no particular persistence mechanism such as Git or a repository is required.
2. **iorMemory**: the planned reference implementation / Skill implementing PPMP. Its initial persistence strategy may remain repository-backed because that is currently the preferred implementation, without making repositories part of PPMP semantics.
3. **Platform adapters**: platform-specific integration behavior such as ChatGPT Project bootstrap triggers, `.chatgpt/` conventions, and isolation constraints. Future adapters may target other AI project or agent environments.

Under this separation, PPMP defines durable project-memory semantics and behavior; iorMemory defines a concrete implementation; repository storage is a backend choice; and ChatGPT is one supported platform rather than part of the protocol identity.

The existing RPM v1.0.0 specification is treated as the repository- and ChatGPT-oriented prototype from which PPMP and iorMemory will be extracted. This decision records the architecture direction only; normative PPMP specifications, migration rules, repository naming, and release/version changes remain to be designed and must not be inferred solely from this decision.
