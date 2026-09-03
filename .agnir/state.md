# Agnir Current State

Agnir `v0.2.0` is now the published stable repository release. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Stable publication — 2026-09-03

Immutable lightweight tag `v0.2.0` resolves directly to exact publication revision `fc84095ed5d500be9e1b43a4af0e93356571bbd4`.

GitHub Release id `381710267` was created for that tag with `draft=false` and `prerelease=false`. Publication/conformance workflow run `33711982062` succeeded: the full conformance job completed before the stable publication job received write permission.

Independent post-publication reads confirmed:

- `refs/tags/v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- Release id `381710267`, `draft=false`, `prerelease=false`;
- GitHub `releases/latest` -> `v0.2.0`.

The accepted RC tag `v0.2.0-rc.1` remains immutable at `50a8cd565954e7e8055b8b628e2d620ac7357bab`; stable publication did not move or repurpose it.

## Stable package provenance

The immutable operational-package baseline applied to construct the tagged stable candidate is `f59a83754346982170142a355a01c94050ddf3a5` (tree `2605d39fd355cd98939ac2862dcf56c2764ce29c`), verified by workflow `33711830312`.

`extensions.agnir/operations` records release `0.2.0` with that baseline as `applied_revision`. The tagged publication revision is a release receipt/tag target, not a self-referential package identity.

## Compatibility

Repository `v0.2.0` publishes stable Core `0.2` and stable `repository-filesystem/0.2`. The repository SemVer promotion from `0.2.0-rc.1` did not introduce another Core/profile compatibility change.

Core/profile `0.1` compatibility artifacts remain available for existing `v0.1.1` Projects and explicit `0.1` → `0.2` migration. Migration remains explicit; an ordinary compatible upgrade must not silently rewrite a Core/profile `0.1` Project into `0.2`.

## Release-line continuity

This moving release branch remains logical lineage `urn:agnir:lineage:v0.2.0`, separately bound to `refs/heads/release/v0.2.0`. The immutable stable tag stays at the exact publication revision even when this branch records later publication receipts.

Authoritative `main` is still a separate logical lineage. Published stable Project/package results and publication facts must now be reconciled back into main through staged target-first publication, preserving main lineage `urn:agnir:lineage:authoritative` and selector `refs/heads/main`.

`.agnir/next-actions.md` is the ordered resume plan.
