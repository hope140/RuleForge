# RuleForge 优先规则预览

> 仅供审阅，当前模板和正式路由不会引用这些候选规则。

## 摘要

- 目标：`mihomo`
- 存活的跨分类重叠：326
- 实际策略不一致：24
- Apple 统一策略缺口：24
- 可自动生成的候选规则：22
- 仍需审阅：0
- 无法构造验证样例：0

## 候选优先规则

| 规则 | 分类 | 策略 | 可信度 | 证据数 | 验证样例 |
| --- | --- | --- | --- | ---: | --- |
| `DOMAIN,apple-relay.fastly-edge.com` | `apple` | `苹果服务` | high | 1 | `apple-relay.fastly-edge.com` |
| `DOMAIN,apple-relay.cloudflare.com` | `apple` | `苹果服务` | high | 1 | `apple-relay.cloudflare.com` |
| `DOMAIN,radio.itunes.apple.com` | `apple` | `苹果服务` | high | 1 | `radio.itunes.apple.com` |
| `DOMAIN,apple-relay.apple.com` | `apple` | `苹果服务` | high | 1 | `apple-relay.apple.com` |
| `DOMAIN,cp4.cloudflare.com` | `apple` | `苹果服务` | high | 1 | `cp4.cloudflare.com` |
| `DOMAIN,facetime.apple.com` | `apple` | `苹果服务` | high | 1 | `facetime.apple.com` |
| `DOMAIN,guzzoni.apple.com` | `apple` | `苹果服务` | high | 1 | `guzzoni.apple.com` |
| `DOMAIN,books.apple.com` | `apple` | `苹果服务` | high | 1 | `books.apple.com` |
| `DOMAIN,time.apple.com` | `apple` | `苹果服务` | high | 1 | `time.apple.com` |
| `DOMAIN-SUFFIX,weather-analytics-events.apple.com` | `apple` | `苹果服务` | high | 1 | `weather-analytics-events.apple.com` |
| `DOMAIN-SUFFIX,weather-adge.apple.com` | `apple` | `苹果服务` | high | 1 | `weather-adge.apple.com` |
| `DOMAIN-SUFFIX,weather-data.apple.com` | `apple` | `苹果服务` | high | 1 | `weather-data.apple.com` |
| `DOMAIN-SUFFIX,weather-edge.apple.com` | `apple` | `苹果服务` | high | 1 | `weather-edge.apple.com` |
| `DOMAIN-SUFFIX,weather-map.apple.com` | `apple` | `苹果服务` | high | 1 | `weather-map.apple.com` |
| `DOMAIN-SUFFIX,apps.mzstatic.com` | `apple` | `苹果服务` | high | 1 | `apps.mzstatic.com` |
| `DOMAIN-SUFFIX,smoot.apple.com` | `apple` | `苹果服务` | high | 1 | `smoot.apple.com` |
| `DOMAIN-SUFFIX,humb.apple.com` | `apple` | `苹果服务` | high | 1 | `humb.apple.com` |
| `DOMAIN-SUFFIX,push.apple.com` | `apple` | `苹果服务` | high | 1 | `push.apple.com` |
| `DOMAIN-SUFFIX,ess.apple.com` | `apple` | `苹果服务` | high | 1 | `ess.apple.com` |
| `DOMAIN-SUFFIX,ssl.apple.com` | `apple` | `苹果服务` | high | 1 | `ssl.apple.com` |
| `DOMAIN-SUFFIX,ls.apple.com` | `apple` | `苹果服务` | high | 1 | `ls.apple.com` |
| `DOMAIN-SUFFIX,icloud.com` | `apple` | `苹果服务` | high | 1 | `icloud.com` |

## 未自动处理的差异

| 验证样例 | 预期策略 | 当前策略 | 关系 | 原因 |
| --- | --- | --- | --- | --- |
| 无 |  |  |  |  |
