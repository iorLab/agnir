# Independent implementation challenge attempt 5 — issue #20

Date: 2026-09-05

## Source and artifact receipt

- challenge issue: `iorLab/agnir#20`;
- exact pinned source: `3face3590510948003f958ae16c929c3105a7687`;
- uploaded archive: `agnir-issue20-independent-challenge-3face359.zip`;
- archive SHA-256 independently recomputed: `645fe95cd38b87640980dfeeb1055a0ab102c9fa5736d605a3cb87ac8b34e04c`;
- archive contains 48 entries;
- ZIP integrity passed;
- bundled integrity manifest verified every recorded file byte count and SHA-256;
- bundled aggregate SHA-256 independently recomputed: `da3f96956708a4173a98c1957b3beed4b55d79eb529f9c7838b65d9f7e41dad3`.

## Independence and freeze discipline

The reviewer declared a fresh unpersonalized context and used issue #20 plus public material at the exact pinned source. Phase A and Phase B were frozen before reference inspection.

- Phase A aggregate: `08e1a63e6430cf94e5f268ed9f25bc78fd17437affb0e20bd40a2c48aecf6bbf`;
- Phase B aggregate: `72ed258e0018dea370b6108fc613c56f09d7251ab7144b5ce4257dd13d5bedfe`;
- post-reference revalidation reported all recorded Phase A/B files byte-for-byte unchanged.

## Phase B

Before freeze the independent implementation passed:

- 16/16 unit tests;
- 32/32 machine-readable recorded observations;
- direct schema/profile positive and negative fixture matrix;
- cold start/fresh resume;
- explicit discovery, identity, lineage, locator, external authorization and VCS-binding failures;
- checkpoint no-op/material/stale, preservation and lineage isolation;
- migration preservation/idempotence/stale-source pressure.

## Phase C findings

Final reviewer verdict: **`FAIL-DOCS`**.

The controlling product finding was behavior-material documentation under-specification for local `memory.evidence` in `repository-filesystem/0.2`:

- the published JSON Schema serialized `memory.evidence` as `string | null`;
- the normative profile showed a directory-shaped example but did not state that a non-null local Evidence locator MUST resolve to a directory;
- the reference resolver required a directory while the independent implementation reasonably accepted one regular file;
- therefore the same schema-valid locator string could be accepted by one implementation and rejected by another without a public normative rule deciding the result.

The review additionally noted that baseline flat-vs-recursive Evidence collection traversal was not explicitly fixed. This was not counted as a separate controlling defect because the file-vs-directory acceptance divergence was already decisive.

Two independent-implementation defects were also preserved:

1. explicit YAML `agnir.version: null` was classified as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; the public schema/profile and reference require malformed selected-profile serialization semantics, `AGNIR_DISCOVERY_INCONSISTENT`;
2. an authorized Core/profile 0.1→0.2 migration with an empty initial lineage identity was classified as `AGNIR_MIGRATION_CONFLICT`; public lineage-selection/migration semantics and both migration references require `AGNIR_LINEAGE_REQUIRED`-class behavior.

These implementation defects independently prevent PASS but do not change the controlling `FAIL-DOCS` classification.

No reference/conformance contradiction with an adequately specified public rule was identified.

## Public repair

The documentation omission was independently confirmed and repaired by PR `#21` without redesigning Core 0.2 semantics.

The repair:

- makes local target shapes explicit for stable `repository-filesystem/0.2` and compatibility `repository-filesystem/0.1`;
- requires non-null local State/Next Actions/Decisions to resolve to regular files and non-null local Evidence to resolve to a directory;
- defines baseline Evidence discovery as the regular-file children immediately contained by the declared Evidence directory; richer recursive/indexed behavior remains extension-defined;
- adds JSON Schema descriptions that separate serialized locator validation from filesystem target-shape semantics;
- adds conformance pressure for 0.1/0.2 Evidence-directory enforcement and flat 0.2 baseline discovery.

Accepted receipts:

- PR head: `871eb8f6a9ea19e29d45d590d2bb108a2f6af533`;
- PR conformance run `33917111455`: success;
- merged authoritative repair: `aa86b2653c0e6b1d183cce70c46b5b63a78a39be`;
- authoritative-main conformance run `33917149552`: success.

## Disposition

Issue #20 is closed as completed external evidence, not as a gate PASS.

The independent-implementation gate remains open. Acceptance requires another genuinely fresh reviewer against an exact post-checkpoint authoritative source. The next challenge should require systematic schema-derived boundary coverage and migration-lineage selection coverage before Phase B freeze, while still requiring the reviewer to derive expected behavior solely from the pinned public contract.
