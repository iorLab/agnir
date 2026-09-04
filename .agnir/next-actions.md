# Agnir Next Actions

Agnir `v0.2.0` is stable. The minimum real-Project, real upgrade-boundary, real parallel-lineage/reconciliation, VCS/non-VCS lineage, materially distinct execution-surface, and genuine mount-boundary evidence gates are now satisfied. The accepted mount evidence is the Agnir self-host Docker bind-mount checkpoint/fresh-resume experiment at validation head `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`, run `33860631526`.

1. **Obtain independent-implementation documentation evidence.** Have an implementer or rigorous reviewer who is not relying on private Agnir design-chat history reconstruct Core/profile behavior from the published Core/profile specs, activation/discovery guidance, migration/versioning docs, conformance suite, repository map, and examples. The review must identify what is normative, rebuild expected state transitions/failure behavior, and attempt to implement or precisely specify a conforming resolver/checkpoint path without coaching from private context.
2. **Treat ambiguities as documentation/product defects.** If the independent implementation/review cannot determine required behavior from public repository material, fix the public specification, examples, repository maps, or conformance tests. Do not close the gate by supplying private oral/chat explanations.
3. **Re-run independent review after material documentation fixes.** Acceptance must be based on the corrected public material, not on the reviewer's accumulated private clarification from the failed attempt.
4. **Refresh readiness immediately after the independent-implementation gate changes.** Reopen any provisional Core/failure/compatibility gate if the review exposes a real semantic ambiguity rather than preserving a stale green status.
5. **Prepare an explicit `1.0.0-rc` cycle only after independent-implementation quality is credibly satisfied.** Construct an exact RC candidate and rerun every normative suite from a fresh environment, including Core, repository/filesystem profile, migration/upgrade, failure paths, cold start/fresh resume, lineage, self-hosting, and the current release/package gates.
6. **Keep FishUp production publication separate.** Its migration-line validation is complete. Do not advance FishUp `main` unless the Principal separately authorizes the Cloudflare/D1 production side effect caused by every main push.
7. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable commits, workflow runs, artifacts, releases, and Evidence. Neither the VocaPort DSH validation lineage nor the Agnir mount-validation lineage should be merged into authoritative Project continuity merely because their evidence was accepted externally.
8. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and explicitly migrated.

## Current high-value receipts

- stable Agnir `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- Svif authoritative published migration checkpoint: `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648`;
- FishUp validated migration-line head: `bea8c4e6e52347e1a0164596a5a9132b17de9631`, runs `33737783270` / `33737919224`;
- VocaPort authoritative installation candidate/publication: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3`, candidate run `33786785234`, publication verifier `33787496205`;
- VocaPort post-install checkpoint: `eb9a3cca54d6e5daa80fbacc72624a735057328b`, fresh-resume verifier `33787760565`;
- DSH Session 1 / corrected / Session 2 checkpoints: `b4f87d3ebd86d647adc2b7b101498ca4c80e6287` / `29549ebf45071003ae3e885664c7c9e960d838eb` / `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`;
- genuine mount-boundary final validation head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`;
- mount-boundary accepted run/job: `33860631526` / `100984005488`;
- mount-boundary artifact: id `9931961351`, digest `sha256:2c7bb33c87e4de0e95542cfb12b3759ecdb005c6085962856bb4a2ad052b25ce`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Core/profile `0.1` -> `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
- Real evidence must come from real behavior; synthetic equivalence, repository affiliation, product-platform diversity, ordinary filesystem behavior, or private reviewer coaching cannot substitute for the specific v1 gate being claimed.
