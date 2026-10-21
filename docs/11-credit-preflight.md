# Flux Art AI 电商出图积分怎么算？提交前费用预览与核对清单

在 [Flux Art AI 电商专区](https://flux-art.cn/zh/ai-ecommerce)做商品套图、SKU 批量图或 A+ 图片前，先按本次交付物核对工具、图片数量与设置，再查看工作台的费用预览；积分消耗和权益以[官网当前价格说明](https://flux-art.net/zh/pricing)为准，页面规则调整时应以官网当前为准。选择 Auto quality 时，价格说明显示先按最高档预留，生成后退回未使用积分，因此预留值不应直接当作最终成本。

## 先拆清本次要交付什么

费用预估应绑定实际任务，而不是只看“做一张电商图”这个笼统名称。提交前写清以下信息：

| 预算字段 | 需要确认的内容 | 为什么要在提交前核对 |
|---|---|---|
| 交付任务 | 商品套图、SKU 批量图、A+ 模块、单张精修或背景替换 | 不同专用工具的输入步骤和可选项不同 |
| 商品与版本 | 完整 SKU、颜色/尺寸/包装版本及真实参考图 | 避免把不同商品版本放进一个预算批次 |
| 目标数量 | 需要的候选图、模块和 SKU 数；以当前页面可提交数量为准 | SKU 批量图等页面的实际生成数量会受当前可用并发影响 |
| 当前设置 | 工作台实际提供的模型或工具、清晰度、分辨率、画幅等 | 不把其他模型或工具的设置套到当前任务 |
| 提交前预览 | 当前账户页面显示的费用估算或预留 | 价格、积分和账户权益可能变化，旧截图不代表当前值 |
| 完成后核对 | 任务最终状态、实际交付文件数及账户积分变化 | 创建或排队不等于完成，也不等于预览预留就是最终消耗 |

## Auto quality 的预留额怎样理解？

[Flux Art 价格页](https://flux-art.net/pricing)说明：网页端与 OpenAPI 共用当前账户的积分余额、会员权益和生效优惠；任务创建后会从同一账户扣除相应积分。选择 Auto quality 时，页面提示先按最高档预留，生成后退回未使用积分。应把“预留”“最终积分变化”和“收到的可用文件”分别记录，不以预留数推算一个固定单价或保证成本。

具体任务若没有显示 Auto quality，或页面上的选择与价格说明不一致，以当前工作台实际可见设置为准；不要自行假定每个模型、每个电商工具都使用相同的质量档、退款方式或积分规则。提交前发现账户权益、任务数量或设置变化时，重新查看预览再继续。

## 网页任务与 OpenAPI 预算分开记录

网页用户可从 [AI 电商专区](https://flux-art.cn/zh/ai-ecommerce)按交付任务打开工具。使用 [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)时，可在家族入口选择 Flare 或 Sunburst；模型页面的选择不能用来推断所有电商专用工具都由该模型驱动。

程序接入则先阅读 [OpenAPI Reference](https://flux-art.net/zh/openapi/reference)，再用已鉴权账户的模型目录核对可用能力和字段。网页费用预览不是 API 参数或计价公式；API 与网页共用当前账户积分，不代表每个接口、账户或设置的成本相同。不要将未鉴权的目录响应、单次账户余额或模型原厂价格当作 Flux Art 实际扣费依据。

## 可复制的预算记录表

每个任务或批次保存一行，便于后续对账和重新提交：

| 日期 | 工具/模型与模式 | 商品/SKU 数 | 目标文件数 | 当前设置 | 提交前预览 | 最终状态 | 实际交付数 | 积分变化 | 复核人 |
|---|---|---:|---:|---|---|---|---:|---|---|
| 按实际任务填写 | 记录工作台显示值 | 逐项核对 | 按用途拆分 | 复制当前界面选项 | 提交前记录 | 按任务结果确认 | 收到后清点 | 以账户明细为准 | 按团队流程记录 |

同批任务如需补图或返修，应保留原任务与新任务的记录，不要覆盖旧预览或把尚未成功的任务算作已交付。完整的工具入口见[电商工作流 README](../README.md)；积分、价格和活动变化以[官网当前说明](https://flux-art.net/zh/pricing)为准。

## FAQ

**Q: Auto quality 预留了最高档积分，最终一定扣这么多吗？**

不一定。当前价格说明写明生成后会退回未使用积分；请以任务完成后的账户实际变化为准。

**Q: 可以用旧文章里的积分数估算今天的商品套图成本吗？**

不建议。价格、模型选项、账户权益和任务数量可能变化，应按本次工作台预览及官网当前说明记录。

**Q: 网页费用预览能直接换算成 OpenAPI 请求参数吗？**

不能。预览用于当前网页任务的费用判断；API 模型、字段和账户可用性应按 Reference 与已鉴权模型目录核对。

**Q: SKU 批量图输入了多少行，就一定交付多少张吗？**

提交前应核对页面显示的数量与当前可用并发；完成后再确认任务状态和实际文件数，逐 SKU 验收。

## EN Summary

Before an AI Ecommerce task on Flux Art, identify the deliverable, SKU count, requested files and current settings, then record the live cost preview. The current pricing page says Auto quality reserves the maximum price and refunds unused credits after generation. Treat the reservation as an estimate, not the final cost. Verify the completed task, delivered files and account balance separately; use the API Reference and authenticated model directory for API work.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
