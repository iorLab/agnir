# Agnir brand system

This directory contains the branch-approved Agnir identity system derived from the Principal-approved Today 10:42 AM visual reference.

## Directory responsibilities

```text
brand/
├── README.md                         # this guide
├── APPROVED-VISUAL-REFERENCE.md      # locked visual authority and source hashes
├── PRODUCTION-STATUS.md              # current production gate / completed work
├── brand-handoff.md                  # downstream usage rules
├── brand-process-log.md              # design/production chronology retained for audit
├── reference/                        # extraction coordinates and reference manifests
├── masters/                          # approved production vector masters
│   └── candidates/                   # superseded/review candidates; not production truth
├── exports/                          # materialized production derivatives
├── qa/                               # final review scope and QA evidence metadata
└── tools/                            # deterministic derivative/review tooling
```

## Production authority

The production geometry authority is:

- `masters/agnir-mark.svg`
- `masters/agnir-wordmark.svg`
- `masters/agnir-horizontal-lockup.svg`
- `masters/agnir-vertical-lockup.svg`

Agnir v0.3 was accepted in Principal-facing clean review and promoted to these production master paths. Files under `masters/candidates/` are provenance only.

## Derivatives

`exports/` contains light/dark/monochrome, app-icon and favicon delivery surfaces generated from the approved masters. Small-size favicon pruning may remove only particles below the documented visibility thresholds; it must not change the A geometry, major particles, pale inner A, or central anchor.

## QA

`qa/FINAL-QA.md` defines the symmetric 13-item final QA scope shared with Svif. Large raster QA sheets and delivery bundles are hash-recorded until they can be preserved through a byte-safe repository path.

## Integration status

Everything in this directory is branch-local until reconciled with the latest authoritative `main` and integrated coherently. The locked visual authority must not be regenerated or aesthetically reinterpreted during integration.
