# Agnir Decisions

## 2026-08-27 — New main-line structure

- `main` now implements the Agnir identity directly; predecessor PPMP/PPM/Sandminni behavior is preserved on `legacy/ppmp-v2.0.0` rather than retained as the active structure.
- Top-level `AGNIR.yaml` is the normative discovery anchor for the `repository-filesystem/0.1` profile. This filename is a profile rule, not an Agnir Core rule.
- This Project uses `.agnir/` for colocated durable memory. The directory is an implementation/profile choice; `AGNIR.yaml` locators are authoritative.
- Agnir Core version is declared as string `"0.1"`. Profile versions use `<profile-name>/<major.minor>` such as `repository-filesystem/0.1`.
- Project identity is a non-empty durable identifier. URI/URN forms are recommended when identity should survive backend changes; Core does not require global registration.
- Extension namespaces in the reference YAML use `<owner>/<name>` keys. `agnir/*` is reserved for Agnir-defined extensions; other owners may define their own namespaces.
- `state` and `next_actions` locators are required. `decisions` and `evidence` may be null only when the Project genuinely has no required durable content in those categories.
- Relative filesystem locators are resolved from the Project root under the repository/filesystem profile.
- Cold-start discovery is a Core invariant; arbitrary searching outside the declared Project boundary is not a valid repair strategy.
- `.chatgpt/project-memory.yaml` remains only as an execution-surface compatibility shim that points to the authoritative Agnir discovery/state. It must not become a second mutable memory root.

## Relationship to Svif

- Svif consumes Agnir Core, not the Agnir reference repository layout or any specific backend/adapter.
- Agnir remains independently useful without Svif.

## 2026-08-27 — Repository identity transition

- The repository/public-name rename is no longer deferred until late-stage completion. The active `main` structure now implements Agnir directly, so retaining the predecessor repository name `rpm` creates unnecessary identity debt.
- Rename `mattamior/rpm` to `mattamior/agnir` first, before the coordinated Svif and Cloudflare starter renames.
- The broader sequence is `mattamior/rpm` -> `mattamior/agnir`, `iorLab/zerolocal` -> `iorLab/svif`, then `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter`.
- The predecessor branch `legacy/ppmp-v2.0.0` is intentionally not renamed; it preserves predecessor identity and history.
- GitHub redirects may preserve navigation after a rename, but redirects are compatibility behavior rather than canonical Project identity. `AGNIR.yaml`, repository extensions, the bootstrap shim, documentation, cross-project references, and CI/reference URLs must be reconciled immediately after the rename.
- Repository naming is a discovery/profile metadata concern, not an Agnir Core storage or execution dependency.
