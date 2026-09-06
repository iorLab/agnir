# Independent implementation challenge attempt 7 — Issue #24

## Scope

External independent-implementation acceptance attempt against exact source:

`iorLab/agnir@56892930c139f4d662b7c9aa9c0f33cc829a61fa`

Issue: `#24` — `v1 independent implementation challenge — clean acceptance run`.

The reviewer operated in a fresh unpersonalized context under the issue's Phase A → Phase B freeze → Phase C discipline. This evidence records the returned artifact and the maintainer-side reconciliation; it is not itself product specification.

## Artifact integrity

Uploaded archive: `agnir_issue24_independent_implementation_challenge.zip`.

- SHA-256: `e9d7f135403093ea277fcc8f9704cfe8c73850c2a9ed20b79b7fa395be5f934a`
- ZIP entries: 55
- ZIP integrity check: pass
- bundled content manifest: 42 recorded files; every recorded file hash verified
- Phase A aggregate freeze: `75d1ef7882de2c83205cdd942b84f8fdb326afb5c4d8a46cb8c8c9c871cee1ee`
- Phase B aggregate freeze: `aca11730d7ad5726eaba84d1acdad016b5644207051f6b75d403cce8b3e9ce1d`
- Phase A/B post-Phase-C revalidation: pass

## Frozen implementation pressure

- Direct pre-freeze boundary matrix: 71/71 pass.
- Required semantic receipts all pass, covering valid cold start/fresh resume, checkpoint no-op/material/stale conflict, preservation, lineage isolation, explicitly authorized migration, migration idempotence/conflicting repeat/stale source, and fresh 0.2 resume.
- No controlling independent-implementation defect was reported.

## Phase C findings

### C-01 — reference/conformance mismatch: migration authorization precedence

The stable public migration contract required an upgrade path encountering Core 0.1 while targeting Core 0.2 to surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` until migration is explicitly authorized.

The pinned Core and repository/filesystem migration references validated the requested initial-lineage string first. Therefore a valid Core 0.1 source with `authorized=false` and empty/whitespace initial-lineage input could return `AGNIR_LINEAGE_REQUIRED` before the compatibility-line authorization gate.

Maintainer review independently confirmed the contradiction.

### C-02 — public documentation omission: string-valued initial-lineage normalization

The public Core/profile/schema material required a durable non-empty lineage identity but did not specify whether explicit string-valued migration input was preserved exactly, trimmed, or otherwise canonicalized. The pinned reference used implementation-specific `.strip()` behavior.

This was behavior-material because two independent implementations could publish different authoritative logical lineage identities from the same Principal input and then disagree on idempotence/conflict semantics.

Maintainer review independently confirmed the omission.

## Verdict

Singular final verdict: **`FAIL-DOCS`**.

Concurrent failure class: **`FAIL-CONFORMANCE`** for C-01.

The gate remains open. This reviewer is not eligible as the next fresh reviewer after Phase C reference inspection.

## Repair

PR #25 — `fix: define migration lineage normalization and precedence`.

The repair:

1. gives the explicit 0.1→0.2 authorization gate precedence over migration-only target-lineage validation while the authoritative source remains Core 0.1;
2. defines migration-specific deterministic normalization for string-valued initial-lineage input by removing leading/trailing Unicode code points whose `White_Space` property is `Yes`, with the exact compatibility-line codepoint set published in `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
3. uses the normalized identity for emptiness, persistence, idempotence, and conflict comparison;
4. adds Core and repository/filesystem conformance pressure for unauthorized+invalid-lineage precedence, Unicode whitespace normalization, whitespace-only rejection after authorization, and normalization-equivalent repeated migration.

This repair intentionally does not redefine general Core 0.2 lineage identity representation.

## Repair receipts

- PR head: `e7d65d7de8e3c03e51c1034d645c247429c03c89`
- PR conformance run: `33977471985` — success
- merged authoritative repair: `f82d795a025e38ae6c33b51ef078bec819e766c7`
- authoritative main conformance run: `33977552588` — success

## Next acceptance condition

Create a new clean challenge only after the checkpoint carrying this evidence is green on authoritative `main`. Pin the new issue to that exact post-checkpoint revision. Acceptance still requires one genuinely fresh reviewer to produce a clean frozen `PASS` with no unresolved documentation, independent-implementation, or reference/conformance defect.
