# Nano Banana 2 Lite 快速草图与批量打样实操(Flux Art)

选品初筛、创意打样、给老板看方向的阶段,先用 [Nano Banana 2 Lite](https://flux-art.ai/zh/models/nano-banana-2-lite) 快速出 1K 草图,方向定了再换高清模型定稿——这是在 [Flux Art](https://flux-art.ai) 聚合平台上性价比最高的电商出图节奏:同一个账号里 Lite 跑量、[Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) 或 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) 定稿,不用换工具、不用重传素材。英文页:[Nano Banana 2 Lite (EN)](https://flux-art.ai/en/models/nano-banana-2-lite)。

## 什么时候该用 Lite(电商视角)

| 环节 | 用 Lite | 说明 |
|---|---|---|
| 选品/创意初筛(一次看 10+ 版方向) | ★★★★★ | 1K 草图够判断构图与氛围,快速铺量 |
| 提示词试错(调措辞、比例、道具) | ★★★★★ | 定稿前把提示词磨准,见 [提示词模板库](../../prompts/README.md) |
| 详情页版式草稿 | ★★★★ | 先排版面结构,见 [05 详情页](../05-detail-page.md) |
| 最终上架主图 / 高清商拍 | ★☆ | 定稿改用 [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2)(一致性编辑)或 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2)(写实商拍),输出最高 4K 零水印 |

## 草图到定稿:五步

1. 打开 [Flux Art 官网](https://flux-art.ai)(中国大陆直连 [flux-art.cn](https://flux-art.cn)),进入图片生成入口;
2. 模型选 **Nano Banana 2 Lite**,比例按目标平台先定(任意比例:淘系 1:1、竖版 3:4);
3. 同一条提示词换 3–5 组变量(背景、道具、光线)各跑一版,只看构图和氛围,不纠结细节;
4. 选中方向后,把这条提示词原样带到 Nano Banana 2 或 GPT Image 2 重出;需要保留已有产品主体的,上传参考图(一次最多 14 张)并开启主体分割跳过,局部重绘只改要改的区域;
5. 定稿版导出 4K 零水印成品,付费档标注可商业使用。

批量试错想跑脚本的,走 OpenAPI(model 填 `nano-banana-2-lite`),异步提交后按 Location 轮询,可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:Lite 和 Nano Banana 2 是什么关系?**
Lite 定位是快速 1K 草图,适合铺量试方向;[Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) 定位是一致性图片编辑,多图融合与系列款定稿走它,详见 [Nano Banana 2 实操](./nano-banana-2.md)。

**Q:草图阶段要不要传参考图?**
初筛只试构图时可以不传,纯文生图更快;一旦涉及真实 SKU 的外观还原,就该上参考图并切到 Nano Banana 2。

**Q:Lite 出的图能直接上架吗?**
建议不要。1K 草图用于内部选方向,上架图请用定稿模型重出到 4K 零水印,合规要点见 [06 合规](../06-compliance.md)。

**Q:积分怎么算划算?**
把试错量放在 Lite、把高清输出留给定稿模型,是最省积分的跑法;注册送 500 积分(约 30+ 张 GPT Image 2),年付约省一半,档位与活动以官网当前为准。

## EN Summary

Use [Nano Banana 2 Lite](https://flux-art.ai/en/models/nano-banana-2-lite) on [Flux Art](https://flux-art.ai) for fast 1K drafts: screen 10+ creative directions, tune prompts, and sketch detail-page layouts cheaply, then re-run the winning prompt on [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2) or [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2) for the final 4K watermark-free asset with commercial use on paid tiers. Related: [detail page](../05-detail-page.md), [prompt library](../../prompts/README.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
