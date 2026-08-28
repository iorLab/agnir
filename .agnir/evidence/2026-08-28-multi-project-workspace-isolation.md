# Multi-project workspace isolation evidence — 2026-08-28

## Claim

Agnir now has executable conformance evidence that a shared workspace registry can locate multiple Projects without becoming a shared mutable continuity store or allowing one Project's checkpoint to alter another Project's durable truth.

## Implementation

- Locator-only workspace registry reference: `conformance/workspace_registry_reference.py`, commit `1c5f4505406be9ef118b673890dd792eb18e15e1`.
- Multi-project isolation tests: `conformance/test_workspace_isolation.py`, commit `bf9586f731029ac41752ca5b785cc53e397f37dd`.
- Self-host checker registration: commit `dc971669bed27e876cf9eebd4a7fa5be5b1700f7`.

## Scenario proven

The fixture creates two independent Projects, Alpha and Beta, each with its own durable SQLite continuity store. A shared `workspace.json` registry contains only:

- Project identity;
- backend kind;
- database locator; and
- durable project key.

The registry contains no Current State, Next Actions, Decisions, Evidence, memory payload, or continuity payload.

The test proves:

1. Alpha and Beta resolve to different Project Entry Points and independently recover their own continuity;
2. checkpointing Alpha changes Alpha's State / Next Actions / Decisions / Evidence;
3. Beta's State / Next Actions / Decisions / Evidence remain byte-for-byte semantically unchanged;
4. the workspace registry file itself remains byte-for-byte unchanged by Alpha's checkpoint;
5. a fresh registry resolver and fresh SQLite continuity resolver can recover both Projects after the checkpoint;
6. a registry entry that embeds `state` or other continuity payload is rejected as `AGNIR_DISCOVERY_INCONSISTENT`;
7. an unknown Project identity in the registry is `AGNIR_DISCOVERY_NOT_FOUND`;
8. registry location does not bypass the independently required Project identity check (`AGNIR_DISCOVERY_PROJECT_MISMATCH`).

## Verification

GitHub Actions run `33143930233` for head `dc971669bed27e876cf9eebd4a7fa5be5b1700f7` completed successfully.

Job `98760729955` succeeded, including the unittest discovery step that runs `conformance/test_workspace_isolation.py`.

## Boundary

The workspace registry is conformance-only convenience metadata. It is not canonical Project truth and MUST NOT become a second mutable continuity root. Each Project remains independently authoritative through its own Agnir continuity path.
