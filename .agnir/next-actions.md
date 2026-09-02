# Agnir Next Actions

Agnir `v0.1.1` remains the latest published stable release. Temporary branch `release/v0.2.0-rc.1` is the Core `0.2` / `repository-filesystem/0.2` RC lineage for Project `urn:agnir:project:agnir-core`, logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, selector `refs/heads/release/v0.2.0-rc.1`.

## Complete v0.2.0-rc.1

1. **Run final exact-candidate conformance.** Require the complete release-branch workflow to pass on the candidate revision containing truthful `agnir/operations` provenance (`0.2.0-rc.1` / `bee78b2c9bb8c5ce5916d08691019dcde939b813`), final State/Next/Evidence, `RELEASE.md`, and repository-tree update.
2. **If and only if that exact candidate is green, publish immutable prerelease `v0.2.0-rc.1`.** Create the tag directly at the verified candidate revision and create a GitHub Release with `prerelease=true`, `draft=false`. Never move the tag.
3. **Verify publication.** Confirm the tag resolves directly to the exact green candidate, the Release is marked prerelease, and `v0.1.1` remains the latest stable release semantics used by README/Skill upgrade resolution.
4. **Record a post-publication checkpoint without retagging.** Persist the actual tag target, Release id/publication receipt, and final verification run on the release branch after publication; this later checkpoint must not redefine the immutable RC target.
5. **Close and retire validation-only surfaces after receipts are durable.** Close Draft PR #7 without merge and retire `validation/v0.2.0-rc.1-from-v0.1.1` plus `release/validation-v0.2.0-rc.1-from-v0.1.1` when safe. Their immutable commits/runs remain Evidence.
6. **Do not move `main` as part of RC publication.** Later, reconcile the RC lineage back into authoritative `main` with the same staged target-publication discipline. Final stable `v0.2.0` is a separate decision after the RC cycle.
7. Continue broader real-Project/execution-surface evidence toward `v1.0.0`; do not invent additional synthetic gates unless RC/consumer evidence exposes a missing invariant.

## Completed RC gates

- safe Core `0.2` main integration: `a32c9143687b72426617ddd701b90ffd237a111c`; authoritative-main CI `33653087179` success;
- post-integration main checkpoint: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`; CI `33653383024` success;
- RC self-host migration: `a72654060c21600e1b7a4345634e09f9222ca4fb`; CI `33654332505` success;
- synchronized RC Skill/contracts: `1ccede8d0f31565231dc05495a9c519ef5a45bc2`; CI `33673748474` success;
- fresh install + exact published-v0.1.1 fixture: `b6fde55e525f4a077a070e1cf181304a3dfd7a9d`; CI `33673869587` success;
- dedicated release gate baseline: `bee78b2c9bb8c5ce5916d08691019dcde939b813`; CI `33673892651` success;
- real repository migration from immutable `v0.1.1`: migration revision `041f540a213c90e55d10e70aebaf14d8c1194a2a`, validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97`; CI `33674731595` success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Compatibility-line change is explicit migration, not silent upgrade.
- Source continuity is reconciliation input, not target truth.
- Target publication must be coherent; stale candidates fail.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch.
