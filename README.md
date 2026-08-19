# RuleForge

RuleForge 收集多个公开项目的代理分流规则，经过统一解析、规范化、去重和冲突裁决后，生成 Quantumult X 与 Mihomo 可以使用的分类规则。

项目只处理公开规则及其生成过程，不提供节点订阅，也不保存账号、Cookie、Token、证书或私钥。

## 输出内容

### Quantumult X

- [已裁决分类规则](outputs/quantumult-x/categories/safe/)用于远程分流。每条规则都带有策略列。
- [候选分类规则](outputs/quantumult-x/categories/candidates/)保留去重后的候选项，其中包括发生过冲突、最终可能被排除的规则。
- [远程过滤器片段](outputs/quantumult-x/filter_remote.safe.conf)按业务优先级引用各分类文件。
- [构建摘要](outputs/quantumult-x/build.json)记录来源哈希、规则数量和裁决统计。
- [冲突报告](outputs/quantumult-x/conflicts.md)记录冲突内容、处理结果和裁决原因。

### Mihomo

- [已裁决 Classical 规则](outputs/mihomo/categories/safe/)不包含策略列，具体策略由配置中的 `RULE-SET` 指定。
- [候选分类规则](outputs/mihomo/categories/candidates/)用于审阅合并和裁决前的候选项。
- [Rule Provider 片段](outputs/mihomo/rule-providers.safe.yaml)包含 26 个远程规则提供者。
- [路由规则片段](outputs/mihomo/rules.safe.yaml)按业务优先级引用 26 个 Rule Provider。
- [通用配置示例](profiles/mihomo/config.example.yaml)提供双订阅、地区测速组和业务策略组。
- [构建摘要](outputs/mihomo/build.json)与[冲突报告](outputs/mihomo/conflicts.md)记录 Mihomo 来源的构建结果。

## Mihomo 配置示例

下载 [`profiles/mihomo/config.example.yaml`](profiles/mihomo/config.example.yaml) 后，替换下面两个订阅地址占位符。

```yaml
REPLACE_WITH_SUBSCRIPTION_1
REPLACE_WITH_SUBSCRIPTION_2
```

模板默认只监听本机，`secret` 为空，TUN 与 IPv6 关闭，DNS 使用 Fake-IP。业务策略组排在地区测速组之前，图标来自 Orz-3 `mini/Color`。完整使用说明见 [Mihomo 模板说明](profiles/mihomo/README.md)。

26 个 Rule Provider 指向本仓库 `main` 分支，每 172800 秒刷新一次。模板不包含 Quantumult X 的重写、MITM 和定时脚本。

## 业务分类

| 分类 | 默认策略 | 用途 |
| --- | --- | --- |
| `reject`、`privacy` | `reject` | 广告、跟踪和隐私规则 |
| `alipay`、`wechat` | `direct` | 支付宝与微信直连 |
| `china-services` | `direct` | 国内电商、地图、出行和常用服务 |
| `china-streaming` | `direct` | 哔哩哔哩、优酷、爱奇艺和 AcFun |
| `china-direct`、`direct-exception` | `direct` | 国内直连与明确的直连例外 |
| `ai` | `AI` | OpenAI、Claude、Gemini、Copilot 等 AI 服务 |
| `apple` | `苹果服务` | Apple 相关服务 |
| `google-voice` | `美国节点` | Google Voice |
| `google` | `谷歌服务` | Google 相关服务 |
| `microsoft`、`cloud` | `全球加速` | Microsoft、OneDrive、Dropbox、MEGA 等服务 |
| `social` | `全球加速` | Twitter、Facebook、Instagram、Discord 等社交服务 |
| `developer` | `全球加速` | GitLab、Docker、Figma、Notion、npm 等开发者服务 |
| `github` | `GitHub` | GitHub 相关服务 |
| `spotify` | `Spotify` | Spotify |
| `telegram` | `电报代理` | Telegram |
| `tiktok` | `海外抖音` | TikTok |
| `youtube` | `YouTube` | YouTube |
| `netflix` | `Netflix` | Netflix |
| `china-media` | `港台番剧` | 国内及港台媒体补充规则 |
| `global-media` | `国际媒体` | 国际流媒体 |
| `proxy-exception`、`proxy` | `全球加速` | 明确的代理例外与全球代理兜底 |

