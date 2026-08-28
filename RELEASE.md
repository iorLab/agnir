# Agnir 0.1.0 Release

**Repository version:** `0.1.0`

**Core compatibility line:** `0.1`

**Repository/filesystem profile:** `repository-filesystem/0.1`

## Status

The current `main` is the Agnir `0.1.0` publication candidate. This document does not itself create a Git tag or GitHub Release.

Agnir `0.1` is a greenfield protocol line. Historical PPMP / PPM / Sandminni material under `history/` is lineage/reference material only and is not part of the active compatibility contract, conformance baseline, or release gate.

## Version model

Agnir separates three version layers:

- `agnir.version: "0.1"` identifies the Core compatibility line in a Discovery Record.
- `repository-filesystem/0.1` identifies the compatibility line of the repository/filesystem discovery profile.
- `VERSION` records the SemVer release of this reference specification/conformance repository.

Breaking Core semantics require a new Core compatibility line. Breaking repository/filesystem profile semantics require a new profile compatibility line after publication. Patch releases of the repository may clarify text, strengthen non-breaking conformance, or fix reference tooling without changing those compatibility identifiers.

The durable Agent-activation route was incorporated before the first `v0.1.0` publication. It therefore forms part of the initial `repository-filesystem/0.1` Agent-operable initialization contract rather than a post-publication compatibility change.

## Release scope

The `0.1.0` release includes:

- stable normative Core continuity semantics;
- normative discovery and failure semantics;
- `repository-filesystem/0.1` profile and manifest schema;
- Agent-operable repository initialization with durable activation via `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml`;
- prompt-free fresh-Agent activation pressure proving that an initialized Project does not depend on the initialization conversation;
- self-hosting cold-start validation;
- executable pressure for all named discovery failure classes;
- durable non-repository SQLite continuity pressure;
- external-memory authorization pressure without plaintext credentials;
- multi-project isolation pressure;
- Locator Chain cycle, stale, and inconsistency pressure;
- symlink and real Git worktree boundary pressure;
- bilingual README architecture/activation/continuity documentation;
- main-only branch governance and immutable historical indexing.

## Known limitation

Real mount-boundary behavior remains explicitly unproven because the current conformance environment does not provide a real mount-capable test case. Ordinary directories are not accepted as substitute evidence. This limitation does not alter the published Core `0.1` semantics.

Execution surfaces differ in whether they automatically inspect `AGENTS.md` or Project documentation. Agnir persists the activation route; a surface that ignores Project instruction files may require one-time surface configuration. Repeating an Agnir bootstrap prompt in every session is not part of the intended initialized-Project workflow.

## Publication gate

A publication commit is ready when all of the following hold:

1. `VERSION` is `0.1.0`;
2. `AGNIR.yaml`, schema, Core spec, discovery spec, profile, README files, and conformance baseline agree on the Core/profile compatibility lines;
3. root `AGENTS.md` points to the canonical README `Agnir Project Instructions` section, and that section contains the durable activation instructions required by the repository/filesystem profile;
4. the Agent activation conformance proves Project root → `AGENTS.md` → README instruction → `AGNIR.yaml` → durable memory without relying on a repeated user bootstrap prompt;
5. active protocol/profile files contain no dependency on retired predecessor branch refs or predecessor bootstrap layouts;
6. the full self-hosting and executable conformance suite passes on the publication commit;
7. `main` is the only live branch and historical branch tips remain indexed under `history/`;
8. known limitations are stated without being represented as proven.

Tagging `v0.1.0` or creating a GitHub Release is a separate publication action.
