# Repository Tree / 目录树

本页是 `iorLab/agnir` 当前 `main` 的**仓库结构与职责地图**。README 中的仓库树只用于快速导航；这里进一步展开 active protocol、profile、conformance、Project continuity 和历史参考的主要 tracked 结构。

维护规则：只要这里明确列出的文件 / 目录被新增、删除、移动，或者职责发生实质变化，就必须在同一个 change set 中同步更新本页；README 中的简略目录树若受影响，也必须一起更新。`.agnir/evidence/` 是刻意按**目录职责**记录的 append-style evidence collection，不逐个重复登记 checkpoint evidence 文件名；新增 evidence 本身不再要求为了更新本树而制造额外仓库 mutation。

> Git 内部元数据（例如 `.git/`）不是 tracked 内容，因此不列出。

```text
agnir/                                                    # Agnir Agent Skill + Core / profiles / conformance 主仓库
├── .agnir/                                               # Agnir 项目自身的 canonical durable continuity
│   ├── state.md                                          # 当前 Project 状态与已验证事实
│   ├── next-actions.md                                   # 下次恢复时继续推进的 durable work
│   ├── decisions.md                                      # 已确认的协议、Skill、profile、conformance 与文档决策
│   └── evidence/                                         # checkpoint / conformance / audit evidence；按目录职责维护，不逐文件登记
│
├── .github/
│   └── workflows/
│       └── conformance.yml                               # CI：self-host + Skill / activation / Core/profile conformance
│
├── spec/                                                 # 当前 Agnir Core 协议层规范
│   ├── AGNIR_CORE.md                                     # Core 0.1 durable continuity / identity / transactional checkpoint / version semantics
│   └── AGNIR_DISCOVERY.md                                # cold-start discovery / Locator Chain / failure vocabulary
│
├── profiles/                                             # Core 之外的具体 discovery / storage realization
│   └── REPOSITORY_FILESYSTEM.md                          # repository-filesystem/0.1；activation/init + upgrade + VCS integration
│
├── schemas/
│   └── agnir-manifest.schema.json                        # repository/filesystem AGNIR.yaml JSON Schema
│
├── conformance/                                          # executable pressure
│   ├── activation_reference.py                           # AGENTS.md → README canonical activation resolver
│   ├── agents_merge_reference.py                         # conformance-only：existing AGENTS.md non-destructive merge / conflict reference
│   ├── agnir-0.1.md                                      # Agnir 0.1 stable conformance baseline
│   ├── check_agnir_0_1.py                                # self-host + Skill packaging + stable release-readiness checker
│   ├── checkpoint_reference.py                           # substrate-neutral checkpoint no-op / atomic generation / stale-base conflict model
│   ├── upgrade_reference.py                              # compatible upgrade / stable-target / provenance / migration classification model
│   ├── core_reference.py                                 # shared Core failure semantics reference
│   ├── external_memory_reference.py                      # external memory + authorization reference model
│   ├── locator_chain_reference.py                        # Locator Chain CYCLE / STALE / INCONSISTENT reference model
│   ├── repository_filesystem_reference.py                # repository-filesystem resolver reference
│   ├── sqlite_backend_reference.py                       # non-repository SQLite durable backend reference
│   ├── workspace_registry_reference.py                   # locator-only multi-project workspace registry reference
│   ├── test_agent_activation.py                          # prompt-free Project activation + negative fixtures
│   ├── test_agents_merge.py                              # existing AGENTS preserve / minimal create / idempotence / explicit conflict tests
│   ├── test_checkpoint_semantics.py                      # no-op / coherent publication / AGNIR_CHECKPOINT_CONFLICT tests
│   ├── test_upgrade_semantics.py                         # compatible/no-op upgrade, stable-target, provenance preservation, migration tests
│   ├── test_external_memory_authorization.py             # external authorization failure semantics
│   ├── test_locator_chain_failures.py                    # cycle / stale / inconsistency tests
│   ├── test_repository_filesystem_boundaries.py          # symlink / Git worktree filesystem boundaries
│   ├── test_repository_filesystem_failures.py            # discovery failure fixtures
│   ├── test_skill_package.py                             # root SKILL.md + user prompt + upgrade + commit/push intent tests
│   ├── test_sqlite_backend.py                            # SQLite cold-start / checkpoint / fresh-resume
│   └── test_workspace_isolation.py                       # multi-Project isolation tests
│
├── history/                                              # predecessor lineage；不属于 active Core / Skill procedure
│   ├── BRANCH_ARCHIVE.md                                 # 已删除 branch tip SHA 历史索引
│   ├── MIGRATION_PPMP_V2.md                              # 可选历史迁移指南；非 release gate
│   └── PREDECESSOR.md                                    # predecessor lineage 的 immutable commit 定位
│
├── SKILL.md                                              # canonical Agent Skill；install/upgrade/use/checkpoint/commit/push/repair procedure
├── AGENTS.md                                             # 本仓库 Agent-facing locator：指向 README canonical Agnir Project Instructions
├── AGNIR.yaml                                            # 本仓库 repository-filesystem/0.1 discovery anchor
├── RELEASE.md                                            # 0.1.0 版本、upgrade/Skill/activation 与 publication gate
├── README.md                                             # 英文入口：一句话安装提示 + Skill/架构/activation/continuity
├── README.zh-CN.md                                       # 简体中文入口：同一 canonical 模型
├── REPOSITORY_TREE.md                                    # 本文件：仓库结构与职责地图
└── VERSION                                               # 仓库 SemVer；当前 0.1.0
```

## 如何使用这张树

第一次安装 Agnir 时，用户只需要 README 开头的一句话提示词；Agent 找到本仓库后读取根目录 `SKILL.md`，由 Skill 持有完整 procedure。已经初始化的 Project 正常使用时仍通过自己的 `AGENTS.md → README → AGNIR.yaml` 路线 activation；只有用户明确要求升级 Agnir 时才重新调用 distribution/Skill 的 upgrade procedure。

本页不是第二套协议或 Skill procedure。**Agent procedure 以根目录 `SKILL.md` 为准；Core 语义以 `spec/` 为准；repository/filesystem 行为以 `profiles/REPOSITORY_FILESYSTEM.md` 为准；机器可读 manifest 约束以 `schemas/` 为准；`history/` 仅保存 lineage。**
