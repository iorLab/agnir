from __future__ import annotations

import unittest

from core_reference import DiscoveryFailure
from external_memory_reference import (
    ExternalDiscoveryRecord,
    ExternalMemoryReference,
    ExternalMemoryRegistry,
    ExternalProjectEntryPoint,
)


PROJECT_ID = "urn:test:agnir-external-project"
DISCOVERY = "external://registry/projects/project-a"
AUTH_REF = "credential-ref://vault/agnir/project-a"
STATE = "external://memory/project-a/state"
NEXT = "external://memory/project-a/next"
DECISIONS = "external://memory/project-a/decisions"


class RecordingAuthorization:
    def __init__(self, granted_refs: set[str] | None = None) -> None:
        self.granted_refs = granted_refs or set()
        self.calls: list[str] = []

    def __call__(self, reference: str) -> bool:
        self.calls.append(reference)
        return reference in self.granted_refs


def populated_registry() -> ExternalMemoryRegistry:
    registry = ExternalMemoryRegistry()
    registry.put_record(
        DISCOVERY,
        ExternalDiscoveryRecord(
            project_identity=PROJECT_ID,
            authorization_ref=AUTH_REF,
            state_locator=STATE,
            next_actions_locator=NEXT,
            decisions_locator=DECISIONS,
        ),
    )
    registry.put_object(STATE, "# State\nexternal durable fact\n")
    registry.put_object(NEXT, "# Next\ncontinue external work\n")
    registry.put_object(DECISIONS, "# Decisions\nexternal memory is authoritative\n")
    return registry


class ExternalMemoryAuthorizationTests(unittest.TestCase):
    def test_unknown_discovery_record_is_not_found_without_auth_attempt(self) -> None:
        authorization = RecordingAuthorization()
        resolver = ExternalMemoryReference(populated_registry(), authorization)

        with self.assertRaises(DiscoveryFailure) as raised:
            resolver.load(
                ExternalProjectEntryPoint("external://registry/projects/missing"),
                expected_project_identity=PROJECT_ID,
            )

        self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_NOT_FOUND")
        self.assertEqual(authorization.calls, [])

    def test_known_discovery_record_without_grant_is_unauthorized(self) -> None:
        authorization = RecordingAuthorization()
        resolver = ExternalMemoryReference(populated_registry(), authorization)

        with self.assertRaises(DiscoveryFailure) as raised:
            resolver.load(
                ExternalProjectEntryPoint(DISCOVERY),
                expected_project_identity=PROJECT_ID,
            )

        self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNAUTHORIZED")
        self.assertEqual(authorization.calls, [AUTH_REF])
        self.assertNotIn("token", str(raised.exception).lower())
        self.assertNotIn("password", str(raised.exception).lower())

    def test_authorized_reference_loads_external_continuity(self) -> None:
        authorization = RecordingAuthorization({AUTH_REF})
        resolver = ExternalMemoryReference(populated_registry(), authorization)

        snapshot = resolver.load(
            ExternalProjectEntryPoint(DISCOVERY),
            expected_project_identity=PROJECT_ID,
        )

        self.assertEqual(snapshot.project_identity, PROJECT_ID)
        self.assertIn("external durable fact", snapshot.state)
        self.assertIn("continue external work", snapshot.next_actions)
        self.assertIn("external memory is authoritative", snapshot.decisions)
        self.assertEqual(authorization.calls, [AUTH_REF])

    def test_authorized_but_missing_state_is_unresolvable_not_unauthorized(self) -> None:
        registry = populated_registry()
        del registry.objects[STATE]
        authorization = RecordingAuthorization({AUTH_REF})
        resolver = ExternalMemoryReference(registry, authorization)

        with self.assertRaises(DiscoveryFailure) as raised:
            resolver.load(
                ExternalProjectEntryPoint(DISCOVERY),
                expected_project_identity=PROJECT_ID,
            )

        self.assertEqual(raised.exception.code, "AGNIR_DISCOVERY_UNRESOLVABLE")
        self.assertEqual(authorization.calls, [AUTH_REF])

    def test_fixture_carries_authorization_reference_not_secret_value(self) -> None:
        registry = populated_registry()
        record = registry.discovery_records[DISCOVERY]

        self.assertEqual(record.authorization_ref, AUTH_REF)
        self.assertTrue(record.authorization_ref.startswith("credential-ref://"))
        self.assertFalse(hasattr(record, "credential"))
        self.assertFalse(hasattr(record, "secret"))
        self.assertFalse(hasattr(record, "token"))


if __name__ == "__main__":
    unittest.main()
