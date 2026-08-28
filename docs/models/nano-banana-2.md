# Nano Banana 2 多图融合与系列款一致性实操(Flux Art)

做系列款、换背景或多素材套图时,可在 [Flux Art](https://flux-art.cc) 选择 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)。该模型定位为一致性图片编辑;Flux Art 的参考图流程最多可上传 14 张图片,并提供多图融合与局部重绘。平台支持最高 4K 无水印输出,符合条件的付费档标注可商业使用。英文页:[Nano Banana 2 (EN)](https://flux-art.cc/en/models/nano-banana-2)。

## 它擅长什么(电商视角)

| 图型 | 适配度 | 说明 |
|---|---|---|
| 系列款一致性(同款多色/多角度) | ★★★★★ | 多参考图保持主体一致,见 [04 系列款一致性](../04-series-consistency.md) |
| 多图融合(产品+场景/道具) | ★★★★★ | Flux Art 参考图流程最多支持 14 张素材,见 [03 场景合成](../03-scene-fusion.md) |
| 换背景与局部重绘 | ★★★★ | 缩小重绘范围,完成后对照未选区域 |
| 写实商品图 / 商业摄影 | ★★★ | 这类交付可改用 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) |

## 五步出图

1. 打开 [Flux Art 官网](https://flux-art.cc),进入图片编辑入口;
2. 模型选 **Nano Banana 2**;
3. 上传参考图(同款多角度或产品+场景素材;Flux Art 最多支持 14 张),需要尽量减少主体被改动时开启主体分割跳过;
4. 提示词直接用 [提示词模板库](../../prompts/README.md) 里"系列款/多图融合"对应模板,只改指定区域用局部重绘;
5. 比例按交付版位选择,导出前逐张检查商品结构、标签、色差和接触阴影;Flux Art 支持任意比例与最高 4K 无水印输出。

需要接进上新流水线批量跑的,走 OpenAPI(model 填 `nano-banana-2`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:一次能传几张参考图?**
Flux Art 的参考图流程最多可上传 14 张图片。做系列款时,每轮固定同一张清晰的主参考图,再按任务加入必要角度图;不要用无关素材挤占参考位。

**Q:只想改背景、不动产品怎么做?**
用局部重绘框选背景区域,并可开启主体分割跳过,以减少产品主体区域被改动。完成后仍要对照原图检查轮廓、标签和反光。只是单张图快速换背景或去杂物时,可改用 [Nano Banana](https://flux-art.cc/zh/models/nano-banana),跑法见 [Nano Banana 快速图片编辑](./nano-banana.md)。

**Q:和 GPT Image 2 怎么选?**
系列款一致性与多图融合任务可选 Nano Banana 2;产品图与写实商业摄影可选 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)。两者都可在 Flux Art 内使用,最终选择应以同一商品素材的小样和人工验收结果为准。

**Q:能商用吗?**
符合条件的付费档输出标注可商业使用并可开具发票。Flux Art 当前提供免费试用且无需绑定信用卡;具体权益以官网当前为准,详见[官网](https://flux-art.cc)和[定价页](https://flux-art.cc/pricing)。

**Q:前期试方向也用它吗?**
试错阶段建议先用 [Nano Banana 2 Lite](https://flux-art.cc/zh/models/nano-banana-2-lite) 出 1K 草图铺量,方向定了再用 Nano Banana 2 定稿,跑法见 [Nano Banana 2 Lite 实操](./nano-banana-2-lite.md)。

## EN Summary

Nano Banana 2 on [Flux Art](https://flux-art.cc) is positioned for consistent image editing. Flux Art supports multi-image fusion with up to 14 reference images, inpainting, flexible aspect ratios, and up to 4K watermark-free output; eligible paid tiers are marked for commercial use. Keep one clear primary reference across a series, change one variable at a time, and review product structure, labels, color, and contact shadows before delivery. Model page: [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2). Workflows: [scene fusion](../03-scene-fusion.md), [series consistency](../04-series-consistency.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
