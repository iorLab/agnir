# Agnir conformance / migration-audit checkpoint

Timestamp: 2026-08-28T13:23:00+08:00

## Verified repository state

- Canonical repository: `iorLab/agnir`.
- Authoritative branch: `main`.
- Pre-checkpoint head: `16adfdf69156eda5393f94495f250dccdff27117` (`docs: expose full Agnir conformance suite in Chinese`).
- Agnir conformance run `33144314449`: **success**.

## Core 0.1 executable baseline

The current conformance suite now provides executable pressure for all named Core discovery failure semantics:

- `AGNIR_DISCOVERY_NOT_FOUND`
- `AGNIR_DISCOVERY_AMBIGUOUS`
- `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`
- `AGNIR_DISCOVERY_PROJECT_MISMATCH`
- `AGNIR_DISCOVERY_UNRESOLVABLE`
- `AGNIR_DISCOVERY_UNAUTHORIZED`
- `AGNIR_DISCOVERY_CYCLE`
- `AGNIR_DISCOVERY_STALE`
- `AGNIR_DISCOVERY_INCONSISTENT`

Additional proven pressure includes:

- self-hosted repository/filesystem cold start;
- durable SQLite-style non-repository continuity with checkpoint and fresh-resolver resume;
- external-memory authorization references without secret values;
- locator-only multi-project workspace isolation;
- substrate-neutral Locator Chain cycle/stale/inconsistency semantics;
- symlinked Project Entry Point handling;
- rejection of relative-locator symlink escape without an authorized external Locator Chain;
- real Git worktree cold start.

Real mount-boundary behavior remains explicitly unproven.

## Predecessor migration audit finding

The migration spec is explicitly PPMP v2 -> Agnir 0.1, but accessible real predecessor Projects inspected during this checkpoint did not provide a second external Project with a clear PPMP v2.0.0 manifest.

`iorLab/svif@legacy/zerolocal-v0.1` is genuine external predecessor evidence relative to Agnir and can validate predecessor-memory -> Agnir semantic migration. However its `.chatgpt/project-memory.yaml` is an earlier v1/RPM-era serialization, not PPMP v2.0.0. `mattamior/agent-skills` likewise carries an older `.chatgpt/project-memory.yaml` form.

Therefore:

- these Projects MUST NOT be relabeled as PPMP v2 fixtures;
- they MAY be used to validate the migration spec's predecessor fallback semantics and durable-knowledge preservation requirements;
- exact external PPMP v2 migration evidence remains an unmet release-pressure item unless a qualifying Project is found or an explicitly classified PPMP v2 fixture is introduced without pretending it is an external historical Project.

## Material cross-project finding

The Svif predecessor audit found one real durable-knowledge regression: ZeroLocal predecessor state explicitly preserved `installable-plugin` as the long-term product form, while the current Svif rewrite had generalized that intent to `distribution` and omitted it from canonical state. Svif has begun restoring that product target. This is evidence that Agnir migration validation must compare material durable knowledge, not merely verify that new locator files exist.

## Resume point

1. Complete an explicit predecessor-memory -> Agnir migration evidence envelope using the real Svif predecessor, clearly labeling it as pre-PPMP-v2/v1-era evidence.
2. Continue searching only if needed for a genuinely external PPMP v2.0.0 Project; do not fake or relabel evidence.
3. Define Agnir Core `0.1` release/compatibility notation after migration evidence is reconciled.
4. Keep a real mount case unproven until an appropriate mount-capable environment exists.
