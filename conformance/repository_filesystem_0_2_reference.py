from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from core_reference import discovery_failure
from repository_filesystem_reference import _resolve_local_locator


CORE_0_2_VERSION = "0.2"
PROFILE_0_2 = "repository-filesystem/0.2"
_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "agnir-manifest-0.2.schema.json"
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA)


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


def _load_and_validate_manifest_0_2(manifest: Path) -> dict[str, object]:
    try:
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"repository/filesystem 0.2 manifest cannot be parsed safely: {exc}",
        ) from exc

    if not isinstance(data, dict):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "repository/filesystem 0.2 manifest must be a mapping/object",
        )

    agnir = data.get("agnir")
    declared_version = agnir.get("version") if isinstance(agnir, dict) else None
    if isinstance(declared_version, str) and declared_version != CORE_0_2_VERSION:
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            f"expected Agnir Core {CORE_0_2_VERSION}, discovered {declared_version!r}",
        )

    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        first = errors[0]
        location = ".".join(str(item) for item in first.absolute_path) or "<root>"
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"repository/filesystem 0.2 manifest violates published schema at {location}: {first.message}",
        )

    return data


def _load_flat_local_evidence(root: Path, evidence_path: Path) -> dict[str, str]:
    evidence: dict[str, str] = {}
    for item in sorted(evidence_path.iterdir()):
        if not item.is_file():
            continue
        resolved = item.resolve()
        if not resolved.is_relative_to(root):
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"Evidence child {item.name!r} escapes the selected Project root",
            )
        evidence[item.name] = resolved.read_text(encoding="utf-8")
    return evidence


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

    data = _load_and_validate_manifest_0_2(manifest)
    agnir = data["agnir"]
    project = data["project"]
    continuity = data["continuity"]
    memory = data["memory"]
    assert isinstance(agnir, dict)
    assert isinstance(project, dict)
    assert isinstance(continuity, dict)
    assert isinstance(memory, dict)

    version = agnir["version"]
    profile = agnir["discovery_profile"]
    identity = project["identity"]
    lineage = continuity["lineage"]
    assert isinstance(version, str)
    assert isinstance(profile, str)
    assert isinstance(identity, str)
    assert isinstance(lineage, str)

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

    state_locator = memory["state"]
    next_locator = memory["next_actions"]
    decisions_locator = memory["decisions"]
    evidence_locator = memory["evidence"]
    assert isinstance(state_locator, str)
    assert isinstance(next_locator, str)
    assert decisions_locator is None or isinstance(decisions_locator, str)
    assert evidence_locator is None or isinstance(evidence_locator, str)

    state_path = _resolve_local_locator(
        root,
        state_locator,
        required=True,
        kind="Current State",
    )
    next_path = _resolve_local_locator(
        root,
        next_locator,
        required=True,
        kind="Next Actions",
    )
    decisions_path = _resolve_local_locator(
        root,
        decisions_locator,
        required=False,
        kind="Decisions",
    )
    evidence_path = _resolve_local_locator(
        root,
        evidence_locator,
        required=False,
        kind="Evidence",
        expect_directory=True,
    )

    evidence: dict[str, str] = {}
    if evidence_path is not None:
        evidence = _load_flat_local_evidence(root, evidence_path)

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
