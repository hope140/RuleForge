# RuleForge 优先规则预览

> 仅供审阅，当前模板和正式路由不会引用这些候选规则。

## 摘要

- 目标：`quantumult-x`
- 存活的跨分类重叠：762
- 实际策略不一致：6
- Apple 统一策略缺口：2
- 可自动生成的候选规则：4
- 仍需审阅：2
- 无法构造验证样例：0

## 候选优先规则

| 规则 | 分类 | 策略 | 可信度 | 证据数 | 验证样例 |
| --- | --- | --- | --- | ---: | --- |
| `host,apple-relay.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.cloudflare.com` |
| `host,cp4.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `cp4.cloudflare.com` |
| `host,googletraveladservices-cn.com,谷歌服务` | `google` | `谷歌服务` | medium | 1 | `googletraveladservices-cn.com` |
| `host,googletraveladservices.com,谷歌服务` | `google` | `谷歌服务` | medium | 1 | `googletraveladservices.com` |

## 未自动处理的差异

| 验证样例 | 预期策略 | 当前策略 | 关系 | 原因 |
| --- | --- | --- | --- | --- |
| `googletraveladservices-cn.com` | `reject` | `direct` | `host-keyword-overlap` | third-rule-interference / security-contract / high |
| `googletraveladservices.com` | `reject` | `direct` | `host-keyword-overlap` | third-rule-interference / security-contract / high |
