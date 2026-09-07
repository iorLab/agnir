# Brand public surface, About permission boundary, and branch retirement — 2026-09-07

Status: **README/public brand surface complete; integrated brand branch retired; GitHub About metadata remains an administrative follow-up because the available automation credential is metadata-read-only.**

## Public brand surface

Commit `75dde01da2123e731a6de461fb2f3269fd6bbbbb` updated the authoritative Agnir public/documentation surface:

- `README.md` now displays `brand/exports/png/agnir-horizontal-lockup.png` at the top and adds an `Identity` section;
- `README.zh-CN.md` mirrors that with `品牌识别`;
- both explain Agnir as the sand/warm-mineral **Structure Layer / 结构层**, particle-built A, and central anchor;
- `brand/README.md`, `brand/APPROVED-VISUAL-REFERENCE.md`, and `brand/INTEGRATION-NOTE.md` were updated from branch-local language to canonical post-PR #11 status;
- `.agnir/evidence/2026-09-07-svif-agnir-1.0-adoption.md` was added as the first post-v1 real-project adoption record.

Conformance run `34077491299`, repository job `101606358819`: success. Publication jobs were skipped as required.

## GitHub About attempt

Repository readback before the attempt showed:

- `description: null`;
- `topics: []`.

Intended description:

`Agnir — project-owned durable continuity, assembled from discoverable Project truth: state, next actions, decisions, and evidence.`

Intended topics:

- `durable-continuity`
- `project-continuity`
- `state-management`
- `protocol`
- `developer-tools`

A one-shot workflow was deliberately ordered to update and verify GitHub About metadata **before** deleting the integrated brand branch. Exact arm revision `1eec3aa8f10f6b6ddae80534dfe31cfb2f0e1320` triggered workflow `34077611205`, job `101606699693`.

The runner exposed:

- `Contents: write`;
- `Metadata: read`.

`PATCH /repos/iorLab/agnir` failed with HTTP 403: `Resource not accessible by integration`. Because the shell used `set -e` and About mutation preceded branch deletion, the failure occurred before any branch-retirement action. The same revision passed ordinary Agnir conformance in run `34077611209`, job `101606699370`.

After the failed metadata attempt, independent repository readback still showed `description=null` and `topics=[]`. No claim of successful About publication is made.

## Brand branch retirement

The workflow was narrowed to contents-only branch retirement and revalidated:

- narrowing commit: `4dd888ddc51217d6193bd02f91310a96d496ba62`;
- conformance run/job: `34077672138` / `101606870599` — success.

Exact arm revision:

`77eaada2b200b2fb3dd73309eddd259623540666`

Results:

- retirement workflow/job: `34077763678` / `101607125525` — success;
- same-revision Agnir conformance: `34077763682` / `101607125572` — success;
- `brand/identity-system` absent from independent branch inventory afterward;
- remaining branches: `main`, `release/v1.0.0-rc.1`, `release/v1.0.0`, `validation/mount-boundary-v0.2.0`.

Release anchors were verified unchanged:

- `v1.0.0` -> `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`.

The one-shot housekeeping workflow was removed at `222d60c0467c0368b1aefe68b55cc01ef43cda56`. Post-removal conformance run `34077835425`, repository job `101607318275`: success; all publication jobs skipped.

## Interpretation

The canonical brand integration is complete: approved assets are on `main`, the public README surfaces the identity, and the obsolete integration branch is retired. GitHub About is a host-level metadata surface outside canonical Agnir Project truth. The only unfinished piece is applying the intended description/topics using a repository-admin credential or UI with metadata-write authority.