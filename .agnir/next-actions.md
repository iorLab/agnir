# Agnir Next Actions

Agnir `v0.1.1` remains the latest published stable release. The active temporary release lineage is Core `0.2` / `repository-filesystem/0.2`, Project `urn:agnir:project:agnir-core`, logical lineage `urn:agnir:lineage:v0.2.0-rc.1`, selector `refs/heads/release/v0.2.0-rc.1`.

## Complete v0.2.0-rc.1 publication

1. Push this checkpoint with exact commit message `rc: arm v0.2.0-rc.1 publication`.
2. Require the ordinary `repository-filesystem` conformance job to pass on that exact commit. The dependent publication job must not run before conformance succeeds.
3. Require publication verification to prove immutable tag `v0.2.0-rc.1` points directly to that exact SHA and the GitHub Release is `prerelease=true`, `draft=false`.
4. Verify `v0.1.1` remains the latest stable semantics used by README/Skill upgrade resolution; do not advertise the RC as stable.
5. Create a post-publication checkpoint recording actual tag target, Release id, and workflow receipt without moving the tag.
6. Close Draft PR #7 without merge and retire validation-only refs after their immutable commit/run receipts are safely recorded.
7. Do not move `main` during RC publication. Later reconcile the RC lineage back into authoritative `main` using staged target publication. Final stable `v0.2.0` is a separate decision after the RC cycle.

## Completed gates

- safe Core `0.2` main integration: `a32c9143687b72426617ddd701b90ffd237a111c`; CI `33653087179` success;
- post-integration main checkpoint: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`; CI `33653383024` success;
- RC self-host migration: `a72654060c21600e1b7a4345634e09f9222ca4fb`; CI `33654332505` success;
- synchronized RC package: `1ccede8d0f31565231dc05495a9c519ef5a45bc2`; CI `33673748474` success;
- RC fresh-install/exact published migration fixture: `b6fde55e525f4a077a070e1cf181304a3dfd7a9d`; CI `33673869587` success;
- applied operational package baseline: `bee78b2c9bb8c5ce5916d08691019dcde939b813`; CI `33673892651` success;
- real repository migration from immutable `v0.1.1`: validation head `2219c5c8c37f1d62d3a839cc321e67d564b36f97`; CI `33674731595` success;
- final pre-publication candidate `79f8eb071d0b29bc4505d3448550c55619bd7cc9`; exact-head CI `33675222129` success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != lineage identity != selector/revision receipt.
- Compatibility-line changes require explicit migration.
- Target publication is coherent and stale candidates fail.
- Tag immutability is mandatory.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch.
