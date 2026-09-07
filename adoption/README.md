# Agnir Launch and Adoption Strategy

Status: **Principal-approved**  
Applies to: Agnir post-`v1.0.0` adoption and public launch work  
Canonical product category: **Project Continuity**

## Purpose

Agnir `v1.0.0` is already a published and independently verified stable release. The next product problem is not proving that the protocol can exist; it is proving that people with no founding-context knowledge can understand it, install it, resume real Projects with it, and keep using it.

The launch strategy therefore optimizes first for **external adoption evidence**, not raw attention.

North-star outcome:

> A Project that is not controlled by the Agnir maintainers is successfully resumed by a fresh compatible Executor using Project-owned Agnir continuity.

## Positioning

### Category

Agnir should lead with **Project Continuity**, not “AI memory” or “agent memory”.

Canonical positioning:

> **Agnir is project-owned durable continuity.**

Supporting principle:

> **The Project persists; Executors come and go.**

Agnir may use search/discovery terms such as `agent-memory`, `project-memory`, `coding-agents`, or `context-engineering` where useful for discoverability, but those terms must not redefine the product category or Core boundary.

### Problem statement

The first user-facing problem is simple:

> AI sessions forget. Projects should not.

The product promise is that changing session, Agent, execution surface, machine, or work context does not require the human to reconstruct the Project's durable truth from private chat history.

### Messaging hierarchy

Use messaging in this order:

1. **Pain** — fresh sessions lose durable context.
2. **Outcome** — a fresh Executor can continue the Project.
3. **Ownership** — continuity belongs to the Project, not a specific AI product.
4. **Mechanism** — State, Next Actions, Decisions, and Evidence are discoverable and durable.
5. **Credibility** — stable specification, conformance, independent implementation, compatibility, lineage and failure semantics.

Do not lead first-time users with protocol vocabulary such as lineage selectors, reconciliation, mount boundaries, or compatibility promotion unless the audience is explicitly technical.

## Core public messages

Primary working lines:

> **Your agent forgets. Your project shouldn't.**

> **New session. Same project continuity.**

> **Switch agents, not projects.**

> **Your project continuity shouldn't belong to your AI tool.**

These are working public messages, not Core normative language. Public copy may evolve without changing Agnir protocol semantics.

## First audiences

### 1. AI coding power users

Primary first audience.

Typical pain:

- starting a fresh coding session and losing context;
- repeatedly re-explaining Project state;
- switching among Codex, Claude Code, Cursor, ChatGPT, IDEs, or other execution surfaces;
- resuming multi-day work;
- agents repeatedly scanning the repository to infer what happened.

Message:

> **Stop re-explaining your Project to every new AI session.**

Desired first experience:

```text
install once
→ do real Project work
→ checkpoint
→ end the session
→ open a fresh context
→ continue
```

### 2. Agent / IDE / developer-tool builders

Message:

> **Agnir is not another memory database. It is a portable Project continuity contract.**

For this audience, explain storage neutrality, execution-surface neutrality, Project identity, logical Continuity Lineage, checkpoints, failure semantics, conformance, and independent implementation.

### 3. Agent infrastructure / interoperability audiences

Longer-term discussion:

> Should durable Project continuity be an interoperability layer rather than private state owned by each execution surface?

This is a later category-development conversation, not the first adoption pitch.

## Demo strategy

### Demo 1 — fresh-session recovery

This is the primary 30-second demo.

Without Agnir:

```text
Session A
User: implement feature X
Agent: ...work...
User: stop here

Fresh Session B
User: continue
Agent: what were we working on?
```

With Agnir:

```text
Session A
User: implement feature X
Agent: ...work...
User: checkpoint

Fresh Session B
User: continue
Agent:
  Current state: implementation complete
  Next action: add failure-path tests
  Decision: preserve API compatibility
  Continuing...
```

Close with:

> **New session. Same Project continuity.**

### Demo 2 — cross-Executor / cross-surface continuation

Demonstrate one compatible execution surface checkpointing a Project and a different fresh surface resuming it.

The point is not that Agnir belongs to either product. The point is that **the Project owns continuity**.

### Demo 3 — protocol depth

Only after the basic value is understood, demonstrate deeper behavior such as:

- parallel Continuity Lineages;
- branch/worktree reconciliation;
- storage or mount relocation;
- explicit compatibility promotion;
- negative discovery/failure behavior;
- independent implementation from public documentation.

These demos establish technical credibility; they should not be the first marketing experience.

## Launch sequence

### Wave 0 — launch hygiene

Before sending meaningful external traffic, make the landing surface complete:

- set a concise GitHub repository description;
- add useful GitHub topics for discovery;
- confirm license presentation and public contribution expectations;
- provide an obvious feedback/discussion path;
- ensure README first-screen messaging states the problem and outcome quickly;
- prepare a canonical 30-second fresh-session demo;
- prepare a stable social preview / share image using the approved brand system;
- ensure installation remains copy-ready and points to an actually published stable release.

Repository-host metadata is convenience/discovery infrastructure, not canonical Project truth.

### Wave 1 — design-user adoption

