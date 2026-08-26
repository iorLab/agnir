# Project Classification

Version: 2.0.0

Classification selects composable domain profiles that extend iorMemory Core. It MUST organize durable knowledge without forcing a Project into a rigid single category.

Each Project has a `primary_type` and one or more active `profiles`.

Supported v2 profiles are `generic`, `software`, `product`, `content`, `research`, and `planning`.

## Evidence priority

Use explicit user statements first, then existing durable configuration, current project artifacts/structure, project documentation, observed recurring work patterns, and finally model inference. Do not silently override an explicit classification based on weaker signals.

## Profile signals

- **software** — source code, systems, infrastructure, tests, deployment, schemas, implementation.
- **product** — requirements, user stories, roadmap, metrics, prioritization, launch planning.
- **content** — editorial output, drafts, style rules, content strategy, campaigns.
- **research** — questions, sources, hypotheses, evidence synthesis, experiments, findings.
- **planning** — plans, milestones, constraints, risks, budgets, options, scenarios.
- **generic** — no specialized profile clearly adds durable value yet.

A Project MAY activate multiple profiles when each represents recurring or structurally important work. Prefer a smaller profile set over speculative expansion.

Classification is mutable. Reclassification MUST preserve useful durable knowledge and MUST NOT delete historical artifacts automatically.
