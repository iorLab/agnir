from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ACTIVATION_HEADING = "## Agnir Project Instructions"
CANONICAL_INSTRUCTIONS = "AGNIR.md"


class ActivationFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class ActivationSnapshot:
    agents_path: Path
    readme_path: Path
    # Compatibility field retained for pre-1.0.1 self-host helpers. On the new
    # direct route it contains the canonical instruction content from AGNIR.md.
    readme_section: str
    instructions_path: Path
    instructions: str
    route: str


def _extract_section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        raise ActivationFailure(f"AGNIR_ACTIVATION_NOT_FOUND: missing README section {heading}")
    remainder = text[start + len(heading) :]
    next_heading = remainder.find("\n## ")
    if next_heading >= 0:
        remainder = remainder[:next_heading]
    return heading + remainder


def _validate_instructions(text: str, *, source: str) -> None:
    for marker in (
        "Project Entry Point",
        "AGNIR.yaml",
        "Current State",
        "Next Actions",
        "Decisions",
        "Evidence",
        "checkpoint",
    ):
        if marker not in text:
            raise ActivationFailure(
                f"AGNIR_ACTIVATION_INCOMPLETE: {source} activation instructions missing {marker}"
            )


def _reject_agents_procedure_fork(agents_text: str) -> None:
    duplicated_markers = sum(
        marker in agents_text
        for marker in ("Current State", "Next Actions", "Decisions", "Evidence", "checkpoint")
    )
    if duplicated_markers >= 3:
        raise ActivationFailure(
            "AGNIR_ACTIVATION_INCONSISTENT: AGENTS.md duplicates the canonical activation contract"
        )


def resolve_agent_activation(project_root: Path) -> ActivationSnapshot:
    root = project_root.resolve()
    agents_path = root / "AGENTS.md"
    readme_path = root / "README.md"
    instructions_path = root / CANONICAL_INSTRUCTIONS

    if not agents_path.is_file():
        raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: missing AGENTS.md")

    agents_text = agents_path.read_text(encoding="utf-8")
    _reject_agents_procedure_fork(agents_text)

    # v1.0.1 canonical route: AGENTS.md -> AGNIR.md -> AGNIR.yaml -> continuity.
    if CANONICAL_INSTRUCTIONS.casefold() in agents_text.casefold():
        if not instructions_path.is_file():
            raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: AGENTS.md points to missing AGNIR.md")
        instructions = instructions_path.read_text(encoding="utf-8")
        _validate_instructions(instructions, source="AGNIR.md")
        for marker in ("checkpoint evaluation", "commit", "提交"):
            if marker not in instructions:
                raise ActivationFailure(
                    f"AGNIR_ACTIVATION_INCOMPLETE: AGNIR.md operation instructions missing {marker}"
                )

        if not readme_path.is_file():
            raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: missing README.md compatibility locator")
        compatibility_section = _extract_section(
            readme_path.read_text(encoding="utf-8"), ACTIVATION_HEADING
        )
        if CANONICAL_INSTRUCTIONS not in compatibility_section:
            raise ActivationFailure(
                "AGNIR_ACTIVATION_UNRESOLVABLE: README compatibility section must point to AGNIR.md"
            )
        copied_markers = sum(
            marker in compatibility_section
            for marker in ("Current State", "Next Actions", "Decisions", "Evidence", "checkpoint evaluation")
        )
        if copied_markers >= 3:
            raise ActivationFailure(
                "AGNIR_ACTIVATION_INCONSISTENT: README compatibility locator duplicates AGNIR.md procedure"
            )

        return ActivationSnapshot(
            agents_path=agents_path,
            readme_path=readme_path,
            readme_section=instructions,
            instructions_path=instructions_path,
            instructions=instructions,
            route="agnir-md",
        )

    # Backward-compatible v1.0.0 route so an existing Project can activate before upgrade.
    if "README.md" in agents_text and "Agnir Project Instructions" in agents_text:
        if not readme_path.is_file():
            raise ActivationFailure("AGNIR_ACTIVATION_NOT_FOUND: missing README.md")
        readme_section = _extract_section(readme_path.read_text(encoding="utf-8"), ACTIVATION_HEADING)
        _validate_instructions(readme_section, source="legacy README")
        return ActivationSnapshot(
            agents_path=agents_path,
            readme_path=readme_path,
            readme_section=readme_section,
            instructions_path=readme_path,
            instructions=readme_section,
            route="legacy-readme",
        )

    raise ActivationFailure(
        "AGNIR_ACTIVATION_UNRESOLVABLE: AGENTS.md must point to AGNIR.md or the legacy README.md Agnir Project Instructions"
    )
