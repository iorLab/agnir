# Agnir Decisions

## 2026-08-27 — New main-line structure

- `main` implements the Agnir identity directly; predecessor PPMP/PPM/Sandminni behavior is preserved on `legacy/ppmp-v2.0.0` rather than retained as the active structure.
- Top-level `AGNIR.yaml` is the normative discovery anchor for the `repository-filesystem/0.1` profile. This filename is a profile rule, not an Agnir Core rule.
- This Project uses `.agnir/` for colocated durable memory. The directory is an implementation/profile choice; `AGNIR.yaml` locators are authoritative.
- Agnir Core version is declared as string `"0.1"`. Profile versions use `<profile-name>/<major.minor>` such as `repository-filesystem/0.1`.
- Project identity is a non-empty durable identifier. URI/URN forms are recommended when identity should survive backend changes; Core does not require global registration.
- Extension namespaces in the reference YAML use `<owner>/<name>` keys. `agnir/*` is reserved for Agnir-defined extensions; other owners may define their own namespaces.
- `state` and `next_actions` locators are required. `decisions` and `evidence` may be null only when the Project genuinely has no required durable content in those categories.
- Relative filesystem locators are resolved from the Project root under the repository/filesystem profile.
- Cold-start discovery is a Core invariant; arbitrary searching outside the declared Project boundary is not a valid repair strategy.

## Relationship to Svif

- Svif is a separate Project orchestration product whose stable kernel consumes a Continuity Provider interface; Agnir Core `0.1` is its current founding continuity implementation.
- Svif consumes Agnir protocol semantics, not the Agnir reference repository layout or a specific backend/adapter.
- Agnir remains independently useful without Svif, and Svif execution/delivery/provider/authority semantics remain outside Agnir Core.

## 2026-08-27 — Repository identity transition

- The active canonical repository is `iorLab/agnir`; it was renamed from `mattamior/rpm` and transferred into the `iorLab` organization.
- Svif is canonical at `iorLab/svif`.
- A standalone Svif Cloudflare reference existed during migration/validation but is no longer part of the active canonical topology; provider-specific Svif Cloudflare behavior is now owned inside `iorLab/svif`.
- The predecessor branch `legacy/ppmp-v2.0.0` is intentionally not renamed; it preserves predecessor identity and history.
- Repository redirects are compatibility behavior rather than canonical Project identity.
- Repository naming is a discovery/profile metadata concern, not an Agnir Core storage or execution dependency.

## 2026-08-28 — Remove execution-surface bootstrap from active Project structure

- Active Agnir Projects must not need a ChatGPT-specific bootstrap file to discover durable continuity.
- For the repository/filesystem profile used here, cold start begins directly at top-level `AGNIR.yaml`.
- Execution-surface integrations may keep their own workspace/bootstrap configuration outside the canonical Project structure.
- The former `.chatgpt/project-memory.yaml` compatibility shim is removed from active `main` and conformance now treats `.chatgpt/` as forbidden active structure in this reference Project.

## 2026-08-28 — README architecture diagrams and localization

- `README.md` is the English project entry point and `README.zh-CN.md` is the Simplified Chinese entry point.
- Both language versions MUST contain a current **Architecture Diagram** and **Continuity Flow** diagram using Mermaid.
- Changes to Agnir's layer model, discovery path, durable-memory semantics, Project boundary, or continuity flow MUST update the affected diagrams in both README language versions in the same change set.
- Localized READMEs explain the same canonical protocol architecture; translation may adapt prose but must not create a second semantic model.
- Localized diagrams are **comprehension-first, not literal translations**. In `README.zh-CN.md`, each node SHOULD explain in Chinese what the object is and what responsibility it has in Agnir; English terms remain secondary annotation or exact identifiers only.
- Conformance checks enforce diagram/locale structure rather than byte-for-byte prose.

## 2026-08-28 — Discovery conformance reference and selected-root semantics

