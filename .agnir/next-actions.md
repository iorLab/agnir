# Agnir Next Actions

1. **Record the Core `0.1` compatibility/release freeze in `.agnir/decisions.md`.** Preserve the now-frozen separation between Core compatibility (`"0.1"`), profile compatibility (`repository-filesystem/0.1`), and repository SemVer (`0.1.0-rc.1` -> stable `0.1.0`).
2. **Create a final RC evidence record** covering the real ZeroLocal predecessor audit, exact PPMP v2 migration fixture, frozen compatibility semantics, and the final all-green conformance head.
3. **Run a final stale-wording/release-boundary audit** across normative and user-facing docs. Remove or qualify any wording that still incorrectly describes the line as an unfrozen development contract, while preserving `0.1.0-rc.1` as pre-release rather than claiming stable publication.
4. **Coordinate Svif against the Core compatibility line `"0.1"`.** Svif must not bind itself to a particular Agnir repository patch release, backend, adapter, or repository layout.
5. Keep the **real mount-boundary case** explicitly unproven until a mount-capable environment is available; do not invent a fake mount fixture and do not block RC solely on its absence.
6. **Do not create a public GitHub Release/tag without explicit authorization.** Repository RC preparation is authorized by the current development workflow; public release publication is a separate external effect.
7. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Completed in the current sequence

- Real non-fixture predecessor migration audit completed using `iorLab/svif@legacy/zerolocal-v0.1`; classified correctly as v1/RPM-era evidence rather than PPMP v2.
- The audit compared material durable knowledge and caught/repaired the lost `installable-plugin` product intent in Svif.
- The release criterion requiring a second independently hosted historical PPMP v2 Project was rejected as non-semantic historical availability.
- Canonical exact PPMP v2 source remains `legacy/ppmp-v2.0.0` at commit `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`.
- Exact PPMP v2 -> Agnir executable migration conformance was added under `conformance/fixtures/ppmp-v2/`, `conformance/ppmp_v2_migration_reference.py`, and `conformance/test_ppmp_v2_migration.py`.
- The fixture preserves material state / next actions / decisions / checkpoint evidence, cold-starts the migrated target through current Agnir discovery, and rejects v1/RPM serialization as PPMP v2.
- Full conformance including the migration fixture passed in run `33150059494` (job `98779726021`).
- Core `0.1` version/compatibility semantics were frozen in `spec/AGNIR_CORE.md`.
- Repository `VERSION` advanced from `0.1.0-dev` to **`0.1.0-rc.1`**.
- English and Simplified Chinese READMEs now describe the RC line and the frozen versioning model.

## Documentation maintenance rule

- Architecture/continuity changes update affected diagrams and explanations in both `README.md` and `README.zh-CN.md` in the same change set.
- Localized diagrams remain comprehension-first.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive tracked file-level map and must be updated whenever tracked files are added, removed, moved, or materially change responsibility.
