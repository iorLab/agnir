# Repository Tree / 目录树

本页是 `iorLab/agnir` 当前 `main` 的**完整文件级仓库结构说明**。README 中的仓库树只用于快速导航；这里展开当前 tracked 文件，并说明它们在 Skill packaging、协议、profile、conformance、本 Project continuity 和历史参考中的职责。

维护规则：只要仓库新增、删除、移动文件，或者某个目录 / 文件职责发生实质变化，就必须在同一个 change set 中同步更新本页；README 中的简略目录树若受影响，也必须一起更新。

> Git 内部元数据（例如 `.git/`）不是 tracked 内容，因此不列出。

```text
agnir/                                                    # Agnir Agent Skill + Core / profiles / conformance 主仓库
├── .agnir/                                               # Agnir 项目自身的 canonical durable continuity
│   ├── state.md                                          # 当前 Project 状态与已验证事实
│   ├── next-actions.md                                   # 下次恢复时继续推进的 durable work
│   ├── decisions.md                                      # 已确认的协议、Skill、profile、conformance 与文档决策
│   └── evidence/                                         # checkpoint、conformance 与历史审计证据
│       ├── 2026-08-27-mainline-implementation.md
│       ├── 2026-08-27-repository-rename-checkpoint.md
│       ├── 2026-08-28-agent-skill-packaging.md           # 一句话用户提示词 + SKILL.md Agent procedure 分层与 conformance 证据
│       ├── 2026-08-28-agnir-0.1.0-release-readiness.md
│       ├── 2026-08-28-conformance-and-migration-audit-checkpoint.md
│       ├── 2026-08-28-durable-agent-activation.md
│       ├── 2026-08-28-external-memory-authorization.md
│       ├── 2026-08-28-filesystem-boundaries.md
│       ├── 2026-08-28-locator-chain-failures.md
│       ├── 2026-08-28-main-only-branch-cleanup-checkpoint.md
│       ├── 2026-08-28-multi-project-workspace-isolation.md
│       ├── 2026-08-28-negative-discovery-fixtures.md
│       ├── 2026-08-28-readme-agent-quick-start-checkpoint.md
│       ├── 2026-08-28-readme-diagram-localization-checkpoint.md
│       ├── 2026-08-28-readme-language-navigation-deferred-checkpoint.md
│       └── 2026-08-28-sqlite-non-repository-backend.md
│
├── .github/
│   └── workflows/
│       └── conformance.yml                               # CI：self-host + Skill / activation / Core/profile conformance
│
├── spec/                                                 # 当前 Agnir Core 协议层规范
│   ├── AGNIR_CORE.md                                     # Core 0.1 durable continuity / identity / checkpoint / version semantics
│   └── AGNIR_DISCOVERY.md                                # cold-start discovery / Locator Chain / failure vocabulary
│
├── profiles/                                             # Core 之外的具体 discovery / storage realization
│   └── REPOSITORY_FILESYSTEM.md                          # repository-filesystem/0.1；含 Agent activation/init + safe AGENTS merge contract
│
├── schemas/
│   └── agnir-manifest.schema.json                        # repository/filesystem AGNIR.yaml JSON Schema
│
├── conformance/                                          # executable pressure
│   ├── activation_reference.py                           # AGENTS.md → README canonical activation resolver
│   ├── agents_merge_reference.py                         # conformance-only：existing AGENTS.md non-destructive merge / conflict reference
│   ├── agnir-0.1.md                                      # Agnir 0.1 stable conformance baseline
│   ├── check_agnir_0_1.py                                # self-host + Skill packaging + stable release-readiness checker
│   ├── core_reference.py                                 # shared Core failure semantics reference
│   ├── external_memory_reference.py                      # external memory + authorization reference model
│   ├── locator_chain_reference.py                        # Locator Chain CYCLE / STALE / INCONSISTENT reference model
│   ├── repository_filesystem_reference.py                # repository-filesystem resolver reference
│   ├── sqlite_backend_reference.py                       # non-repository SQLite durable backend reference
│   ├── workspace_registry_reference.py                   # locator-only multi-project workspace registry reference
│   ├── test_agent_activation.py                          # prompt-free Project activation + negative fixtures
│   ├── test_agents_merge.py                              # existing AGENTS preserve / minimal create / idempotence / explicit conflict tests
│   ├── test_external_memory_authorization.py             # external authorization failure semantics
│   ├── test_locator_chain_failures.py                    # cycle / stale / inconsistency tests
│   ├── test_repository_filesystem_boundaries.py          # symlink / Git worktree filesystem boundaries
│   ├── test_repository_filesystem_failures.py            # discovery failure fixtures
│   ├── test_skill_package.py                             # root SKILL.md + one-line user prompt / Agent-procedure boundary tests
│   ├── test_sqlite_backend.py                            # SQLite cold-start / checkpoint / fresh-resume
│   └── test_workspace_isolation.py                       # multi-Project isolation tests
│
├── history/                                              # predecessor lineage；不属于 active Core / Skill procedure
│   ├── BRANCH_ARCHIVE.md                                 # 已删除 branch tip SHA 历史索引
│   ├── MIGRATION_PPMP_V2.md                              # 可选历史迁移指南；非 release gate
│   └── PREDECESSOR.md                                    # predecessor lineage 的 immutable commit 定位
│
├── SKILL.md                                              # canonical Agent Skill entrypoint；完整 install/use/checkpoint/repair + safe merge procedure
├── AGENTS.md                                             # 本仓库 Agent-facing locator：指向 README canonical Agnir Project Instructions
├── AGNIR.yaml                                            # 本仓库 repository-filesystem/0.1 discovery anchor
├── RELEASE.md                                            # 0.1.0 版本、Skill packaging、activation 与 publication gate
├── README.md                                             # 英文入口：一句话用户安装提示 + Skill/架构/activation/continuity
├── README.zh-CN.md                                       # 简体中文入口：一句话用户安装提示 + 同一 canonical 模型
├── REPOSITORY_TREE.md                                    # 本文件：当前 main 完整 tracked file 级结构
└── VERSION                                               # 仓库 SemVer；当前 0.1.0
```

## 如何使用这张树

第一次安装 Agnir 时，用户只需要 README 开头的一句话提示词；Agent 找到本仓库后读取根目录 `SKILL.md`，由 Skill 持有完整 procedure。一个已经初始化好的 Agent-operable Project 不应要求用户再次粘贴 Agnir procedure，而应由目标 Project 自己的 `AGENTS.md → README → AGNIR.yaml` 路线完成 activation / discovery。

本页不是第二套协议或 Skill procedure。**Agent procedure 以根目录 `SKILL.md` 为准；Core 语义以 `spec/` 为准；repository/filesystem 行为以 `profiles/REPOSITORY_FILESYSTEM.md` 为准；机器可读 manifest 约束以 `schemas/` 为准；`history/` 仅保存 lineage。**
