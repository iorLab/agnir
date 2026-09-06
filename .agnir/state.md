# Agnir Current State

Agnir `v0.2.0` remains the published latest stable release and authoritative `main` remains a valid Core/profile `0.2` self-host. The deliberate Core/profile `1.0` stability-promotion machinery is now accepted on `main`; this does not itself relabel the authoritative Project or publish `v1.0.0`.

Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

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
- final verdict `PASS` with no concurrent documentation, conformance, or implementation failure class.

Evidence detail: `.agnir/evidence/2026-09-06-independent-implementation-challenge-acceptance.md`.

## Core/profile 1.0 promotion — accepted on main

Issue #27 / PR #28 completed the semantics-preserving promotion candidate.

Accepted receipts:

- final promotion-branch candidate: `dfc1af9203673cfc2aa41633143c4c90e274c976`;
- exact-head PR conformance run: `34020641603` success;
- squash merge to authoritative `main`: `0337be5c0ef5ccd74d207135646b30947c275776`;
- authoritative-main verification run: `34025528147` success;
- public 1.0 Core contract: `spec/AGNIR_CORE_1_0.md`;
- public 1.0 repository/filesystem profile: `profiles/REPOSITORY_FILESYSTEM_1_0.md`;
- exact 1.0 manifest schema: `schemas/agnir-manifest-1.0.schema.json`;
- explicit promotion boundary: `spec/CORE_0_2_TO_1_0_PROMOTION.md`;
- executable coverage includes Core 1.0 stability semantics, strict 1.0 discovery, explicit authorized/staged/stale-safe/idempotent 0.2→1.0 promotion, and composed 0.1→0.2→1.0 behavior;
- historical 0.1/0.2 normative contracts were not rewritten by the promotion PR.

The accepted model keeps a `1.0` distribution multi-version capable: unchanged supported `0.2` Projects remain `0.2`; a Project compatibility declaration changes to `1.0` only through explicit authorized promotion. The authoritative `main` self-host therefore remains Core/profile `0.2` until a distinct RC lineage intentionally performs that Project-owned promotion.

Evidence detail: `.agnir/evidence/2026-09-06-core-profile-1.0-promotion-acceptance.md`.

## v1 readiness — current

- Core semantics: **satisfied for promotion candidate**;
- compatibility/migration/promotion contracts: **satisfied for 0.1→0.2 and 0.2→1.0**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation: **satisfied** via Svif;
- VCS + non-VCS lineage evidence: **satisfied**;
- materially different real Projects: **satisfied (3)**;
- materially different execution surfaces/adapters: **satisfied (2)**;
- genuine mount-boundary evidence: **satisfied**;
- independent-implementation documentation/implementation quality: **satisfied by issue #26 clean PASS**;
- Core/profile `1.0` promotion candidate: **satisfied and reconciled to main**;
- repeatable release operations: **satisfied for 0.2; explicit 1.0 RC publication still required**;
- repository `v1.0.0-rc.1` cycle: **next active release stage**;
- stable `v1.0.0`: **blocked on a clean exact-source RC cycle**.

No accepted evidence has exposed a breaking Core/profile `0.2` semantic defect or a behavior-material divergence in the 1.0 promotion candidate. The immediate task is now to fork the explicit `release/v1.0.0-rc.1` lineage from the verified authoritative checkpoint, promote that release lineage's self-host declaration to Core/profile `1.0`, arm repository version/release metadata, run exact RC conformance, and only then publish the immutable prerelease.
