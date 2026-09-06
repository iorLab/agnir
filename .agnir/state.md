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

## Post-v1 repository housekeeping

The first safe temporary-ref retirement pass is complete.

- cleanup arm revision: `a1007845d5d28947f5409fc7dc7643dac54d72d6`;
- cleanup workflow `34040930337`, job `101507430125`: success;
- cleanup-arm conformance `34040930367`, repository job `101507430301`: success;
- one-shot cleanup workflow removed at `a4b7d9d0642e81974ba35f4f8ccf943099281de1`;
- workflow-removal conformance `34041050353`, repository job `101507754342`: success;
- 17 completed temporary feature/integration/promotion/release/repair/validation branch refs were retired;
- obsolete independent-challenge issue #14 was closed as superseded/completed;
- no open issue remains after that housekeeping closure.

Five branch refs remain intentionally at this checkpoint boundary:

- `main` — authoritative;
- `brand/identity-system` — retained because open draft PR #11 still depends on it and its byte-exact brand-binary gate remains unresolved;
- `release/v1.0.0-rc.1` — retained as RC acceptance evidence anchor;
- `release/v1.0.0` — retained as stable staging acceptance evidence anchor;
- `validation/mount-boundary-v0.2.0` — retained as genuine mount-boundary evidence anchor.

The three evidence-only retained refs are non-authoritative and may be retired later only after their exact evidence reachability has an equally durable replacement. Published release tags remain immutable.

Agnir has crossed the v1.0.0 release boundary and completed the safe post-release ref cleanup pass. Ongoing work is ordinary stable maintenance, post-1.0 adoption evidence, and separately scoped unfinished work such as PR #11.