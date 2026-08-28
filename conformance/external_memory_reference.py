from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from core_reference import CORE_VERSION, discovery_failure


@dataclass(frozen=True)
class ExternalProjectEntryPoint:
    discovery_locator: str


@dataclass(frozen=True)
class ExternalDiscoveryRecord:
    project_identity: str
    authorization_ref: str
    state_locator: str
    next_actions_locator: str
    decisions_locator: str | None = None
    version: str = CORE_VERSION


@dataclass(frozen=True)
class ExternalContinuitySnapshot:
    project_identity: str
    state: str
    next_actions: str
    decisions: str | None


class ExternalMemoryRegistry:
    """Conformance-only external registry/store with no credential values."""

    def __init__(self) -> None:
        self.discovery_records: dict[str, ExternalDiscoveryRecord] = {}
        self.objects: dict[str, str] = {}

    def put_record(self, locator: str, record: ExternalDiscoveryRecord) -> None:
        self.discovery_records[locator] = record

    def put_object(self, locator: str, value: str) -> None:
        self.objects[locator] = value


class ExternalMemoryReference:
    """Conformance reference for externally located, authorization-gated memory.

    `authorization_check` receives only the durable authorization reference from
    the Discovery Record. Secret/credential values are outside this model.
    """

    def __init__(
        self,
        registry: ExternalMemoryRegistry,
        authorization_check: Callable[[str], bool],
    ) -> None:
        self._registry = registry
        self._authorization_check = authorization_check

    def _resolve_object(self, locator: str, label: str) -> str:
        if locator not in self._registry.objects:
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"authorized external {label} locator does not resolve",
            )
        return self._registry.objects[locator]

    def load(
        self,
        entry_point: ExternalProjectEntryPoint,
        *,
        expected_project_identity: str | None = None,
    ) -> ExternalContinuitySnapshot:
        record = self._registry.discovery_records.get(entry_point.discovery_locator)
        if record is None:
            raise discovery_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "external Project Entry Point did not resolve a Discovery Record",
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

        if not self._authorization_check(record.authorization_ref):
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNAUTHORIZED",
                "external Discovery Record resolved but required authorization is absent or denied",
            )

        state = self._resolve_object(record.state_locator, "Current State")
        next_actions = self._resolve_object(record.next_actions_locator, "Next Actions")
        decisions = None
        if record.decisions_locator is not None:
            decisions = self._resolve_object(record.decisions_locator, "Decisions")

        return ExternalContinuitySnapshot(
            project_identity=record.project_identity,
            state=state,
            next_actions=next_actions,
            decisions=decisions,
        )
