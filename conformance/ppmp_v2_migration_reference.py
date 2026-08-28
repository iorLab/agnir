from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


PPMP_V2 = "2.0.0"
AGNIR_VERSION = "0.1"
AGNIR_PROFILE = "repository-filesystem/0.1"


class PPMPMigrationFailure(RuntimeError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


@dataclass(frozen=True)
class PPMPV2Snapshot:
    project_root: Path
    project_name: str
    state: str
    next_actions: str
    decisions: str
    checkpoints: dict[str, str]


def _strip_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_scalars(text: str) -> dict[tuple[str, str], str]:
    values: dict[tuple[str, str], str] = {}
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


def _resolve_inside(root: Path, relative: str, *, expect_directory: bool, label: str) -> Path:
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root):
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_UNRESOLVABLE",
            f"{label} escapes the predecessor Project root",
        )
    if not candidate.exists():
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_UNRESOLVABLE",
            f"{label} does not resolve: {relative}",
        )
    if expect_directory and not candidate.is_dir():
        raise PPMPMigrationFailure("PPMP_MIGRATION_UNRESOLVABLE", f"{label} is not a directory")
    if not expect_directory and not candidate.is_file():
        raise PPMPMigrationFailure("PPMP_MIGRATION_UNRESOLVABLE", f"{label} is not a file")
    return candidate


def load_ppmp_v2(project_root: str | Path) -> PPMPV2Snapshot:
    root = Path(project_root).resolve()
    manifest = root / ".chatgpt" / "project-memory.yaml"
    if not manifest.is_file():
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_NOT_FOUND",
            "predecessor .chatgpt/project-memory.yaml is missing",
        )

    values = _parse_scalars(manifest.read_text(encoding="utf-8"))
    version = values.get(("ppmp", "version"))
    if version != PPMP_V2:
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_UNSUPPORTED_PREDECESSOR",
            f"expected PPMP {PPMP_V2}, discovered {version!r}",
        )

    project_name = values.get(("project", "name"))
    memory_root = values.get(("memory", "root"))
    state_name = values.get(("memory", "state"))
    next_name = values.get(("memory", "next_steps"))
    decisions_name = values.get(("memory", "decisions"))
    checkpoints_name = values.get(("memory", "checkpoints"))
    required = {
        "project.name": project_name,
        "memory.root": memory_root,
        "memory.state": state_name,
        "memory.next_steps": next_name,
        "memory.decisions": decisions_name,
        "memory.checkpoints": checkpoints_name,
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_INCONSISTENT",
            f"required predecessor fields are missing: {', '.join(missing)}",
        )

    memory_dir = _resolve_inside(root, memory_root, expect_directory=True, label="memory.root")
    state_path = _resolve_inside(memory_dir, state_name, expect_directory=False, label="state")
    next_path = _resolve_inside(memory_dir, next_name, expect_directory=False, label="next_steps")
    decisions_path = _resolve_inside(memory_dir, decisions_name, expect_directory=False, label="decisions")
    checkpoints_path = _resolve_inside(
        memory_dir,
        checkpoints_name,
        expect_directory=True,
        label="checkpoints",
    )

    checkpoints = {
        item.name: item.read_text(encoding="utf-8")
        for item in sorted(checkpoints_path.iterdir())
        if item.is_file()
    }
    if not checkpoints:
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_INCONSISTENT",
            "predecessor checkpoint directory contains no durable checkpoint evidence",
        )

    return PPMPV2Snapshot(
        project_root=root,
        project_name=project_name,
        state=state_path.read_text(encoding="utf-8"),
        next_actions=next_path.read_text(encoding="utf-8"),
        decisions=decisions_path.read_text(encoding="utf-8"),
        checkpoints=checkpoints,
    )


def materialize_agnir_target(
    source: PPMPV2Snapshot,
    target_root: str | Path,
    *,
    project_identity: str,
) -> Path:
    if not project_identity.strip():
        raise PPMPMigrationFailure(
            "PPMP_MIGRATION_INCONSISTENT",
            "target Agnir Project identity must be explicit",
        )

    root = Path(target_root).resolve()
    memory = root / ".agnir"
    evidence = memory / "evidence"
    evidence.mkdir(parents=True, exist_ok=True)

    (memory / "state.md").write_text(source.state, encoding="utf-8")
    (memory / "next-actions.md").write_text(source.next_actions, encoding="utf-8")
    (memory / "decisions.md").write_text(source.decisions, encoding="utf-8")
    for name, text in source.checkpoints.items():
        (evidence / name).write_text(text, encoding="utf-8")

    (evidence / "migration-ppmp-v2.md").write_text(
        "# PPMP v2 migration\n\n"
        f"Source Project name: {source.project_name}\n\n"
        f"Source format: PPMP {PPMP_V2}\n\n"
        f"Target Agnir identity: {project_identity}\n",
        encoding="utf-8",
    )

    (root / "AGNIR.yaml").write_text(
        "agnir:\n"
        f'  version: "{AGNIR_VERSION}"\n'
        f'  discovery_profile: "{AGNIR_PROFILE}"\n\n'
        "project:\n"
        f'  identity: "{project_identity}"\n\n'
        "memory:\n"
        '  state: ".agnir/state.md"\n'
        '  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n'
        '  evidence: ".agnir/evidence/"\n',
        encoding="utf-8",
    )

    return root
