# 来源清单

来源清单登记公开规则地址、格式、策略映射和维护说明，也允许极少量经过审阅的 `inline:` 精确例外；不登记节点订阅或其他私密地址。

清单只接受 `schema_version: 1`，`target` 必须是 `quantumult-x` 或 `mihomo`。根字段、来源字段、字段类型以及 `kind` / `format` / `parser` 组合都会严格校验；`enabled` 必须使用不带引号的 YAML 布尔值，未知字段会使 lint 和构建失败。

## 字段约定

- `id`：稳定的内部标识
- `kind`：资源类型，公开来源使用 `filter`，本地精确例外使用 `inline`
- `format`：上游格式，例如 `quantumult-x`、`clash` 或 `surge`
- `category`：业务分类
- `policy`：目标客户端通过规则分类使用的策略
- `url`：公开 HTTP(S) 资源地址或 `inline:` 本地规则数据
- `parser`：解析方式
- `enabled`：是否纳入构建
- `notes`：特殊处理或保留原因

`inline:` 地址只用于稳定、可审计的本地补充规则，不访问网络，也不应放入订阅或凭据。当前用于补充 Apple 的 `cma2.itunes.apple.com` 精确主机，以及 QX 没有 GeoSite 兜底时的 `oaistatsig.com` 根域。

## 命名约定

- `id` 使用 `来源-业务分类[-补充说明]` 的小写 kebab-case，例如 `blackmatrix-openai`、`rulego-ai-supplement`。
- `category` 使用稳定的小写 kebab-case，表示业务归属，例如 `ai`、`apple`、`social`、`china-services`；同类来源必须使用同一个分类名。
- `policy` 只填写目标配置中已经存在的策略名，例如 `AI`、`苹果服务`、`direct`，不在来源名称里重复表达策略。

规则源更新后，先记录变更，再运行解析、Curation、去重和冲突审计；不要直接覆盖生成结果。

## 来源角色

- `Blackmatrix7/ios_rule_script`：优先使用其原生 Quantumult X 分类列表，作为主要来源。
- `ConnersHua/RuleGo`：补充 Surge 格式的跨客户端分类规则，经过本项目转换后使用。
- `ACL4SSR/ACL4SSR`：作为交叉来源，优先用于发现主来源遗漏的规则；不把它的客户端配置格式直接当作 Quantumult X 输出。

同一个 `category` 可以登记多个来源。构建时会先把同类来源合并，再统一规范化；共享云厂商 ASN 和通用 SaaS 根域等明确排除项会进入 Curation 报告，不参加后续冲突裁决，最后分别输出候选版和已按优先级裁决的规则版。

## 双目标来源

- `quantumultx.yaml` 使用 Blackmatrix 原生 Quantumult X 列表。
- `mihomo.yaml` 是独立清单，沿用相同业务分类与策略边界，但使用 Blackmatrix 原生 Clash classical YAML；兼容的 RuleGo Surge 与 ACL4SSR Clash 文本继续作为补充。
- 两份清单的来源 ID 保持对应，便于比较覆盖差异；生成结果不互相作为输入。
- Mihomo 构建严格拒绝 `USER-AGENT`、`URL-REGEX` 等核心不支持的规则类型，避免静默降级。

## 冲突优先级

冲突裁决按以下顺序执行。完全相同的 selector 是 exclusive conflict，只保留一个策略；域名后缀、关键词、通配符和 CIDR 的覆盖关系是 ordered overlap，两条规则都保留并记录 first-match 约束，避免删除宽泛规则造成未重叠地址失去覆盖。

1. 安全策略优先：明确的 `direct-exception` 可以覆盖 `reject`，普通 `direct` 或 `proxy` 不覆盖 `reject`。
2. 显式 value/category override 优先于一般规则，例如 GitHub Copilot、Grok 和 Apple 服务端点的明确业务归属。
3. 规则 specificity 优先于业务分类：`HOST` > `HOST-SUFFIX`，更长的 `HOST-SUFFIX` > 更短的后缀，非关键词规则 > `HOST-KEYWORD`，更具体的 CIDR > 更宽的 CIDR。
4. specificity 无法判断时，才使用业务 category preference，例如 AI > Google、YouTube > Google，以及已登记的国内/国际媒体边界。
5. 来源优先级只用于同一 category 内部的冲突；其中 Blackmatrix 仅作为同类来源的 tie-breaker。
6. 仍无法按上述规则区分的 exclusive conflict 保留为 unresolved 并从已裁决输出中排除；稳定的 category fallback 只用于 semantic overlap 的 first-match 排序。ordered overlap 不因无法自动决定类别胜负而删除整条规则。
