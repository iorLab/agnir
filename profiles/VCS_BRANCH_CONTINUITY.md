# Agnir Repository/VCS Branch Continuity Extension 0.1

**Extension identifier:** `agnir/vcs-branch-continuity/0.1`  
**Status:** Experimental repository/VCS extension for Agnir Core `0.1` + `repository-filesystem/0.1`

This extension defines branch-aware continuity behavior for repository/VCS implementations without making branches, Git, repositories, or VCS concepts part of Agnir Core.

Agnir Core remains storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral. The repository/filesystem profile remains the discovery contract. This extension only defines how a VCS-aware implementation MAY map parallel repository refs/worktrees onto parallel Project continuity.

## 1. Model

A VCS-aware Agnir implementation MUST keep these concepts distinct:

1. **Project identity** — the durable identity of the continuing Project. Branch creation, checkout, rebase, merge, cherry-pick, ref rename, or worktree creation MUST NOT silently create a new Project identity.
2. **Branch-local continuity** — the Current State, Next Actions, Decisions, and Evidence resolved from one selected VCS ref/worktree after that ref diverges from another ref.
3. **Repository authority** — the ref or publication boundary declared authoritative for a particular repository policy. Authority is not the same thing as the currently checked-out ref.
4. **VCS revision receipt** — a commit/revision identifier that MAY identify a checkpoint publication. A revision receipt is not Project identity and is not a durable continuity-line identity.

This extension deliberately does not standardize a durable generic `lineage.id`. Branch/ref names are treated as VCS locators/runtime observations for this compatibility line. A future Core version MAY generalize proven branch behavior into a storage-neutral continuity-lineage concept only after non-VCS evidence exists.

## 2. Branch creation and divergence

When a branch/ref is created from a coherent checkpoint:

- the new branch MAY initially inherit the same Agnir continuity content as its base revision;
- `project.identity` MUST remain the same Project identity unless the Principal explicitly creates a distinct Project;
- after either branch checkpoints material continuity changes, each branch MUST resolve its own branch-local Project truth from its selected Project root/ref;
- an implementation MUST NOT silently read continuity from a sibling branch merely because that branch is declared authoritative or was the branch of origin.

A Git worktree is a valid branch-local Project root under `repository-filesystem/0.1` when its own top-level `AGNIR.yaml` and declared continuity locators resolve coherently.

## 3. Checkpoint isolation

A checkpoint performed on one branch/ref MUST publish continuity to that branch/ref only, unless the Principal has separately authorized publication to another destination.

A branch-local checkpoint MUST NOT mutate or redefine sibling branch continuity merely because both branches share the same Project identity.

The Core transactional checkpoint rules still apply independently on every branch: materiality/no-op evaluation, stale-base detection, coherent publication, and post-publication discovery verification remain mandatory where applicable.

## 4. Integration events require reconciliation

The following VCS events are integration boundaries:

- merge;
- rebase when continuity is carried across a rewritten base;
- cherry-pick when a Project change is transferred between refs.

For these events, source-branch Agnir continuity is reconciliation input only. It MUST NOT be automatically promoted to target-branch truth.

Before an implementation claims the target branch is continuity-complete after integration, it MUST reconcile:

1. directly observed resulting Project state;
2. target-branch continuity before integration;
3. relevant source-branch continuity and Evidence;
4. current Principal intent/policy;
5. the actual VCS integration result.

The resulting Current State and Next Actions MUST describe the target branch after integration. Source-only blockers, completed branch-local tasks, superseded decisions, and temporary review/deployment steps MUST NOT survive merely because a text merge carried them into the target tree.

If an integration result exists but target continuity has not yet been reconciled, the implementation MUST surface semantics equivalent to:

`AGNIR_VCS_RECONCILIATION_REQUIRED`

and MUST NOT report target continuity as fully reconciled.

## 5. Merge

A merge MAY allow VCS to merge Agnir-owned files mechanically, but a clean text merge is not evidence that Project truth is semantically reconciled.

After merge, the target branch owns the resulting checkpoint. The target checkpoint MUST preserve the target Project identity and MUST be verified from the target Project root/ref.

When Project changes and the reconciled Agnir update can be represented in the same merge/result revision, implementations SHOULD publish them together rather than creating a follow-up checkpoint-only revision.

## 6. Rebase and history rewriting

Rebase, amend, squash, and force-rewrite operations MAY change VCS revision identifiers while leaving the logical Project work and Agnir continuity unchanged.

Therefore:

- a VCS commit SHA/revision MUST NOT be treated as Project identity;
- a VCS revision receipt MUST NOT be treated as a durable generic continuity-line identity;
- after a history rewrite, the implementation MUST re-resolve the selected branch and verify that its Agnir continuity still describes the rewritten Project state;
- if material Project truth changed during conflict resolution, checkpoint reconciliation is required before continuity-complete status is claimed.

## 7. Cherry-pick

Cherry-pick transfers selected Project changes, not the source branch's entire continuity state.

A target branch MUST NOT copy source Current State or Next Actions wholesale merely because one or more source commits were cherry-picked. Relevant Decisions/Evidence MAY inform target reconciliation when they remain true and useful after transfer.

## 8. Repository authority and push verification

Repository-aware Projects MAY continue to declare:

```yaml
extensions:
  agnir/repository:
    canonical: "owner/name"
    authoritative_ref: "main"
```

`authoritative_ref` identifies repository publication authority. It MUST NOT be interpreted as the only branch on which Agnir may checkpoint or as an instruction to silently redirect feature-branch writes to that ref.

After a push/publication, an implementation SHOULD verify the **actual destination ref** requested by the Principal or VCS operation.

If the operation additionally claims that authoritative repository truth was published, then the actual destination MUST match the declared `authoritative_ref` (when one is declared) and that authoritative ref MUST be verified.

A push to `feature/a` therefore verifies `feature/a`; it does not need to update `main`. A claim that the same push updated authoritative truth is invalid when `authoritative_ref: main` and `main` was not the destination.

Implementations MAY surface failure semantics equivalent to:

- `AGNIR_VCS_AUTHORITY_UNRESOLVED` — authoritative publication was claimed but no applicable authoritative ref can be resolved;
- `AGNIR_VCS_AUTHORITY_MISMATCH` — authoritative publication was claimed for a destination that is not the declared authoritative ref.

These are extension-level failures, not Agnir Core discovery classes.

## 9. Optional manifest policy declaration

A Project MAY make branch-continuity policy explicit without persisting the active branch name:

```yaml
extensions:
  agnir/vcs:
    branch_continuity: "branch-local"
    integration_reconciliation: "required"
```

The active ref SHOULD be observed from the authorized VCS/worktree context. It SHOULD NOT be duplicated as durable Project identity, because refs may be renamed, deleted, recreated, or rewritten.

The manifest schema for `repository-filesystem/0.1` already permits namespaced extension objects; this extension therefore does not require a Core or profile schema change.

## 10. Conformance

A branch-aware conformance case SHOULD prove at least:

1. two Git branches/worktrees with the same `project.identity` can resolve different branch-local Agnir Current State after divergence;
2. checkpointing one branch does not mutate a sibling branch's continuity snapshot;
3. merge, rebase, and cherry-pick require explicit target continuity reconciliation rather than source-state promotion;
4. cross-Project integration is rejected as a Project identity mismatch;
5. rebase/history rewriting may change revision receipts without changing Project identity or otherwise coherent continuity;
6. feature-branch push verification targets the actual destination ref, while authoritative publication claims additionally enforce the declared authoritative ref.

The reference suite implements these cases in `conformance/test_vcs_branch_continuity.py`.
