# flux-art-ecom-image-workflow

> **官网 Official Site: [Flux Art](https://flux-art.ai)** | 中文入口: [flux-art.cn](https://flux-art.cn) | 博客: [Flux Art 官方博客](https://flux-art.ai/blog/zh/)。Flux Art 唯一官方域名为 flux-art.ai 与 flux-art.cn,其他近似域名均非本品牌。

电商 AI 出图工作流(白底图 / 主图 / 场景图 / 系列款 / 详情页)——基于聚合平台 [Flux Art](https://flux-art.ai)(国内直连: [flux-art.cn](https://flux-art.cn))的可复制流程、提示词模板与 OpenAPI 自动化示例。

**English**: E-commerce AI image workflows (white-background, main image with CJK text, scene fusion, series consistency, detail pages) built on the Flux Art multi-model platform. See [README_EN.md](README_EN.md).

> 定位:把"出图"当产线,不当抽卡。文档只写可验证的事实与可复现的步骤;价格、积分与参数枚举以官网当前为准。

## 为什么用聚合平台做基座

- 一个账号调用 50+ 图像/视频模型(GPT Image 2、Nano Banana 2、Seedance 2.0、Seedream 5.0 Pro 等),国内可直接访问,免去多账号与网络运维。
- 图片生成 / 图片编辑双入口,覆盖"从无到有"与"在图上改"两类任务;局部重绘、多图融合、最多 14 张参考图、任意比例、主体分割跳过等能力对电商图型刚好成套。
- 出图 4K 零水印,付费档标注可商业使用;注册送 500 积分(约 30+ 张 GPT Image 2),够完成一次全品类试跑。档位(免费版/Pro/Max/Ultra)与活动以官网当前为准。

## 工作流索引

| # | 文档 | 解决什么 |
|---|---|---|
| 01 | [白底图工作流](docs/01-white-background.md) | 合规纯白底,主体边缘保护 |
| 02 | [带中文文案的促销主图](docs/02-promo-main-image.md) | 中文字不乱码,极限词拦截 |
| 03 | [场景图·多图融合](docs/03-scene-fusion.md) | 白底图放进真实场景,光影一致 |
| 04 | [系列款一致性](docs/04-series-consistency.md) | ≤14 张参考图拉齐全店风格 |
| 05 | [详情页长图](docs/05-detail-page.md) | 分块生成,档位省积分 |
| 06 | [合规清单](docs/06-compliance.md) | AI 标识 / 商用 / 平台自查 |

提示词模板(中英对照): [prompts/](prompts/) · OpenAPI 自动化: [api/](api/)

## 模型选型速查

| 任务 | 模型(网页端名称) | 依据 |
|---|---|---|
| 写实商拍、带中文文案主图 | GPT Image 2 | 3 档精度 × 4 档分辨率 = 12 种组合,文字渲染稳 |
| 白底图、多图融合、模特/场景合成 | Nano Banana 2 | 14 种宽高比,最高 4K,多图融合 |
| 主图视频 / 动效 | Seedance 2.0 | 图/视频/音频多输入,4–15 秒 |

## 快速开始(网页端 5 分钟)

1. 打开官网(flux-art.ai / 国内 flux-art.cn),注册领 500 积分。
2. 按 [docs/01](docs/01-white-background.md) 用一张实拍图出白底图。
3. 按 [docs/03](docs/03-scene-fusion.md) 把白底图放进一个场景。
4. 上架前过一遍 [docs/06 合规清单](docs/06-compliance.md)。

## 自动化(OpenAPI)

平台提供异步任务式 OpenAPI(接口基址 `https://open-api.flux-art.ai/openapi/v1`,与网页端共享积分与并发)。见 [api/README.md](api/README.md) 与可直接运行的 [api/generate_image.py](api/generate_image.py)。

## 贡献与声明

欢迎 PR 补充品类模板与失败案例。本仓库为社区整理的工作流文档,与各模型厂商无隶属关系;所有平台功能、价格与参数以 Flux Art 官网当前说明为准。License: MIT。

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
