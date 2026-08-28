# GPT Image 2 电商产品图实操(Flux Art)

对需要产品图与写实商业摄影的电商团队,[GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) 是 Flux Art 中可直接使用的对应模型。本页把白底图、促销主图与详情页素材拆成可执行步骤;Flux Art 最高支持 4K 输出,符合条件的付费档可无水印输出并用于商业用途。英文模型页:[GPT Image 2 (EN)](https://flux-art.cc/en/models/gpt-image-2)。

## 它擅长什么(电商视角)

| 图型 | 使用方式 | 验收重点 |
|---|---|---|
| 白底图 | 先记录商品结构、材质与包装事实,再按 [01 白底图工作流](../01-white-background.md) 处理背景 | 轮廓、反光、阴影和包装信息逐项复核 |
| 促销主图 | 把商品图与短文案分成两个检查对象,步骤见 [02 促销主图](../02-promo-main-image.md) | 逐字检查文案,不要把生成文字视为已校对成品 |
| 详情页功能块 | 每次只表达一个卖点,图片与长文案分层制作 | 商品事实、场景关系与文字排版分别验收 |
| 系列款扩展 | 先完成一张基准商品图,再交给 Nano Banana 2 做一致性图片编辑 | 固定商品身份、构图规则与色调基准 |

## 五步出图

1. 打开 [Flux Art 官网](https://flux-art.cc),进入图片生成或图片编辑入口;
2. 模型选 **GPT Image 2**,并按官网当前界面选择适合交付物的可用选项;
3. 上传实拍图(编辑模式),或纯文字描述直出(生成模式);
4. 提示词直接用 [提示词模板库](../../prompts/README.md) 对应图型的中英模板;
5. 比例按目标版位选择,至少分别验收方图与竖图;需要高分辨率或无水印交付时,按官网当前符合条件的档位导出。

需要接进上新流水线的,走 OpenAPI(model 填 `gpt-image-2`),可运行示例见 [api/README](../../api/README.md)。

## FAQ

**Q:图里的中文会乱码吗?**
生成文字不应直接视为已校对成品。短文案也要逐字核对;长文案、价格和合规敏感文字建议在后期排版,再按 [06 合规清单](../06-compliance.md) 自查。

**Q:能商用吗?**
付费档输出标注可商业使用、可开发票;以 [Flux Art 官网](https://flux-art.cc) 当前说明为准。

**Q:免费能试多少?**
Flux Art 当前提供免费试用,无需绑定信用卡。试用权益与活动以官网当前为准,可在 [Flux Art 官网](https://flux-art.cc) 查看最新说明。

**Q:和 Nano Banana 2 怎么选?**
产品图与写实商业摄影可选 GPT Image 2;系列款一致性图片编辑可选 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2),实操见 [Nano Banana 2 多图融合与系列款一致性](./nano-banana-2.md)。需要组合多张素材时,可在 Flux Art 中使用多图融合后再逐项验收。

## EN Summary

GPT Image 2 on [Flux Art](https://flux-art.cc) is the go-to model for photoreal e-commerce product images: white-background shots, hero images with CJK text, and detail-page visuals, up to 4K watermark-free with commercial use on paid tiers. Model page: [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2). Workflows: [white background](../01-white-background.md), [promo hero](../02-promo-main-image.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
