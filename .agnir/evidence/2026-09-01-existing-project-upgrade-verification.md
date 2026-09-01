# Existing Project upgrade candidate verification — 2026-09-01

Implementation checkpoint:

`2a0cb7bf2068b11f361e315670b2f2dc497b2588`

GitHub Actions verification:

- workflow: `Agnir conformance`
- run: `33463490510`
- job: `99718447961`
- self-hosting cold-start conformance: success
- full `test_*.py` suite: success
- job conclusion: success

The verified checkpoint contains the accepted first-class existing-Project upgrade contract: non-destructive compatible upgrade, optional `agnir/operations` provenance, same-baseline no-op, explicit unstable-target authorization, and migration-required handling for Core/profile compatibility changes.

This evidence records an external verification result after publication of the implementation revision. It does not promote this later observation checkpoint into a new release candidate; `2a0cb7bf2068b11f361e315670b2f2dc497b2588` remains the content-addressed verified `0.1.0` publication candidate.
