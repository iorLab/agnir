# Transactional checkpoint CI repair — 2026-09-01

## Observed revision

Implementation checkpoint:

`7e40da7f4bacf98d58570d93310a4e124b2d927b`

GitHub Actions workflow:

- workflow: `Agnir conformance`
- run: `33425797110`
- job: `99598920436`
- result: failure in `Self-hosting cold-start conformance`

## Failure

The self-host checker required the case-sensitive marker:

`mixed checkpoint generations`

The Core contained the same semantic phrase at sentence start with uppercase `Mixed`, so the marker check failed before the unit-test stage ran.

This is a conformance wording mismatch, not evidence that transactional checkpoint behavior itself failed.

## Repair

The Core wording is strengthened to state:

`A fresh compatible resolver MUST NOT accept mixed checkpoint generations as a completed checkpoint.`

The repair keeps the checker strict and makes the intended resolver invariant explicit rather than weakening the test to ignore wording drift.

## Checkpoint behavior demonstrated

The failed commit was observed after publication. Agnir did not create an unconditional checkpoint simply because a commit existed; the external CI result changed material Project truth, so this repair checkpoint updates Current State, Next Actions, Core wording, and Evidence together.

The next repaired Git revision is the backend checkpoint receipt. Its own commit SHA is intentionally not embedded in this file before publication.
