# Agnir Next Actions

Agnir `v0.1.1` remains the latest published stable release. Temporary branch `release/v0.2.0-rc.1` self-hosts Core `0.2` / `repository-filesystem/0.2` as logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, separately bound to selector `refs/heads/release/v0.2.0-rc.1`.

## Complete v0.2.0-rc.1

1. **Verify the synchronized RC package checkpoint.** Run exact-head release-branch CI after the Core/profile normative promotion, bilingual README update, Skill migration/lineage procedure update, repository-tree update, durable Decisions update, and `_DRAFT` cleanup. All RC self-host, stable `0.1` regression, Core `0.2`, VCS, profile, migration, and full-suite gates must remain green.
2. **Construct an exact RC candidate revision.** After the synchronized package is green, create a candidate checkpoint whose `extensions.agnir/operations` records repository release `0.2.0-rc.1` and an actual immutable candidate source revision used by subsequent install/migration validation. Avoid invented/self-referential provenance; use a two-step candidate/provenance strategy only if the immutable revision cannot otherwise be represented honestly.
3. **Validate a fresh RC installation.** Use a genuinely fresh test Project with explicit non-stable-target authorization. Install Core/profile `0.2`, create one durable Project identity and one logical lineage, keep any VCS selector separate, persist activation, and prove cold-start resume without predecessor-private context.
4. **Validate one real published-v0.1.1 migration.** On an explicitly authorized real Project, migrate from Core/profile `0.1` to `0.2`; preserve Project identity, memory locators/content, unrelated Project instructions/extensions, establish one initial logical lineage plus backend binding as applicable, and prove fresh resume. Do not classify the compatibility change as a compatible operational upgrade.
5. **Reconcile any defect at the earliest layer.** If fresh install or real migration exposes a contract/Skill/profile gap, fix that layer and repeat exact-head/candidate verification; do not weaken gates or add branch-specific exceptions.
6. **Run final exact-candidate conformance.** Require RC self-host, stable `0.1` regressions, Core `0.2` VCS/non-VCS/profile/binding/migration pressure, full suite, and the new real install/migration evidence.
7. **Tag/publish `v0.2.0-rc.1` only from the exact verified candidate.** Mark it prerelease, keep the tag immutable, and keep `latest stable` pointing to published `v0.1.1`.
8. **After RC evidence is complete, plan safe reconciliation back into authoritative `main`.** Use the same target-publication discipline: stage candidate, reconcile main continuity, validate exact tree, then advance main coherently. Final `v0.2.0` remains a separate stable-publication decision after the RC cycle.
9. Continue broader real-Project/execution-surface evidence toward `v1.0.0`; add new synthetic lineage cases only if real RC/consumer evidence exposes a missing invariant.

## Completed RC setup

- safe Core `0.2` integration into main: `a32c9143687b72426617ddd701b90ffd237a111c`; authoritative-main CI `33653087179` success;
- post-integration main checkpoint: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`; CI `33653383024` success;
- RC branch self-host migration: `a72654060c21600e1b7a4345634e09f9222ca4fb`; exact-head CI `33654332505` success;
- normative RC contracts: `spec/AGNIR_CORE_0_2.md`, `profiles/REPOSITORY_FILESYSTEM_0_2.md`, migration spec, 0.2 schema;
- repository SemVer: `0.2.0-rc.1`;
- latest published stable remains `v0.1.1` at `e9712357ab590e5c1e5357b3cf3219d07d789aff`.

## RC identity

- Project: `urn:agnir:project:agnir-core`.
- Core compatibility: `0.2`.
- profile: `repository-filesystem/0.2`.
- logical lineage: `urn:agnir:lineage:v0.2.0-rc.1`.
- VCS selector: `refs/heads/release/v0.2.0-rc.1`.
- RC baseline main: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.
- currently recorded applied operational package: published `v0.1.1`, intentionally pending exact RC candidate provenance.

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
