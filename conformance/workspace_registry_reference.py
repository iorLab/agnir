from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from core_reference import discovery_failure
from sqlite_backend_reference import SQLiteProjectEntryPoint


_ALLOWED_ENTRY_KEYS = {"backend", "database", "project_key"}
_FORBIDDEN_CONTINUITY_KEYS = {
    "state",
    "next_actions",
    "decisions",
    "evidence",
    "memory",
    "continuity",
}


@dataclass(frozen=True)
class WorkspaceProjectLocator:
    project_identity: str
    entry_point: SQLiteProjectEntryPoint


class WorkspaceRegistryReference:
    """Conformance-only locator registry for multiple independent Projects.

    The registry is convenience metadata. It may locate a Project Entry Point but
    must not become a second mutable Agnir continuity store.
    """

    def __init__(self, registry_path: str | Path) -> None:
        self.registry_path = Path(registry_path).resolve()
        self.workspace_root = self.registry_path.parent.resolve()
        self._entries = self._load()

    def _load(self) -> dict[str, WorkspaceProjectLocator]:
        try:
            payload = json.loads(self.registry_path.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise discovery_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "workspace registry metadata does not exist",
            ) from exc
        except json.JSONDecodeError as exc:
            raise discovery_failure(
                "AGNIR_DISCOVERY_INCONSISTENT",
                "workspace registry metadata is not valid JSON",
            ) from exc

        projects = payload.get("projects") if isinstance(payload, dict) else None
        if not isinstance(projects, dict):
            raise discovery_failure(
                "AGNIR_DISCOVERY_INCONSISTENT",
                "workspace registry requires a projects mapping",
            )

        entries: dict[str, WorkspaceProjectLocator] = {}
        for project_identity, raw in projects.items():
            if not isinstance(project_identity, str) or not project_identity:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry Project identity must be a non-empty string",
                )
            if not isinstance(raw, dict):
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry entry must be an object",
                )
            if _FORBIDDEN_CONTINUITY_KEYS.intersection(raw):
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry must contain locators only, not Project continuity",
                )
            if set(raw) != _ALLOWED_ENTRY_KEYS:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry entry has unsupported non-locator metadata",
                )
            if raw.get("backend") != "sqlite-conformance":
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry fixture supports only sqlite-conformance locators",
                )
            database = raw.get("database")
            project_key = raw.get("project_key")
            if not isinstance(database, str) or not database:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry database locator must be a non-empty string",
                )
            if not isinstance(project_key, str) or not project_key:
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry project_key must be a non-empty string",
                )

            database_path = (self.workspace_root / database).resolve()
            if not database_path.is_relative_to(self.workspace_root):
                raise discovery_failure(
                    "AGNIR_DISCOVERY_INCONSISTENT",
                    "workspace registry fixture locator escapes the workspace boundary",
                )
            entries[project_identity] = WorkspaceProjectLocator(
                project_identity=project_identity,
                entry_point=SQLiteProjectEntryPoint(database_path, project_key),
            )

        return entries

    def resolve(self, project_identity: str) -> WorkspaceProjectLocator:
        entry = self._entries.get(project_identity)
        if entry is None:
            raise discovery_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                "workspace registry has no Project Entry Point for the requested Project",
            )
        return entry
