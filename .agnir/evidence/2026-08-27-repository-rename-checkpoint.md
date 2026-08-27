# Checkpoint — 2026-08-27 repository identity transition

## Scope

Durable checkpoint after the first direct Agnir Core 0.1 main-line implementation and before coordinated GitHub repository renaming.

## Source boundary

- Project: Agnir
- Repository at checkpoint entry: `mattamior/rpm`
- Branch: `main`
- Pre-checkpoint head: `6537fe56157d2673c0ddc8b205919c73fdda117e`
- Pre-checkpoint verification: Agnir conformance workflow run `33081100118` completed successfully.
- Predecessor boundary: `legacy/ppmp-v2.0.0`; the branch remains authoritative predecessor history and is not to be renamed.

## Durable result

- Agnir Core 0.1, repository/filesystem discovery profile, `AGNIR.yaml`, `.agnir/` continuity, schema, and executable conformance are the active `main` structure.
- Agnir remains Project-owned durable continuity independent of ChatGPT, GitHub, Git, Svif, or any specific storage/backend realization.
- The repository-rename decision has changed from deferred cleanup to immediate next execution work.
- Planned rename order is Agnir first, Svif second, Cloudflare starter third.
- Planned names are `mattamior/agnir`, `iorLab/svif`, and `iorLab/svif-cloudflare-starter`.
- Legacy branch names remain unchanged to preserve predecessor identity.

## Resume point

1. Rename `mattamior/rpm` to `mattamior/agnir` and immediately update durable repository references.
2. Reconcile Svif's dependency/cross-project references once `iorLab/zerolocal` becomes `iorLab/svif`.
3. Verify Agnir conformance after the identity transition.
4. Continue negative cold-start fixtures, non-repository backend evidence, external-memory authorization, and multi-project isolation.
5. Keep Svif coupling at the Agnir protocol boundary only.

The Git commit containing this record is the checkpoint commit; its immutable commit identity is resolved from repository history rather than recursively embedded in this file.
