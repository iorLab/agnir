# Agnir Next Actions

Agnir `1.0.0` stable publication is armed on authoritative `main`. No further semantic change belongs in the publication transaction.

1. **Wait for the exact arm revision workflow.** `repository-filesystem` and `Publish v1.0.0 stable release` must both succeed on the same exact arm SHA.
2. **Verify publication independently.** Require `refs/tags/v1.0.0` == exact arm SHA; GitHub Release `draft=false`, `prerelease=false`; `releases/latest == v1.0.0`; accepted RC `v1.0.0-rc.1` remains exactly `092945289f1a0a9803e4fe0583104aa380ceaadc`.
3. **Run a fresh immutable stable-source verification cycle.** Re-run the publication workflow against the same immutable stable source without moving the tag; conformance and publication verification must be idempotent.
4. **Checkpoint final stable receipts into authoritative continuity.** Record stable tag/release IDs, publication run/jobs, fresh attempt, and latest-stable state in `AGNIR.yaml`, State/Next Actions/Evidence and operations provenance. Require the final checkpoint CI to pass.
5. **Close issue #29 and retire temporary validation/release refs when safe.** Never move published RC/stable tags.
6. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Publication preconditions satisfied

- exact prepublication checkpoint: `b99ea0d37cca852df023ef9071d4102c0376f0fe`;
- workflow `34038863673`: success;
- repository job `101501837860`: success;
- stable package gates: success;
- full suite: success;
- stable publication job at the prepublication checkpoint: skipped as required;
- accepted RC remains `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Stable publication is exact-authoritative-main only.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
