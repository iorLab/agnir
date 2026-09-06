from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path

from core_reference import discovery_failure
from core_0_2_migration_reference import (
    MigrationConflict,
    normalize_initial_lineage_identity,
)
from repository_filesystem_0_2_reference import (
    DiscoverySnapshot02,
    discover_repository_filesystem_0_2,
)
from repository_filesystem_reference import _parse_scalars
from upgrade_reference import UpgradeMigrationRequired


CORE_0_1 = "0.1"
PROFILE_0_1 = "repository-filesystem/0.1"
CORE_0_2 = "0.2"
PROFILE_0_2 = "repository-filesystem/0.2"


@dataclass(frozen=True)
class RepositoryFilesystem02MigrationCandidate:
    project_root: Path
    project_identity: str
    lineage_identity: str
    source_manifest_digest: str
    candidate_manifest_text: str
    changed: bool


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _replace_agnir_compatibility(text: str) -> str:
    lines = text.splitlines(keepends=True)
    section: str | None = None
    version_replaced = False
    profile_replaced = False
    output: list[str] = []

    for line in lines:
        stripped = line.strip()
        if line and not line.startswith((" ", "\t")) and stripped.endswith(":"):
            section = stripped[:-1]
        if section == "agnir" and stripped.startswith("version:"):
            newline = "\n" if line.endswith("\n") else ""
            output.append('  version: "0.2"' + newline)
            version_replaced = True
            continue
        if section == "agnir" and stripped.startswith("discovery_profile:"):
            newline = "\n" if line.endswith("\n") else ""
            output.append('  discovery_profile: "repository-filesystem/0.2"' + newline)
            profile_replaced = True
            continue
        output.append(line)

    if not version_replaced or not profile_replaced:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "Core 0.1 manifest does not contain the required agnir compatibility scalars",
        )
    return "".join(output)


def _insert_continuity_before_memory(text: str, *, lineage_identity: str) -> str:
    marker = "memory:\n"
    index = text.find(marker)
    if index < 0:
        marker = "memory:\r\n"
        index = text.find(marker)
    if index < 0:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "Core 0.1 manifest does not contain a top-level memory section",
        )
    serialized = json.dumps(lineage_identity, ensure_ascii=False)
    block = "continuity:\n" f"  lineage: {serialized}\n\n"
    return text[:index] + block + text[index:]


def stage_repository_filesystem_0_1_to_0_2(
    project_root: str | Path,
    *,
    lineage_identity: str,
    authorized: bool,
    expected_project_identity: str | None = None,
) -> RepositoryFilesystem02MigrationCandidate:
    root = Path(project_root).resolve()
    manifest_path = root / "AGNIR.yaml"
    if not manifest_path.is_file():
        raise discovery_failure(
            "AGNIR_DISCOVERY_NOT_FOUND",
            "migration could not resolve top-level AGNIR.yaml",
        )

    text = manifest_path.read_text(encoding="utf-8")
    values = _parse_scalars(text)
    version = values.get(("agnir", "version"))
    profile = values.get(("agnir", "discovery_profile"))
    project_identity = values.get(("project", "identity"))

    if not project_identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "project.identity is missing",
        )
    if expected_project_identity is not None and project_identity != expected_project_identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            f"expected {expected_project_identity!r}, discovered {project_identity!r}",
        )

    if version == CORE_0_2 and profile == PROFILE_0_2:
        logical = normalize_initial_lineage_identity(lineage_identity)
        if not logical:
            raise discovery_failure(
                "AGNIR_LINEAGE_REQUIRED",
                "repository/filesystem 0.1 to 0.2 migration requires an initial logical lineage identity",
            )
        existing_lineage = values.get(("continuity", "lineage"))
        if existing_lineage != logical:
            raise MigrationConflict(
                f"{MigrationConflict.code}: Project already migrated with lineage "
                f"{existing_lineage!r}, not {logical!r}"
            )
        return RepositoryFilesystem02MigrationCandidate(
            project_root=root,
            project_identity=project_identity,
            lineage_identity=logical,
            source_manifest_digest=_digest(text),
            candidate_manifest_text=text,
            changed=False,
        )

    if version != CORE_0_1 or profile != PROFILE_0_1:
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            f"expected {CORE_0_1}/{PROFILE_0_1} migration source, discovered {version!r}/{profile!r}",
        )

    if not authorized:
        raise UpgradeMigrationRequired(
            f"{UpgradeMigrationRequired.code}: Core/profile 0.1 -> 0.2 changes a compatibility line"
        )

    logical = normalize_initial_lineage_identity(lineage_identity)
    if not logical:
        raise discovery_failure(
            "AGNIR_LINEAGE_REQUIRED",
            "repository/filesystem 0.1 to 0.2 migration requires an initial logical lineage identity",
        )

    candidate_text = _replace_agnir_compatibility(text)
    candidate_text = _insert_continuity_before_memory(
        candidate_text,
        lineage_identity=logical,
    )

    return RepositoryFilesystem02MigrationCandidate(
        project_root=root,
        project_identity=project_identity,
        lineage_identity=logical,
        source_manifest_digest=_digest(text),
        candidate_manifest_text=candidate_text,
        changed=True,
    )


def publish_repository_filesystem_0_2_migration(
    candidate: RepositoryFilesystem02MigrationCandidate,
) -> tuple[DiscoverySnapshot02, bool]:
    manifest_path = candidate.project_root / "AGNIR.yaml"
    current_text = manifest_path.read_text(encoding="utf-8")

    if not candidate.changed:
        snapshot = discover_repository_filesystem_0_2(
            candidate.project_root,
            expected_project_identity=candidate.project_identity,
            expected_lineage_identity=candidate.lineage_identity,
        )
        return snapshot, False

    if _digest(current_text) != candidate.source_manifest_digest:
        raise MigrationConflict(
            f"{MigrationConflict.code}: authoritative Core 0.1 manifest changed after migration staging"
        )

    temp_path = candidate.project_root / ".AGNIR.yaml.agnir-migration.tmp"
    try:
        with temp_path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(candidate.candidate_manifest_text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, manifest_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    snapshot = discover_repository_filesystem_0_2(
        candidate.project_root,
        expected_project_identity=candidate.project_identity,
        expected_lineage_identity=candidate.lineage_identity,
    )
    return snapshot, True
