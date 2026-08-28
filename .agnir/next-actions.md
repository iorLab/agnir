# Agnir Next Actions

1. **Validate PPMP v2 -> Agnir migration against external predecessor evidence** and record an explicit migration evidence envelope. The validation must show what is preserved, what is intentionally not carried forward, and how a fresh Agnir Executor resumes without depending on predecessor-private bootstrap context.
2. **Freeze Agnir Core `0.1` release compatibility notation** after migration validation, using the accumulated repository/filesystem, non-repository, authorization, multi-project, Locator Chain, and boundary evidence.
3. Keep a **real mount-boundary case** explicitly unproven until a mount-capable test environment is available; do not block Core release solely on a fake or simulated mount test.
4. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, or authority semantics into Agnir Core.
5. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

Architecture/continuity changes are incomplete until the corresponding diagrams in both `README.md` and `README.zh-CN.md` are updated in the same change set. Localized diagrams are comprehension-first rather than literal translations.

## Completed conformance baseline

- Every named Agnir Core `0.1` discovery failure class has executable pressure.
- Durable non-repository SQLite continuity proves storage neutrality, including checkpoint and fresh-resolver resume.
- External-memory authorization distinguishes missing Discovery Record, denied authorization reference, and authorized-but-unresolvable memory without plaintext credentials.
- Multi-project workspace isolation proves locator-only registry metadata cannot become shared Project truth.
- Generic Locator Chain fixtures cover cycle, stale, and materially inconsistent continuity.
- Repository/filesystem boundary tests prove symlinked Project Entry Point behavior, reject implicit symlink escape, and cold-start a real Git worktree.
- Corrected filesystem-boundary run `33144199717`, job `98761550583`, succeeded; durable evidence is `.agnir/evidence/2026-08-28-filesystem-boundaries.md`.
