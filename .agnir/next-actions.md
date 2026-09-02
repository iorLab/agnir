# Agnir Next Actions

This temporary validation lineage exists only to prove a real-repository migration from immutable published `v0.1.1` to the explicit Core/profile `0.2` RC package.

1. Run validation-root fresh activation and `repository-filesystem/0.2` discovery on this exact ref.
2. Run stable Core `0.1` regression, Core `0.2`, VCS/lineage/profile/migration, RC fixture, and full conformance suites.
3. If green, record the exact validation revision/run back on `release/v0.2.0-rc.1` durable Evidence.
4. Close any validation PR used only for CI discovery and retire temporary validation refs after receipts are captured.
5. Do not merge this validation lineage into `main` and do not use it as the RC tag target.
