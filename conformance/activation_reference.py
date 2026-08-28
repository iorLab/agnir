from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ACTIVATION_HEADING = "## Agnir Project Instructions"


class ActivationFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class ActivationSnapshot:
    agents_path: Path
    readme_path: Path
    readme_section: str


def _extract_section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        raise ActivationFailure(f"AGNIR_ACTIVATION_NOT_FOUND: missing README section {heading}")
    remainder = text[start + len(heading) :]
    next_heading = remainder.find("\n## ")
    if next_heading >= 0:
        remainder = remainder[:next_heading]
    return heading + remainder


def resolve_agent_activation(project_root: Path) -> ActivationSnapshot:
    root = project_root.resolve()
    agents_path = root / "AGENTS.md"
    readme_path = root / "README.md"

    if not agents_path.is_file():
        raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: missing AGENTS.md")
    if not readme_path.is_file():
        raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: missing README.md")

    agents_text = agents_path.read_text(encoding="utf-8")
    if "README.md" not in agents_text or "Agnir Project Instructions" not in agents_text:
        raise ActivationFailure(
            "AGNIR_ACTIVATION_UNRESOLVABLE: AGENTS.md must point to README.md Agnir Project Instructions"
        )

    readme_text = readme_path.read_text(encoding="utf-8")
    section = _extract_section(readme_text, ACTIVATION_HEADING)
    for marker in (
        "Project Entry Point",
        "AGNIR.yaml",
        "Current State",
        "Next Actions",
        "Decisions",
        "Evidence",
        "checkpoint",
    ):
        if marker not in section:
            raise ActivationFailure(
                f"AGNIR_ACTIVATION_INCOMPLETE: README activation section missing {marker}"
            )

    duplicated_markers = sum(
        marker in agents_text
        for marker in ("Current State", "Next Actions", "Decisions", "Evidence", "checkpoint")
    )
    if duplicated_markers >= 3:
        raise ActivationFailure(
            "AGNIR_ACTIVATION_INCONSISTENT: AGENTS.md duplicates the canonical README activation contract"
        )

    return ActivationSnapshot(
        agents_path=agents_path,
        readme_path=readme_path,
        readme_section=section,
    )
