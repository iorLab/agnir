# Agnir Next Actions

Agnir `v0.2.0` is stable and the v1 independent-implementation gate is now satisfied by issue #26. The accepted reviewer used exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`, produced a clean frozen `PASS`, and exposed no unresolved documentation, conformance, or independent-implementation defect. The next release stage is deliberate Core/profile `1.0` promotion, followed by the explicit repository `1.0.0-rc` cycle.

1. **Verify the acceptance checkpoint on authoritative `main`.** Treat the complete conformance result for the final checkpoint commit as release-blocking evidence before beginning promotion work.
2. **Define the Core/profile `1.0` promotion contract.** The intent is a stability promotion of the proven Core/profile `0.2` semantics, not a feature release or redesign. Record exactly which identifiers become `1.0` and which historical `0.1`/`0.2` contracts remain supported.
3. **Specify the exact `0.2` → `1.0` compatibility/promotion mechanics before implementation.** Decide and document how a Project declaring Core/profile `0.2` becomes `1.0`, what is preserved, whether the serialized compatibility identifier change is an explicit migration boundary, idempotence/conflict behavior, and how fresh 1.0 resume is verified. Do not silently reinterpret existing `0.2` manifests.
4. **Create the public 1.0 contract surfaces.** Add the Core 1.0 specification, repository/filesystem 1.0 profile, 1.0 manifest schema, migration/promotion guidance, and matching conformance while preserving immutable historical 0.1/0.2 material.
5. **Update release/versioning documentation consistently.** `VERSIONING.md`, `RELEASE_MILESTONES.md`, `V1_RELEASE_CRITERIA.md`, README variants, `REPOSITORY_TREE.md`, `SKILL.md`, release/package checks, and examples must all distinguish repository `1.0.0`, Core `1.0`, profile `1.0`, and historical compatibility lines without ambiguity.
6. **Build and verify a promotion candidate on a temporary branch.** Run all Core/profile/schema/discovery/failure/checkpoint/migration/lineage/self-host/package suites and add direct `0.2` → `1.0` promotion receipts. No candidate advances authoritative `main` until the complete suite is green.
7. **Prepare explicit `v1.0.0-rc.1`.** Pin an exact candidate revision, update release metadata, create the immutable prerelease only after all release-blocking checks pass, and preserve package/source provenance.
8. **Run the final RC evidence cycle from a fresh environment.** Re-exercise Core/profile/schema/migration/failure/cold-start/fresh-resume/lineage/self-host/release/package gates against the exact RC source. Any release-blocking Core defect reopens the relevant gate.
9. **Publish `v1.0.0` only after a clean RC cycle.** Reconcile the accepted RC into authoritative `main`, verify exact destination revision, publish immutable tag/release/artifacts, and checkpoint the final release receipts.
10. **Keep FishUp production publication separate.** Do not advance FishUp `main` unless the Principal separately authorizes its Cloudflare/D1 production side effect.

## Current high-value receipts

- stable `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- Svif authoritative migration checkpoint/run: `eba1b8538c4692a08bf69452525b735d23564599` / `33727957648`;
- FishUp migration-line head/runs: `bea8c4e6e52347e1a0164596a5a9132b17de9631` / `33737783270`, `33737919224`;
- VocaPort installation/publication: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3` / `33786785234`, `33787496205`;
- VocaPort fresh-resume checkpoint/run: `eb9a3cca54d6e5daa80fbacc72624a735057328b` / `33787760565`;
- genuine mount-boundary head/run/job: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa` / `33860631526` / `100984005488`;
- independent acceptance issue/source: `#26` / `eabc599d589f2c3dfe6b3d9508a093d120f33c95`;
- issue #26 ZIP SHA-256: `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`;
- issue #26 payload aggregate: `04e87857dcf22e5c5ea8fa8d3493523f8b009e8efc7ff3915a6ee371644a5d86`;
- issue #26 freezes: Phase A `1b422ad2ce17ed046baf488a180fe288f0a6d6599e642a5f3403d74d8d46eb56`, Phase B `6d75402a99795eddd1781a8e075584834995868becb9ae8fb7a74a5b20b86cde`;
- issue #26 boundary/focused/semantic/edge results: `81/81`, `10/10`, `19/19`, `10/10`;
- issue #26 final verdict: `PASS`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Historical Core/profile `0.1` and `0.2` contracts are not rewritten by the 1.0 promotion.
- The intended 1.0 work is stability promotion of proven semantics; semantic redesign requires a separately justified compatibility change and must not be smuggled into promotion.
- The independent-implementation gate is satisfied and is reopened only by later material public-contract change or evidence of a real defect.
