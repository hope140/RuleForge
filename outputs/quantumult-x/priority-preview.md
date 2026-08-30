# RuleForge 优先规则预览

> 仅供审阅，当前模板和正式路由不会引用这些候选规则。

## 摘要

- 目标：`quantumult-x`
- 存活的跨分类重叠：475
- 实际策略不一致：33
- Apple 统一策略缺口：6
- 可自动生成的候选规则：18
- 仍需审阅：9
- 无法构造验证样例：0

## 候选优先规则

| 规则 | 分类 | 策略 | 可信度 | 证据数 | 验证样例 |
| --- | --- | --- | --- | ---: | --- |
| `host,apple-relay.fastly-edge.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.fastly-edge.com` |
| `host,apple-relay.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.cloudflare.com` |
| `host,apple-relay.apple.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apple-relay.apple.com` |
| `host,cp4.cloudflare.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `cp4.cloudflare.com` |
| `host,gateway.icloud.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `gateway.icloud.com` |
| `host,apps.mzstatic.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `apps.mzstatic.com` |
| `host-suffix,smoot.apple.com,苹果服务` | `apple` | `苹果服务` | high | 1 | `smoot.apple.com` |
| `host,tvbtracking.azurewebsites.net,国际媒体` | `global-media` | `国际媒体` | medium | 1 | `tvbtracking.azurewebsites.net` |
| `host-suffix,disney-portal.my.onetrust.com,国际媒体` | `global-media` | `国际媒体` | medium | 1 | `disney-portal.my.onetrust.com` |
| `host-suffix,hbo.com.edgesuite.net,国际媒体` | `global-media` | `国际媒体` | medium | 1 | `hbo.com.edgesuite.net` |
| `host-suffix,abcnews.edgesuite.net,国际媒体` | `global-media` | `国际媒体` | medium | 1 | `abcnews.edgesuite.net` |
| `host-suffix,cdn.optimizely.com,国际媒体` | `global-media` | `国际媒体` | medium | 1 | `cdn.optimizely.com` |
| `host-suffix,qingmail.com,direct` | `china-services` | `direct` | medium | 1 | `qingmail.com` |
| `host-suffix,qingmail.cn,direct` | `china-services` | `direct` | medium | 1 | `qingmail.cn` |
| `host,merchant-rating.alibaba.com,全球加速` | `proxy` | `全球加速` | medium | 1 | `merchant-rating.alibaba.com` |
| `host,login.alibaba.com,全球加速` | `proxy` | `全球加速` | medium | 1 | `login.alibaba.com` |
| `host,new.c.mi.com,全球加速` | `proxy` | `全球加速` | medium | 1 | `new.c.mi.com` |
| `host,c.mi.com,全球加速` | `proxy` | `全球加速` | medium | 1 | `c.mi.com` |

## 未自动处理的差异

| 验证样例 | 预期策略 | 当前策略 | 关系 | 原因 |
| --- | --- | --- | --- | --- |
| `apple-relay.apple.com` | `AI` | `AI` | `host-inside-host-suffix` | apple-policy-missing / apple-service-contract / high |
| `gateway.icloud.com` | `AI` | `AI` | `host-keyword-overlap` | apple-policy-missing / apple-service-contract / high |
| `gateway.icloud.com` | `AI` | `AI` | `nested-host-suffix` | apple-policy-missing / apple-service-contract / high |
| `apps.mzstatic.com` | `AI` | `AI` | `nested-host-suffix` | apple-policy-missing / apple-service-contract / high |
| `smoot.apple.com` | `AI` | `AI` | `nested-host-suffix` | apple-policy-missing / apple-service-contract / high |
| `gateway.icloud.com` | `苹果服务` | `AI` | `host-keyword-overlap` | third-rule-interference / apple-service-contract / high |
| `probe-spotify--spotify-com.example` | `国际媒体` | `Spotify` | `host-keyword-overlap` | not-auto-eligible / specificity / medium |
| `probe-spotify-spotify.com.example` | `国际媒体` | `Spotify` | `host-keyword-overlap` | not-auto-eligible / specificity / medium |
| `probe-blogspot-.blogspot.example` | `全球加速` | `谷歌服务` | `host-keyword-overlap` | not-auto-eligible / specificity / medium |
