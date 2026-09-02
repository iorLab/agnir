# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Core 0.2 integrated main target — 2026-09-02

This continuity is reconciled for the revision intended to advance authoritative `main` with the combined PR `#4` + PR `#5` Project result. It preserves the existing stable release truth while adding the completed Core `0.2` Parallel Continuity development/evidence line.

Target parent before integration: `main` at `1bbdb5b258645ec7c5e0109c9b17dbaac004e625`.

Integrated development source: `feature/core-0.2-lineage` at `68cc443d6c44929f1b71d9d534e9b0f73f9745bf`, which contains the stacked `feature/multibranch-continuity` work. The combined compare is 86 commits ahead of the target with no target-side divergence.

The source checkpoint passed Agnir conformance run `33620080730`: stable Core `0.1` self-hosting, experimental VCS branch continuity, Core `0.2` non-VCS/VCS mapping, repository-filesystem `0.2`, VCS lineage binding, semantic and concrete `0.1`→`0.2` migration, and the full suite all succeeded.

## Compatibility and publication status

- repository stable release remains `0.1.1` / tag `v0.1.1`;
- stable tag target remains `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- this repository self-host remains Core `0.1` + `repository-filesystem/0.1` until the `0.2` release line is intentionally published/migrated;
- Core `0.2` and `repository-filesystem/0.2` are integrated as the pre-RC candidate contract/conformance line, not silently reclassified as stable `0.1` behavior;
- `VERSION` remains the published repository version until the RC release change is intentionally constructed.

## Core 0.2 evidence now integrated

The main candidate includes:

- backend-neutral Continuity Lineage Core draft and design rationale;
- VCS branch-continuity extension and selector/binding semantics;
- non-VCS SQLite lineage model;
- repository-filesystem `0.2` draft resolver/schema;
- storage-neutral and concrete Core/profile `0.1`→`0.2` migration;
- release/versioning/v1 stability criteria;
- the completed Svif real-consumer evidence.

The active Core `0.2` invariants are:

1. Project identity is distinct from logical lineage identity;
2. logical lineage identity is distinct from backend selector/locator and revision receipt;
3. ordinary work resolves one lineage deterministically without sibling scanning;
4. checkpoints are lineage-local;
5. an Agnir-controlled lineage fork publishes new lineage identity + selector binding + coherent inherited/reconciled continuity together;
6. integration is target reconciliation, not source-continuity copying;
7. staged integration does not advance the target publication boundary;
8. integrated Project result + reconciled target continuity publish coherently;
9. source or target advancement invalidates a stale integration candidate;
10. Core `0.1`→`0.2` is explicit migration preserving Project identity and durable truth.

## Real Project validation

Svif `urn:svif:project:svif-core` completed migration, two independently advancing logical lineages, real divergence, branch-local checkpoints, binding-driven fresh resume, staged two-parent integration with target ref unchanged, target reconciliation before publication, one coherent target advancement, and independent source survival.

Key receipts include source `d2d0c1bf25526b54490cce14c5aa8797c85c4d54` / CI `33618885830`, target pre-integration `79c5b7c7ee2ed545492702bea43d0f7135602f35` / CI `33619053159`, staged candidate `4b86b3adafe08cc2f7fd48eb4f685d2b633b25c3`, reconciled target `1cd25539c75f8a2a32c84b822c0db80b176fd319`, and final validation checkpoint `d42489f72cc8985d353ccbf2f9b6ae7249fe6480` / CI `33619807614`.

## Main integration safety

The final target tree is not a wholesale copy of feature-local continuity. Main's published `v0.1.1` facts, existing upgrade/execution-surface evidence, stable decisions, and maintenance obligations remain target truth. Feature continuity and evidence were used as reconciliation input.

The intended integration mechanism is: construct this reconciled two-parent revision while `main` remains unchanged → expose it on a temporary integration candidate ref for CI/review → if green, advance `main` directly to the exact reconciled revision. Do not use ordinary GitHub merge-first/follow-up-continuity-repair.

## Next release boundary

After the exact candidate passes CI and becomes `main`, verify authoritative-main cold-start/conformance and then construct `v0.2.0-rc.1` deliberately. The RC must exercise fresh install plus explicit migration/resume from published `v0.1.1` before final `v0.2.0` publication.

`.agnir/next-actions.md` is the canonical resume order and `.agnir/decisions.md` contains the merged active decision set.
