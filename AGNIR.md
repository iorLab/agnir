# Agnir Project Instructions

This file is the canonical Executor-facing activation and Project-operation surface for this Agnir-enabled Project. It is Project content, not Agnir Core state and not a replacement for `AGNIR.yaml` or `.agnir/` durable continuity.

## Activation

1. **Enter through the authorized Project Entry Point.** Treat the Project root supplied by the Principal or execution surface as the boundary for discovery. Do not search neighboring Projects or guess another root.
2. **Discover.** Read top-level `AGNIR.yaml`. Validate the declared Core/profile compatibility, Project identity, and — for Core `0.2` or `1.0` — the selected logical Continuity Lineage. Validate selector/binding separately from lineage identity and dispatch according to the compatibility line actually declared.
3. **Load.** Load Current State and Next Actions from the declared selected continuity. Load Decisions and Evidence when they materially constrain the operation. Prefer durable Project truth over private conversational memory unless superseded by a newer Principal instruction or directly observed Project fact.
4. **Work.** Perform the actual Project task outside Agnir Core. Root `SKILL.md` is the canonical Agnir distribution procedure for install, migration, compatibility promotion, upgrade, or repair.

## Checkpoint

At an intentional checkpoint, save-progress, finish, or repository commit boundary:

1. reconcile Project truth, not a transcript;
2. classify only material continuity changes for the selected lineage;
3. if durable truth is unchanged, the checkpoint evaluation is a no-op;
4. if material truth changed, construct the complete coherent checkpoint candidate before publication;
5. reject stale-base publication with `AGNIR_CHECKPOINT_CONFLICT`, then re-resolve and reconcile instead of overwriting newer truth;
6. fresh-resolve the same Project identity and selected lineage after publication so a fresh Executor can resume.

A checkpoint boundary requires **checkpoint evaluation**, not forced mutation of `.agnir/`. Never manufacture State or Evidence changes merely to make a commit contain Agnir files.

## Repository operations

Interpret repository intent by context rather than global string matching.

- `commit`, `提交`, or `提交代码` in repository context means: **checkpoint evaluation → Project-defined pre-commit policy when declared → commit**.
- `commit and push` or `提交推送` means: **checkpoint evaluation → Project-defined pre-commit policy when declared → commit → push → verify the actual destination ref**.
- Do not execute an isolated Git commit path that bypasses checkpoint evaluation in an Agnir-enabled Project.
- Prefer one coherent VCS revision for Project changes and any material Agnir checkpoint changes. A legitimate checkpoint no-op does not require an `.agnir/` diff.

Project-defined verification commands belong to the Project's operation policy; they are not Agnir Core checkpoint semantics.

## Integrate Continuity Lineages safely

For Core `0.2`/`1.0` parallel continuity, source continuity is reconciliation input, not target truth. Stage without target advancement when Agnir controls the path, reconcile target continuity against the integrated Project result, then publish integrated Project + reconciled target checkpoint coherently.

## Compatibility locator

`README.md#Agnir-Project-Instructions` may remain as a backward-compatible locator for older Agnir `1.0.0` activation paths. It must point to this file rather than become a second copy of this procedure.
