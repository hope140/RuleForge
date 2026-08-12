# RuleForge

个人代理分流规则整理、合并和生成项目。

## 前言

RuleForge 从多个公开规则项目收集分流规则，按业务分类统一解析、规范化、去重和冲突审计，当前主要生成 Quantumult X 分类过滤器。

本项目的定位是“来源整理和规则加工”，不是另一个规则作者集合，也不包含节点订阅、账号、Cookie、证书或私钥。

## 索引

### Quantumult X 分流规则

- [已裁决分类规则](outputs/quantumult-x/categories/safe/)：按来源和策略优先级生成，可作为后续客户端验证的起点。
- [完整候选分类规则](outputs/quantumult-x/categories/candidates/)：保留去重后的全部候选，包含尚未裁决的冲突。
- [远程过滤器片段](outputs/quantumult-x/filter_remote.safe.conf)：分类远程过滤器配置模板。
- [构建摘要](outputs/quantumult-x/build.json)：来源哈希、规则数量和裁决统计。
- [冲突报告](outputs/quantumult-x/conflicts.md)：按业务分类记录每次冲突及裁决原因。

### 业务分类

| 分类 | 默认策略 | 说明 |
| --- | --- | --- |
| `ai` | `AI` | OpenAI、Claude、Gemini、Copilot 等 AI 服务 |
| `apple` | `苹果服务` | Apple 相关服务 |
| `google` | `谷歌服务` | Google 相关服务 |
| `microsoft` / `cloud` | `全球加速` | Microsoft、OneDrive、Dropbox、MEGA 等海外云服务 |
| `social` | `全球加速` | Twitter、Facebook、Instagram、Discord 等社交服务 |
| `developer` | `全球加速` | GitLab、Docker、Figma、Notion、npm 等开发者服务 |
| `china-media` | `港台番剧` | 国内及港台媒体补充分类 |
| `china-streaming` | `direct` | 哔哩哔哩、优酷、爱奇艺、AcFun 等国内影音 |
| `china-services` | `direct` | 国内电商、地图、出行、内容和基础服务 |
| `global-media` | `国际媒体` | 国际流媒体分类 |
| `github` | `GitHub` | GitHub 相关服务 |
| `youtube` / `netflix` | 对应策略 | 视频服务 |
| `alipay` / `wechat` | `direct` | 国内应用直连例外 |
| `reject` / `privacy` | `reject` | 广告和跟踪类规则 |
| `proxy` / `proxy-exception` | 对应策略 | 代理和代理例外 |

### 来源与文档

- [来源清单](sources/quantumultx.yaml)
- [来源字段、命名和优先级](sources/README.md)
- [Quantumult X 输出说明](profiles/quantumult-x/README.md)
- [处理架构](docs/architecture.md)
- [回归样例说明](tests/README.md)

## 规则

规则不按 `HOST`、`HOST-SUFFIX`、`IP-CIDR` 等语法类型拆成互不相关的文件，而是按业务意图归类。同一业务分类可以包含多种规则类型，但输出时使用统一的目标客户端格式。

构建处理顺序：

1. 拉取并缓存来源。
2. 按来源格式解析为统一规则模型。
3. 按业务分类合并。
4. 规范化并删除完全重复的规则。
5. 按以下顺序处理策略冲突：Blackmatrix 来源、`direct` 优先于 `reject`、具体规则优先于宽泛规则、已登记的业务分类边界。
6. 无法由以上规则判断的冲突保留在报告中，并从已裁决输出排除。

具体规则包括 `HOST` 对覆盖它的 `HOST-SUFFIX`，以及更长的子域后缀对父域后缀。候选目录用于审阅，`safe` 目录才是经过当前裁决器筛选的版本。

## 来源

当前来源以 [Blackmatrix7/ios_rule_script 的 Quantumult X 目录](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/QuantumultX) 为主要来源，并使用 [ConnersHua/RuleGo](https://github.com/ConnersHua/RuleGo) 和 [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR) 进行交叉补充。Blackmatrix 目录本身包含大量按服务拆分的列表，本轮先纳入常用且业务边界清晰的第一批来源，后续继续按同一流程扩展，不把目录中的所有条目无差别塞进主配置。

所有来源地址、格式、分类、策略映射和维护说明均登记在 [sources/quantumultx.yaml](sources/quantumultx.yaml) 中。来源更新后应重新构建，不直接手工覆盖生成文件。

## 本地构建

无需安装第三方运行时依赖：

```powershell
python tools/ruleforge.py lint --manifest sources/quantumultx.yaml
python -m unittest discover -s tests -v
python tools/ruleforge.py build --manifest sources/quantumultx.yaml --refresh --fail-on-conflict
```

仓库已公开，生成的 Raw 地址可以被 Quantumult X 直接远程拉取。日常手动更新时运行上面的构建命令，确认无未决冲突后提交并推送 `outputs/quantumult-x`。

## 自动更新

仓库使用 [GitHub Actions](.github/workflows/update-rules.yml) 每天运行一次，时间为 UTC 02:17，即香港时间 10:17。工作流会依次执行回归测试、刷新全部公开来源、解析、去重和冲突审计。

- 构建失败、来源抓取失败或出现未决冲突时，不会推送新规则，上一版继续保留。
- 只有规则、来源哈希、数量或审计结果发生实际变化时才会提交，单纯生成时间变化不会产生提交。
- 也可以在 GitHub 的 `Actions` 页面手动运行 `Update Quantumult X rules`。
- 自动更新成功后，Quantumult X 按远程过滤器中的 `update-interval=172800` 重新拉取。

## 特别声明

1. 本项目主要进行公开规则的登记、格式转换、分类、去重和审计，不主张拥有上游规则的原创权；具体权利、许可和署名要求以上游项目说明为准。
2. 上游规则来自互联网，无法保证其准确性、完整性、实时性或持续可用性。生成结果不代表任何上游项目对本项目的认可。
3. 本项目不提供节点订阅，也不处理账号、密码、Cookie、Token、证书或私钥。使用者应自行保管本地配置和隐私数据。
4. 使用者应自行确认所在国家、地区、组织网络及目标服务的法律、合规和服务条款要求，不得将本项目用于违法或未经授权的用途。
5. 生成结果只代表静态规则处理结果，不等同于 Quantumult X 客户端、网络环境或具体业务页面的运行验证；正式使用前应自行测试并保留回滚方案。
6. 某条规则的内容、误判或失效问题，应优先根据来源记录联系对应上游维护者；本项目只负责整理链路和生成过程。
7. 本项目会根据来源变化、客户端格式和维护需要调整目录、优先级、免责声明及生成结果，使用者应以当前版本说明为准。

## 感谢

感谢所有公开规则项目及其维护者：

- [Blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [ConnersHua/RuleGo](https://github.com/ConnersHua/RuleGo)
- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)

本项目只在来源登记和格式转换层面进行整合，尽量保留来源信息并遵守各项目的许可和声明。
