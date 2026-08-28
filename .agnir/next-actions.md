# Agnir Next Actions

1. **Add real repository/filesystem boundary pressure** for symlink escape and Git worktree cold-start behavior. Do not fake a mount case; record mount-boundary validation as unproven unless a real mount-capable test environment is used.
2. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
3. Freeze Agnir Core `0.1` release compatibility notation only after the remaining boundary/migration pressure cases pass.
4. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, or authority semantics into Agnir Core.
5. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

Architecture/continuity changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations.

## Completed in the current implementation sequence

- Repository/filesystem negative fixtures cover `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, pre-root-selection `AMBIGUOUS`, and nested selected-root isolation.
- Durable SQLite-style non-repository fixture proves Core continuity without repository/filesystem discovery, including checkpoint and fresh-resolver resume.
- External-memory fixture distinguishes missing Discovery Record (`NOT_FOUND`), denied known authorization reference (`UNAUTHORIZED`), and authorized-but-missing required memory (`UNRESOLVABLE`) without storing plaintext credentials.
- Multi-project workspace isolation proves a locator-only shared registry does not become a shared continuity root.
- Generic Locator Chain fixtures now cover `CYCLE`, `STALE`, and materially `INCONSISTENT` semantics, closing the executable baseline across all Core `0.1` discovery failure classes.
- Locator Chain conformance run `33144042330`, job `98761070215`, succeeded; durable evidence is `.agnir/evidence/2026-08-28-locator-chain-failures.md`.
