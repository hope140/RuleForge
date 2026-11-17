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

## 非冲突变更审阅

2026-11-17 来源快照相对已发布规则还有以下变化；不把“无冲突”当作业务正确性的充分证明。

- RuleGo AI 新增 `scontent-*.xx.fbcdn.net`。无法证明该通配范围只用于 AI；历史已审核 social 已含 `HOST-SUFFIX,fbcdn.net` 和 `HOST-KEYWORD,fbcdn`，因此保守地只排除此条 AI 通配规则，维持已有社交路由。不阻断该域名，不强制直连，也不删除具体 AI 主机或 `meta.ai`。风险：如果 Meta AI 某些图片也用这些共享主机，会继续走社交策略而非独立 AI 策略，这是避免将全部共享图片流量划到 AI 的明确取舍。
- Anthropic 来源新增两个精确日志端点：`http-intake.logs.us5.datadoghq.com`、`o1158394.ingest.us.sentry.io`，保留来源给出的精确主机。没有扩大到 `datadoghq.com` / `sentry.io` 根域。这是上游归属声明，并非我们独立确认全部租户用途。
- `production-copilot-host-westus.webpubsub.azure.com` 从 Microsoft 的全球加速归入 GitHub，由既有 GitHub/Microsoft 业务优先级裁决。没有扩大到 `azure.com`。
- 国际媒体新增 `h264.io`，来源给出的流媒体补充项。
- Google 来源删除 13 个单标签后缀规则，随上游移除。现有服务域名及回归仍保留；单标签后缀不再有专门谷歌策略，可能落入其余规则或默认策略。
- Mihomo 的部分 IP-ASN 新增 `no-resolve` 选项；审计模型忽略其作为 selector 身份差异，但原生格式保留该选项。这不是更换 ASN 或业务类别。

三份被冻结分类的新输出与已审核版本逐条一致：QX Apple 2098 / Telegram 65 / 中国直连 256 条；Mihomo 分别 2102 / 71 / 293 条。

## 固定快照字节校验

全部来自上述固定 Git 提交，以下是包含注释头的 SHA256：

|目标|分类|SHA256|
|---|---|---|
|quantumult-x|apple|`f841490b91553d20f2f19bd6472c143842a8b89b5dc68fe4ab3260c6ebd5be55`|
|quantumult-x|telegram|`4143d7997696f227808968583a1ea1b17136f9ab925c03e8f3e6feb3c35d648b`|
|quantumult-x|china-direct|`7faf846d449ee12d393a0e03224360d856ea9372b392ac724f06dfe56e67f18e`|
|mihomo|apple|`befaaa040fc818c433c6ac8b616342dda628a42fe7c47288f29e7fc812c21edd`|
|mihomo|telegram|`1fee155f6e1ed64692ddd6b6658ca0a4bab5c22210fcce79d88055973c0c34c7`|
|mihomo|china-direct|`370c54f6d97e57e01cafcbc79b49c525dde4d4c063bb534658ff9fe65ce0c121`|
