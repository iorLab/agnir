# Agnir Next Actions

Agnir `v0.2.0` is stable. The real-Project, upgrade, parallel-lineage/reconciliation, VCS/non-VCS, execution-surface, and genuine mount-boundary gates are satisfied. Challenge #24 returned `FAIL-DOCS` with a concurrent `FAIL-CONFORMANCE`: the 0.1→0.2 migration path lacked deterministic string-lineage normalization and the reference applied initial-lineage validation before the explicit authorization gate. PR #25 repaired both boundaries; PR run `33977471985` and authoritative main run `33977552588` succeeded. The independent-implementation gate remains open only until one genuinely fresh frozen implementation produces a clean `PASS` against the new exact authoritative checkpoint.

1. **Verify this checkpoint on authoritative `main`.** Treat the complete conformance result for the checkpoint commit as release-blocking evidence; do not launch the next external challenge until it is green.
2. **Create one new clean acceptance challenge pinned to the exact post-checkpoint revision.** The reviewer must begin in a genuinely fresh unpersonalized context and must not inspect prior challenge issues/reports, PR history, `.agnir/**`, private Agnir context, or `conformance/*_reference.py` before the permitted Phase C boundary.
3. **Require systematic pre-freeze boundary coverage without supplying answers.** Expected results must be derived from pinned public schema/profile/specification. Coverage must include serialization type/null/requiredness, identity/lineage boundaries, local locator target shape/indirection, Evidence collection, checkpoint semantics, and explicit 0.1→0.2 migration authorization/normalization/idempotence/conflict/stale-source behavior.
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
- challenge #24 source/archive: `56892930c139f4d662b7c9aa9c0f33cc829a61fa` / `e9d7f135403093ea277fcc8f9704cfe8c73850c2a9ed20b79b7fa395be5f934a`, verdict `FAIL-DOCS` + concurrent `FAIL-CONFORMANCE`;
- #24 freezes: Phase A `75d1ef7882de2c83205cdd942b84f8fdb326afb5c4d8a46cb8c8c9c871cee1ee`, Phase B `aca11730d7ad5726eaba84d1acdad016b5644207051f6b75d403cce8b3e9ce1d`;
- #24 boundary matrix 71/71; required semantic receipts all pass;
- migration-boundary repair PR head/run: `e7d65d7de8e3c03e51c1034d645c247429c03c89` / `33977471985` success;
- migration-boundary authoritative repair/run: `f82d795a025e38ae6c33b51ef078bec819e766c7` / `33977552588` success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Core/profile `0.1` → `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
- For a still-Core-0.1 source, explicit migration authorization precedes migration-only initial-lineage validation.
- String-valued initial-lineage input for the published 0.1→0.2 migration is normalized by the contract-defined leading/trailing Unicode `White_Space` set before emptiness, persistence, idempotence, or conflict comparison.
- Under repository/filesystem 0.2, string-valued incompatible Core version is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing/null/wrong-type version serialization is `AGNIR_DISCOVERY_INCONSISTENT`.
- Local State/Next Actions/non-null Decisions resolve to regular files; non-null local Evidence resolves to a directory; baseline Evidence is flat, and local filesystem indirection must not read canonical targets outside the selected Project root without authorized external binding.
- A fresh reviewer must not receive private answers, prior findings, or reference knowledge before the allowed comparison boundary.
