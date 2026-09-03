# Agnir Current State

Agnir `v0.2.0-rc.1` is published as an immutable prerelease at `50a8cd565954e7e8055b8b628e2d620ac7357bab`, and its accepted Project/package changes are reconciled into authoritative `main`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Stable v0.2.0 candidate lineage — 2026-09-03

Temporary branch `release/v0.2.0` is the stable-release candidate carrier forked from verified authoritative main checkpoint `1af33e0cc470107aadaeb5d4d2f0f4570d81ee1d`.

Project identity remains `urn:agnir:project:agnir-core`. This branch self-hosts Core `0.2` / `repository-filesystem/0.2` on logical Continuity Lineage `urn:agnir:lineage:v0.2.0`, separately bound to selector `refs/heads/release/v0.2.0`. Selector and revision receipts are not lineage identity.

The repository SemVer candidate is `0.2.0`. This is a promotion from repository prerelease `0.2.0-rc.1`; it does not introduce another Core/profile compatibility change. Core remains `0.2` and the repository/filesystem profile remains `repository-filesystem/0.2`.

## Stable-readiness basis

The repository `v0.2.0` milestone requires Core `0.2` design, migration, dual-backend conformance, and real-Project validation. Those gates are now represented by durable evidence and successful CI:

- Core `0.2` lineage semantics and normative contract are implemented;
- non-VCS SQLite and VCS-backed models both exercise the Core lineage invariants;
- semantic and concrete `0.1` → `0.2` migration pass;
- a genuinely fresh Core `0.2` install passes;
- the exact published `v0.1.1` manifest shape migrates and fresh-resumes;
- a real repository migration starting directly from immutable `v0.1.1` passed;
- Svif supplied real consumer/Project lineage evidence during the Core 0.2 development cycle;
- immutable RC `v0.2.0-rc.1` was published only after exact-head conformance;
- the accepted RC was reconciled into authoritative main through a staged target-first candidate;
- authoritative main Core `0.2` fresh verification passed run `33705538455`.

No repository policy requires a fixed RC waiting period, and no release-blocking Core/profile defect is currently known from these gates. Real mount-boundary behavior remains explicitly unproven but is not a declared `v0.2.0` release gate.

## Stable candidate package boundary

This branch must promote RC-only status wording to stable `0.2` contracts and stable repository documentation, add a generic Core `0.2` self-host checker, and add stable-specific publication gates. It must preserve:

- Project identity and durable memory locators;
- Core/profile `0.1` compatibility artifacts and regression coverage;
- explicit `0.1` → `0.2` migration behavior;
- published RC tag immutability;
- short user-facing install/upgrade intents;
- non-destructive activation and execution-surface handoff semantics;
- staged target reconciliation and coherent publication semantics.

Until the stable package baseline has an exact verified revision, `extensions.agnir/operations` truthfully continues to record the already applied immutable RC package `0.2.0-rc.1` at `50a8cd...`. A later candidate checkpoint may record stable `0.2.0` provenance using an already verified immutable package baseline; it must not invent or self-reference its own future SHA.

`v0.1.1` remains GitHub `latest stable` until the exact stable `v0.2.0` candidate is published as a non-prerelease Release. `.agnir/next-actions.md` is the ordered resume plan.
