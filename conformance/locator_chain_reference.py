from __future__ import annotations

from dataclasses import dataclass

from core_reference import CORE_VERSION, discovery_failure


@dataclass(frozen=True)
class ChainRecord:
    project_identity: str
    version: str = CORE_VERSION
    next_locator: str | None = None
    state_locator: str | None = None
    next_actions_locator: str | None = None
    authoritative: bool = True
    superseded: bool = False


@dataclass(frozen=True)
class MemoryObject:
    value: str
    checkpoint_id: str


@dataclass(frozen=True)
class ChainSnapshot:
    project_identity: str
    state: str
    next_actions: str
    checkpoint_id: str


class LocatorChainRegistry:
    """Conformance-only abstract locator substrate.

    It models Core Locator Chain semantics without implying any filesystem,
    database, URI scheme, transport, or normative storage profile.
    """

    def __init__(self) -> None:
        self.records: dict[str, ChainRecord] = {}
        self.memory: dict[str, MemoryObject] = {}

    def put_record(self, locator: str, record: ChainRecord) -> None:
        self.records[locator] = record

    def put_memory(self, locator: str, memory: MemoryObject) -> None:
        self.memory[locator] = memory


class LocatorChainReference:
    def __init__(self, registry: LocatorChainRegistry) -> None:
        self._registry = registry

    def resolve(
        self,
        entry_locator: str,
        *,
        expected_project_identity: str | None = None,
    ) -> ChainSnapshot:
        visited: set[str] = set()
        locator = entry_locator

        while True:
            if locator in visited:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_CYCLE",
                    "Locator Chain revisits a previously resolved locator",
                )
            visited.add(locator)

            record = self._registry.records.get(locator)
            if record is None:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_NOT_FOUND",
                    "Locator Chain cannot resolve the next Discovery Record",
                )
            if record.version != CORE_VERSION:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                    f"expected Agnir Core {CORE_VERSION}, discovered {record.version!r}",
                )
            if expected_project_identity is not None and record.project_identity != expected_project_identity:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                    f"expected {expected_project_identity!r}, discovered {record.project_identity!r}",
                )
            if not record.authoritative or record.superseded:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_STALE",
                    "Locator Chain resolves only to a known superseded or non-authoritative record",
                )

            if record.next_locator is not None:
                if record.state_locator is not None or record.next_actions_locator is not None:
                    raise discovery_failure(
                        "AGNIR_DISCOVERY_INCONSISTENT",
                        "Locator Chain hop simultaneously declares another record and terminal memory",
                    )
                locator = record.next_locator
                continue

            if record.state_locator is None or record.next_actions_locator is None:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    "terminal Discovery Record lacks required durable-memory locators",
                )

            state = self._registry.memory.get(record.state_locator)
            next_actions = self._registry.memory.get(record.next_actions_locator)
            if state is None or next_actions is None:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    "terminal Discovery Record points to missing required durable memory",
                )
            if state.checkpoint_id != next_actions.checkpoint_id:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "Current State and Next Actions resolve to different checkpoint generations",
                )

            return ChainSnapshot(
                project_identity=record.project_identity,
                state=state.value,
                next_actions=next_actions.value,
                checkpoint_id=state.checkpoint_id,
            )
