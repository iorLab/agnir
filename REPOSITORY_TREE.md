# Repository Tree / 目录树

本页是 `iorLab/agnir` 当前仓库的结构与职责地图。README 提供快速导航；这里列出 active compatibility contracts、profiles、conformance、Project continuity、release surfaces、brand/adoption surfaces 与历史参考。

维护规则：新增、删除、移动或实质改变这里列出的文件职责时，应在同一个 change set 中同步更新本页。`.agnir/evidence/` 按目录职责记录，不逐个枚举全部 Evidence 文件。

```text
agnir/
├── .agnir/                                               # 本 Project canonical durable continuity
│   ├── state.md                                          # selected lineage 当前 durable truth
│   ├── next-actions.md                                   # ordered remaining work
│   ├── decisions.md                                      # active durable decisions
│   └── evidence/                                         # recovery / audit / migration / release / adoption Evidence
│
├── brand/                                                # approved Agnir identity system and production assets
│   ├── APPROVED-VISUAL-REFERENCE.md                      # locked visual authority and precedence
│   ├── INTEGRATION-NOTE.md                               # integration boundary / current target
│   ├── PRODUCTION-STATUS.md                              # production + QA + integration status
│   ├── README.md                                         # brand surface entry
│   ├── brand-handoff.md                                  # downstream production/use handoff
│   ├── brand-process-log.md                              # brand derivation/review provenance
│   ├── masters/                                          # approved vector masters + superseded candidates
│   ├── exports/                                          # SVG exports + byte-exact PNG delivery derivatives
│   ├── reference/                                        # byte-exact Principal-approved reference boards
│   ├── qa/                                               # symmetric final QA contract
│   └── tools/                                            # deterministic build/render/review tooling
│
├── adoption/                                             # positioning, launch, demos, design-user and case-study strategy
│   └── README.md                                         # Principal-approved post-v1 launch/adoption strategy
│
├── .github/
│   └── workflows/
│       └── conformance.yml                               # main/release CI + exact gated publication jobs
│
├── spec/
│   ├── AGNIR_CORE.md                                     # Core 0.1 compatibility contract
│   ├── AGNIR_CORE_0_2.md                                 # stable Core 0.2 normative contract
│   ├── AGNIR_CORE_1_0.md                                 # stable Core 1.0 normative contract
│   ├── AGNIR_DISCOVERY.md                                # discovery / Locator Chain / failures
│   ├── CORE_0_1_TO_0_2_MIGRATION.md                      # explicit 0.1 -> 0.2 migration
│   ├── CORE_0_2_TO_1_0_PROMOTION.md                      # stable explicit 0.2 -> 1.0 promotion
│   └── CORE_0_2_DESIGN.md                                # lineage/selector/integration rationale
│
├── profiles/
│   ├── REPOSITORY_FILESYSTEM.md                          # repository-filesystem/0.1
│   ├── REPOSITORY_FILESYSTEM_0_2.md                      # stable repository-filesystem/0.2
│   ├── REPOSITORY_FILESYSTEM_1_0.md                      # stable repository-filesystem/1.0
│   └── VCS_BRANCH_CONTINUITY.md                          # legacy Core/profile 0.1 VCS extension material
│
├── schemas/
│   ├── agnir-manifest.schema.json                        # repository-filesystem/0.1 schema
│   ├── agnir-manifest-0.2.schema.json                    # repository-filesystem/0.2 schema
│   └── agnir-manifest-1.0.schema.json                    # repository-filesystem/1.0 schema
│
├── conformance/
│   ├── activation_reference.py                           # AGENTS.md -> README activation resolver
│   ├── agents_merge_reference.py                         # non-destructive AGENTS merge
│   ├── checkpoint_reference.py                           # no-op/coherent/stale-base checkpoint model
│   ├── upgrade_reference.py                              # compatible upgrade / stable-target model
│   ├── core_reference.py                                 # Core 0.1 shared failure semantics
│   ├── core_0_2_reference.py                             # Core 0.2 logical-lineage model
│   ├── core_1_0_reference.py                             # Core 1.0 stability reference surface
│   ├── repository_filesystem_reference.py                # repository-filesystem/0.1 resolver
│   ├── repository_filesystem_0_2_reference.py            # repository-filesystem/0.2 resolver
│   ├── repository_filesystem_1_0_reference.py            # strict repository-filesystem/1.0 resolver
│   ├── repository_filesystem_1_0_promotion_reference.py  # staged 0.2 -> 1.0 promotion reference
│   ├── external_memory_reference.py                      # external memory authorization model
│   ├── locator_chain_reference.py                        # Locator Chain cycle/stale model
│   ├── sqlite_backend_reference.py                       # non-repository backend reference
│   ├── workspace_registry_reference.py                   # multi-Project isolation model
│   ├── check_agnir_0_1.py                                # Core/profile 0.1 self-host helper
│   ├── check_agnir_0_2.py                                # Core/profile 0.2 self-host gate
│   ├── check_agnir_1_0.py                                # Core/profile 1.0 RC/stable self-host gate
│   ├── test_agent_activation.py                          # prompt-free activation pressure
│   ├── test_agents_merge.py                              # AGENTS preservation/idempotence/conflict pressure
│   ├── test_checkpoint_semantics.py                      # checkpoint semantics
│   ├── test_upgrade_semantics.py                         # upgrade/migration classification
│   ├── test_skill_package.py                             # Skill + UX + release-status pressure
│   ├── test_1_0_package_surface.py                       # 1.0 package/RC/stable publication surface pressure
│   ├── test_core_1_0_stability.py                        # Core 1.0 stability semantics
│   ├── test_repository_filesystem_1_0.py                 # exact 1.0 discovery/failure pressure
│   ├── test_repository_filesystem_1_0_promotion.py       # explicit 0.2 -> 1.0 promotion pressure
│   ├── test_stable_release_gates.py                      # version-scoped stable 0.2/1.0 package gates
│   └── test_*.py                                         # remaining backend/lineage/migration/integration pressure
│
├── history/
│   ├── PREDECESSOR.md                                    # predecessor immutable history locator
│   ├── MIGRATION_PPMP_V2.md                              # historical predecessor migration material
│   └── BRANCH_ARCHIVE.md                                 # retired branch tip index
│
├── SKILL.md                                               # canonical Agent-facing procedure
├── AGENTS.md                                              # locator to README Agnir Project Instructions
├── AGNIR.yaml                                             # selected Project/lineage discovery record
├── README.md                                              # English user/Agent entry point
├── README.zh-CN.md                                        # 简体中文 parallel entry point
├── REPOSITORY_TREE.md                                     # 本文件
├── RELEASE.md                                             # stable source package + publication invariant
├── RELEASE_MILESTONES.md                                  # v0.1/v0.2/v1 milestone meaning
├── VERSIONING.md                                          # repository/Core/profile version policy
├── V1_RELEASE_CRITERIA.md                                 # v1 stability gates
└── VERSION                                                # selected source-tree repository SemVer
```

