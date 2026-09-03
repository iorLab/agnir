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
            "fresh repository activation test",
            "### Complete execution-surface activation",
            "## Upgrade an existing Agnir Project",
            "## Resume or use an existing Agnir Project",
            "## Checkpoint",
            "## Commit and push integration",
            "## Repair",
        ):
            self.assertIn(marker, text)

    def test_skill_defines_execution_surface_activation_handoff(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "Repository activation and execution-surface activation are separate completion dimensions",
            "copy-ready execution-surface handoff",
            "pending user configuration",
            "Do not report full fresh activation as passed",
            "ChatGPT Project",
            "Agnir Project bootstrap",
            "Canonical Project: <owner/repository>",
            "Authoritative ref: <ref>",
            "At the first substantive turn of every new conversation",
            "append or merge",
            "do not overwrite unrelated existing Project Instructions",
            "repository activation status",
            "execution-surface activation status",
        ):
            self.assertIn(marker, text)

        chatgpt_block = text.split("```text\nAgnir Project bootstrap", 1)[1].split("```", 1)[0]
        self.assertIn("read root AGENTS.md", chatgpt_block)
        self.assertIn("AGNIR.yaml", chatgpt_block)
        self.assertIn("canonical durable Project truth", chatgpt_block)
        self.assertNotIn("Current State", chatgpt_block)
        self.assertNotIn("Next Actions", chatgpt_block)

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

    def test_skill_defines_core_0_2_migration_and_lineage_selection(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "spec/AGNIR_CORE_0_2.md",
            "profiles/REPOSITORY_FILESYSTEM_0_2.md",
            "spec/CORE_0_1_TO_0_2_MIGRATION.md",
            "## Migrate Core/profile compatibility",
            "continuity.lineage",
            "not automatically lineage identity",
            "AGNIR_LINEAGE_REQUIRED",
            "## Integrate Continuity Lineages",
            "without advancing the target",
            "source continuity is input, not automatic target truth",
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

    def test_readmes_explain_execution_surface_handoff(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        for marker in (
            "one-time persistent Project locator",
            "copy-ready handoff",
            "surface activation separately from repository activation",
            "Execution-surface bootstrap",
            "append Project locator only",
        ):
            self.assertIn(marker, english)

        for marker in (
            "一次性的持久 Project locator",
            "可直接复制的 handoff",
            "execution-surface configuration",
            "Execution-surface bootstrap",
            "仅追加 Project locator",
        ):
            self.assertIn(marker, chinese)

    def test_readme_project_surface_marks_add_vs_entry_only(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        surface_en = english.split("## What Agnir Adds to a Project", 1)[1].split("## Architecture Diagram", 1)[0]
        surface_zh = chinese.split("## Agnir 会给 Project 增加什么", 1)[1].split("## 架构图", 1)[0]

        self.assertIn("Agnir does not take over existing Project files.", surface_en)
        self.assertIn("[EDIT: add entry only]", surface_en)
        self.assertGreaterEqual(surface_en.count("[EDIT: add entry only]"), 2)
        self.assertGreaterEqual(surface_en.count("[ADD]"), 6)
        self.assertIn("preserve existing instructions", surface_en)
        self.assertIn("preserve existing content", surface_en)

        self.assertIn("Agnir 不会接管已有 Project 文件。", surface_zh)
        self.assertIn("[编辑：仅添加入口]", surface_zh)
        self.assertGreaterEqual(surface_zh.count("[编辑：仅添加入口]"), 2)
        self.assertGreaterEqual(surface_zh.count("[新增]"), 6)
        self.assertIn("保留原有 instructions", surface_zh)
        self.assertIn("保留原有内容", surface_zh)

    def test_readmes_do_not_claim_core_0_2_lineage_is_deferred(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        for text in (english, chinese):
            self.assertIn("Core `0.2`", text)
            self.assertIn("Continuity Lineage", text)
            self.assertNotIn("generic durable lineage is still deferred", text)
            self.assertNotIn("AGNIR_CORE_0_2_DRAFT.md", text)
            self.assertNotIn("REPOSITORY_FILESYSTEM_0_2_DRAFT.md", text)

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
