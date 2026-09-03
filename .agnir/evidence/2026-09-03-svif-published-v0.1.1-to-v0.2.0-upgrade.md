# Svif published v0.1.1 -> v0.2.0 downstream migration evidence — 2026-09-03

Status: **qualifying v1 downstream-upgrade evidence; authoritative Svif main acceptance verified.**

## Why this evidence matters

Agnir's v1 release criteria require production-like evidence from real Projects, including at least one Project that has crossed an Agnir upgrade boundary and, because parallel continuity is in Core, at least one real Project that has exercised independent lineages plus reconciliation.

Svif now supplies both kinds of evidence. This run is stronger than Agnir's synthetic migration fixtures and stronger than the earlier pre-release Svif Core 0.2 experiment because both compatibility endpoints are published Agnir releases and the accepted result is now Svif authoritative-main truth.

## Downstream Project

- repository: `iorLab/svif`;
- Project identity: `urn:svif:project:svif-core`;
- captured pre-migration authoritative main: `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- source Agnir release: published `v0.1.1`;
- source Agnir revision: `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- source compatibility: Core `0.1`, `repository-filesystem/0.1`.

## Target published package

- target Agnir release: published stable `v0.2.0`;
- target Agnir revision: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- target compatibility: Core `0.2`, `repository-filesystem/0.2`.

## Migration-line validation

Svif created a temporary migration lineage rather than mutating authoritative main first.

- preparatory dual-line adapter/test commit: `ddaee058efe4c8381f60f5a2ebcae0de9ee9203d`;
- atomic Project migration commit: `eac2ab0dd70695d972b99afad084614eae26c77c`;
- converged migration source checkpoint: `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`;
- migration source tree: `d6ffec2fddc48ec0052dd0531ca0088fb13b37b2`;
- exact source CI run: `33724859300`, all repository-integrity/runtime-kernel/portable-contracts jobs success.

The migration preserved:

- Project identity `urn:svif:project:svif-core`;
- `.agnir/state.md`;
- `.agnir/next-actions.md`;
- `.agnir/decisions.md`;
- `.agnir/evidence/`.

It introduced an explicit Core 0.2 logical lineage and kept logical lineage identity separate from its VCS selector.

## Target-owned reconciliation before publication

The validated migration source was not copied directly onto main. Svif reconciled target-owned authoritative continuity first.

- target-reconciled candidate: `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`;
- candidate tree: `191db90c0b959254025cb061159044c1b0ddf3d6`;
- first parent: captured main `dac058789a27f32f4ed1949874c1954f31f12bd8`;
- second parent: migration source `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`;
- target logical lineage: `urn:svif:lineage:authoritative`;
- target selector: `refs/heads/main`.

Candidate CI run `33725164044` passed all three Svif jobs. Draft validation PR #7 produced synthetic merge commit `1db24d60c7b4d60bde243c20fac1ab6ea1968798`, whose tree was exactly `191db90c0b959254025cb061159044c1b0ddf3d6`.

Fresh stale checks immediately before publication confirmed the captured main, migration source, and integration candidate refs had not advanced.

## Authoritative publication and fresh verification

Svif authoritative `main` advanced non-force exactly once from `dac058789a27...` directly to `2b5b92ab234...`. Ordinary PR merge was not used. Therefore there was no target-visible interval in which migration-line continuity was published first and repaired afterward.

Post-publication main push CI run `33725240001` passed repository-integrity, runtime-kernel full unittest discovery, and portable-contracts.

Fresh reads from authoritative main confirmed:

- Core `0.2`;
- profile `repository-filesystem/0.2`;
- Project identity `urn:svif:project:svif-core`;
- logical lineage `urn:svif:lineage:authoritative`;
- VCS selector `refs/heads/main`;
- unchanged durable memory locators;
- Agnir operational provenance `v0.2.0@fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- matching Svif Continuity Provider binding in `SVIF.yaml`.

Svif then wrote post-integration checkpoint `eba1b8538c4692a08bf69452525b735d23564599`; checkpoint CI run `33727957648` passed all three jobs.

## Observed usability / defect result

No Agnir `v0.2.0` semantic defect was exposed. The only failures during convergence were Svif tests/checks that still encoded the former current Core/profile `0.1` binding. Those were corrected without weakening retained Core/profile `0.1` regression coverage.

One product distinction proved important and is now guarded explicitly: Svif's current repository self-host binding can be Core/profile `0.2` while the already published immutable `v0.2.0-preview.1` Plugin first-use bootstrap remains on its published Core/profile `0.1` onboarding baseline. A downstream Project migration must not silently rewrite the behavior of an already published Svif distribution.

## v1 gate consequence

This evidence satisfies:

- `V1_RELEASE_CRITERIA.md` real upgrade evidence: **at least 1 real Project crossed an Agnir upgrade boundary**;
- real Project parallel continuity/reconciliation evidence: **satisfied via Svif**.

It does not satisfy the entire v1 real-world gate. Remaining evidence includes at least 3 materially different real Projects overall, at least 2 materially different execution surfaces/adapters, and genuine mount-boundary pressure when an appropriate environment exists.
