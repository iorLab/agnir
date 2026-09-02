# Brand branch reconciliation with authoritative main — 2026-09-03

Status: **branch-local integration evidence; not canonical until brand integration reaches authoritative `main`.**

## Trigger

During final brand QA, `brand/identity-system` was observed diverged from authoritative `main`: the brand branch was ahead with the approved identity work but behind by 88 commits because Core 0.2 Parallel Continuity had meanwhile been integrated into `main`.

Latest authoritative main observed before reconciliation: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.

The current `main` continuity contract includes `agnir/vcs.branch_continuity: branch-local` and `integration_reconciliation: required`; Core 0.2 remains a pre-RC integrated line while the repository self-host remains Core/profile 0.1 until deliberate RC migration.

## Reconciliation

A reverse-sync PR was opened with `head=main` and `base=brand/identity-system` so authoritative main would be absorbed into the temporary brand branch without changing `main`.

- PR: `#8`
- main head: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`
- pre-sync brand head: `c45cd4c4c4fe7bd2cffb0789e3be1c5fa1908843`
- merge commit on brand branch: `b00e0d7c544e74d4b0245569450ecebb271461d5`

Post-merge comparison reports `brand/identity-system` ahead of `main` and **behind by 0**.

## Result

The remaining branch diff is brand-local work only: approved visual references, production masters/exports/tools, QA/handoff material, and brand candidate evidence. The brand branch no longer attempts to carry older versions of canonical `AGNIR.yaml`, Current State, Next Actions, Decisions, release metadata, Core 0.2 contracts, or repository maps over newer authoritative truth.

Therefore future brand-to-main integration must start from this reconciled base and add only durable brand decisions/evidence that remain material after final package/binary/documentation gates.
