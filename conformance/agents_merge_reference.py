from __future__ import annotations


class AgentsMergeConflict(RuntimeError):
    """Raised when installing the Agnir locator would conflict with existing instructions."""


AGNIR_LOCATOR_BLOCK = """## Agnir

Before Project work, read and follow `AGNIR.md`.

This is a locator only. `AGNIR.md` is the canonical Agnir activation and Project-operation instruction; do not duplicate the full Agnir rules here.
"""

# Deliberately small, explicit conformance vocabulary. Production Executors still have to
# reason about semantic conflicts beyond these exact phrases rather than guessing.
_EXPLICIT_CONFLICTS = (
    "do not read agnir.md",
    "don't read agnir.md",
    "ignore agnir.md",
    "do not follow agnir.md",
    "do not read agnir.yaml",
    "ignore agnir.yaml",
    "do not use agnir",
    "disable agnir",
)


def _upgrade_legacy_locator(original: str) -> str | None:
    lines = original.splitlines(keepends=True)
    changed = False
    upgraded: list[str] = []
    for line in lines:
        lowered = line.casefold()
        if "agnir project instructions" in lowered and "readme.md" in lowered:
            ending = "\n" if line.endswith("\n") else ""
            upgraded.append("Before Project work, read and follow `AGNIR.md`." + ending)
            changed = True
            continue
        if "readme section" in lowered and "canonical agnir" in lowered:
            ending = "\n" if line.endswith("\n") else ""
            upgraded.append("`AGNIR.md` is the canonical Agnir instruction." + ending)
            changed = True
            continue
        upgraded.append(line)
    return "".join(upgraded) if changed else None


def merge_agents_locator(existing: str | None) -> str:
    """Reference non-destructive merge for the Agnir AGENTS.md locator.

    Existing unrelated content is preserved. Explicitly contradictory instructions fail
    before mutation. The v1.0.0 README locator is upgraded in place to the v1.0.1
    `AGNIR.md` locator; an existing v1.0.1 locator is idempotent.
    """

    original = existing or ""
    lowered = original.casefold()

    if any(marker in lowered for marker in _EXPLICIT_CONFLICTS):
        raise AgentsMergeConflict(
            "AGNIR_INSTALL_AGENTS_CONFLICT: existing AGENTS.md materially conflicts "
            "with durable Agnir activation"
        )

    if "agnir.md" in lowered and "agnir" in lowered:
        return original

    upgraded = _upgrade_legacy_locator(original)
    if upgraded is not None:
        return upgraded

    if not original:
        return "# Agent Instructions\n\n" + AGNIR_LOCATOR_BLOCK

    if original.endswith("\n\n"):
        separator = ""
    elif original.endswith("\n"):
        separator = "\n"
    else:
        separator = "\n\n"

    return original + separator + AGNIR_LOCATOR_BLOCK
