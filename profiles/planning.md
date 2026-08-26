# Planning Profile

Version: 2.0.0

Use this profile for implementation plans, migrations, itineraries, business planning, milestones, constraints, budgets, risks, options, and scenario comparison where execution may occur outside the storage system.

Create plan, milestones, risks, options, budget, or equivalent durable artifacts lazily when Core is insufficient. Storage layout is implementation-specific.

Persist confirmed objectives, constraints, milestones, dependencies, risk responses, option decisions, budget assumptions, schedule changes, blockers, and evidence that materially changes the plan.

Plans MUST distinguish Proposed options from Planned commitments and should replace stale current-plan statements rather than accumulating contradictory snapshots.
