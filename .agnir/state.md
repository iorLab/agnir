# Agnir Current State

Durable continuity belongs to the Project.

Agnir `v1.0.0` is now **published, independently verified, and the latest stable release**.

The immutable stable tag `v1.0.0` points to exact authoritative arm revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`. GitHub Release id `383612171` is non-draft and non-prerelease, and `releases/latest` resolves to `v1.0.0`.

The publication workflow was `34039014354`:

- attempt 1 repository job `101502237380`: success;
- attempt 1 stable publication job `101502271312`: success;
- fresh immutable-source attempt 2 repository job `101502430280`: success;
- fresh immutable-source attempt 2 stable publication job `101502473422`: success.

The accepted RC remains immutable: `v1.0.0-rc.1` still points exactly to `092945289f1a0a9803e4fe0583104aa380ceaadc`.

Issue #29 (`v1.0.0 stable release: reconcile accepted RC and publish`) is closed as completed. No v1.0.0 release gate remains open.

## Stable compatibility state

- repository/distribution: `1.0.0`;
- Core: `1.0`;
- repository/filesystem profile: `repository-filesystem/1.0`;
- explicit Core/profile `0.2` → `1.0` promotion remains Project-owned and separately authorized;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain supported;
- installing a `1.0.x` distribution does not silently relabel an existing valid `0.2` Project.

## Release evidence chain

- independent implementation gate: issue #26 clean `PASS`;
- Core/profile 1.0 promotion: issue #27 / PR #28 accepted;
- immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`, Release id `383536840`;
- RC workflow `34026167762`, attempts 1 and 2: success;
- RC acceptance checkpoint: `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- accepted stable staging source: `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- accepted stable staging checkpoint: `5f88a9c8bcc67753012f8bcae533241482dc1a7d`, run `34030753962`;
- authoritative target verification: `ab5dcc3341d39631e843499632739864a90bba14`, run `34030974021`;
- publication-precondition checkpoint: `b99ea0d37cca852df023ef9071d4102c0376f0fe`, run `34038863673`;
- stable arm/tag revision: `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- stable publication workflow: `34039014354`, attempts 1 and 2 success.

Agnir has crossed the v1.0.0 release boundary. Ongoing work is ordinary stable maintenance and downstream adoption evidence, not completion of the v1 release gate.
