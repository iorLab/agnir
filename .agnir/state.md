# Agnir Current State

Agnir is the active greenfield project/protocol identity on `main`. Repository branch governance is main-only; predecessor history is archival under immutable Git history and `history/`.

## Stable release line

Agnir is **release-ready at repository version `0.1.0`**, pending only the explicit publication action (tag / GitHub Release).

Version layers remain distinct:

- Core compatibility: `0.1`;
- repository/filesystem profile: `repository-filesystem/0.1`;
- repository release SemVer: `0.1.0`.

`RELEASE.md` is the publication contract. No `v0.1.0` tag or GitHub Release has been created yet.

## Active contract

- **Durable continuity belongs to the Project**, not an Executor, execution environment, repository host, or conversation.
- Agnir Core remains storage-, platform-, VCS-, repository-, agent-, Skill-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- A compatible Executor that already knows the applicable profile can cold-start from the authorized Project Entry Point through the Discovery Record and durable memory.
- For an Agent-operable Project using `repository-filesystem/0.1`, initialization additionally persists an activation route so a future general-purpose Agent can learn that Agnir applies without a repeated user prompt.

Reference target-Project activation route:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

`README.md` owns the canonical **Agnir Project Instructions** in the initialized target Project. Root `AGENTS.md` is a locator to that section and must not fork a second copy of the full rules.

## Agent Skill distribution baseline

Agnir is now packaged as an **Agent Skill** through top-level `SKILL.md`.

The instruction surfaces are deliberately separated:

- **user-facing install prompt:** one short sentence expressing intent and identifying the Agnir repository;
- **Agent-facing procedure:** root `SKILL.md`, which owns install / initialize / resume / checkpoint / repair;
- **post-install target-Project activation:** target `AGENTS.md` → target README `Agnir Project Instructions` → target `AGNIR.yaml` → durable memory.

Canonical user-facing install requests shown in the bilingual READMEs are:

```text
Install and initialize Agnir for this Project: https://github.com/iorLab/agnir
```

```text
为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir
```

The user does **not** carry Agnir's implementation checklist. The Agent locates this repository, reads `SKILL.md`, and executes the current procedure. The Skill procedure itself is self-contained; the user prompt intentionally is not.

This supersedes the earlier Quick Start wording that placed a long self-contained initialization checklist directly in the user-facing prompt.

After initialization, normal Project work does not depend on the Skill repository or original install conversation just to activate Agnir. The target Project is self-describing through its durable activation route.

## Skill and activation conformance

Current executable pressure includes:

- `conformance/test_skill_package.py` — verifies Skill frontmatter, full Agent procedure, exact one-line bilingual user prompts, and absence of the internal checklist from Quick Start;
- `conformance/activation_reference.py` + `test_agent_activation.py` — verifies prompt-free target-Project activation and negative activation cases;
- `conformance/check_agnir_0_1.py` — self-hosts Skill packaging, Agent activation, `AGNIR.yaml` discovery, version/profile agreement, release surface, and repository documentation structure.

Skill packaging candidate `434f237dbcccfa8173a4d7f6be550ce9133bbc97` passed Agnir conformance run `33176730016`.

## Conformance coverage

The stable suite also covers:

- all nine named Agnir discovery failure classes;
- durable non-repository SQLite continuity and fresh-resolver resume;
- external-memory authorization without plaintext credentials;
- multi-project isolation;
- Locator Chain cycle / stale / inconsistency pressure;
- symlink boundaries and real Git worktree cold start.

Real mount-boundary behavior remains explicitly unproven; ordinary directories are not accepted as substitute mount evidence.

## Documentation baseline

- `README.md` and `README.zh-CN.md` remain separate bilingual entry documents; same-page language switching remains explicitly deferred and is not a release blocker.
- Both READMEs put the user-facing Quick Start before architecture.
- New-Project Quick Start contains only the one-line install request and points the Agent to root `SKILL.md`.
- Existing initialized Projects require no recurring Agnir bootstrap prompt.
- Architecture diagrams distinguish the one-time Skill installation path from the post-install durable Project activation/discovery path.
- `REPOSITORY_TREE.md` is the exhaustive tracked-file map.

## Relationship to Svif

Svif remains a separate Project orchestration product at `iorLab/svif`. It consumes Agnir Core/profile continuity semantics through its Continuity Provider integration; Skill packaging does not make Agnir repository internals, Git/GitHub, or a particular Agent platform universal requirements.

## Current resume point

Development required for the initial Agnir `0.1.0` release is complete, including Agent Skill packaging and durable post-install activation.

Next operation is **publication only**:

1. after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release;
2. after publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines and keep `0.1.x` maintenance non-breaking;
3. preserve the user-prompt / Skill-procedure / target-Project-activation separation;
4. optionally add real mount-boundary evidence when a real mount-capable environment is available.

## Branch governance

- `main` is the only long-lived and authoritative branch.
- Retired branch tips remain indexed in `history/BRANCH_ARCHIVE.md`.
- Historical recovery uses commit SHAs and Git history, not live legacy refs.
