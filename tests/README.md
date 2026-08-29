# 回归样例

第一批测试样例：

- 支付宝主站和常见子域名应进入 direct。
- Apple 服务应进入 苹果服务。
- OpenAI、Claude、Gemini、Copilot 应进入 AI。
- Apple、Google、社交、开发者、云服务和国内服务应进入各自业务分类。
- 国内 IP 直连不能覆盖更具体的业务规则。
- 同一 selector 命中不同策略时按安全策略、direct-exception、业务分类和 Blackmatrix tie-breaker 裁决；语义覆盖关系保留双方并记录顺序约束。
- 规则源失效、返回 HTML 或格式异常时构建应失败或明确报警。
- first-match route simulator 应保证 OpenAI、reject/direct 和 direct-exception 探针命中预期策略。

双目标回归还应保证 QX 输出不变、Mihomo 不含 QX 类型或内嵌策略列、26 个 Rule Provider 与模板引用一致，并使用固定且校验过 SHA256 的 Mihomo 内核执行配置测试。

静态生成、route simulator 和 Mihomo 配置测试不等于 Quantumult X 或真实 Mihomo 客户端运行验证；客户端导入、订阅兼容性、节点 UDP 能力和真实业务页面仍需单独验收。
