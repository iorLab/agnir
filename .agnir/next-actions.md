# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Core `0.2` Parallel Continuity work is active on `feature/core-0.2-lineage` / draft PR `#5`, stacked on the VCS evidence branch `feature/multibranch-continuity` / draft PR `#4`.

## Core 0.2 active work

1. Get the combined PR CI green with all five explicit gates: stable Core `0.1` self-hosting, experimental VCS branch continuity, Core `0.2` non-VCS lineage, Core `0.2` VCS mapping, and Core `0.1` → `0.2` migration, followed by the full suite. Fix failures at the earliest faulty layer; do not weaken stable invariants merely to admit experimental artifacts.
2. Pressure the current Core `0.2` Discovery Record direction against both backend models. Current direction: ordinary discovery resolves one selected lineage; Core does not require sibling-lineage enumeration. Confirm that profile-level defaults and explicit execution context are sufficient without introducing hidden branch assumptions.
3. Extend migration pressure from the storage-neutral semantic model into a concrete repository/filesystem migration candidate only after the Core `0.2` Discovery serialization/profile shape is settled. Preserve Project identity and durable truth; never silently treat a Core-line change as compatible upgrade.
4. Add/update branch evidence once CI passes, recording the two self-hosting regressions already found by the stable gate (`docs/` structural violation and dropped Project ownership invariant) and their non-weakening repairs.
5. Once synthetic VCS + non-VCS + migration conformance are green, validate Core `0.2` against one explicitly authorized real Project, preferably Svif, using genuine parallel work, independent checkpoints, and target reconciliation.
6. Before integrating PR `#4` / PR `#5`, construct an integration mechanism that reconciles final `main` Current State / Next Actions / Decisions before `main` advances. Do not use a normal server-side merge that first exposes feature-local `.agnir` truth as authoritative `main` continuity.
7. If Core `0.2`, migration, dual-backend, and real-Project gates pass, prepare repository `v0.2.0` as the next feature release. Do not label this architecture change `v0.1.2` merely for conservatism.
8. Keep `v1.0.0` gated by `V1_RELEASE_CRITERIA.md`: stable Core architecture, explicit compatibility/migration discipline, conformance/failure/publication integrity, multiple real Projects/execution surfaces, real upgrade evidence, independent implementability, repeatable release engineering, and an RC with no release-blocking Core defect.

## Invariants to preserve

- Durable continuity belongs to the Project.
- Project identity is not lineage identity.
- Lineage identity is logical and durable within Project scope; backend revision receipts are not identity.
- Lineage selection is explicit/contextual/default and never guessed by scanning siblings.
- A selected missing lineage does not silently fall back.
- Checkpoints are lineage-local by default.
- Source continuity is integration input, not automatic target truth.
- Integrated Project state and reconciled target continuity publish coherently.
- Stale target/source integration candidates fail rather than overwrite newer truth.
- Core `0.1` → `0.2` is explicit migration; same migration is idempotent and conflicting rebinding fails.
- Cross-Project identity mismatch remains a hard boundary.
- Stable Core `0.1` remains unchanged until Core `0.2` is accepted and intentionally published.

## Current stable release

- repository release: `0.1.1`
- tag: `v0.1.1`
- exact target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
