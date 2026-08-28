# Agnir Next Actions

Agnir `0.1.0` is release-ready. Development work required for the initial stable release is complete.

1. **Publication only:** after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release.
2. After publication, keep Core `0.1` and `repository-filesystem/0.1` frozen as compatibility lines. Any `0.1.x` maintenance must remain non-breaking.
3. Reconcile any future Svif dependency updates against the stable Agnir Core/profile compatibility lines, not repository internals or historical material.
4. Keep a real mount-boundary case as optional additional evidence when a real mount-capable test environment exists; do not represent ordinary directories as mount evidence.

## Documentation maintenance rule

- Architecture/continuity changes are incomplete until the corresponding diagrams and affected explanatory sections in both `README.md` and `README.zh-CN.md` are updated in the same change set.
- Localized diagrams are comprehension-first rather than literal translations.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive file-level repository map. Tracked file additions/removals/moves or material responsibility changes must update it in the same change set; if the compact tree is affected, both README language versions must update together.

## Stable release baseline completed

- Core compatibility line `0.1` frozen.
- Repository/filesystem profile compatibility line `repository-filesystem/0.1` frozen.
- Repository release SemVer set to `0.1.0`.
- Stable Core version semantics are normative in `spec/AGNIR_CORE.md`.
- Active profile no longer contains predecessor bootstrap fallback.
- `AGNIR.yaml` no longer references retired predecessor branches.
- `RELEASE.md` defines the publication contract and known limitation.
- All nine discovery failure classes have executable conformance pressure.
- Non-repository SQLite continuity, external-memory authorization, multi-project isolation, Locator Chain failures, symlink boundaries, and real Git worktree cold start are covered.
- Stable publication candidate `846d794384e24f4d0431bb72b0f1036c60503bdd` passed conformance run `33161463275`.
- Release-readiness evidence is `.agnir/evidence/2026-08-28-agnir-0.1.0-release-readiness.md`.
- Main-only branch governance remains in force; retired branch tips are indexed in `history/BRANCH_ARCHIVE.md`.
