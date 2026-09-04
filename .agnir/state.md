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

The gate has produced preserved external evidence across multiple genuinely fresh sessions. It has improved the public contract and conformance but has not yet produced one clean frozen implementation PASS.

### #15 — `FAIL-IMPLEMENTATION`

Pinned source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`; preserved archive SHA-256 `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`. Phase A understood the 0.2 serialization, but Phase B used incompatible shorthand fields. The review also exposed public drift that was repaired before the next clean attempt.

### #17 — `FAIL-CONFORMANCE`

Pinned source `5b73acf914e323ce337a0af295d5a9e96eaafdc8`; preserved archive SHA-256 `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`. Independent Phase B passed 21/21 scenarios, but Phase C showed the reference resolver did not enforce the published 0.2 JSON Schema. PR #18 aligned the reference with the normative schema; authoritative repair `a0b322d4e7f4e62e2ed77121b0a1b4e3b2328d1a`, main run `33907748617` success.

### #19 — `FAIL-IMPLEMENTATION`

Pinned source `7e844fe8bde08be8288dbf05393e5e03601ea4f0`; archive SHA-256 `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854`. Phase A found no behavior-material documentation ambiguity and Phase B passed 12/12 unit tests + 30/30 receipts, but a post-freeze `agnir.version: null` edge case was misclassified by the independent resolver. No new public contract/reference defect was identified in that attempt.

### #20 — `FAIL-DOCS`; Evidence locator shape repaired

Pinned source `3face3590510948003f958ae16c929c3105a7687`.

Preserved artifact receipts:

- uploaded ZIP SHA-256: `645fe95cd38b87640980dfeeb1055a0ab102c9fa5736d605a3cb87ac8b34e04c`;
- 48 entries; ZIP integrity passed;
- bundled integrity manifest verified every recorded file and aggregate SHA-256 `da3f96956708a4173a98c1957b3beed4b55d79eb529f9c7838b65d9f7e41dad3`;
- Phase A freeze `08e1a63e6430cf94e5f268ed9f25bc78fd17437affb0e20bd40a2c48aecf6bbf`;
- Phase B freeze `72ed258e0018dea370b6108fc613c56f09d7251ab7144b5ce4257dd13d5bedfe`;
- post-reference freeze revalidation passed;
- Phase B passed 16/16 unit tests and 32/32 recorded observations before freeze.

Phase C found one behavior-material public omission: `repository-filesystem/0.2` did not normatively state whether non-null local `memory.evidence` must resolve to a directory or could resolve to one regular file. The reference required a directory; the independent implementation accepted a file. Baseline flat-vs-recursive Evidence collection behavior was also not explicitly fixed.

Two separate independent-implementation defects were preserved: null Core-version dispatch and empty migration-lineage failure classification. They do not change the controlling `FAIL-DOCS` verdict.

PR #21 repaired the public omission as a compatibility clarification aligned with existing reference behavior:

- non-null local State/Next Actions/Decisions resolve to regular files;
- non-null local Evidence resolves to a directory;
- baseline Evidence discovery is flat over immediate regular-file children;
- richer recursive/indexed behavior is extension-defined;
- schema descriptions and conformance now pressure the target-shape rule.

Repair receipts:

- PR head `871eb8f6a9ea19e29d45d590d2bb108a2f6af533`;
- PR run `33917111455` success;
- merged repair `aa86b2653c0e6b1d183cce70c46b5b63a78a39be`;
- main run `33917149552` success.

Evidence detail: `.agnir/evidence/2026-09-05-independent-implementation-challenge-attempt-5.md`.

The independent-implementation gate remains **open**. The next acceptance evidence must come from another genuinely fresh reviewer against the exact post-checkpoint authoritative source. A clean PASS must include both a conforming frozen implementation and no unresolved behavior-material public/reference ambiguity.

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

No accepted real-Project, execution-surface, mount, or external-review evidence has exposed a breaking Core/profile `0.2` semantic defect. Immediate external work is one fresh independent implementation against the repaired exact source; if it passes, proceed to the deliberate Core/profile `0.2` → `1.0` stability promotion and repository `1.0.0-rc` preparation.
