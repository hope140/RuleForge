# Mihomo 模板

`config.example.yaml` 是不含真实订阅和密钥的通用 Mihomo 模板。使用前至少替换：

1. `provider-1` 与 `provider-2` 的订阅 URL。
2. `external-controller` 的 `secret`。
3. 如端口冲突，调整 `mixed-port` 与控制器端口。

模板默认仅监听本机、关闭 TUN 与 IPv6、启用 Fake-IP DNS。地区组通过 `filter` 和 `exclude-filter` 从两个订阅筛选节点，业务组再引用地区组。Rule Provider 每 172800 秒刷新一次。

Quantumult X 的重写、MITM、脚本和定时任务没有迁入。模板通过静态和 Mihomo 内核检查也不等同于真实订阅、节点、DNS 与客户端环境验收，首次使用应保留原配置以便回滚。

`config.branch-test.yaml` 用于合并前测试当前功能分支。它只包含一个订阅入口，替换 `REPLACE_WITH_YOUR_SUBSCRIPTION_URL` 后即可导入；26 个 Rule Provider 均指向 `codex/mihomo-rules` 分支。合并到 `main` 后应改用 `config.example.yaml`，不要长期依赖测试分支 URL。
