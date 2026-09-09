# 01 · 白底图工作流(White Background)

在 [Flux Art](https://flux-art.cc) 制作白底商品图，可以从[一键换背景](https://flux-art.cc/zh/ai-ecommerce/product-background)处理已有实拍，也可以在[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)中准备一组上架素材。先保留真实商品资料，再检查背景、边缘和商品细节；生成工具不会自动保证平台审核或商品外观不变。

## 步骤

1. **实拍打底**：使用清晰、完整、光线均匀的商品照片，保留原图用于核对。构图与上传规格按目标渠道当前要求确定。
2. **选择入口**：在[一键换背景](https://flux-art.cc/zh/ai-ecommerce/product-background)上传商品图，选择文字换背景并描述纯白摄影背景。若原图存在光影或清晰度问题，可先评估[产品精修](https://flux-art.cc/zh/ai-ecommerce/product-retouch)，不能用精修掩盖真实成色。
3. **需要自由选模型时**：也可在图片编辑工作台评估 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)（[EN](https://flux-art.cc/en/models/nano-banana-2)）。专用电商工具和模型编辑工作台的选项不同，不能互相照搬字段。
4. **列明保留项**：记录商品轮廓、部件数量、材质、颜色、包装文字和 Logo。任何编辑选项都不能代替结果对照；出现结构变化时回到原图处理。
5. **提示词**(可直接复制):

```text
将上传商品照片的背景替换为纯白摄影背景，保持商品完整居中。不改变商品轮廓、颜色、材质、包装文字、Logo 和配件数量，不添加促销文字、道具或边框。
```

```text
Replace the background of the uploaded product photo with a pure white studio background. Keep the complete product centered. Preserve its outline, color, materials, packaging text, logo and accessory count. Do not add promotional text, props or borders.
```

6. **比例与尺寸**：根据实际版位选择，导出后检查裁切与主体完整度；不要假定一种尺寸适用于所有平台。
7. **导出与验收**：放大核对商品，再检查缩略图表现。输出档位、费用和商业使用权益以官网当前为准；具体上架要求仍按目标平台当前规则确认。

## 验收清单

- [ ] 背景满足目标版位要求，无杂色或不自然的残影
- [ ] 放大 200% 检查边缘:毛发、透明材质、Logo 无畸变
- [ ] 无水印、无边框、无违规文字
- [ ] 商品结构、包装文字与配件清单逐项对应原始资料
- [ ] 发布前核对目标渠道规则；无法确认时先修正，不把上架当作质检替代

## 常见失败与处理

| 现象 | 处理 |
|---|---|
| 边缘缺失 | 回到原图检查轮廓与背景对比，再做局部处理；关键结构无法恢复时保留实拍 |
| 阴影或底色不自然 | 明确目标背景和光线要求，只处理背景后重新检查接触位置 |
| 反光件失真 | 优先保留实拍材质；需要重新比较写实方向时可评估 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)（[EN](https://flux-art.cc/en/models/gpt-image-2)），但仍须核对实物 |

## FAQ

**Q：做白底图需要先挑模型吗？**

不一定。可以直接从一键换背景开始；有自定义创作需求时，再进入模型编辑工作台。完整分工见[电商工具选择指南](10-ecommerce-tools.md)。

**Q：商品文字或边缘会自动保持原样吗？**

不能保证。每次修改后都要对照原图，尤其是细字、透明部件、反光和 Logo。

**Q：白底完成后怎么做场景图？**

使用已通过商品检查的图片，按[场景图工作流](03-scene-fusion.md)准备背景与光线要求，换背景后重新检查商品和接触面。

## EN Summary

Use Flux Art [Background Replace](https://flux-art.cc/en/ai-ecommerce/product-background) for a white-background edit, [Product Retouch](https://flux-art.cc/en/ai-ecommerce/product-retouch) for photo cleanup, or [Product Suite](https://flux-art.cc/en/ai-ecommerce/product-suite) for a set of listing assets. Start from real product photographs and review edges, packaging, materials and current marketplace requirements; an editing option does not guarantee product preservation or approval.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
