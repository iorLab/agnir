# Agnir Next Actions

Agnir `v0.2.0` remains the latest published stable release. Issue #27 / PR #28 has completed and the Core/profile `1.0` semantics-preserving promotion candidate is accepted on authoritative `main` at `0337be5c0ef5ccd74d207135646b30947c275776`, with main verification run `34025528147` successful. The next release stage is the explicit `v1.0.0-rc.1` cycle.

1. **Create the temporary `release/v1.0.0-rc.1` lineage from the verified authoritative checkpoint.** Give it its own logical lineage identity `urn:agnir:lineage:v1.0.0-rc.1` and bind that identity separately to selector `refs/heads/release/v1.0.0-rc.1`.
2. **Promote the release-lineage self-host explicitly from Core/profile `0.2` to `1.0`.** Preserve Project identity and durable continuity semantics; change the compatibility declaration only under the accepted `spec/CORE_0_2_TO_1_0_PROMOTION.md` contract. Do not reinterpret authoritative `main` as already promoted.
3. **Prepare exact RC package metadata.** Set repository `VERSION` to `1.0.0-rc.1`, set release-lineage `AGNIR.yaml` to Core `1.0` / `repository-filesystem/1.0`, record RC lineage binding and package provenance, and update release documentation only where it describes the RC candidate rather than published stable status.
4. **Run the complete RC candidate gates before publication is armed.** Require `conformance/check_agnir_1_0.py`, Core/profile/schema/discovery/failure/checkpoint/lineage/VCS/non-VCS/migration/promotion/package suites, and full `test_*.py` to pass on the exact release-lineage revision.
5. **Arm `v1.0.0-rc.1` publication only after the exact candidate is green.** The final release-branch commit message must be exactly `rc: arm v1.0.0-rc.1 publication`; verify the dormant workflow creates an immutable prerelease tag/release pointing to that exact revision while `releases/latest` remains `v0.2.0`.
6. **Run the fresh RC evidence cycle against the immutable RC source.** Re-exercise cold start/fresh resume, failure mapping, checkpoint semantics, lineage isolation/integration, 0.2 compatibility regression, 0.2→1.0 promotion, composed 0.1→0.2→1.0, self-host, package, and release checks. Any release-blocking defect reopens the relevant gate.
7. **Prepare stable `v1.0.0` only after the RC is accepted.** Reconcile the accepted RC result back into the authoritative lineage, verify main, then use a distinct stable publication step/tag/release; do not retag or mutate the RC.
8. **Keep FishUp production publication separate.** Do not advance FishUp `main` unless the Principal separately authorizes its Cloudflare/D1 production side effect.

## Current high-value receipts

- stable `v0.2.0`: `fc84095ed5d500be9e1b43a4af0e93356571bbd4`, publication run `33711982062`;
- independent acceptance issue/source: `#26` / `eabc599d589f2c3dfe6b3d9508a093d120f33c95`;
- issue #26 ZIP SHA-256: `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`;
- issue #26 final verdict: `PASS`;
- promotion tracking: issue `#27`, PR `#28`;
- final promotion candidate: `dfc1af9203673cfc2aa41633143c4c90e274c976`;
- final promotion candidate CI: `34020641603` success;
- promotion merge to main: `0337be5c0ef5ccd74d207135646b30947c275776`;
- authoritative main verification: `34025528147` success;
- public Core/profile 1.0 contracts: `spec/AGNIR_CORE_1_0.md`, `profiles/REPOSITORY_FILESYSTEM_1_0.md`;
- explicit promotion contract: `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Validation/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- Historical Core/profile `0.1` and `0.2` contracts are not rewritten by the 1.0 promotion.
- Existing valid `0.2` Projects remain supported by the v1 distribution unless Project policy explicitly chooses promotion.
- Merging 1.0 contract machinery into `main` does not itself promote the authoritative Project's compatibility declaration.
- The independent-implementation gate is satisfied and is reopened only by later material public-contract change or evidence of a real defect.
