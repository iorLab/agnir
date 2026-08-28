# Agnir Next Actions

1. **Perform the final stable-release boundary audit** for Agnir Core `0.1`: review normative specs, profiles, README language variants, conformance docs, VERSION, and release-facing metadata for contradictions with the frozen RC compatibility model. Do not change Core `0.1` semantics during this audit.
2. **Run final release-candidate conformance after any cleanup** and record the resulting immutable head/run as the candidate for stable `0.1.0` publication.
3. **Coordinate Svif against Core compatibility `"0.1"`**, not against `0.1.0-rc.1` or any future patch build. Keep implementation/backend/adapter/repository-layout freedom intact.
4. Keep the **real mount-boundary case** explicitly unproven until a mount-capable environment is available. Do not invent a fake mount fixture; its absence alone is not a blocker for the current Core `0.1` RC baseline.
5. **Do not create a public GitHub tag/Release without explicit authorization.** Stable publication is a separate external effect from preparing and validating the repository.
6. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Completed release prerequisites

- Real non-fixture predecessor migration audit completed using `iorLab/svif@legacy/zerolocal-v0.1`, correctly classified as v1/RPM-era rather than PPMP v2.
- Material durable-knowledge comparison caught and repaired the lost Svif `installable-plugin` product intent.
- A second independently hosted historical PPMP v2 Project was rejected as a non-semantic release prerequisite.
- Canonical exact PPMP v2 source remains `legacy/ppmp-v2.0.0` at commit `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`.
- Exact PPMP v2 -> Agnir migration conformance exists under `conformance/fixtures/ppmp-v2/`, `conformance/ppmp_v2_migration_reference.py`, and `conformance/test_ppmp_v2_migration.py`.
- The exact fixture preserves state / next actions / decisions / checkpoint evidence, cold-starts the migrated target through current Agnir discovery, and rejects v1/RPM serialization as PPMP v2.
- Migration-fixture conformance passed run `33150059494`, job `98779726021`.
- Core `0.1` compatibility semantics are frozen in `spec/AGNIR_CORE.md` and `.agnir/decisions.md`.
- Repository `VERSION` is **`0.1.0-rc.1`**.
- English and Simplified Chinese READMEs describe the frozen RC/versioning model.
- RC freeze evidence is `.agnir/evidence/2026-08-28-core-0.1-rc1-freeze.md`.
- Frozen RC checker head `967292d95ba2ed7f3c5315d0f9e0540e0e84c263` passed run `33150494178`.

## Documentation maintenance rule

- Architecture/continuity changes update affected diagrams and explanations in both `README.md` and `README.zh-CN.md` in the same change set.
- Localized diagrams remain comprehension-first.
- README repository trees remain compact navigation views.
- `REPOSITORY_TREE.md` is the exhaustive tracked-file map and must be updated whenever tracked files are added, removed, moved, or materially change responsibility.
