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

## Repository layout

```text
rpm/
├── README.md
├── spec/
│   ├── CORE.md
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
│   └── SESSION.md
└── examples/
    ├── software-project.yaml
    ├── content-project.yaml
    └── mixed-project.yaml
```

## Minimal integration

Each consuming project keeps a manifest at:

```text
.chatgpt/project-memory.yaml
```

At the first substantive turn of a new conversation, the assistant should read that manifest, load the Core memory documents, and then load profile-specific documents only as needed.

If the manifest is missing, the assistant should offer to initialize RPM before substantive project work continues.

## Core memory

Every initialized RPM project maintains:

- `PROJECT_STATE.md` — current authoritative state;
- `NEXT_STEPS.md` — actionable priorities, blockers, and outstanding work;
- `DECISIONS.md` — confirmed durable decisions and rationale;
- `sessions/` — concise checkpoint logs, never raw chat transcripts.

Profiles extend this Core without replacing it.

## Design goals

RPM is designed to be:

- **durable** — important project knowledge survives chat deletion or memory loss;
- **explicit** — project state is inspectable and version controlled;
- **lightweight** — only durable knowledge is persisted;
- **composable** — projects may use more than one profile;
- **lazy** — optional files are created only when they become useful;
- **auditable** — state changes and decisions are traceable through Git history.
