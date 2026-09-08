from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryOperationPlan:
    intent: str
    steps: tuple[str, ...]


_COMMIT_INTENTS = {"commit", "提交", "提交代码"}
_PUSH_INTENTS = {"commit and push", "commit & push", "提交推送"}


def classify_repository_intent(intent: str, *, repository_context: bool) -> RepositoryOperationPlan | None:
    """Reference intent dispatcher for Agnir-aware repository operations.

    Exact short intents are intercepted only in repository context. This intentionally
    avoids global substring matching while making the required checkpoint boundary
    explicit before any VCS mutation.
    """

    if not repository_context:
        return None

    normalized = " ".join(intent.strip().casefold().split())
    if normalized in _COMMIT_INTENTS:
        return RepositoryOperationPlan(
            intent="commit",
            steps=(
                "checkpoint_evaluation",
                "project_precommit_policy_if_declared",
                "commit",
            ),
        )
    if normalized in _PUSH_INTENTS:
        return RepositoryOperationPlan(
            intent="commit-and-push",
            steps=(
                "checkpoint_evaluation",
                "project_precommit_policy_if_declared",
                "commit",
                "push",
                "verify_destination_ref",
            ),
        )
    return None
