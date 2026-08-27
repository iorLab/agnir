# Agnir

Agnir is a project-owned durable continuity protocol.

It exists so a Project can be safely resumed when Executors, execution environments, storage implementations, or conversational contexts change. The Project owns the memory; execution surfaces do not.

## Active line

`main` implements the Agnir Core `0.1` development line. The released predecessor PPMP v2.0.0 / Persistent Project Memory / Sandminni line is preserved on `legacy/ppmp-v2.0.0` and is not silently relabeled as Agnir.

The active structure is:

```text
AGNIR.yaml                     # repository/filesystem discovery anchor
.agnir/                        # this Project's authoritative colocated continuity
spec/AGNIR_CORE.md             # Core 0.1 working specification
spec/AGNIR_DISCOVERY.md        # cold-start discovery contract
spec/MIGRATION_PPMP_V2.md      # explicit predecessor migration rules
profiles/REPOSITORY_FILESYSTEM.md
schemas/agnir-manifest.schema.json
conformance/                   # executable conformance pressure
history/PREDECESSOR.md         # locator to preserved predecessor lineage
```

Predecessor implementation/backend/adapter/site/template material is deliberately absent from active `main`; it remains available on the legacy branch.

`AGNIR.yaml` is a rule of the repository/filesystem profile, not Agnir Core. Core remains storage-, VCS-, platform-, host-, and execution-surface-neutral.

## Core memory semantics

Agnir requires durable recovery of Current State, Next Actions, Decisions, and Evidence / Checkpoints.

A fresh Executor given only an authorized Project Entry Point must be able to resolve the Project's Discovery Record and required durable state without replaying predecessor-private context.

## Cold start

For the repository/filesystem profile, cold start begins at the Project root and resolves top-level `AGNIR.yaml`. The manifest identifies the Agnir line, Project identity, and authoritative memory locators.

Run the active self-hosting check with:

```bash
python conformance/check_agnir_0_1.py
```

## Layer model

Agnir separates Core, Profiles, Implementations, Backends, and Adapters. Those lower layers are intentionally empty/minimal on the new main line until Agnir-native implementations are introduced and validated.

## Svif

Svif is a separate consuming protocol. Dependency direction is `Svif -> Agnir`: Svif may require a compatible Agnir Core version, but not a specific Agnir backend, adapter, or repository layout.
