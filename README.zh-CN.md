# Agnir

[English](README.md) | **简体中文**

Agnir 是一个 **由 Project 自己拥有的持久连续性协议（durable continuity protocol）**。

它让 Project 在 Agent、对话、执行环境或存储实现发生变化后仍然可以安全恢复和继续。Durable continuity 属于 Project，而不属于某个 execution surface。

## 30 秒快速开始

### 新 Project

只需要把这一句话交给 Agent：

```text
为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir
```

这才是**给用户的安装提示词**。Agent 找到本仓库后，应读取根目录 [`SKILL.md`](SKILL.md)，由 Skill 自己接管完整的 Agent-side 安装 / 初始化流程。用户不需要把 Agnir 内部的任务清单复制到提示词里。

Skill 会负责安装或校验 Project 的 Agnir continuity，包括让未来 Agent 能自动发现 Agnir 的持久激活入口。

### 已经初始化 Agnir 的 Project

**不需要再给 Agent 任何 Agnir bootstrap 提示词。** 正确初始化后的 Agent-operable Project 会自己持久保存激活路线：

```text
Project 根目录
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ durable memory
```

把 Project 正常交给 Agent，然后直接开始真正的任务即可。如果某个 execution surface 不会自动读取 Project instruction files，应对该 execution surface 做一次性配置，而不是让用户每次会话都重复 Agnir 的内部 procedure。

## Agnir Project Instructions

本仓库自己也使用 Agnir 保存 durable Project continuity。

开始任何 Project 工作前，把本仓库根目录视为已授权的 Project Entry Point。先读取顶层 `AGNIR.yaml`，然后加载 Current State 和 Next Actions；需要时再加载 Decisions 和 Evidence。除非有更新的 Principal 指令或直接观察到的当前 Project 事实覆盖，否则 Agnir 中持久保存的 Project truth 优先于聊天记录或 Agent 私有记忆。

当进行 checkpoint、保存进度或结束工作时，把重要的状态、后续动作、决策和必要 Evidence reconcile 到 `AGNIR.yaml` 声明的位置。Checkpoint 应当是一个一致的 authoritative transition：durable truth 没有实质变化时做 no-op，不能把不同 checkpoint generation 拼成表面一致的状态，发布后还要重新验证 fresh discovery。

在 repository / VCS 上下文中，把已授权的 `commit`、`提交`、`提交代码` 或同义请求视为 checkpoint boundary：**先 reconcile Agnir，再 commit**，并优先把 Project 改动与 Agnir 改动放进同一个 revision。`commit and push`、`提交推送` 或同义请求表示 checkpoint + commit + push，并在声明了 authoritative remote/ref 时验证推送结果。只是观察到一个外部产生的 commit，只触发 checkpoint evaluation，不代表必须无条件再写一次 Agnir。

根目录 `AGENTS.md` 故意只做 locator，指向本 section；本 section 才是 canonical activation instruction。

## Skill 与用户提示词的边界

Agnir 明确把两层指令分开：

- **给用户的安装提示词**：只有一句，表达“我要安装 Agnir”并给出 Agnir 源仓库。
- **给 Agent 的 Skill procedure**：根目录 `SKILL.md`，完整负责 install / initialize / resume / checkpoint / repair。

Skill 是发行和操作入口，不改变 Agnir Core 语义。初始化完成后，目标 Project 已经通过自己的 `AGENTS.md → README → AGNIR.yaml` 路线做到 self-describing；以后正常工作不需要再打开 Skill 来提醒 Agent “这个 Project 使用 Agnir”。

对于 `repository-filesystem/0.1`，Skill 通常会建立或校验：

```text
Project/
├── AGENTS.md                 # 指向 README 中 canonical Agnir 指令
├── AGNIR.yaml                # repository/filesystem discovery anchor
├── README.md                 # 包含 ## Agnir Project Instructions
└── .agnir/
    ├── state.md
    ├── next-actions.md
    ├── decisions.md
    └── evidence/
```

规范性的初始化 / 激活要求由 [`profiles/REPOSITORY_FILESYSTEM.md`](profiles/REPOSITORY_FILESYSTEM.md) 定义；根目录 `SKILL.md` 是把这些要求交给 Agent 执行的 procedure。

## 架构图（Architecture Diagram）

```mermaid
flowchart TB
    U["用户<br/>只给一句安装意图"] --> K["Agnir Agent Skill<br/>SKILL.md 保存完整安装 procedure"]
    K -. "初始化一次" .-> P["目标 Project 根目录"]

    P --> G["持久 Agent 激活入口<br/>AGENTS.md → README Agnir Project Instructions"]
    G --> D["发现适配层（Discovery Profile / Adapter）"]
    D --> R["发现记录（Discovery Record）<br/>repository profile 中为 AGNIR.yaml"]

    subgraph C[Agnir Core 0.1]
        V["版本与 Project identity 校验"]
        M["Continuity semantics"]
        V --> M
    end

    R --> V
    M --> S["Current State"]
    M --> N["Next Actions"]
    M --> J["Decisions"]
    M --> E["Evidence / Checkpoints"]

    D -. "当前 profile" .-> Y["repository-filesystem/0.1"]
    Y --> A["AGNIR.yaml"]
    A --> F["Durable locators<br/>本仓库为 .agnir/"]
```

`SKILL.md` 是 Agent-facing packaging layer；`AGENTS.md → README` 是面向 Agent 的 repository activation convention。两者都不是 Agnir Core 的依赖。已经知道适用 profile 的 Executor / adapter 可以直接从 Project Entry Point / Discovery Record 开始。

