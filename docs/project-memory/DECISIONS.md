# PPMP Decisions

## D-001 — Repository-backed canonical memory

RPM v1 treated the repository as canonical durable memory.

**Status:** Historical for RPM v1; retained by the PPM repository backend, not by the PPMP protocol.

## D-002 — Unified Core plus composable profiles

Every PPMP project uses the shared Core semantic layer. Domain profiles extend Core and are selected conservatively based on recurring or structurally important work.

## D-003 — Per-project manifest

RPM v1 required `.chatgpt/project-memory.yaml`.

**Status:** Superseded at protocol level. PPMP v2 requires configuration semantics but not a file path or serialization. The path remains a PPM ChatGPT + repository convention.

## D-004 — Project isolation

Durable continuity MUST NOT depend on implicit model memory. ChatGPT Project-only memory is adapter-specific behavior.

## D-005 — Self-hosting

This specification repository uses PPM with the repository backend and ChatGPT adapter to maintain its own durable maintenance state. Self-hosted maintenance files do not duplicate or override normative specification files.

## D-006 — Conservative classification

**Status:** Updated for current repository reality.

The maintenance project is classified as `software` because its recurring work now includes specification tooling, implementation/backend contracts, website code, build/deployment integration, and technical validation. Classification remains conservative: a specialized profile is used only because these activities are structurally recurring rather than incidental.

## D-007 — Website is non-normative

The public website may explain and render PPMP and PPM material but MUST NOT become an independent source of protocol semantics.

## D-008 — Static Cloudflare deployment

The public site uses Astro static generation and Cloudflare Workers Static Assets with GitHub-integrated builds.

## D-009 — Separate protocol, implementation, backends, and adapters

The architecture separates platform/storage-neutral protocol semantics from implementation behavior, persistence technology, and platform integration.

## D-010 — PPMP is the protocol identity

The public standard/protocol identity is **PPMP — Persistent Project Memory Protocol**. PPMP defines the normative semantics and version lineage.

**Correction note:** an erroneous maintenance change on 2026-08-27 briefly inverted the names and described iorMemory as the protocol. That inversion was not the intended architecture and is superseded by this decision.

## D-011 — iorMemory was a temporary reference-Skill name

After restoring PPMP as the protocol identity, **iorMemory** was briefly selected as the first reference Skill/implementation name.

**Status:** Superseded by D-013.

Rationale for supersession: iorMemory has higher pronunciation, spelling, and explanation cost. Persistent Project Memory (PPM) has an immediate semantic relationship to PPMP and is easier to understand and propagate in technical documentation.

## D-012 — PPMP v2.0.0 is a major migration from RPM v1

The shift from repository/ChatGPT-bound RPM semantics to platform- and storage-agnostic PPMP semantics is incompatible at the protocol/configuration level. The first normative PPMP release in this lineage is therefore version **2.0.0**, and RPM v1 projects require explicit migration.

## D-013 — Persistent Project Memory (PPM) is the reference Skill

The first reference Skill/implementation is **Persistent Project Memory**, abbreviated **PPM**. It implements PPMP and initially uses repository-backed persistence plus a ChatGPT adapter.

Reference manifests use the stable machine identifier `persistent-project-memory` rather than the bare acronym `ppm`.

PPMP conformance MUST NOT depend on PPM-specific implementation conventions.

## D-014 — Sandminni is the public product brand

**Sandminni** is the public-facing product brand for the Persistent Project Memory (PPM) reference implementation.

The layer identities remain distinct:

- **PPMP** is the protocol and normative standard;
- **Persistent Project Memory (PPM)** remains the technical name and abbreviation for the reference Skill/implementation;
- `persistent-project-memory` remains the stable implementation machine identifier;
- **Sandminni** is the product/brand identity presented to users.

The brand metaphor is memory accumulated grain by grain. Future visual identity and logo exploration SHOULD draw from three related motifs: **sand/grains**, **convergence or accumulation**, and **memory/durable continuity**.

This is a branding decision, not a change to PPMP semantics or conformance behavior, and therefore does not require a PPMP protocol version change.

## D-015 — Repository memory checkpoints minimize CI/CD side effects

A real RPM v1 → PPMP v2 / PPM migration in `mattamior/tree-hole` showed that memory-only commits can accidentally trigger production deployment when a consuming repository deploys every successful `main` push.

The reference repository backend therefore treats CI/CD side-effect minimization as backend operational behavior: memory-only checkpoints SHOULD use repository-supported non-deploying mechanisms when project policy permits; a logical checkpoint SHOULD be coalesced into one coherent commit when practical; and persistence verification MUST remain distinct from application/release verification.

This decision does not change PPMP Core semantics or conformance. Under `spec/VERSIONING.md`, backend behavior may evolve independently, so the PPMP protocol remains **v2.0.0**.

## D-016 — Site CI verifies build/packageability, not live production

The repository maintains path-scoped GitHub Site CI for changes that can affect the generated public site: `site/`, `VERSION`, protocol/profile/implementation/backend/adapter material, templates, and the workflow itself.

