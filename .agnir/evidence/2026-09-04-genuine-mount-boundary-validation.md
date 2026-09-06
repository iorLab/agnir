# Genuine mount-boundary validation evidence

Date: 2026-09-04
Status: accepted external evidence

## Purpose

Close Agnir's v1 genuine mount-boundary evidence gap with real repository/filesystem behavior across a Linux container bind-mount boundary, rather than inferring mount behavior from ordinary same-filesystem paths.

This evidence pressures the existing `repository-filesystem/0.2` profile. It does **not** claim a new storage backend/profile and does **not** count Docker as another Agent execution surface.

## Captured authoritative source and isolated validation lineage

- authoritative Agnir `main` before the experiment: `4eb15a5c6df80983b1b799a9311ffc79a1d868d9`;
- authoritative tree: `3e96a01501cf050430f93f3b48c9b72143894a16`;
- stable Agnir package: `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- Project identity: `urn:agnir:project:agnir-core`;
- temporary validation branch: `validation/mount-boundary-v0.2.0`;
- validation lineage: `urn:agnir:lineage:mount-boundary-validation`;
- validation selector: `refs/heads/validation/mount-boundary-v0.2.0`;
- final validated branch head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`;
- final branch tree: `962b9ceb16e8a0e15c92f940a34415915d08bb5f`.

The validation lineage is evidence input only. It is not merged into authoritative `urn:agnir:lineage:authoritative` continuity.

## Test topology

The test ran on a GitHub-hosted Ubuntu 24.04 runner with Docker Engine 28.0.4 and `python:3.12-slim` containers. The runner checkout was the durable Project substrate.

### Container A — activation and checkpoint

The host checkout was bind-mounted read/write at:

`/workspace/project-a`

`/proc/self/mountinfo` recorded the real mount mapping from the host checkout to that container path. The repository's own `conformance/repository_filesystem_0_2_reference.py` resolved:

- Project identity `urn:agnir:project:agnir-core`;
- Core/profile `0.2` / `repository-filesystem/0.2`;
- logical lineage `urn:agnir:lineage:mount-boundary-validation`;
- State, Next Actions, Decisions, and Evidence from the mounted Project root.

Container A then wrote a unique temporary State marker and `.agnir/evidence/.mount-boundary-runtime-checkpoint.json` through the bind mount. A fresh resolver call in the same container observed both durable changes. Container A was then destroyed.

### Container B — fresh resume at a different mount path

A genuinely new container was started after A had been removed. The same host Project was bind-mounted read/write at a different in-container path:

`/mnt/agnir-project-b`

The resolver recovered the same Project identity and lineage from the new root and recovered Container A's State/Evidence checkpoint solely from Project-owned mounted continuity. The runtime receipt explicitly recorded:

- current Project root: `/mnt/agnir-project-b`;
- recovered checkpoint writer: `container-a`;
- recovered checkpoint root: `/workspace/project-a`.

Container B then wrote a second temporary resume marker and Evidence receipt, fresh-resolved both A and B markers, and was destroyed.

The host independently observed both persisted runtime Evidence files and State markers after the containers were gone.

## Negative-path evidence

### Read-only mount

The same Project was mounted at `/readonly/project:ro`. Discovery succeeded, proving the continuity remained readable, but checkpoint append failed at the filesystem boundary with:

- errno `30` (`EROFS`);
- `[Errno 30] Read-only file system: '/readonly/project/.agnir/state.md'`.

### Missing selected Project root

Discovery against `/selected/project-not-mounted` failed explicitly with:

`AGNIR_DISCOVERY_NOT_FOUND`

### Wrong/empty mounted Project root

An actual empty host directory was bind-mounted at `/wrong/project`. `/proc/self/mountinfo` confirmed the mount existed. Discovery still failed explicitly with:

`AGNIR_DISCOVERY_NOT_FOUND`

The resolver did not guess or walk to the valid sibling `/reference` Project.

## Workflow receipts

### Run 1 — semantic pass, harness cleanup defect

- staged head: `294b600267e8dcfa34e9387784b9ce3a8e3c8ccc`;
- workflow run: `33860211185`;
- job: `100982680413`;
- artifact id: `9931858846`;
- artifact digest: `sha256:bc74b1ab516a33054e149a9470c6cd78ccf36a83a206d0ac0d5637ba7ba72210`.

All mount-semantic positive and negative steps passed. The job failed only because the cleanup harness forgot to remove Python `conformance/__pycache__/` generated while importing the mounted reference implementation.

### Run 2 — semantic pass, root-owned cleanup defect

- head: `a4113c06579885bb8c360c46fa25e6e75d2cb947`;
- workflow run: `33860517098`;
- job: `100983650817`;
- artifact id: `9931920562`;
- artifact digest: `sha256:c6221b25534858b9f2042e0c812669943185ec8b9a8cd24d0c44d03be550d826`.

Again every mount-semantic step passed. Cleanup failed only because the containers ran as root and produced root-owned `.pyc` files that the host runner user could not delete. No Core/profile behavior was changed.

### Run 3 — accepted all-green run

- exact head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`;
- exact tree: `962b9ceb16e8a0e15c92f940a34415915d08bb5f`;
- workflow run: `33860631526`;
- job: `100984005488`;
- conclusion: **success**;
- artifact id: `9931961351`;
- artifact name: `agnir-mount-boundary-33860631526`;
- artifact digest: `sha256:2c7bb33c87e4de0e95542cfb12b3759ecdb005c6085962856bb4a2ad052b25ce`;
- artifact size: `3596` bytes.

Every step passed, including cleanup and final clean-worktree verification.

## Artifact external review

The final artifact was downloaded and inspected directly. It contains:

- `container-a.json` — actual mountinfo, identity/lineage/profile, A checkpoint marker;
- `container-b.json` — different mount path and recovered A checkpoint root;
- `runtime-checkpoint.json` and `runtime-resume.json` — durable cross-container checkpoint/resume receipts;
- `host.json` — host sees checkpoint and resume after A destruction/B resume;
- `read-only.json` — errno 30 checkpoint rejection;
- `missing-mount.json` and `wrong-mount.json` — `AGNIR_DISCOVERY_NOT_FOUND` receipts;
- `final-git-status.txt` — empty, proving runtime mutations and root-owned cache were cleaned after evidence capture.

The final receipt nonce is:

`33860631526-1-ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`

## Acceptance decision

This is accepted as **genuine mount-boundary evidence** for the current v1 readiness gate because it demonstrates, on a real mounted-volume boundary:

1. repository/filesystem activation and discovery through a bind-mounted Project root;
2. durable checkpoint persistence through the mount;
3. destruction of the first execution environment;
4. fresh resume in a new execution environment with the same Project mounted at a different absolute path;
5. stable Project identity and logical lineage independent of the container-local root path;
6. host visibility of the persisted checkpoint/resume state;
7. explicit read-only checkpoint failure;
8. explicit missing/wrong selected-root discovery failure without sibling guessing;
9. clean restoration of the validation worktree after runtime evidence capture.

This closes the current **real mount-boundary evidence** gate. It does not establish universal behavior for every possible network filesystem, FUSE implementation, Kubernetes volume, or other mount substrate; those remain optional future robustness evidence rather than the current v1 minimum gate.

No Agnir Core/profile `0.2` semantic defect was exposed. The next remaining external v1 evidence gate is independent-implementation documentation quality.
