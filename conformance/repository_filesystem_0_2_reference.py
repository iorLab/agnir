from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from core_reference import discovery_failure
from repository_filesystem_reference import _parse_scalars, _resolve_local_locator


CORE_0_2_VERSION = "0.2"
PROFILE_0_2 = "repository-filesystem/0.2"


@dataclass(frozen=True)
class DiscoverySnapshot02:
    project_root: Path
    project_identity: str
    lineage_identity: str
    version: str
    profile: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]


def discover_repository_filesystem_0_2(
    project_root: str | Path,
    *,
    expected_project_identity: str | None = None,
    expected_lineage_identity: str | None = None,
) -> DiscoverySnapshot02:
    root = Path(project_root).resolve()
    manifest = root / "AGNIR.yaml"
    if not manifest.is_file():
        raise discovery_failure(
            "AGNIR_DISCOVERY_NOT_FOUND",
            "repository/filesystem 0.2 could not resolve top-level AGNIR.yaml at the selected Project root",
        )

    values = _parse_scalars(manifest.read_text(encoding="utf-8"))
    version = values.get(("agnir", "version"))
    profile = values.get(("agnir", "discovery_profile"))
    identity = values.get(("project", "identity"))
    lineage = values.get(("continuity", "lineage"))

    if version != CORE_0_2_VERSION:
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            f"expected Agnir Core {CORE_0_2_VERSION}, discovered {version!r}",
        )
    if profile != PROFILE_0_2:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"expected discovery profile {PROFILE_0_2}, discovered {profile!r}",
        )
    if not identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "project.identity is missing",
        )
    if not lineage:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "continuity.lineage is missing",
        )
    if expected_project_identity is not None and identity != expected_project_identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            f"expected {expected_project_identity!r}, discovered {identity!r}",
        )
    if expected_lineage_identity is not None and lineage != expected_lineage_identity:
        raise discovery_failure(
            "AGNIR_LINEAGE_NOT_FOUND",
            f"expected lineage {expected_lineage_identity!r}, discovered selected lineage {lineage!r}",
        )

    state_path = _resolve_local_locator(
        root,
        values.get(("memory", "state")),
        required=True,
        kind="Current State",
    )
    next_path = _resolve_local_locator(
        root,
        values.get(("memory", "next_actions")),
        required=True,
        kind="Next Actions",
    )
    decisions_path = _resolve_local_locator(
        root,
        values.get(("memory", "decisions")),
        required=False,
        kind="Decisions",
    )
    evidence_path = _resolve_local_locator(
        root,
        values.get(("memory", "evidence")),
        required=False,
        kind="Evidence",
        expect_directory=True,
    )

    evidence: dict[str, str] = {}
    if evidence_path is not None:
        evidence = {
            item.name: item.read_text(encoding="utf-8")
            for item in sorted(evidence_path.iterdir())
            if item.is_file()
        }

    return DiscoverySnapshot02(
        project_root=root,
        project_identity=identity,
        lineage_identity=lineage,
        version=version,
        profile=profile,
        state=state_path.read_text(encoding="utf-8"),
        next_actions=next_path.read_text(encoding="utf-8"),
        decisions=None if decisions_path is None else decisions_path.read_text(encoding="utf-8"),
        evidence=evidence,
    )
