# Agnir brand system

This directory contains the **canonical Agnir identity system** derived from the Principal-approved Today 10:42 AM visual reference and integrated into authoritative `main` through PR #11.

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

`qa/FINAL-QA.md` defines the symmetric 13-item final QA scope shared with Svif. The complete PNG delivery package and byte-exact approved reference boards are preserved under `brand/` and hash-verified.

## Canonical integration status

The identity system is now authoritative Project content on `main`.

- PR #11: merged;
- final integration branch head: `3ce946741835498d91aad9ab1eba0cfad6188e30`;
- authoritative squash merge: `37e08498448797de56dc7ab03823bdc2d430a38f`;
- post-merge conformance: run `34042053904` / repository job `101510482659` — success;
- stable `v1.0.0` and accepted `v1.0.0-rc.1` release tags were not changed.

The locked visual authority must not be regenerated, aesthetically reinterpreted, or treated as permission to redesign the identity. Future derivatives must remain faithful to the approved masters and applicable reference board.