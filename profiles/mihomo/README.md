# Mihomo 示例配置

[`config.example.yaml`](config.example.yaml) 是一份不含真实订阅和密钥的通用 Mihomo 配置。它使用两个订阅提供者，并引用本仓库生成的 26 个远程 Rule Provider。

## 使用方法

1. 下载 `config.example.yaml`。
2. 把 `REPLACE_WITH_SUBSCRIPTION_1` 和 `REPLACE_WITH_SUBSCRIPTION_2` 替换为真实订阅地址。
3. 如果本机端口冲突，修改 `mixed-port` 或 `external-controller`。
4. 将配置导入 Mihomo 客户端，等待订阅和规则下载完成。

只有一个订阅时，可以删除 `provider-2` 配置块，并把所有 `use: [provider-1, provider-2]` 改为 `use: [provider-1]`。

## 默认设置

- `mixed-port` 使用 7890。
- 外部控制器只监听 `127.0.0.1:9090`。
- `secret` 为空。
- `allow-lan`、TUN 与 IPv6 默认关闭。
- DNS 使用 Fake-IP 模式。
- 策略选择和 Fake-IP 状态会保存。

控制器目前只允许本机访问。若要改成局域网或公网监听，应先设置随机密钥，并同时限制防火墙和访问来源。

## 策略组

业务策略组排在地区测速组之前。地区组从两个订阅中筛选香港、台湾、日本、韩国、新加坡和美国节点，其余节点进入特殊节点组。地区组使用 `url-test`，业务组再引用地区组。

策略组图标使用 Orz-3 `mini/Color`。节点名称不符合现有筛选表达式时，节点可能进入特殊节点组，也可能让某个地区组为空。

## 规则更新

模板引用 26 个 Classical 文本 Rule Provider。规则文件不带策略列，`rules` 中的 `RULE-SET` 负责把分类交给对应策略组。

每个 Rule Provider 的刷新间隔为 172800 秒，也就是 48 小时。GitHub Actions 每天更新一次仓库中的规则文件，客户端按自己的刷新间隔重新下载。

## 迁移范围

Quantumult X 的重写、MITM、脚本和定时任务没有迁入这份模板。Mihomo 内核检查通过只能证明配置格式、策略引用和 Rule Provider 引用有效，真实订阅、节点连通性、DNS 和客户端界面仍需单独测试。
