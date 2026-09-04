# Agnir Next Actions

Agnir `v0.2.0` is stable. The minimum real-Project, real upgrade-boundary, real parallel-lineage/reconciliation, VCS/non-VCS lineage, and materially distinct execution-surface gates are now satisfied. The accepted second execution surface is the VocaPort DSH two-session fresh activation/checkpoint/fresh-resume experiment. Remaining v1 work is concentrated in genuine mount-boundary evidence, independent-implementation documentation quality, and then an explicit `1.0.0-rc` cycle.

1. **Obtain genuine mount-boundary evidence.** Use a real environment where Project visibility genuinely crosses a mount / mounted-volume / workspace boundary. Exercise activation/discovery, continuity load, checkpoint persistence, and fresh resume across that actual boundary. Do not simulate a mount in the same ordinary repository filesystem and then claim the gate is closed.
2. **Obtain independent-implementation documentation evidence.** Have an implementer or rigorous reviewer reconstruct Core/profile behavior from published specs, migration docs, conformance, activation guidance, and repository maps without private design-chat context. Treat ambiguities as documentation/product defects and fix the public material rather than coaching around them.
3. **Refresh readiness immediately after either remaining external evidence gate changes.** If mount-boundary or independent-implementation work exposes a semantic/documentation defect, reopen any affected provisional gate instead of preserving a stale green status.
4. **Prepare a `1.0.0-rc` cycle only after mount-boundary and independent-implementation gates are credibly closed.** Construct an exact RC candidate and rerun every normative suite from a fresh environment, including Core, repository/filesystem profile, migration/upgrade, failure paths, cold start/fresh resume, lineage, and self-hosting.
5. **Keep FishUp production publication separate.** Its migration-line validation is complete. Do not advance FishUp `main` unless the Principal separately authorizes the Cloudflare/D1 production side effect caused by every main push.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable commits, workflow runs, releases, and Evidence. The VocaPort DSH validation lineage must not be merged into authoritative VocaPort continuity merely because its evidence was accepted by Agnir.
7. **Keep stable maintenance compatible.** Future `v0.2.x` fixes should preserve Core/profile `0.2` unless a deliberate new compatibility line is justified and explicitly migrated.

## Current high-value receipts

- stable Agnir `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- Svif authoritative published migration checkpoint: `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648`;
- FishUp validated migration-line head: `bea8c4e6e52347e1a0164596a5a9132b17de9631`, runs `33737783270` / `33737919224`;
- VocaPort authoritative installation candidate/publication: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3`, candidate run `33786785234`, publication verifier `33787496205`;
- VocaPort post-install checkpoint: `eb9a3cca54d6e5daa80fbacc72624a735057328b`, fresh-resume verifier `33787760565`;
- VocaPort DSH execution-surface protocol baseline: `439866051d7b9863565540fb592f408de64c1081`;
- DSH Session 1 checkpoint / corrected checkpoint: `b4f87d3ebd86d647adc2b7b101498ca4c80e6287` / `29549ebf45071003ae3e885664c7c9e960d838eb`;
- DSH Session 2 fresh-resume checkpoint: `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Core/profile `0.1` -> `0.2` remains explicit migration; stable `0.2.x` maintenance does not silently redefine compatibility.
- Real evidence must come from real behavior; synthetic equivalence, repository affiliation, product-platform diversity, or ordinary filesystem behavior cannot substitute for the specific v1 gate being claimed.
