from __future__ import annotations


class AgentsMergeConflict(RuntimeError):
    """Raised when installing the Agnir locator would conflict with existing instructions."""


AGNIR_LOCATOR_BLOCK = """## Agnir

Before Project work, read and follow the **Agnir Project Instructions** section in `README.md`.

This is a locator only. The README section is the canonical Agnir instruction; do not duplicate the full Agnir rules here.
"""

# Deliberately small, explicit conformance vocabulary. Production Agents still have to
# reason about semantic conflicts beyond these exact phrases rather than guessing.
_EXPLICIT_CONFLICTS = (
    "do not read readme.md",
    "don't read readme.md",
    "ignore readme.md",
    "do not follow readme.md",
    "do not read agnir.yaml",
    "ignore agnir.yaml",
    "do not use agnir",
    "disable agnir",
)


def merge_agents_locator(existing: str | None) -> str:
    """Reference non-destructive merge for the Agnir AGENTS.md locator.

    Existing content is preserved exactly as a prefix. Explicitly contradictory
    instructions fail before mutation. An existing equivalent locator is idempotent.
    """

    original = existing or ""
    lowered = original.casefold()

    if any(marker in lowered for marker in _EXPLICIT_CONFLICTS):
        raise AgentsMergeConflict(
            "AGNIR_INSTALL_AGENTS_CONFLICT: existing AGENTS.md materially conflicts "
            "with durable Agnir activation"
        )

    if "agnir project instructions" in lowered and "readme.md" in lowered:
        return original

    if not original:
        return "# Agent Instructions\n\n" + AGNIR_LOCATOR_BLOCK

    if original.endswith("\n\n"):
        separator = ""
    elif original.endswith("\n"):
        separator = "\n"
    else:
        separator = "\n\n"

    return original + separator + AGNIR_LOCATOR_BLOCK
