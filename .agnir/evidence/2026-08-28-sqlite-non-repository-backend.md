# Non-repository SQLite backend evidence — 2026-08-28

## Claim

Agnir Core `0.1` continuity has executable evidence on a durable database-style backend that does not use the active repository/filesystem profile.

The fixture cold-starts from a SQLite Project Entry Point composed of:

- a durable database locator; and
- a durable project key.

It does **not** use `AGNIR.yaml`, `.agnir/`, a repository root, Git, or GitHub for discovery or continuity retrieval.

## Implementation

- Shared conformance Core failure semantics: `conformance/core_reference.py`, commit `ecad85a8618fa8774f6dd256378e37f97ff6266e`.
- Repository/filesystem reference refactored to share those semantics: commit `a0d2f85e5f17278dad5ef4c50480144fa2a5c6b4`.
- SQLite conformance-only backend: `conformance/sqlite_backend_reference.py`, commit `7c0c5dd82c6f74968c0d65c51c4194ccdaacaa26`.
- SQLite conformance tests: `conformance/test_sqlite_backend.py`, commit `08a0cb3f2707b3b5fcd7fdbf0b24a32f4fd0c7eb`.
- Self-host checker registers the non-repository fixtures since commit `cf260a1f864a47d2a08902c8c8db069b2cf9003b`.

## Scenario proven

The SQLite fixture:

1. stores the Discovery Record equivalent in a database `projects` table;
2. stores Current State, Next Actions, and Decisions in database memory rows;
3. stores Evidence independently in database evidence rows;
4. cold-starts from only the SQLite Project Entry Point and expected Project identity;
5. validates Agnir Core version and Project identity;
6. loads the required durable continuity semantics;
7. checkpoints updated state / next actions / decisions / evidence;
8. creates a fresh resolver and reloads the updated durable continuity;
9. proves the temporary fixture directory contains neither `AGNIR.yaml` nor `.agnir/`.

The suite also proves that the durable project key participates in discovery (`NOT_FOUND` for an unknown key) and that cross-Project identity mismatch remains `AGNIR_DISCOVERY_PROJECT_MISMATCH` without repository assumptions.

## Verification

GitHub Actions run `33143655399` for head `cf260a1f864a47d2a08902c8c8db069b2cf9003b` completed successfully.

Job `98759873676` (`repository-filesystem`) succeeded. Its `Negative discovery fixtures` step runs unittest discovery over all `conformance/test_*.py`, including `test_sqlite_backend.py`.

## Boundary

`conformance/sqlite_backend_reference.py` is conformance evidence, not a normative SQLite profile and not a production backend shipped by Agnir. Its purpose is to prove that the Core continuity contract survives a materially non-repository realization.
