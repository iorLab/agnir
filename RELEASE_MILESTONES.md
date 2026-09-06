# Agnir Release Milestones

- `v0.1.x`: established and pressure-tested the first stable Core `0.1` + repository/filesystem `0.1` profile.
- `v0.2.0`: stable pre-1.0 feature release line for Continuity Lineages. Its acceptance gates included Core `0.2` design, explicit `0.1` → `0.2` migration, materially different VCS and non-VCS backend conformance, fresh install/resume, real-Project validation, mount-boundary evidence, and an RC cycle. Historical Core/profile `0.2` remains a supported compatibility surface after 1.0 rather than being renamed in place.
- `v1.0.0`: stability milestone. Core `1.0` + `repository-filesystem/1.0` deliberately promote the independently validated `0.2` behavior into the first long-term stable compatibility identifiers. Existing `0.2` Projects remain supported and are not forcibly rewritten; explicit semantics-preserving `0.2` → `1.0` Project promotion remains separately authorized and conformance-tested.

## v1 acceptance receipts

The v1 stability milestone reached stable-package preparation only after:

- clean independent-implementation `PASS` from issue #26;
- Core/profile `1.0` promotion acceptance through issue #27 / PR #28;
- immutable `v1.0.0-rc.1` at `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC publication/conformance workflow `34026167762` attempt 1 success;
- fresh immutable-source workflow `34026167762` attempt 2 success;
- RC acceptance checkpoint `afc07d062b957e8dbfe3f859834c787e64aa52be`.

## Current publication status

Repository `1.0.0` is the stable source package. Stable publication remains a distinct authoritative operation: the staging result must be reconciled into `main`, exact-main conformance must pass, and only the exact main commit message `release: publish v1.0.0 stable` may arm the non-prerelease tag/Release.

`latest stable` resolution is determined by the actually published non-prerelease release. The accepted `v1.0.0-rc.1` remains prerelease evidence and never substitutes for stable resolution.
