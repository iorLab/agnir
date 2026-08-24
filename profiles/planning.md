# Planning Profile

Version: 1.0.0

Use this profile for projects whose durable output is primarily a plan, roadmap of actions, migration path, itinerary, operating plan, decision process, or other structured execution framework.

## Optional artifacts

Create lazily when justified:

```text
docs/planning/PLAN.md
docs/planning/MILESTONES.md
docs/planning/CONSTRAINTS.md
docs/planning/OPTIONS.md
docs/planning/RISKS.md
```

### PLAN

Use for the current integrated execution plan. It SHOULD remain current rather than becoming a chronological log.

### MILESTONES

Use when sequencing, dependencies, deadlines, or completion gates matter across multiple stages.

### CONSTRAINTS

Use for durable budget, time, policy, resource, geographic, technical, or other boundaries that govern decisions.

### OPTIONS

Use for important alternatives that require explicit comparison. Once an option is selected, the accepted choice belongs in `DECISIONS.md`; `OPTIONS.md` MAY retain the comparative analysis when it remains useful.

### RISKS

Use for material uncertainties, failure modes, mitigations, and triggers that affect execution.

## Persistence triggers specific to planning

Persist when:

- the plan changes materially;
- milestones or dependencies change;
- a constraint becomes authoritative;
- an option is selected or rejected for durable reasons;
- a material risk or mitigation is identified;
- timing, budget, or resource assumptions change enough to alter execution.

## Planning discipline

Plans MUST distinguish approved actions from possible options. Forecasts and estimates SHOULD include assumptions when those assumptions materially affect decisions.

## Recommended manifest extension

```yaml
extensions:
  planning:
    plan: docs/planning/PLAN.md
    milestones: docs/planning/MILESTONES.md
    constraints: docs/planning/CONSTRAINTS.md
    options: docs/planning/OPTIONS.md
    risks: docs/planning/RISKS.md
```
