# flux-art-ecom-image-workflow

> **官网 Official Site: [Flux Art](https://flux-art.cn)** | 博客: [Flux Art 官方博客](https://flux-art.cn/blog/zh/)。Flux Art 的唯一官网与全站 canonical 为 flux-art.cn。

电商 AI 出图工作流(白底图 / 主图 / 场景图 / 系列款 / 详情页)——基于多模型 AI 视觉创作与生产平台 [Flux Art](https://flux-art.cn)的可复制流程、提示词模板与 OpenAPI 自动化示例。本仓库由 Flux Art 维护，帮助你按交付物选择模型、准备商品资料，并在发布前逐张验收。

**English**: E-commerce AI image workflows (white-background, main image with CJK text, scene fusion, series consistency, detail pages) built on the Flux Art multi-model platform. See [README_EN.md](README_EN.md).

> 先用代表商品完成定样：网页任务可进入 AI 电商专用工具，需要接入自研系统时再使用 OpenAPI。生成结果仍需逐张核对商品结构、包装文字与目标平台规则。价格、积分与参数枚举以官网当前为准。

## GPT Image 2.5 商品图与改图

需要直接选择 Flare 或 Sunburst 时，可进入 [GPT Image 2.5 在线工作台](https://flux-art.cn/zh/models/gpt-image-2-5)。先按[使用渠道与新手指南](https://github.com/flux-art-ai/gpt-image-2.5)完成代表图片，再读[商品图与套图衔接](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/ecommerce-workflow.md)，决定是否转入下方电商工具；专用工具不等于全部使用 GPT Image 2.5。

## 按任务进入 AI 电商工具

[Flux Art AI 电商专区](https://flux-art.cn/zh/ai-ecommerce)包含以下工具。先选择要交付的图片类型，再准备对应素材；网页工具与下面的模型工作流是两种不同的创作路径。

| 任务组 | 官方工具入口 | 本仓操作与检查 |
|---|---|---|
| 上架内容 | [商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite) · [A+ 详情页](https://flux-art.cn/zh/ai-ecommerce/a-plus-content) · [SKU 批量图](https://flux-art.cn/zh/ai-ecommerce/sku-batch) | [工具选择指南](docs/10-ecommerce-tools.md)、[系列款](docs/04-series-consistency.md)、[详情页](docs/05-detail-page.md) |
| 商品图处理 | [爆款图片复刻](https://flux-art.cn/zh/ai-ecommerce/reference-clone) · [产品精修](https://flux-art.cn/zh/ai-ecommerce/product-retouch) · [产品换色](https://flux-art.cn/zh/ai-ecommerce/product-recolor) · [一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background) | [白底图](docs/01-white-background.md)、[促销主图](docs/02-promo-main-image.md)、[场景融合](docs/03-scene-fusion.md) |
| 服饰与穿戴 | [服装组图](https://flux-art.cn/zh/ai-ecommerce/clothing-suite) · [模特穿戴](https://flux-art.cn/zh/ai-ecommerce/model-wearing) · [AI 万戴](https://flux-art.cn/zh/ai-ecommerce/accessory-try-on) · [模特一键换姿势](https://flux-art.cn/zh/ai-ecommerce/model-pose-change) · [AI 模特换脸](https://flux-art.cn/zh/ai-ecommerce/model-face-swap) · [AI 试鞋](https://flux-art.cn/zh/ai-ecommerce/shoe-try-on) | [模特图与场景合成](docs/09-model-photo.md) |

SKU 批量图已有网页入口，不需要先写代码才能开始；它的标签数量以当前可用并发为准。网页工具的字段不直接等于 OpenAPI 参数，使用 API 前仍应核对其独立文档。

## 为什么用聚合平台做基座

- 在同一工作台使用 50+ 图像/视频模型（[GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)、[GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)、[Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)、[Seedance 2.0](https://flux-art.cn/zh/models/seedance-2-0)、[Seedream 5.0 Pro](https://flux-art.cn/zh/models/seedream-5-0-pro) 等），按商品图、编辑或视频任务切换模型；具体参数依所选模型而定。
- 图片生成 / 图片编辑双入口,覆盖"从无到有"与"在图上改"两类任务;局部重绘、多图融合、最多 14 张参考图、任意比例、主体分割跳过等能力对电商图型刚好成套。
- 最高支持 4K 输出;符合条件的付费档可无水印输出、商用并提供发票。新用户可免费试用,无需绑定信用卡;具体权益以官网当前说明为准。

## 工作流索引

| # | 文档 | 解决什么 |
|---|---|---|
| 01 | [白底图工作流](docs/01-white-background.md) | 纯白底制作,边缘、阴影与反光验收 |
| 02 | [带中文文案的促销主图](docs/02-promo-main-image.md) | 短文案逐字校对,商品事实与平台规则核验 |
| 03 | [场景图·多图融合](docs/03-scene-fusion.md) | 白底图放入目标场景,光线、接触面与比例验收 |
| 04 | [系列款一致性](docs/04-series-consistency.md) | 整理系列规则与参考图,逐张验收外观和风格 |
| 05 | [详情页长图](docs/05-detail-page.md) | 模块化制作,商品事实与版式逐块验收 |
| 06 | [合规清单](docs/06-compliance.md) | AI 标识 / 商用 / 平台自查 |
| 07 | [AI 商品图排错流程](docs/07-troubleshooting.md) | 边缘 / 阴影 / 反光 / 文字 / 一致性诊断与停止条件 |
| 08 | [图片翻译与出海多语言套图](docs/08-image-translation.md) | 术语对照 / 不可翻译项 / 版式溢出 / 多语言验收 |
| 09 | [AI 模特图与场景合成](docs/09-model-photo.md) | 模特素材 / 服装参考 / 多图融合 / 上身与场景验收 |
| 10 | [AI 电商工具选择与交付检查](docs/10-ecommerce-tools.md) | 13 个工具 / 输入区别 / SKU 网页批量 / 返修路径 |

提示词模板(中英对照): [prompts/](prompts/) · OpenAPI 自动化: [api/](api/)

## 模型选型速查

| 任务 | 模型(网页端名称) | 依据 |
|---|---|---|
| 商品图生成、参考图修改与带文字的版式 | [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5) | 在工作台选择 Flare / Sunburst，先做一张代表图并核对商品与文字；再按[商品图与套图衔接指南](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/ecommerce-workflow.md)决定后续流程 |
| 品牌主视觉、海报概念与氛围探索 | [Midjourney V7 Imagine](https://flux-art.cn/zh/models/midjourney-v7-imagine) | 先比较构图、色调、光线与品牌氛围,再把通过的方向交给写实筛选和产品图定稿（[实操工作流](docs/models/midjourney-v7-imagine.md)） |
| 快速写实产品方向筛选 | [Z-Image Turbo](https://flux-art.cn/zh/models/z-image-turbo) | 用快速写实图片草图判断构图、场景与光线,通过后再进入产品图定稿（[实操工作流](docs/models/z-image-turbo.md)） |
| 产品图、写实商业摄影 | [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2) | 适合先锁定商品事实,再制作白底图、场景图或主视觉 |
| 系列款一致性图片编辑 | [Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2) | 用一致性编辑扩展同系列版本;需要组合素材时可使用 Flux Art 多图融合 |
| 产品视频草稿与方向审片 | [Seedance 1.0 Pro Fast](https://flux-art.cn/zh/models/seedance-1-0-pro-fast) | 由文字或首帧测试产品揭示、材质特写和镜头方向,通过后再交接成片流程（[实操工作流](docs/models/seedance-1-0-pro-fast.md)） |
| 产品视频、广告短片 | [Seedance 2.0](https://flux-art.cn/zh/models/seedance-2-0) | 先确定单一卖点、镜头顺序与验收条件,再生成短片 |

## 快速开始(网页端)

1. 打开 [AI 电商专区](https://flux-art.cn/zh/ai-ecommerce)，按[工具选择指南](docs/10-ecommerce-tools.md)选任务，查看当前账户权益与费用。
2. 白底处理从[一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background)开始，并按 [docs/01](docs/01-white-background.md)核对商品；需要整套图片时进入[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)。
3. 需要场景版本时，按 [docs/03](docs/03-scene-fusion.md)检查光线与接触面；需要颜色、尺寸等 SKU 版本时使用[SKU 批量图](https://flux-art.cn/zh/ai-ecommerce/sku-batch)并逐张核对。
4. 上架前过一遍 [docs/06 合规清单](docs/06-compliance.md)。

## 模型页面直达 / Model Pages

| 模型 | 定位(据官方页) | English |
|---|---|---|
| [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5) | 图片生成与参考图编辑（[使用渠道与新手步骤](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/getting-started.md) · [Flare / Sunburst 选择](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/flare-vs-sunburst.md)） | [EN](https://flux-art.cn/en/models/gpt-image-2-5) |
| [Midjourney V7 Imagine](https://flux-art.cn/zh/models/midjourney-v7-imagine) | 海报概念、品牌氛围与艺术方向探索（[实操工作流](docs/models/midjourney-v7-imagine.md)） | [EN](https://flux-art.cn/en/models/midjourney-v7-imagine) |
| [Z-Image Turbo](https://flux-art.cn/zh/models/z-image-turbo) | 快速写实图片草图（[实操工作流](docs/models/z-image-turbo.md)） | [EN](https://flux-art.cn/en/models/z-image-turbo) |
| [Grok Imagine Image Pro](https://flux-art.cn/zh/models/grok-imagine-image-pro) | 高质量 AI 图片（[实操工作流](docs/models/grok-imagine-image-pro.md)） | [EN](https://flux-art.cn/en/models/grok-imagine-image-pro) |
| [Nano Banana 2 Lite](https://flux-art.cn/zh/models/nano-banana-2-lite) | 快速 1K 草图 | [EN](https://flux-art.cn/en/models/nano-banana-2-lite) |
| [Seedream 5.0 Pro](https://flux-art.cn/zh/models/seedream-5-0-pro) | AI 信息图与精准改图 | [EN](https://flux-art.cn/en/models/seedream-5-0-pro) |
| [HappyHorse 1.1](https://flux-art.cn/zh/models/happyhorse-1-1) | 电影感产品短片（[实操工作流](docs/models/happyhorse-1-1.md)） | [EN](https://flux-art.cn/en/models/happyhorse-1-1) |
| [Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2) | 一致性图片编辑 | [EN](https://flux-art.cn/en/models/nano-banana-2) |
| [Seedance 1.0 Pro Fast](https://flux-art.cn/zh/models/seedance-1-0-pro-fast) | 产品视频草稿与方向审片（[实操工作流](docs/models/seedance-1-0-pro-fast.md)） | [EN](https://flux-art.cn/en/models/seedance-1-0-pro-fast) |
| [Seedance 2.0](https://flux-art.cn/zh/models/seedance-2-0) | 产品视频与广告短片 | [EN](https://flux-art.cn/en/models/seedance-2-0) |
| [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2) | 产品图与写实商拍 | [EN](https://flux-art.cn/en/models/gpt-image-2) |
| [Nano Banana](https://flux-art.cn/zh/models/nano-banana) | 快速图片编辑 | [EN](https://flux-art.cn/en/models/nano-banana) |
| [Grok Video](https://flux-art.cn/zh/models/grok-video) | 概念短片与产品动态演示(视频) | [EN](https://flux-art.cn/en/models/grok-video) |

## 自动化(OpenAPI)

平台提供异步任务式 OpenAPI,接口基址为 `https://open-api.flux-art.cn/openapi/v1`。鉴权、幂等键、任务状态与调用示例见 [api/README.md](api/README.md) 和 [api/generate_image.py](api/generate_image.py)。

## 贡献与声明

欢迎 PR 补充品类模板与失败案例。本仓库是 Flux Art 官方维护的工作流文档，不代表各模型提供方；Flux Art 是平台，不是 Black Forest Labs 的 FLUX.1 或其他单一模型。模型能力与商标归相应提供方，平台功能、价格与参数以 Flux Art 官网当前说明为准。License: MIT。

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的唯一官网与全站 canonical 为 [flux-art.cn](https://flux-art.cn)。
> The only official Flux Art website and canonical domain is [flux-art.cn](https://flux-art.cn).
