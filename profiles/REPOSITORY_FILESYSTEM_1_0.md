# Agnir Repository/Filesystem Profile 1.0

**Profile identifier:** `repository-filesystem/1.0`  
**Core compatibility:** Agnir Core `1.0`  
**Status:** Candidate stable normative profile for the Agnir `1.0.0` release line.

## 1. Stability-promotion rule

`repository-filesystem/1.0` is the stable 1.0 promotion of the accepted `repository-filesystem/0.2` profile.

Except for the compatibility identifiers changing from Core/profile `0.2` to `1.0`, the schema filename/identifier changing to the 1.0 schema, and the explicit promotion rules in this document, the normative behavior of `profiles/REPOSITORY_FILESYSTEM_0_2.md` §§1–10 and §12 is incorporated into this profile **without behavioral change**.

That incorporated behavior includes:

- one authorized selected Project root with top-level `AGNIR.yaml`;
- no arbitrary parent/sibling guessing;
- one explicit logical `continuity.lineage` per selected root;
- State/Next Actions/non-null Decisions resolving to regular files;
- non-null Evidence resolving to a directory;
- flat baseline Evidence discovery of immediate regular-file children;
- local canonical-target authority remaining inside the selected Project root unless an authorized external Locator Chain is explicitly used;
- the accepted machine-visible failure mapping;
- lineage-local checkpoint publication;
- VCS selector/binding separation from logical lineage identity;
- fork/rebind/delete-recreate/integration semantics;
- staged reconciliation and coherent target publication.

A `repository-filesystem/1.0` implementation MUST NOT introduce a behavioral difference from those incorporated `0.2` rules unless a later compatible `1.x` profile contract explicitly defines it.

## 2. Discovery anchor and serialized shape

The selected Project root contains top-level `AGNIR.yaml` declaring:

```yaml
agnir:
  version: "1.0"
  discovery_profile: "repository-filesystem/1.0"

project:
  identity: "urn:example:project:p"

continuity:
  lineage: "urn:example:lineage:l1"

memory:
  state: ".agnir/state.md"
  next_actions: ".agnir/next-actions.md"
  decisions: ".agnir/decisions.md"
  evidence: ".agnir/evidence/"
```

`schemas/agnir-manifest-1.0.schema.json` is the normative serialized-shape constraint for this profile.

A selected `repository-filesystem/1.0` manifest MUST satisfy that schema. Forbidden additional properties, missing required properties, wrong scalar/container types, invalid extension names, and other schema violations MUST NOT be silently ignored.

## 3. Required discovery-failure mapping

The accepted `repository-filesystem/0.2` failure precedence is retained under the `1.0` identifiers:

