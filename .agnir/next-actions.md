# Agnir Next Actions

This selected continuity is the `v1.0.0-rc.1` release lineage. Candidate `e4d5ad8f7e4013314401ecf3d987edb66f509ce5` / run `34026056687` and evidence checkpoint `c05199291b8eda9ccceca8b918545773e330ad75` / run `34026116079` are both green. Publication is now armed under the exact workflow contract.

1. **Verify the armed revision's repository conformance job succeeds.** Publication must remain dependency-gated on that exact SHA.
2. **Verify immutable prerelease publication.** Require tag `v1.0.0-rc.1` to target the exact armed revision, Release `prerelease=true`, `draft=false`, and GitHub `releases/latest` to remain `v0.2.0`.
3. **Checkpoint the publication result in this RC lineage.** Record exact armed revision, publication run, tag target, Release id/flags, and latest-stable verification.
4. **Run a fresh post-publication evidence cycle from immutable tag `v1.0.0-rc.1`.** Re-exercise Core/profile/schema/discovery/failure/checkpoint/lineage/VCS/non-VCS/0.2 regression/0.2→1.0 promotion/0.1→0.2→1.0/self-host/package/release gates against the tag source.
5. **Only after the immutable RC cycle is accepted, prepare stable `v1.0.0`.** Reconcile accepted RC results into the authoritative lineage and use a distinct stable publication step; never move or mutate the RC tag.
6. **Keep FishUp production publication separate.** Do not advance FishUp `main` without separate Principal authorization.
