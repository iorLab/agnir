# Agnir Current State

Durable continuity belongs to the Project.

## Stable release and active patch candidate

Agnir `v1.0.0` remains **published, independently verified, and the latest stable release**. Its immutable tag remains at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`; accepted `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

Repository/distribution `1.0.1` is now an **implemented, conformance-green patch candidate** on PR #50 / `release/v1.0.1-activation-hardening`. It is not yet published and does not replace `v1.0.0` as latest stable.

The `1.0.1` candidate changes activation/packaging reliability only:

- Core remains `1.0`;
- repository/filesystem remains `repository-filesystem/1.0`;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- root `AGNIR.md` is the canonical Executor-facing Project activation + operation surface;
- `AGENTS.md` remains locator-only and points directly to `AGNIR.md`;
- README `Agnir Project Instructions` remains a backward-compatible locator for pre-upgrade `1.0.0` Projects, not a second procedure copy;
- the legacy `AGENTS.md -> README` activation route remains accepted only so an existing `1.0.0` Project can activate before compatible upgrade/repair;
- repository-context `commit` / `提交` / `提交代码` dispatches checkpoint evaluation before commit;
- `commit and push` / `提交推送` adds push + destination-ref verification;
- checkpoint evaluation is mandatory at the boundary, but unchanged durable truth remains a valid no-op and does not require artificial `.agnir/` mutation;
- Project-defined pre-commit verification remains Project policy, not Agnir Core semantics.

Exact pre-checkpoint candidate validation:

- candidate head: `ea254e09b999dde8024a76d32e55d5d5fe5868d6`;
- PR: #50;
- workflow: `34254831971`;
- repository job: `102157842277`;
- result: **success**;
- self-host, Core 0.1 regression, Core 0.2 surfaces, Core 1.0 stability/discovery/promotion, stable package gates, and full conformance suite all passed;
- all publication jobs, including `Publish v1.0.1 stable release`, were correctly skipped.

`VERSION` and `AGNIR.yaml extensions.agnir/release.repository_version` both declare repository source package `1.0.1`. `AGNIR.yaml` still declares Core `1.0`, `repository-filesystem/1.0`, authoritative Project identity/lineage, and `latest_stable: "v1.0.0"`. The `agnir/operations` applied stable package remains `1.0.0` until an actual `v1.0.1` stable publication is accepted.

## Publication boundary

Implementation, PR acceptance, or merge does not publish `v1.0.1`.

The dormant main-only publication job is armed only by exact authoritative-main commit intent `release: publish v1.0.1 stable`. It re-verifies exact source and full conformance before creating/validating `v1.0.1`, verifies `releases/latest == v1.0.1`, and verifies immutable `v1.0.0` / `v1.0.0-rc.1` receipts remain unchanged.

Stable publication therefore remains a separate Project-owned operation after target reconciliation and explicit authorization.

## Public product state

The Principal-approved Agnir brand identity remains canonical under `brand/`. The bilingual README/website, scoped GitHub Pages publication, transparent render-self-contained brand surfaces, Apache-2.0 licensing, bilingual contribution guidance, repository topics/homepage, and GitHub Issues feedback intake remain accepted public surfaces on authoritative `main`.

The public product category remains **Project Continuity**. The first-user value remains fresh-session recovery: **the Project persists; Executors come and go**. `adoption/README.md` remains canonical launch/adoption strategy.

Svif remains the first accepted real-project post-1.0 adoption case. External cold-start resumes, external design users, cross-Executor cases, and independently built integrations remain the highest-value next adoption evidence.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical Continuity Lineage identity != selector/binding != revision/checkpoint receipt.
- A checkpoint is reconciliation of durable Project truth, not an activity log.
- Unchanged durable truth is a checkpoint no-op.
- Published tags are immutable.
- `latest stable` is determined by actual publication, not a moving source branch or candidate version.
- Core/profile compatibility identifiers are not silently rewritten by a distribution upgrade.
- `AGNIR.md` is a Project activation/operation packaging surface and does not redefine Agnir Core.
- README, website, brand, adoption strategy, repository-host metadata, and execution-surface configuration are not Core semantic dependencies.
