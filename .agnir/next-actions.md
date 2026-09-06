# Agnir Next Actions

The stable staging input is accepted and an authoritative-target candidate is being validated under issue #29.

1. **Run exact target-candidate conformance.** Require self-host, historical Core/profile 0.1/0.2, Core/profile 1.0, migration/promotion, VCS/non-VCS lineage, stable-package, and full `test_*.py` success.
2. **Re-read authoritative `main` immediately after candidate acceptance.** The candidate is based on `11148c3063e63dd1ea7450b9d538ac1eccec5639`. Any advancement invalidates direct publication and requires reconstruction/reconciliation.
3. **Advance authoritative `main` coherently only if the base is unchanged.** The target commit has the exact authoritative lineage identity `urn:agnir:lineage:authoritative` and selector `refs/heads/main`; no release-lineage binding may leak into main.
4. **Require the resulting exact main revision to pass its own CI.** Do not treat integration-branch CI as authoritative verification.
5. **Checkpoint main verification if needed before arm.** Publication remains dormant.
6. **Create a separate exact main commit whose message is exactly `release: publish v1.0.0 stable`.** This commit may record publication-arm evidence/status but must not introduce unrelated semantics.
7. **Wait for both jobs on the same arm SHA.** `repository-filesystem` and `Publish v1.0.0 stable release` must both succeed.
8. **Verify publication independently.** `refs/tags/v1.0.0` == arm SHA; Release `draft=false`, `prerelease=false`; `releases/latest == v1.0.0`; `v1.0.0-rc.1` still == `092945289f1a0a9803e4fe0583104aa380ceaadc`.
9. **Checkpoint final authoritative stable receipts and close issue #29.** Update release/operations provenance only from observed publication results.
10. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Current accepted receipts

- target base: `11148c3063e63dd1ea7450b9d538ac1eccec5639`;
- accepted staging source: `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- accepted staging checkpoint: `5f88a9c8bcc67753012f8bcae533241482dc1a7d`, run `34030753962`;
- accepted RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC Release id `383536840`;
- stable tag to be published: `v1.0.0`.

## Invariants

- Project identity != logical lineage identity != selector/revision receipt.
- Staging/source continuity is reconciliation input, not automatic target truth.
- Target publication is coherent; stale targets fail.
- Stable publication is main-only and exact-source gated.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
