# Agnir Current State

Durable continuity belongs to the Project.

Authoritative `main` now carries the Agnir `1.0.0` stable source package at exact revision `ab5dcc3341d39631e843499632739864a90bba14`, preserving Project identity `urn:agnir:project:agnir-core`, logical lineage `urn:agnir:lineage:authoritative`, and selector `refs/heads/main`.

That exact authoritative revision passed workflow `34030974021`, repository job `101480276759`, including self-host cold start, historical Core/profile 0.1/0.2 regressions, Core/profile 1.0, 0.2→1.0 promotion, VCS/non-VCS lineage behavior, stable package gates, and the complete `test_*.py` suite. Stable publication was correctly skipped because the exact arm message has not yet been used.

Stable `v1.0.0` is therefore **authoritative and verified, but not yet published**. `publication_status` remains `not-armed`; the previously published non-prerelease stable release remains the resolver target until publication succeeds.

## Accepted release evidence

- accepted RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC Release id `383536840`;
- RC workflow `34026167762` attempts 1 and 2: success;
- RC acceptance checkpoint `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- accepted stable staging source `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- accepted staging checkpoint `5f88a9c8bcc67753012f8bcae533241482dc1a7d`, run `34030753962`;
- target validation revision `ab5dcc3341d39631e843499632739864a90bba14`, run `34030934536`;
- authoritative-main verification of the same revision: run `34030974021`.

## Remaining boundary

The next checkpoint records these authoritative verification receipts. After that checkpoint itself passes exact-main CI, stable publication may be armed by a separate main commit with the **exact** message `release: publish v1.0.0 stable`. No unrelated semantic change belongs in that arm transition.
