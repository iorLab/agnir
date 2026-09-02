# Agnir Next Actions

Agnir `v0.1.1` remains the published stable release. Core `0.2` Parallel Continuity is now safely integrated into authoritative `main`; exact integrated revision `a32c9143687b72426617ddd701b90ffd237a111c` passed authoritative-main conformance run `33653087179`.

## v0.2.0-rc.1 preparation

1. **Create a temporary `release/v0.2.0-rc.1` branch from the post-integration main checkpoint.** Keep `main` authoritative and do not mutate published `v0.1.1` tags/releases.
2. **Promote only the intended Core/profile 0.2 contracts from draft to RC/normative form.** Preserve compatibility-line separation: repository SemVer, Core compatibility, profile versions, and experimental VCS extension versions remain distinct.
3. **Update repository release metadata deliberately for `0.2.0-rc.1`.** `VERSION`, release notes/contracts, README compatibility wording, operational provenance, and repository maps must agree; `latest stable` must still resolve to published `v0.1.1`, not the RC.
4. **Migrate the RC branch's own Agnir self-host from Core/profile `0.1` to `0.2` explicitly.** Preserve Project identity and durable truth, assign/bind an RC-branch logical lineage coherently, and verify fresh Core `0.2` discovery. Do not reinterpret the branch selector or revision receipt as lineage identity.
5. **Run exact RC candidate conformance.** Require stable `0.1` regression coverage, Core/profile `0.2`, VCS lineage/binding, migration, full suite, and fresh self-host resume on the RC branch.
6. **Exercise fresh install and real migration/resume.** Validate a fresh `0.2.0-rc.1` installation and at least one real Project migration from published `v0.1.1` / Core/profile `0.1` to Core/profile `0.2`, followed by cold-start resume without predecessor-private context.
7. **Tag/publish `v0.2.0-rc.1` only from an exact verified candidate.** RC publication must be immutable. It is prerelease evidence, not `latest stable`.
8. **After RC evidence is green, reconcile the release branch back into `main` through the same target-publication discipline and prepare final `v0.2.0`.** Final stable publication still requires explicit exact-candidate verification.
9. Continue broader real-Project/execution-surface evidence for eventual `v1.0.0`; add synthetic lineage cases only when real RC/consumer evidence exposes a missing invariant.

## Completed pre-RC gates

- Core `0.2` dual-backend/profile/migration conformance: green.
- Svif real-consumer validation: green; final checkpoint `d42489f72cc8985d353ccbf2f9b6ae7249fe6480`, CI `33619807614`.
- Agnir Core `0.2` source checkpoint: `68cc443d6c44929f1b71d9d534e9b0f73f9745bf`, CI `33620080730`.
- Safe-main candidate: `a32c9143687b72426617ddd701b90ffd237a111c`, tree `759766c34e0f39f0c8d51bea1af22d7d41ad591c`.
- Candidate-tree PR CI: `33653019074`, success.
- Authoritative-main CI: `33653087179`, success.
- PR `#4` and validation PR `#6` recognized merged through exact ancestry; stacked PR `#5` closed as already integrated through the same main revision.

## Invariants to preserve

- Durable continuity belongs to the Project.
- Project identity is not lineage identity; lineage identity is not selector or revision receipt.
- Agnir-aware fork publishes lineage identity + selector binding + coherent inherited/reconciled continuity together.
- Checkpoints are lineage-local by default.
- Source continuity is reconciliation input, not target truth.
- Target-ref advancement is a publication boundary.
- Stale source/target candidates fail rather than overwrite newer truth.
- Core/profile `0.1`→`0.2` is explicit migration; compatible operational upgrade remains separate.
- `latest stable` means an actually published stable release; `v0.1.1` remains stable until final `v0.2.0` publication.
- `main` remains the only intended long-lived authoritative branch; release/validation branches are temporary evidence carriers.
