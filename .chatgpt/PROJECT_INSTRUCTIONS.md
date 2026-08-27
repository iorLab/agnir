This ChatGPT Project maintains PPMP and its reference implementation PPM, publicly branded as Sandminni.

Canonical repository: `mattamior/rpm`

At the first substantive turn of every new conversation:
1. Read `.chatgpt/project-memory.yaml`.
2. Load `docs/project-memory/PROJECT_STATE.md` and `NEXT_STEPS.md`.
3. Read `DECISIONS.md` and relevant files under `spec/`, `profiles/`, `templates/`, `implementations/`, `backends/`, or `adapters/` only when needed.

Treat the repository as the source of truth; chat is working context only.

Keep PPMP protocol rules, PPM implementation behavior, backend behavior, adapter behavior, and project-specific state in their proper layers.

Do not persist raw conversations. Persist only durable state, decisions, next steps, important findings, and verification evidence.

When I say “收尾”, “结束”, “先到这里”, “checkpoint”, or equivalent, perform a PPM checkpoint before finishing.
