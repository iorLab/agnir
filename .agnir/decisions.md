# Agnir Decisions

## 2026-08-27 — New main-line structure

- `main` implements the Agnir identity directly; predecessor PPMP/PPM/Sandminni behavior is historical lineage rather than active structure.
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
- Agnir remains independently useful without Svif, and Svif execution/delivery/provider/authority/distribution semantics remain outside Agnir Core.

## 2026-08-27 — Repository identity transition

- The active canonical repository is `iorLab/agnir`; it was renamed from `mattamior/rpm` and transferred into the `iorLab` organization.
- Svif is canonical at `iorLab/svif`.
- A standalone Svif Cloudflare reference existed during migration/validation but is no longer part of the active canonical topology; provider-specific Svif Cloudflare behavior is now owned inside `iorLab/svif`.
- Repository redirects are compatibility behavior rather than canonical Project identity.
- Repository naming is a discovery/profile metadata concern, not an Agnir Core storage or execution dependency.

## 2026-08-28 — Remove execution-surface bootstrap from active Project structure

- Active Agnir Projects must not need a ChatGPT-specific bootstrap file to discover durable continuity.
- For the repository/filesystem profile used here, cold start begins directly at top-level `AGNIR.yaml`.
- Execution-surface integrations may keep their own workspace/bootstrap configuration outside the canonical Project structure.
- The former `.chatgpt/project-memory.yaml` compatibility shim is removed from active `main` and conformance treats `.chatgpt/` as forbidden active structure in this reference Project.

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
- Active negative fixtures cover `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.

## 2026-08-28 — Non-repository backend conformance baseline

- Agnir Core storage neutrality is pressure-tested by a durable SQLite-style conformance fixture that does not use `AGNIR.yaml`, `.agnir/`, a repository root, Git, or GitHub for discovery or continuity retrieval.
- The SQLite Project Entry Point is a database locator plus durable project key; this is a conformance realization of Core concepts, not a normative SQLite profile.
- `conformance/sqlite_backend_reference.py` and `conformance/test_sqlite_backend.py` are conformance-only artifacts, not promoted production backend code.
- The fixture proves cold start, version/identity validation, Current State / Next Actions / Decisions / Evidence retrieval, checkpoint persistence, and fresh-resolver resume on the database-backed path.

## 2026-08-28 — External-memory authorization semantics

- External memory conformance resolves the Discovery Record before authorization. A missing external Discovery Record maps to `AGNIR_DISCOVERY_NOT_FOUND` and MUST NOT be disguised as an authorization failure.
- Once an external Discovery Record is known, denied or unavailable authorization for its declared authorization reference maps to `AGNIR_DISCOVERY_UNAUTHORIZED`.
- After authorization succeeds, a missing declared required memory object maps to `AGNIR_DISCOVERY_UNRESOLVABLE`, not `UNAUTHORIZED` or `NOT_FOUND`.
- Durable external Discovery Records carry authorization **references** only. Plaintext tokens, passwords, secret values, or credential payloads remain outside Agnir durable memory and outside the conformance fixture.

## 2026-08-28 — Multi-project workspace isolation

- A workspace registry MAY provide locator-only convenience metadata mapping Project identity to Project Entry Point, but it MUST NOT become canonical Current State, Next Actions, Decisions, Evidence, or any other mutable continuity root.
- Multiple Projects discovered through one workspace registry remain independently authoritative through their own Agnir continuity stores.
- Checkpointing one Project MUST NOT mutate another Project's continuity or the locator-only workspace registry.
- A registry locator does not bypass Project identity validation; cross-Project resolution still fails as `AGNIR_DISCOVERY_PROJECT_MISMATCH`.

## 2026-08-28 — Locator Chain cycle, stale, and inconsistency semantics

- `conformance/locator_chain_reference.py` is a substrate-neutral conformance model for Core Locator Chain semantics, not a normative storage profile or production implementation.
- Revisiting a previously resolved locator in the same chain MUST surface `AGNIR_DISCOVERY_CYCLE`.
- A record known to be superseded or non-authoritative MUST surface `AGNIR_DISCOVERY_STALE` even if the physical state objects still exist.
- Current State and Next Actions from different checkpoint generations are materially inconsistent and MUST NOT be spliced into one apparent Project truth.

## 2026-08-28 — Repository/filesystem indirection boundaries

- An authorized filesystem indirection used as the Project Entry Point MAY be canonicalized when it resolves to exactly one selected Project root. A symlinked Project Entry Point is therefore not inherently invalid.
- A relative memory locator that escapes the selected Project root through a symlink MUST NOT become an implicitly authorized external memory binding merely because the target is readable. Without an explicit authorized external Locator Chain it fails as `AGNIR_DISCOVERY_UNRESOLVABLE`.
- A Git worktree is a valid repository/filesystem Project root when the worktree itself contains top-level `AGNIR.yaml` and its declared continuity. Discovery MUST NOT depend on `.git` being a directory; Git worktrees commonly use a `.git` metadata file.
- Declared durable continuity must actually survive the substrate. Git does not track empty directories, so an Evidence locator to an otherwise empty directory can legitimately become unresolvable in a new worktree. The conformance fixture was fixed by persisting real Evidence rather than weakening discovery semantics.
- Real mount-boundary behavior remains unproven. It MUST NOT be claimed by substituting an ordinary directory for a real mount-capable environment.
- Corrected boundary run `33144199717`, job `98761550583`, succeeded; durable evidence is `.agnir/evidence/2026-08-28-filesystem-boundaries.md`.

## 2026-08-28 — README repository structure tree

- The README repository explanation uses a **plain-text tree**, not a third Mermaid architecture diagram and not a second abstract repository-map visualization.
- The tree MUST follow the actual active repository closely enough to show where protocol definitions, profiles, schemas, conformance, Project continuity, and predecessor history live, while remaining selective rather than exhaustive.
- Each documented directory or key file SHOULD include a short responsibility explanation directly in the tree.
- If a documented directory is added, removed, moved, or materially changes responsibility, `README.md` and `README.zh-CN.md` MUST update the affected tree in the same change set.
- Self-hosting conformance checks enforce the presence of the explanatory tree and key anchors without byte-for-byte locking the full presentation.

## 2026-08-28 — Greenfield Core; history is non-authoritative

- This decision supersedes any interpretation that Agnir Core `0.1` release readiness depends on PPMP/PPM/Sandminni migration or predecessor compatibility.
- Predecessor artifacts are retained only for lineage, audit, and optional historical reference.
- Active Core semantics, profiles, conformance, release gates, Project state, and next actions MUST NOT depend on predecessor serialization, `.chatgpt/` layout, ChatGPT-specific adapters, legacy repository structure, or historical external Projects.
- Historical ideas become active only when independently restated in current Agnir Core/profile decisions.
- Current Agnir `main` is intentionally a new protocol namespace and architecture; backward compatibility with PPMP is not implied by lineage.

## 2026-08-28 — Historical migration guidance lives outside active spec

- Active `spec/` contains only current Agnir protocol definitions: `spec/AGNIR_CORE.md` and `spec/AGNIR_DISCOVERY.md`.
- Optional PPMP migration guidance lives at `history/MIGRATION_PPMP_V2.md` and is explicitly archival/reference material.
- `history/MIGRATION_PPMP_V2.md` is not an Agnir Core `0.1` semantic dependency, conformance requirement, compatibility obligation, or release gate.
- The self-hosting checker forbids `spec/MIGRATION_PPMP_V2.md` from reappearing on active `main`, so legacy migration cannot silently drift back into the normative specification surface.

## 2026-08-28 — Main-only branch governance

- `main` is the only long-lived branch in `iorLab/agnir`.
- Legacy, website, feature, release-pointer, and temporary branch refs are deleted after their final tip SHAs are recorded in `history/BRANCH_ARCHIVE.md`.
- Historical predecessor boundaries are referenced by immutable commit SHA and Git history rather than a live `legacy/*` branch.
- No active Core semantic, conformance rule, release gate, or recovery path may require a retired branch ref.

## 2026-08-28 — Stable Agnir 0.1.0 compatibility and release boundary

- Agnir Core `0.1` is the stable initial Core compatibility line.
- `repository-filesystem/0.1` is the stable initial repository/filesystem profile compatibility line.
- Repository release SemVer is independent from those compatibility identifiers; the initial stable repository release is `0.1.0`.
- Breaking Core field meaning, required continuity semantics, identity rules, or discovery invariants require a new Core compatibility line such as `0.2`.
- Breaking repository/filesystem discovery-anchor, required serialization, locator interpretation, or selected-root authority semantics require a new profile compatibility line.
- Repository `0.1.x` patch releases may clarify specification text, add non-breaking conformance pressure, or fix reference tooling, but MUST NOT redefine Core `0.1` or profile `repository-filesystem/0.1` semantics.
- The active repository/filesystem profile has no predecessor bootstrap fallback; historical migration guidance remains outside active profile/spec semantics.
- `AGNIR.yaml` contains no retired predecessor branch reference.
- `RELEASE.md` is the publication contract and records the known unproven real-mount boundary.
- Stable publication candidate `846d794384e24f4d0431bb72b0f1036c60503bdd` passed conformance run `33161463275`.
- Agnir is release-ready; creating tag `v0.1.0` and/or a GitHub Release is a separate explicit publication action.

## 2026-08-28 — README operational Quick Start is a required entry surface

- The first operational section in both `README.md` and `README.zh-CN.md` MUST be a Quick Start placed before the Architecture Diagram.
- The Quick Start MUST support two direct user paths: using an already-configured Agnir Project and initializing a new Project.
- The existing-Project path SHOULD be expressible as a copyable Agent instruction that starts from the authorized Project root, reads `AGNIR.yaml`, follows durable memory locators, and checkpoints changed Project truth on request.
- The initialization path SHOULD be expressible as a copyable Agent instruction that creates the minimal repository/filesystem manifest and durable memory layout, persists initialization evidence, and verifies a fresh cold start.
- The Quick Start MUST show enough minimal `AGNIR.yaml` and `.agnir/` structure for a user with an Agent that already has Project-directory read/write access to begin without separate installation/setup documentation.
- These prompts are operational examples, not additional Core normative fields or execution-surface requirements. Agent-specific wording MAY evolve while preserving the same Agnir semantics.
- Self-hosting conformance enforces Quick Start position and structural content without byte-for-byte locking prompt prose.
- Quick Start enforcement commit `820d8847bba4bc825740972bda19d3cc22378ad0` passed conformance run `33162899443`; durable evidence is `.agnir/evidence/2026-08-28-readme-agent-quick-start-checkpoint.md`.
