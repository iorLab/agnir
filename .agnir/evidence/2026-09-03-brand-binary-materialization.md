# Agnir brand binary materialization — 2026-09-03

Status: **branch-local integration evidence; not canonical until integrated into authoritative `main`.**

## Trigger

The approved 10:42 AM source board and larger PNG delivery derivatives could not be sent byte-exactly through the direct ChatGPT-to-GitHub base64 bridge. Rather than attach unverified blobs, a byte-safe handoff archive was prepared and the Principal uploaded it directly to the root of `brand/identity-system` in both repositories.

## Transport verification

The uploaded archive was verified as:

- filename: `svif-agnir-brand-binary-integration-handoff.zip`;
- size: `7,925,506` bytes;
- SHA-256: `52e8cee3c03f0762fc47d579505122dc452e5de97dafb462a3b470ed5457f72d`;
- Git blob: `3f49c176a5c5680620de6f4de09beb6297f99bf0`.

The same Git blob was observed in both repositories, proving the browser upload preserved exact archive bytes.

## Latest-main reconciliation before materialization

Immediately before materialization, authoritative Agnir `main` had advanced to `3564a4dd1485d3be29052f9698356202685ab31d`; the uploaded brand branch head was `042de482059df030e4c462c9ee3c517137d2db0c` and was behind by 9 commits.

Reverse-sync PR `#13` exposed real conflicts. No stale branch-side canonical Core/release/state files were selected. Instead an explicit latest-main-wins two-parent candidate was constructed:

- latest-main tree: `e883044b6263dd56ae894eb5c1dee871262014c6`;
- retained branch-local surface: `brand/`, six brand evidence files and the uploaded archive;
- reconciled tree: `66ad3603c081e4dc214099758544ef21264bd78a`;
- reconciliation commit: `e8dd3662cb2d12bc6ae49b2bd0fc1d8c8f2a0f9d`.

The branch ref advanced to that commit without force. GitHub subsequently recognized PR `#13` as merged through ancestry. Post-reconcile comparison reported `behind main = 0`.

## Byte-exact GitHub-runner materialization

Temporary workflow creation commit: `b9810bea8549844c864c18b2e08208263a1c50ab`.

Workflow run `33730501685` completed successfully. It:

1. verified the uploaded archive SHA-256;
2. extracted the handoff;
3. selected all 15 Agnir targets;
4. verified each source payload SHA-256;
5. copied each source to its final repository path;
6. verified each destination SHA-256 again;
7. reapplied only the brand entries to latest-main README/repository maps;
8. committed the results;
9. removed the root transport ZIP and temporary workflow.

Final materialization commit: `a858de5c2d12f800ef6d9057f28422320ff5a012`.

## Repository result

Byte-exact approved references now exist at:

- `brand/reference/agnir-approved-reference.png`;
- `brand/reference/svif-agnir-family-approved-reference.png`.

The complete 13-item PNG delivery package exists under `brand/exports/png/`, while the approved v0.3 vector masters remain authoritative under `brand/masters/`.

Final tree inspection confirmed all 13 PNG files, including mark, wordmark, both lockups, light/dark/mono, app icon, four favicon targets and social card.

## Gate result

The **large byte-exact binary preservation gate is closed** for the Agnir brand branch. Remaining gates are latest-main freshness, final Draft PR `#11` synthetic-merge conformance, coherent target publication and post-publication verification.
