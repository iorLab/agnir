# Project Classification

Version: 1.0.0

## 1. Goal

Classification selects the domain profiles that extend RPM Core. Classification MUST help organize durable knowledge; it MUST NOT force a project into a single rigid category when multiple profiles are genuinely useful.

Each project has:

- `primary_type` — the dominant project mode;
- `profiles` — one or more active domain profiles.

Supported v1 profiles are:

- `generic`
- `software`
- `product`
- `content`
- `research`
- `planning`

## 2. Evidence priority

Determine classification using the following evidence order:

1. **Explicit user statement** — strongest evidence.
2. **Existing manifest configuration** — authoritative until intentionally changed.
3. **Repository structure and durable artifacts**.
4. **README, project instructions, and project description**.
5. **Observed recurring work patterns**.
6. **Model inference** — weakest evidence.

Do not silently override an explicit user classification because the repository contains tooling associated with another profile.

## 3. Typical signals

### software

Signals include source code, dependency manifests, tests, CI workflows, infrastructure configuration, deployment scripts, schema or migration files, and implementation-focused README content.

Typical examples:

```text
src/
app/
tests/
package.json
pyproject.toml
.github/workflows/
wrangler.toml
Dockerfile
migrations/
```

### product

Signals include product requirements, user stories, roadmaps, release plans, product metrics, prioritization artifacts, launch criteria, and cross-functional feature planning.

Typical examples:

```text
PRD/
ROADMAP.md
REQUIREMENTS.md
user-stories/
release-plan/
```

### content

Signals include editorial calendars, drafts, published assets, brand/style rules, content strategy, platform-specific output, campaign planning, and reusable production workflows.

Typical examples:

```text
drafts/
published/
assets/
STYLE_GUIDE.md
CONTENT_STRATEGY.md
TOPIC_BACKLOG.md
```

### research

Signals include research questions, literature or source tracking, evidence synthesis, hypotheses, experiments, findings, and source-quality assessment.

Typical examples:

```text
research/
papers/
references/
SOURCES.md
FINDINGS.md
RESEARCH_QUESTIONS.md
```

### planning

Signals include itineraries, migration plans, business plans, implementation plans, decision matrices, milestones, constraints, budgets, risks, and scenario comparison where execution may happen outside the repository.

Typical examples:

```text
PLAN.md
MILESTONES.md
RISKS.md
OPTIONS.md
BUDGET.md
```

### generic

Use `generic` when no specialized profile clearly adds value, or as a safe temporary classification when evidence is insufficient.

## 4. Multi-profile projects

A project MAY activate multiple profiles when each profile has durable artifacts or recurring work that would otherwise be poorly represented.

Examples:

```yaml
primary_type: software
profiles:
  - software
  - product
```

for a SaaS codebase with substantial PRD and roadmap work, or:

```yaml
primary_type: content
profiles:
  - content
  - research
```

for an editorial project whose output depends on recurring source research.

Do not add profiles merely because a project touches a topic once. A profile SHOULD represent a recurring or structurally important mode of work.

## 5. Initialization decision procedure

When initializing RPM:

1. Inspect existing durable repository evidence.
2. Determine the likely `primary_type`.
3. Add only profiles with clear current value.
4. If classification uncertainty would materially change the structure, ask the user for confirmation.
5. Otherwise initialize conservatively and record the classification in the manifest.

## 6. Reclassification

Classification is mutable. When the nature of a project changes, the manifest MAY be updated.

Reclassification MUST NOT delete useful historical documentation automatically. Obsolete profile artifacts SHOULD be retained, archived, or explicitly migrated as appropriate.

## 7. Classification confidence

Implementations MAY record a classification note or confidence, but MUST NOT present inferred classification as a user-confirmed fact.

When uncertain, prefer a smaller profile set over speculative expansion.
