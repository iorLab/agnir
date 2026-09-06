# Agnir Next Actions

The Agnir `1.0.0` stable source package is now reconciled into authoritative `main` and verified there. Stable publication remains not armed.

1. **Checkpoint the authoritative-main verification receipt.** Record exact main revision `ab5dcc3341d39631e843499632739864a90bba14`, workflow `34030974021`, and repository job `101480276759`. This checkpoint must itself pass exact-main CI.
2. **After that checkpoint is green, create the sole stable publication-arm commit on main.** Its commit message must be exactly `release: publish v1.0.0 stable`. The arm transition may record publication-intent evidence/status but must not introduce unrelated semantics.
3. **Wait for both jobs on that same exact arm SHA.** `repository-filesystem` and `Publish v1.0.0 stable release` must both succeed.
4. **Verify publication independently.** Require `refs/tags/v1.0.0` == exact arm SHA; GitHub Release `draft=false`, `prerelease=false`; `releases/latest == v1.0.0`; accepted RC `v1.0.0-rc.1` still == `092945289f1a0a9803e4fe0583104aa380ceaadc`.
5. **Perform a fresh immutable stable-source evidence cycle if useful before final closure.** Re-run the exact publication source in a fresh runner without moving the stable tag; publication verification must be idempotent.
6. **Checkpoint final stable receipts into authoritative continuity.** Update `AGNIR.yaml`, State/Next Actions/Evidence and operations provenance from observed release results, then require the final checkpoint CI to pass.
7. **Comment/close issue #29 and retire temporary validation/release refs when safe.** Never move published RC/stable tags.
8. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Authoritative verification receipt

- exact authoritative revision: `ab5dcc3341d39631e843499632739864a90bba14`;
- authoritative workflow: `34030974021`;
- authoritative repository job: `101480276759`;
- stable package gates: success;
- full suite: success;
- stable publication job: skipped as required;
- target validation run for same revision: `34030934536`, success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/staging continuity is reconciliation input, not automatic target truth.
- Stable publication is exact-authoritative-main only.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