## 当前版本职责

- **当前 stable distribution source package:** repository `1.0.0`, Core `1.0`, `repository-filesystem/1.0`. `latest stable` resolution remains determined by the actually published non-prerelease Release, not by this moving branch.
- **Accepted RC evidence:** immutable `v1.0.0-rc.1` at `092945289f1a0a9803e4fe0583104aa380ceaadc`; it remains prerelease evidence and must not be moved during stable publication.
- **Historical compatibility:** Core/profile `0.1` and `0.2` normative/schema/reference/tests remain supported. A `1.0.x` distribution dispatches according to the Project compatibility identifiers actually declared.
- **Stable 0.2 -> 1.0 promotion contract:** `spec/CORE_0_2_TO_1_0_PROMOTION.md` plus `conformance/repository_filesystem_1_0_promotion_reference.py` and `conformance/test_repository_filesystem_1_0_promotion.py`.
- **Release gates:** `conformance/test_stable_release_gates.py` is version-scoped for stable `0.2.0` and `1.0.0`. `conformance/test_1_0_package_surface.py` verifies both immutable RC publication and the dormant main-only stable `v1.0.0` publication path.
- **Stable publication boundary:** `release/v1.0.0` is staging/reconciliation input. Exact stable publication is authorized only from verified authoritative `main` with commit message `release: publish v1.0.0 stable`.
- **VCS mapping:** Core/profile `0.2` and `1.0` use their normative Core/profile VCS semantics. A VCS selector is not logical lineage identity; a commit SHA is a receipt, not identity.
- **Brand boundary:** `brand/` is the canonical approved visual identity/production-asset authority; brand assets do not define Core semantics.
- **Adoption boundary:** `adoption/` owns post-v1 positioning, launch, demo, design-user, community and case-study strategy; adoption materials may consume brand assets but do not redefine them or Core semantics.

Historical `.agnir/evidence/` and Git history may contain earlier draft/RC wording because those records describe earlier checkpoints accurately.

## 如何使用这张树

用户安装/升级时只需要 README 开头的简短提示。Agent 获取 distribution 后由根目录 `SKILL.md` 承担完整 procedure；初始化后的 Project 通过自己的 `AGENTS.md -> README -> AGNIR.yaml` route activation。

本页不是第二套协议。Core `0.1` / `0.2` / `1.0` 分别以对应 Core contract 为准；repository-filesystem `0.1` / `0.2` / `1.0` 分别以对应 profile 为准；0.2 -> 1.0 Project promotion 以 `spec/CORE_0_2_TO_1_0_PROMOTION.md` 为准；机器可读 manifest 约束在 `schemas/`；Agent procedure 以 `SKILL.md` 为准；`brand/` 负责视觉身份；`adoption/` 负责采用策略；`history/` 只保存 predecessor/history material。
