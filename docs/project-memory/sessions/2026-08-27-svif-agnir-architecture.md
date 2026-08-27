# Agnir / Svif Architecture Checkpoint — 2026-08-27 21:30 +08:00

## Scope

This checkpoint captures the Agnir architecture transition and its versioned dependency boundary with Svif.

## Agnir state

- Agnir is the new umbrella project/protocol identity; PPMP v2, PPM, Sandminni, and RPM v1 remain explicit predecessor identities/evidence.
- Agnir begins a new version namespace with target line Agnir Core 0.1 rather than inheriting PPMP 2.x numbering.
- Layer model: Agnir Core -> Profiles -> Implementations -> Backends -> Adapters.
- Durable memory is project-owned, platform-neutral, storage-neutral, and executor-neutral.
- Neutral roles are Principal and Executor.
- Core continuity concepts are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Cold-start discovery uses Project Entry Point -> Discovery Record -> Locator Chain -> durable memory.
- The first repository/filesystem profile selects top-level `AGNIR.yaml` as its discovery anchor; `.agnir/` is optional recommended colocated storage and is not Core.
- Explicit predecessor, migration, and Agnir modes prevent silent promotion of PPMP v2 projects into Agnir claims.
- The repository currently self-hosts maintenance through PPMP v2 / PPM during migration; that remains predecessor implementation evidence, not Agnir conformance.

## Version-line preservation

The predecessor PPMP v2.0.0 / PPM / Sandminni line is preserved on branch `legacy/ppmp-v2.0.0`, pinned to commit `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`, the last pure predecessor commit before the Agnir transition began.

`main` is the active Agnir development line and may now evolve directly instead of preserving predecessor naming/layout in-place.

## Svif boundary

- Dependency direction is Svif -> Agnir.
- Svif depends on compatible Agnir Core protocol conformance, not an Agnir implementation/backend/adapter.
- Current draft target is Agnir Core 0.1; exact release compatibility remains unfrozen until Core/Discovery semantics stabilize.
- Agnir remains independently useful outside Svif and outside software-delivery workflows.

## Next work

1. Freeze `AGNIR.yaml` schema/versioning and repository/filesystem profile boundary.
2. Implement executable cold-start conformance from only a Project root.
3. Define a materially non-repository backend conformance fixture.
4. Define multi-project workspace isolation conformance.
5. Freeze the Agnir 0.1 release compatibility expression consumed by Svif.
6. Self-migrate this repository from PPMP/PPM predecessor mode only after those contracts are executable.
