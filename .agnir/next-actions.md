# Agnir Next Actions

Agnir `v0.2.0` is stable. The minimum real-Project, real upgrade-boundary, real parallel-lineage/reconciliation, VCS/non-VCS lineage, materially distinct execution-surface, and genuine mount-boundary evidence gates are satisfied. Challenge #19 independently reported no behavior-material documentation ambiguity and no reference/published-contract contradiction, and its Phase B passed 30/30 recorded receipts, but one post-freeze null-version failure-dispatch defect produced `FAIL-IMPLEMENTATION`. The independent-implementation gate therefore remains open only because a clean frozen implementation PASS is still required.

1. **Create one more clean independent-implementation challenge pinned to the exact authoritative post-checkpoint revision.** The next reviewer must begin in a genuinely fresh unpersonalized context and must not inspect prior challenge findings, archives, issues/PR history, private Agnir design context, or `conformance/*_reference.py` before the permitted Phase C boundary.
2. **Use a schema-derived negative mutation matrix before Phase B freeze.** In addition to a direct positive fixture, require independently derived negative cases covering requiredness/absence, explicit null and wrong scalar/container type, const/enum mismatch, forbidden additional properties, and applicable pattern constraints. The challenge may require the categories but must not supply private expected answers; the reviewer derives each expected failure from the public pinned schema/profile.
3. **Preserve the Phase A → Phase B freeze → Phase C boundary.** Require auditable hashes/receipts before reference inspection and verify frozen artifacts remain unchanged afterward.
4. **Close the independent-implementation gate only on a clean `PASS`.** `FAIL-IMPLEMENTATION`, `FAIL-DOCS`, and `FAIL-CONFORMANCE` remain useful evidence but do not satisfy the acceptance rule.
5. **Do not modify Core/profile 0.2 merely to make the next reviewer pass.** Challenge #19 found the public contract and reference aligned. Only a newly demonstrated product-contract or conformance defect justifies another public-source repair.
6. **After independent acceptance, define the Core/profile `1.0` promotion candidate.** Promote the proven stable 0.2 semantics to clear `1.0` compatibility identifiers rather than shipping repository `v1.0.0` with confusing pre-1.0 protocol identifiers; preserve published `v0.2.0` history.
7. **Then prepare the explicit repository `1.0.0-rc` cycle.** The RC must run every normative suite from a fresh environment, including Core, repository/filesystem profile, schema, migration/upgrade, machine-visible failure paths, cold start/fresh resume, lineage, self-hosting, conformance dependencies, and release/package gates.
8. **Keep FishUp production publication separate.** Its migration-line validation is complete; do not advance FishUp `main` unless the Principal separately authorizes the Cloudflare/D1 production side effect caused by every main push.
9. **Retire temporary release/validation/repair refs when a safe delete-ref path is available.** Preserve immutable commits, workflow runs, artifacts, issues, releases, and Evidence; validation/repair lines are staging/evidence inputs, not automatic authoritative continuity.
10. **Keep stable maintenance compatible.** Future `v0.2.x` repairs may improve documentation, conformance, packaging, or implementation but must preserve Core/profile `0.2` semantics unless a deliberate new compatibility line is justified and explicitly migrated.

## Current high-value receipts

- stable Agnir `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- Svif authoritative published migration checkpoint: `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648`;
- FishUp validated migration-line head: `bea8c4e6e52347e1a0164596a5a9132b17de9631`, runs `33737783270` / `33737919224`;
- VocaPort authoritative installation candidate/publication: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3`, candidate run `33786785234`, publication verifier `33787496205`;
- VocaPort post-install checkpoint: `eb9a3cca54d6e5daa80fbacc72624a735057328b`, fresh-resume verifier `33787760565`;
- DSH Session 1 / corrected / Session 2 checkpoints: `b4f87d3ebd86d647adc2b7b101498ca4c80e6287` / `29549ebf45071003ae3e885664c7c9e960d838eb` / `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`;
- genuine mount-boundary final validation head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`, accepted run/job `33860631526` / `100984005488`;
- challenge #15 source/archive/verdict: `d4d5c5a441766ca5993366429ecf6235d7c2a7bc` / `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61` / `FAIL-IMPLEMENTATION`;
- challenge #17 source/archive/verdict: `5b73acf914e323ce337a0af295d5a9e96eaafdc8` / `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523` / `FAIL-CONFORMANCE`;
- schema/reference repair authoritative commit/run: `a0b322d4e7f4e62e2ed77121b0a1b4e3b2328d1a` / `33907748617` success;
- challenge #19 source/archive/verdict: `7e844fe8bde08be8288dbf05393e5e03601ea4f0` / `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854` / `FAIL-IMPLEMENTATION`;
- challenge #19 independent Phase B: 12/12 unit tests + 30/30 recorded receipts PASS; documentation sufficiency and reference alignment both pass that review.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Core/profile `0.1` -> `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
- The normative published schema is part of the executable repository-filesystem/0.2 contract; reference/conformance code must not silently accept forbidden or malformed serialized fields.
- A fresh independent reviewer must not receive private answers, prior challenge findings, or reference knowledge before the challenge's allowed comparison boundary.
- A negative mutation matrix strengthens implementation validation but does not replace independent contract reconstruction: expected behavior must come from public pinned sources, not challenge coaching.
- Real evidence must come from real behavior; synthetic equivalence, repository affiliation, product-platform diversity, ordinary filesystem behavior, or private reviewer coaching cannot substitute for the specific v1 gate being claimed.
