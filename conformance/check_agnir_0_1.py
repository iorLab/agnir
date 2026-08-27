#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "AGNIR.yaml"
SCHEMA = ROOT / "schemas" / "agnir-manifest.schema.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def section_scalar(text: str, section: str, key: str) -> str | None:
    lines = text.splitlines()
    in_section = False
    for line in lines:
        if re.match(rf"^{re.escape(section)}:\s*$", line):
            in_section = True
            continue
        if in_section and line and not line.startswith((" ", "\t", "#")):
            break
        if in_section:
            m = re.match(rf"^\s{{2}}{re.escape(key)}:\s*(.+?)\s*$", line)
            if m:
                value = m.group(1).strip()
                if value in {"null", "~"}:
                    return None
                return value.strip("\"'")
    return None


def locator_exists(locator: str | None, key: str) -> None:
    if locator is None:
        if key in {"state", "next_actions"}:
            fail(f"required memory locator {key} is null or missing")
        return
    if "://" in locator:
        return  # External locator resolution belongs to a backend-specific fixture.
    target = ROOT / locator
    if not target.exists():
        fail(f"memory locator {key} does not resolve: {locator}")


def main() -> None:
    if not MANIFEST.is_file():
        fail("top-level AGNIR.yaml is missing")
    text = MANIFEST.read_text(encoding="utf-8")

    version = section_scalar(text, "agnir", "version")
    profile = section_scalar(text, "agnir", "discovery_profile")
    identity = section_scalar(text, "project", "identity")

    if version != "0.1":
        fail(f"unsupported or missing Agnir version: {version!r}")
    if profile != "repository-filesystem/0.1":
        fail(f"unexpected discovery profile: {profile!r}")
    if not identity:
        fail("project.identity is missing")

    for key in ("state", "next_actions", "decisions", "evidence"):
        locator_exists(section_scalar(text, "memory", key), key)

    state_locator = section_scalar(text, "memory", "state")
    if state_locator is None or "://" in state_locator:
        fail("self-hosting fixture requires a local state locator")
    state_text = (ROOT / state_locator).read_text(encoding="utf-8")
    if "Durable continuity belongs to the Project" not in state_text:
        fail("cold-start fixture did not recover the expected material durable fact")

    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"manifest schema is not valid JSON: {exc}")
    try:
        version_const = schema["properties"]["agnir"]["properties"]["version"]["const"]
        profile_const = schema["properties"]["agnir"]["properties"]["discovery_profile"]["const"]
    except KeyError as exc:
        fail(f"manifest schema is missing required constants: {exc}")
    if version_const != version or profile_const != profile:
        fail("manifest and JSON Schema version/profile declarations diverge")

    print(f"PASS: Agnir {version} repository/filesystem cold-start structure for {identity}")


if __name__ == "__main__":
    main()
