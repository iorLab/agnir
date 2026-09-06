# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. The v1 release transaction and the first safe post-release temporary-ref retirement pass are complete.

1. **Operate in stable-maintenance mode.** `v1.0.0` is the current latest stable distribution. Patch releases must preserve the stable Core/profile 1.0 public contract unless a deliberate new compatibility line is introduced.
2. **Preserve multi-version support.** Keep historical Core/profile `0.1` and `0.2` compatibility/migration surfaces working and tested. Do not silently reinterpret or relabel them as `1.0`.
3. **Treat `0.2` → `1.0` as an explicit Project-owned promotion.** Preserve authorization, staging, stale-source rejection, identity/lineage preservation, and idempotence semantics.
4. **Preserve the three retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines. Do not retire them merely for branch-count cleanliness.
5. **Resolve the remaining active brand branch separately.** `brand/identity-system` stays while draft PR #11 and its byte-exact large-binary preservation gate remain unresolved. Reconcile it against then-current authoritative `main` before any eventual integration; do not delete it as housekeeping while the PR is active.
6. **Collect post-1.0 adoption evidence without reopening satisfied gates by default.** Reopen a release/compatibility gate only if new evidence exposes a real defect.
7. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Stable release receipts

- latest stable: `v1.0.0`;
- stable/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable GitHub Release id: `383612171`;
- publication workflow: `34039014354`;
- attempt 1 repository job: `101502237380` success;
- attempt 1 stable publication job: `101502271312` success;
- fresh attempt 2 repository job: `101502430280` success;
- fresh attempt 2 stable publication job: `101502473422` success;
- accepted RC remains `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- issue #29: closed completed.

## Housekeeping receipts

- retired temporary branch refs: 17;
- cleanup arm: `a1007845d5d28947f5409fc7dc7643dac54d72d6`;
- cleanup workflow/run/job: `34040930337` / `101507430125`, success;
- cleanup conformance run/job: `34040930367` / `101507430301`, success;
- one-shot workflow removal: `a4b7d9d0642e81974ba35f4f8ccf943099281de1`;
- removal conformance run/job: `34041050353` / `101507754342`, success;
- obsolete issue #14: closed completed;
- retained branches after cleanup: `main`, `brand/identity-system`, `release/v1.0.0-rc.1`, `release/v1.0.0`, `validation/mount-boundary-v0.2.0`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/staging continuity is reconciliation input, not automatic target truth.
- Published tags are immutable.
- Active PR branches are not housekeeping garbage.
- Diverged evidence anchors are retained until their evidence role is durably replaced.
- Historical Core/profile 0.1 and 0.2 remain supported.
