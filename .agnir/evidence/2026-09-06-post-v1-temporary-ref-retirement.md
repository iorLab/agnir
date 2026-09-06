# Post-v1 temporary ref retirement

Date: 2026-09-06
Status: accepted repository-housekeeping evidence

## Purpose

Retire completed temporary feature, integration, promotion, release, repair, and validation branch refs after Agnir `v1.0.0` stable publication, without changing any published tag or deleting an active/evidence-bearing branch that still has a distinct purpose.

## Preconditions

- stable `v1.0.0` remained immutable at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted RC `v1.0.0-rc.1` remained immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- authoritative post-release checkpoint before housekeeping was `5871f653c11b874cb92c9c9ef3b8261d528ee899`;
- issue #29 was already closed completed;
- the only open pull request was PR #11 on `brand/identity-system`, so that branch was excluded from retirement;
- obsolete issue #14 was explicitly closed as superseded by issue #26's clean independent-implementation PASS and the completed v1 release.

## Retirement mechanism

The connected GitHub surface did not expose direct branch-ref deletion, so a one-shot repository workflow was staged, verified while unarmed, then armed only by the exact commit message:

`housekeeping: retire safe temporary refs`

The workflow verified immutable release tags and retained anchors before and after deletion.

Receipts:

- initial workflow staging commit: `e52fa73ea702c73420d24743153f13e7fcfe7a35`;
- corrected guarded workflow commit: `384189e078099790f7556f5e32b652e0f814179e`;
- unarmed workflow run: `34040863300`, job `101507249233`, success;
- unarmed conformance run: `34040863172`, repository job `101507248939`, success;
- exact cleanup arm revision: `a1007845d5d28947f5409fc7dc7643dac54d72d6`;
- cleanup workflow run: `34040930337`, job `101507430125`, success;
- cleanup-arm conformance run: `34040930367`, repository job `101507430301`, success;
- one-shot workflow removal revision: `a4b7d9d0642e81974ba35f4f8ccf943099281de1`;
- workflow-removal conformance run: `34041050353`, repository job `101507754342`, success.

The first staged workflow definition produced workflow-level run `34040807970` with zero jobs because its initial job-level guard form was rejected before scheduling. No branch was deleted by that failed definition. The guard was then simplified to a shell-level exact-message check before the real retirement run.

## Retired branch refs

Exactly 17 branch refs were retired:

1. `feature/core-0.2-lineage`
2. `feature/multibranch-continuity`
3. `integration/core-0.2-main-candidate`
4. `integration/v0.2.0-rc.1-main-reconcile`
5. `integration/v0.2.0-stable-main-reconcile`
6. `integration/v1.0.0-stable`
7. `promotion/core-profile-1.0`
8. `release/v0.2.0-rc.1`
9. `release/v0.2.0`
10. `release/v1.0.0-target-validation`
11. `release/validation-v0.2.0-rc.1-from-v0.1.1`
12. `repair/evidence-locator-shape`
13. `repair/independent-docs-v1`
14. `repair/migration-lineage-normalization`
15. `repair/reference-schema-conformance`
16. `repair/version-type-conformance`
17. `validation/v0.2.0-rc.1-from-v0.1.1`

These refs were either already represented in authoritative ancestry/merged PR history or were completed temporary validation/release carriers whose material result is preserved by published tags, canonical evidence, or repository history.

## Retained branch refs

After retirement, the repository had exactly five branch refs:

- `main` — sole intended long-lived authoritative branch;
- `brand/identity-system` at `57bc3ffdfb2d96406ecf768bae1fce39e180ae83` — retained because open draft PR #11 still depends on it and its byte-exact large-binary preservation gate remains unresolved;
- `release/v1.0.0-rc.1` at `afc07d062b957e8dbfe3f859834c787e64aa52be` — retained as the RC acceptance checkpoint/evidence anchor;
- `release/v1.0.0` at `5f88a9c8bcc67753012f8bcae533241482dc1a7d` — retained as the stable staging acceptance checkpoint/evidence anchor;
- `validation/mount-boundary-v0.2.0` at `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa` — retained as the accepted genuine mount-boundary evidence anchor.

The three evidence-only retained refs may be retired later only after their exact evidence reachability has an equally durable replacement. They are not authoritative runtime truth.

## Invariants verified after cleanup

- `v1.0.0` still points exactly to `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- `v1.0.0-rc.1` still points exactly to `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- no publication job was re-armed by housekeeping;
- full Agnir conformance remained green after branch retirement and after removing the one-shot workflow;
- the active brand branch and three explicit evidence anchors were preserved.

## Decision

The safe post-v1 temporary-ref retirement is complete. Future cleanup should treat active PR branches and diverged evidence anchors as retained by default until their dependency/evidence role is explicitly discharged.