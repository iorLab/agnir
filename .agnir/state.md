# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and v1 evidence baseline

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- publication run `33711982062` success;
- authoritative lineage `urn:agnir:lineage:authoritative` is bound separately to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported compatibility/migration surfaces;
- real-Project minimum is satisfied by Svif, FishUp, and VocaPort;
- materially distinct execution-surface minimum is satisfied by the ChatGPT/GitHub-connected path plus the accepted VocaPort DSH two-session fresh activation/checkpoint/resume experiment;
- genuine Linux Docker bind-mount boundary evidence is accepted, including fresh remount resume, read-only `EROFS`, and explicit missing/wrong-root failure behavior.

## Independent-implementation gate — open

The gate has produced preserved external evidence across multiple genuinely fresh sessions. It has repeatedly improved public documentation/conformance but has not yet produced one clean frozen implementation `PASS`.

### #15 — `FAIL-IMPLEMENTATION`

Pinned source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`; archive SHA-256 `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`. Phase A understood the 0.2 serialization, but Phase B used incompatible shorthand fields. Public drift exposed in the review was repaired before the next clean attempt.

### #17 — `FAIL-CONFORMANCE`

Pinned source `5b73acf914e323ce337a0af295d5a9e96eaafdc8`; archive SHA-256 `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`. Independent Phase B passed 21/21 scenarios, but Phase C showed the reference resolver did not enforce the normative 0.2 JSON Schema. PR #18 aligned the reference; authoritative repair `a0b322d4e7f4e62e2ed77121b0a1b4e3b2328d1a`, main run `33907748617` success.

### #19 — `FAIL-IMPLEMENTATION`

Pinned source `7e844fe8bde08be8288dbf05393e5e03601ea4f0`; archive SHA-256 `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854`. Phase A found no behavior-material documentation ambiguity and Phase B passed 12/12 unit tests + 30/30 receipts, but the frozen resolver misclassified explicit null Core-version serialization. No repository-side defect was found in that attempt.

### #20 — `FAIL-DOCS`

Pinned source `3face3590510948003f958ae16c929c3105a7687`; archive SHA-256 `645fe95cd38b87640980dfeeb1055a0ab102c9fa5736d605a3cb87ac8b34e04c`. The public profile did not normatively fix non-null local Evidence target shape or baseline collection depth. PR #21 defined local State/Next Actions/non-null Decisions as regular files, non-null local Evidence as a directory, and baseline Evidence discovery as flat immediate regular-file children. PR run `33917111455` and authoritative main run `33917149552` succeeded.

### #22 — `FAIL-CONFORMANCE`; malformed-version reference repaired

Pinned source `4dae8b81b5c523110e84311d9d84469e868fc064`.

Preserved artifact receipts:

- uploaded ZIP SHA-256 `a2ca0598728dd15efcc43f17573af8a16ea7abba80f316da9b39eb36697a84dd`;
- ZIP integrity passed; 769 ZIP entries;
- bundled package manifest verified 441 regular-file hashes and 3 symlink records with no mismatch;
- Phase A freeze `f4e4fb7d478dee1df20353e125a2df2643610e7261354e273da435f1fa556837`;
- Phase B freeze `794b7af1bb4fbbdf667dcb921690065869f14ebe05ce2aaf05d3e71c63be5a85`;
- post-Phase-C revalidation preserved both freeze hashes;
- frozen boundary matrix 60/60 against its own frozen expectations, then 58/60 against the published contract after Phase C re-audit;
- semantic checkpoint/migration receipts 10/10 pass;
- independent post-freeze edge probes 7/7 pass.

Phase A reported no behavior-material documentation conflict. Phase C found a repository-side conformance mismatch: a wrong-container `agnir.version` was classified by the pinned reference as `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`, while the public profile/schema require malformed/non-string serialization to be `AGNIR_DISCOVERY_INCONSISTENT`. The independent frozen resolver separately misclassified both explicit null and wrong-container Core-version values, so the attempt also contained an implementation defect; the singular reported verdict remained `FAIL-CONFORMANCE` to preserve the repository-side contradiction.

PR #23 repaired the repository side without redesigning Core 0.2 semantics:

- only string-valued incompatible Core-version declarations take `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- missing/null/wrong-container version serialization is schema-invalid and `AGNIR_DISCOVERY_INCONSISTENT`;
- explicit null and wrong-container cases are now conformance-tested;
- local Evidence filesystem indirection may expose an in-root regular-file target, but must not read a canonical target outside the selected Project root without an authorized external Locator Chain.

Repair receipts:

- PR head `65f3b519dc7d522cf5118f9c2c4004171b4d49ea`;
- PR run `33969067170` success;
- merged authoritative repair `dde6ac366d6afb8a90bc59738451b9fc1b03df3f`;
- authoritative main run `33969102525` success.

Evidence detail: `.agnir/evidence/2026-09-05-independent-implementation-challenge-attempt-6.md`.

The independent-implementation gate remains **open**. The next acceptance evidence must come from another genuinely fresh reviewer against the exact post-checkpoint authoritative source. A clean `PASS` must contain a conforming frozen implementation and no unresolved behavior-material public/reference contradiction.

## v1 readiness — current

- Core semantics: **provisionally satisfied**; reopen only if fresh evidence exposes a real semantic defect;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation: **satisfied** via Svif;
- VCS + non-VCS lineage evidence: **satisfied**;
- materially different real Projects: **satisfied (3)**;
- materially different execution surfaces/adapters: **satisfied (2)**;
- genuine mount-boundary evidence: **satisfied**;
- independent-implementation documentation/implementation quality: **open — one clean fresh PASS still required**;
- Core/profile `1.0` promotion: **future, after independent acceptance**;
- repository `1.0.0-rc` cycle: **future final release gate after deliberate 1.0 promotion**.

No accepted real-Project, execution-surface, mount, or external-review evidence has exposed a breaking Core/profile `0.2` semantic defect. Immediate external work is one fresh independent implementation against the repaired exact source; if it passes, proceed to deliberate Core/profile `0.2` → `1.0` stability promotion and repository `1.0.0-rc` preparation.
