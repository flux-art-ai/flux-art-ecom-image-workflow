# 02 · 带中文文案的促销主图(Promo Main Image with CJK Text)

需要制作带中文短文案的促销主图时，可以在 Flux Art 使用 [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2) 生成产品图、电商主图或海报方向；品牌名、价格、日期、参数和促销文字必须逐字人工校对，最终是否符合目标平台规则也要在发布前单独核验。英文模型页见 [GPT Image 2 (EN)](https://flux-art.cn/en/models/gpt-image-2)。

## 从电商专用工具开始

已有想参考的构图时，可进入[爆款图片复刻](https://flux-art.cn/zh/ai-ecommerce/reference-clone)，分别上传自己的商品图与有权使用的参考图。参考图用于布局和视觉风格，不是复制其他品牌 Logo、价格、认证或卖点的依据。

需要围绕同一商品制作多种用途的图片，可从[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)组织素材；底图有划痕、色偏或清晰度问题时，先用[产品精修](https://flux-art.cn/zh/ai-ecommerce/product-retouch)处理并对照实物复核。需要自选模型和逐轮调整提示词时，再使用下文的模型工作流。完整分流见[电商工具选择指南](10-ecommerce-tools.md)。

## 先把商品事实和画面文案拆开

开始生成前，先把不能由模型补写的事实固定下来。文案越短、层级越清楚，后续校对和局部修改越容易。

| 项目 | 写入方式 | 发布前检查 |
|---|---|---|
| 商品主体 | 写清品类、颜色、材质和必须保留的外观特征 | 对照原始商品图检查结构、标签和配件 |
| 主标题 | 使用引号写入已确认的短句 | 逐字核对品牌名、标点和字形 |
| 辅助文案 | 只保留一到两条已核实卖点 | 不让模型补充参数、认证或优惠条件 |
| 版式 | 指定标题区、商品区和留白位置 | 检查文字是否遮挡主体，移动端是否易读 |

## 五步完成促销主图

1. 打开 [GPT Image 2 中文模型页](https://flux-art.cn/zh/models/gpt-image-2)，进入 Flux Art 图片生成入口。
2. 整理商品事实、必须出现的原文、禁止改写项和目标比例；不要把未知参数交给模型补全。
3. 首轮只比较构图、商品位置、光线和文案层级，不把生成文字直接当作已校对成品。
4. 发现单个文字区或局部画面需要调整时，使用 Flux Art 的图片编辑与局部重绘处理选定区域；修改后复核边界及整张画面。
5. 交付前逐字检查文案，并按 [合规清单](06-compliance.md) 核对素材权利、AI 内容标识和目标平台当前规则；画面异常可参照 [商品图排错流程](07-troubleshooting.md)。

## 可直接使用的提示词

### 新品促销主图

```text
为一款黑色头戴式耳机制作 1:1 电商促销主图。商品居中，完整呈现耳罩、头梁和侧面标识，置于浅灰色磨砂台面。画面上方保留标题区，标题原文为“新品上市”，辅助文案原文为“轻盈随行”。使用明亮、简洁的商业摄影风格，不添加未提供的参数、认证、价格或品牌文字。交付前逐字核对画面文字并对照原始商品图检查外观。
```

### 只修改一处标题

```text
以上传图片为基础，只修改顶部标题区：把原标题替换为“新品上市”。商品位置、商品外观、背景、光线、阴影、辅助文案和其他元素保持当前构图。完成后检查修改区边缘，并逐字核对标题和整张画面的其他文字。
```

## 活动结束后的下线与常规图恢复

制作促销主图时，同时准备一份不含活动日期、限时价格和优惠条件的常规母版。促销版、常规版和渠道导出文件分别保存，文件名或资产表写清完整 SKU、活动名称、开始时间、结束时间、来源母版和负责人，避免活动到期后依靠记忆找图。

| 阶段 | 操作 | 验收证据 |
|---|---|---|
| 上线前 | 确认常规母版仍对应当前商品；登记促销版投放渠道、广告位和多语言版本 | 母版验收记录、渠道清单、计划起止时间 |
| 到期下线 | 按各渠道实际结束时间撤下促销版，恢复常规版或当前有效版本 | 后台选中版本与操作时间 |
| 衍生文件检查 | 复核裁切图、缩略图、详情模块、广告素材和翻译版本 | 每个衍生文件都能追溯到当前母版 |
| 前台确认 | 在目标页面和常用展示尺寸查看实际图片；若仍显示旧促销图，检查渠道缓存或发布状态 | 页面截图、复核人和完成时间 |
| 归档 | 保留活动文件和下线记录，但从当前交付目录、模板和自动化输入中移出 | 当前目录只包含仍可发布资产 |

恢复常规图不是把活动文案模糊掉。若底图仍可用，可在 [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)的图片编辑入口限定文字区域；若需要重建整套无促销版本，可从 [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)或[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)开始。无论使用哪个入口，都应对照真实商品资料验收，不能让模型推断当前价格、库存或活动状态。

## 文案与合规检查

“最”“第一”“顶级”“国家级”“全网最低”“绝对”等表述可能涉及广告与平台规则风险。不要让模型自行改写或扩展宣传语；使用已经确认的描述性文案，并以投放地区法律、目标平台当前规则和内部审核结论为准。

## 交付验收清单

- [ ] 商品颜色、结构、标签、Logo 和配件与原始素材一致
- [ ] 品牌名、标题、价格、日期、参数和标点已逐字校对
- [ ] 文案没有遮挡商品主体，缩略图和移动端仍可阅读
- [ ] 生成内容没有补入未经确认的卖点、认证或优惠条件
- [ ] 上传素材、字体、Logo 和人物肖像具备相应使用权限
- [ ] AI 内容标识及目标平台规则已单独核对

## FAQ

**Q：GPT Image 2 生成的中文文案可以直接发布吗？**

不建议。生成文字仍需逐字核对，尤其是品牌名、价格、日期、参数和受监管表述。模型输出不能代替人工审校。

**Q：只有一个字写错时怎么处理？**

在 Flux Art 图片编辑入口框选对应文字区，写清替换后的完整原文和必须保持的画面元素。修改后检查框选区边缘，并再次复核全图文字。

**Q：促销主图可以只靠模型完成审核吗？**

不可以。商品事实、素材权利、广告表述、AI 内容标识和目标平台规则都需要独立核验，生成结果只能作为制作素材。

**Q：在哪里查看 GPT Image 2 的官方入口？**

使用 [GPT Image 2 中文模型页](https://flux-art.cn/zh/models/gpt-image-2) 或 [GPT Image 2 英文模型页](https://flux-art.cn/en/models/gpt-image-2)，并从 [Flux Art 官网](https://flux-art.cn) 进入图片工作台；涉及模型可用性、价格和权益时，以官网当前为准。

## EN Summary

Use [GPT Image 2](https://flux-art.cn/en/models/gpt-image-2) on [Flux Art](https://flux-art.cn) to create product-image, ecommerce-hero, and poster directions with short in-image copy. Lock product facts before generation, keep the text hierarchy simple, proofread every name, price, date, parameter, and punctuation mark, and verify rights, AI labeling, and current marketplace rules before release. For related checks, see the [compliance checklist](06-compliance.md) and [troubleshooting guide](07-troubleshooting.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的唯一官网与全站 canonical 为 [flux-art.cn](https://flux-art.cn)。
> The only official Flux Art website and canonical domain is [flux-art.cn](https://flux-art.cn).
