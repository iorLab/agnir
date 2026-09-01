from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    def test_root_skill_has_agent_skill_frontmatter(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("\nname: agnir\n", text)
        self.assertIn("\ndescription:", text)

    def test_skill_owns_full_operational_procedure(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "Do not require the user to carry Agnir's implementation checklist",
            "## Install or initialize Agnir",
            "### Merge existing AGENTS.md safely",
            "preserve its existing unrelated content",
            "equivalent Agnir locator already exists",
            "do not guess and do not overwrite it",
            "report the exact conflict to the Principal",
            "AGNIR.yaml",
            ".agnir/state.md",
            ".agnir/next-actions.md",
            ".agnir/decisions.md",
            ".agnir/evidence/",
            "## Agnir Project Instructions",
            "AGENTS.md",
            "fresh activation test",
            "## Upgrade an existing Agnir Project",
            "## Resume or use an existing Agnir Project",
            "## Checkpoint",
            "## Commit and push integration",
            "## Repair",
        ):
            self.assertIn(marker, text)

    def test_skill_defines_transactional_checkpoint_and_repository_intent(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "no-op",
            "candidate checkpoint",
            "AGNIR_CHECKPOINT_CONFLICT",
            "one VCS revision",
            "提交代码",
            "提交推送",
            "checkpoint evaluation",
            "not by global string matching",
        ):
            self.assertIn(marker, text)

    def test_skill_defines_non_destructive_upgrade(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "Upgrade is **not re-initialization**",
            "latest stable release",
            "Do not silently treat `main`",
            "compatible operational upgrade",
            "AGNIR_UPGRADE_MIGRATION_REQUIRED",
            "agnir/operations",
            "applied_revision",
            "Preserve `project.identity`",
            "upgrade evaluation is a no-op",
        ):
            self.assertIn(marker, text)

    def test_readmes_keep_user_prompts_short_and_copyable(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        install_en = "Install and initialize Agnir for this Project: https://github.com/iorLab/agnir"
        upgrade_en = "Upgrade Agnir to the latest stable release: https://github.com/iorLab/agnir"
        install_zh = "为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir"
        upgrade_zh = "把这个 Project 的 Agnir 升级到最新稳定版：https://github.com/iorLab/agnir"

        for prompt in (install_en, upgrade_en):
            self.assertIn(f"```text\n{prompt}\n```", english)
        for prompt in (install_zh, upgrade_zh):
            self.assertIn(f"```text\n{prompt}\n```", chinese)

        self.assertIn("SKILL.md", english)
        self.assertIn("SKILL.md", chinese)

        user_entry_en = english.split("## Agnir Project Instructions", 1)[0]
        user_entry_zh = chinese.split("## Agnir Project Instructions", 1)[0]
        self.assertNotIn("Requirements:\n1.", user_entry_en)
        self.assertNotIn("要求：\n1.", user_entry_zh)

    def test_initialized_project_instructions_persist_commit_boundary_semantics(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        section_en = english.split("## Agnir Project Instructions", 1)[1].split("\n## ", 1)[0]
        section_zh = chinese.split("## Agnir Project Instructions", 1)[1].split("\n## ", 1)[0]

        for marker in ("commit", "提交代码", "提交推送", "commit boundary"):
            self.assertIn(marker, section_en)
            self.assertIn(marker, section_zh)


if __name__ == "__main__":
    unittest.main()
