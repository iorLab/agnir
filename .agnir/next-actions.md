# Agnir Next Actions

Agnir `v0.2.0` is stable and the v1 independent-implementation gate is satisfied by issue #26. The accepted reviewer used exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`, produced a clean frozen `PASS`, and exposed no unresolved documentation, conformance, or independent-implementation defect. The next release stage is now active as **issue #27 / branch `promotion/core-profile-1.0` / draft PR #28**. Initial candidate surfaces already exist for Core 1.0, repository-filesystem 1.0, the 1.0 manifest schema, and the explicit 0.2→1.0 promotion contract.

1. **Continue draft PR #28 as the single promotion candidate.** Do not merge or advance authoritative `main` to Core/profile 1.0 until the promotion implementation, conformance, documentation, and package/release gates below are complete and green.
2. **Keep the promotion semantics-preserving.** Core/profile `1.0` are the stable compatibility commitment for the proven `0.2` behavior, not a feature release or redesign. Any material semantic change must be separated and must reopen the relevant compatibility decision.
3. **Implement the exact `0.2` → `1.0` compatibility/promotion mechanics defined on the promotion branch.** Existing `0.2` Projects remain supported and are not forcibly rewritten by a 1.0 distribution; a Project that chooses to change its serialized compatibility identifiers requires explicit authorization, preservation, idempotence, stale-source conflict handling, and fresh 1.0 verification.
4. **Add 1.0 resolver/reference and conformance.** Cover schema validation/failure precedence, cold start/fresh resume, target-shape/Evidence rules, checkpoint no-op/material/stale behavior, lineage isolation/integration, VCS/non-VCS semantics, and self-host behavior under the 1.0 identifiers.
5. **Add direct promotion conformance.** Cover unauthorized 0.2→1.0 rejection, authorized preservation, repeat no-op, conflicting/stale promotion rejection, fresh 1.0 resume, and the composed 0.1→0.2→1.0 path without bypassing the established 0.1→0.2 lineage migration semantics.
6. **Update versioning/release documentation consistently.** `VERSIONING.md`, `RELEASE_MILESTONES.md`, README variants, `REPOSITORY_TREE.md`, `SKILL.md`, release/package checks, and examples must distinguish repository `1.0.0`, Core `1.0`, profile `1.0`, and historical `0.1`/`0.2` lines without ambiguity.
7. **Verify the complete promotion candidate on PR #28.** Run all Core/profile/schema/discovery/failure/checkpoint/migration/lineage/self-host/package suites and preserve exact promotion receipts. Draft status remains until the release-blocking suite is complete.
8. **Prepare explicit `v1.0.0-rc.1` only after promotion acceptance.** Pin an exact candidate revision, update release metadata, create the immutable prerelease only after all release-blocking checks pass, and preserve package/source provenance.
9. **Run the final RC evidence cycle from a fresh environment.** Re-exercise Core/profile/schema/migration/failure/cold-start/fresh-resume/lineage/self-host/release/package gates against the exact RC source. Any release-blocking Core defect reopens the relevant gate.
10. **Publish `v1.0.0` only after a clean RC cycle.** Reconcile the accepted RC into authoritative `main`, verify exact destination revision, publish immutable tag/release/artifacts, and checkpoint the final release receipts.
11. **Keep FishUp production publication separate.** Do not advance FishUp `main` unless the Principal separately authorizes its Cloudflare/D1 production side effect.

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
- issue #26 final verdict: `PASS`;
- acceptance checkpoint before promotion branch: `725bbb7f4d9f5a6a9aac74cf4e192392e3fac5d1`, conformance run `33981357353` success;
- active 1.0 promotion tracking: issue `#27`, branch `promotion/core-profile-1.0`, draft PR `#28`;
- initial PR #28 head after public contract scaffolding: `feb6fb6287de436ae23f364621c599e5da1f5478`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Historical Core/profile `0.1` and `0.2` contracts are not rewritten by the 1.0 promotion.
- Existing valid `0.2` Projects remain supported by the v1 distribution unless Project policy explicitly chooses promotion.
- The intended 1.0 work is stability promotion of proven semantics; semantic redesign requires a separately justified compatibility change and must not be smuggled into promotion.
- The independent-implementation gate is satisfied and is reopened only by later material public-contract change or evidence of a real defect.
