# External-memory authorization evidence — 2026-08-28

## Claim

Agnir Core `0.1` now has executable conformance evidence that distinguishes an external Discovery Record that is absent from one that is known but authorization-gated, without transporting plaintext secret values through durable Project state or fixture payloads.

## Implementation

- External-memory conformance reference: `conformance/external_memory_reference.py`, commit `60a10aaa10f52ce7ab95bcdc2e5ba7983cc7dd0f`.
- Authorization fixture suite: `conformance/test_external_memory_authorization.py`, commit `82585c5b9d6fd38951392710baf238a55d1b237c`.
- Self-host checker registration: commit `775c8b0657c445514c52fd70ff5988d92ac8275d`.

## Semantics proven

The fixture models an external Project Entry Point that resolves a durable external Discovery Record containing:

- Agnir Core version;
- Project identity;
- external state / next-actions / decisions locators; and
- an authorization **reference** such as `credential-ref://vault/agnir/project-a`.

No token, password, secret value, or credential payload is stored in the Discovery Record.

Cases:

1. unknown external Discovery Record locator -> `AGNIR_DISCOVERY_NOT_FOUND`, with no authorization attempt;
2. known Discovery Record + authorization reference denied/unavailable -> `AGNIR_DISCOVERY_UNAUTHORIZED`;
3. known record + granted authorization reference -> continuity loads successfully;
4. granted authorization + missing declared Current State object -> `AGNIR_DISCOVERY_UNRESOLVABLE`, not `UNAUTHORIZED`;
5. Project identity mismatch remains independently classified by the shared Core failure semantics.

## Verification

GitHub Actions run `33143771320` for head `775c8b0657c445514c52fd70ff5988d92ac8275d` completed successfully.

Job `98760235526` succeeded. Its `Negative discovery fixtures` step runs unittest discovery over all `conformance/test_*.py`, including `test_external_memory_authorization.py`.

## Boundary

The external-memory registry and authorization callback are conformance fixtures only. The authorization callback receives the durable authorization reference; the protected credential value remains outside Agnir memory and outside this fixture model.
