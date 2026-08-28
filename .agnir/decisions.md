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
- Agnir remains independently useful without Svif, and Svif execution/delivery/provider/authority/distribution semantics remain outside Agnir Core.

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

## 2026-08-28 — Predecessor evidence classification for migration

- Real predecessor evidence and exact PPMP v2 evidence are distinct categories. A Project MUST NOT be relabeled as PPMP v2 merely because it predates Agnir or uses `.chatgpt/project-memory.yaml`.
- `iorLab/svif@legacy/zerolocal-v0.1` is genuine predecessor evidence relative to Agnir, but its project-memory serialization is earlier v1/RPM-era form rather than PPMP v2.0.0. `mattamior/agent-skills` is likewise older project-memory evidence, not PPMP v2.
- These older Projects MAY validate migration requirements that are semantic across predecessor forms: durable-knowledge preservation, explicit transition, cold-start independence from predecessor-private context, and distinction between predecessor and target conformance.
- Exact external PPMP v2 migration validation remains separately unmet unless a qualifying historical Project is found.
- Release criteria MUST state explicitly whether exact external PPMP v2 evidence is required or whether a clearly classified PPMP v2 conformance fixture plus real older-predecessor migration evidence is sufficient.
- Migration validation MUST compare material Project knowledge, not only locator/file presence. The Svif audit's temporary loss of the durable `installable-plugin` product target is a concrete example of a migration regression that structural checks alone would miss.

## 2026-08-28 — README repository structure tree

- The README repository explanation uses a **plain-text tree**, not a third Mermaid architecture diagram and not a second abstract repository-map visualization.
- The tree MUST follow the actual active repository closely enough to show where protocol definitions, profiles, schemas, conformance, Project continuity, and predecessor history live, while remaining selective rather than exhaustive.
- Each documented directory or key file SHOULD include a short responsibility explanation directly in the tree.
- If a documented directory is added, removed, moved, or materially changes responsibility, `README.md` and `README.zh-CN.md` MUST update the affected tree in the same change set.
- Self-hosting conformance checks enforce the presence of the explanatory tree and key anchors without byte-for-byte locking the full presentation.

## 2026-08-28 — Exhaustive repository tree companion

- README repository trees remain compact navigation views rather than exhaustive listings.
- `REPOSITORY_TREE.md` is the canonical exhaustive file-level repository map for documentation purposes.
- Every tracked file SHOULD appear in `REPOSITORY_TREE.md` with a concise responsibility annotation or clear inherited directory responsibility.
- Tracked file additions, removals, moves, or material responsibility changes MUST update `REPOSITORY_TREE.md` in the same change set.
- If the change affects the compact README tree, both `README.md` and `README.zh-CN.md` MUST update together.
- `REPOSITORY_TREE.md` is explanatory documentation, not a second protocol specification; normative semantics remain in `spec/`, profiles, schemas, and canonical decisions/state.

## 2026-08-28 — PPMP v2 release-evidence requirement resolved

- A second independently hosted historical PPMP v2 Project is **not** a hard Agnir Core `0.1` release prerequisite.
- The availability of such a Project is accidental historical evidence, not a semantic property of Agnir or PPMP migration.
- Release-quality predecessor pressure requires instead:
  1. preservation of the canonical exact PPMP v2 predecessor boundary on `legacy/ppmp-v2.0.0`;
  2. an explicit reproducible exact PPMP v2 -> Agnir migration conformance fixture derived from that canonical predecessor semantics;
  3. at least one real non-fixture predecessor migration audit that compares material durable knowledge;
  4. clear separation of predecessor evidence, migration evidence, and target Agnir conformance.
- `iorLab/svif@legacy/zerolocal-v0.1` satisfies the real non-fixture migration-pressure requirement but remains classified as v1/RPM-era, not PPMP v2.
- `conformance/fixtures/ppmp-v2/`, `conformance/ppmp_v2_migration_reference.py`, and `conformance/test_ppmp_v2_migration.py` satisfy the reproducible exact PPMP v2 fixture requirement.
- The fixture MUST reject v1/RPM serialization rather than silently promote it to PPMP v2.
- First full conformance including the exact migration fixture passed run `33150059494`, job `98779726021`.

## 2026-08-28 — Core 0.1 compatibility and RC freeze

- Core compatibility, profile compatibility, and repository release version are separate version layers.
- Discovery Records for this line serialize Core compatibility as `agnir.version: "0.1"`.
- The current repository/filesystem profile remains `repository-filesystem/0.1`.
- Repository/distribution releases use SemVer; the first stable release for this Core line is `0.1.0`.
- `VERSION` is advanced to `0.1.0-rc.1`; this is a release-candidate label for the same Core `"0.1"` compatibility semantics, not a new Core line.
- Consumers such as Svif SHOULD bind to Core compatibility `"0.1"`, not to a particular repository patch or RC build.
- Patch releases in `0.1.x` MAY clarify prose, fix implementations, add conforming fixtures/profiles, or strengthen conformance, but MUST NOT redefine existing Core `0.1` field meaning, required durable-memory semantics, discovery failure semantics, or compatibility claims.
- A deliberate breaking Core semantic change MUST move to a new compatibility line such as `"0.2"`, with repository release beginning at `0.2.0`.
- Entering `0.1.0-rc.1` does **not** authorize creation of a public GitHub Release or tag; publication remains a separate explicit external effect.
