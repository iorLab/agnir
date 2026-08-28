# Locator Chain failure evidence — 2026-08-28

## Claim

Agnir Core `0.1` now has executable substrate-neutral conformance fixtures for `AGNIR_DISCOVERY_CYCLE`, `AGNIR_DISCOVERY_STALE`, and materially `AGNIR_DISCOVERY_INCONSISTENT` Locator Chain semantics.

## Implementation

- Generic Locator Chain conformance reference: `conformance/locator_chain_reference.py`, commit `27807c43c0629eb59f4c2190852b3de16bea0a44`.
- Failure fixtures: `conformance/test_locator_chain_failures.py`, commit `11fcf95befdec22b3154029b199518e5956d54bf`.
- Self-host checker registration: commit `58e3108b5e6ec93cb100aeabd72e01a8374f7206`.

## Semantics proven

- A Locator Chain that revisits a previously resolved locator fails as `AGNIR_DISCOVERY_CYCLE`; it is not allowed to fabricate a terminal continuity state.
- A record explicitly known to be superseded or non-authoritative fails as `AGNIR_DISCOVERY_STALE` even when durable objects still physically exist.
- A chain hop that simultaneously claims another Discovery Record and terminal memory is materially contradictory and fails as `AGNIR_DISCOVERY_INCONSISTENT`.
- Current State and Next Actions resolved from different checkpoint generations fail as `AGNIR_DISCOVERY_INCONSISTENT`; an implementation must not splice them into an apparently coherent Project truth.
- A consistent multi-hop chain with matching Project identity and checkpoint generation resolves successfully.

## Verification

GitHub Actions run `33144042330` for head `58e3108b5e6ec93cb100aeabd72e01a8374f7206` completed its `repository-filesystem` job successfully.

Job `98761070215` succeeded, including the unittest discovery step that runs `conformance/test_locator_chain_failures.py`.

## Boundary

The Locator Chain registry is an abstract conformance substrate only. It does not define a storage profile, URI scheme, database model, or production Agnir implementation.
