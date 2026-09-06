# Agnir Next Actions

Agnir `v1.0.0` stable is published and verified. The approved brand identity system has now been integrated into authoritative `main` and verified by post-merge conformance.

1. **Operate in stable-maintenance mode.** `v1.0.0` remains the current latest stable distribution. Patch releases must preserve the stable Core/profile 1.0 public contract unless a deliberate new compatibility line is introduced.
2. **Preserve multi-version support.** Keep historical Core/profile `0.1` and `0.2` compatibility/migration surfaces working and tested. Do not silently reinterpret or relabel them as `1.0`.
3. **Treat `0.2` -> `1.0` as an explicit Project-owned promotion.** Preserve authorization, staging, stale-source rejection, identity/lineage preservation, and idempotence semantics.
4. **Preserve retained evidence-anchor refs until an equally durable replacement exists.** `release/v1.0.0-rc.1`, `release/v1.0.0`, and `validation/mount-boundary-v0.2.0` are non-authoritative evidence anchors, not active product lines.
5. **Retire `brand/identity-system` when convenient after this checkpoint is verified.** PR #11 is merged and the material brand result is canonical on `main`; the branch is no longer an active product line.
6. **Collect post-1.0 adoption evidence without reopening satisfied gates by default.** Reopen a release/compatibility gate only if new evidence exposes a real defect.
7. **Keep cross-project follow-up scoped correctly.** Svif may consume Agnir 1.0 through its Continuity Provider integration, but Svif compatibility/binding updates belong to Svif's own canonical continuity and must not be smuggled into Agnir maintenance.
8. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Brand integration receipts

- PR: `#11`;
- final brand head: `3ce946741835498d91aad9ab1eba0cfad6188e30`;
- authoritative squash merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- post-merge conformance run/job: `34042053904` / `101510482659` — success;
- byte-exact reference and complete PNG preservation: closed/verified;
- published `v1.0.0` and `v1.0.0-rc.1` tags: unchanged.

## Stable release receipts

- latest stable: `v1.0.0`;
- stable/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable GitHub Release id: `383612171`;
- publication workflow: `34039014354`;
- accepted RC remains `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- issue #29: closed completed.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source/staging continuity is reconciliation input, not automatic target truth.
- Published tags are immutable.
- Historical Core/profile 0.1 and 0.2 remain supported.
- Brand assets do not redefine Agnir Core/profile semantics.