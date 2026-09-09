# 05 · 详情页长图(Detail Page)

在 [Flux Art](https://flux-art.cc) 制作电商详情页长图时，先把商品事实和页面结构锁定，再按模块生成、校对和拼接，通常比一次生成整张长图更容易控制。产品图与写实商业摄影可使用 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)（[EN](https://flux-art.cc/en/models/gpt-image-2)）；需要参考图控制、海报排版或电商主视觉时可比较 [Seedream 4.5](https://flux-art.cc/zh/models/seedream-4-5)（[EN](https://flux-art.cc/en/models/seedream-4-5)）；高信息量视觉和精准图片编辑可使用 [Seedream 5.0 Pro](https://flux-art.cc/zh/models/seedream-5-0-pro)（[EN](https://flux-art.cc/en/models/seedream-5-0-pro)）。所有文字、金额、数字和商品细节仍需人工复核。

## 使用 A+ 详情页入口组织模块

希望直接按电商模块制作内容，可进入 [A+ 详情页](https://flux-art.cc/zh/ai-ecommerce/a-plus-content)，准备真实商品图片、商品名称、品类与已核实信息，再按页面当前提供的选项选择模块。需要同一商品的其他展示图片时，可配合[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)；原图需要清理时先用[产品精修](https://flux-art.cc/zh/ai-ecommerce/product-retouch)，不要通过修图增加实物没有的结构。

A+ 图片生成不代表平台审核通过，也不替代文案、参数和素材授权检查。专用工具与自选模型的分工见[电商工具选择指南](10-ecommerce-tools.md)。工具费用、积分与账户权益以官网当前为准。

## 先拆成交付模块

| 模块 | 需要锁定的内容 | 制作与验收重点 |
|---|---|---|
| 首屏主视觉 | 商品、核心卖点、画面比例、留白 | 商品结构、品牌元素、构图与阅读入口 |
| 场景与功能块 | 使用场景、动作、功能事实 | 接触面、比例、光线与真实产品一致 |
| 材质与细节块 | 材质、纹理、接口、配件 | 不补写未知结构，不把示意图当实拍证据 |
| 参数与对比块 | 已核实参数、单位、对比维度 | 逐字校对，不让模型推断缺失参数 |
| 售后与说明块 | 官方原文、适用范围、限制条件 | 保留原意，按当前平台规则和商品资料发布 |

先建立一张商品事实表，记录名称、SKU、颜色、材质、尺寸、包装清单、已核实卖点、禁止改写项和素材来源。任何无法从商品资料确认的内容都不进入提示词或成品。

## 三类图片任务怎么分流

- **产品图与写实场景**：使用 GPT Image 2 制作产品图或写实商业摄影模块；需要把商品放入具体环境时，可配合[场景图工作流](03-scene-fusion.md)检查透视、接触面和光线。
- **参考图控制与版式探索**：Seedream 4.5 的官方页面定位包含参考图控制、局部改图、海报排版和电商视觉。把产品外观、品牌配色、材质或构图分别指定给对应参考图，不要让多张素材承担相互冲突的角色。
- **信息图与精准修改**：Seedream 5.0 Pro 适合高信息量视觉、信息图和精准图片编辑。先定义信息层级，再按区域修改；具体做法见 [Seedream 5.0 Pro 信息图实操](models/seedream-5-0-pro.md)。

如果参数密集、法规文字较长或需要严格复用品牌字体，先生成无文字视觉底图，再在排版工具中加入已核实文案。模型生成的标题、促销金额、日期、参数、单位和免责声明都必须逐字校对。

## 五步完成详情页长图

1. **写页面大纲**：按首屏、场景、功能、材质、参数、售后划分模块，每块只回答一个用户问题。
2. **建立视觉规则**：固定比例、背景、镜头、色调、字体区和留白；需要系列延展时使用同一组已核准参考图。
3. **逐块生成**：先完成首屏和关键功能块，每轮只改变一个变量。尚未通过商品事实验收的图片不能作为下一块的参考。
4. **分层修正**：文字或局部区域有问题时只修改目标区域，并明确哪些商品、构图、光线和其他文字必须保持不变；修改后检查边界和整图是否发生意外变化。
5. **拼接与终检**：统一模块宽度、间距和色调，导出后分别检查手机端与桌面端的文字可读性、产品一致性、素材权利和当前平台要求。

## 可直接使用的提示词

### 参考图控制的详情页首屏

```text
为上传图片中的台灯制作电商详情页首屏主视觉。商品结构、颜色、Logo 和配件位置以商品图为准。台灯放在简洁书桌上，主体居中偏下，顶部保留标题区域。不得新增参考资料中没有的接口、配件、认证、参数或促销信息。保持透视和接触阴影自然，不生成文字。
```

### 带信息层级的功能块

```text
为上传图片中的台灯制作 4:5 细节展示图。标题为“细节展示”，依次安排整体外观、灯罩和底座三个区域。产品外观、颜色、Logo 和包装文字以参考图为准，不展示原图没有提供的内部结构，不补写功率、价格或认证。保持清晰层级，在图片旁保留文字排版空间，方便后续加入已经核实的商品说明。
```

## 与视频素材衔接

详情页需要产品视频或广告短片时，可使用 [Seedance 2.0](https://flux-art.cc/zh/models/seedance-2-0)（[EN](https://flux-art.cc/en/models/seedance-2-0)）。先让静态模块通过商品事实和视觉验收，再把已核准的商品图、场景与单一卖点整理为视频素材，避免在视频阶段重新定义商品外观。

## 交付验收清单

- [ ] 商品结构、颜色、材质、Logo、标签和配件与原始资料一致
- [ ] 标题、促销金额、日期、参数、单位和免责声明已逐字核对
- [ ] 各模块比例、色调、留白和阅读顺序一致
- [ ] 局部修改没有意外改变商品、构图、光线或其他文字
- [ ] 手机端与桌面端预览中的文字、细节和拼接边界清晰可读
- [ ] 参考图、字体、Logo、人物和其他素材具备使用权限
- [ ] 发布前已检查当前平台规则与 [Flux Art 合规清单](06-compliance.md)

## FAQ

**Q:详情页应该一次生成整张长图吗?**

建议先拆成可以单独验收的模块。分块制作便于固定商品事实、发现局部问题和控制修改范围，最后再统一宽度、间距和色调完成拼接。

**Q:Seedream 4.5 和 Seedream 5.0 Pro 怎么选?**

参考图控制、局部改图、海报排版或电商主视觉可比较 Seedream 4.5；高信息量视觉、信息图或精准图片编辑可比较 Seedream 5.0 Pro。两者都不能替代商品事实、文字和素材权利的人工验收。

**Q:为什么不直接让模型生成全部参数和文案?**

详情页中的参数、单位、促销金额、日期、认证和售后说明必须来自已核实资料。模型可帮助组织视觉，但不能补全未知商品事实；发布前仍要逐字校对。

**Q:怎样避免局部修改影响整张图?**

每轮只框选一个目标区域，同时列出必须保持不变的商品、构图、光线、色彩和其他文字。完成后先检查修改边界，再检查整张图是否出现意外变化；影响范围扩大时返回上一个已核准版本。

## EN Summary

Build long ecommerce detail pages in [Flux Art](https://flux-art.cc) as reviewable modules rather than one unstructured image. Use [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) for product images and photorealistic commercial photography, compare [Seedream 4.5](https://flux-art.cc/en/models/seedream-4-5) for reference-controlled ecommerce visuals and poster layouts, and use [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro) for information-rich visuals and precise image editing. Lock verified product facts first, change one variable per iteration, proofread every label and number, inspect local-edit boundaries, and confirm asset rights and current marketplace requirements before release.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
