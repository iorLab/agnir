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

A profile implementation MAY preserve existing Core `0.1` memory paths during migration. Core `0.2` does not require moving continuity merely to add lineage identity.

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
10. Core `0.1` migration preserves durable truth and fresh-resumes as exactly one initial lineage.
