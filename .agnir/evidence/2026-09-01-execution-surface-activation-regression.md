# Execution-surface activation regression — 2026-09-01

## Trigger

A real Agnir initialization was performed from the ChatGPT web `skills-hub` Project against `mattamior/skills-hub`. Repository initialization created/validated the expected Agnir Project surface and commit `5c965da6edcd2b0dead7c5b444a5a910770ad796` recorded the initial continuity setup.

The completion report claimed fresh activation had passed, but the ChatGPT Project had not been given the persistent Project Instructions needed for a new conversation to locate the canonical repository. This exposed a distinction that the previous Skill mentioned but did not enforce operationally: repository activation can pass while execution-surface activation is still incomplete.

## Target Project facts observed

At the time of repair validation, `mattamior/skills-hub` `main` resolved to `f94c3894ec9412724607febbc27b25408a9a90cc`.

Its `AGNIR.yaml` declares:

```yaml
agnir:
  version: "0.1"
  discovery_profile: "repository-filesystem/0.1"
project:
  identity: "urn:github:mattamior:skills-hub"
memory:
  state: ".agnir/state.md"
  next_actions: ".agnir/next-actions.md"
  decisions: ".agnir/decisions.md"
  evidence: ".agnir/evidence/"
extensions:
  agnir/repository:
    canonical: "mattamior/skills-hub"
    authoritative_ref: "main"
```

Therefore the ChatGPT execution-surface handoff produced by the repaired Skill is expected to use `mattamior/skills-hub` and `main`, while continuing to defer all Project truth to the repository's `AGENTS.md` → README → `AGNIR.yaml` route.

## Repair contract

The repaired root `SKILL.md` now requires:

- separate repository-activation and execution-surface-activation status;
- automatic persistent surface configuration when the active tools/authority permit it;
- otherwise a copy-ready locator-only handoff and `pending user configuration` status;
- no full fresh-activation success claim while required surface configuration is pending or unverified;
- a fresh-context test after configuration when possible;
- a ChatGPT Project bootstrap that identifies canonical repository/ref and points the new conversation to root `AGENTS.md` and `AGNIR.yaml`, without embedding Current State, Next Actions, Decisions, Evidence, or the full Agnir procedure.

The expected `skills-hub` handoff is:

```text
Agnir Project bootstrap

Canonical Project: mattamior/skills-hub
Authoritative ref: main

At the first substantive turn of every new conversation, open the canonical Project repository, read root AGENTS.md, and follow its Agnir activation locator before doing Project work.

Load the Project continuity declared by AGNIR.yaml. Treat repository-managed Agnir state as canonical durable Project truth; ChatGPT Project memory and conversation context are working memory only.

When Project work materially changes durable continuity, follow the Project's Agnir checkpoint instructions before finishing, committing, or pushing.
```

This block is to be appended/merged into the ChatGPT Project's persistent Instructions, preserving unrelated existing instructions. It is not a second copy of Project memory.

## Implementation revisions and CI

The repair sequence on `iorLab/agnir/main` was:

1. `9f6cc36241b3fae788b12192d33f5c716809d88b` — added execution-surface handoff semantics and regression checks. CI run `33497279483` failed because the older self-hosting checker still required the literal marker `fresh activation test`.
2. `ab026a0e665ba7110695f5849a6a46554ffe3323` — preserved that compatibility marker while clarifying that it denotes repository-layer activation, not execution-surface completion.
3. `3d8c7d689fd2a5a1bca9ea4fd051c914769136c9` — synchronized bilingual README architecture/flow and added README handoff conformance. CI run `33497611755` passed the self-hosting gate but exposed one over-specific README test marker.
4. `b46656793a5e1ea7a94e39f2da1506fc73db177e` — aligned the test with the documented semantic wording. GitHub Actions `Agnir conformance` run `33497764549` completed successfully.

Run `33497764549` proves the repository-level implementation and executable regression suite are green on exact revision `b46656793a5e1ea7a94e39f2da1506fc73db177e`.

## Remaining evidence gate

The execution-surface behavior itself is not yet proven end-to-end. Before publishing `v0.1.1`, the Principal should append/merge the generated bootstrap into the real ChatGPT `skills-hub` Project Instructions and start a genuinely fresh conversation. The fresh conversation must locate `mattamior/skills-hub`, follow root `AGENTS.md`, load the repository-managed Agnir continuity, and resume Project work without relying on the original initialization conversation.

Until that succeeds, the correct status is:

- repository repair/conformance: **passed**;
- real ChatGPT Project execution-surface activation: **pending user configuration / fresh-context verification**;
- `v0.1.1` publication: **not yet complete**.
