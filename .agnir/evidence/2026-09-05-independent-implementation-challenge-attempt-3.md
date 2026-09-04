# Independent implementation challenge attempt 3 — issue #17

Date: 2026-09-05 (project local time)

## Exact challenge source

- public challenge: `iorLab/agnir#17`;
- exact pinned Agnir source: `5b73acf914e323ce337a0af295d5a9e96eaafdc8`;
- reviewer was instructed to use a fresh unpersonalized context, exclude prior challenge/private context, freeze Phase A and Phase B before reference inspection, and package all deliverables.

## Preserved archive

Principal supplied `agnir_issue17_independent_implementation.zip` back to the authoritative Agnir working conversation.

Independent local inspection of the supplied bytes:

- SHA-256: `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`;
- ZIP entries: 80;
- package includes frozen Phase A reconstruction/source classification/ambiguity log, independent implementation, tests, direct schema/profile fixtures, machine-readable receipts, freeze manifests, Phase C comparison, and final verdict.

## Phase A / Phase B result

The reviewer reconstructed the published repository-filesystem/0.2 serialization and machine-visible failure mapping before implementation.

Frozen Phase B independently implemented resolver/checkpoint behavior and recorded:

- 21/21 tests/scenarios PASS;
- schema-derived positive published 0.2 fixture accepted;
- schema-derived negative fixture with forbidden extra top-level shorthand rejected as `AGNIR_DISCOVERY_INCONSISTENT`;
- valid cold start/fresh resume;
- missing root/anchor, unsupported Core, profile mismatch, Project/lineage mismatch, local locator failure/escape, real external authorization distinction;
- no sibling fallback;
- unchanged checkpoint no-op;
- successful material checkpoint + fresh resume;
- stale-base rejection;
- unrelated-content preservation;
- selected-lineage isolation.

Phase A and Phase B freeze verification passed before Phase C reference inspection.

## Phase C verdict

Final reviewer verdict: **`FAIL-CONFORMANCE`**.

Material finding C-01: the pinned public schema has top-level `additionalProperties: false`, but `conformance/repository_filesystem_0_2_reference.py` used the older scalar parser, extracted only selected fields, and ignored forbidden additional/shorthand serialization. A schema-invalid manifest could therefore be accepted by the executable reference while an implementation honoring the published schema rejected it.

Secondary finding C-02: absent `agnir.version` was not explicitly separated from a present incompatible Core version in the profile text; the reference treated both as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`.

Other observed differences (Evidence physical representation, filesystem checkpoint sidecar/locking, external locator adapter syntax) were classified as non-normative implementation choices rather than Core/profile defects.

## Repair

PR `#18` repaired reference/schema conformance without changing the stable Core/profile 0.2 semantics:

1. `repository_filesystem_0_2_reference.py` now parses YAML and validates the exact repository `schemas/agnir-manifest-0.2.schema.json` using pinned conformance dependencies;
2. schema-invalid forbidden additional properties are rejected rather than ignored;
3. `profiles/REPOSITORY_FILESYSTEM_0_2.md` now explicitly says missing required `agnir.version` is `AGNIR_DISCOVERY_INCONSISTENT`, while a present declared value other than Core 0.2 is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
4. conformance adds direct positive optional-field and negative forbidden-extra-field cases plus missing-version and declared-mismatch cases;
5. `conformance/requirements.txt` pins `PyYAML==6.0.2` and `jsonschema==4.23.0`; CI installs them before the suite.

Receipts:

- repair PR head: `b753ad65548e81b30a7f0d189034284fde0f2002`;
- PR workflow run `33907695244`: success;
- merged main repair: `a0b322d4e7f4e62e2ed77121b0a1b4e3b2328d1a`;
- authoritative main workflow run `33907748617`: success.

## Gate disposition

The independent-implementation documentation gate remains **open** because issue #17 ended `FAIL-CONFORMANCE` even though its independent Phase B implementation was conforming.

Next acceptance evidence must use another genuinely fresh reviewer against the exact post-repair/post-checkpoint source. Prior #15/#17 reports, private design history, repair explanation, and reference implementation knowledge must not be supplied before that review's permitted Phase C boundary.
