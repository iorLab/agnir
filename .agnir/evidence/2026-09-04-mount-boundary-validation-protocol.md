# Genuine mount-boundary validation protocol

Date: 2026-09-04
Status: staged

## Purpose

Close the remaining Agnir v1 mount-boundary evidence gap using a real Linux Docker bind mount on a GitHub-hosted Ubuntu runner. This is intentionally stronger than ordinary path relocation: the Project crosses a container mount namespace and is re-mounted at different in-container paths across two destroyed/recreated execution environments.

## Captured source

- authoritative Agnir main before the experiment: `4eb15a5c6df80983b1b799a9311ffc79a1d868d9`;
- stable Agnir package: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- Project identity: `urn:agnir:project:agnir-core`;
- validation lineage: `urn:agnir:lineage:mount-boundary-validation`;
- validation selector: `refs/heads/validation/mount-boundary-v0.2.0`.

## Positive path

### Container A

The runner checkout is bind-mounted read/write into Container A at `/workspace/project-a`.

Container A must:

- prove `/workspace/project-a` is an actual mount point from `/proc/self/mountinfo`;
- invoke the repository's published `repository_filesystem_0_2_reference` against the mounted root;
- recover the expected Project identity, Core/profile, lineage, State, Next Actions, Decisions, and Evidence;
- append a unique runtime marker to `.agnir/state.md` and create a temporary Evidence checkpoint under `.agnir/evidence/`;
- fresh-resolve within A and prove the marker/checkpoint are now part of Project-owned continuity.

Container A is then destroyed.

### Container B

The same host Project is bind-mounted read/write into a new Container B at `/mnt/agnir-project-b`.

Container B must:

- prove that path is an actual mount point;
- start with no A process/environment state;
- invoke the same repository-owned resolver from the new mounted root;
- recover the same Project identity and validation lineage;
- recover A's State marker and Evidence checkpoint solely from mounted Project state;
- write a second temporary resume Evidence receipt.

Container B is then destroyed. The host must independently observe the same checkpoint/resume files and State marker.

## Negative paths

1. **Read-only mount:** the resolver may read continuity, but a checkpoint write through a `:ro` Project mount must fail at the filesystem boundary.
2. **Missing Project mount:** using the reference implementation with a selected root that is not mounted and does not contain `AGNIR.yaml` must produce `AGNIR_DISCOVERY_NOT_FOUND`.
3. **Wrong/empty Project mount:** bind-mounting an empty host directory as the selected Project root must likewise produce `AGNIR_DISCOVERY_NOT_FOUND`; the implementation must not guess another sibling/root.

## Cleanup and receipts

Runtime State/Evidence mutations are test data only. Before job completion the host must copy exact runtime receipts to an Actions artifact, restore `.agnir/state.md`, remove temporary Evidence files, and prove the Git worktree is clean.

The artifact should include Container A/B discovery receipts, mountinfo excerpts, negative-path receipts, and host verification data. External review must inspect the workflow run and artifact before authoritative Agnir continuity may mark the mount-boundary gate satisfied.

## Non-claims

- This does not create a new storage backend/profile; it pressures the existing repository/filesystem profile across a genuine mount boundary.
- Docker itself is not counted as a third Agent execution surface.
- This validation lineage is not authoritative Agnir target truth and must not be merged into `main`.
