# Agnir Current State

Agnir `v0.1.1` remains the latest formally published **stable** repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Active v0.2.0-rc.1 release lineage — 2026-09-03

Temporary branch `release/v0.2.0-rc.1` is the release-candidate evidence carrier forked from verified authoritative-main checkpoint `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`.

Project identity remains `urn:agnir:project:agnir-core`. This branch has explicitly migrated its self-hosting compatibility from Core `0.1` / `repository-filesystem/0.1` to Core `0.2` / `repository-filesystem/0.2`.

The selected logical Continuity Lineage is `urn:agnir:lineage:v0.2.0-rc.1`, bound separately to VCS selector `refs/heads/release/v0.2.0-rc.1`. The selector string and branch revision are not lineage identity.

The migration preserves the inherited durable Project truth from the verified main baseline and existing `.agnir/state.md`, `.agnir/next-actions.md`, `.agnir/decisions.md`, and `.agnir/evidence/` locator layout. It adds the logical lineage/binding required by Core/profile `0.2` rather than relocating memory merely to change compatibility lines.

## RC contract status

The release branch now contains RC normative compatibility candidates:

- `spec/AGNIR_CORE_0_2.md` — Core `0.2` normative release-candidate contract;
- `profiles/REPOSITORY_FILESYSTEM_0_2.md` — `repository-filesystem/0.2` normative release-candidate profile;
- `schemas/agnir-manifest-0.2.schema.json` — Core/profile `0.2` manifest schema;
- `conformance/check_agnir_0_2_rc.py` — RC self-host cold-start/release consistency gate.

Repository SemVer on this branch is `0.2.0-rc.1`. This is a prerelease candidate, not `latest stable`. Published stable `v0.1.1`, its tag/release, and its Core/profile `0.1` compatibility artifacts remain immutable and supported regression surfaces.

## Operational provenance boundary

`extensions.agnir/operations` intentionally still records the actually applied published operational package `v0.1.1` at `e9712357...`. The RC Skill/README operational procedure has not yet been fully synchronized and assigned an exact immutable applied revision, so this checkpoint does not invent self-referential RC operational provenance.

After the RC operational package is synchronized and an exact candidate revision exists, provenance may be advanced coherently as part of that candidate/installation validation.

## Completed pre-RC evidence

- Core `0.2` source checkpoint `68cc443d6c44929f1b71d9d534e9b0f73f9745bf` passed conformance run `33620080730`.
- Svif real-consumer validation completed at `d42489f72cc8985d353ccbf2f9b6ae7249fe6480`, CI `33619807614`.
- Safe main integration candidate `a32c9143687b72426617ddd701b90ffd237a111c`, tree `759766c34e0f39f0c8d51bea1af22d7d41ad591c`, passed candidate CI `33653019074` and authoritative-main CI `33653087179`.
- Post-integration main checkpoint `f0b2cbd5329adb6ac7309076d7ea09337bb057c5` passed run `33653383024`.

## Remaining RC work

The next work is to synchronize `README.md`, `README.zh-CN.md`, `SKILL.md`, `REPOSITORY_TREE.md`, and release documentation with Core/profile `0.2`; remove or clearly demote the obsolete draft-contract files; then run exact RC branch conformance, fresh-install validation, and at least one real published-`v0.1.1` → Core/profile `0.2` migration plus cold-start resume.

Do not publish/tag `v0.2.0-rc.1` until those gates are green. Do not treat the RC as `latest stable`; stable resolution remains `v0.1.1` until final `v0.2.0` is intentionally published.

`.agnir/next-actions.md` is the ordered resume plan. `.agnir/decisions.md` remains the durable decision set inherited from authoritative main plus the already integrated Core `0.2` decisions.
