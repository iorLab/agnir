# Agnir Repository/Filesystem Profile 0.2

**Profile identifier:** `repository-filesystem/0.2`  
**Core compatibility:** Agnir Core `0.2`  
**Status:** Stable normative profile for repository `v0.2.0` and later repository releases that explicitly declare `repository-filesystem/0.2` compatibility.

This profile extends the repository/filesystem discovery model so a selected Project root resolves one explicit logical Continuity Lineage.

It does not require Git or any VCS. VCS selector/binding behavior is an optional adapter/extension layer described below.

## 1. Project root and discovery anchor

The selected Project root contains a top-level `AGNIR.yaml` discovery anchor.

A fresh compatible Executor MUST NOT recursively search arbitrary parents, sibling repositories, sibling branches, or unrelated workspaces to guess the Project root or lineage.

The manifest declares Core/profile compatibility and the logical lineage exposed by the selected root.

Minimum semantic shape:

```yaml
agnir:
  version: "0.2"
  discovery_profile: "repository-filesystem/0.2"

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

`schemas/agnir-manifest-0.2.schema.json` is the normative serialized-shape constraint for this profile. A selected `AGNIR.yaml` MUST satisfy that schema. Forbidden additional properties, missing required properties, wrong scalar/container types, invalid extension names, and other schema violations MUST NOT be silently ignored. Unless a more specific failure rule below applies, a schema-invalid selected manifest surfaces `AGNIR_DISCOVERY_INCONSISTENT`.

`project.identity` and `continuity.lineage` MUST both be non-empty.

`continuity.lineage` is the resolved **logical lineage identity**, not a filesystem path, VCS revision, or implicit branch name.

## 2. Selected-root semantics

Ordinary discovery resolves one selected Project root and therefore one logical lineage identity.

The profile does not require `AGNIR.yaml` to enumerate sibling lineages. Parallel lineage enumeration, registries, dashboards, or workspace indexes may be provided by adapters/extensions but are not required for cold-start resume of one selected lineage.

A selected Project root MUST resolve Current State and Next Actions for the lineage declared by `continuity.lineage`. Decisions and Evidence follow the same optionality rules as Core.

## 3. Memory locators

The locator rules from `repository-filesystem/0.1` remain conceptually valid:

- State and Next Actions are required;
- Decisions and Evidence may be nullable only when no material durable content is required;
- local locators must remain within the authorized selected Project root unless an authorized Locator Chain explicitly resolves external memory;
- a fresh resolver must reject unresolvable or mixed-generation continuity rather than guessing.

For this profile, the local repository/filesystem target shape is normative and distinct from the YAML scalar type used to serialize the locator:

- `memory.state` MUST resolve to one regular file;
- `memory.next_actions` MUST resolve to one regular file;
- non-null `memory.decisions` MUST resolve to one regular file;
- non-null `memory.evidence` MUST resolve to one directory that serves as the local Evidence collection root.

A schema-valid locator string therefore does not by itself prove that the referenced filesystem object has the required target shape. A non-null local Evidence locator resolving to a regular file is not a conforming alternative representation of the Evidence collection and MUST fail with `AGNIR_DISCOVERY_UNRESOLVABLE`.

Baseline local Evidence discovery is intentionally flat for this compatibility line: the Evidence objects exposed by ordinary profile discovery are the regular-file children immediately contained by the declared Evidence directory, identified by their child filenames. Nested directories MAY exist for adapter- or Project-specific organization, but this profile does not require recursive traversal of them for baseline `repository-filesystem/0.2` discovery. An extension MAY define richer recursive/indexed Evidence behavior without changing the baseline target-shape rule above.

Filesystem indirection does not waive selected-root authority for the Evidence collection. An immediate Evidence entry reached through a symlink or equivalent filesystem indirection MAY be exposed as a local Evidence object only when its canonical resolved target is a regular file within the authorized selected Project root. If such an immediate entry resolves outside the selected Project root without an authorized external Locator Chain, ordinary local discovery MUST fail with `AGNIR_DISCOVERY_UNRESOLVABLE` rather than read the external target as local Evidence.

A profile implementation MAY preserve existing Core `0.1` memory paths during migration. Core `0.2` does not require moving continuity merely to add lineage identity.

### Required discovery-failure mapping

For interoperability, a resolver executing this selected profile MUST classify the following conditions consistently:

- missing top-level `AGNIR.yaml` at the authorized selected Project root → `AGNIR_DISCOVERY_NOT_FOUND`;
- missing required `agnir.version` in an otherwise selected 0.2-profile manifest → `AGNIR_DISCOVERY_INCONSISTENT`;
- a present string-valued `agnir.version` that declares a Core version other than `0.2` → `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`;
- after this profile has been selected, missing or mismatched `agnir.discovery_profile`, missing `project.identity`, missing `continuity.lineage`, a non-string/wrong-container `agnir.version`, or another published-schema violation without a more specific rule → `AGNIR_DISCOVERY_INCONSISTENT`;
- an explicitly expected Project identity that differs from the resolved Project identity → `AGNIR_DISCOVERY_PROJECT_MISMATCH`;
- an explicitly selected/expected logical lineage that does not resolve to the lineage exposed by the selected root → `AGNIR_LINEAGE_NOT_FOUND` or a more specific binding failure in addition to that Core semantic class;
- required local State/Next Actions locators that are missing, invalid, escape the selected Project root without an authorized external Locator Chain, or do not resolve to regular files → `AGNIR_DISCOVERY_UNRESOLVABLE`;
- a non-null local Decisions locator that does not resolve to a regular file, or a non-null local Evidence locator that does not resolve to a directory, → `AGNIR_DISCOVERY_UNRESOLVABLE`;
- a known external Locator Chain target whose required authorization is absent or denied → `AGNIR_DISCOVERY_UNAUTHORIZED` when the implementation can safely distinguish authorization failure from not-found/unresolvable state.

`AGNIR_DISCOVERY_UNSUPPORTED_VERSION` therefore requires an actually declared incompatible Core version serialized as a string-valued version declaration. Absence of the required version field, explicit null, or a wrong scalar/container type is malformed selected-profile serialization and is `AGNIR_DISCOVERY_INCONSISTENT`. A profile mismatch is likewise not an unsupported-Core condition. Conversely, a local locator escaping the selected Project root is unresolvable as a local locator; it becomes an authorization question only when an explicit external Locator Chain/binding is actually being resolved.

## 4. Checkpoint publication

A repository/filesystem `0.2` checkpoint is scoped to the logical lineage exposed by the selected root.

The transactional checkpoint invariants remain:

1. reconcile Project truth;
2. construct a coherent candidate;
3. detect stale authoritative base;
4. publish changed Project/continuity objects coherently;
5. verify fresh discovery of the same Project identity and logical lineage identity.

A completed checkpoint MUST NOT silently mutate another logical lineage merely because another root/ref shares the same Project identity.

## 5. Optional VCS selector/binding extension

A VCS-aware implementation MUST keep the selected VCS ref/worktree separate from `continuity.lineage`.

Recommended extension shape:

```yaml
extensions:
  agnir/vcs:
    branch_continuity: "lineage-bound"
    integration_reconciliation: "required"
    lineage_binding:
      kind: "vcs-ref"
      selector: "refs/heads/main"
