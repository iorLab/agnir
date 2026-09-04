# Independent implementation challenge attempt 4 — issue #19

Date: 2026-09-05

## Source and artifact receipt

- challenge issue: `iorLab/agnir#19`;
- exact pinned source: `7e844fe8bde08be8288dbf05393e5e03601ea4f0`;
- uploaded archive: `agnir_issue19_independent_implementation_challenge.zip`;
- archive SHA-256 independently recomputed: `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854`;
- ZIP integrity check passed (`testzip` returned no bad member);
- archive contains 62 entries;
- the bundled `COMPLETE_FILE_SHA256SUMS.txt` verified every covered deliverable successfully.

## Independence and freeze discipline

The reviewer declared a fresh unpersonalized context, used issue #19 plus public repository material at the exact pinned SHA, excluded prior Agnir challenge/issues/private context, did not use `.agnir/**` as product specification, and did not inspect `conformance/*_reference.py` before Phase C.

Phase A and Phase B were frozen with SHA-256 receipts before reference inspection; post-reference verification reported all frozen files unchanged.

## Phase A

The reviewer reconstructed the public Core/profile 0.2 contract and reported no behavior-material documentation ambiguity, conflict, or omission for the required minimal resolver/checkpoint path.

The reconstruction correctly identified:

- repository release, Core compatibility, and profile compatibility as distinct version layers;
- Project identity, logical Continuity Lineage, selector/binding, and revision receipt as distinct concepts;
- the published 0.2 JSON Schema as the normative serialized-shape constraint;
- missing `agnir.version` as `AGNIR_DISCOVERY_INCONSISTENT`;
- a present incompatible Core version as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- profile mismatch and other schema-invalid selected-profile serialization as `AGNIR_DISCOVERY_INCONSISTENT` absent a more-specific failure rule;
- required local locator failure/escape as `AGNIR_DISCOVERY_UNRESOLVABLE`;
- distinguishable external authorization denial as `AGNIR_DISCOVERY_UNAUTHORIZED`;
- no-op/material/stale checkpoint and fresh-resume semantics;
- explicit 0.1→0.2 migration, VCS selector/binding separation, and lineage-local integration semantics.

## Phase B

The independently authored implementation passed:

- 12/12 unit tests;
- 30/30 machine-readable receipt cases;
- direct schema/profile positive fixture acceptance;
- direct schema-derived negative fixture rejection;
- no-op/material/stale checkpoint tests;
- preservation and selected-lineage isolation;
- fresh-resume, explicit discovery failures, and adapter-simulated external authorization pressure.

## Phase C finding

Phase C exposed one material defect in the already-frozen independent resolver:

- explicit YAML `agnir.version: null` was classified as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- the public schema/profile make that a malformed schema-invalid serialization, therefore `AGNIR_DISCOVERY_INCONSISTENT` absent a more-specific rule;
- the pinned reference agrees: it only takes the unsupported-version branch for a non-null declared value, so explicit null falls through to schema validation and becomes `AGNIR_DISCOVERY_INCONSISTENT`.

The reviewer correctly left frozen Phase B unchanged after reference inspection.

Other observed differences — Evidence representation, backend receipt encoding, external locator adapter representation, and recommended VCS extension representation — were classified as non-normative implementation choices.

## Verdict and disposition

Final reviewer verdict: **`FAIL-IMPLEMENTATION`**.

This result does **not** identify a new public documentation defect or a reference/conformance contradiction. Documentation sufficiency, direct schema/profile cross-check, required receipts, freeze discipline, and reference alignment all passed this review; the only release-gate blocker is the frozen implementer's null-version dispatch defect.

The independent-implementation gate therefore remains **open**. The failed implementation is preserved as evidence but cannot be repaired retroactively for acceptance, and the reviewer cannot be reused after Phase C reference inspection.

The next acceptance attempt must use another genuinely fresh reviewer. To reduce repeated transcription/edge-case failures without supplying private answers, the next challenge should require a compact schema-derived negative mutation matrix before Phase B freeze, covering requiredness, explicit null/wrong type, const/enum mismatch, and forbidden additional properties where applicable. Expected outcomes must still be derived by the reviewer from the public pinned contract.
