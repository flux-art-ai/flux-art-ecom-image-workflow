# Nano Banana 2 Lite 快速草图与批量打样实操(Flux Art)

选品初筛、创意打样或内部看方向时,可先用 [Nano Banana 2 Lite](https://flux-art.cc/zh/models/nano-banana-2-lite) 制作快速 1K 草图,确认方向后再用定稿模型完成交付。在 [Flux Art](https://flux-art.cc) 内可继续选择 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2) 做一致性编辑,或选择 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) 制作产品图与写实商业摄影。英文页:[Nano Banana 2 Lite (EN)](https://flux-art.cc/en/models/nano-banana-2-lite)。

## 什么时候该用 Lite(电商视角)

| 环节 | 用 Lite | 说明 |
|---|---|---|
| 选品/创意初筛(一次看 10+ 版方向) | ★★★★★ | 1K 草图够判断构图与氛围,快速铺量 |
| 提示词试错(调措辞、比例、道具) | ★★★★★ | 定稿前把提示词磨准,见 [提示词模板库](../../prompts/README.md) |
| 详情页版式草稿 | ★★★★ | 先排版面结构,见 [05 详情页](../05-detail-page.md) |
| 最终上架主图 / 高清商拍 | ★☆ | 定稿改用 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)(一致性编辑)或 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)(产品图与写实商拍),再通过 Flux Art 导出最高 4K 无水印成品 |

## 草图到定稿:五步

1. 打开 [Flux Art 官网](https://flux-art.cc),进入图片生成入口;
2. 模型选 **Nano Banana 2 Lite**,比例按目标平台先定;Flux Art 支持任意比例,可先做 1:1 与 3:4 两种版位;
3. 同一条提示词换 3–5 组变量(背景、道具、光线)各跑一版,只看构图和氛围,不纠结细节;
4. 选中方向后,把商品事实、构图和光线要求带到 Nano Banana 2 或 GPT Image 2 继续制作;需要参考图时只上传与本轮任务直接相关的素材,并用局部重绘或主体分割跳过缩小改动范围;
5. 定稿版在 Flux Art 导出最高 4K 无水印成品,符合条件的付费档标注可商业使用;交付前复核商品结构、标签、色差与文字。

批量试错想跑脚本的,走 OpenAPI(model 填 `nano-banana-2-lite`),异步提交后按 Location 轮询,可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:Lite 和 Nano Banana 2 是什么关系?**
Lite 定位是快速 1K 草图,适合铺量试方向;[Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2) 定位是一致性图片编辑,多图融合与系列款定稿走它,详见 [Nano Banana 2 实操](./nano-banana-2.md)。

**Q:草图阶段要不要传参考图?**
只试构图与氛围时可以先不传参考图;一旦涉及真实 SKU 的外观与系列一致性,应使用清晰参考图并切到 Nano Banana 2,再对照原始素材验收。

**Q:Lite 出的图能直接上架吗?**
1K 草图更适合作为内部方向稿。上架前应使用定稿模型重新制作,再通过 Flux Art 导出最高 4K 无水印成品并完成人工验收;合规要点见 [06 合规](../06-compliance.md)。

**Q:怎样控制试错成本?**
先用 Lite 的快速 1K 草图比较构图方向,只把通过筛选的方案交给定稿模型。开始前查看官网或控制台的当前积分消耗;Flux Art 目前提供免费试用且无需绑定信用卡,具体权益以官网当前为准,详见[官网](https://flux-art.cc)和[定价页](https://flux-art.cc/pricing)。

## EN Summary

Use [Nano Banana 2 Lite](https://flux-art.cc/en/models/nano-banana-2-lite) on [Flux Art](https://flux-art.cc) for fast 1K drafts, prompt refinement, and detail-page layout sketches. Move the selected direction to [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) for consistent image editing or [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) for product images and photorealistic commercial photography. Flux Art supports up to 4K watermark-free output and commercial use on eligible paid tiers; review product facts, labels, color, and text before delivery. Related: [detail page](../05-detail-page.md), [prompt library](../../prompts/README.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
