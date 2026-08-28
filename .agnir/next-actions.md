# Agnir Next Actions

1. **Add explicit fixtures for remaining discovery failure classes**: `AGNIR_DISCOVERY_CYCLE`, `AGNIR_DISCOVERY_STALE`, and materially `AGNIR_DISCOVERY_INCONSISTENT`. The fixtures should pressure-test Locator Chain semantics without introducing a new normative storage profile.
2. **Add symlink, mount, and worktree boundary cases** for `repository-filesystem/0.1` without turning substrate details into Core requirements.
3. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
4. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
5. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, or authority semantics into Agnir Core.
6. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

Architecture/continuity changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations.

## Completed in the current implementation sequence

- Repository identity transition completed and active execution-surface bootstrap removed.
- English and Simplified Chinese READMEs include synchronized Architecture and Continuity Flow diagrams with comprehension-first Chinese nodes.
- Repository/filesystem negative fixtures cover `NOT_FOUND`, broken-locator `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.
- Durable SQLite-style non-repository fixture proves Core continuity without repository/filesystem discovery, including checkpoint and fresh-resolver resume.
- External-memory fixture distinguishes missing Discovery Record (`NOT_FOUND`), denied known authorization reference (`UNAUTHORIZED`), and authorized-but-missing required memory (`UNRESOLVABLE`) without storing plaintext credentials.
- Multi-project workspace isolation proves a locator-only shared registry does not become a shared continuity root: checkpointing one Project leaves another Project and the registry unchanged; embedded continuity in the registry is rejected as `INCONSISTENT`.
- Multi-project conformance run `33143930233`, job `98760729955`, succeeded; durable evidence is `.agnir/evidence/2026-08-28-multi-project-workspace-isolation.md`.
