# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. The v1 release transaction is complete.

1. **Operate in stable-maintenance mode.** `v1.0.0` is the current latest stable distribution. Patch releases must preserve the stable Core/profile 1.0 public contract unless a deliberate new compatibility line is introduced.
2. **Preserve multi-version support.** Keep historical Core/profile `0.1` and `0.2` compatibility/migration surfaces working and tested. Do not silently reinterpret or relabel them as `1.0`.
3. **Treat `0.2` → `1.0` as an explicit Project-owned promotion.** Preserve authorization, staging, stale-source rejection, identity/lineage preservation, and idempotence semantics.
4. **Retire temporary release/validation refs when safe.** They are non-authoritative audit/staging refs only; published tags `v1.0.0-rc.1` and `v1.0.0` must never move.
5. **Collect post-1.0 adoption evidence without reopening satisfied gates by default.** Reopen a release/compatibility gate only if new evidence exposes a real defect.
6. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

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

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/staging continuity is reconciliation input, not automatic target truth.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
