# Bootstrap Protocol

Version: 1.0.0

## 1. Trigger

The bootstrap check runs at the first substantive turn of each new conversation in a ChatGPT Project that uses RPM.

It is not necessary to repeat the bootstrap check on every message in the same conversation unless the repository or manifest is intentionally changed.

## 2. Bootstrap sequence

1. Identify the associated project repository.
2. Check for `.chatgpt/project-memory.yaml`.
3. If the manifest is missing, notify the user that RPM is not initialized and offer initialization before substantive work continues.
4. If the manifest exists, read and validate it.
5. Confirm that the declared RPM version is supported.
6. Read the Core memory files declared by the manifest, normally:
   - `PROJECT_STATE.md`
   - `NEXT_STEPS.md`
7. Read `DECISIONS.md` when the current task depends on prior decisions.
8. Load profile-specific or historical artifacts only when relevant.
9. Continue substantive work using the repository as durable context.

## 3. Initialization sequence

After user approval to initialize RPM:

1. Inspect repository structure, README, existing documentation, and other durable evidence.
2. Classify the project according to `CLASSIFICATION.md`.
3. Select a conservative `primary_type` and profile set.
4. Create `.chatgpt/project-memory.yaml` from the current manifest template.
5. Create the Core memory root and required Core files.
6. Populate the Core files from actual repository state; do not create false completion claims.
7. Create profile-specific artifacts only when existing durable information already justifies them.
8. Commit the initialization as one coherent documentation change when practical.
9. Report the selected classification, created files, and commit SHA.

## 4. Missing or inconsistent Core files

If the manifest exists but a required Core file is missing:

- do not treat the project as uninitialized automatically;
- inspect whether the file was moved, renamed, or intentionally omitted;
- repair the RPM structure when safe, otherwise surface the inconsistency.

If the manifest and repository disagree materially, current observed repository state takes precedence for factual claims, and the memory documents SHOULD be repaired.

## 5. Loading discipline

Bootstrap SHOULD remain lightweight.

Default load order:

```text
manifest
  ↓
PROJECT_STATE.md
  ↓
NEXT_STEPS.md
  ↓
DECISIONS.md when relevant
  ↓
profile artifacts on demand
  ↓
recent sessions only if needed
```

Do not read every session log or every profile document by default.

## 6. Minimal ChatGPT Project Instructions

A consuming ChatGPT Project SHOULD contain a short bootstrap hook similar to:

```text
This project uses RPM (Repository Project Memory).

At the first substantive turn of every new conversation, check
`.chatgpt/project-memory.yaml` in the associated repository.

If missing, offer RPM initialization.
If present, load it and follow the declared RPM specification and profiles before substantive work.

The repository is the canonical source of truth; chats are working memory.
Persist meaningful durable project knowledge according to RPM.

When I say “收尾”, “结束”, “先到这里”, “checkpoint”, or equivalent,
perform a final RPM checkpoint before finishing.
```

The complete operational rules belong in the RPM specification repository, not duplicated in every ChatGPT Project.

## 7. No open-project event assumption

RPM does not assume that ChatGPT receives a reliable event when a user merely opens a Project. Bootstrap therefore occurs on the first substantive conversational turn, not on project-open UI state.
