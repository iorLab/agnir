# Agnir Brand Process Log

## Record metadata

| Field | Value |
| --- | --- |
| Brand or product | Agnir |
| Record owner | Agnir Project (`iorLab/agnir`) |
| Started | 2026-09-01 |
| Last updated | 2026-09-02 |
| Approval authority | Principal |
| Working branch | `brand/identity-system` |
| Canonical Project ref | `main` — this branch records candidate work until integration |

## Brief

### Audience and positioning

Agnir is a **project-owned durable continuity protocol**. The identity should communicate durable, discoverable pieces of Project truth rather than a chat-history, database, repository-host, or storage-backend product.

Agnir and Svif are independent brands with one visual family language: Agnir represents structure/continuity; Svif represents motion/orchestration around that persistent truth.

### Intended surfaces

Repository/GitHub identity, Skill/distribution identity, documentation, and later favicon/app/social assets only when an approved production master and real surface require them.

### Required languages

- Mark: language-neutral where practical.
- Product name: `Agnir` casing preserved.
- Supporting brand explanation: English + Simplified Chinese.

### Constraints and exclusions

- Preserve the `agnir` tiny-bits/particles metaphor without reducing it to literal dust/debris.
- Preserve platform/storage/execution neutrality.
- Avoid generic AI-memory/database clichés.
- Agnir must remain independently recognizable apart from Svif.
- Production artwork must be vector-native and self-contained.
- Small-size simplification must be an explicitly approved variant, never a silent redraw.
- Similarity review is not legal/trademark clearance.

### Success criteria

The identity should express durable composable truth, remain visibly related to Svif without subordination, preserve neutrality, survive small sizes, and support reproducible derivatives from one locked master.

## Evidence register

| Date | Evidence | Location | What it establishes | Status |
| --- | --- | --- | --- | --- |
| 2026-09-02 | Agnir durable state / active decisions | `.agnir/state.md`, `.agnir/decisions.md` | Current stable release, Project-owned continuity, name meaning, branch governance | Evidence |
| 2026-09-01 | Brand Design System workflow | `mattamior/skills-hub/skills/brand-design-system` | Exploration → approval → master lock → derivatives → visual QA | External process evidence |
| 2026-09-02 | Selected concept direction | conversation exploration boards | 01 + 03 + 05 hybrid, Agnir sand / Svif teal | Principal approval; previews are not masters |
| 2026-09-02 | Direction candidate continuity | `.agnir/evidence/2026-09-02-brand-identity-direction-candidate.md` | Branch-local selected-direction summary | Candidate evidence |
| 2026-09-02 | Deterministic master candidate | `brand/masters/agnir-mark-v0.1.svg` | Fixed particle-A vector geometry | Candidate production evidence |
| 2026-09-02 | Master specification | `brand/masters/MASTER-SPEC-v0.1.md` | Candidate palette, geometry, size rules, remaining gates | Candidate production evidence |
| 2026-09-02 | Master QA candidate | `.agnir/evidence/2026-09-02-brand-master-v0.1-candidate.md` | 64/32/16px rendering result and small-size rationale | Candidate evidence |

## Exploration and decisions

| Date | Direction or decision | Outcome | Rationale | Approver |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Temporary `brand/identity-system` branch | Approved | Isolate brand work from concurrent `main` development | Principal |
| 2026-09-01 | Related but independent Svif/Agnir identity system | Approved | Matches Project architecture and paired naming metaphor | Principal |
| 2026-09-02 | Retain 01 Particle + Motion, 03 S/A Geometry, 05 Flow & Structure | Approved for synthesis | Strongest particle/family/structure directions | Principal |
| 2026-09-02 | Fuse 01 + 03 + 05 | **Selected direction** | Agnir = Structure Layer; Svif = Motion Layer | Principal |
| 2026-09-02 | Agnir sand / Svif teal | **Selected palette direction** | Sand reinforces particle/mineral/structure associations | Principal |
| 2026-09-02 | Generated master-style boards | Accepted for reconstruction, not locked | Visual intent only; no editable production geometry | Principal |
| 2026-09-02 | Deterministic SVG master candidate v0.1 | Created, **not yet approved as locked master** | Converts visual intent into inspectable vector rules | Pending review |
| 2026-09-02 | Separate small-size candidate | Created, **not yet approved** | Full particle field loses clarity at favicon scale | Pending review |

## Approved invariants

### Geometry and proportions

Approved at direction level:

- structured A-shaped geometry;
- A is constructed/revealed through discrete particles rather than a generic solid glyph;
- a central anchor particle is part of the selected language;
- Agnir reads as **Structure Layer / 结构层**;
- shared particle-and-geometry family grammar with Svif.

Candidate v0.1 now fixes one reconstructable particle layout, but those exact coordinates, counts, sizes and A proportions remain pending master approval.

### Palette

Approved direction: sand / warm mineral.

Candidate v0.1 values sampled from the selected concept board:

- Dark Sand `#B27635`;
- Mid Sand `#CD9147`;
- Light Sand `#E7C7A0`.

Exact values remain pending master approval.

### Typography and casing

- `Agnir` casing approved.
- Wordmark typeface/custom lettering and path geometry unresolved.
- Concept-board black sans-serif typography is not a production font decision.

### Small-size behavior

Preliminary QA: the complete particle A reads at repository size but loses structure as the particles approach favicon scale. Current candidate recommends a separate small-size A made from two structural legs plus the central anchor at `32px` and below, with `16px` requiring it. Pending Principal approval.

### Negative space, backgrounds, lockups

Standalone mark + horizontal lockup are intended. Exact clear space, alignment, dark/reverse/monochrome behavior and final lockup ratio remain unresolved.

## Approval checkpoints

| Date | Checkpoint | Decision | Approver |
| --- | --- | --- | --- |
| 2026-09-01 | Brand work isolation | Keep `main` authoritative; develop on temporary branch | Principal |
| 2026-09-02 | Direction selection | 01 + 03 + 05 hybrid | Principal |
| 2026-09-02 | Color direction | Agnir sand, Svif teal | Principal |
| 2026-09-02 | Master-stage entry | Reconstruct production candidates without reopening concept exploration by default | Principal |
| 2026-09-02 | Master v0.1 lock | **Pending** | Principal |

## Inferences and unknowns

| Item | Classification | Follow-up |
| --- | --- | --- |
| Candidate sand values | Candidate, not locked | Review against selected concept board and contrast requirements |
| Exact A/particle geometry | Candidate, not locked | Principal visual review |
| Wordmark construction | Unknown | Select/draw, confirm licensing, pathify |
| Small-size switch rule | Candidate, not locked | Approve or revise after 16/32/64px review |
| Monochrome/reverse behavior | Unknown | Produce and visually QA |
| Trademark/similarity clearance | Unknown | Optional visual risk review; legal clearance separate |

## Next brand-stage work

1. Principal review of deterministic primary and small-size SVG candidates.
2. Revise/freeze geometry and candidate sand values.
3. Build a license-safe pathified wordmark and horizontal lockup candidate.
4. Produce monochrome/reverse variants and render 16/32/64/128/512px QA.
5. Lock the master only after explicit approval; then create `brand-handoff.md` and required derivatives.
6. Before merge, re-resolve latest `main` and reconcile approved brand truth into canonical Agnir continuity as one coherent integration.
