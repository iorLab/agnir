# Agnir 中文社交平台母版

Status: **Principal-approved mother copy**  
Audience: 中文开发者 / AI coding power users  
Purpose: Wave 1 external design-user recruitment  
Derived platform copy SHOULD preserve the positioning and factual claims here unless newer authoritative Project state supersedes them.

## Mother copy

我越来越觉得，AI coding 现在缺的，不只是更长的上下文。

而是：

**项目自己的记忆。**

一个很常见的场景：

你和 AI 做了几个小时项目。

功能做到一半，测试还剩几个，之前也已经做过一些关键决定。

然后你结束会话。

第二天打开一个完全新的会话，只说一句：

**「继续。」**

如果项目本身没有保存这些信息，新的 AI 并不知道该继续什么。

于是你又开始解释：

做到哪里了、下一步是什么、为什么之前这么设计、哪些东西已经验证过……

问题是，这些信息本来就不应该只存在于某一个聊天窗口里。

**它们应该属于项目。**

所以我做了 **Agnir**。

Agnir 是一个 AI Native 的项目记忆系统，更准确地说，是一套 **Project Continuity / 项目连续性**机制。

它让项目自己保存和携带那些真正应该持续存在的东西：

- 当前状态
- 下一步
- 已做出的关键决定
- 已验证的证据

Agent、会话和执行环境可以变化。

**项目本身继续存在。**

我现在最喜欢用一个非常简单的方式解释 Agnir：

打开两个全新的 AI 会话。

它们都只收到一句：

**「继续。」**

但大有不同。

没有 Agnir 的一边，只知道这是一个新会话，不知道之前发生过什么。

有 Agnir 的一边，会从项目本身发现当前状态、下一步和关键决定，然后继续工作。

这也是现在 Agnir 官网首页的动态演示。

Agnir 已经发布到 **v1.0.1 stable**。

它是开源的，使用 Apache-2.0 License。

而且它不是把聊天记录搬到另一个数据库里。

Agnir 的核心想法恰恰相反：

**项目连续性不应该属于某一个 AI 工具。**

它应该属于 Project。

如果你想直接试一下，不需要先研究 Agnir 的协议，也不需要先学习一套新的工作方式。

把下面这句话发给能访问你项目的 Agent：

**为这个项目安装并初始化 Agnir：https://github.com/iorLab/agnir**

安装完成以后，继续像原来一样工作。

等到一个合适的节点结束当前会话，再打开一个完全新的会话。

只说一句：

**「继续。」**

然后看看会发生什么。

现在，我准备开始找第一批真正的外部用户。

我最想找的是那些经常用 ChatGPT、Codex、Claude Code、Cursor 或其他 AI 工具做真实项目，并且遇到过这种问题的人：

**每开一个新会话，都要重新解释项目。**

我现在最关心的也不是 Star 数量。

而是一个非常具体的问题：

**你把 Agnir 装进一个真实项目以后，关掉当前会话，再打开一个完全新的会话，只说一句「继续」——它能不能真的接上？**

如果能，这就是我要验证的东西。

如果不能，我也非常想知道它在哪里断掉。

Agnir：

https://iorlab.github.io/agnir/

GitHub：

https://github.com/iorLab/agnir

## Derivation guardrails

- Lead with the fresh-session pain and outcome before protocol vocabulary.
- Keep **Project Continuity / 项目连续性** as the product category; “AI Native 的项目记忆” is user-facing discovery language, not a Core redefinition.
- Preserve the core test: install → normal work → fresh session → only `继续。` → observe whether the Project resumes.
- Do not claim external adoption, retention, cross-Executor success, or performance numbers until accepted evidence exists.
- Prefer recruiting real design users over asking for stars.
- Canonical public links remain the Agnir website and `iorLab/agnir` repository unless authoritative Project state changes them.
