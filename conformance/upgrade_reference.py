from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


class UpgradeTargetRejected(RuntimeError):
    code = "AGNIR_UPGRADE_TARGET_REJECTED"


class UpgradeMigrationRequired(RuntimeError):
    code = "AGNIR_UPGRADE_MIGRATION_REQUIRED"


@dataclass(frozen=True)
class OperationalTarget:
    core_version: str
    discovery_profile: str
    distribution: str
    release: str
    source: str
    revision: str
    stable: bool = True


def classify_upgrade(
    manifest: dict,
    target: OperationalTarget,
    *,
    allow_unstable: bool = False,
) -> str:
    """Classify an Agnir operational-package upgrade without mutating Project truth."""
    if not target.stable and not allow_unstable:
        raise UpgradeTargetRejected(
            f"{UpgradeTargetRejected.code}: target {target.release}@{target.revision} is not a stable release"
        )

    agnir = manifest.get("agnir", {})
    current_core = agnir.get("version")
    current_profile = agnir.get("discovery_profile")
    if current_core != target.core_version or current_profile != target.discovery_profile:
        raise UpgradeMigrationRequired(
            f"{UpgradeMigrationRequired.code}: {current_core}/{current_profile} -> "
            f"{target.core_version}/{target.discovery_profile} changes a compatibility line"
        )

    operations = manifest.get("extensions", {}).get("agnir/operations")
    if not isinstance(operations, dict):
        return "compatible-upgrade"

    if (
        operations.get("distribution") == target.distribution
        and operations.get("release") == target.release
        and operations.get("source") == target.source
        and operations.get("applied_revision") == target.revision
    ):
        return "no-op"

    return "compatible-upgrade"


def apply_compatible_upgrade(manifest: dict, target: OperationalTarget) -> tuple[dict, bool]:
    """Return a copied manifest with only operational provenance changed.

    This reference intentionally does not rewrite Project identity, Core/profile
    compatibility fields, memory locators, or unrelated extensions.
    """
    classification = classify_upgrade(manifest, target)
    if classification == "no-op":
        return deepcopy(manifest), False

    upgraded = deepcopy(manifest)
    extensions = upgraded.setdefault("extensions", {})
    extensions["agnir/operations"] = {
        "distribution": target.distribution,
        "release": target.release,
        "source": target.source,
        "applied_revision": target.revision,
    }
    return upgraded, True
