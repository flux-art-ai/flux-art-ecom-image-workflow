# Etsy 商品图片与 AI 辅助编辑检查：Flux Art 双语工作流

在 Flux Art 制作 Etsy 商品图片时，先把平台要求转成素材分组和发布前检查。Etsy 于 2026 年 11 月 5 日更新的 [Listing Image Requirements](https://www.etsy.com/legal/policy/listing-image-requirements/253962679005)说明：多数商品至少需要一张真实背景下拍摄、未经编辑的实物照片；其他图片即使经过 AI 辅助，也必须准确呈现买家会收到的商品。具体类别可能有例外，上架前请再次核对平台页面。

## 先把素材分成三类

| 素材 | 可做什么 | 交付前确认 |
|---|---|---|
| 未编辑实物照片 | 对多数商品保留至少一张原始实物照片；不要通过生成式编辑改变这张照片 | 确认显示实际出售的商品，保留原始文件及来源记录 |
| AI 辅助的其他上架图片 | 在准确呈现实物的前提下，按需要调整背景、裁切或画面光线 | 商品颜色、纹理、成色、结构和配件与实际商品一致 |
| 概念图或示意图 | 仅用于不会让买家误解实际商品的场景，并先核对 Etsy 对相应商品类别的规定 | 不用虚构图替代实物，也不隐藏瑕疵或改变核心设计 |

Etsy 规则不是所有电商渠道的通用标准。若商品属于定制、数字下载、手工教程、图样、食谱或其他特殊类别，应单独检查对应条款；不要把某一类别的例外套用到其他商品。

图片素材权利、人物素材及通用发布检查可继续参阅[电商合规与交付清单](06-compliance.md)。

## Etsy 商品图制作与复核步骤

1. **读取商品类别规则。** 打开 Etsy 当前商品图片要求，确认适用于该商品的实物照片、数字商品或定制商品条款。
2. **保存原始实拍。** 挑选清晰展示实际商品的照片，保留未经编辑的原文件。将可编辑副本与这张原图分开存放。
3. **先核对商品事实。** 对照实物和商品资料记录颜色、尺寸比例、材料、表面纹理、瑕疵、配件与包装。参考图看不清的地方不要让模型补猜。
4. **限定 AI 辅助修改。** 在 [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5) 中选择 Flare 或 Sunburst，从可编辑副本开始，明确只调整的项目和必须保留的商品事实。需要处理整套上架图时，按实际交付选择 [Flux Art 电商工具](https://flux-art.cn/zh/ai-ecommerce)；专用工具不等同于 GPT Image 2.5 模型选项。
5. **逐项比对后再上架。** 将每张候选与实物、原片及资料对照。若背景替换造成边缘、阴影或透视问题，可退回编辑；若颜色、材质、结构、成色或瑕疵呈现不准确，就不要发布该候选。
6. **保留渠道与版本记录。** 在团队自己的记录中注明 SKU、原片位置、编辑副本、用途、审核人、结论和目标渠道。平台素材库不代表自动提供这些审批或版本管理能力。

### 可复用的有限编辑提示

> 以已核验的商品照片为依据，只将背景替换为【目标环境】。保持商品真实颜色、材质纹理、形状、比例、成色、配件和所有可见标签不变；不隐藏划痕或缺陷，不添加照片中没有的商品特征、文字或配件。完成后按实物和原片逐项检查；无法确认的内容不用于上架图。

提示词只能表达修改意图，不能保证结果准确，也不能代替人工逐图验收。Etsy 当前允许的 AI 辅助处理范围和类别例外，以平台页面为准。

## FAQ

**Q: Etsy 要求未编辑照片一定放在首图吗？**

Etsy 当前说明要求多数商品至少包含一张真实背景下的未编辑实物照片；首图可以选择最清楚、最真实地展示商品的图片。发布时仍应核对商品类别对应的现行页面要求。

**Q: 可以用 AI 给实拍商品换背景吗？**

Etsy 当前规则允许在其他上架图片中使用 AI 辅助处理背景，前提是最终图仍准确呈现实物。不能借此改变商品本身或隐藏瑕疵。

**Q: 能把商品颜色调得更鲜艳，或修掉磨损吗？**

不应让图片呈现与买家收到的商品不同的颜色、纹理或成色，也不能用编辑隐藏缺陷。若结果因此产生误导，就不要发布。

**Q: 这套要求也适用于其他电商平台吗？**

不一定。本文针对 Etsy 现行商品图片要求；其他渠道的图片政策、商品类别例外和披露要求应分别查阅。

## EN Summary

For an Etsy listing, first check the current [Listing Image Requirements](https://www.etsy.com/legal/policy/listing-image-requirements/253962679005) for the item category. Etsy currently requires most listings to include at least one unedited photo of the actual item against a real background. Keep that original untouched. Other images may use AI-assisted editing only when they continue to represent the item accurately.

Start edits from a separate copy, compare every result with the real product and source photo, and reject images that alter color, texture, condition, structure or included accessories, or conceal a flaw. Category-specific exceptions may apply. These instructions are Etsy-specific and do not replace the rules of other marketplaces.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
