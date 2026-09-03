# Agnir Next Actions

Agnir `v0.2.0-rc.1` is published as an immutable prerelease and its accepted Project/package changes are now safely reconciled into authoritative `main` at `cd0427d26dddfabae768bcd76b78dc8d042151c7`. Main self-hosts Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`. Stable `latest` remains `v0.1.1`.

1. **Evaluate stable `v0.2.0` readiness from current authoritative main.** Re-read `RELEASE.md`, `RELEASE_MILESTONES.md`, `VERSIONING.md`, migration contracts, RC/main acceptance Evidence, and all known limitations. Separate release-blocking defects from non-blocking evidence gaps; do not infer stable readiness solely from the existence of the RC.
2. **If the stable gate is satisfied, construct a temporary exact `v0.2.0` stable-candidate lineage from current main.** Change repository SemVer/release metadata deliberately from `0.2.0-rc.1` to `0.2.0` without changing Core/profile compatibility lines, preserve Project identity and authoritative-main continuity semantics, and keep `main` unchanged while candidate validation runs.
3. **Run stable candidate conformance.** Require Core/profile `0.2` self-host, Core/profile `0.1` regression coverage, VCS/lineage/profile/migration pressure, fresh stable installation, published-v0.1.1 migration/fresh resume, and full suite on the exact candidate tree. Any release-blocking defect means repair and another candidate; never move `v0.2.0-rc.1`.
4. **Publish stable `v0.2.0` only from an exact verified candidate.** Create an immutable stable tag/release, verify `prerelease=false`, and verify GitHub `releases/latest` resolves to `v0.2.0` only after publication succeeds.
5. **Reconcile the published stable result back into authoritative main if the stable candidate is not already the exact main tree.** Use the same staged target-publication discipline and preserve authoritative lineage identity/binding.
6. **Retire temporary release/validation/integration refs when a safe delete-ref path is available.** Preserve immutable tags, commits, workflow runs, and durable Evidence; do not repurpose temporary refs.
7. Continue broader real-Project/execution-surface evidence toward `v1.0.0` and `V1_RELEASE_CRITERIA.md`.

## Current verified receipts

- authoritative-main integration: `cd0427d26dddfabae768bcd76b78dc8d042151c7`, tree `8c931fe53c09b019fd7bfd964c2ebc5d2b02dcd0`;
- candidate-tree PR run: `33705224034` success;
- authoritative-main push run: `33705292185` success;
- PR #9 auto-recognized merged through ancestry at the exact candidate;
- immutable RC tag: `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`;
- RC Release id: `381532232`;
- stable latest remains `v0.1.1` Release id `380414987`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source continuity is reconciliation input, not target truth.
- Compatibility-line changes require explicit migration; repository SemVer promotion alone does not change Core/profile lines.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch.
