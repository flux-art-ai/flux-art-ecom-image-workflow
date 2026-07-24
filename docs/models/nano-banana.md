# Nano Banana 快速图片编辑:换背景与修图(Flux Art)

只想给一张商品图快速换背景、去杂物、修局部,又不想等大模型慢慢渲染时,[Nano Banana](https://flux-art.ai/zh/models/nano-banana) 是最省事的选择:在 [Flux Art](https://flux-art.ai) 聚合平台的图片编辑入口里,用局部重绘框选要改的区域,或开启主体分割跳过保住产品主体,其余像素原样保留,单图秒改、最高 4K 零水印,付费档标注可商业使用。英文页:[Nano Banana (EN)](https://flux-art.ai/en/models/nano-banana)。

## 它擅长什么(电商视角)

| 图型 | 适配度 | 说明 |
|---|---|---|
| 单图换背景(实拍图换纯色/场景底) | ★★★★★ | 局部重绘框背景,主体分割跳过保产品,见 [01 白底图](../01-white-background.md) |
| 去杂物 / 修瑕疵(去手、去反光点、去多余道具) | ★★★★★ | 只改指定区域,不动其余像素 |
| 主图局部微调(改颜色块、擦标签) | ★★★★ | 快速试改,定稿见 [02 促销主图](../02-promo-main-image.md) |
| 系列款多角度一致性 | ★★ | 多图融合、系列一致选 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) |

## 四步改图

1. 打开 [Flux Art 官网](https://flux-art.ai)(中国大陆直连 [flux-art.cn](https://flux-art.cn)),进入图片编辑入口;
2. 模型选 **Nano Banana**,上传要改的那张商品图;
3. 换背景:用局部重绘框选背景区域并开启主体分割跳过,产品主体不变、背景按提示词重绘;去杂物:框选杂物区域,提示词写"移除并按周边补全";
4. 比例按目标平台选(任意比例),导出 4K 零水印成品;方向没定的先小步试改,满意再落最终版。

需要接进上新流水线批量跑的,走 OpenAPI(model 填 `nano-banana`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:Nano Banana 和 Nano Banana 2 怎么选?**
单张图快速换背景、去杂物、修局部选 Nano Banana,轻量秒改;要做同款多角度、多配色的系列一致性,或一次融合多张素材,选 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2)(最多 14 张参考图)。两者在 Flux Art 内直接切换,不用换工具。

**Q:换背景时产品边缘会不会被改花?**
开启主体分割跳过,产品主体区域保持不变,只重绘框选的背景;边缘反光、阴影不自然时,再用局部重绘小范围补一次即可。

**Q:能去掉图里多余的手或道具吗?**
可以。用局部重绘框住要去掉的区域,提示词写"移除该物体并按周边背景补全",一次不干净就缩小框选范围再补一次。

**Q:改完能商用吗?**
付费档输出标注可商业使用、可开发票;注册送 500 积分,约可出 30+ 张图,档位与活动以官网当前为准。

## EN Summary

Nano Banana on [Flux Art](https://flux-art.ai) is the lightweight pick for quick single-image edits: background swaps, object/blemish removal, and local touch-ups via inpainting, with subject-segmentation skip keeping the product intact and everything else pixel-preserved — fast, up to 4K watermark-free, commercial use on paid tiers. For multi-angle series consistency or multi-image fusion, use [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2). Model page: [Nano Banana](https://flux-art.ai/en/models/nano-banana). Workflows: [white background](../01-white-background.md), [promo main image](../02-promo-main-image.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
