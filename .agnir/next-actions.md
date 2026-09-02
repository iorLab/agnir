# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Core `0.2` Parallel Continuity work is active on `feature/core-0.2-lineage` / draft PR `#5`, stacked on the VCS evidence branch `feature/multibranch-continuity` / draft PR `#4`.

## Core 0.2 active work

1. Complete the first CI cycle for the new non-VCS Core `0.2` gate. Fix any reference-model/test failures without weakening the lineage invariants.
2. Add an explicit VCS→Core mapping conformance layer showing that the existing real Git branch/worktree cases satisfy the same generic invariants as the SQLite namespace backend: shared Project identity, durable logical lineage identity, explicit selection, independent checkpointing, reconciliation, stale-candidate rejection where applicable, and coherent target publication.
3. Specify and test Core `0.1` → `0.2` migration. The default migration hypothesis is: an existing single continuity line becomes one initial/default lineage while preserving Project identity and existing durable truth. Migration must be explicit and idempotent; Core/profile line changes must not be silently treated as compatible upgrade.
4. Decide the final Core `0.2` Discovery Record semantics after dual-backend pressure. Current direction is one selected lineage per ordinary discovery result; Core does not require sibling-lineage enumeration.
5. Once synthetic VCS + non-VCS conformance pass, validate Core `0.2` against one explicitly authorized real Project, preferably Svif, using genuine parallel work and target reconciliation.
6. Before integrating PR `#4` / PR `#5`, construct an integration mechanism that reconciles final `main` Current State / Next Actions / Decisions before `main` advances. Do not use a normal server-side merge that first exposes feature-local `.agnir` truth as authoritative `main` continuity.
7. If Core `0.2`, migration, dual-backend, and real-Project gates pass, prepare repository `v0.2.0` as the next feature release. Do not call the result `v0.1.2` merely to be conservative about version numbers.
8. Keep `v1.0.0` gated by `docs/V1_RELEASE_CRITERIA.md`: stable Core architecture, explicit compatibility/migration discipline, conformance/failure/publication integrity, multiple real Projects/execution surfaces, real upgrade evidence, independent implementability, repeatable release engineering, and an RC with no release-blocking Core defect.

## Invariants to preserve

- Project identity is not lineage identity.
- Lineage identity is logical and durable within Project scope; backend revision receipts are not identity.
- Lineage selection is explicit/contextual/default and never guessed by scanning siblings.
- A selected missing lineage does not silently fall back.
- Checkpoints are lineage-local by default.
- Source continuity is integration input, not automatic target truth.
- Integrated Project state and reconciled target continuity publish coherently.
- Stale target/source integration candidates fail rather than overwrite newer truth.
- Cross-Project identity mismatch remains a hard boundary.
- Stable Core `0.1` remains unchanged until Core `0.2` is accepted and intentionally published.

## Stable maintenance still open

- Broaden execution-surface handoff and compatible-upgrade evidence with additional real Projects when useful.
- Keep real mount-boundary validation explicitly unproven until a genuine mount-capable environment is available.

## Current stable release

- repository release: `0.1.1`
- tag: `v0.1.1`
- exact target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
