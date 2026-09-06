# Agnir Discovery 0.1

**Status:** Normative supporting discovery/failure contract for Agnir Core `0.1`, and the inherited discovery-failure vocabulary for later Core lines that explicitly retain these semantics, including Core `0.2`.

Later profiles MAY define stricter mappings for profile-specific validation conditions. When they do, those profile-specific mappings govern that profile without redefining the general failure classes below.

## 1. Discovery algorithm

A fresh Executor SHOULD resolve continuity in this order:

1. accept or resolve the authorized Project Entry Point;
2. select the discovery profile/adapter convention applicable to that entry-point type;
3. resolve exactly one authoritative Discovery Record;
4. detect cycles and conflicting candidate records;
5. validate Agnir Core version compatibility;
6. validate Project identity against the active Project boundary;
7. resolve Current State and Next Actions;
8. resolve Decisions and Evidence as required;
9. validate consistency sufficient for safe continuation;
10. surface unresolved failures rather than fabricate continuity.

The I/O mechanism is implementation-specific.

## 2. Locator Chain requirements

Each Locator Chain hop MUST be directly resolvable by the active backend/adapter, explicitly point to the next locator, or use a stable environment binding durably associated with the Project.

A Locator Chain MUST NOT depend on a previous conversation, private model memory, an unstated predecessor-only path, a secret value that existed only in a prompt, or mutable workspace notes not durably bound to the Project.

External memory is conforming only when the Project Entry Point durably resolves it, Project identity can be checked, authorization can be invoked without predecessor-private context, and authorization failure is distinguishable from not-found when the implementation can safely tell the difference.

## 3. Failure semantics

### `AGNIR_DISCOVERY_NOT_FOUND`
No Discovery Record can be resolved under the active convention.

### `AGNIR_DISCOVERY_AMBIGUOUS`
Multiple candidate records or roots exist and authority cannot be determined.

### `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`
The declared Agnir **Core version** cannot be safely interpreted by the active implementation. Profile-specific contracts may use another class for a profile identifier that contradicts the already-selected profile.

### `AGNIR_DISCOVERY_PROJECT_MISMATCH`
Resolved memory identifies a different Project.

### `AGNIR_DISCOVERY_UNRESOLVABLE`
A required locator exists but cannot resolve to durable state under the active locator convention.

### `AGNIR_DISCOVERY_UNAUTHORIZED`
The locator is known but required authorization is absent or denied. A local locator that is invalid under the selected local profile is not automatically an authorization attempt; profile-specific contracts may classify it as unresolvable unless an explicit external Locator Chain is being resolved.

### `AGNIR_DISCOVERY_CYCLE`
The Locator Chain cycles instead of terminating in required durable state.

### `AGNIR_DISCOVERY_STALE`
A locator resolves only to state known to be superseded or non-authoritative.

### `AGNIR_DISCOVERY_INCONSISTENT`
Resolved memory or discovery metadata materially contradicts the selected Discovery Record/profile or itself such that safe continuation is not established.

## 4. Repair rule

Repair MUST target the earliest violated discovery invariant. An implementation MUST NOT silently adopt a different Project, silently downgrade an unsupported version, or invent missing current state.

After repair, the implementation SHOULD rerun discovery from the original Project Entry Point.

## 5. Cold-start conformance procedure

A cold-start case starts with a fresh Executor/environment that receives only:

- an authorized Project Entry Point; and
- the implementation/profile needed to interpret that entry-point type.

The case passes only if the Executor can locate the Discovery Record, validate version and Project identity, load Current State and Next Actions, retrieve required Decisions/Evidence, identify declared blockers, and recover at least one material fact that was not supplied by the test harness.

A test that directly supplies the memory path or current state outside normal discovery does not prove cold-start continuity.
