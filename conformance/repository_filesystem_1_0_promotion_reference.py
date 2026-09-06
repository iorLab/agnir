from __future__ import annotations

import hashlib
import json
import os
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

import yaml

from core_0_2_migration_reference import MigrationConflict
from core_reference import discovery_failure
from repository_filesystem_0_2_reference import (
    DiscoverySnapshot02,
    discover_repository_filesystem_0_2,
)
from repository_filesystem_1_0_reference import (
    DiscoverySnapshot10,
    _SCHEMA_VALIDATOR,
    discover_repository_filesystem_1_0,
)
from repository_filesystem_reference import _resolve_local_locator
from upgrade_reference import UpgradeMigrationRequired


CORE_0_2 = "0.2"
PROFILE_0_2 = "repository-filesystem/0.2"
CORE_1_0 = "1.0"
PROFILE_1_0 = "repository-filesystem/1.0"


@dataclass(frozen=True)
class RepositoryFilesystem10PromotionCandidate:
    project_root: Path
    project_identity: str
    lineage_identity: str
    source_manifest_digest: str
    source_continuity_digest: str
    candidate_manifest_text: str
    changed: bool
    source_snapshot: DiscoverySnapshot02 | None


def _digest_bytes(parts: list[tuple[str, bytes]]) -> str:
    digest = hashlib.sha256()
    for label, payload in sorted(parts, key=lambda item: item[0]):
        digest.update(label.encode("utf-8"))
        digest.update(b"\0")
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)
    return digest.hexdigest()


def _manifest_digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _parse_manifest_text(text: str) -> dict[str, object]:
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"promotion source manifest cannot be parsed safely: {exc}",
        ) from exc
    if not isinstance(data, dict):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source manifest must be a mapping/object",
        )
    return data


def _continuity_digest(root: Path, manifest_text: str, data: dict[str, object]) -> str:
    memory = data.get("memory")
    if not isinstance(memory, dict):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source is missing a valid memory mapping",
        )

    state = memory.get("state")
    next_actions = memory.get("next_actions")
    decisions = memory.get("decisions")
    evidence = memory.get("evidence")
    if not isinstance(state, str) or not isinstance(next_actions, str):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source has invalid required memory locators",
        )
    if decisions is not None and not isinstance(decisions, str):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source has invalid Decisions locator",
        )
    if evidence is not None and not isinstance(evidence, str):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source has invalid Evidence locator",
        )

    parts: list[tuple[str, bytes]] = [("AGNIR.yaml", manifest_text.encode("utf-8"))]
    state_path = _resolve_local_locator(root, state, required=True, kind="Current State")
    next_path = _resolve_local_locator(root, next_actions, required=True, kind="Next Actions")
    decisions_path = _resolve_local_locator(root, decisions, required=False, kind="Decisions")
    evidence_path = _resolve_local_locator(
        root,
        evidence,
        required=False,
        kind="Evidence",
        expect_directory=True,
    )
    parts.append(("state", state_path.read_bytes()))
    parts.append(("next_actions", next_path.read_bytes()))
    if decisions_path is not None:
        parts.append(("decisions", decisions_path.read_bytes()))
    if evidence_path is not None:
        for child in sorted(evidence_path.iterdir()):
            if not child.is_file():
                continue
            resolved = child.resolve()
            if not resolved.is_relative_to(root):
                raise discovery_failure(
                    "AGNIR_DISCOVERY_UNRESOLVABLE",
                    f"Evidence child {child.name!r} escapes the selected Project root",
                )
            parts.append((f"evidence/{child.name}", resolved.read_bytes()))
    return _digest_bytes(parts)


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
            newline = "\r\n" if line.endswith("\r\n") else ("\n" if line.endswith("\n") else "")
            output.append('  version: "1.0"' + newline)
            version_replaced = True
            continue
        if section == "agnir" and stripped.startswith("discovery_profile:"):
            newline = "\r\n" if line.endswith("\r\n") else ("\n" if line.endswith("\n") else "")
            output.append('  discovery_profile: "repository-filesystem/1.0"' + newline)
            profile_replaced = True
            continue
        output.append(line)

    if not version_replaced or not profile_replaced:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "Core/profile 0.2 manifest does not contain required Agnir compatibility scalars",
        )
    return "".join(output)


def _validate_semantics_preserving_candidate(
    source_data: dict[str, object],
    candidate_text: str,
) -> None:
    candidate_data = _parse_manifest_text(candidate_text)
    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate_data),
        key=lambda error: (list(error.absolute_path), error.message),
    )
    if errors:
        first = errors[0]
        location = ".".join(str(item) for item in first.absolute_path) or "<root>"
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"staged 1.0 promotion candidate violates published schema at {location}: {first.message}",
        )

    expected = deepcopy(source_data)
    agnir = expected.get("agnir")
    if not isinstance(agnir, dict):
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "promotion source is missing an Agnir compatibility mapping",
        )
    agnir["version"] = CORE_1_0
    agnir["discovery_profile"] = PROFILE_1_0
    if candidate_data != expected:
        raise MigrationConflict(
            f"{MigrationConflict.code}: staged 1.0 candidate changes data beyond the compatibility declaration"
        )


