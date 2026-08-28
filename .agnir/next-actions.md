# Agnir Next Actions

1. **Add one materially non-repository backend fixture** to demonstrate that Agnir Core continuity does not depend on repository/filesystem layout. Prefer a durable database-style fixture with a non-filesystem Project Entry Point and explicit Discovery Record / state retrieval semantics.
2. **Add an external-memory authorization fixture** that distinguishes `AGNIR_DISCOVERY_UNAUTHORIZED` from `AGNIR_DISCOVERY_NOT_FOUND` without exposing secret values.
3. **Add the multi-project workspace isolation case** with independent Agnir state and locator-only workspace registry metadata. Keep this distinct from the already-proven selected nested-root isolation case.
4. Add explicit fixtures for remaining discovery failure classes where meaningful: cycle, stale locator, and materially inconsistent continuity.
5. Add symlink, mount, and worktree boundary cases for `repository-filesystem/0.1` without turning those substrate details into Core requirements.
6. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
7. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
8. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, or authority semantics into Agnir Core.
9. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

Architecture/continuity changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations.

## Completed in the current implementation sequence

- Repository identity transition completed and canonical references reconciled to `iorLab/agnir`.
- Active ChatGPT-specific bootstrap shim removed; `AGNIR.yaml` is the direct repository/filesystem cold-start entry point.
- English and Simplified Chinese README entry points include synchronized Architecture and Continuity Flow diagrams with comprehension-first Chinese nodes.
- Shared conformance-only repository/filesystem resolver added at `conformance/repository_filesystem_reference.py`.
- Self-hosting checker now uses that resolver.
- Negative fixture suite covers `NOT_FOUND`, broken-locator `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.
- `repository-filesystem/0.1` now explicitly distinguishes unresolved candidate-root ambiguity from authority already fixed by a selected Project root.
- Conformance run `33143495855`, job `98759373389`, succeeded for both cold-start self-hosting and negative fixtures; durable evidence is `.agnir/evidence/2026-08-28-negative-discovery-fixtures.md`.
