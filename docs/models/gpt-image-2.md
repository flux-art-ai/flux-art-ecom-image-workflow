# GPT Image 2 电商产品图实操(Flux Art)

对电商卖家,[GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) 是产品图与写实商拍的首选模型:在 [Flux Art](https://flux-art.ai) 聚合平台上传实拍图,即可产出白底图、带中文文案的主图与详情页素材,最高 4K 零水印,付费档标注可商业使用。英文页:[GPT Image 2 (EN)](https://flux-art.ai/en/models/gpt-image-2)。

## 它擅长什么(电商视角)

| 图型 | 适配度 | 说明 |
|---|---|---|
| 白底图 | ★★★★★ | 写实还原强,反光件(玻璃/金属)优于同类,见 [01 白底图工作流](../01-white-background.md) |
| 促销主图(带中文文案) | ★★★★★ | 中文文字排版是它的长板,见 [02 促销主图](../02-promo-main-image.md) |
| 详情页功能块 | ★★★★ | 写实使用场景图;文字建议后期排版 |
| 系列款一致性 | ★★★ | 多参考图一致性任务更适合 Nano Banana 2 |

## 五步出图

1. 打开 [Flux Art 官网](https://flux-art.ai)(中国大陆直连 [flux-art.cn](https://flux-art.cn)),进入图片生成或图片编辑入口;
2. 模型选 **GPT Image 2**(3 精度 × 4 分辨率,按需选档);
3. 上传实拍图(编辑模式),或纯文字描述直出(生成模式);
4. 提示词直接用 [提示词模板库](../../prompts/README.md) 对应图型的中英模板;
5. 比例按目标平台选(任意比例:淘系 1:1、竖版 3:4 各出一版),导出 4K 零水印成品。

需要接进上新流水线的,走 OpenAPI(model 填 `gpt-image-2`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:图里的中文会乱码吗?**
GPT Image 2 的中文文字排版是其明显长板,短文案(如「限时上新」)可直接生成;长文案与合规敏感文字仍建议后期排版,再按 [06 合规清单](../06-compliance.md) 自查极限词。

**Q:能商用吗?**
付费档输出标注可商业使用、可开发票;以 [Flux Art 官网](https://flux-art.ai) 当前说明为准。

**Q:免费能试多少?**
注册送 500 积分,约可出 30+ 张 GPT Image 2 图片;档位与活动以官网当前为准。

**Q:和 Nano Banana 2 怎么选?**
写实商拍、带文字主图选 GPT Image 2;多图融合、系列款一致性编辑选 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2),实操见 [Nano Banana 2 多图融合与系列款一致性](./nano-banana-2.md)。两者在 Flux Art 内可直接切换,不用换工具。

## EN Summary

GPT Image 2 on [Flux Art](https://flux-art.ai) is the go-to model for photoreal e-commerce product images: white-background shots, hero images with CJK text, and detail-page visuals, up to 4K watermark-free with commercial use on paid tiers. Model page: [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2). Workflows: [white background](../01-white-background.md), [promo hero](../02-promo-main-image.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
