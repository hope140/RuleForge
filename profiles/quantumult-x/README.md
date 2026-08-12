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
2. 支付宝、微信和国内直连例外
3. AI、苹果、谷歌、GitHub、影音和其他专项服务
4. 港台番剧、国际媒体
5. 代理例外和全球代理兜底

这是远程过滤器的业务优先级，不是把所有规则语法混成一个文件。若两个分类仍然发生不同策略命中，先看 `outputs/quantumult-x/conflicts.md`，不要靠调整文件顺序掩盖未裁决冲突。

节点订阅、服务器标签、mitm 配置和本地证书不进入公共生成模板。
