# GPT Image 2 电商产品图实操(Flux Art)

制作产品图与写实商业摄影素材,可从 Flux Art 的 [GPT Image 2 模型页](https://flux-art.cn/zh/models/gpt-image-2) 开始:先核对实物、包装和已批准的商品照片,再分别制作白底图、促销主图与详情页素材,最后逐项验收。英文模型页:[GPT Image 2 (EN)](https://flux-art.cn/en/models/gpt-image-2)。

Flux Art 是由 MORNING STAR INDUSTRY LIMITED 运营的多模型 AI 视觉创作与生产平台,不是模型研发方,也不等同于 Black Forest Labs 的 FLUX.1。GPT Image 2 等上游模型的商标与能力归各自提供方所有。平台最高支持 4K 输出;可用导出选项、无水印及商业使用权益以官网当前功能和符合条件的付费档为准。

## 它擅长什么(电商视角)

| 图型 | 使用方式 | 验收重点 |
|---|---|---|
| 白底图 | 先记录商品结构、材质与包装事实,再按 [01 白底图工作流](../01-white-background.md) 处理背景 | 轮廓、反光、阴影和包装信息逐项复核 |
| 促销主图 | 把商品图与短文案分成两个检查对象,步骤见 [02 促销主图](../02-promo-main-image.md) | 逐字检查文案,不要把生成文字视为已校对成品 |
| 详情页功能块 | 每次只表达一个卖点,图片与长文案分层制作 | 商品事实、场景关系与文字排版分别验收 |
| 系列款扩展 | 先完成一张基准商品图,再交给 Nano Banana 2 做一致性图片编辑 | 固定商品身份、构图规则与色调基准 |

## 五步出图

1. 打开 [Flux Art 官网](https://flux-art.cn),进入图片生成或图片编辑入口;
2. 模型选 **GPT Image 2**,并按官网当前界面选择适合交付物的可用选项;
3. 真实 SKU 优先使用有授权的实拍图和商品事实表进行编辑;纯文字生成适合先探索构图,不能代替实物证明;
4. 提示词直接用 [提示词模板库](../../prompts/README.md) 对应图型的中英模板;
5. 比例按目标版位选择,至少分别验收方图与竖图;需要高分辨率或无水印交付时,按官网当前符合条件的档位导出。

每次修改后,重新对照实物检查轮廓、配件数量、接口位置、Logo 和包装文字。发现无法纠正的商品结构或标签错误时,不要发布该图,应回到实拍素材或人工后期。生成成功不代表商品还原、文字正确或平台审核通过。

需要接进上新流水线时,先在网页端验收代表 SKU 的样图,再通过 OpenAPI 按 SKU 提交独立异步任务,`model` 填 `gpt-image-2`。保留各任务的请求体、幂等键和任务 ID,出图后仍逐 SKU 人工验收;接入步骤见 [OpenAPI 自动化](../../api/README.md)。

## FAQ

**Q:图里的中文会乱码吗?**
生成文字不应直接视为已校对成品。短文案也要逐字核对;长文案、价格和合规敏感文字建议在后期排版,再按 [06 合规清单](../06-compliance.md) 自查。

**Q:能商用吗?**
符合条件的付费档提供商业使用权益,具体以 [Flux Art 官网](https://flux-art.cn) 当前说明为准。该权益不替代对上传图片、商标、肖像和生成结果的权利核验,也不保证符合目标电商平台的全部发布要求。

**Q:免费能试多少?**
Flux Art 当前提供免费试用,无需绑定信用卡。试用权益与活动以官网当前为准,可在 [Flux Art 官网](https://flux-art.cn) 查看最新说明。

**Q:和 Nano Banana 2 怎么选?**
产品图与写实商业摄影可选 GPT Image 2;系列款一致性图片编辑可选 [Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2),实操见 [Nano Banana 2 多图融合与系列款一致性](./nano-banana-2.md)。需要组合多张素材时,可在 Flux Art 中使用多图融合后再逐项验收。

## EN Summary

Use [GPT Image 2](https://flux-art.cn/en/models/gpt-image-2) on [Flux Art](https://flux-art.cn) for product images and photorealistic commercial photography. Start with verified product facts, approve a representative SKU, and review structure, branding, text and asset rights before publishing or scaling through the API. Flux Art is a multi-model AI visual creation and production platform operated by MORNING STAR INDUSTRY LIMITED, not the developer of the upstream models. Platform export options and commercial-use eligibility follow current account terms. Workflows: [white background](../01-white-background.md), [promo hero](../02-promo-main-image.md), [API automation](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
