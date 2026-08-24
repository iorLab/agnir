# Generic Profile

Version: 1.0.0

Use the Generic profile when no specialized profile clearly adds durable value, or when a project is still too early to classify safely.

Generic projects use RPM Core without mandatory domain-specific extensions.

## Behavior

- Maintain `PROJECT_STATE.md`, `NEXT_STEPS.md`, `DECISIONS.md`, and meaningful session logs.
- Create additional documents only when durable information no longer fits cleanly in the Core.
- Prefer later reclassification into a specialized profile over inventing ad hoc structure prematurely.

## Persistence triggers

Use the general persistence rules in `spec/PERSISTENCE.md`.

## Reclassification

When recurring work patterns become clear, update the manifest to add or replace profiles according to `spec/CLASSIFICATION.md`.

Reclassification SHOULD preserve useful existing documents and SHOULD NOT move files solely for cosmetic consistency unless the benefit outweighs churn.
