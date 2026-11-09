# Quantumult X 配置输出

这里存放 Quantumult X 的策略命名、规则顺序、完整配置模板和生成结果说明。

## 两种交付物

- [`config.example.conf`](config.example.conf) 是沿用既有实际 Quantumult X 模板整理的完整配置。策略组、DNS、远程重写、本地规则、定时任务和各配置分区均保留；`[server_remote]`、`[server_local]` 不携带节点，`[mitm]` 不携带本地证书材料。
- [`filter_remote.safe.conf`](../../outputs/quantumult-x/filter_remote.safe.conf) 是只包含 `[filter_remote]` 的规则片段，适合已经有完整配置、只想独立更新规则的用户。

完整模板中的 `[filter_remote]` 使用当前生成的分类顺序和 `update-interval=86400`，并在安全分类后、AI 分类前接入 `priority-overrides.safe.list`。该小文件只承载跨分类 specificity/业务 override 必须提前命中的规则，例如 Google 的 gvt1 子域；模板引用 28 个分类文件及 1 个跨分类优先规则文件。

维护示例配置时，构建后运行 `python tools/ruleforge.py sync-qx-profile` 同步整个 `[filter_remote]` 段，或加 `--check` 核对内容和顺序。

## 更新已有配置

1. 从示例配置的 `[policy]` 复制「游戏商店」和「游戏下载」两条完整策略行。已经有这两组时，用带图标的新策略行替换旧定义。
2. 在 `[filter_remote]` 合入片段中的 game-download、game-store 两条引用，按这个顺序放在 global-media 后、alipay 前。已经有这两条引用时，保留现有引用即可。
3. 更新远程规则，在连接日志里分别确认商店页面和游戏下载命中的策略。商店默认跟随全球加速，下载默认直连。

两个游戏组使用与 Mihomo 相同的 Koolson Qure 彩色图标。地区测速组按字母边界识别 HK01、US-01 等短码，含多个地区标签的节点可在「特殊节点」手选。该组包含全部节点。

远程规则引用的策略名称如下。

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
- 游戏商店（默认跟随全球加速）
- 游戏下载（默认直连）
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
3. 跨分类优先规则
4. AI 与 Google Voice、YouTube、Netflix、TikTok、Telegram、Spotify 等地区敏感专项服务
5. 开发者、GitHub、Apple、社交、Google、Microsoft、云服务、港台番剧和国际媒体
6. 游戏下载和游戏商店
7. 支付宝、微信、国内服务和国内影音直连规则
8. 代理例外和全球代理兜底

这是远程过滤器的业务优先级。跨分类 priority 文件只复制已经通过审计、但所在分类文件顺序无法表达的获胜规则，不改变分类文件的归属。完全相同 selector 的策略冲突按 `security > explicit override > specificity > category semantics > same-category source preference > fallback` 裁决；只有明确的 `direct-exception` 可以覆盖 `reject`。域名后缀、关键词、通配符和 CIDR 的 ordered overlap 会保留双方，并在审计报告中记录 first-match 约束。

分类文件使用 Quantumult X 原生的小写规则类型，并为每条规则保留完整的策略列。生成时会清理上游行尾注释，并过滤 Surge/Clash 专属选项，只保留当前配置使用的 QuanX 兼容选项。远程过滤器片段另外使用 `force-policy` 绑定分类策略；这样即使关闭资源解析器（`opt-parser=false`），规则也能直接导入。

单独的 `filter_remote.safe.conf` 输出只是 `[filter_remote]` 片段，不包含 `[policy]`、节点订阅、最终规则、DNS、重写或 MITM。导入前必须确认本地存在上面列出的策略名；`force-policy` 只对实际命中的远程资源生效，未命中的域名仍由本地其他规则和最终策略处理。QX 没有 Mihomo 的 `GEOSITE,openai` 兜底，也没有 Mihomo 的 `GEOSITE,cn` 域名兜底，因此 `oaistatsig.com` 已作为 QX 专用补充规则登记。QX 规则文件也不能声明订阅节点的 UDP 能力；完整模板设置 `fallback_udp_policy = reject`，分流选中的代理节点不支持 UDP 转发时，该 UDP 连接会被拒绝。

节点订阅、服务器标签、mitm 配置和本地证书不进入公共生成模板。

微博重写使用本目录的 `weibo.snippet`，基于 fmz200/wool_scripts 的快照修改三条远程 `echo-response` 为 `reject-dict`，保留原匹配条件。该快照不会自动跟随上游更新；引用的外部脚本仍按原地址加载。来源、作者与许可见文件头及 `LICENSE.weibo`。现有配置需将 `[rewrite_remote]` 中的微博地址替换为模板中的地址，更新远程重写后生效。
