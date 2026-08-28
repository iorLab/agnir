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
- Agnir Core remains storage-, platform-, VCS-, repository-, agent-, and execution-surface-neutral.
- Required durable semantics are Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- A compatible Executor that already knows the applicable profile can cold-start from the authorized Project Entry Point through the Discovery Record and durable memory.
- For an Agent-operable Project using `repository-filesystem/0.1`, initialization must additionally persist an activation route so a future general-purpose Agent can learn that Agnir applies without a repeated user prompt.

Reference Agent activation route:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

`README.md` owns the canonical **Agnir Project Instructions**. Root `AGENTS.md` is a locator to that section and should not fork a second copy of the full rules.

## Durable Agent activation fix

The earlier Quick Start had a bootstrap gap: it asked users to paste an Agnir prompt into an already initialized Project, while the initialization prompt assumed the Agent already understood Agnir.

That gap is closed:

- an already initialized Agent-operable Project requires **no recurring Agnir bootstrap prompt**;
- the initialization prompt is self-contained and explains Agnir before asking the Agent to initialize it;
- initialization creates/validates `AGNIR.yaml` and declared durable memory;
- initialization writes/updates canonical `## Agnir Project Instructions` in `README.md`;
- initialization creates/updates root `AGENTS.md` to reference that README section without duplicating the full contract;
- existing unrelated README / AGENTS content must be preserved and merged, not overwritten;
- initialization ends with fresh-agent validation: Project root → `AGENTS.md` → README instruction → `AGNIR.yaml` → durable memory;
- an execution surface that ignores Project instruction files may require one-time surface configuration, but repeating the Agnir prompt every session is not the intended workflow.

This activation convention is profile-level for Agent-operable repository Projects and does not add an AI-Agent dependency to Core `0.1`.

Implementation head `39d1e029e2b6fe8d47417f1e60c10dcbb0aef80c` passed Agnir conformance run `33165874089`.

Durable evidence: `.agnir/evidence/2026-08-28-durable-agent-activation.md`.

## Conformance coverage

The stable suite now includes:

- self-host Agent activation before `AGNIR.yaml` discovery;
- positive prompt-free fresh-Agent activation;
- negative activation cases for missing `AGENTS.md`, unresolved README reference, incomplete canonical README instruction, and duplicated/forked activation rules;
- all nine named Agnir discovery failure classes;
- durable non-repository SQLite continuity and fresh-resolver resume;
- external-memory authorization without plaintext credentials;
- multi-project isolation;
- Locator Chain cycle / stale / inconsistency pressure;
- symlink boundaries and real Git worktree cold start.

Real mount-boundary behavior remains explicitly unproven; ordinary directories are not accepted as substitute mount evidence.

## Documentation baseline

- `README.md` and `README.zh-CN.md` remain separate bilingual entry documents; same-page language switching remains explicitly deferred and is not a release blocker.
- Both READMEs put the operational Quick Start before architecture.
- Existing-Project Quick Start now states that no recurring Agnir prompt is required.
- New-Project initialization is self-contained and includes durable activation installation.
- Architecture and continuity diagrams show the Agent activation route before repository/filesystem discovery.
- `REPOSITORY_TREE.md` is the exhaustive tracked-file map.

## Relationship to Svif

Svif remains a separate Project orchestration product at `iorLab/svif`. It consumes Agnir Core/profile continuity semantics through its Continuity Provider integration; Svif does not make Git/GitHub or Agnir repository internals universal requirements.

## Current resume point

Development required for the initial Agnir `0.1.0` release is complete, including the durable Agent activation gap fix.

Next operation is **publication only**:

1. after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release;
2. after publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines and keep `0.1.x` maintenance non-breaking;
3. optionally add real mount-boundary evidence when a real mount-capable environment is available.

## Branch governance

- `main` is the only long-lived and authoritative branch.
- Retired branch tips remain indexed in `history/BRANCH_ARCHIVE.md`.
- Historical recovery uses commit SHAs and Git history, not live legacy refs.
