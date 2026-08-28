# Agnir 0.1 Release Candidate

**Repository version:** `0.1.0-rc.1`

**Core compatibility line:** `0.1`

**Repository/filesystem profile:** `repository-filesystem/0.1`

## Status

The current `main` is release-candidate ready. This repository has not been tagged or published as a GitHub Release by this document alone.

Agnir `0.1` is a greenfield protocol line. Historical PPMP / PPM / Sandminni material under `history/` is lineage/reference material only and is not part of the active compatibility contract, conformance baseline, or release gate.

## Version model

Agnir separates three version layers:

- `agnir.version: "0.1"` identifies the Core compatibility line in a Discovery Record.
- `repository-filesystem/0.1` identifies the compatibility line of the repository/filesystem discovery profile.
- `VERSION` records the SemVer release of this reference specification/conformance repository.

Breaking Core semantics require a new Core compatibility line. Breaking repository/filesystem profile semantics require a new profile compatibility line. Patch releases of the repository may clarify text, strengthen non-breaking conformance, or fix reference tooling without changing those compatibility identifiers.

## Release scope

The `0.1.0-rc.1` candidate includes:

- normative Core continuity semantics;
- normative discovery and failure semantics;
- `repository-filesystem/0.1` profile and manifest schema;
- self-hosting cold-start validation;
- executable pressure for all named discovery failure classes;
- durable non-repository SQLite continuity pressure;
- external-memory authorization pressure without plaintext credentials;
- multi-project isolation pressure;
- Locator Chain cycle, stale, and inconsistency pressure;
- symlink and real Git worktree boundary pressure;
- bilingual README architecture/continuity documentation;
- main-only branch governance and immutable historical indexing.

## Known limitation

Real mount-boundary behavior remains explicitly unproven because the current conformance environment does not provide a real mount-capable test case. Ordinary directories are not accepted as substitute evidence. This limitation does not alter the published Core `0.1` semantics.

## Publication gate

A publication commit is ready when all of the following hold:

1. `VERSION` is the intended release version;
2. `AGNIR.yaml`, schema, Core spec, discovery spec, profile, README files, and conformance baseline agree on the Core/profile compatibility lines;
3. active protocol/profile files contain no dependency on retired predecessor branch refs or predecessor bootstrap layouts;
4. the full self-hosting and executable conformance suite passes on the publication commit;
5. `main` is the only live branch and historical branch tips remain indexed under `history/`;
6. known limitations are stated without being represented as proven.

Tagging or creating a GitHub Release is a separate publication action.
