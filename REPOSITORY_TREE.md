# Repository Tree / 目录树

本页是 `iorLab/agnir` 当前仓库的**仓库结构与职责地图**。README 中的仓库树用于快速导航；这里展开 active compatibility contracts、stable release contracts、profiles、conformance、Project continuity 与历史参考。

维护规则：这里明确列出的文件 / 目录被新增、删除、移动或职责发生实质变化时，必须在同一个 change set 中同步更新本页；README 的简略仓库树若受影响，也必须一起更新。`.agnir/evidence/` 按**目录职责**记录，不逐个枚举 checkpoint Evidence 文件。

```text
agnir/                                                    # Agnir Skill + protocol/profile/conformance repository
├── .agnir/                                               # 本 Project canonical durable continuity
│   ├── state.md                                          # selected lineage 当前 durable truth
│   ├── next-actions.md                                   # 下次恢复时继续推进的 ordered work
│   ├── decisions.md                                      # active durable protocol/release/operation decisions
│   └── evidence/                                         # recovery / audit / migration / release evidence collection
│
├── .github/
│   └── workflows/
│       └── conformance.yml                               # main/release CI + gated prerelease/stable publication jobs
│
├── brand/                                                # Agnir 品牌识别与 production asset surface
│   ├── README.md                                         # 品牌目录职责、production authority 与 integration status
│   ├── APPROVED-VISUAL-REFERENCE.md                      # Principal 批准的 10:42 AM 视觉基准与 source hash
│   ├── PRODUCTION-STATUS.md                              # 当前 master / derivative / QA / integration gates
│   ├── brand-handoff.md                                  # 下游使用规则与禁止替换项
│   ├── brand-process-log.md                              # 品牌设计与生产过程记录
│   ├── INTEGRATION-NOTE.md                               # 品牌分支与最新 main 的 reconcile 说明
│   ├── reference/                                       # byte-exact approved references / extraction manifests
│   ├── masters/                                         # 批准的 Agnir vector production masters
│   │   └── candidates/                                  # 历史 review candidates；不作为 production truth
│   ├── exports/                                         # SVG treatments and byte-exact PNG delivery derivatives
│   ├── qa/                                              # 对称 13 项 final QA 范围与 evidence metadata
│   └── tools/                                           # deterministic derivative / raster / review tooling
│
├── spec/                                                 # Core/discovery/migration contracts
│   ├── AGNIR_CORE.md                                     # Core 0.1 compatibility contract
│   ├── AGNIR_CORE_0_2.md                                 # stable Core 0.2 normative contract
│   ├── AGNIR_DISCOVERY.md                                # cold-start discovery / Locator Chain / failure vocabulary
│   ├── CORE_0_1_TO_0_2_MIGRATION.md                      # explicit Core/profile migration semantics
│   └── CORE_0_2_DESIGN.md                                # lineage / selector / integration design rationale
│
├── profiles/                                             # concrete discovery/storage/integration realization
│   ├── REPOSITORY_FILESYSTEM.md                          # repository-filesystem/0.1 compatibility profile
│   ├── REPOSITORY_FILESYSTEM_0_2.md                      # stable repository-filesystem/0.2 normative profile
│   └── VCS_BRANCH_CONTINUITY.md                          # VCS branch/ref/worktree mapping + integration extension
│
├── schemas/
│   ├── agnir-manifest.schema.json                        # repository-filesystem/0.1 AGNIR.yaml schema
│   └── agnir-manifest-0.2.schema.json                    # repository-filesystem/0.2 schema with continuity.lineage
│
├── conformance/                                          # executable compatibility, migration and release pressure
│   ├── agnir-0.1.md                                      # Core/profile 0.1 compatibility baseline
│   ├── agnir-0.2-plan.md                                 # Core 0.2 evidence/conformance plan and historical gate map
│   ├── check_agnir_0_1.py                                # Core/profile 0.1 compatibility helpers
│   ├── check_agnir_0_2.py                                # generic/stable Core/profile 0.2 self-host/release gate
│   ├── check_agnir_0_2_rc.py                             # immutable-RC-era audit/reference self-host gate
│   ├── activation_reference.py                           # AGENTS.md → README activation resolver
│   ├── agents_merge_reference.py                         # non-destructive AGENTS merge/conflict reference
│   ├── checkpoint_reference.py                           # no-op/coherent/stale-base checkpoint model
│   ├── upgrade_reference.py                              # compatible upgrade / stable target / provenance model
│   ├── core_reference.py                                 # shared Core 0.1 failure semantics
│   ├── core_0_2_reference.py                             # generic logical-lineage selection/integration model
│   ├── core_0_2_vcs_mapping_reference.py                 # VCS selector/receipt → Core 0.2 semantic mapping
│   ├── core_0_2_migration_reference.py                   # storage-neutral 0.1 → 0.2 migration model
│   ├── repository_filesystem_reference.py                # repository-filesystem/0.1 resolver
│   ├── repository_filesystem_0_2_reference.py            # repository-filesystem/0.2 selected-lineage resolver
│   ├── repository_filesystem_0_2_migration_reference.py  # concrete staged/atomic AGNIR.yaml migration
│   ├── sqlite_backend_reference.py                       # stable non-repository SQLite backend reference
│   ├── sqlite_lineage_reference.py                       # non-VCS Core 0.2 transactional lineage backend
│   ├── vcs_branch_continuity_reference.py                # VCS staged integration/reconciliation reference
│   ├── vcs_lineage_binding_reference.py                  # selector↔logical-lineage fork/rebind/mismatch reference
│   ├── external_memory_reference.py                      # external memory authorization model
│   ├── locator_chain_reference.py                        # Locator Chain cycle/stale/inconsistent model
│   ├── workspace_registry_reference.py                   # locator-only multi-Project isolation model
│   ├── test_agent_activation.py                          # prompt-free activation pressure
│   ├── test_agents_merge.py                              # AGENTS preservation/idempotence/conflict pressure
│   ├── test_checkpoint_semantics.py                      # checkpoint no-op/coherent/conflict pressure
│   ├── test_upgrade_semantics.py                         # compatible upgrade + migration classification
│   ├── test_core_0_2_parallel_continuity.py              # non-VCS lineage selection/isolation/integration
│   ├── test_core_0_2_vcs_mapping.py                      # selector != identity + receipt/integration mapping
│   ├── test_core_0_2_migration.py                        # explicit/idempotent semantic migration
│   ├── test_repository_filesystem_0_2.py                 # 0.2 discovery/schema compatibility
│   ├── test_repository_filesystem_0_2_migration.py       # concrete migration/stale/no-op/fresh-discovery
│   ├── test_rc_release_gates.py                          # immutable RC + exact-v0.1.1 install/migration evidence
│   ├── test_stable_release_gates.py                      # stable 0.2 package/status/binding compatibility gates
│   ├── test_vcs_lineage_binding.py                       # fork/rebind/external mismatch binding pressure
│   ├── test_vcs_branch_continuity.py                     # real worktree + staged target publication pressure
│   ├── test_repository_filesystem_failures.py            # 0.1 discovery failures
│   ├── test_repository_filesystem_boundaries.py          # filesystem/symlink/Git-worktree boundaries
│   ├── test_sqlite_backend.py                            # stable SQLite cold-start/checkpoint/fresh-resume
│   ├── test_external_memory_authorization.py             # external authorization failures
│   ├── test_locator_chain_failures.py                    # cycle/stale/inconsistent pressure
│   ├── test_workspace_isolation.py                       # multi-Project isolation
│   └── test_skill_package.py                             # Skill / short UX / upgrade / handoff / commit intent
│
├── history/                                              # predecessor lineage; not an active compatibility contract
│   ├── BRANCH_ARCHIVE.md                                 # deleted/retired branch tip SHA index
│   ├── MIGRATION_PPMP_V2.md                              # historical predecessor migration material
│   └── PREDECESSOR.md                                    # predecessor immutable history locator
│
├── SKILL.md                                              # canonical Agent-facing install/migrate/upgrade/use/checkpoint/integrate/repair procedure
├── AGENTS.md                                             # Agent locator to README canonical Agnir Project Instructions
├── AGNIR.yaml                                            # current selected Project/lineage discovery record
├── RELEASE.md                                            # current repository stable release publication contract/evidence
├── RELEASE_MILESTONES.md                                 # v0.2.0 / v1.0.0 milestone meaning
├── VERSIONING.md                                         # active repository SemVer vs Core/profile compatibility policy
├── V1_RELEASE_CRITERIA.md                                # v1.0.0 stability/compatibility gates
├── README.md                                             # English user/Agent entry point + architecture/continuity
├── README.zh-CN.md                                       # 简体中文 parallel entry point
├── REPOSITORY_TREE.md                                    # 本文件
└── VERSION                                               # repository SemVer of the selected source tree
```

