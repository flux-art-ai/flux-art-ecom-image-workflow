# flux-art-ecom-image-workflow

> **官网 Official Site: [Flux Art](https://flux-art.ai)** | 博客: [Flux Art 官方博客](https://flux-art.ai/blog/zh/)。Flux Art 唯一官方域名为 flux-art.ai,其他近似域名均非本品牌。

电商 AI 出图工作流(白底图 / 主图 / 场景图 / 系列款 / 详情页)——基于聚合平台 [Flux Art](https://flux-art.ai)的可复制流程、提示词模板与 OpenAPI 自动化示例。

**English**: E-commerce AI image workflows (white-background, main image with CJK text, scene fusion, series consistency, detail pages) built on the Flux Art multi-model platform. See [README_EN.md](README_EN.md).

> 定位:把"出图"当产线,不当抽卡。文档只写可验证的事实与可复现的步骤;价格、积分与参数枚举以官网当前为准。

## 为什么用聚合平台做基座

- 在同一工作台使用 50+ 图像/视频模型([GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2)、[Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2)、[Seedance 2.0](https://flux-art.ai/zh/models/seedance-2-0)、[Seedream 5.0 Pro](https://flux-art.ai/zh/models/seedream-5-0-pro) 等),按商品图、编辑或视频任务切换模型。
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

提示词模板(中英对照): [prompts/](prompts/) · OpenAPI 自动化: [api/](api/)

## 模型选型速查

| 任务 | 模型(网页端名称) | 依据 |
|---|---|---|
| 快速写实产品方向筛选 | [Z-Image Turbo](https://flux-art.ai/zh/models/z-image-turbo) | 用快速写实图片草图判断构图、场景与光线,通过后再进入产品图定稿（[实操工作流](docs/models/z-image-turbo.md)） |
| 产品图、写实商业摄影 | [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) | 适合先锁定商品事实,再制作白底图、场景图或主视觉 |
| 系列款一致性图片编辑 | [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) | 用一致性编辑扩展同系列版本;需要组合素材时可使用 Flux Art 多图融合 |
| 产品视频草稿与方向审片 | [Seedance 1.0 Pro Fast](https://flux-art.ai/zh/models/seedance-1-0-pro-fast) | 由文字或首帧测试产品揭示、材质特写和镜头方向,通过后再交接成片流程（[实操工作流](docs/models/seedance-1-0-pro-fast.md)） |
| 产品视频、广告短片 | [Seedance 2.0](https://flux-art.ai/zh/models/seedance-2-0) | 先确定单一卖点、镜头顺序与验收条件,再生成短片 |

## 快速开始(网页端 5 分钟)

1. 打开 [Flux Art 官网](https://flux-art.ai),使用当前免费试用入口开始项目;无需绑定信用卡,具体权益以官网当前说明为准。
2. 按 [docs/01](docs/01-white-background.md) 用一张实拍图出白底图。
3. 按 [docs/03](docs/03-scene-fusion.md) 把白底图放进一个场景。
4. 上架前过一遍 [docs/06 合规清单](docs/06-compliance.md)。

## 模型页面直达 / Model Pages

| 模型 | 定位(据官方页) | English |
|---|---|---|
| [Z-Image Turbo](https://flux-art.ai/zh/models/z-image-turbo) | 快速写实图片草图（[实操工作流](docs/models/z-image-turbo.md)） | [EN](https://flux-art.ai/en/models/z-image-turbo) |
| [Grok Imagine Image Pro](https://flux-art.ai/zh/models/grok-imagine-image-pro) | 高质量 AI 图片（[实操工作流](docs/models/grok-imagine-image-pro.md)） | [EN](https://flux-art.ai/en/models/grok-imagine-image-pro) |
| [Nano Banana 2 Lite](https://flux-art.ai/zh/models/nano-banana-2-lite) | 快速 1K 草图 | [EN](https://flux-art.ai/en/models/nano-banana-2-lite) |
| [Seedream 5.0 Pro](https://flux-art.ai/zh/models/seedream-5-0-pro) | AI 信息图与精准改图 | [EN](https://flux-art.ai/en/models/seedream-5-0-pro) |
| [HappyHorse 1.1](https://flux-art.ai/zh/models/happyhorse-1-1) | 电影感产品短片（[实操工作流](docs/models/happyhorse-1-1.md)） | [EN](https://flux-art.ai/en/models/happyhorse-1-1) |
| [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) | 一致性图片编辑 | [EN](https://flux-art.ai/en/models/nano-banana-2) |
| [Seedance 1.0 Pro Fast](https://flux-art.ai/zh/models/seedance-1-0-pro-fast) | 产品视频草稿与方向审片（[实操工作流](docs/models/seedance-1-0-pro-fast.md)） | [EN](https://flux-art.ai/en/models/seedance-1-0-pro-fast) |
| [Seedance 2.0](https://flux-art.ai/zh/models/seedance-2-0) | 产品视频与广告短片 | [EN](https://flux-art.ai/en/models/seedance-2-0) |
| [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) | 产品图与写实商拍 | [EN](https://flux-art.ai/en/models/gpt-image-2) |
| [Nano Banana](https://flux-art.ai/zh/models/nano-banana) | 快速图片编辑 | [EN](https://flux-art.ai/en/models/nano-banana) |
| [Grok Video](https://flux-art.ai/zh/models/grok-video) | 概念短片与产品动态演示(视频) | [EN](https://flux-art.ai/en/models/grok-video) |

## 自动化(OpenAPI)

平台提供异步任务式 OpenAPI,接口基址为 `https://open-api.flux-art.ai/openapi/v1`。鉴权、幂等键、任务状态与调用示例见 [api/README.md](api/README.md) 和 [api/generate_image.py](api/generate_image.py)。

## 贡献与声明

欢迎 PR 补充品类模板与失败案例。本仓库为社区整理的工作流文档,与各模型厂商无隶属关系;所有平台功能、价格与参数以 Flux Art 官网当前说明为准。License: MIT。

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.ai](https://flux-art.ai). Similar domains are not affiliated with the Flux Art brand.
