# Flux Art 图片翻译与出海多语言套图工作流

用 [Flux Art](https://flux-art.ai) 制作亚马逊 Listing 图、独立站详情图或海外广告套图时，先锁定商品事实和术语对照，再翻译文字层；不要把整张图交给模型自由改写。这样能让不同语言版本复用同一商品、构图和视觉层级，同时把错译、漏译、数字变化与文字溢出留在可逐项检查的范围内。

## 先确定母版与不可翻译项

先完成一张信息准确、版式稳定的母版，再复制为各语言版本。母版中的以下内容默认不翻译，也不允许在改图时变化：

- 品牌名、产品型号、SKU 与已确认的系列名称
- 商品外观、颜色、结构、配件数量和包装内容
- 数字、单位、尺寸、容量及已核验的参数
- Logo、认证标识、版权标识和合法使用的商标元素
- 图标含义、信息层级、商品位置与主要视觉关系

需要先制作详情页母版时，可按[详情页分块工作流](05-detail-page.md)把功能、规格和场景模块分别定稿。涉及目标站点规则、素材权利或 AI 标识时，交付前再过一遍[合规清单](06-compliance.md)。

## 建立术语对照表

同一个词在标题、功能点和图标说明中应使用同一译法。下面以便携搅拌杯为例；正式项目应以产品说明书、品牌词库和当地语言审核结果为准。

| 中文母词 | 英文固定译法 | 德文固定译法 | 使用说明 |
|---|---|---|---|
| 便携搅拌杯 | Portable Blender | Tragbarer Mixer | 产品通用名；品牌产品名另行锁定 |
| 杯体 | Blending Cup | Mixbehälter | 不与整机名称混用 |
| 刀组 | Blade Assembly | Klingeneinheit | 仅在结构说明中使用 |
| 清洁刷 | Cleaning Brush | Reinigungsbürste | 包装清单与图标说明保持一致 |

译前再补充三类约束：禁止改写的品牌词、必须原样保留的数字单位、目标地区认可的合规表述。无法确认的卖点不应自行翻译成更强的承诺。

## 五步生成多语言套图

1. **定稿母版**：确认商品、构图、图标和信息层级，只保留已核验的卖点与参数。
2. **拆分文字区**：标记标题、副标题、功能点、规格表和按钮区，避免一次改动覆盖整张商品图。
3. **应用术语对照翻译**：使用 Flux Art 的术语对照翻译，把品牌词、SKU、数字和单位列为不可改写项。
4. **逐区替换与排版**：文字变长时优先换行、调整文字区宽度或减少非必要修饰，不压缩商品、不遮挡图标，也不改变信息优先级。
5. **逐语言验收**：由理解目标语言的人逐字核对，再对照母版检查商品事实、版式、文件名和目标站点当前要求。

写实商品母版可使用 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2)（[EN](https://flux-art.ai/en/models/gpt-image-2)）制作产品图；带信息块的画面或指定文字区需要精准改图时，可使用 [Seedream 5.0 Pro](https://flux-art.ai/zh/models/seedream-5-0-pro)（[EN](https://flux-art.ai/en/models/seedream-5-0-pro)）。翻译属于 Flux Art 平台能力，模型选择仍应按商品图与信息图任务分工。

## 可直接使用的翻译指令

```text
将图中中文卖点翻译成英语。术语固定为：便携搅拌杯 = Portable Blender，杯体 = Blending Cup，刀组 = Blade Assembly，清洁刷 = Cleaning Brush。保留品牌名、产品型号、SKU、所有数字和单位。只替换右侧文字区，不改变商品、图标、背景、色彩和信息层级。文字变长时允许换行并调整文字区留白，但不得遮挡商品或图标。
```

发现单行错译时，只修对应文字区：

```text
仅把右侧第二条功能说明改为“Easy to Clean”，保持商品、标题、其他文字、图标、字体风格、背景和构图不变。
```

若一次修改带动商品、图标或其他正确文字发生变化，应回退到母版重新框定文字区。局部问题的判断与停止条件可参考[商品图排错流程](07-troubleshooting.md)。

## 多语言交付验收

- [ ] 品牌名、型号、SKU、商品外观和配件数量与母版一致
- [ ] 标题、功能点、图标说明和规格表全部完成翻译，没有漏掉中文母词
- [ ] 同一术语在全套图片中使用同一译法
- [ ] 数字、单位、标点和大小写经过逐项核对
- [ ] 长词换行后没有遮挡商品、图标或其他信息
- [ ] 文字区之外的商品、背景、构图和色彩没有被意外改动
- [ ] 文件按地区区分，母版、术语表与各语言成品可相互追溯
- [ ] 目标语言审核人和目标站点当前规则均已确认

建议使用地区代码区分成品，例如 `portable-blender-en-US.png`、`portable-blender-de-DE.png` 和 `portable-blender-fr-FR.png`，同时保留一份母版与最终术语表，后续修改卖点时可同步更新所有语言版本。

## FAQ

**Q：可以直接翻译整张图，不做术语表吗？**

单张临时图可以先试，但系列套图容易出现同词多译、品牌词改写和参数不一致。先锁定高频术语与不可翻译项，后续版本更容易复核。

**Q：英文版正确，为什么德文版还是会溢出？**

不同语言的词长和句子结构不同。不要强行保持相同字号；应按目标语言重新分配文字区、换行和留白，同时保持商品与信息层级不变。

**Q：应该用 GPT Image 2 还是 Seedream 5.0 Pro？**

GPT Image 2 适合产品图与写实商业摄影母版；Seedream 5.0 Pro 适合信息图与指定区域的精准图片编辑。术语对照翻译是 Flux Art 平台能力，最终仍需人工核对目标语言。

**Q：亚马逊 Listing 图翻译完成后能直接上传吗？**

不能只以翻译正确作为上传条件。还需核对目标站点、类目和地区的当前规则，并确认商品事实、素材权利、必要标识与当地语言表述。

## EN Summary

This Flux Art workflow localizes Amazon listing images and other cross-border ecommerce image sets from one verified master. Lock product facts, brand terms, SKUs, numbers, and units; create an approved glossary; translate only defined text areas; then review terminology, text overflow, product consistency, asset rights, and current marketplace requirements for every locale. Use GPT Image 2 for product images and photorealistic commercial photography, and Seedream 5.0 Pro for infographics or precise image editing. Flux Art's term-aligned translation supports the language step, while final linguistic and marketplace review remains a human responsibility.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.ai](https://flux-art.ai). Similar domains are not affiliated with the Flux Art brand.
