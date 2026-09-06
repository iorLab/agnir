# Agnir Next Actions

This selected continuity is the `v1.0.0-rc.1` release lineage. It is intentionally Core/profile `1.0`, but publication remains unarmed.

1. Run/inspect the exact release-branch conformance for the current candidate, including `conformance/check_agnir_1_0.py` and the full `test_*.py` suite.
2. Fix only genuine RC/package/conformance defects; do not introduce unrelated semantic redesign into the stability-promotion RC.
3. Preserve historical Core/profile `0.1` and `0.2` compatibility regression while allowing version-specific package tests to dispatch/skip only when they are genuinely inapplicable to this RC source.
4. Once an exact candidate revision is fully green, checkpoint its receipts into this release lineage.
5. Only then create the final branch commit whose message is exactly `rc: arm v1.0.0-rc.1 publication` so the dormant workflow may publish the immutable prerelease.
6. Verify tag target, Release prerelease/draft flags, and that `releases/latest` remains `v0.2.0`.
7. Run the fresh post-publication RC evidence cycle from the immutable tag source before any stable `v1.0.0` work.
8. Keep FishUp production publication separate; do not advance FishUp `main` without separate Principal authorization.
