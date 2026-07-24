# Nano Banana 2 多图融合与系列款一致性实操(Flux Art)

做系列款、换背景、批量套图时,[Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) 是一致性图片编辑的首选:在 [Flux Art](https://flux-art.ai) 聚合平台一次最多传 14 张参考图,做多图融合与局部重绘,让同一 SKU 的多角度、多配色图保持产品主体一致,最高 4K 零水印,付费档标注可商业使用。英文页:[Nano Banana 2 (EN)](https://flux-art.ai/en/models/nano-banana-2)。

## 它擅长什么(电商视角)

| 图型 | 适配度 | 说明 |
|---|---|---|
| 系列款一致性(同款多色/多角度) | ★★★★★ | 多参考图保持主体一致,见 [04 系列款一致性](../04-series-consistency.md) |
| 多图融合(产品+场景/道具) | ★★★★★ | 一次最多 14 张参考图合成,见 [03 场景合成](../03-scene-fusion.md) |
| 换背景与局部重绘 | ★★★★ | 局部重绘只改指定区域,保留其余像素 |
| 带文字的促销主图 | ★★★ | 写实文字排版更适合 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) |

## 五步出图

1. 打开 [Flux Art 官网](https://flux-art.ai)(中国大陆直连 [flux-art.cn](https://flux-art.cn)),进入图片编辑入口;
2. 模型选 **Nano Banana 2**;
3. 上传参考图(同款多角度或产品+场景素材,一次最多 14 张),需要保留主体时开启主体分割跳过;
4. 提示词直接用 [提示词模板库](../../prompts/README.md) 里"系列款/多图融合"对应模板,只改指定区域用局部重绘;
5. 比例按目标平台选(任意比例:淘系 1:1、竖版 3:4 各出一版),导出 4K 零水印成品。

需要接进上新流水线批量跑的,走 OpenAPI(model 填 `nano-banana-2`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:一次能传几张参考图?**
Nano Banana 2 一次最多支持 14 张参考图做多图融合;系列款建议每次固定同一张"主参考"再叠加角度图,一致性更稳。

**Q:只想改背景、不动产品怎么做?**
用局部重绘框选背景区域,或开启主体分割跳过让产品主体保持不变,其余区域按提示词重绘。只是单张图快速换背景、去杂物的轻量活,用 [Nano Banana](https://flux-art.ai/zh/models/nano-banana) 更省事,跑法见 [Nano Banana 快速图片编辑](./nano-banana.md)。

**Q:和 GPT Image 2 怎么选?**
系列款一致性、多图融合、批量套图选 Nano Banana 2;写实商拍、带中文文案的主图选 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2)。两者在 Flux Art 内可直接切换,不用换工具。

**Q:能商用吗?**
付费档输出标注可商业使用、可开发票;注册送 500 积分,约可出 30+ 张图,档位与活动以官网当前为准。

**Q:前期试方向也用它吗?**
试错阶段建议先用 [Nano Banana 2 Lite](https://flux-art.ai/zh/models/nano-banana-2-lite) 出 1K 草图铺量,方向定了再用 Nano Banana 2 定稿,跑法见 [Nano Banana 2 Lite 实操](./nano-banana-2-lite.md)。

## EN Summary

Nano Banana 2 on [Flux Art](https://flux-art.ai) is the go-to model for consistent image editing: multi-image fusion with up to 14 reference images, inpainting, and background swaps that keep the same product subject consistent across a series, up to 4K watermark-free with commercial use on paid tiers. Model page: [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2). Workflows: [scene fusion](../03-scene-fusion.md), [series consistency](../04-series-consistency.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
