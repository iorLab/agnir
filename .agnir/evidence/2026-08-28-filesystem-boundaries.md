# Repository/filesystem boundary evidence — 2026-08-28

## Claim

Agnir `repository-filesystem/0.1` now has executable boundary pressure for symlinked Project Entry Points, relative-locator symlink escape, and real Git worktree cold start.

## Implementation

- Boundary fixture suite: `conformance/test_repository_filesystem_boundaries.py`, introduced in commit `bcd774427364191c39fba05c1aed1939d26a3d3d`.
- Self-host checker registration: `3605b87f0e14c372bc76fcf36a825c678bdd52b3`.
- Profile clarification: `43185baefeab6a608ab27c1b793f36bd57d2ad7f`.
- Worktree fixture corrected to persist real Evidence content in commit `b8468c93783c00473f79e25358bbe3072d101678`.

## Semantics proven

1. An authorized filesystem indirection that resolves to exactly one selected Project root can be canonicalized; a symlink Project Entry Point successfully cold-starts the target Project.
2. A relative memory locator that reaches outside the selected Project root through a symlink does not become an implicitly authorized external Locator Chain; it fails as `AGNIR_DISCOVERY_UNRESOLVABLE`.
3. A real Git worktree whose `.git` is a worktree metadata file (not a repository directory) cold-starts from its own top-level `AGNIR.yaml` and declared continuity locators.
4. Evidence declared by the Discovery Record must actually survive the substrate. The first worktree fixture failed because Git does not track empty directories; the fix added real evidence content rather than weakening discovery semantics.

## Verification

The first boundary run `33144160874` failed specifically in the Git worktree case because `.agnir/evidence/` was empty in the source repository and therefore absent from the created worktree. The resolver correctly surfaced `AGNIR_DISCOVERY_UNRESOLVABLE`.

After the fixture was corrected, GitHub Actions run `33144199717` for head `b8468c93783c00473f79e25358bbe3072d101678` succeeded.

Job `98761550583` succeeded, including the unittest discovery step that runs all three repository/filesystem boundary tests.

## Boundary

A real mount-boundary case is **not** proven by this evidence. It should be tested only in an environment that can create/use a real mount boundary. An ordinary directory must not be presented as mount conformance evidence.
