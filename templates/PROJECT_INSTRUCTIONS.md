This project uses RPM (Repository Project Memory).

At the first substantive turn of every new conversation, check `.chatgpt/project-memory.yaml` in the associated repository.

If it is missing, tell me RPM is not initialized and offer to initialize it.

If it exists, read the manifest and follow the declared RPM specification and profiles before substantive work. Load `PROJECT_STATE.md` and `NEXT_STEPS.md` first; load `DECISIONS.md`, profile artifacts, and session history only when relevant.

The repository is the canonical source of truth; chats are working memory. Persist meaningful durable project knowledge according to RPM.

Do not store raw chat transcripts or trivial discussion.

When I say “收尾”, “结束”, “先到这里”, “checkpoint”, “save progress”, or equivalent, perform a final RPM checkpoint before finishing.
