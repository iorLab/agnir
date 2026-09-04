# VocaPort DSH cross-Agent execution-surface validation

Date: 2026-09-04

## Purpose

This evidence records external acceptance of a real second Agnir Agent execution surface using `iorLab/VocaPort` and DSH. The goal was not to count another repository or product runtime; it was to prove that a materially distinct Agent environment can activate, load, continue, checkpoint, and freshly resume an Agnir Project using only Project-owned continuity, without predecessor-private chat/session memory.

The existing primary Agnir operating path is the ChatGPT/GitHub-connected Agent environment used for canonical Agnir/Svif/VocaPort work. DSH is a materially distinct Agent execution environment. GitHub Actions and VocaPort Web/Desktop/Android runtimes are not counted as separate Agent execution surfaces.

## Project and isolated validation lineage

Canonical VocaPort authoritative main remained:

- `refs/heads/main` -> `eb9a3cca54d6e5daa80fbacc72624a735057328b`;
- Project identity `urn:agnir:project:vocaport`;
- authoritative lineage `urn:vocaport:lineage:authoritative`.

The DSH experiment used an isolated validation lineage and selector:

- branch `validation/dsh-execution-surface-v0.2.0`;
- protocol baseline `439866051d7b9863565540fb592f408de64c1081`;
- logical lineage `urn:vocaport:lineage:dsh-execution-surface-validation`;
- selector `refs/heads/validation/dsh-execution-surface-v0.2.0`;
- Core/profile `0.2` / `repository-filesystem/0.2`.

The validation lineage was never merged into authoritative VocaPort continuity and `main` was not advanced by this experiment.

## Environment preflight and excluded first attempt

An initial DSH attempt was rejected as invalid evidence because the local clone was stale/different from the canonical GitHub state and SSH transport was unavailable. It did not operate on the prepared validation lineage and its local checkpoint never reached canonical GitHub.

A separate Git transport preflight then proved:

- canonical HTTPS repository `https://github.com/iorLab/VocaPort.git` was reachable;
- `gh` authentication had repository write capability;
- SSH on port 22 remained unavailable in that environment;
- the prepared remote validation branch existed at exact protocol baseline `439866051d7b9863565540fb592f408de64c1081`;
- DSH synchronized its local worktree to that exact remote content before the accepted experiment began.

The invalid attempt is not counted as Session 1 and does not contribute to the surface gate.

## Accepted Session 1 — fresh activation, real work, checkpoint

A genuinely fresh DSH session began from exact canonical branch head:

- start `439866051d7b9863565540fb592f408de64c1081`.

Without predecessor-private session context it followed repository-owned entry points and loaded:

- `AGENTS.md`;
- the `README.md` Agnir Project Instructions section;
- `AGNIR.yaml`;
- `.agnir/state.md`;
- `.agnir/next-actions.md`;
- `.agnir/decisions.md`;
- relevant Project-owned Evidence.

It independently recovered:

- Project identity `urn:agnir:project:vocaport`;
- Core/profile `0.2` / `repository-filesystem/0.2`;
- logical lineage `urn:vocaport:lineage:dsh-execution-surface-validation`;
- selector `refs/heads/validation/dsh-execution-surface-v0.2.0`.

The Project-owned Next Action required a low-risk real observation task: determine the clean-environment prerequisites and repository steps required before root `pnpm typecheck` can succeed, without modifying product files.

Session 1 created and pushed:

- initial checkpoint `b4f87d3ebd86d647adc2b7b101498ca4c80e6287` — `checkpoint: record DSH execution-surface Session 1`.

Only `.agnir/` continuity/evidence files changed.

## External review correction preserved as auditable continuity

External evidence review found a material error in the first observation conclusion: Session 1 had inferred that root `pnpm typecheck` did not require the generated Web WASM module / Rust-WASM generation stack.

The same Session 1 was instructed to re-investigate safely rather than rewrite history. A controlled reversible test moved ignored generated `apps/web/src/wasm/pkg/` outside the repository, ran typecheck, restored it exactly, and reran typecheck:

- generated WASM absent -> `pnpm typecheck` failed exit 2 with `apps/web` TS2307 for `./wasm/pkg/vocaport_web_runtime`;
- generated WASM restored -> `pnpm typecheck` passed exit 0;
- no tracked product file changed.