## 生成过程

规则按业务用途分类，同一个分类可以同时包含域名、IP 段等不同规则类型。目标渲染器负责把统一规则模型转换为客户端语法，不改变分类和策略。

每次构建依次执行以下步骤。

1. 拉取来源并更新缓存。
2. 按来源格式解析为统一规则模型。
3. 合并同一业务分类中的多个来源。
4. 规范化规则并删除完全重复的内容。
5. 检查语义重叠和策略冲突。
6. 按来源优先级、策略优先级、规则具体程度和已登记的业务边界进行裁决。
7. 生成客户端规则、构建摘要和冲突报告。

Blackmatrix7 来源优先于补充来源，`direct` 优先于 `reject`。完全匹配的域名规则比覆盖范围更大的域名后缀规则具体，更长的子域后缀也比父域后缀具体。裁决器无法判断的冲突会保留在报告中，并从 `safe` 输出中排除。

`categories/candidates/` 用于检查候选规则，`categories/safe/` 才是提供给客户端的已裁决版本。

## 规则来源

当前主要来源为 [Blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)，并使用 [ConnersHua/RuleGo](https://github.com/ConnersHua/RuleGo) 与 [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR) 补充和交叉检查。

Quantumult X 与 Mihomo 使用两份独立清单。两份清单保持相同的业务分类和策略边界，各自采用适合目标客户端的上游格式，生成结果不会互相作为输入。

- [Quantumult X 来源清单](sources/quantumultx.yaml)
- [Mihomo 来源清单](sources/mihomo.yaml)
- [来源字段与冲突优先级](sources/README.md)
- [Quantumult X 输出说明](profiles/quantumult-x/README.md)
- [处理架构](docs/architecture.md)
- [回归测试说明](tests/README.md)

## 本地构建

需要 Python 3.11 或更高版本。生成器只使用 Python 标准库，不需要安装第三方 Python 包。

```powershell
python tools/ruleforge.py lint --manifest sources/quantumultx.yaml
python tools/ruleforge.py lint --manifest sources/mihomo.yaml
python -m unittest discover -s tests -v
python tools/ruleforge.py build --manifest sources/quantumultx.yaml --refresh --fail-on-conflict
python tools/ruleforge.py build --manifest sources/mihomo.yaml --refresh --fail-on-conflict
```

带有 `--refresh` 的构建会访问上游来源。任一来源抓取失败、解析异常、出现不受支持的规则类型或仍有未决冲突时，命令会失败。

## 自动更新

[Update proxy rules](.github/workflows/update-rules.yml) 每天在 UTC 2 时 17 分运行，对应中国时间 10 时 17 分。也可以从 GitHub Actions 页面手动触发。

工作流先运行回归测试，再依次构建 Quantumult X 与 Mihomo。两个目标全部通过后才会提交生成结果。单纯的生成时间和缓存状态变化不会产生提交。

CI 使用固定版本的 Mihomo v1.19.30，并校验下载文件的 SHA256。内核检查通过后，工作流还会访问 26 个公开 Mihomo Raw 地址，确认主分支上的远程规则可以读取。

## 使用边界

- 上游规则可能出现误判、遗漏、更新延迟或地址失效。使用者需要结合自己的网络环境测试。
- 静态测试和 Mihomo 内核配置检查只能证明文件格式与引用关系成立，不能代替真实客户端、节点、DNS 和业务页面验收。
- 规则内容的许可、署名和转载要求以上游项目说明为准。本项目不主张拥有上游规则的原创权。
- 请遵守所在地法律、组织网络规定和目标服务条款，不要将本项目用于违法或未经授权的用途。
- 正式使用前应保留原配置，以便出现问题时回退。

## 致谢

感谢以下公开规则项目及其维护者。

- [Blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [ConnersHua/RuleGo](https://github.com/ConnersHua/RuleGo)
- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
