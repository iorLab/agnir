# Agnir Current State

Agnir `v0.2.0` remains the published stable line. This temporary branch exists only to validate genuine mount-boundary behavior; authoritative Agnir `main` is captured at `4eb15a5c6df80983b1b799a9311ffc79a1d868d9` and must not be advanced by this experiment.

## Validation binding

- Project identity: `urn:agnir:project:agnir-core`.
- Core/profile: `0.2` / `repository-filesystem/0.2`.
- Validation logical lineage: `urn:agnir:lineage:mount-boundary-validation`.
- Validation selector: `refs/heads/validation/mount-boundary-v0.2.0`.
- Authoritative lineage remains `urn:agnir:lineage:authoritative` on `refs/heads/main`; validation continuity is evidence input only and MUST NOT be merged into main as target truth.

## Experiment goal

Prove that repository/filesystem discovery and durable continuity survive a real Linux container bind-mount boundary rather than only an ordinary same-filesystem path change.

The validation workflow must:

1. checkout this exact validation branch on a GitHub-hosted Ubuntu runner;
2. start Container A with the Project bind-mounted read/write at one container path;
3. activate/discover Project identity, lineage, State, Next Actions, Decisions, and Evidence through the mounted Project root;
4. persist a temporary Project-owned State marker plus Evidence checkpoint through that mount;
5. destroy Container A;
6. start fresh Container B with the same host Project mounted at a different container path, with no process/environment memory from A;
7. fresh-resolve continuity and recover A's checkpoint solely from mounted Project state, then write a resume receipt;
8. prove read-only checkpoint rejection and explicit missing/wrong-mount discovery failure;
9. verify the host sees the same persisted checkpoint, capture receipts, and restore the validation worktree to its committed clean state.

## Safety boundary

- Do not publish this validation lineage to authoritative `main`.
- Do not change Core/profile semantics to make the test pass.
- Runtime checkpoint markers are temporary workflow data and must be cleaned before the job completes.
- Acceptance is an external Agnir evidence decision after exact workflow/Git receipts are reviewed.
