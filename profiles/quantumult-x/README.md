# Quantumult X 配置输出

这里存放 Quantumult X 的策略命名、规则顺序、完整配置模板和生成结果说明。

## 两种交付物

- [`config.example.conf`](config.example.conf) 是沿用既有实际 Quantumult X 模板整理的完整配置。策略组、DNS、远程重写、本地规则、定时任务和各配置分区均保留；`[server_remote]`、`[server_local]` 不携带节点，`[mitm]` 不携带本地证书材料。
- [`filter_remote.safe.conf`](../../outputs/quantumult-x/filter_remote.safe.conf) 是只包含 `[filter_remote]` 的规则片段，适合已经有完整配置、只想独立更新规则的用户。

完整模板中的 `[filter_remote]` 使用当前生成的分类顺序和 `update-interval=86400`。规则内容通过远程分类文件更新，因此后续可以只更新规则片段，不必改动节点配置。

当前策略名称沿用个人配置中的稳定名称：

- 苹果服务
- 港台番剧
- 国际媒体
- AI
- 谷歌服务
- GitHub
- Spotify
- YouTube
- Netflix
- 海外抖音
- 电报代理
- 美国节点
- direct
- reject
- 全球加速
- proxy
- 兜底策略

## 分类文件顺序

生成的 `filter_remote.safe.conf` 使用以下优先级：

1. 明确的 `direct-exception`
2. `reject`、`privacy`
3. AI 与 Google Voice、YouTube、Netflix、TikTok、Telegram、Spotify 等地区敏感专项服务
4. 支付宝、微信、国内服务和国内影音直连例外
5. Apple、Google、Microsoft、云服务、社交、开发者、GitHub、港台番剧和国际媒体
6. 代理例外和全球代理兜底

这是远程过滤器的业务优先级，不是把所有规则语法混成一个文件。完全相同 selector 的策略冲突按安全策略和业务边界裁决；只有明确的 `direct-exception` 可以覆盖 `reject`。域名后缀、关键词、通配符和 CIDR 的 ordered overlap 会保留双方，并在审计报告中记录 first-match 约束。

分类文件使用 Quantumult X 原生的小写规则类型，并为每条规则保留完整的策略列。生成时会清理上游行尾注释，并过滤 Surge/Clash 专属选项，只保留当前配置使用的 QuanX 兼容选项。远程过滤器片段另外使用 `force-policy` 绑定分类策略；这样即使关闭资源解析器（`opt-parser=false`），规则也能直接导入。

单独的 `filter_remote.safe.conf` 输出只是 `[filter_remote]` 片段，不包含 `[policy]`、节点订阅、最终规则、DNS、重写或 MITM。导入前必须确认本地存在上面列出的策略名；`force-policy` 只对实际命中的远程资源生效，未命中的域名仍由本地其他规则和最终策略处理。QX 没有 Mihomo 的 `GEOSITE,openai` 兜底，也没有 Mihomo 的 `GEOSITE,cn` 域名兜底，因此 `oaistatsig.com` 已作为 QX 专用补充规则登记。QX 规则文件也不能声明订阅节点的 UDP 能力；完整模板默认使用 `fallback_udp_policy = reject`，使用地区敏感服务时仍应在 QX 客户端确认节点支持 UDP，或按客户端能力关闭 QUIC/HTTP3。

节点订阅、服务器标签、mitm 配置和本地证书不进入公共生成模板。
