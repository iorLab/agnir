# v1 real-Project and execution-surface candidate reconnaissance — 2026-09-03

Status: **read-only candidate classification; no downstream Project mutation authorized or performed.**

## Purpose

Turn the open v1 real-Project and execution-surface gates into concrete evidence candidates without manufacturing low-value fixtures or silently modifying unrelated Projects.

## Repository inventory

Accessible `iorLab` repositories observed during reconnaissance:

- `iorLab/agnir` — current product/self-host; not an external real-Project candidate;
- `iorLab/svif` — already qualifying external real Project;
- `iorLab/fishup` — private, substantial repository; existing Agnir Core/profile `0.1` Project;
- `iorLab/VocaPort` — private, substantial Rust/WASM/native application; no `AGNIR.yaml` observed;
- `iorLab/dsh-web-search-custom` — public DSH WebSearchProvider plugin; no `AGNIR.yaml` observed;
- `iorLab/dsh-ui-settings-yaml` — public DSH settings UI plugin; no `AGNIR.yaml` observed;
- `iorLab/imixTV` — private, repository size reported as `0`;
- `iorLab/novo` — private, repository size reported as `0`.

Empty repositories are not suitable for inflating the v1 real-Project count.

## FishUp — preferred next migration candidate

Read-only `iorLab/fishup/main` receipt: `a57b5ec7b679874af08da094fef3e8e7bdee90e3`.

Existing `AGNIR.yaml` declares:

- Core `0.1`;
- profile `repository-filesystem/0.1`;
- Project identity `urn:agnir:project:fishup`;
- canonical repository `iorLab/fishup`;
- authoritative ref `main`;
- operational Agnir release `0.1.1`;
- applied revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`.

FishUp is materially different from Agnir/Svif: it is a Vite + TypeScript + three.js + Rapier3D game with Cloudflare Workers + Static Assets deployment, D1-backed APIs, automatic deployment from main, extensive game/content state, and existing Project-specific Agent instructions. Its `AGENTS.md` is already locator-oriented and retains unrelated FishUp rules.

This makes FishUp a strong second published `v0.1.1` -> published `v0.2.0` real migration candidate. A future authorized migration should preserve Project identity, durable locators/content, FishUp product/deployment state, existing README/AGENTS instructions and unrelated decisions; use a temporary migration lineage plus target-owned main reconciliation.

No FishUp writes were performed by this reconnaissance.

## VocaPort — preferred fresh-install candidate

No `AGNIR.yaml` was found on `iorLab/VocaPort/main` during explicit file lookup.

VocaPort is materially different from the existing evidence set:

- Rust business/runtime crates;
- Rust/WASM Web runtime;
- Rust native Desktop runtime;
- Android/Desktop release automation;
- durable interrupted-session snapshots in the product itself;
- GitHub Release / Pages distribution;
- existing bilingual `README.*` and `AGENTS.*` documents.

Its root `AGENTS.md` already contains critical Project-owned rules: Rust owns business logic; Rust/TypeScript bridge contracts stay synchronized; generated Android output is not hand-maintained; Android regressions require fresh `adb logcat`; formal docs remain bilingual.

That pre-existing instruction surface makes VocaPort a useful non-destructive fresh Agnir `v0.2.0` bootstrap test: successful installation must add only the Agnir activation/instruction entry while preserving these existing rules and documentation organization.

No VocaPort writes were performed by this reconnaissance.

## DSH repositories — useful context, not surface evidence by themselves

`iorLab/dsh-web-search-custom` is a pluggable DeepSeek Harness WebSearchProvider. It registers a search provider and settings schema, calls OpenAI-compatible Responses API gateways with server-side native `web_search`, and maps results into DSH's search contract.

`iorLab/dsh-ui-settings-yaml` is a DeepSeek Harness configuration UI for selected `settings.yaml` values. Its README explicitly states: **there is no model-visible surface**; it does not produce messages, tool calls, session events, or model-observable input.

Therefore these repository identities must not be counted as a second Agnir execution surface merely because they integrate with DSH. To satisfy the v1 surface gate, DSH (or another materially distinct Agent environment) must actually activate, load, operate, checkpoint and fresh-resume a real Agnir Project without predecessor-private context.

The DSH repositories themselves currently have no `AGNIR.yaml` from explicit file lookup and were not modified.

## Recommended evidence sequence

1. After explicit Principal authorization naming `iorLab/fishup`, run the published `v0.1.1` -> `v0.2.0` migration as a separate real Project validation.
2. After explicit Principal authorization naming `iorLab/VocaPort`, run a fresh stable `v0.2.0` non-destructive installation/activation and cold-start resume test.
3. Use one explicitly authorized real Agnir Project from a genuinely distinct Agent environment such as DSH to obtain the second execution-surface/adapter receipt. The environment must operate the Project; affiliation with a DSH plugin is insufficient.
4. Keep mount-boundary and independent-implementation evidence as separate gates rather than trying to make one repository exercise prove everything.

This sequence would, if successful, raise the external real-Project set from one qualifying Project (Svif) to three (Svif + FishUp + VocaPort) while keeping the execution-surface gate independently honest.
