# 2026-11-17 上游分类临时隔离

## 原因

诊断运行 https://github.com/hope140/RuleForge/actions/runs/44028400537 同时刷新 QX 与 Mihomo，均发现 6583 项未决冲突。主要是 Apple/Telegram 3679 项、中国直连/Telegram 2896 项。QX Telegram 从已审核快照的 63 条增至 3741 条，AppleProxy 从 65 条增至 3970 条，Apple 从 2087 条增至 5993 条，Direct 从 263 条增至 3383 条。

例如 `analytics-fe.digital-cloud.medallia.eu`、`bot.cdn.adeo.cloud` 同时被归入 Apple 与 Telegram。这些文件通过上游索引和 SHA 校验，问题属于分类内容而非传输损坏。部分带哈希名字的下载 URL 与旧版完全相同，字节内容却已经不同，所以固定旧上游 URL 不能恢复旧内容。

## 临时处理

- 暂停 `magicrule-apple-proxy`；其已审核覆盖包含在 Apple 快照中。
- Apple、Telegram、中国直连用本仓库提交 `893b4f3cb68f415c9025ce82fade7011fd5333a3` 下的三份已裁决分类文件作为明确、不可漂移的来源。
- 每个客户端使用自己的同格式快照，不跨客户端转换。快照来自 2026-11-09 构建，各自当时均为 0 未决冲突；现有历史提交包含来源与审计证据。
- 其余 73 个 MagicRule 分类及 RuleGo、ACL4SSR、本地补充继续正常更新。Apple 的其他细分类来源仍继续更新，快照不是宣称整个 Apple 服务永远冻结。
- 保留 `--fail-on-conflict`、原子发布及全套回归。失败时不替换正式输出。
- 快照是应急隔离，不是最新上游，也不应长期无声冻结。其缺点是被隔离来源的新端点不会自动引入。

## 独立的 Facebook API 冲突

RuleGo AI 新增 `graph.facebook.com`，与 WhatsApp/social 的现有归属冲突。Meta 文档 https://developers.facebook.com/docs/graph-api/overview/ 明确该域名为通用 Graph API，不是 AI 专用端点；历史已发布 social 文件也已包含该精确主机。因此只对 `ai/social + graph.facebook.com` 作 social 优先裁决，不扩展为整个 Facebook 根域，也不影响 `meta.ai` 等 AI 端点。明确拒绝规则仍优先。

## 恢复条件

上游修复后，在独立分支恢复四个原始来源，对比快照、当前新增/删除以及分类重叠；确认无大批无关域名、双端严格构建及实际路由回归通过，才移除隔离。不能仅因为未决数量变成零就自动恢复，也不能用批量优先级掩盖上游内容异常。

诊断工作流只读、无提交/发布步骤。`--diagnostics-dir` 的报告写入独立目录，保留来源哈希、具体冲突和分组统计；公共来源缓存以 7 天 artifact 保存，便于复现。运行本地诊断也必须与正式输出目录分离。
