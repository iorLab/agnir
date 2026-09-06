# Agnir Release Milestones

- `v0.1.x`: established and pressure-tested the first stable Core `0.1` + repository/filesystem `0.1` profile.
- `v0.2.0`: stable pre-1.0 feature release line for Continuity Lineages. Its acceptance gates are Core `0.2` design, explicit `0.1` → `0.2` migration, materially different VCS and non-VCS backend conformance, fresh install/resume, real-Project validation, mount-boundary evidence, and an RC cycle. Historical Core/profile `0.2` remains a supported compatibility surface after 1.0 rather than being renamed in place.
- `v1.0.0`: stability milestone. Core `1.0` + `repository-filesystem/1.0` deliberately promote the independently validated `0.2` behavior into the first long-term stable compatibility identifiers. Existing `0.2` Projects remain supported and are not forcibly rewritten; an explicit, semantics-preserving `0.2` → `1.0` Project promotion is separately authorized and conformance-tested. Publish stable `v1.0.0` only after the promotion candidate is complete, all historical regressions remain green, and at least one exact `1.0.0-rc` cycle passes every release-blocking gate.

## Current publication status

`v0.2.0` remains the latest published stable release while the Core/profile `1.0` promotion candidate is developed and verified. Presence of candidate 1.0 specifications, schemas, references, or tests on `main`/a promotion branch does not itself constitute a `v1.0.0` release.
