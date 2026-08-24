# RPM — Repository Project Memory

RPM is a repository-backed persistence standard for long-running ChatGPT projects.

Its core principle is simple:

> The repository is the canonical source of truth for durable project knowledge; chat conversations are working memory.

RPM defines:

- a small, stable Core memory layer shared by every project;
- project classification and composable domain profiles;
- a per-project manifest at `.chatgpt/project-memory.yaml`;
- rules for deciding what should and should not be persisted;
- checkpoint and bootstrap behavior for new conversations;
- versioned templates and examples.

## Status

Current specification: **RPM v1.0.0**

The authoritative version is also recorded in the root `VERSION` file.

## Repository layout

```text
rpm/
├── README.md
├── VERSION
├── spec/
│   ├── CORE.md
│   ├── MANIFEST.md
│   ├── CLASSIFICATION.md
│   ├── PERSISTENCE.md
│   ├── BOOTSTRAP.md
│   └── VERSIONING.md
├── profiles/
│   ├── software.md
│   ├── product.md
│   ├── content.md
│   ├── research.md
│   ├── planning.md
│   └── generic.md
├── templates/
│   ├── project-memory.yaml
│   ├── PROJECT_STATE.md
│   ├── NEXT_STEPS.md
│   ├── DECISIONS.md
│   ├── SESSION.md
│   └── PROJECT_INSTRUCTIONS.md
└── examples/
    ├── software-project.yaml
    ├── content-project.yaml
    └── mixed-project.yaml
```

## Core memory

Every initialized RPM project maintains a Core memory layer, normally under `docs/project-memory/`:

- `PROJECT_STATE.md` — current authoritative state;
- `NEXT_STEPS.md` — actionable priorities, blockers, and outstanding work;
- `DECISIONS.md` — confirmed durable decisions and rationale;
- `sessions/` — concise checkpoint logs, never raw chat transcripts.

Profiles extend this Core without replacing it.

## Profiles

RPM v1 includes:

- `software`
- `product`
- `content`
- `research`
- `planning`
- `generic`

A project has one `primary_type` and may activate multiple profiles when each represents a recurring or structurally important mode of work.

## Quick start for a consuming project

### 1. Add the Project Instructions hook

Copy `templates/PROJECT_INSTRUCTIONS.md` into the ChatGPT Project's Project Instructions.

### 2. Start working normally

At the first substantive turn, the assistant checks:

```text
.chatgpt/project-memory.yaml
```

If it does not exist, the assistant offers RPM initialization.

### 3. Initialize RPM

After approval, the assistant should:

1. inspect the repository;
2. classify the project;
3. create the manifest;
4. initialize the Core memory files using actual repository state;
5. create only justified profile-specific artifacts;
6. commit the initialization.

### 4. Continue normally

On later conversations, the assistant loads the manifest, `PROJECT_STATE.md`, and `NEXT_STEPS.md` first, then reads decisions, profile artifacts, and session history only when relevant.

During substantive work, meaningful durable state changes are checkpointed back to the repository according to `spec/PERSISTENCE.md`.

## Design goals

RPM is designed to be:

- **durable** — important project knowledge survives chat deletion or memory loss;
- **explicit** — project state is inspectable and version controlled;
- **lightweight** — only durable knowledge is persisted;
- **composable** — projects may use more than one profile;
- **lazy** — optional files are created only when they become useful;
- **auditable** — state changes and decisions are traceable through Git history.

## Key rule

Do not use RPM to archive conversations. RPM stores durable project knowledge: current state, confirmed decisions, actionable next steps, meaningful findings, and domain-specific artifacts that would be expensive to rediscover.