- missing top-level `AGNIR.yaml` at the authorized selected Project root → `AGNIR_DISCOVERY_NOT_FOUND`;
- missing required `agnir.version` in an otherwise selected 1.0-profile manifest → `AGNIR_DISCOVERY_INCONSISTENT`;
- a present string-valued `agnir.version` declaring a Core version other than `1.0` → `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- after this profile has been selected, missing/mismatched `agnir.discovery_profile`, missing Project identity, missing lineage identity, non-string/wrong-container Core-version serialization, or another schema violation without a more specific rule → `AGNIR_DISCOVERY_INCONSISTENT`;
- expected Project identity mismatch → `AGNIR_DISCOVERY_PROJECT_MISMATCH`;
- explicitly expected/selected logical lineage mismatch → `AGNIR_LINEAGE_NOT_FOUND` or a more specific binding failure in addition to that Core semantic class;
- missing/invalid/escaping/wrong-shape required local State/Next Actions → `AGNIR_DISCOVERY_UNRESOLVABLE`;
- non-null Decisions not resolving to a regular file, or non-null Evidence not resolving to a directory → `AGNIR_DISCOVERY_UNRESOLVABLE`;
- distinguishable denied authorization for an explicitly known external Locator Chain → `AGNIR_DISCOVERY_UNAUTHORIZED`.

A valid `0.2` manifest is not malformed merely because `1.0` exists. A multi-version distribution may dispatch it to the published `repository-filesystem/0.2` resolver. The `1.0` resolver itself MUST NOT silently accept `0.2` as `1.0`.

## 4. Local target-shape and Evidence rules

The repository/filesystem target-shape rules remain:

- `memory.state` → one regular file;
- `memory.next_actions` → one regular file;
- non-null `memory.decisions` → one regular file;
- non-null `memory.evidence` → one directory serving as the local Evidence collection root.

Baseline Evidence discovery remains flat: ordinary profile discovery exposes immediate regular-file children of the declared Evidence directory and does not recursively treat nested files as immediate baseline Evidence objects.

Filesystem indirection does not waive selected-root authority. An immediate Evidence entry reached through a symlink/equivalent MAY be exposed only when the canonical resolved target is a regular file inside the authorized selected Project root. An out-of-root canonical target without an authorized external Locator Chain is `AGNIR_DISCOVERY_UNRESOLVABLE`.

## 5. Checkpoint and lineage semantics

A `repository-filesystem/1.0` checkpoint is scoped to the logical lineage exposed by the selected root.

The accepted transactional invariants remain:

1. reconcile Project truth;
2. construct a coherent candidate;
3. detect stale authoritative base;
4. publish changed Project/continuity objects coherently;
5. verify fresh discovery of the same Project identity and logical lineage identity.

A completed checkpoint MUST NOT silently mutate another logical lineage merely because another root/ref shares Project identity.

Optional VCS selector/binding, fork/rebind, delete/recreate, and integration semantics remain behaviorally equivalent to the incorporated `0.2` profile. Selector/binding, logical lineage identity, and revision/checkpoint receipt remain distinct concepts.

## 6. Relationship to repository-filesystem/0.2

`repository-filesystem/0.2` remains a supported historical compatibility profile.

A repository/distribution containing `repository-filesystem/1.0` MAY continue to resolve an unchanged `0.2` Project through the published `0.2` resolver. Merely installing the `1.0` distribution MUST NOT silently rewrite the Project's profile identifier.

A Project that chooses to change from Core/profile `0.2` to `1.0` follows `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

That promotion preserves Project identity, logical lineage identity, durable memory semantics/content/locators, Project policy, unrelated extensions, optional VCS binding semantics, and unrelated Project content. It changes the compatibility declaration and validates/fresh-resolves the resulting 1.0 Project.

## 7. Relationship to repository-filesystem/0.1

A `repository-filesystem/0.1` Project MUST NOT be silently relabeled as `1.0` because it lacks the explicit Continuity Lineage semantics introduced by `0.2`.

A supported path to `1.0` preserves the existing boundaries:

1. explicit Core/profile `0.1` → `0.2` migration;
2. explicit Core/profile `0.2` → `1.0` stability promotion.

A higher-level tool MAY compose both steps but MUST preserve the observable semantics of each.

## 8. Conformance requirements

Stable `repository-filesystem/1.0` conformance MUST demonstrate at least:

1. cold-start discovery returns Core `1.0`, profile `repository-filesystem/1.0`, one Project identity and one logical lineage identity;
2. selected missing/unresolvable memory fails explicitly;
3. schema-invalid serialization is rejected rather than ignored;
4. the 1.0 failure-precedence rules above are machine-visible;
5. State/Next/Decisions/Evidence target shape and flat Evidence semantics match the accepted 0.2 behavior;
6. local filesystem indirection never silently reads an unauthorized out-of-root target;
7. checkpoint no-op/material/stale/fresh-resume behavior remains equivalent to 0.2;
8. two selected roots/worktrees may share Project identity while exposing distinct lineages and continuity;
9. VCS selector and logical lineage identity may differ; binding mismatch does not fall back or guess;
10. fork/rebind/integration semantics remain equivalent to accepted 0.2 behavior;
11. valid `0.2` Projects remain resolvable through the separate 0.2 compatibility path in a 1.0 distribution;
12. explicit `0.2` → `1.0` promotion is authorized, preserving, idempotent, stale-safe, and fresh-resumable;
13. composed `0.1` → `0.2` → `1.0` behavior preserves the published 0.1→0.2 migration contract.

The normative Core 1.0 contract is `spec/AGNIR_CORE_1_0.md`. The promotion boundary is `spec/CORE_0_2_TO_1_0_PROMOTION.md`.