## 当前版本职责

- **Repository stable line:** `0.2.0` publishes Core `0.2` + `repository-filesystem/0.2` when the immutable stable tag/Release is successfully created. Before publication, the preceding actually published stable release remains the stable-resolution target.
- **Accepted prerelease evidence:** immutable `v0.2.0-rc.1` remains audit/release evidence and must not be moved or silently treated as stable.
- **Core 0.2 normative contract:** `spec/AGNIR_CORE_0_2.md`.
- **Profile 0.2 normative contract:** `profiles/REPOSITORY_FILESYSTEM_0_2.md`.
- **Core/profile 0.1 compatibility:** `spec/AGNIR_CORE.md`, `profiles/REPOSITORY_FILESYSTEM.md`, 0.1 schema/reference/tests remain supported compatibility and migration surfaces.
- **Migration contract:** `spec/CORE_0_1_TO_0_2_MIGRATION.md` plus semantic/concrete executable conformance.
- **Stable release gate:** `conformance/test_stable_release_gates.py` checks stable package/status/binding semantics; `conformance/test_rc_release_gates.py` retains exact published-v0.1.1 shape and fresh install/migration evidence.
- **VCS mapping:** `profiles/VCS_BRANCH_CONTINUITY.md` and VCS reference/tests. A VCS selector is not automatically logical lineage identity; a commit SHA is a receipt, not identity.

Historical `.agnir/evidence/` and Git history may mention earlier `_DRAFT` or RC filenames/status because those references describe the development/release-candidate checkpoints accurately.

## 如何使用这张树

用户安装/升级时仍只需要 README 开头的简短提示；Agent 找到分发包后由根目录 `SKILL.md` 承担完整 procedure。已经初始化的 Project 正常使用时通过自己的 `AGENTS.md → README → AGNIR.yaml` route activation；只有明确的 install/upgrade/migration/repair intent 才需要 distribution procedure。

本页不是第二套协议。**Core `0.1` 以 `spec/AGNIR_CORE.md` 为 compatibility contract；Core `0.2` 以 `spec/AGNIR_CORE_0_2.md` 为 stable normative contract；repository-filesystem `0.1` 以 `profiles/REPOSITORY_FILESYSTEM.md` 为准；repository-filesystem `0.2` 以 `profiles/REPOSITORY_FILESYSTEM_0_2.md` 为 stable normative profile；机器可读 manifest 约束在 `schemas/`；Agent procedure 以 `SKILL.md` 为准；`history/` 只保存 predecessor lineage。**
