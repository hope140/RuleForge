# 来源清单

来源清单登记公开规则地址、格式、策略映射和维护说明，也允许极少量经过审阅的 `inline:` 精确例外；不登记节点订阅或其他私密地址。

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

`inline:` 地址只用于稳定、可审计的本地补充规则，不访问网络，也不应放入订阅或凭据。当前仅用于补充 Apple 的 `cma2.itunes.apple.com` 精确主机。

## 命名约定

- `id` 使用 `来源-业务分类[-补充说明]` 的小写 kebab-case，例如 `blackmatrix-openai`、`rulego-ai-supplement`。
- `category` 使用稳定的小写 kebab-case，表示业务归属，例如 `ai`、`apple`、`social`、`china-services`；同类来源必须使用同一个分类名。
- `policy` 只填写目标配置中已经存在的策略名，例如 `AI`、`苹果服务`、`direct`，不在来源名称里重复表达策略。

规则源更新后，先记录变更，再运行解析、去重和冲突审计；不要直接覆盖生成结果。

## 来源角色

- `Blackmatrix7/ios_rule_script`：优先使用其原生 Quantumult X 分类列表，作为主要来源。
- `ConnersHua/RuleGo`：补充 Surge 格式的跨客户端分类规则，经过本项目转换后使用。
- `ACL4SSR/ACL4SSR`：作为交叉来源，优先用于发现主来源遗漏的规则；不把它的客户端配置格式直接当作 Quantumult X 输出。

同一个 `category` 可以登记多个来源。构建时会先把同类来源合并，再统一规范化、精确去重、语义冲突审计，最后分别输出候选版和已按优先级裁决的规则版。

## 双目标来源

- `quantumultx.yaml` 使用 Blackmatrix 原生 Quantumult X 列表。
- `mihomo.yaml` 是独立清单，沿用相同业务分类与策略边界，但使用 Blackmatrix 原生 Clash classical YAML；兼容的 RuleGo Surge 与 ACL4SSR Clash 文本继续作为补充。
- 两份清单的来源 ID 保持对应，便于比较覆盖差异；生成结果不互相作为输入。
- Mihomo 构建严格拒绝 `USER-AGENT`、`URL-REGEX` 等核心不支持的规则类型，避免静默降级。

## 冲突优先级

冲突裁决按以下顺序执行。语义重叠先按已登记的业务边界和保护性规则处理，避免渲染后的客户端顺序把宽泛关键词或网段误认为最终策略；完全相同的规则仍按来源和策略优先级裁决。

1. 直连 `direct` 优先于阻断 `reject`。
2. 业务边界优先于宽泛关键词和网段重叠：Google Voice > Google、AI > Google、YouTube > Google、Apple/Google > 国内直连；国内影音与国际影音按服务边界区分。
3. 更具体的单独规则优先于更宽泛的整体规则，例如 `HOST` 优先于覆盖它的 `HOST-SUFFIX`，非关键词域名规则优先于覆盖它的 `HOST-KEYWORD`，更长的子网优先于父网段。
4. 广告和隐私阻断规则保护已识别的语义重叠；开发者服务优先于泛 GitHub 分类，`naver.com` 优先国际媒体，社交与 Netflix 的专用网段优先各自业务分类。
5. 完全相同且仍无法按业务边界判断的规则，再由 Blackmatrix 来源优先于其他来源。
6. 不符合以上条件的冲突不猜测，保留在审计报告并从已裁决输出中排除。
