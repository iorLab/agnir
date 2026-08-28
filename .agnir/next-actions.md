# Agnir Next Actions

1. **Complete a real predecessor-memory -> Agnir migration evidence envelope using `iorLab/svif@legacy/zerolocal-v0.1`.** Treat it as genuine predecessor evidence but classify its `.chatgpt/project-memory.yaml` as earlier v1/RPM-era serialization, not PPMP v2. The envelope must show what material durable knowledge was preserved, what was intentionally retired, and which migration regressions were discovered/repaired.
2. **Resolve the exact PPMP v2 external-fixture requirement before release freeze.** No qualifying second external Project with a clear PPMP v2.0.0 manifest was found in the current audit. Do not relabel older v1/RPM Projects as PPMP v2. Decide whether Core `0.1` release requires a genuinely historical external PPMP v2 Project or whether an explicitly classified PPMP v2 conformance fixture plus real older-predecessor migration evidence is sufficient.
3. **Freeze Agnir Core `0.1` release compatibility notation** only after the migration evidence decision is explicit, using the accumulated repository/filesystem, non-repository, authorization, multi-project, Locator Chain, and boundary evidence.
4. Keep a **real mount-boundary case** explicitly unproven until a mount-capable test environment is available; do not block Core release solely on a fake or simulated mount test.
5. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif execution, delivery, provider, authority, or distribution semantics into Agnir Core.
6. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Documentation maintenance rule

- Architecture/continuity changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set.
- Localized diagrams are comprehension-first rather than literal translations.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level repository map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is affected, both README language versions must update together.

## Completed conformance/documentation baseline

- Every named Agnir Core `0.1` discovery failure class has executable pressure.
- Durable non-repository SQLite continuity proves storage neutrality, including checkpoint and fresh-resolver resume.
- External-memory authorization distinguishes missing Discovery Record, denied authorization reference, and authorized-but-unresolvable memory without plaintext credentials.
- Multi-project workspace isolation proves locator-only registry metadata cannot become shared Project truth.
- Generic Locator Chain fixtures cover cycle, stale, and materially inconsistent continuity.
- Repository/filesystem boundary tests prove symlinked Project Entry Point behavior, reject implicit symlink escape, and cold-start a real Git worktree.
- English and Simplified Chinese READMEs contain synchronized Architecture / Continuity diagrams plus compact annotated repository trees.
- `REPOSITORY_TREE.md` now provides the complete tracked file-level repository map with responsibility annotations.
- Self-hosting conformance enforces the documentation baseline without byte-for-byte prose locking.
- Pre-checkpoint repository-documentation head `0ca0982a6807acd4af3bf945601f85a5882b88bc` passed conformance run `33146757923`.