Goal: obtain the first set of genuinely external usage evidence.

Target:

- 10 Projects not controlled by the Agnir maintainers successfully initialized;
- observe whether users understand the category from the landing page;
- verify one-line installation;
- verify fresh-session continuation;
- record friction without coaching users through hidden founding context.

For each design user, answer:

1. Could they understand what Agnir is from the repository?
2. Did installation succeed from the public procedure?
3. Did the second fresh session produce obvious value?
4. What did they misunderstand, skip, or have to repair?
5. Did they keep Agnir after the first test?

Fix public product/documentation defects exposed by these cases rather than teaching users undocumented answers.

### Wave 2 — technical launch

After Wave 1 produces credible external evidence, publish a technical launch suitable for communities such as Hacker News and developer forums.

Recommended framing:

> **Show HN: Agnir — Project-owned continuity for AI coding agents**

Lead with the continuity problem and fresh-session demo. Explain protocol depth only after the basic user value.

A strong technical story is the independent-implementation challenge:

> We gave a fresh implementation only Agnir's public repository and asked it to reconstruct the behavior.

The important narrative is not “many tests”; it is that documentation and contracts were repeatedly tightened until an independent implementation could succeed without founding-chat knowledge.

### Wave 3 — broader developer launch

Once real cases exist, expand into wider developer channels such as X, Reddit, LinkedIn, long-form technical writing, video, Chinese developer communities, or Product Hunt.

Prefer case-backed claims:

> A fresh Executor resumed a real Project from Project-owned continuity.

over creator-centric claims:

> We built a new memory tool.

## Content strategy

Agnir content should teach the problem space more often than it advertises the product.

Working mix:

- **50% problem education**
- **30% demos / evidence / case studies**
- **20% direct Agnir product communication**

Useful topics include:

- Why `AGENTS.md` is not Project memory.
- Why chat history is the wrong authority for Project state.
- Persistent memory vs Project continuity.
- What should survive when an AI coding session ends?
- Why a commit SHA is a receipt rather than Project identity.
- What happens when two AI coding contexts work on parallel branches?
- Why tool-owned memory creates switching costs.
- How to test whether “fresh-session recovery” is actually independent.

## Adoption metrics

### North-star metric

**Successful external cold-start resumes.**

A qualifying success should involve a Project outside direct maintainer control and a fresh compatible Executor recovering the durable truth needed to continue without predecessor-private conversational context.

### Early evidence targets

Initial targets:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the release gate.

These are adoption targets, not protocol conformance requirements and not release gates.

### Secondary signals

Track, but do not optimize the first stage around:

- GitHub stars;
- forks;
- social impressions;
- repository traffic;
- mentions.

A smaller number of repeated real resumes is stronger evidence than a larger number of passive stars.

## Evidence policy

Adoption evidence should remain materially useful and privacy-conscious.

Record evidence when it expands confidence about a real adoption dimension, for example:

- first fresh-session resume outside maintainer control;
- first cross-Executor resume;
- first new execution surface;
- first long-running Project;
- first independently built integration;
- first meaningful documentation failure discovered through adoption.

Do not turn every installation into Project memory noise. Do not reopen satisfied release gates unless adoption exposes a real protocol, compatibility, conformance, packaging, or documentation defect.

## Brand and adoption boundary

`brand/` remains the authority for Agnir's approved identity system, visual masters, exports, QA, and downstream visual-use rules.

`adoption/` owns launch, positioning, adoption, demo, community, and case-study strategy.

Adoption materials may consume canonical brand assets, but they do not redefine the brand masters or Agnir Core semantics.

## Near-term execution order

1. Complete GitHub About metadata using repository-admin authority.
2. Make launch/feedback surfaces complete enough for strangers.
3. Produce the canonical 30-second fresh-session demo.
4. Recruit the first small group of external design users.
5. Capture genuine fresh-session and cross-Executor adoption evidence.
6. Refine public messaging from observed confusion.
7. Run the technical launch only after external proof exists.
8. Broaden distribution after repeat usage and case studies emerge.

## Guardrails

- Do not position Agnir as a proprietary memory database.
- Do not imply that Git, GitHub, ChatGPT, Codex, Claude, Cursor, or any other execution surface is a Core dependency.
- Do not claim adoption, retention, interoperability, or performance numbers that have not been observed.
- Do not treat stars as the primary proof of product value.
- Do not let marketing copy silently change protocol semantics.
- Do not use internal/founding context to rescue an adoption test that is supposed to validate public sufficiency.
- Keep Svif adoption and Svif product execution in Svif's own canonical Project continuity.

## Strategy review trigger

Revisit this strategy when evidence shows one of the following:

- users consistently misunderstand the “Project Continuity” category;
- installation succeeds but second-session value is weak;
- adoption concentrates on a use case materially different from the current target;
- a new integration surface changes distribution economics;
- external implementation evidence reveals a better interoperability story;
- the Project deliberately changes its post-1.0 product direction.

Until then, the default strategy is:

```text
Project Continuity
→ fresh-session value
→ external adoption evidence
→ technical credibility
→ broader distribution
```
