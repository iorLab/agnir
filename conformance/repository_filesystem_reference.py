from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from core_reference import CORE_VERSION, DiscoveryFailure, discovery_failure


PROFILE = "repository-filesystem/0.1"


@dataclass(frozen=True)
class DiscoverySnapshot:
    project_root: Path
    project_identity: str
    version: str
    profile: str
    state: str
    next_actions: str
    decisions: str | None
    evidence: dict[str, str]


def _strip_scalar(value: str) -> str | None:
    value = value.strip()
    if value in {"null", "Null", "NULL", "~"}:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_scalars(text: str) -> dict[tuple[str, str], str | None]:
    values: dict[tuple[str, str], str | None] = {}
    section: str | None = None
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        top = re.match(r"^([A-Za-z0-9_/-]+):\s*$", raw)
        if top:
            section = top.group(1)
            continue
        if section is None:
            continue
        scalar = re.match(r"^\s{2}([A-Za-z0-9_/-]+):\s*(.*?)\s*$", raw)
        if scalar:
            values[(section, scalar.group(1))] = _strip_scalar(scalar.group(2))
    return values


def _resolve_local_locator(
    root: Path,
    locator: str | None,
    *,
    required: bool,
    kind: str,
    expect_directory: bool = False,
) -> Path | None:
    if locator is None:
        if required:
            raise discovery_failure(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                f"required {kind} locator is null or missing",
            )
        return None

    if "://" in locator:
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            f"{kind} uses an external locator but this local conformance resolver has no authorized external binding",
        )

    candidate = (root / locator).resolve()
    if not candidate.is_relative_to(root):
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            f"{kind} locator escapes the selected Project root without an authorized external Locator Chain",
        )
    if not candidate.exists():
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            f"{kind} locator does not resolve: {locator}",
        )
    if expect_directory and not candidate.is_dir():
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            f"{kind} locator is not a directory",
        )
    if not expect_directory and not candidate.is_file():
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNRESOLVABLE",
            f"{kind} locator is not a file",
        )
    return candidate


def select_unique_project_root(candidates: list[str | Path]) -> Path:
    """Core-level authority selection before repository/filesystem root discovery.

    Once a repository/filesystem Project root is selected, nested parent/child
    projects do not make that root ambiguous. Ambiguity belongs here: multiple
    candidate roots exist and no authority rule has selected one.
    """

    unique = sorted({Path(candidate).resolve() for candidate in candidates}, key=str)
    if not unique:
        raise discovery_failure(
            "AGNIR_DISCOVERY_NOT_FOUND",
            "no candidate Project root is available",
        )
    if len(unique) != 1:
        raise discovery_failure(
            "AGNIR_DISCOVERY_AMBIGUOUS",
            "multiple candidate Project roots exist and authority cannot be determined",
        )
    return unique[0]


def discover_repository_filesystem(
    project_root: str | Path,
    *,
    expected_project_identity: str | None = None,
) -> DiscoverySnapshot:
    root = Path(project_root).resolve()
    manifest = root / "AGNIR.yaml"
    if not manifest.is_file():
        raise discovery_failure(
            "AGNIR_DISCOVERY_NOT_FOUND",
            "repository/filesystem profile could not resolve top-level AGNIR.yaml at the selected Project root",
        )

    values = _parse_scalars(manifest.read_text(encoding="utf-8"))
    version = values.get(("agnir", "version"))
    profile = values.get(("agnir", "discovery_profile"))
    identity = values.get(("project", "identity"))

    if version != CORE_VERSION:
        raise discovery_failure(
            "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
            f"expected Agnir Core {CORE_VERSION}, discovered {version!r}",
        )
    if profile != PROFILE:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            f"expected discovery profile {PROFILE}, discovered {profile!r}",
        )
    if not identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            "project.identity is missing",
        )
    if expected_project_identity is not None and identity != expected_project_identity:
        raise discovery_failure(
            "AGNIR_DISCOVERY_PROJECT_MISMATCH",
            f"expected {expected_project_identity!r}, discovered {identity!r}",
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

    return DiscoverySnapshot(
        project_root=root,
        project_identity=identity,
        version=version,
        profile=profile,
        state=state_path.read_text(encoding="utf-8"),
        next_actions=next_path.read_text(encoding="utf-8"),
        decisions=None if decisions_path is None else decisions_path.read_text(encoding="utf-8"),
        evidence=evidence,
    )
