# Agnir Next Actions

1. **Add the multi-project workspace isolation case** with independent Agnir state and locator-only workspace registry metadata. Keep this distinct from the already-proven selected nested-root isolation case: the workspace registry may identify Project Entry Points but MUST NOT become a shared mutable continuity store.
2. Add explicit fixtures for remaining discovery failure classes where meaningful: cycle, stale locator, and materially inconsistent continuity.
3. Add symlink, mount, and worktree boundary cases for `repository-filesystem/0.1` without turning those substrate details into Core requirements.
4. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
5. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
6. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, or authority semantics into Agnir Core.
7. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

Architecture/continuity changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations.

## Completed in the current implementation sequence

- Repository identity transition completed and canonical references reconciled to `iorLab/agnir`.
- Active ChatGPT-specific bootstrap shim removed; `AGNIR.yaml` is the direct repository/filesystem cold-start entry point.
- English and Simplified Chinese README entry points include synchronized Architecture and Continuity Flow diagrams with comprehension-first Chinese nodes.
- Shared conformance-only repository/filesystem resolver added and used by self-hosting cold-start checks.
- Negative fixtures cover `NOT_FOUND`, broken-locator `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.
- Durable SQLite-style non-repository fixture proves Core continuity without `AGNIR.yaml`, `.agnir/`, repository-root discovery, Git, or GitHub, including checkpoint and fresh-resolver resume.
- External-memory fixture distinguishes missing Discovery Record (`NOT_FOUND`), denied known authorization reference (`UNAUTHORIZED`), and authorized-but-missing required memory (`UNRESOLVABLE`) without storing plaintext credentials.
- Conformance run `33143771320`, job `98760235526`, succeeded with the external-memory authorization tests included; durable evidence is `.agnir/evidence/2026-08-28-external-memory-authorization.md`.
