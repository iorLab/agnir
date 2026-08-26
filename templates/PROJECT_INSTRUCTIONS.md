This Project uses **Persistent Project Memory (PPM)**, the reference implementation of the **iorMemory** protocol.

At the first substantive turn of every new conversation:

1. Check `.chatgpt/project-memory.yaml` in the associated repository.
2. If missing, offer PPM initialization.
3. If present, validate the declared iorMemory version and load the configured Current State and Next Steps.
4. Read Decisions when prior decisions are relevant.
5. Load profile-specific or checkpoint history only as required by the current task.

For this repository-backed setup, durable project knowledge in the repository is authoritative; chats are working context only.

Persist meaningful durable changes according to iorMemory and PPM. Do not archive raw conversations.

When I say “收尾”, “结束”, “先到这里”, “checkpoint”, “save progress”, or equivalent, perform a final PPM checkpoint before finishing.
