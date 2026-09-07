# Agnir Current State

Durable continuity belongs to the Project.

Agnir `v1.0.0` is **published, independently verified, and the latest stable release**. Ordinary stable-maintenance mode applies.

The immutable stable tag `v1.0.0` points to exact released revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. GitHub Release id `383612171` is non-draft and non-prerelease, and `releases/latest` resolves to `v1.0.0`. Accepted RC `v1.0.0-rc.1` remains immutable at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

## Stable compatibility state

- repository/distribution: `1.0.0`;
- Core: `1.0`;
- repository/filesystem profile: `repository-filesystem/1.0`;
- explicit Core/profile `0.2` -> `1.0` promotion remains Project-owned and separately authorized;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- installing a `1.0.x` distribution does not silently relabel an existing valid `0.2` Project.

## Brand identity and public repository surface

The Principal-approved Agnir identity system is authoritative on `main` and is now surfaced directly in both public README variants.

- brand integration PR: `#11`, merged completed;
- authoritative squash merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- brand acceptance checkpoint: `e5305ab0474c4c8c562dbfbfaca54185b84d07f1`;
- README/brand public-surface + first adoption evidence commit: `75dde01da2123e731a6de461fb2f3269fd6bbbbb`;
- public-surface conformance run/job: `34077491299` / `101606358819` — success;
- README identity: Agnir = sand/warm-mineral **Structure Layer / 结构层**, particle-built A with a central anchor;
- canonical production masters remain under `brand/masters/`; delivery PNG/app-icon/favicon surfaces remain under `brand/exports/png/`.

The completed `brand/identity-system` integration branch was retired by exact arm revision `77eaada2b200b2fb3dd73309eddd259623540666`; branch-retirement workflow `34077763678` / job `101607125525` succeeded, and the same revision passed Agnir conformance run `34077763682` / job `101607125572`. The one-shot workflow was then removed at `222d60c0467c0368b1aefe68b55cc01ef43cda56`, whose conformance run `34077835425` / job `101607318275` succeeded.

Current ordinary branch inventory is intentionally small: `main` plus three retained evidence anchors (`release/v1.0.0-rc.1`, `release/v1.0.0`, `validation/mount-boundary-v0.2.0`).

GitHub repository **About metadata is not yet updated**. An exact-arm attempt tried to set the repository description/topics before branch retirement, but GitHub Actions exposed `Metadata: read` only and rejected `PATCH /repos/iorLab/agnir` with HTTP 403 (`Resource not accessible by integration`). The failure occurred before any branch deletion. Repository readback still reports `description=null` and `topics=[]`. This host-metadata limitation does not affect canonical Project truth or the README brand surface.

## Post-1.0 adoption evidence

Svif (`iorLab/svif`) is now the first recorded real-project downstream adoption case for Agnir 1.0.

Svif completed an explicit, Principal-authorized Core/profile `0.2` -> `1.0` promotion while preserving Project identity, logical lineage, selector, durable memory locators, historical 0.1/0.2 adapter support, product version, brand assets, and the immutable Preview.1 distribution boundary. Agnir records this at `.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md`.

Key Svif receipts:

- captured source: `a00ad6ed9f18abddbed1979a619f932350cefe54`;
- candidate: `5a88eee4bc214b8da3b4c5f48640067b167248b8`;
- staging/full run: `34076031454` success;
- PR #9 synthetic-merge checks: `34076166897` success;
- authoritative promotion merge: `5da0eb76e38e817ba0f5111ce2b08750afa3b9c3`;
- authoritative post-merge checks: `34076249501` success;
- Svif post-promotion checkpoint: `6c2c33da68e88a221ba36289d895f0423d64063a`.

No Agnir defect was exposed by the Svif adoption case. Previously satisfied v1 gates remain closed.

## Release evidence chain

- independent implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`, Release id `383536840`;
- stable arm/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable publication workflow: `34039014354`, attempts 1 and 2 success.

Agnir is now in stable maintenance + downstream adoption mode. Brand integration and its temporary branch are complete; GitHub About metadata is a small repository-host administrative follow-up, not a protocol/release gate.