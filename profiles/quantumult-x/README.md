# Quantumult X 配置输出

这里存放 Quantumult X 的策略命名、规则顺序和生成结果说明。

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
- direct
- reject
- 全球加速
- 兜底策略

## 分类文件顺序

生成的 `filter_remote.safe.conf` 使用以下优先级：

1. `reject`、`privacy`
2. 支付宝、微信、国内服务和国内影音直连例外
3. AI、苹果、谷歌、Microsoft、云服务、社交、开发者、GitHub、影音和其他专项服务
4. 港台番剧、国际媒体
5. 代理例外和全球代理兜底

这是远程过滤器的业务优先级，不是把所有规则语法混成一个文件。规则冲突在生成前按以下顺序处理：Blackmatrix 来源优先，`direct` 优先于 `reject`，更具体的单独规则优先于宽泛规则，再按业务边界处理 Google Voice、AI、YouTube、Apple、Google 与代理分类；其余冲突继续保留在报告中，不靠调整文件顺序掩盖。

分类文件使用 Quantumult X 原生的小写规则类型，并为每条规则保留完整的策略列。生成时会清理上游行尾注释，并过滤 Surge/Clash 专属选项，只保留当前配置使用的 QuanX 兼容选项。远程过滤器片段另外使用 `force-policy` 绑定分类策略；这样即使关闭资源解析器（`opt-parser=false`），规则也能直接导入。

节点订阅、服务器标签、mitm 配置和本地证书不进入公共生成模板。
