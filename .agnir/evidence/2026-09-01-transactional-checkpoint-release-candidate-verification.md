# Transactional checkpoint release-candidate verification — 2026-09-01

## Verified candidate

`05103320afa25085d2cb9b65b249a8ad63e883e9`

This revision contains the transactional checkpoint semantics, repository commit/push integration, executable checkpoint pressure, bilingual durable activation instructions, evidence-index write-amplification reduction, and the Core wording repair discovered by the predecessor CI run.

## GitHub Actions evidence

- workflow: `Agnir conformance`
- run: `33425996098`
- job: `99599577461`
- exact `head_sha`: `05103320afa25085d2cb9b65b249a8ad63e883e9`
- `Self-hosting cold-start conformance`: success
- `Negative discovery fixtures` / full `test_*.py` discovery: success
- overall repository-filesystem job: success

## Interpretation

The exact content-addressed candidate passed the full active publication gate after the earlier case-sensitive marker failure was repaired. The earlier failure remains durable evidence at `.agnir/evidence/2026-09-01-transactional-checkpoint-ci-repair.md`; it is not hidden or rewritten.

This observation checkpoint records the already-existing external result. It does not redefine the candidate and does not require its own later commit SHA to be embedded in this file. The verified publication candidate remains `05103320afa25085d2cb9b65b249a8ad63e883e9`.

## Resume consequence

Development required for initial `0.1.0` publication is complete again. The next operation is publication only and still requires explicit Principal authorization before tag `v0.1.0` and/or a GitHub Release is created.
