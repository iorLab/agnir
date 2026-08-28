from __future__ import annotations


CORE_VERSION = "0.1"


class DiscoveryFailure(RuntimeError):
    """Conformance-only carrier for Agnir discovery semantic failure classes."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


def discovery_failure(code: str, message: str) -> DiscoveryFailure:
    return DiscoveryFailure(code, message)
