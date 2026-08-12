# 架构草案

## 处理链路

```text
source manifest
  -> fetch and cache
  -> parser
  -> canonical rule model
  -> group by business category
  -> exact deduplication
  -> semantic overlap analysis
  -> policy resolution
  -> category filter renderer
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

### 默认只报告

- HOST 与 HOST-SUFFIX 的包含关系
- 不同策略命中的同一域名
- 不同来源对同一域名给出不同策略
- USER-AGENT、IP-ASN、GEOIP 等无法仅凭域名判断的规则

## 输出原则

Quantumult X 输出应优先使用其原生规则类型。Surge 来源不能未经解析就直接复制到原生 Quantumult X 输出中；每个输出文件都要标记生成器版本、来源快照和构建时间。

当前输出按业务分类拆分，而不是按 `HOST`、`IP-CIDR` 等语法类型拆分。同一类可以同时包含多个规则类型，但只承载一个明确的业务意图和策略映射。远程过滤器片段按业务优先级输出，专项服务不会因为规则语法不同而被拆散。

当前输出分为两层：`categories/candidates/<category>.list` 保留所有规范化后的候选规则；`categories/safe/<category>.list` 按 Blackmatrix、`direct`、具体规则的优先级自动裁决，仍无法判断的冲突才从已裁决输出中排除，并写入冲突报告。

每个业务分类的处理顺序是：先合并多个上游来源，再做精确去重和语义冲突审计；后续的策略裁决器只处理报告中的歧义，不再重复搬运上游规则。

## 安全边界

- 不接收或生成节点订阅。
- 不把用户本地 mitm、证书、私钥、Cookie、Token 写入仓库。
- 公开输出前重新检查来源许可和第三方转载要求。
