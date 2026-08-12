# RuleForge

个人代理规则整理与生成项目。

目标是把来自不同作者、不同客户端格式的公开规则，经过来源登记、格式解析、规范化、去重和冲突审计后，生成可验证的 Quantumult X 配置；后续再考虑扩展 Clash、Surge 等输出。

## 当前状态

- 仓库：实验性、私有
- 第一目标：Quantumult X
- 当前种子来源：25 条公开分流资源，包含 Blackmatrix、RuleGo 和 ACL4SSR 的交叉来源
- 当前阶段：按业务分类合并、规范化、去重和冲突审计
- 尚未承诺：自动生成结果可直接用于生产环境

## 设计原则

1. 原始来源、规范化结果和生成结果分层保存。
2. 完全重复的规则自动去重。
3. 不同策略之间的冲突只报告，不盲目删除。
4. 每条生成规则保留来源和处理依据。
5. 不保存节点订阅、密码、Cookie、证书、私钥等敏感内容。
6. 先验证 Quantumult X，再扩展到其他客户端。
7. 上游规则遵循各自的许可证、署名和转载要求。

## 目录

- `sources/`：上游来源清单和来源元数据
- `profiles/`：业务策略和输出目标定义
- `docs/`：架构、规则语义和维护约定
- `reports/`：冲突、去重和更新报告
- `tests/`：回归样例和客户端边界测试
- `tools/`：后续的拉取、解析、构建和审计工具

## 本地运行

不安装第三方运行时依赖即可执行：

```powershell
python tools/ruleforge.py lint --manifest sources/quantumultx.yaml
python tools/ruleforge.py build --manifest sources/quantumultx.yaml
```

构建会生成：

- `outputs/quantumult-x/categories/candidates/<category>.list`：按业务分类合并后的完整候选结果
- `outputs/quantumult-x/categories/safe/<category>.list`：排除未裁决冲突后的保守结果
- `outputs/quantumult-x/filter_remote.safe.conf`：可复制到 Quantumult X 的分类远程过滤器片段
- `outputs/quantumult-x/audit.json`：机器可读审计数据
- `outputs/quantumult-x/conflicts.md`：需要人工确认的冲突
- `outputs/quantumult-x/build.json`：来源快照、哈希和构建摘要

在策略裁决器完成前，不应把候选结果直接作为日常配置；优先查看保守结果和冲突报告。分类文件可以混合 `HOST`、`HOST-SUFFIX`、`IP-CIDR` 等规则类型，因为分类依据是业务意图，而不是语法类型。

当前仓库仍为私有仓库，因此 `filter_remote.safe.conf` 中的 GitHub Raw 地址暂时只作为发布模板；要在 Quantumult X 中直接远程拉取，需要先公开这些生成文件或改成自己的可访问静态地址。

RuleForge 是独立项目，不依赖其他配置仓库。旧项目不会被读取、同步或作为生成输入。

## 免责声明

本项目只整理和生成配置，不保证任何上游规则的准确性、完整性或持续可用性。使用前应检查来源要求，并在目标客户端中实际验证。
