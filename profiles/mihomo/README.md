# Mihomo 示例配置

[`config.example.yaml`](config.example.yaml) 是一份不含真实订阅和密钥的通用 Mihomo 配置。它使用两个订阅提供者，并引用本仓库生成的 26 个远程 Rule Provider。

## 使用方法

1. 下载 `config.example.yaml`。
2. 把 `REPLACE_WITH_SUBSCRIPTION_1` 和 `REPLACE_WITH_SUBSCRIPTION_2` 替换为真实订阅地址。
3. 如果本机端口冲突，修改 `mixed-port` 或 `external-controller`。
4. 将配置导入 Mihomo 客户端，等待订阅、规则和 GeoSite 数据下载完成。
5. TUN 默认关闭，普通应用需要使用系统代理 `127.0.0.1:7890`；需要接管未配置代理的应用时，再按客户端权限开启 TUN。

只有一个订阅时，可以删除 `provider-2` 配置块，并把 `特殊节点` 的 `use: [provider-1, provider-2]` 改为 `use: [provider-1]`。地区组使用 `include-all: true`，会自动从现有 provider 中筛选节点。

## 默认设置

- `mixed-port` 使用 7890。
- 外部控制器只监听 `127.0.0.1:9090`。
- `secret` 为空。
- `allow-lan`、TUN 与 IPv6 默认关闭。
- DNS 使用 Fake-IP 模式。
- `find-process-mode` 使用 `strict`，以支持规则中的 `PROCESS-NAME`。
- 策略选择和 Fake-IP 状态会保存。
- GeoSite 使用 MetaCubeX 的 `geosite.dat`，每 48 小时自动更新。
- `GEOSITE,cn,DIRECT` 位于明确代理规则之后，用于覆盖 Fake-IP 下无法通过 `GEOIP,CN` 判断的中国域名。

控制器目前只允许本机访问。若要改成局域网或公网监听，应先设置随机密钥，并同时限制防火墙和访问来源。

## 策略组

业务策略组排在地区测速组之前。地区组从两个订阅中筛选香港、台湾、日本、韩国、新加坡和美国节点，带有多个地区标签的节点或没有地区标签的节点保留在特殊节点组。地区组使用 `url-test`，业务组再引用地区组。模板保留订阅原始节点名称，不额外添加前缀。

策略组图标使用 Orz-3 `mini/Color`。地区测速要求健康检查返回 HTTP 204；如果订阅没有匹配地区，模板不会显式把空组回退到 `DIRECT`，应在客户端检查 provider 内容和节点筛选结果。业务组中是否允许 `DIRECT` 仍由各业务组的 `proxies` 列表决定。

## 规则更新

模板引用 26 个 Classical 文本 Rule Provider，并额外加载 GeoSite 数据库。规则文件不带策略列，`rules` 中的 `RULE-SET` 负责把分类交给对应策略组，`GEOSITE,cn,DIRECT` 负责中国域名兜底。

每个 Rule Provider 的刷新间隔为 172800 秒，也就是 48 小时。GitHub Actions 每天更新一次仓库中的规则文件，客户端按自己的刷新间隔重新下载。

## DNS 与 TUN 边界

模板默认是普通系统代理模式，不会因为 `dns.enable` 就自动接管 Windows 的全部 DNS 请求。Fake-IP、`dns-hijack` 和未配置系统代理的应用需要 TUN 或客户端自身的 DNS 接入才能生效。开启 TUN 后，如果某些应用只连接 IP 或使用 QUIC，建议按实际流量再启用域名嗅探，并检查防火墙和 DNS 泄漏。

当前模板只提供国内 DoH 解析器，没有替用户决定海外 DNS、分流 DNS 或代理 DNS。遇到海外 CDN 解析不佳、DoH 不可达或地区服务异常时，应按网络环境补充 `nameserver-policy`、`fallback` 或专用 DNS，不能只更换节点。

## 迁移范围

Quantumult X 的重写、MITM、脚本和定时任务没有迁入这份模板。Mihomo 内核检查通过只能证明配置格式、策略引用和 Rule Provider 引用有效，真实订阅、节点连通性、DNS 和客户端界面仍需单独测试。
