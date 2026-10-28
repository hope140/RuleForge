# MagicRule 来源迁移

MagicRule 接替原 Blackmatrix 远程来源，保留 RuleForge 的 26 个业务分类和客户端订阅地址。迁移不新增策略组，也不改变订阅、DNS 或节点设置。

## 分类映射

原来两端各登记 85 个 Blackmatrix 来源。76 个同名分类改为 MagicRule 动态来源，Npmjs 改为 NPM，共 77 个远程分类。Claude、Civitai、AppleID、AppleMail、GoogleDrive、BiliBiliIntl、ParamountPlus、Peacock 没有独立的同名分类，其既有 selector 保留为本地 `inline:` 补充。Claude 与 Apple 等规则可与较大的新分类去重；补充本身不再依赖旧仓库。

QX 保留 31 条迁移补充，Mihomo 保留 28 条；差异是 QX 的 Google Drive USER-AGENT 规则。审阅后两端另各保留 15 条 Apple、Netflix、Hulu/JOOX 和第三方 Telegram 客户端别名，以及 TVB 的专用主机。原有 Apple cma2 和 QX oaistatsig 本地规则继续保留。来源 ID 改用 `magicrule-` 与 `local-`，历史 Blackmatrix 测试样例和旧摘要字段继续兼容。

本地补充在原规则基础上保留原策略，属于固定种子，不会从 MagicRule 自动更新。新站将来提供独立分类时应审阅覆盖，再替换这些条目。原规则贡献归属保留在项目致谢中。

## 动态下载

来源清单通过 `resolver: magicrule` 显式启用索引解析。`url` 包含客户端索引和分类名 fragment，刷新时依次访问索引、分类 manifest、当前文本产物。索引可将文件分发到不同的官方 pages.dev 分片。

只接受 HTTPS 元数据及文本产物，检查客户端、分类名称、唯一性、二进制/空文件标记，以及上游提供的文件 SHA256。部分 Mihomo 共享产物保留较早的四行注释头；仅当上游明确声明 `standard_header_normalized`、四行标准头和 `semantic_sha256` 时，允许按去掉这四行后的正文校验，否则原始字节哈希不符即失败。正文发生变化仍会失败。分类缺失、重名、格式变化、哈希不符或下载失败均令构建失败，不自动切回旧来源，也不覆盖上一版正式输出。离线构建使用缓存中的实际规则文件。

构建摘要同时记录逻辑来源 URL、`resolved_url` 和规则文件 SHA256。`source_preferred_conflict_count` 记录同分类来源优先级；旧 `blackmatrix_preferred_conflict_count` 继续保留，供已有报告读取器兼容。

## 业务边界

新站分类并非原列表的逐字迁移。初次同名替换试验在两端各产生 94 个未决冲突，因此继续沿用原有安全、业务归属和规则具体程度的门禁。

- 新站 Copilot 聚合了多家 AI 厂商。该来源只接入明确的 Copilot 域名、服务主机与进程；其他 AI 服务由既有独立来源负责，避免把国内服务和共享云设施整体划入 AI 策略。被排除的行保留在 Curation 报告中。
- GitHub 专项策略优先于 Microsoft 汇总来源；AI 专项优先于 Microsoft，Microsoft 既有服务优先于通用国内直连。
- Copilot 代理主机进入 AI；GitHub 的遥测与 workspace 主机继续进入 GitHub；Microsoft 附件主机继续进入全球加速。
- Tenor、LINE TV、BiliBili 海外内容主机按原有业务策略处理。国内与港台媒体重叠遵循现有港台媒体优先边界。
- npm 包管理域名在去重前统一归入开发者服务，避免 Microsoft 汇总列表与同策略去重掩盖其业务归属。TVB 的既有专用 Azure 主机作为本地补充保留。
- Google FCM 保留迁移前实际策略：Mihomo 九个 mtalk 推送主机直连；QX 的八个 alt 主机直连，主 mtalk 主机进入谷歌服务。
- 上游在多个分类重复添加的署名标记主机不属于业务流量，统一排除并记录原因。

## 分流变化审阅

审阅使用迁移前 Git 基线与当前分类文件，并按客户端实际 first-match 顺序比较域名样例。对两端共约 4.9 万个域名/后缀根及构造子域名进行静态检查；样例数量不代表独立网站或真实连接数量，GeoSite/GEOIP 与真实 DNS 不在该模拟范围内。

- 修复 Google 上游错误收录的两字母地区后缀，例如 `.hk`、`.tw` 和 `.co`，防止把其他厂商站点归入谷歌服务。保留 Google 自有品牌顶级域 `.google` 和具体的 `google.com.hk`。
- 排除 AI 来源中的共享 Statsig 根域、Google Cloud Storage 通用端点，以及 Datadog、Sentry、Sift、Codex、Colab 等含义过宽的关键词；保留明确产品域名、进程和专用子域名。`storage.googleapis.com` 是[Google Cloud 的通用存储接口](https://docs.cloud.google.com/storage/docs/request-endpoints)，不能单凭该主机识别某个 AI 产品。
- 将 WeTV、JOOX 等海外媒体域名从腾讯汇总直连分类归回国际媒体，避免公司归属覆盖地区策略。国内腾讯、微信和其他国内业务继续直连。
- 根据 [AWS 官方公开地址池](https://ip-ranges.amazonaws.com/ip-ranges.json) 核对 Netflix IP 列表，排除其中覆盖共享 EC2/CloudFront 地址的非单机网段，避免无关云流量进入 Netflix 策略。保留明确的单 IP 端点和 Netflix 自有网段，已知 Netflix 域名仍走 Netflix。经审阅的 129 个共享地址池、数据日期和源哈希记录在 `src/ruleforge/shared_cloud.py`，构建不新增网络依赖；该清单需随后续审阅维护。
- 保留合理的业务细化，包括 Microsoft 下载/CDN 直连、jsDelivr 全球加速、Telegram 专项 IP 策略，以及 Google AI 服务进入 AI、Apple 专用中继进入苹果服务。

静态解析、完整构建、路由回归与 Mihomo 内核检查用于验证文件和引用关系；真实客户端、节点和业务访问仍需单独验收。

## 本地验证记录

2026-10-28 完成本地迁移验证。

- 两端来源清单 lint 通过，每端 77 个 MagicRule 远程来源，均不再登记旧仓库下载地址。
- 两端完整构建通过，解析问题、抓取错误和未决冲突均为 0；各生成 26 个业务分类。QX 最终保留 14,105 条分类规则，Mihomo 保留 14,152 条；两端均排除 Netflix 来源中 1,132 条覆盖共享 AWS 地址池的非单机 IP 规则。
- 完整回归 99 项通过，包含原有路由验收样例，以及动态索引、哈希变化、失败缓存保护、Copilot 边界、地域后缀、共享云、海外媒体和迁移服务覆盖测试。
- Mihomo v1.19.30 校验器通过官方发布 SHA256 验证，完整模板和片段组装配置均通过内核配置检查；检查使用本地测试 provider。
- 上述检查证明静态规则与配置有效；真实客户端、节点与地区解锁访问尚未验收。