def stage_repository_filesystem_0_2_to_1_0(
    project_root: str | Path,
    *,
    authorized: bool,
    expected_project_identity: str | None = None,
    expected_lineage_identity: str | None = None,
) -> RepositoryFilesystem10PromotionCandidate:
    root = Path(project_root).resolve()
    manifest_path = root / "AGNIR.yaml"
    if not manifest_path.is_file():
        raise discovery_failure(
            "AGNIR_DISCOVERY_NOT_FOUND",
            "promotion could not resolve top-level AGNIR.yaml",
        )

    text = manifest_path.read_text(encoding="utf-8")
    data = _parse_manifest_text(text)
    agnir = data.get("agnir")
    version = agnir.get("version") if isinstance(agnir, dict) else None
    profile = agnir.get("discovery_profile") if isinstance(agnir, dict) else None

    if version == CORE_1_0 and profile == PROFILE_1_0:
        snapshot = discover_repository_filesystem_1_0(
            root,
            expected_project_identity=expected_project_identity,
            expected_lineage_identity=expected_lineage_identity,
        )
        return RepositoryFilesystem10PromotionCandidate(
            project_root=root,
            project_identity=snapshot.project_identity,
            lineage_identity=snapshot.lineage_identity,
            source_manifest_digest=_manifest_digest(text),
            source_continuity_digest=_continuity_digest(root, text, data),
            candidate_manifest_text=text,
            changed=False,
            source_snapshot=None,
        )

    if version != CORE_0_2 or profile != PROFILE_0_2:
        if isinstance(version, str) and version not in {CORE_0_2, CORE_1_0}:
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                f"expected Core/profile 0.2 promotion source, discovered {version!r}/{profile!r}",
            )
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"expected exact {CORE_0_2}/{PROFILE_0_2} promotion source, discovered {version!r}/{profile!r}",
        )

    source_snapshot = discover_repository_filesystem_0_2(
        root,
        expected_project_identity=expected_project_identity,
        expected_lineage_identity=expected_lineage_identity,
    )

    if not authorized:
        raise UpgradeMigrationRequired(
            f"{UpgradeMigrationRequired.code}: Core/profile 0.2 -> 1.0 changes compatibility identifiers"
        )

    candidate_text = _replace_agnir_compatibility(text)
    _validate_semantics_preserving_candidate(data, candidate_text)

    return RepositoryFilesystem10PromotionCandidate(
        project_root=root,
        project_identity=source_snapshot.project_identity,
        lineage_identity=source_snapshot.lineage_identity,
        source_manifest_digest=_manifest_digest(text),
        source_continuity_digest=_continuity_digest(root, text, data),
        candidate_manifest_text=candidate_text,
        changed=True,
        source_snapshot=source_snapshot,
    )


def publish_repository_filesystem_1_0_promotion(
    candidate: RepositoryFilesystem10PromotionCandidate,
) -> tuple[DiscoverySnapshot10, bool]:
    manifest_path = candidate.project_root / "AGNIR.yaml"
    current_text = manifest_path.read_text(encoding="utf-8")

    if not candidate.changed:
        snapshot = discover_repository_filesystem_1_0(
            candidate.project_root,
            expected_project_identity=candidate.project_identity,
            expected_lineage_identity=candidate.lineage_identity,
        )
        return snapshot, False

    if _manifest_digest(current_text) != candidate.source_manifest_digest:
        raise MigrationConflict(
            f"{MigrationConflict.code}: authoritative manifest changed after 1.0 promotion staging"
        )

    current_data = _parse_manifest_text(current_text)
    if _continuity_digest(candidate.project_root, current_text, current_data) != candidate.source_continuity_digest:
        raise MigrationConflict(
            f"{MigrationConflict.code}: authoritative continuity changed after 1.0 promotion staging"
        )

    _validate_semantics_preserving_candidate(current_data, candidate.candidate_manifest_text)

    temp_path = candidate.project_root / ".AGNIR.yaml.agnir-1.0-promotion.tmp"
    try:
        with temp_path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(candidate.candidate_manifest_text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, manifest_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    snapshot = discover_repository_filesystem_1_0(
        candidate.project_root,
        expected_project_identity=candidate.project_identity,
        expected_lineage_identity=candidate.lineage_identity,
    )
    source = candidate.source_snapshot
    if source is not None and (
        snapshot.state != source.state
        or snapshot.next_actions != source.next_actions
        or snapshot.decisions != source.decisions
        or snapshot.evidence != source.evidence
    ):
        raise MigrationConflict(
            f"{MigrationConflict.code}: 1.0 promotion did not preserve durable continuity"
        )
    return snapshot, True
