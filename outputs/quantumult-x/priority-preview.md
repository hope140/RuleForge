# RuleForge 优先规则预览

> 仅供审阅，当前模板和正式路由不会引用这些候选规则。

## 摘要

- 目标：`quantumult-x`
- 存活的跨分类重叠：465
- 实际策略不一致：3
- Apple 统一策略缺口：3
- 可自动生成的候选规则：3
- 仍需审阅：0
- 无法构造验证样例：0

## 候选优先规则

| 规则 | 分类 | 策略 | 可信度 | 证据数 | 验证样例 |
| --- | --- | --- | --- | ---: | --- |
| `host,apple-relay.fastly-edge.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.fastly-edge.com` |
| `host,apple-relay.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.cloudflare.com` |
| `host,cp4.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `cp4.cloudflare.com` |

## 未自动处理的差异

| 验证样例 | 预期策略 | 当前策略 | 关系 | 原因 |
| --- | --- | --- | --- | --- |
| 无 |  |  |  |  |
