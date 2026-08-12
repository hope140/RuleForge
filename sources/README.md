# 来源清单

来源清单只登记公开规则地址、格式、策略映射和维护说明，不登记节点订阅或其他私密地址。

## 字段约定

- `id`：稳定的内部标识
- `kind`：资源类型，目前使用 `filter`
- `format`：上游格式，例如 `quantumult-x` 或 `surge`
- `category`：业务分类
- `policy`：输出到 Quantumult X 时使用的策略
- `url`：公开资源地址
- `parser`：解析方式
- `enabled`：是否纳入构建
- `notes`：特殊处理或保留原因

## 命名约定

- `id` 使用 `来源-业务分类[-补充说明]` 的小写 kebab-case，例如 `blackmatrix-openai`、`rulego-ai-supplement`。
- `category` 使用稳定的小写 kebab-case，表示业务归属，例如 `ai`、`apple`、`china-media`；同类来源必须使用同一个分类名。
- `policy` 只填写目标 Quantumult X 中已经存在的策略名，例如 `AI`、`苹果服务`、`direct`，不在来源名称里重复表达策略。

规则源更新后，先记录变更，再运行解析、去重和冲突审计；不要直接覆盖生成结果。

## 来源角色

- `Blackmatrix7/ios_rule_script`：优先使用其原生 Quantumult X 分类列表，作为主要来源。
- `ConnersHua/RuleGo`：补充 Surge 格式的跨客户端分类规则，经过本项目转换后使用。
- `ACL4SSR/ACL4SSR`：作为交叉来源，优先用于发现主来源遗漏的规则；不把它的客户端配置格式直接当作 Quantumult X 输出。

同一个 `category` 可以登记多个来源。构建时会先把同类来源合并，再统一规范化、精确去重、语义冲突审计，最后分别输出候选版和已按优先级裁决的规则版。

## 冲突优先级

冲突裁决按以下顺序执行：

1. Blackmatrix 来源优先于其他来源。
2. 直连 `direct` 优先于阻断 `reject`。
3. 更具体的单独规则优先于更宽泛的整体规则，例如 `HOST` 优先于覆盖它的 `HOST-SUFFIX`，更长的子域后缀优先于父域后缀。
4. 业务边界按分类优先级处理：Google Voice > Google、AI > Google、YouTube > Google、Apple/Google > 国内直连。
5. 明确 AI 域名优先 AI；共享 CDN、云存储和基础设施域名优先全球代理；`naver.com` 优先国际媒体。
6. 不符合以上条件的冲突不猜测，保留在审计报告并从已裁决输出中排除。
