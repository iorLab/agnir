# Independent implementation challenge attempt 6 — issue #22

Date: 2026-09-05

## Source and artifact receipt

- challenge issue: `iorLab/agnir#22`;
- exact pinned source: `4dae8b81b5c523110e84311d9d84469e868fc064`;
- uploaded archive: `agnir_issue22_independent_implementation_challenge.zip`;
- archive SHA-256 independently recomputed: `a2ca0598728dd15efcc43f17573af8a16ea7abba80f316da9b39eb36697a84dd`;
- ZIP integrity check passed (`testzip` returned no bad member);
- archive contains 769 ZIP entries;
- bundled `PACKAGE_CONTENTS_SHA256.txt` verified 441 regular-file hashes and 3 symlink records with no mismatch.

## Independence and freeze discipline

The reviewer declared a fresh unpersonalized Temporary Chat context, used only issue #22 plus public repository material at the exact pinned SHA, excluded prior Agnir challenges/issues/PRs/private context, did not use `.agnir/**` or `history/**` as product specification, and did not inspect `conformance/*_reference.py` before Phase C.

Freeze receipts:

- Phase A aggregate SHA-256: `f4e4fb7d478dee1df20353e125a2df2643610e7261354e273da435f1fa556837`;
- Phase B aggregate SHA-256: `794b7af1bb4fbbdf667dcb921690065869f14ebe05ce2aaf05d3e71c63be5a85`;
- post-Phase-C revalidation reproduced both hashes exactly;
- no Phase B bytecode cache was introduced.

## Phase A

The frozen reconstruction covered all required contract areas and reported no behavior-material public documentation conflict. It logged only intentional/non-material latitude around exact no-lineage migration failure code, backend checkpoint receipt/atomicity mechanism, and external locator adapter syntax.

The public 0.2 profile/schema was sufficient to determine that malformed Core-version serialization — including explicit null or wrong scalar/container type — is schema-invalid and `AGNIR_DISCOVERY_INCONSISTENT`, while a string-valued actually declared incompatible Core version is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`.

## Phase B

The independently authored resolver/checkpoint/migration path reported before freeze:

- boundary matrix 60/60 PASS against its frozen expectations;
- semantic checkpoint/migration receipts 10/10 PASS;
- checkpoint no-op, coherent material publication, stale-base conflict, fresh resolve, preservation, lineage isolation, explicit migration, repeat/idempotence/conflict, stale-source rejection, external authorization simulation, locator boundaries, and Evidence flat collection were exercised.

Phase C later re-audited the immutable boundary matrix against the public contract and found it was actually 58/60: `version_null` and `version_list` had incorrect frozen expectations/behavior.

## Phase C findings

### C-01 — explicit null Core version

- public contract: `AGNIR_DISCOVERY_INCONSISTENT`;
- frozen independent implementation: `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- pinned reference: `AGNIR_DISCOVERY_INCONSISTENT`;
- classification: independent reconstruction/implementation defect.

### C-02 — wrong-container Core version

- public contract: `AGNIR_DISCOVERY_INCONSISTENT`;
- frozen independent implementation: `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- pinned reference: `AGNIR_DISCOVERY_UNSUPPORTED_VERSION` because it performed a generic non-null/not-equal dispatch before schema validation;
- classification: independent implementation defect **and** reference/conformance mismatch with the published contract.

The reviewer reported the singular final verdict as **`FAIL-CONFORMANCE`** to preserve the repository-side contradiction while explicitly retaining the concurrent implementation defect. Issue #22 provided no precedence rule for simultaneous failure classes.

The independent post-freeze edge probe set passed 7/7. Other differences were classified as non-normative implementation choices. One observed Evidence-child symlink divergence was not used for the verdict; the independent implementation conservatively rejected an escaping canonical target while the reference could follow it.

## Repository repair

PR #23 repaired the repository-side finding and hardened the observed Evidence indirection boundary without redesigning Core 0.2:

- unsupported-version dispatch now requires a string-valued incompatible Core-version declaration;
- explicit null and wrong-container values fall through to normative schema validation and become `AGNIR_DISCOVERY_INCONSISTENT`;
- conformance includes explicit null and wrong-container Core-version cases;
- the stable profile makes that string-vs-malformed distinction explicit;
- baseline local Evidence indirection may resolve to an in-root regular file but must not read a canonical target outside the selected Project root without an authorized external Locator Chain;
- conformance covers both in-root Evidence symlink resolution and out-of-root rejection.

Receipts:

- PR #23 head: `65f3b519dc7d522cf5118f9c2c4004171b4d49ea`;
- PR conformance run: `33969067170` success;
- merged authoritative repair: `dde6ac366d6afb8a90bc59738451b9fc1b03df3f`;
- authoritative main conformance run: `33969102525` success.

## Verdict and disposition

Challenge #22 is a completed **`FAIL-CONFORMANCE`** attempt and does not close the independent-implementation gate. Its archive, freeze receipts, successful dimensions, independent implementation defects, and repository-side conformance defect are preserved as evidence.

Because the reviewer inspected reference code in Phase C, that session cannot be reused for acceptance. The next attempt must use another genuinely fresh reviewer against the exact post-checkpoint authoritative source. A clean `PASS` is still required before Core/profile `1.0` promotion and the repository `1.0.0-rc` cycle.