Agnir Core **不要求** Git、GitHub、repository、ChatGPT、AI Agent、Skill system 或某种具体 storage backend。

## 连续性流程（Continuity Flow）

安装完成后，正常 Project continuity 不再依赖最初那句用户安装提示词，也不依赖初始化对话：

```mermaid
flowchart TD
    C["新的 Agent / 新执行上下文"] --> P["获得已授权的 Project 根目录"]
    P --> A["读取 AGENTS.md"]
    A --> I["跟随 README 的 Agnir Project Instructions"]
    I --> R["读取 AGNIR.yaml / 解析 Discovery Record"]
    R --> V{"版本与 Project identity 是否兼容？"}
    V -- "否" --> F["显式返回 discovery failure"]
    V -- "是" --> L["加载 Current State + Next Actions"]
    L --> Q["按需要加载 Decisions / Evidence"]
    Q --> W["Executor 执行真正的 Project 工作<br/>不属于 Agnir Core"]
    W --> U["形成明确的 continuity 更新"]
    U --> K["Reconcile + 原子发布一致 checkpoint"]
    K --> S["持久连续性存储"]
    S --> N["未来新的 Agent / 环境"]
    N --> P
```

Agnir 不执行流程中间的 Project 工作。它负责让 continuity 持久、可发现、绑定到正确 Project，并让未来 Executor 可以安全恢复。Not-found、ambiguity、unsupported version、Project mismatch、authorization failure、cycle、stale locator、material inconsistency 等 failure 都必须显式暴露，不能靠猜测静默修复。

## 当前版本线

`main` 是 Agnir `0.1.0` 稳定发布线。兼容标识分别为 Core `0.1` 和 `repository-filesystem/0.1`；仓库 SemVer 独立记录在 `VERSION`。

PPMP / PPM / Sandminni 等前身材料只属于 `history/` 与 immutable Git history，不属于当前兼容契约。

## 发布状态

当前仓库正在完成 Agnir `0.1.0` 的正式发布前收口。`RELEASE.md` 定义版本模型、发布范围、发布门槛和已知限制。创建 `v0.1.0` Git tag / GitHub Release 仍是单独的 publication 动作。

三个版本层必须区分：

- Core compatibility：`0.1`；
- repository/filesystem profile：`repository-filesystem/0.1`；
- repository release：`0.1.0`。

## 仓库结构

```text
agnir/
├── spec/                              # 当前协议层定义
│   ├── AGNIR_CORE.md                  # Core 0.1，含 transactional checkpoint 语义
│   └── AGNIR_DISCOVERY.md             # discovery / Locator Chain / failures
├── profiles/
│   └── REPOSITORY_FILESYSTEM.md       # repository-filesystem/0.1 activation/init + VCS event integration
├── schemas/
│   └── agnir-manifest.schema.json     # AGNIR.yaml schema
├── conformance/
│   ├── check_agnir_0_1.py             # self-host + release-readiness
│   ├── activation_reference.py        # AGENTS → README activation resolver
│   ├── checkpoint_reference.py        # atomic/no-op/conflict checkpoint reference model
│   ├── test_skill_package.py          # Skill / 用户提示词边界 + commit intent 测试
│   └── test_*.py                      # 其他 executable conformance
├── .agnir/                            # 本 Project 的 canonical durable continuity
├── history/                           # 仅历史 lineage
├── .github/workflows/                 # CI
├── SKILL.md                           # canonical Agent-facing Agnir Skill procedure
├── AGENTS.md                          # 指向 README canonical Project instructions
├── AGNIR.yaml                         # repository/filesystem discovery anchor
├── RELEASE.md
├── README.md
├── README.zh-CN.md
└── VERSION                            # 0.1.0
```

需要查看完整 tracked file 级目录树，请看 **[REPOSITORY_TREE.md](REPOSITORY_TREE.md)**。

## Core memory semantics

Agnir 要求能够持久恢复 Current State、Next Actions、Decisions 和 Evidence / Checkpoints。Fresh compatible Executor 必须能够恢复继续 Project 所需的 truth，而不依赖上一段私有对话上下文。

## 与 Svif 的关系

Svif 是独立的 **Project orchestration product**，位于 `iorLab/svif`。当前 Svif 通过 Agnir adapter 使用 Agnir 作为首个 Continuity Provider；Agnir 不依赖 Svif，也可以独立使用。

## 文档同步规则

`README.md` 与 `README.zh-CN.md` 是并行入口。Layer model、Skill / install 边界、activation path、discovery path、durable-memory semantics、Project boundary 或 continuity flow 变化时，必须在同一个 change set 同步更新两种语言中受影响的说明 / 图。

README 的 Quick Start 必须始终面向用户并保持极简：**安装提示词只有一句；完整 Agent procedure 属于根目录 `SKILL.md`。** `REPOSITORY_TREE.md` 是完整结构地图；它说明 evidence 目录职责，不再重复登记每一个 checkpoint evidence 文件名。

## Conformance

运行：

```bash
python conformance/check_agnir_0_1.py
python -m unittest discover -s conformance -p 'test_*.py' -v
```

`0.1.0` suite 覆盖 Agent Skill packaging、免重复提示的 Project activation、repository/filesystem discovery 与 failures、checkpoint atomic/no-op/conflict 语义、SQLite 非 repository continuity、external-memory authorization、multi-project isolation、Locator Chain failures、symlink boundaries 和真实 Git worktree cold start。

真实 mount-boundary 仍明确未验证；普通目录不能冒充 mount evidence。