Site CI runs the actual site dependency installation and `npm run check:deploy`, which performs the Astro build and a Wrangler deploy dry-run. A successful run is durable evidence that the repository revision builds and packages for the configured Worker target.

Site CI does **not** prove that Cloudflare production deployment completed, that the public origin is reachable, or that browser-only interactions work. Those remain separate live-production acceptance claims.

## D-017 — ChatGPT Project Instructions are external adapter configuration

Actual ChatGPT Project Instructions are platform-side configuration and can drift independently of repository manifests, templates, and implementation/adapter documentation. Updating repository state does not automatically migrate that external setting.

After a migration or adapter/implementation change that affects bootstrap naming, discovery, or checkpoint behavior, acceptance includes verifying the actual external Project Instructions and exercising a fresh conversation. A repository-backed project-specific snapshot MAY be maintained to make the intended setting reviewable and recoverable, but that snapshot does not replace or prove the actual platform configuration.

This is ChatGPT-adapter behavior rather than PPMP Core semantics, so it does not change the PPMP protocol version.

## D-018 — Keep maintenance Project Instructions concise

The PPMP maintenance ChatGPT Project uses a concise external instruction set containing only the bootstrap, source-of-truth, layer-boundary, persistence, and checkpoint rules needed for reliable operation.

Detailed governance and explanatory material remains in the repository rather than being duplicated into the external ChatGPT Project Instructions. The repository snapshot at `.chatgpt/PROJECT_INSTRUCTIONS.md` SHOULD mirror the intended concise platform configuration.

This is project/adapter configuration, not PPMP Core semantics, and does not change the protocol version.

## D-019 — Agnir is the new project identity and the PPMP/PPM/Sandminni lineage remains historical evidence

**Agnir** is the new target identity for the project currently developed in `mattamior/rpm`.

This supersedes the future-facing PPMP / PPM / Sandminni naming stack, but does **not** silently rewrite or invalidate PPMP v2.0.0 history. PPMP v2, PPM, Sandminni, and RPM v1 remain explicit predecessor identities and evidence until an intentional migration specifies how the new Agnir lineage relates to them.

The Agnir transition is architectural as well as nominal. Broad file, repository, website, implementation-ID, and domain renames are deferred until the compatibility/versioning model is explicit.

## D-020 — Agnir is project-owned, platform-neutral, storage-neutral, and executor-neutral durable memory

Agnir is not `GitHub-backed Agent memory` and MUST NOT be defined by Git, GitHub, a repository host, ChatGPT, a conversational UI, an AI-agent identity, or a particular storage layout.

The durable memory belongs to the **project**. Any compatible reader/executor may consume it if it can discover and interpret the project's Agnir state according to the applicable contract.

The core properties include:

- project ownership rather than executor ownership;
- durability across executor loss or replacement;
- portability across execution environments;
- self-description sufficient for compatible interpretation;
- discoverability from the project or a project-declared durable locator;
- independence from predecessor-private conversational/model context.

Git repositories, local filesystems, databases, documents, APIs, synced workspaces, cloud stores, and other persistence mechanisms are backends/implementations rather than Agnir Core requirements.

## D-021 — Generalize fresh-conversation recovery into cold-start/fresh-executor discovery

The important invariant behind prior RPM/PPMP ChatGPT bootstrap work is not ChatGPT-specific `fresh conversation` behavior.

A compatible executor with no private predecessor context must be able to enter the project, discover the applicable Agnir state, interpret it, and resume safely.

This generalized failure/recovery class is provisionally called **cold-start discovery** or **fresh-executor recovery**. ChatGPT Project Instructions, repository refs, local workspace files, IDE metadata, or other environment locators are adapter/backend mechanisms rather than the normative invariant itself.

## D-022 — Agnir remains independent of Svif; Svif depends on Agnir-compatible continuity

`iorLab/zerolocal` is evolving into the separate **Svif** project.

- Agnir MAY be used by projects that do not use Svif.
- Agnir MUST NOT depend on Svif software-delivery lifecycle semantics.
- Svif builds on Agnir-compatible durable project continuity.
- The dependency direction is **Svif -> Agnir**.
- The exact versioned compatibility contract is not yet frozen and must be designed explicitly.

This separation keeps durable project continuity reusable outside software delivery, cloud deployment, provider adapters, or any single execution surface.

## D-023 — Shared workspace is allowed; durable project memory remains isolated

A single ChatGPT Project or other execution workspace MAY be used to develop multiple related projects such as Svif and Agnir.

The workspace is not a project identity and MUST NOT become an authoritative shared mutable memory store.

Each project retains its own durable Agnir state and canonical project identity. Cross-project decisions are written independently into each affected project's memory according to their local meaning.

Workspace-level configuration SHOULD be a thin registry/locator containing only enough information to discover the participating projects. It SHOULD NOT duplicate current state, decisions, blockers, or other mutable project memory.

For project-scoped work, an executor SHOULD load only that project's Agnir. For explicitly cross-project work, it MAY load all affected projects.

This shared-workspace/separate-memory arrangement is a candidate future conformance scenario for proving multi-project continuity without durable context bleed.
