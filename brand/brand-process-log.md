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
| Canonical Project ref | `main` (brand branch records candidate work until integration) |

## Brief

### Audience and positioning

Agnir is a **project-owned durable continuity protocol**. Durable Project continuity belongs to the Project rather than to an Executor, conversation, execution environment, repository host, VCS, storage mechanism, Agent, or Skill.

The brand should communicate durable, discoverable pieces of Project truth and continuity across changing Executors/environments. It should feel precise, composable, dependable, and infrastructure-oriented rather than like a chat-history or note-taking product.

Agnir and Svif are independent Projects with a deliberate brand relationship. Agnir represents the small durable pieces of Project truth; Svif represents motion/orchestration around that persistent continuity. Their identities should be visibly related without making Agnir look subordinate to Svif.

### Intended surfaces

- repository / GitHub identity;
- Skill/distribution identity where a visual mark is useful;
- documentation and README branding;
- favicon/application icons when an actual surface requires them;
- social/share assets only when an actual surface references them.

Production integration into shared `main` surfaces remains deferred until production masters and visual QA are complete.

### Required languages

- Brand mark: language-neutral where practical.
- Wordmark/product name: `Agnir` casing preserved.
- Supporting brand explanation: English and Simplified Chinese.

### Constraints and exclusions

- Preserve the established meaning of `Agnir`: Icelandic `agnir`, nominative plural of `ögn`, meaning tiny bits/particles. The product metaphor is discoverable pieces of durable Project truth, not literal dust/debris.
- Preserve protocol neutrality: do not visually bind Agnir to Git, GitHub, ChatGPT, a filesystem layout, storage backend, or another replaceable implementation/execution environment.
- Avoid generic AI clichés such as sparkle/starburst, chatbot bubble, robot head, neural-brain icon, generic database cylinder, or ungrounded “AI memory”.
- Agnir must remain independently recognizable and usable apart from Svif.
- Favor vector-native geometry suitable for editable production SVG.
- Small-size simplification, if needed, must be an explicitly approved variant rather than an untracked redraw.
- Similarity review is not legal/trademark clearance.

### Success criteria

1. Express durable, composable, discoverable Project truth without reducing the idea to “database” or “chat memory”.
2. Maintain a visible family relationship with Svif while remaining independently recognizable.
3. Preserve platform/storage/execution neutrality.
4. Support vector masters and robust monochrome/contrast variants.
5. Remain recognizable at repository/distribution-icon sizes.
6. Permit derivatives to be generated from approved masters without independent redraws.

## Evidence register

| Date | Evidence | Location | What it establishes | Status |
| --- | --- | --- | --- | --- |
| 2026-09-02 | Agnir current durable state | `.agnir/state.md` | Current stable `v0.1.1`, neutrality and repository invariants | Evidence |
| 2026-09-02 | Agnir active decisions | `.agnir/decisions.md` | Project-owned continuity boundary, name meaning, Svif relationship and branch governance | Evidence |
| 2026-09-01 | Existing-brand asset search | repository `main` | No existing production logo system was found | Evidence |
| 2026-09-01 | Brand Design System workflow | `mattamior/skills-hub/skills/brand-design-system` | Exploration → approval → master lock → derivatives → visual QA | External process evidence |
| 2026-09-02 | Selected identity direction | conversation-generated exploration boards | Principal selected the 01/03/05 hybrid direction and current family palette for refinement | Approval evidence; previews are not production masters |
| 2026-09-02 | Candidate continuity record | `.agnir/evidence/2026-09-02-brand-identity-direction-candidate.md` | Branch-local durable summary and integration rule | Candidate evidence |

## Exploration and decisions

