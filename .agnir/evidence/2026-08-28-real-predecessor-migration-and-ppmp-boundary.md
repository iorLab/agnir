# Real predecessor migration and PPMP boundary

Date: 2026-08-28

## Purpose

This record separates three evidence classes that had previously been easy to conflate:

1. **real external predecessor migration evidence**;
2. **exact PPMP v2 predecessor-format evidence**;
3. **Agnir 0.1 target conformance**.

They are related but not interchangeable.

## Real predecessor evidence

The real predecessor Project used for semantic migration pressure is `iorLab/svif@legacy/zerolocal-v0.1` at commit `8ccbb1d30520ca3d0b8b9f2cfe2963d35a853cf6`.

Its durable entry point is `.chatgpt/project-memory.yaml` with `version: 1`, and its mutable continuity is held in `.chatgpt/state.yaml`, `.chatgpt/next-steps.md`, and `.chatgpt/decisions.md`.

That Project therefore provides genuine **v1/RPM-era predecessor evidence**, not exact PPMP v2 evidence.

A detailed semantic migration audit is recorded in Svif at:

`.agnir/evidence/2026-08-28-zerolocal-predecessor-migration.md`

The audit classifies material durable knowledge as preserved, generalized, intentionally retired, repaired after regression, or explicitly not inherited. In particular, it detected and repaired the loss of the durable `installable-plugin` product target.

## Exact PPMP v2 evidence

Agnir's own predecessor release is preserved intact at:

- branch: `legacy/ppmp-v2.0.0`
- boundary commit: `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`

Its `.chatgpt/project-memory.yaml` explicitly declares:

- `ppmp.version: 2.0.0`;
- implementation `persistent-project-memory`;
- repository backend;
- ChatGPT adapter;
- durable state / next steps / decisions / checkpoint locations under `docs/project-memory/`.

This is authoritative exact PPMP v2 predecessor-format evidence, but it is **not a second external Project**. It is the canonical predecessor lineage of the Agnir repository itself.

## Target Agnir evidence

Current Agnir `main` independently defines and executable-tests Agnir Core `0.1` and `repository-filesystem/0.1`.

Current conformance demonstrates:

- target cold-start discovery without predecessor-private conversation state;
- Current State / Next Actions / Decisions / Evidence recovery;
- all named discovery failure classes;
- non-repository durable SQLite continuity;
- external-memory authorization;
- multi-project isolation;
- Locator Chain cycle / stale / inconsistency behavior;
- symlink and Git-worktree repository/filesystem boundaries.

Checkpoint head `7eff15bcbd126f389464b7c8f0f9540b5e15a1a7` passed Agnir conformance run `33149189235`.

## Migration-spec interpretation

`spec/MIGRATION_PPMP_V2.md` requires semantic migration rather than renaming. The real ZeroLocal predecessor audit supplies external real-world pressure for durable-knowledge preservation and explicit transition semantics. The canonical `legacy/ppmp-v2.0.0` branch supplies exact historical PPMP v2 format/source semantics.

A release decision must therefore avoid two incorrect claims:

- the ZeroLocal v1/RPM Project MUST NOT be relabeled as PPMP v2;
- the in-repository canonical PPMP v2 predecessor MUST NOT be called an external independent Project.

## Release-pressure conclusion

Agnir Core `0.1` should not make the existence of a second independently hosted historical PPMP v2 Project a semantic release prerequisite. Availability of such a Project is accidental historical evidence, not a property of the protocol.

The reproducible release requirement should instead be:

1. preserve the exact canonical PPMP v2 predecessor boundary;
2. add an explicit PPMP v2 -> Agnir migration conformance fixture derived from the canonical predecessor semantics;
3. retain at least one real non-fixture predecessor migration audit demonstrating material durable-knowledge comparison;
4. keep predecessor and target conformance classifications distinct.

The ZeroLocal audit satisfies item 3. The canonical legacy branch satisfies item 1. Item 2 remains the next executable migration task before final compatibility/release freeze.

## Classification

- Real external predecessor migration: **PASS, v1/RPM-era**.
- Exact PPMP v2 historical source: **AVAILABLE, canonical predecessor branch, not external**.
- Exact PPMP v2 -> Agnir executable migration fixture: **NOT YET COMPLETE**.
- Agnir Core `0.1` target conformance baseline: **PASS at current development head**.
