# Bootstrap and Recovery

Version: 2.0.0

Bootstrap is the process by which an implementation discovers a Project's durable memory and restores enough context to continue safely.

## Protocol requirements

At the start of a new working context, an implementation SHOULD:

1. identify the Project boundary;
2. discover PPMP configuration using implementation/platform conventions;
3. validate the declared protocol version;
4. load Current State and Next Steps;
5. load Decisions when relevant to the current task;
6. load profile-specific knowledge or checkpoint history only when needed;
7. continue work using durable Project Memory rather than conversational recollection as the primary continuity mechanism.

If required durable memory is missing or inconsistent, the implementation SHOULD inspect available durable evidence, repair safely when authorized, or surface the inconsistency. It MUST NOT fabricate recovered state.

## Initialization

Initialization SHOULD inspect existing durable evidence, classify conservatively, create a minimal Core representation, populate it from observed reality, add profile-specific structures only when justified, and persist the initialization coherently.

The protocol does not define an 'open project' UI event, a repository path, or a particular first-message trigger. Those belong to platform adapters and implementations.

For the reference iorMemory ChatGPT behavior, see `implementations/IORMEMORY.md` and `adapters/CHATGPT.md`.
