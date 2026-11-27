# 01 · 白底图工作流(White Background)

透明 PNG 上传后变黑时，先用两种底色检查实际上传件，再与页面正在展示的文件对比；确认透明度最早在哪一步丢失，才决定重导还是排查页面。在 [Flux Art](https://flux-art.cn) 制作白底商品图，可以从[一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background)处理已有实拍，也可以在[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)中准备一组上架素材。先保留真实商品资料，再检查背景、边缘和商品细节；生成工具不会自动保证平台审核或商品外观不变。

## 步骤

1. **实拍打底**：使用清晰、完整、光线均匀的商品照片，保留原图用于核对。构图与上传规格按目标渠道当前要求确定。
2. **选择入口**：在[一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background)上传商品图，选择文字换背景并描述纯白摄影背景。若原图存在光影或清晰度问题，可先评估[产品精修](https://flux-art.cn/zh/ai-ecommerce/product-retouch)，不能用精修掩盖真实成色。
3. **需要自由选模型时**：也可在图片编辑工作台评估 [Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)（[EN](https://flux-art.cn/en/models/nano-banana-2)）。专用电商工具和模型编辑工作台的选项不同，不能互相照搬字段。
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
| 反光件失真 | 优先保留实拍材质；需要重新比较写实方向时可评估 [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)（[EN](https://flux-art.cn/en/models/gpt-image-2)），但仍须核对实物 |

## 白色商品放到白底上，轮廓消失怎么排查？

以白色马克杯为例，把原片、透明中间图（如果有）和最终白底图按同一倍率并排打开。优先找三个容易丢失的位置：杯口薄边、杯把内孔、杯底与台面的交界。找到哪一步先丢边，再决定返工位置。

| 边缘最先在哪一步消失 | 怎样确认 | 本次只处理什么 |
|---|---|---|
| 实拍原片中已看不清 | 调整查看亮度后，仍无法辨认杯口与背景的分界 | 用能分清轮廓的背景或光线补拍；不让生成工具补猜商品边缘 |
| 原片清楚，透明中间图缺一块 | 将透明图临时叠在深灰底上，杯口仍断开，或本应透出背景的杯把内孔被填满 | 回原片重做提取或手工修蒙版；深灰底仅供检查，不跟着交付 |
| 中间图完整，白底成品才看不清 | 导出前能分清边缘，导出后的实际文件里却与背景融在一起 | 保留商品的真实明暗和纹理，检查合成、导出与终端预览；不要给杯身硬描边 |

如果是直接换背景、没有透明中间图，就比对原片、工作台结果和导出文件，不必为了排查另跑一次抠图。确认最终白底文件在目标展示尺寸下仍能辨认杯把和开口，再上架；背景颜色与是否保留自然阴影，按目标版位的当前要求确认。

## 透明 PNG 上传后变黑怎么排查？

以带内孔的杯把为例。用能显示透明度的编辑器，把透明母版、**实际上传的文件**与能取到的页面图片分别叠在白底和蓝灰底上。重点看杯把内孔与商品外的空白，不凭相册预览的底色下结论。

| 文件对比的结果 | 判断 | 下一步 |
|---|---|---|
| 上传件透明；页面图片也能随底色变化，但在店铺预览中呈黑色 | 图片仍保留透明，先查这个版位的背景或查看器显示 | 对照手机和桌面实际页面；若该版位必须显示固定白底，合成并导出一份白底交付件 |
| 母版透明；实际上传件在两种底色上始终是同一个黑矩形 | 导出或传递环节已把黑底合进文件 | 回母版重新导出保留透明的 PNG，不用截图替代源文件，也不要只把扩展名改成 PNG |
| 实际上传件透明；页面正在使用的可下载文件变成固定黑底 | 客户端收到的版本与上传件不同，具体由哪一步转换仍需确认 | 记录版位和两份文件，交给渠道或页面维护方排查，不先重做商品图 |

如果母版本来就没有透明区域，且必须交透明图，从清楚的原片用[智能抠图](https://flux-art.cn/zh/ai-tools/remove-background) / [Background Remover](https://flux-art.cn/en/ai-tools/remove-background)重新提取主体，再检查杯把内孔和边缘。若渠道只收固定底色，保留透明母版，按该渠道当前规则另导一份成品。

## FAQ

**Q：做白底图需要先挑模型吗？**

不一定。可以直接从一键换背景开始；有自定义创作需求时，再进入模型编辑工作台。完整分工见[电商工具选择指南](10-ecommerce-tools.md)。

**Q：商品文字或边缘会自动保持原样吗？**

不能保证。每次修改后都要对照原图，尤其是细字、透明部件、反光和 Logo。

**Q：白底完成后怎么做场景图？**

使用已通过商品检查的图片，按[场景图工作流](03-scene-fusion.md)准备背景与光线要求，换背景后重新检查商品和接触面。

## EN Summary

Use Flux Art [Background Replace](https://flux-art.cn/en/ai-ecommerce/product-background) for a white-background edit, [Product Retouch](https://flux-art.cn/en/ai-ecommerce/product-retouch) for photo cleanup, or [Product Suite](https://flux-art.cn/en/ai-ecommerce/product-suite) for a set of listing assets. Start from real product photographs and review edges, packaging, materials and current marketplace requirements; an editing option does not guarantee product preservation or approval.

When a white product loses its outline, locate the first bad version: source photo, transparent cutout (if used), or white export. A temporary dark background helps reveal missing cutout pixels and filled holes. Review the actual exported file at its intended display size before listing.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
