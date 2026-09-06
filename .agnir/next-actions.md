# Agnir Next Actions

This selected continuity is the `v1.0.0-rc.1` release lineage. Exact candidate `e4d5ad8f7e4013314401ecf3d987edb66f509ce5` passed full RC-source conformance in run `34026056687`; publication remains unarmed.

1. **Verify this candidate checkpoint itself.** The checkpoint commit that records `e4d5ad8…` / `34026056687` must pass `conformance/check_agnir_1_0.py` and the complete release-branch suite before publication is armed.
2. **If the checkpoint is green, arm publication in one final exact commit.** Its commit message must be exactly `rc: arm v1.0.0-rc.1 publication`; do not use that message before every release-blocking gate is green.
3. **Verify immutable publication.** Require tag `v1.0.0-rc.1` to target the exact armed revision, Release `prerelease=true`, `draft=false`, and GitHub `releases/latest` to remain `v0.2.0`.
4. **Run a fresh post-publication evidence cycle from the immutable tag source.** Re-exercise cold start/fresh resume, failure mapping, checkpoint semantics, lineage isolation/integration, 0.2 compatibility regression, explicit 0.2→1.0 promotion, composed 0.1→0.2→1.0, self-host, package, and release verification.
5. **Only after the immutable RC cycle is accepted, prepare stable `v1.0.0`.** Reconcile accepted RC results into the authoritative lineage and use a distinct stable publication step; never move or mutate the RC tag.
6. **Keep FishUp production publication separate.** Do not advance FishUp `main` without separate Principal authorization.
