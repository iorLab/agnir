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

    def test_skill_owns_full_install_procedure(self) -> None:
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
            "## Resume or use an existing Agnir Project",
            "## Checkpoint",
            "## Repair",
        ):
            self.assertIn(marker, text)

    def test_readmes_keep_user_install_prompt_short(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn(
            "Install and initialize Agnir for this Project: https://github.com/iorLab/agnir",
            english,
        )
        self.assertIn(
            "为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir",
            chinese,
        )
        self.assertIn("SKILL.md", english)
        self.assertIn("SKILL.md", chinese)

        quick_start_en = english.split("## Agnir Project Instructions", 1)[0]
        quick_start_zh = chinese.split("## Agnir Project Instructions", 1)[0]
        self.assertNotIn("Requirements:\n1.", quick_start_en)
        self.assertNotIn("要求：\n1.", quick_start_zh)


if __name__ == "__main__":
    unittest.main()
