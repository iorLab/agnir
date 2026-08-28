# Negative discovery conformance evidence — 2026-08-28

## Claim

Agnir `repository-filesystem/0.1` now has executable conformance pressure for the selected-root discovery boundary and key failure classes.

## Implementation

- Conformance-only repository/filesystem reference resolver: `conformance/repository_filesystem_reference.py`, introduced in commit `5a8c79959248f04f9c453afc8bc732b7e55a8af7`.
- Negative fixture suite: `conformance/test_repository_filesystem_failures.py`, introduced in commit `63cec0a2feda44fe6102e176afa5c99b444462e4`.
- Self-hosting checker refactored to use the same resolver in commit `6269ff4f01ad4b57c6406def87d037b2665324fe`.
- CI runs both self-host cold-start and negative fixtures since commit `02dd1662fadf5451acfcb26370d6f36ff0d4bc8e`.
- Selected-root / nested-project semantics clarified in `profiles/REPOSITORY_FILESYSTEM.md` by commit `2cbad2ad80e18bb674a88f5d91e1d51cc217cdbd`.
- Stale Svif terminology in `spec/AGNIR_CORE.md` corrected in commit `3645bce8940e2e4c3d4c811709852eb9f3dcf8fa`.

## Failure semantics exercised

The suite proves explicit semantic classification for:

- missing top-level Discovery Record -> `AGNIR_DISCOVERY_NOT_FOUND`;
- broken required Current State locator -> `AGNIR_DISCOVERY_UNRESOLVABLE`;
- unsupported Agnir Core version -> `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- Project identity mismatch -> `AGNIR_DISCOVERY_PROJECT_MISMATCH`;
- multiple unresolved candidate Project roots before root authority selection -> `AGNIR_DISCOVERY_AMBIGUOUS`.

## Nested Project boundary

Nested Projects are tested separately from ambiguity.

When parent and child directories each contain their own authoritative `AGNIR.yaml`, selecting the parent root resolves only parent continuity and selecting the child root resolves only child continuity. A mismatch at the selected child root surfaces `AGNIR_DISCOVERY_PROJECT_MISMATCH`; the resolver does not search the parent for a more convenient identity.

This matches the profile rule that the authorized Project Entry Point selects one Project root. `AMBIGUOUS` applies before that selection when multiple candidate roots exist and authority cannot determine one.

## Verification

GitHub Actions run `33143495855` for head `3645bce8940e2e4c3d4c811709852eb9f3dcf8fa` completed successfully.

Job `98759373389` (`repository-filesystem`) succeeded, including:

- `Self-hosting cold-start conformance` — success;
- `Negative discovery fixtures` — success.

## Boundary

`conformance/repository_filesystem_reference.py` is an executable conformance reference, not a promoted Agnir production implementation/backend. It exists to pressure-test normative discovery semantics without making repository/filesystem behavior part of Agnir Core.
