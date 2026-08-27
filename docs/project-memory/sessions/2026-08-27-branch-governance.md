# Agnir checkpoint — branch governance and active-line focus

Saved: 2026-08-27T06:49:51-07:00

## Boundary captured

- `main` is the authoritative active Agnir development line.
- `legacy/ppmp-v2.0.0` preserves the final pure PPMP v2.0.0 / PPM / Sandminni predecessor boundary at `3bd3938ea00276eb51ca51c6c7ee1264d862acd4`.
- Temporary, redundant, or incidental branches are intentionally ignored during the architecture rewrite unless they become explicitly authoritative.
- Branch cleanup is deferred until the new Agnir version is substantially complete.
- The active technical priorities remain the `AGNIR.yaml` schema/versioning, cold-start conformance, migration evidence, materially non-repository storage evidence, and the Svif compatibility boundary.

## Resumption rule

A fresh executor should continue from `main`, use `legacy/ppmp-v2.0.0` only for predecessor evidence or compatibility comparison, and should not spend time cleaning incidental branches before the new version reaches completion unless a branch causes an actual conflict or ambiguity.
