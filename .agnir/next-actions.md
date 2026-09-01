# Agnir Next Actions

Agnir `0.1.0` is release-ready again with the compatible existing-Project upgrade contract included and exact-revision conformance passing.

Verified publication candidate:

`2a0cb7bf2068b11f361e315670b2f2dc497b2588`

Verification:

- GitHub Actions workflow: `Agnir conformance`
- run: `33463490510`
- job: `99718447961`
- self-hosting cold-start conformance: success
- full `test_*.py` suite: success

1. **Publication only:** after explicit Principal authorization, create tag `v0.1.0` / GitHub Release on the intended verified candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`.
2. Until that stable tag/release exists, do not upgrade old Projects to `latest stable` by silently using `main`. A pre-release revision requires explicit authorization.
3. After stable publication, compatible old Projects may be upgraded with the first-class `upgrade` operation. Preserve Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
4. Record applied operational provenance under optional `agnir/operations` when the distribution/revision is known; legacy Projects without provenance remain valid upgrade inputs.
5. Treat Core/profile changes as migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.
6. Preserve same-baseline upgrade no-op behavior and fresh activation as the compatible-upgrade completion gate.
7. Preserve transactional checkpoint, repository commit/push intent, activation, safe `AGENTS.md` merge, and Core storage/VCS neutrality.
8. Keep real mount-boundary validation optional until a real mount-capable environment exists.

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- `RELEASE.md` is the publication contract.
- `.agnir/evidence/` remains represented by directory responsibility rather than per-evidence filename registration.
- `main` remains the only long-lived authoritative branch.