```

Semantics:

- `lineage_binding.selector` is a backend selector/locator;
- `continuity.lineage` is the durable logical lineage identity;
- the selector MAY change through an explicit rebind/rename while the logical lineage identity remains the same;
- a VCS revision/commit SHA is a checkpoint receipt and MUST NOT replace either field.

The exact nested extension serialization may continue to evolve independently; the semantic distinction between logical lineage identity and backend selector/binding is normative for this profile.

## 6. Agnir-aware branch/ref fork

When an Agnir-aware VCS adapter intentionally creates a new parallel continuity line from a coherent source lineage, it MUST distinguish branch creation from lineage forking.

A new VCS ref may initially point at exactly the same revision and therefore expose the same continuity snapshot. Before that ref is published as an independently advancing lineage, the adapter MUST establish a new logical lineage identity and bind the new selector to it.

Safe conceptual sequence:

1. capture source Project identity, logical lineage identity, checkpoint receipt, and continuity;
2. create/select the new VCS ref without changing Project identity;
3. generate/choose a new durable logical lineage identity according to adapter policy;
4. update the selected ref's Core `0.2` discovery/binding metadata to the new lineage identity;
5. preserve inherited continuity as the new lineage baseline;
6. publish the branch-local checkpoint coherently;
7. fresh-resolve the new selector and verify the new lineage identity.

The adapter MUST NOT derive the new lineage identity from the commit SHA.

When Agnir controls the fork, the new lineage identity, selector binding, and coherent inherited/reconciled continuity MUST become visible together; sequential ref-visible writes that temporarily expose copied source binding under the new selector are not a conforming fork publication path.

## 7. External branch creation and binding mismatch

A branch/ref may be created outside Agnir by copying an existing revision. In that case the copied `AGNIR.yaml` may still carry the source logical lineage identity and source binding metadata.

A fresh VCS-aware resolver that observes a selected ref inconsistent with its durable binding MUST NOT guess whether the user intended:

- a new lineage fork;
- a ref rename/rebind of the existing lineage;
- a detached/temporary selector;
- or an accidental stale copy.

It MUST require explicit adapter/Principal resolution before claiming independent lineage continuity.

Recommended profile/adapter failures:

- `AGNIR_VCS_LINEAGE_BINDING_REQUIRED` — selected VCS context has no sufficient durable binding;
- `AGNIR_VCS_LINEAGE_BINDING_MISMATCH` — selected VCS context conflicts with the persisted binding.

Both map to a Core condition where the selected lineage cannot yet be resolved safely; an implementation may additionally expose `AGNIR_LINEAGE_NOT_FOUND` semantics.

## 8. Ref rename/rebind

An explicit VCS ref rename is not a Project fork and need not be a lineage fork.

An Agnir-aware rebind SHOULD:

1. preserve `project.identity`;
2. preserve `continuity.lineage`;
3. update only the backend selector/binding metadata required by the adapter;
4. preserve Current State / Next Actions / Decisions / Evidence unless material Project truth changed;
5. verify fresh discovery through the renamed selector.

An external rename that leaves stale binding metadata is a binding-repair case, not evidence that a new logical lineage should be minted automatically.

## 9. Ref deletion/recreation

A deleted VCS ref does not delete the Project. Whether it retires a logical lineage is a separate Project/backend policy decision.

A later ref recreated with the same textual name MUST NOT automatically inherit the prior logical lineage identity solely because the selector string matches. The adapter must establish continuity from durable Project/binding/evidence context.

This prevents selector reuse from becoming accidental identity reuse.

## 10. Integration

For VCS-backed lineages, merge/rebase/cherry-pick remain profile/adapter integration boundaries.

The Core `0.2` target-reconciliation and coherent-publication rules apply. The VCS adapter must stage the Project integration without target publication, reconcile the target logical lineage, then publish the integrated Project result + reconciled target continuity in the target-advancing revision/transaction.

Source selector/binding metadata is not target truth and must not be copied blindly.

## 11. Core 0.1 migration

A repository/filesystem `0.1` Project may migrate to this profile without relocating existing memory.

A conforming migration MUST:

- explicitly authorize the Core/profile compatibility-line change;
- preserve Project identity;
- choose/generate one initial durable logical lineage identity;
- preserve existing State / Next Actions / Decisions / Evidence;
- write a coherent Core `0.2` + `repository-filesystem/0.2` discovery result;
- establish optional VCS selector binding when the Project is VCS-aware;
- verify fresh `0.2` discovery;
- be idempotent for the same resulting lineage identity/binding.

The storage-neutral migration contract is `spec/CORE_0_1_TO_0_2_MIGRATION.md`; executable concrete migration pressure is part of repository conformance.

## 12. Conformance requirements

Stable `repository-filesystem/0.2` conformance includes at least:

1. cold-start discovery returns Core `0.2`, profile `repository-filesystem/0.2`, one Project identity, and one logical lineage identity;
2. selected missing/unresolvable memory fails explicitly;
3. two selected roots/worktrees may share Project identity while exposing distinct logical lineage identities and continuity;
4. checkpoint verification preserves the selected logical lineage identity;
5. VCS selector and logical lineage identity may differ;
6. unbound/mismatched VCS selection does not fall back or guess;
7. explicit ref rename/rebind can preserve logical lineage identity;
8. a branch fork can establish a new logical lineage identity while preserving Project identity and inherited baseline continuity;
9. target integration obeys staged reconciliation and coherent publication;
10. Core `0.1` migration preserves durable truth and fresh-resumes as exactly one initial lineage;
11. string-valued Core-version mismatch, missing Core-version serialization, wrong-type Core-version serialization, and profile mismatch produce the distinct failure semantics specified above;
12. local locator escape without an authorized external Locator Chain is rejected as `AGNIR_DISCOVERY_UNRESOLVABLE` rather than silently treated as an external-memory authorization path;
13. the reference/conformance resolver rejects published-schema-invalid manifests, including forbidden additional properties, instead of ignoring unknown shorthand fields;
14. non-null local State/Next Actions/Decisions locators resolve to regular files, non-null local Evidence resolves to a directory, and baseline Evidence discovery does not recursively treat nested files as immediate Evidence objects;
15. local Evidence filesystem indirection never reads a canonical target outside the selected Project root without an authorized external Locator Chain.
