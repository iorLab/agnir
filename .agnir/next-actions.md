# Agnir Next Actions

Agnir `v0.2.0` is stable. The real-Project, upgrade, parallel-lineage/reconciliation, VCS/non-VCS, execution-surface, and genuine mount-boundary gates are satisfied. Challenge #22 returned `FAIL-CONFORMANCE`: the public contract was determinate, but the pinned reference misclassified wrong-container Core-version serialization. PR #23 repaired the repository-side mismatch and both PR/main conformance passed. The independent-implementation gate remains open only until one genuinely fresh frozen implementation produces a clean `PASS` against the new exact authoritative checkpoint.

1. **Verify this checkpoint on authoritative `main`.** Treat the complete conformance result for the checkpoint commit as release-blocking evidence; do not launch the next external challenge until it is green.
2. **Create one new clean acceptance challenge pinned to the exact post-checkpoint revision.** The reviewer must begin in a genuinely fresh unpersonalized context and must not inspect prior challenge issues/reports, PR history, `.agnir/**`, private Agnir context, or `conformance/*_reference.py` before the permitted Phase C boundary.
3. **Require systematic pre-freeze boundary coverage without supplying answers.** The reviewer should derive expected results directly from the pinned public schema/profile/specification and cover missing/null/wrong-type Core/profile serialization, identity/lineage/memory schema boundaries, local locator target shape and filesystem indirection, Evidence flat collection, external authorization, no-fallback behavior, checkpoint no-op/material/stale behavior, preservation/isolation, and explicit 0.1→0.2 migration boundaries.
4. **Preserve Phase A → Phase B freeze → Phase C discipline.** Record aggregate hashes before reference inspection and revalidate frozen bytes after all Phase C probes.
5. **Close the independent-implementation gate only on a clean `PASS`.** Any material documentation ambiguity, frozen independent implementation defect, or reference/conformance contradiction keeps the gate open and requires a fresh context after any public repair.
6. **After independent acceptance, define the Core/profile `1.0` promotion candidate.** Promote the proven 0.2 semantics to stable `1.0` compatibility identifiers without rewriting `v0.2.0` history or smuggling semantic redesign into the promotion.
7. **Then prepare the explicit repository `1.0.0-rc` cycle.** Rerun all normative Core/profile/schema/migration/failure/cold-start/fresh-resume/lineage/self-host/release/package gates from a fresh environment.
8. **Keep FishUp production publication separate.** Do not advance FishUp `main` unless the Principal separately authorizes the Cloudflare/D1 production side effect caused by every main push.
9. **Retire temporary repair/validation refs when a safe delete-ref path is available.** Preserve immutable commits, workflow runs, issues, releases, and Evidence.
10. **Keep stable maintenance compatible.** `v0.2.x` repairs may clarify documentation, conformance, packaging, or implementation but must not silently redefine Core/profile `0.2` semantics.

## Current high-value receipts

- stable `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- Svif authoritative migration checkpoint/run: `eba1b8538c4692a08bf69452525b735d23564599` / `33727957648`;
- FishUp migration-line head/runs: `bea8c4e6e52347e1a0164596a5a9132b17de9631` / `33737783270`, `33737919224`;
- VocaPort installation/publication: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3` / `33786785234`, `33787496205`;
- VocaPort fresh-resume checkpoint/run: `eb9a3cca54d6e5daa80fbacc72624a735057328b` / `33787760565`;
- genuine mount-boundary head/run/job: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa` / `33860631526` / `100984005488`;
- challenge #15: source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`, archive `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`, `FAIL-IMPLEMENTATION`;
- challenge #17: source `5b73acf914e323ce337a0af295d5a9e96eaafdc8`, archive `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`, `FAIL-CONFORMANCE`;
- challenge #19: source `7e844fe8bde08be8288dbf05393e5e03601ea4f0`, archive `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854`, `FAIL-IMPLEMENTATION`;
- challenge #20: source `3face3590510948003f958ae16c929c3105a7687`, archive `645fe95cd38b87640980dfeeb1055a0ab102c9fa5736d605a3cb87ac8b34e04c`, `FAIL-DOCS`;
- challenge #22: source `4dae8b81b5c523110e84311d9d84469e868fc064`, archive `a2ca0598728dd15efcc43f17573af8a16ea7abba80f316da9b39eb36697a84dd`, `FAIL-CONFORMANCE`;
- challenge #22 freezes: Phase A `f4e4fb7d478dee1df20353e125a2df2643610e7261354e273da435f1fa556837`, Phase B `794b7af1bb4fbbdf667dcb921690065869f14ebe05ce2aaf05d3e71c63be5a85`;
- #22 frozen/public matrix: 60/60 frozen expectations, 58/60 public-contract re-audit; semantic receipts 10/10; Phase C edge probes 7/7;
- malformed-version repair PR head/run: `65f3b519dc7d522cf5118f9c2c4004171b4d49ea` / `33969067170` success;
- malformed-version authoritative repair/run: `dde6ac366d6afb8a90bc59738451b9fc1b03df3f` / `33969102525` success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Core/profile `0.1` → `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
- Under repository/filesystem 0.2, a string-valued incompatible Core-version declaration is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing/null/wrong-container Core-version serialization is `AGNIR_DISCOVERY_INCONSISTENT`.
- Local State/Next Actions/non-null Decisions resolve to regular files; non-null local Evidence resolves to a directory; baseline Evidence is flat, and local filesystem indirection must not read canonical targets outside the selected Project root without authorized external binding.
- The published schema is the serialized-shape contract; profile rules additionally govern locator resolution and filesystem target shape.
- A fresh reviewer must not receive private answers, prior findings, or reference knowledge before the allowed comparison boundary.
- Coverage requirements may name categories but must not become a substitute private specification; expected behavior must be reconstructed from pinned public sources.