| Date | Direction or decision | Outcome | Rationale | Approver |
| --- | --- | --- | --- | --- |
| 2026-09-01 | Use temporary `brand/identity-system` branch | Approved | Isolates identity work from concurrent `main` development | Principal |
| 2026-09-01 | Design Svif and Agnir as a related brand family with separate canonical assets | Approved | Matches independent-project architecture and deliberate naming metaphor | Principal |
| 2026-09-01 | Keep exploration separate from production integration | Approved working rule | Prevents unapproved concepts from leaking into production surfaces | Principal |
| 2026-09-02 | Retain directions 01 Particle + Motion, 03 S/A Geometry, and 05 Flow & Structure | Approved for synthesis | These directions best expressed particles, family geometry and structure | Principal |
| 2026-09-02 | Fuse 01 + 03 + 05 into one family direction | **Selected direction** | Agnir becomes the structure layer; Svif the motion layer; both share particle-and-geometry language | Principal |
| 2026-09-02 | Agnir uses a sand family; Svif uses the former Agnir teal family | **Selected palette direction** | Sand reinforces particle/mineral/structure associations while teal carries motion for Svif | Principal |
| 2026-09-02 | Generated master-style boards | Direction accepted for refinement, **not production master lock** | Generated previews establish intent, not editable vector geometry or exact production values | Principal |

## Selected direction invariants

### Geometry and proportions

Direction-level invariants now approved:

- Agnir mark is based on a structured **A-shaped geometry**.
- The A is constructed/revealed through a field of discrete particles rather than treated as a generic solid letter alone.
- A central/anchoring particle is part of the current selected visual language.
- Agnir must read as the **Structure Layer** of the family.
- Agnir and Svif share a particle-and-geometry grammar but remain independently recognizable.

Not yet locked: exact A angle, aperture/negative-space geometry, particle counts, particle size sequence, particle positions, construction grid, clear space, lockup ratio, and small-size simplification.

### Palette

Direction-level palette:

- **Agnir: sand / warm mineral family**.
- **Svif: teal / turquoise family**.

Exact HEX/RGB values, contrast variants and monochrome rules are not yet locked.

### Typography and casing

- `Agnir` casing is approved.
- Current black sans-serif wordmark treatment is a preview convention only.
- Typeface/custom lettering and final path geometry are not yet approved.

### Negative space and backgrounds

- The A structure and particle field must remain legible on clean light/dark backgrounds.
- Exact negative-space, reverse and transparency behavior remains to be defined and QA-tested.

### Lockups and spacing

- Standalone mark and mark + `Agnir` lockup are intended production roles.
- Exact alignment, spacing and clear-space rules remain to be defined.

## Approval checkpoints

| Date | Checkpoint | Decision | Approver |
| --- | --- | --- | --- |
| 2026-09-01 | Brand work isolation | Work on temporary brand branch; keep `main` authoritative | Principal |
| 2026-09-01 | Brand-family scope | Related but independent Svif/Agnir identities | Principal |
| 2026-09-02 | Direction selection | 01 + 03 + 05 hybrid selected | Principal |
| 2026-09-02 | Color direction | Agnir sand, Svif teal | Principal |
| 2026-09-02 | Master-stage entry | Proceed to production-master reconstruction without reopening concept exploration by default | Principal |

## Inferences and unknowns

| Item | Classification | Follow-up |
| --- | --- | --- |
| Exact sand palette values | Unknown | Establish production HEX/RGB values and accessible contrast variants |
| Exact A geometry | Unknown | Reconstruct as deterministic editable vector geometry |
| Particle system parameters | Unknown | Define count/scale/spacing rules; test small sizes |
| Wordmark construction/typeface | Unknown | Select or draw; record licensing; pathify if appropriate |
| Small-size mark | Unknown | Test 16/32/64 px and explicitly approve simplification if necessary |
| Trademark/similarity clearance | Unknown | Optional visual similarity review; legal clearance remains separate |

## Next brand-stage work

1. Reconstruct the selected Agnir mark as an editable SVG production candidate.
2. Freeze exact sand values and monochrome/reverse behavior.
3. Define particle geometry and construction rules shared with Svif where appropriate.
4. Build standalone mark and horizontal lockup candidates.
5. Render and inspect 16/32/64/128/512 px outputs.
6. After explicit master approval, create `brand-handoff.md` and only the production derivatives required by actual surfaces.
7. Before merging, re-resolve latest `main`, reconcile material brand outcomes into canonical Agnir Decisions/State/Next Actions as appropriate, then integrate brand assets and continuity coherently.
