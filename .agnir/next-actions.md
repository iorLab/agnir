# Agnir Next Actions

Agnir `v0.1.1` remains the latest published stable release. Temporary branch `release/v0.2.0-rc.1` now self-hosts Core `0.2` / `repository-filesystem/0.2` as logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, separately bound to selector `refs/heads/release/v0.2.0-rc.1`.

## Complete v0.2.0-rc.1

1. **Synchronize both READMEs with the RC architecture.** Replace stale Core/profile `0.1` diagrams/status text and the obsolete claim that generic lineage is deferred. Explain Core `0.2` Continuity Lineages, repository-filesystem `0.2`, VCS selector/binding mapping, explicit `0.1`→`0.2` migration, and the distinction between RC and `latest stable` in both English and Chinese.
2. **Update root `SKILL.md` for the versioned compatibility model.** Stable `latest stable` operations must still resolve published `v0.1.1` until final `v0.2.0`; an explicitly authorized RC target may install/migrate to Core/profile `0.2`. A compatibility-line change must use the explicit migration contract, preserve Project identity/durable truth, assign a logical lineage, and keep VCS selector/binding separate from lineage identity.
3. **Update `REPOSITORY_TREE.md` and release-facing maps.** Register the RC normative Core/profile documents, 0.2 schema, RC self-host checker, migration reference/tests, and release branch responsibilities.
4. **Remove or clearly demote obsolete draft-contract duplicates.** Once all references use `spec/AGNIR_CORE_0_2.md` and `profiles/REPOSITORY_FILESYSTEM_0_2.md`, delete the `_DRAFT` files or replace them only with unambiguous non-normative pointers; do not leave two competing normative-looking 0.2 contracts.
5. **Run exact RC branch conformance.** Require `conformance/check_agnir_0_2_rc.py`, explicit Core/profile `0.1` regression pressure, Core `0.2` non-VCS/VCS mapping, repository-filesystem `0.2`, VCS lineage binding, semantic/concrete `0.1`→`0.2` migration, and full suite.
6. **Build a fresh-install RC fixture.** Initialize a genuinely fresh Project with explicit RC authorization and prove cold-start recovery through Core/profile `0.2` without private predecessor context.
7. **Exercise one real published-v0.1.1 migration.** Use an explicitly authorized real Project, preserve its Project identity and durable truth, migrate from Core/profile `0.1` to `0.2`, bind one logical lineage, and prove fresh resume. Do not silently treat the compatibility change as an operational patch upgrade.
8. **Finalize RC operational provenance only after the operational package is synchronized.** Record `0.2.0-rc.1` under `agnir/operations` with an actual immutable applied revision from the verified RC candidate; do not invent a self-referential revision beforehand.
9. **Tag/publish `v0.2.0-rc.1` only from the exact verified candidate.** The tag/release must be immutable and marked prerelease. `latest stable` remains `v0.1.1`.
10. **After RC evidence is green, reconcile the release branch back into authoritative `main` using the same target-publication discipline before preparing final `v0.2.0`.**

## Current RC identity

- Project: `urn:agnir:project:agnir-core`.
- Core compatibility: `0.2`.
- profile: `repository-filesystem/0.2`.
- logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`.
- VCS selector: `refs/heads/release/v0.2.0-rc.1`.
- repository SemVer: `0.2.0-rc.1`.
- RC baseline main: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.
- latest stable repository release: `v0.1.1` at `e9712357ab590e5c1e5357b3cf3219d07d789aff`.
- currently recorded applied operational package: `v0.1.1`, intentionally pending RC procedure synchronization.

## Invariants

- Durable continuity belongs to the Project.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Compatibility-line change is explicit migration, not silent upgrade.
- Agnir-aware fork/migration publishes logical lineage + selector binding + coherent continuity together when those semantics change together.
- Checkpoints are lineage-local by default.
- Source continuity is reconciliation input, not target truth.
- Target-ref advancement is a publication boundary.
- Stale source/target candidates fail rather than overwrite newer truth.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch; `release/v0.2.0-rc.1` is temporary evidence/release work.
