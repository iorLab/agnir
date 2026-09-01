# Agnir Next Actions

Agnir `0.1.0` is development-complete and release-verified. The Principal has explicitly authorized formal publication.

Verified publication candidate:

`2a0cb7bf2068b11f361e315670b2f2dc497b2588`

Verification:

- GitHub Actions workflow: `Agnir conformance`
- run: `33463490510`
- job: `99718447961`
- self-hosting cold-start conformance: success
- full `test_*.py` suite: success

1. **Publish without asking for authorization again:** create real Git tag `v0.1.0` on `2a0cb7bf2068b11f361e315670b2f2dc497b2588` using an execution surface that exposes Git tag creation.
2. Create the GitHub Release for `v0.1.0` from that tag.
3. Verify the tag resolves exactly to `2a0cb7bf2068b11f361e315670b2f2dc497b2588` and verify the GitHub Release exists before reporting publication complete.
4. Do not substitute a branch named `v0.1.0` for the required Git tag.
5. Until tag + Release verification succeeds, keep `latest stable` upgrade blocked from silently using `main`.
6. After publication, compatible old Projects may be upgraded with the first-class `upgrade` operation while preserving identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
7. Record applied operational provenance under optional `agnir/operations` when distribution/revision is known; legacy Projects without provenance remain valid upgrade inputs.
8. Treat Core/profile changes as migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.
9. Preserve transactional checkpoint, repository commit/push intent, activation, safe `AGENTS.md` merge, and Core storage/VCS neutrality.

## Current execution-surface blocker

The connected GitHub tool available during the 2026-09-01 publication attempt exposed commit/ref operations but no mutation for creating Git tags or GitHub Releases. Preflight confirmed `v0.1.0` tag and release were still absent. Publication is therefore authorized but not yet complete.

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- `RELEASE.md` is the publication contract.
- `.agnir/evidence/` remains represented by directory responsibility rather than per-evidence filename registration.
- `main` remains the only long-lived authoritative branch.