- `conformance/repository_filesystem_reference.py` is a **conformance-only executable reference**, not a promoted Agnir production implementation, backend, or adapter.
- The self-hosting repository/filesystem check and negative fixtures use the same reference resolver so positive and negative conformance pressure share one interpretation of the profile.
- `AGNIR_DISCOVERY_AMBIGUOUS` applies when multiple candidate Project roots exist **before** authority has selected exactly one root.
- Once the authorized Project Entry Point selects a repository/filesystem root, nested parent/child Projects do not make that selected root ambiguous. Discovery remains scoped to the selected root.
- If the selected root identifies another Project, discovery MUST surface `AGNIR_DISCOVERY_PROJECT_MISMATCH`; it MUST NOT search a parent or child root for a more convenient identity.
- Active negative fixtures now cover `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.
- Conformance run `33143495855` succeeded with both self-hosting cold-start and negative discovery fixture steps; durable evidence is `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`.

## 2026-08-28 — Non-repository backend conformance baseline

- Agnir Core storage neutrality is now pressure-tested by a durable SQLite-style conformance fixture that does not use `AGNIR.yaml`, `.agnir/`, a repository root, Git, or GitHub for discovery or continuity retrieval.
- The SQLite Project Entry Point is a database locator plus durable project key; this is a conformance realization of Core concepts, not a normative SQLite profile.
- `conformance/sqlite_backend_reference.py` and `conformance/test_sqlite_backend.py` are conformance-only artifacts, not promoted production backend code.
- The fixture proves cold start, version/identity validation, Current State / Next Actions / Decisions / Evidence retrieval, checkpoint persistence, and fresh-resolver resume on the database-backed path.
- Shared semantic failure classes live in `conformance/core_reference.py` so repository/filesystem and SQLite fixtures preserve equivalent Core failure vocabulary without promoting either substrate into Core.
- Conformance run `33143655399`, job `98759873676`, succeeded with the SQLite tests included in the negative/backend unittest discovery step; durable evidence is `.agnir/evidence/2026-08-28-sqlite-non-repository-backend.md`.

## 2026-08-28 — External-memory authorization semantics

- External memory conformance resolves the Discovery Record before authorization. A missing external Discovery Record maps to `AGNIR_DISCOVERY_NOT_FOUND` and MUST NOT be disguised as an authorization failure.
- Once an external Discovery Record is known, denied or unavailable authorization for its declared authorization reference maps to `AGNIR_DISCOVERY_UNAUTHORIZED`.
- After authorization succeeds, a missing declared required memory object maps to `AGNIR_DISCOVERY_UNRESOLVABLE`, not `UNAUTHORIZED` or `NOT_FOUND`.
- Durable external Discovery Records carry authorization **references** only. Plaintext tokens, passwords, secret values, or credential payloads remain outside Agnir durable memory and outside the conformance fixture.
- `conformance/external_memory_reference.py` and `conformance/test_external_memory_authorization.py` are conformance-only artifacts, not a normative external-memory profile.
- Conformance run `33143771320`, job `98760235526`, succeeded with the external-memory authorization tests included; durable evidence is `.agnir/evidence/2026-08-28-external-memory-authorization.md`.

## 2026-08-28 — Multi-project workspace isolation

- A workspace registry MAY provide locator-only convenience metadata mapping Project identity to Project Entry Point, but it MUST NOT become canonical Current State, Next Actions, Decisions, Evidence, or any other mutable continuity root.
- `conformance/workspace_registry_reference.py` deliberately accepts only locator metadata (`backend`, `database`, `project_key`) for its current fixture and rejects embedded continuity as `AGNIR_DISCOVERY_INCONSISTENT`.
- Multiple Projects discovered through one workspace registry remain independently authoritative through their own Agnir continuity stores.
- Checkpointing one Project MUST NOT mutate another Project's continuity or the locator-only workspace registry.
- A registry locator does not bypass Project identity validation; cross-Project resolution still fails as `AGNIR_DISCOVERY_PROJECT_MISMATCH`.
- The workspace registry is conformance-only convenience metadata, not an Agnir Core-required registry design.
- Conformance run `33143930233`, job `98760729955`, succeeded with the multi-project isolation tests included; durable evidence is `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`.

## 2026-08-28 — Locator Chain cycle, stale, and inconsistency semantics

- `conformance/locator_chain_reference.py` is a substrate-neutral conformance model for Core Locator Chain semantics, not a normative storage profile or production implementation.
- Revisiting a previously resolved locator in the same chain MUST surface `AGNIR_DISCOVERY_CYCLE`; an implementation MUST NOT choose an arbitrary node and fabricate terminal continuity.
- A record known to be superseded or non-authoritative MUST surface `AGNIR_DISCOVERY_STALE` even if the physical state objects still exist.
- A chain hop that simultaneously claims another Discovery Record and terminal memory is materially contradictory and MUST surface `AGNIR_DISCOVERY_INCONSISTENT`.
- Current State and Next Actions from different checkpoint generations are materially inconsistent and MUST NOT be spliced into one apparent Project truth.
- A consistent multi-hop chain with matching identity and checkpoint generation remains valid.
- Conformance run `33144042330`, job `98761070215`, succeeded with the Locator Chain fixtures included; durable evidence is `.agnir/evidence/2026-08-28-locator-chain-failures.md`.
