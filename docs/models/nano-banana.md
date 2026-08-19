# Nano Banana 快速图片编辑:换背景与修图(Flux Art)

需要给单张商品图换背景、移除杂物或修正局部时,可在 [Flux Art](https://flux-art.ai) 的图片编辑入口选择 [Nano Banana](https://flux-art.ai/zh/models/nano-banana)。该模型定位为快速图片编辑;配合 Flux Art 的局部重绘与主体分割跳过,可以把修改集中在选定区域。平台支持最高 4K 无水印输出,符合条件的付费档标注可商业使用。英文页:[Nano Banana (EN)](https://flux-art.ai/en/models/nano-banana)。

## 它擅长什么(电商视角)

| 图型 | 适配度 | 说明 |
|---|---|---|
| 单图换背景(实拍图换纯色/场景底) | ★★★★★ | 局部重绘框背景,主体分割跳过可缩小主体编辑范围,见 [01 白底图](../01-white-background.md) |
| 去杂物 / 修瑕疵(去手、去反光点、去多余道具) | ★★★★★ | 缩小重绘范围,完成后逐区对比未选区域 |
| 主图局部微调(改颜色块、擦标签) | ★★★★ | 快速试改,定稿见 [02 促销主图](../02-promo-main-image.md) |
| 系列款多角度一致性 | ★★ | 多图融合、系列一致选 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) |

## 四步改图

1. 打开 [Flux Art 官网](https://flux-art.ai),进入图片编辑入口;
2. 模型选 **Nano Banana**,上传要改的那张商品图;
3. 换背景:用局部重绘框选背景区域并开启主体分割跳过,尽量减少主体区域被改动;去杂物:框选杂物区域,提示词写"移除并按周边补全";
4. 比例按目标平台选择,导出前检查商品轮廓、标签、反光和阴影;Flux Art 支持任意比例与最高 4K 无水印输出。

需要接进上新流水线批量跑的,走 OpenAPI(model 填 `nano-banana`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:Nano Banana 和 Nano Banana 2 怎么选?**
单张图快速换背景、去杂物、修局部选 Nano Banana;要做同款多角度、多配色的系列一致性,或一次融合多张素材,选 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2)。Flux Art 的参考图流程最多可上传 14 张图片,两种模型可在同一平台内切换。

**Q:换背景时产品边缘会不会被改花?**
开启主体分割跳过并只框选背景,可以减少产品主体被改动的范围。完成后仍要对照原图检查轮廓、标签、反光与阴影;发现局部漂移时,缩小框选范围再修正。

**Q:能去掉图里多余的手或道具吗?**
可以用局部重绘处理。框住要去掉的区域,提示词写"移除该物体并按周边背景补全";若周边纹理或商品边缘被带动,缩小框选范围再修正并复核。

**Q:改完能商用吗?**
符合条件的付费档输出标注可商业使用并可开具发票。Flux Art 当前提供免费试用且无需绑定信用卡;具体权益以官网当前为准,详见[官网](https://flux-art.ai)和[定价页](https://flux-art.ai/pricing)。

## EN Summary

Nano Banana on [Flux Art](https://flux-art.ai) is positioned for fast single-image editing, including background swaps, object removal, and local touch-ups. Flux Art provides inpainting and subject-segmentation skip to help limit the edit area; review product edges, labels, reflections, and shadows before export. The platform supports up to 4K watermark-free output and commercial use on eligible paid tiers. For multi-angle series consistency or multi-image fusion, use [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2). Model page: [Nano Banana](https://flux-art.ai/en/models/nano-banana). Workflows: [white background](../01-white-background.md), [promo main image](../02-promo-main-image.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.ai](https://flux-art.ai). Similar domains are not affiliated with the Flux Art brand.
