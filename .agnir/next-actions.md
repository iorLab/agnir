# Agnir Next Actions

1. **Freeze Agnir Core `0.1` compatibility and repository release notation from the current contract itself.** Keep Core compatibility (`"0.1"`) distinct from repository SemVer and from profile identifiers such as `repository-filesystem/0.1`; do not use predecessor migration as a release prerequisite.
2. **Run a final current-architecture consistency review** across `spec/AGNIR_CORE.md`, `spec/AGNIR_DISCOVERY.md`, `profiles/REPOSITORY_FILESYSTEM.md`, `schemas/`, README documentation, self-hosting discovery, and the executable conformance suite.
3. **Reconcile Svif's Continuity Provider binding** against the current Agnir Core compatibility line only. Svif must not depend on Agnir historical serialization, repository layout, or predecessor migration behavior.
4. Decide release-candidate/stable readiness from the current Core/profile/conformance baseline. Historical PPMP/PPM/Sandminni evidence is not a release gate.
5. Keep a **real mount-boundary case** explicitly unproven until a mount-capable test environment is available; do not block release solely on a fake or simulated mount test.

## Documentation maintenance rule

- Architecture/continuity changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set.
- Localized diagrams are comprehension-first rather than literal translations.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level repository map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is affected, both README language versions must update together.

## Branch governance

- `main` is the only long-lived branch.
- Historical predecessor and retired work is indexed by commit SHA in `history/BRANCH_ARCHIVE.md`; live legacy/feature/site/tmp/release-pointer branch refs are not retained.
- Optional historical migration guidance remains under `history/MIGRATION_PPMP_V2.md`; it is not part of active Core semantics or release gating.

## Completed conformance/documentation baseline

- Every named Agnir Core `0.1` discovery failure class has executable pressure.
- Durable non-repository SQLite continuity proves storage neutrality, including checkpoint and fresh-resolver resume.
- External-memory authorization distinguishes missing Discovery Record, denied authorization reference, and authorized-but-unresolvable memory without plaintext credentials.
- Multi-project workspace isolation proves locator-only registry metadata cannot become shared Project truth.
- Generic Locator Chain fixtures cover cycle, stale, and materially inconsistent continuity.
- Repository/filesystem boundary tests prove symlinked Project Entry Point behavior, reject implicit symlink escape, and cold-start a real Git worktree.
- English and Simplified Chinese READMEs contain synchronized Architecture / Continuity diagrams plus compact annotated repository trees.
- `REPOSITORY_TREE.md` provides the complete tracked file-level repository map with responsibility annotations.
- Self-hosting conformance enforces the documentation baseline without byte-for-byte prose locking.
- `spec/` contains only current Agnir protocol material; PPMP migration guidance lives under `history/`.
