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
