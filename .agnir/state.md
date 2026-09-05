# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and v1 evidence baseline

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`; publication run `33711982062` success;
- authoritative lineage `urn:agnir:lineage:authoritative` is bound separately to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported compatibility/migration surfaces;
- real-Project minimum is satisfied by Svif, FishUp, and VocaPort;
- materially distinct execution-surface minimum is satisfied by the ChatGPT/GitHub-connected path plus accepted VocaPort DSH two-session evidence;
- genuine Linux Docker bind-mount boundary evidence is accepted, including fresh-remount resume, read-only `EROFS`, and explicit missing/wrong-root failures.

## Independent-implementation gate — open

The gate has produced preserved evidence across genuinely fresh sessions and has repeatedly improved the public contract/conformance. No clean frozen implementation `PASS` has yet been accepted.

Previous attempts remain preserved in their issues/Evidence: #15 `FAIL-IMPLEMENTATION`; #17 `FAIL-CONFORMANCE`; #19 `FAIL-IMPLEMENTATION`; #20 `FAIL-DOCS`; #22 `FAIL-CONFORMANCE`.

### #24 — `FAIL-DOCS` with concurrent `FAIL-CONFORMANCE`; migration boundary repaired

Pinned source `56892930c139f4d662b7c9aa9c0f33cc829a61fa`.

Preserved artifact receipts:

- uploaded ZIP SHA-256 `e9d7f135403093ea277fcc8f9704cfe8c73850c2a9ed20b79b7fa395be5f934a`;
- ZIP integrity passed with 55 entries;
- bundled content manifest verified 42 recorded files with no hash mismatch;
- Phase A freeze `75d1ef7882de2c83205cdd942b84f8fdb326afb5c4d8a46cb8c8c9c871cee1ee`;
- Phase B freeze `aca11730d7ad5726eaba84d1acdad016b5644207051f6b75d403cce8b3e9ce1d`;
- post-Phase-C revalidation preserved both freeze aggregates;
- direct pre-freeze boundary matrix 71/71 pass;
- all required semantic checkpoint/migration receipts pass.

Phase C exposed two material repository-side problems:

1. the stable 0.1→0.2 migration contract requires `AGNIR_UPGRADE_MIGRATION_REQUIRED` until migration is explicitly authorized, but the pinned Core and repository/filesystem references validated empty/whitespace initial-lineage input before the authorization gate;
2. the public migration contract did not define deterministic normalization for string-valued initial-lineage input, while the reference used implementation-specific `.strip()` behavior, allowing independent implementations to publish materially different authoritative lineage identities from the same input.

The frozen independent implementation had no controlling implementation defect. The singular verdict was `FAIL-DOCS`; the authorization-order reference contradiction was additionally classified `FAIL-CONFORMANCE`.

PR #25 repaired the published migration boundary without redesigning Core `0.2`:

- for an authoritative Core `0.1` source, explicit migration authorization precedes migration-only initial-lineage validation;
- string-valued initial-lineage input uses a published deterministic leading/trailing Unicode `White_Space` normalization set;
- the normalized identity is used for emptiness, persistence, idempotence, and conflict comparison;
- conformance now covers unauthorized+invalid-lineage precedence, Unicode whitespace normalization, whitespace-only rejection after authorization, and normalization-equivalent repeat no-op.

Repair receipts:

- PR head `e7d65d7de8e3c03e51c1034d645c247429c03c89`;
- PR run `33977471985` success;
- merged authoritative repair `f82d795a025e38ae6c33b51ef078bec819e766c7`;
- authoritative main run `33977552588` success.

Evidence detail: `.agnir/evidence/2026-09-06-independent-implementation-challenge-attempt-7.md`.

The independent-implementation gate remains **open**. The next acceptance evidence must come from another genuinely fresh reviewer against the exact post-checkpoint authoritative source. A clean `PASS` must contain a conforming frozen implementation and no unresolved behavior-material public/reference contradiction.

## v1 readiness — current

- Core semantics: **provisionally satisfied**; reopen only if fresh evidence exposes a real semantic defect;
- compatibility/migration contract: **satisfied for current published lines after #24 repair**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation: **satisfied** via Svif;
- VCS + non-VCS lineage evidence: **satisfied**;
- materially different real Projects: **satisfied (3)**;
- materially different execution surfaces/adapters: **satisfied (2)**;
- genuine mount-boundary evidence: **satisfied**;
- independent-implementation documentation/implementation quality: **open — one clean fresh PASS still required**;
- Core/profile `1.0` promotion: **future, after independent acceptance**;
- repository `1.0.0-rc` cycle: **future final release gate after deliberate 1.0 promotion**.

No accepted real-Project, execution-surface, mount, or external-review evidence has exposed a breaking Core/profile `0.2` semantic defect. Immediate external work is one fresh independent implementation against the repaired exact post-checkpoint source; if it passes, proceed to deliberate Core/profile `0.2` → `1.0` stability promotion and repository `1.0.0-rc` preparation.