The correct clean-environment sequence therefore includes Node + `pnpm@11.7.0`, Rust stable + `wasm32-unknown-unknown`, `wasm-bindgen-cli@0.2.126`, `pnpm install`, `scripts/build-web-wasm.sh`, then root `pnpm typecheck`.

The incorrect result was retained and explicitly marked superseded; it was not squashed away. The correction was committed and pushed as a descendant:

- final Session 1 checkpoint `29549ebf45071003ae3e885664c7c9e960d838eb` — `checkpoint: correct Session 1 typecheck prerequisite (external review)`;
- parent/merge-base remained `b4f87d3ebd86d647adc2b7b101498ca4c80e6287`;
- correction diff changed only `.agnir/evidence/2026-09-04-dsh-session-1.md` and `.agnir/state.md`.

This correction demonstrates that Project-owned continuity can preserve an auditable supersession trail instead of silently rewriting an erroneous observation. The observation mistake was not an Agnir Core/discovery/resume defect.

## Accepted Session 2 — genuinely fresh resume

Session 1 was closed. A genuinely new DSH session received no Session 1 chat/transcript/private Agent memory.

It independently queried canonical HTTPS GitHub and discovered the current validation branch tip:

- Session 2 start `29549ebf45071003ae3e885664c7c9e960d838eb`.

From repository-owned instructions, continuity files, Project Evidence, and git history only, Session 2 correctly recovered:

- Project identity `urn:agnir:project:vocaport`;
- Core/profile `0.2` / `repository-filesystem/0.2`;
- logical lineage `urn:vocaport:lineage:dsh-execution-surface-validation`;
- selector `refs/heads/validation/dsh-execution-surface-v0.2.0`;
- protocol baseline `439866051d7b9863565540fb592f408de64c1081`;
- initial Session 1 checkpoint `b4f87d3ebd86d647adc2b7b101498ca4c80e6287`;
- corrected final Session 1 checkpoint `29549ebf45071003ae3e885664c7c9e960d838eb`;
- the corrected clean-environment typecheck prerequisites;
- that the earlier no-WASM conclusion was explicitly superseded.

It then followed the repository-owned Session 2 Next Action, recorded `.agnir/evidence/2026-09-04-dsh-session-2-resume.md`, updated State/Next, committed, and pushed:

- Session 2 checkpoint `af9b9c0b725ae40d11e462f11e3a9392afed6d8a` — `checkpoint: record DSH execution-surface Session 2 resume`.

Canonical remote verification confirmed the validation branch tip equals `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`.

## External Git receipt review

External review independently confirmed:

- validation branch remote tip `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`;
- canonical VocaPort `main` remained `eb9a3cca54d6e5daa80fbacc72624a735057328b`;
- `29549eb... -> af9b9c0...` is one descendant commit touching only:
  - `.agnir/evidence/2026-09-04-dsh-session-2-resume.md`;
  - `.agnir/state.md`;
  - `.agnir/next-actions.md`;
- the full experiment diff `439866051... -> af9b9c0...` contains only four `.agnir/` paths:
  - `.agnir/evidence/2026-09-04-dsh-session-1.md`;
  - `.agnir/evidence/2026-09-04-dsh-session-2-resume.md`;
  - `.agnir/state.md`;
  - `.agnir/next-actions.md`;
- no VocaPort product source/config/docs/release workflow changed;
- validation continuity was not published as authoritative main truth.

## v1 gate decision

**Accepted: the >=2 materially different execution surfaces/adapters gate is satisfied.**

DSH provides a real second Agent execution surface because it independently performed fresh activation, loaded State/Next/Decisions/Evidence, completed real Project work, checkpointed and pushed, then in a genuinely fresh second session recovered the corrected predecessor checkpoint and current Project truth without predecessor-private context.

This acceptance does **not** claim:

- a new storage/backend profile;
- genuine mount-boundary behavior;
- independent-implementation documentation quality;
- that GitHub Actions or VocaPort product runtimes are separate Agnir execution surfaces.

Those gates remain separate. No Agnir Core/profile `0.2` semantic defect was exposed by the accepted DSH experiment.
