# 架构草案

## 处理链路

```text
source manifest
  -> fetch and cache
  -> parser
  -> canonical rule model
  -> group by business category
  -> curation guardrails
  -> exact deduplication
  -> semantic overlap analysis
  -> policy resolution
  -> target renderer (Quantumult X or Mihomo)
  -> audit report
```

## 统一规则模型

每条规则至少保留：

- 规则类型：HOST、HOST-SUFFIX、HOST-KEYWORD、IP-CIDR、USER-AGENT 等
- 规则值：规范化后的域名、地址或模式
- 策略：direct、reject、业务策略或代理策略
- 来源：source id、原始 URL 和抓取时间
- 处理状态：保留、合并、冲突、忽略
- 原始文本：用于审计和回溯

## 去重边界

### 可以自动处理

- 规则文本完全相同
- 规范化后完全相同
- 同一来源内相同规则重复出现
- 同一规则指向同一策略
- 目标渲染器会丢弃的选项不会参与规则身份比较
- HOST-KEYWORD、HOST-WILDCARD 和 IP-CIDR/IP6-CIDR 的可判断重叠

### 默认只报告

- 无法按业务边界裁决的域名或网段重叠
- 不同策略命中的同一域名
- 不同来源对同一域名给出不同策略
- USER-AGENT、IP-ASN、GEOIP 等无法仅凭域名判断的规则

## 输出原则

Quantumult X 与 Mihomo 各自使用原生来源清单，但共享规范化、去重和冲突裁决。目标渲染器负责语法转换和目标不支持选项过滤，审计会按过滤后的目标语义比较规则身份。Mihomo Classical 文件不包含策略列，策略由配置中的 `RULE-SET` 指定；核心不支持的规则类型必须使构建失败。

当前输出按业务分类拆分，而不是按 `HOST`、`IP-CIDR` 等语法类型拆分。同一类可以同时包含多个规则类型，但只承载一个明确的业务意图和策略映射。远程过滤器片段按业务优先级输出，专项服务不会因为规则语法不同而被拆散。

当前输出分为两层：`categories/candidates/<category>.list` 保留所有规范化后的候选规则；`categories/safe/<category>.list` 按保护性规则、业务边界、具体规则和来源优先级自动裁决，仍无法判断的冲突才从已裁决输出中排除，并写入冲突报告。审计优先使用目标客户端最终会看到的规则身份，避免源规则中被丢弃的选项制造隐性重复。

每个业务分类的处理顺序是：先合并多个上游来源，再应用明确的 Curation 排除项，然后做精确去重和语义冲突审计。完全相同的 selector 才选择一个策略；语义覆盖关系保留双方并记录先后约束，后续的策略裁决器不再通过删除宽泛规则来掩盖重叠。

## 优先规则预览

审计裁决后会单独生成 `priority-preview.json` 与 `priority-preview.md`，但不会改变 `categories/safe/` 或模板引用。预览只检查仍存在于最终安全规则中的跨分类重叠，并为域名、关键词、通配符和 CIDR 重叠构造可复现的匹配样例，再按当前目标渲染器的分类顺序执行 first-match 模拟。

预期策略与实际策略不同时，只有明确安全契约或更具体的 HOST、HOST-SUFFIX、CIDR 规则直接被比较规则挡住，才会进入候选列表。涉及关键词、宽泛规则或第三条更早规则的情况继续标记为待审阅。

预览层同时执行 Apple 服务统一契约：`apple.com`、`icloud.com`、`mzstatic.com` 体系以及 Apple 官方使用的 Private Cloud Compute 中继端点都归入“苹果服务”，即使上游将其登记为 AI、国际媒体、直连或通用代理。明确的 reject 与 direct-exception 高于 Apple 契约。该契约只生成预览候选，不改变正式安全规则。

所有预览均带有 `active: false`，在正式启用阶段完成前不得被 QX 或 Mihomo 模板引用。

## 安全边界

- 不接收或生成节点订阅。
- 不把用户本地 mitm、证书、私钥、Cookie、Token 写入仓库。
- Mihomo 示例模板只保留订阅地址占位符。控制器默认仅监听本机，密钥为空，不登记真实值。
- 公开输出前重新检查来源许可和第三方转载要求。
