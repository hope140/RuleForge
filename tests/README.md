# 回归样例

第一批测试样例：

- 支付宝主站和常见子域名应进入 direct。
- Apple 服务应进入 苹果服务。
- OpenAI、Claude、Gemini、Copilot 应进入 AI。
- Apple、Google、社交、开发者、云服务和国内服务应进入各自业务分类。
- 国内 IP 直连不能覆盖更具体的业务规则。
- 同一 selector 命中不同策略时按 `security > explicit override > specificity > category semantics > same-category source preference > fallback` 裁决；主来源只可在同一 category 内作为来源 tie-breaker，语义覆盖关系保留双方并记录顺序约束。
- MagicRule 刷新必须重新解析索引、manifest 和当前产物，校验客户端、分类、标准文本类型和文件哈希；共享产物仅允许在已声明的四行标准头归一化模式下使用正文哈希。离线缓存应可复用，刷新失败不得破坏旧缓存。
- 两端来源清单不得再依赖旧 Blackmatrix 下载地址；迁移补充保留 Claude、Civitai、Apple ID/邮件、Google Drive、BiliBili 国际版、Paramount+ 和 Peacock 的既有覆盖。
- 规则源失效、返回 HTML 或格式异常时构建应失败或明确报警。
- 规则源没有解析出任何规则时构建应失败，且抓取、解析或渲染失败不得覆盖已有正式输出。
- 缺失、空或全部禁用的来源清单、重复字段、分类文件名碰撞和同分类混合策略应在下载前失败；QX 原生选项和 Mihomo `DST-PORT` 应正确往返解析。
- first-match route simulator 应保证 OpenAI、reject/direct 和 direct-exception 探针命中预期策略。
- 最终产物回归按 QX 远程过滤器、优先规则文件及 Mihomo 路由片段的实际顺序读取规则，同时检查完整模板；不得重新按规则具体程度排序后代替实际命中。离线探针只覆盖明确的域名和 IP 规则，不模拟 GeoSite、GEOIP 数据库、DNS 或系统进程发现。
- 优先文件只能包含最终保留的规则；`mtalk.google.com` 和 `23.211.15.99/32` 的已淘汰规则不得复活。IPv4/IPv6 内联规则的策略列必须位于 `no-resolve` 等选项之前。
- 提升优先规则必须保留其业务前驱及裁决顺序；循环业务约束不能发布。安全分类缺失或为空时，预览仍须与渲染器的实际顺序一致。
- Microsoft 已审阅的下载/CDN 直连端点在优先排序后仍保持直连，该契约不得扩展成 Microsoft 根域直连；同 selector 已存在直接击败全部候选的唯一赢家时，低优先级候选之间的冲突不再阻止严格构建。
- Mihomo 模板的生成区块必须与 `rules.safe.yaml` 一致；同步需保留区块外配置和换行，拒绝缺失、重复或反向标记。CI 构建、同步后再运行回归和内核检查。
- 优先规则预览应过滤已淘汰规则，为存活重叠生成域名或 CIDR 样例，并把第三条规则干扰留在待审阅状态。
- Apple 服务统一契约应把 Apple Intelligence、iCloud 和 Apple 内容端点归入苹果服务，同时保留 reject 与 direct-exception 的安全优先级。
- GitHub Copilot、Grok、Bing/Copilot、gvt1、Netflix/Apple 共享基础设施、Prime Video 和 Trae/MarsCode 的业务边界应通过生成后的路由样例复核。
- 共享基础设施根域审计应记录 category、rule、risk、reason 和 source_id，并允许明确的服务 hostname 继续参与正常审计。
- 地区筛选同时验证 include/exclude，保留 `HK01` 等编号标签和混合地区归属；`Australia`、`Business`、`每日专线` 等词不得造成短码或单字误匹配。

双目标回归还应保证原有关键业务路由、Mihomo 不含 QX 类型或内嵌策略列、26 个 Rule Provider 与模板引用一致，并使用固定且校验过 SHA256 的 Mihomo 内核执行配置测试。

静态生成、route simulator 和 Mihomo 配置测试不等于 Quantumult X 或真实 Mihomo 客户端运行验证；客户端导入、订阅兼容性、节点 UDP 能力和真实业务页面仍需单独验收。
