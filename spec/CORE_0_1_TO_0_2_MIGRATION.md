# Agnir Core 0.1 → 0.2 Migration

**Status:** Stable normative migration contract from published Core `0.1` to published Core `0.2`.

This contract governs the compatibility-line migration used by repository `v0.2.0` and later repository releases that explicitly support Core `0.1` → Core `0.2` migration. Core `0.1` remains a supported compatibility/regression surface for existing published `v0.1.1` Projects; Core `0.2` is the current published stable compatibility line.

## 1. Why migration is explicit

Core `0.2` changes the continuity model from one implicit Project-global continuity line to one or more explicitly identifiable Continuity Lineages. A Core `0.1` implementation is not required to understand lineage selection, lineage-local authority, or lineage integration.

Therefore Core `0.1` → `0.2` is a compatibility-line migration, not a compatible operational-package upgrade.

An upgrade path that encounters Core `0.1` while targeting Core `0.2` MUST surface semantics equivalent to `AGNIR_UPGRADE_MIGRATION_REQUIRED` until migration is explicitly authorized.

This authorization gate has precedence over validation of migration-only target choices. In particular, when the authoritative source is still Core `0.1`, an unauthorized request MUST surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` even if the requested initial-lineage input is absent, empty, or otherwise unusable. Lineage-selection validation becomes authoritative only after the compatibility-line migration has been explicitly authorized. This precedence does not apply to an already-migrated Core `0.2` Project being checked for idempotence or conflict.

## 2. Required preservation

A conforming migration MUST preserve:

- Project identity;
- Current State;
- Next Actions;
- Decisions when present;
- Evidence / Checkpoints when present;
- unrelated Project-owned content and policy not made invalid by the new compatibility line.

Migration MUST NOT fabricate a second Project merely to introduce lineage semantics.

## 3. Initial lineage

The existing Core `0.1` continuity line becomes exactly one initial Core `0.2` Continuity Lineage.

The migration mechanism MUST obtain a durable logical identity for that initial lineage from explicit Principal input or deterministic profile/backend policy. Core does not mandate the literal identity `main`, `default`, or any VCS-derived value.

For a **string-valued** initial-lineage input, this migration contract defines one normalization rule so independently written implementations cannot publish different identities from the same input: before testing for emptiness, persistence, idempotence, or conflict, implementations MUST remove all leading and trailing Unicode code points whose Unicode `White_Space` property is `Yes`. For this compatibility line that set is:

- U+0009–U+000D;
- U+0020;
- U+0085;
- U+00A0;
- U+1680;
- U+2000–U+200A;
- U+2028–U+2029;
- U+202F;
- U+205F;
- U+3000.

The resulting normalized string is the durable logical lineage identity used by the migration. A string that becomes empty after this normalization does not select an initial lineage and MUST fail with semantics equivalent to `AGNIR_LINEAGE_REQUIRED` after migration authorization has been established. A non-string identity representation used by another profile/backend MAY define an equivalent deterministic canonicalization policy appropriate to that representation, but it MUST still yield exactly one durable logical identity.

If no initial lineage identity can be selected deterministically, migration MUST fail rather than guess among backend siblings.

For a backend/profile that supports a default lineage, the migrated initial lineage SHOULD become the default unless explicit Project policy chooses another already-valid lineage.

## 4. Preservation is semantic, not layout-specific

Core `0.2` does not require the migration to rewrite every memory object or move every locator. A backend MAY preserve existing storage locations and add lineage-selection metadata around them, or materialize a new representation, provided the observable Core semantics are preserved and fresh Core `0.2` discovery resolves coherently.

This Core migration contract intentionally remains storage-neutral. `repository-filesystem/0.2` defines the concrete repository/filesystem discovery shape and executable repository conformance defines the corresponding staged publication pressure; other backends MAY realize the same migration semantics differently.

## 5. Idempotence

Repeating the same authorized migration after successful completion MUST be a no-op or otherwise return the already-migrated coherent result without duplicating lineages, changing Project identity, or rewriting continuity merely to record the repeat request.

If a repeated request attempts to reinterpret the already-migrated Core `0.1` continuity as a different initial lineage identity, the implementation MUST fail with migration-conflict semantics rather than silently rename/rebind the authoritative lineage.

For string-valued lineage input, idempotence/conflict comparison uses the normalized identity defined in §3. Inputs that differ only by the leading/trailing Unicode `White_Space` characters removed by that rule therefore identify the same migration target.

Recommended semantic class: `AGNIR_MIGRATION_CONFLICT`.

## 6. Cold-start verification

Migration is not complete until a fresh compatible Core `0.2` resolver can:

1. resolve the same Project identity;
2. select the migrated initial/default lineage from authorized context or declared default;
3. recover the preserved Current State and Next Actions;
4. recover Decisions and Evidence when required;
5. reject an explicitly selected nonexistent lineage rather than falling back;
6. resume without predecessor-private migration context.

## 7. Transactional publication

Migration changes the compatibility line and continuity-selection semantics. Implementations SHOULD construct a coherent migration candidate before changing authoritative discovery.

A completed migration MUST NOT expose a Core `0.2` Discovery Record whose selected lineage or continuity objects are not yet resolvable as one coherent generation.

Use atomic backend publication when available. Otherwise use generation/revision/pointer semantics sufficient to prevent a fresh resolver from accepting a partially migrated Project as completed Core `0.2` truth.

If authoritative Core `0.1` continuity changes after the migration candidate was constructed but before publication, migration MUST fail/re-resolve rather than overwrite the newer truth.

## 8. Conformance requirements

Conformance for this published migration line MUST demonstrate:

- unauthorized Core-line change remains `AGNIR_UPGRADE_MIGRATION_REQUIRED`, including when migration-only initial-lineage input is empty or unusable;
- authorized migration preserves Project identity and all required durable memory semantics;
- exactly one initial lineage is produced from the single Core `0.1` line;
- string-valued initial-lineage normalization follows §3, including whitespace-only rejection after authorization and deterministic equality for inputs that normalize to the same identity;
- fresh Core `0.2` resume succeeds via the initial/default lineage;
- repeated identical migration is a no-op;
- conflicting repeated lineage identity is rejected;
- source mutation/stale-base publication cannot silently overwrite newer Core `0.1` truth;
- no backend-specific branch concept is required by this Core migration contract.
