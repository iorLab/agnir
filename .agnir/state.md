# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and v1 evidence baseline

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`; publication run `33711982062` success;
- authoritative lineage `urn:agnir:lineage:authoritative` remains bound separately to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported compatibility/migration surfaces;
- real-Project minimum is satisfied by Svif, FishUp, and VocaPort;
- materially distinct execution-surface minimum is satisfied by the ChatGPT/GitHub-connected path plus accepted VocaPort DSH two-session evidence;
- genuine Linux Docker bind-mount boundary evidence is accepted, including fresh-remount resume, read-only `EROFS`, and explicit missing/wrong-root failures.

## Independent-implementation gate — satisfied

Issue #26 produced the first clean frozen independent-implementation `PASS` against exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`.

Accepted receipts:

- uploaded ZIP SHA-256 `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`;
- payload manifest: 481 entries, aggregate `04e87857dcf22e5c5ea8fa8d3493523f8b009e8efc7ff3915a6ee371644a5d86`;
- Phase A freeze `1b422ad2ce17ed046baf488a180fe288f0a6d6599e642a5f3403d74d8d46eb56`;
- Phase B freeze `6d75402a99795eddd1781a8e075584834995868becb9ae8fb7a74a5b20b86cde`;
- direct boundary matrix **81/81 pass**;
- focused independent pytest **10/10 pass**;
- required semantic receipts **19/19 pass**;
- Phase C independent edge probes **10/10 pass**;
- post-Phase-C freeze revalidation reproduced both frozen aggregates exactly;
- final verdict `PASS`; `FAIL-DOCS`, `FAIL-CONFORMANCE`, and `FAIL-IMPLEMENTATION` all absent.

The reviewer reconstructed the public contract without private Agnir design history, independently implemented the required Core/profile surface before reference inspection, and found no unresolved behavior-material public or reference contradiction. Gate 9 of `V1_RELEASE_CRITERIA.md` is therefore satisfied. No further independent challenge rerun is required unless later changes reopen the contract or expose a material defect.

Evidence detail: `.agnir/evidence/2026-09-06-independent-implementation-challenge-acceptance.md`.

Earlier failed attempts remain preserved as useful evidence: #15 `FAIL-IMPLEMENTATION`; #17 `FAIL-CONFORMANCE`; #19 `FAIL-IMPLEMENTATION`; #20 `FAIL-DOCS`; #22 `FAIL-CONFORMANCE`; #24 `FAIL-DOCS` with concurrent `FAIL-CONFORMANCE`.

## v1 readiness — current

- Core semantics: **provisionally satisfied**;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation: **satisfied** via Svif;
- VCS + non-VCS lineage evidence: **satisfied**;
- materially different real Projects: **satisfied (3)**;
- materially different execution surfaces/adapters: **satisfied (2)**;
- genuine mount-boundary evidence: **satisfied**;
- independent-implementation documentation/implementation quality: **satisfied by issue #26 clean PASS**;
- repeatable release operations: **satisfied for 0.2; explicit 1.0 RC cycle still required**;
- Core/profile `1.0` promotion: **next active release stage**;
- repository `1.0.0-rc` cycle: **final release stage after deliberate 1.0 promotion**.

No accepted evidence has exposed a breaking Core/profile `0.2` semantic defect. The immediate task is no longer external review. It is to define a deliberate Core/profile `0.2` → `1.0` stability-promotion candidate that preserves the proven semantics, keeps historical `0.2` contracts immutable, specifies the exact promotion/migration compatibility mechanics, and then enters an explicit `1.0.0-rc` verification cycle.
