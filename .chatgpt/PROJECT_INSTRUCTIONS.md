# PPMP Maintenance ChatGPT Project Instructions

This ChatGPT Project is the maintenance workspace for **PPMP — Persistent Project Memory Protocol** and for **Persistent Project Memory (PPM)**, the reference Skill implementation publicly branded as **Sandminni**.

The authoritative repository is:

`mattamior/rpm`

The repository, not chat history or implicit model memory, is the canonical source of durable PPMP maintenance state.

At the first substantive turn of every new conversation:

1. Access `mattamior/rpm`.
2. Read `.chatgpt/project-memory.yaml` and validate the declared PPMP version.
3. Load `docs/project-memory/PROJECT_STATE.md` and `docs/project-memory/NEXT_STEPS.md`.
4. Read `docs/project-memory/DECISIONS.md` when prior architectural, policy, naming, migration, or maintenance decisions are relevant.
5. Load normative files under `spec/`, `profiles/`, `templates/`, `implementations/`, `backends/`, or `adapters/` only as required by the current task.

Treat this repository as the canonical source of truth for PPMP and PPM maintenance. Chat conversations are working context only.

Do not treat durable state from unrelated ChatGPT Projects or consuming repositories as authoritative PPMP maintenance state. Consuming projects own their project-specific durable state.

When a consuming project reveals a potentially reusable improvement, distinguish between:

- project-specific state or policy, which remains in that consuming repository; and
- a reusable PPMP rule, compatibility issue, PPM behavior, backend/adapter improvement, profile improvement, or specification defect, which may be promoted into `mattamior/rpm` at the appropriate layer.

Do not change normative PPMP behavior only in chat. Confirmed durable changes must be reflected in the appropriate repository files.

Normative PPMP rules belong primarily in `spec/`, `profiles/`, `templates/`, `examples/`, and `VERSION`. PPM implementation behavior belongs in `implementations/`; persistence mechanics in `backends/`; platform lifecycle behavior in `adapters/`.

The self-hosted files under `docs/project-memory/` describe the maintenance state of PPMP/PPM itself. They must not duplicate, override, or silently redefine normative specifications.

Follow `spec/VERSIONING.md` when a normative PPMP change may require a version or migration consideration. Implementation, backend, and adapter changes must preserve their layer boundary and supported PPMP compatibility.

Do not archive raw conversations. Persist only durable state, decisions, next steps, important findings, verification evidence, and information that would be expensive to reconstruct.

When I say “收尾”, “结束”, “先到这里”, “checkpoint”, “save progress”, or equivalent, perform a final **PPM checkpoint** before finishing.
