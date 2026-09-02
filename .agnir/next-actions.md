# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release on exact target `e9712357ab590e5c1e5357b3cf3219d07d789aff`. The Core `0.2` Parallel Continuity implementation/evidence line has passed synthetic, dual-backend, concrete migration, and first real-consumer validation and is now at the safe-main-integration boundary.

## Main integration and RC sequence

1. **Verify the reconciled main integration candidate without moving `main`.** Require stable self-hosting cold-start, experimental VCS branch continuity, Core `0.2` non-VCS/VCS mapping, repository-filesystem `0.2`, VCS lineage binding, semantic/concrete `0.1`→`0.2` migration, and full conformance on the exact candidate tree.
2. **If the candidate is green and the target/source refs are unchanged, advance `main` directly to that exact reconciled revision.** Do not use ordinary server-side merge-first/follow-up-repair and do not publish feature-local State / Next Actions / Decisions as target truth.
3. **Verify authoritative `main` after advancement.** Re-run/fetch the main workflow result and fresh-resolve `AGNIR.yaml` → Current State / Next Actions / Decisions / Evidence from `main`; confirm published `v0.1.1` provenance remains unchanged and Core `0.2` remains pre-RC rather than silently stable.
4. **Close/resolve stacked PR `#4` / `#5` through the exact Agnir-aware integration ancestry.** Preserve their feature tips/evidence until GitHub recognizes the integrated ancestry; do not create a second merge path.
5. **Prepare `v0.2.0-rc.1`.** Convert only the artifacts that should become RC contracts out of draft status, update repository release/version metadata deliberately, bind the RC to an exact verified revision, and keep repository SemVer distinct from Core/profile compatibility versions.
6. **Exercise RC migration and fresh resume.** Validate fresh installation plus explicit published `v0.1.1` Core/profile `0.1` → Core/profile `0.2` migration on at least one real Project, then cold-start resume without predecessor-private context.
7. **Publish final `v0.2.0` only after RC gates remain green.** Do not move an RC/stable tag after publication.
8. Continue broader real-Project/execution-surface evidence for eventual `v1.0.0`; add new synthetic lineage cases only when real integration/RC evidence exposes a missing invariant.

## Stable maintenance obligations to preserve

- Root `SKILL.md` remains the canonical Agent-facing operational package.
- Repository activation and execution-surface activation remain separate completion dimensions.
- Compatible `v0.1.1` upgrades preserve Project identity, memory locators/content, unrelated instructions/extensions, and stable activation routes.
- `latest stable` resolves to an actually published stable tag/release, never moving `main` by default.
- Transactional checkpoint no-op/coherent-publication and stale-base safety remain active.
- Prompt-free Project activation and non-destructive `AGENTS.md` merge remain active.
- Real mount-boundary behavior remains unproven until a genuine mount-capable environment is available.

## Core 0.2 release evidence

- Agnir pre-integration Core `0.2` checkpoint: `68cc443d6c44929f1b71d9d534e9b0f73f9745bf`.
- Agnir conformance run: `33620080730` — all stable/experimental/full-suite gates success.
- Svif final real-consumer checkpoint: `d42489f72cc8985d353ccbf2f9b6ae7249fe6480`.
- Svif final validation run: `33619807614` — repository-integrity, portable-contracts, runtime-kernel all success.
- Published stable release remains `v0.1.1` at `e9712357ab590e5c1e5357b3cf3219d07d789aff`.

## Core 0.2 invariants to preserve

- Durable continuity belongs to the Project.
- Project identity is not lineage identity.
- Lineage identity is logical and durable within Project scope; selectors/bindings and revision receipts are not identity.
- Selection is explicit/contextual/default and never guessed by sibling scanning.
- Agnir-aware fork publishes lineage identity + selector binding + coherent inherited/reconciled continuity together.
- Checkpoints are lineage-local by default.
- Source continuity is integration input, not automatic target truth.
- Integrated Project state and reconciled target continuity publish coherently.
- Target-ref advancement is a publication boundary.
- Stale source/target candidates fail rather than overwrite newer truth.
- Core/profile `0.1`→`0.2` is explicit migration; compatible operational upgrade semantics remain separate.
- Cross-Project identity mismatch remains a hard boundary.
