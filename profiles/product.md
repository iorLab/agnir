# Product Profile

Version: 1.0.0

Use this profile when durable project work includes product definition, requirements, prioritization, release planning, user outcomes, or roadmap management.

## Optional artifacts

Create lazily when justified:

```text
docs/product/PRD/
docs/product/ROADMAP.md
docs/product/REQUIREMENTS.md
docs/product/RELEASE_PLAN.md
docs/product/METRICS.md
```

### PRD

Use PRDs for substantial features or product capabilities with durable goals, scope, user value, constraints, and acceptance criteria.

### ROADMAP

Maintain a roadmap only when sequencing across multiple milestones or releases matters. It MUST distinguish committed work from exploratory ideas.

### REQUIREMENTS

Use when durable functional, non-functional, compliance, compatibility, or operational requirements need a canonical home.

### RELEASE_PLAN

Use when launch criteria, rollout sequencing, dependencies, rollback conditions, or release coordination have durable value.

### METRICS

Use when project success is governed by explicit measures. Record definitions and interpretation, not just transient numbers.

## Persistence triggers specific to product work

Persist when:

- scope is accepted or materially changed;
- a requirement becomes authoritative;
- prioritization changes materially;
- a release milestone or launch criterion is confirmed;
- a product trade-off is accepted;
- a user or business constraint changes planned work;
- roadmap sequencing changes.

## Decision discipline

Product ideas remain Proposed until explicitly accepted. Do not silently promote brainstorming output into committed scope.

## Recommended manifest extension

```yaml
extensions:
  product:
    prd: docs/product/PRD
    roadmap: docs/product/ROADMAP.md
    requirements: docs/product/REQUIREMENTS.md
    release_plan: docs/product/RELEASE_PLAN.md
    metrics: docs/product/METRICS.md
```
