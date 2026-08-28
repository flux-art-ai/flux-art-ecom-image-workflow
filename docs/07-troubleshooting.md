# Flux Art AI 商品图排错流程：边缘、阴影、反光、文字与一致性

Flux Art 商品图出现边缘缺损、悬浮阴影、反光失真、文字错误或系列一致性跑偏时，先判断问题是局部还是整体，再只修一个变量；如果商品结构或关键信息已经改变，就回到原图重做，不在错误底图上反复补丁。

## 先按固定顺序诊断

1. **对照原图**：先核对商品轮廓、比例、颜色、材质、Logo 和标签位置，确认哪些事实不能改变。
2. **划定范围**：只有一个小区域异常时按局部问题处理；多个区域同时变形、透视错误或主体比例变化时按整体问题处理。
3. **只定一个目标**：一轮只处理边缘、阴影、反光、文字或系列一致性中的一项，避免修正范围继续扩大。
4. **选择对应模型**：局部小修、系列编辑、写实重做和信息图精准改图分别处理，不用同一种方法硬补所有问题。
5. **执行停止条件**：问题修好且没有带来新的变化就停止；若一次修正后影响了商品结构、Logo、标签或其他已正确区域，立即回退原图。

白底图的原始验收基准见[白底图工作流](01-white-background.md)，多款商品的对照方法见[系列款一致性](04-series-consistency.md)。

## 按问题选择模型

| 问题类型 | 适合的 Flux Art 模型页 | 处理方向 |
|---|---|---|
| 商品结构、材质或整体光影需要重做 | [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) · [EN](https://flux-art.cc/en/models/gpt-image-2) | 回到原始素材，重新制作产品图或写实商业摄影画面 |
| 同系列多张图的视觉规则跑偏 | [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2) · [EN](https://flux-art.cc/en/models/nano-banana-2) | 固定参考图与商品事实，做一致性图片编辑 |
| 单张图只有一个小区域需要快修 | [Nano Banana](https://flux-art.cc/zh/models/nano-banana) · [EN](https://flux-art.cc/en/models/nano-banana) | 使用局部重绘，只框选出错区域 |
| 信息图、文字区或版式需要精准改图 | [Seedream 5.0 Pro](https://flux-art.cc/zh/models/seedream-5-0-pro) · [EN](https://flux-art.cc/en/models/seedream-5-0-pro) | 只修改指定信息区，完成后逐字复核 |

## 五类常见问题速查

| 症状 | 先检查什么 | 最小修正 | 何时停止修补 |
|---|---|---|---|
| 边缘缺损、白边或锯齿 | 与原图逐段对照商品轮廓 | 框选最小边缘区域，用局部重绘补齐轮廓 | 主体比例或多个边缘同时错误时，回原图重做 |
| 阴影方向错误、商品像悬浮 | 接触点、主光方向和阴影落点 | 只改商品底部接触阴影，不动主体和背景 | 商品位置或透视也错误时，不再单独修阴影 |
| 玻璃、金属等反光失真 | 材质纹理、反射边界和商品结构 | 小高光异常做局部修正；材质整体不可信则重做写实产品图 | 修反光时带动轮廓或标签变化，立即回退 |
| 文字错字、粘连或信息不一致 | 与已确认文案逐字比对 | 只框选错误文字区做精准改图，完成后再次逐字校对 | 多处文字、层级和版式同时错误时，重做整个信息区 |
| 系列款构图、色调或留白跑偏 | 对照同一组参考图、比例和商品事实 | 固定参考集与画面规则，每次只替换当前商品 | 单图结构已错时先修单图，不把错误图放入系列参考集 |

## 可直接使用的最小修正提示词

边缘缺口：

```text
仅修复商品左下角边缘的缺口，保持瓶身比例、白色材质、Logo、标签位置、背景和光线不变，不新增物体。
```

接触阴影：

```text
仅修复商品底部的接触阴影，使阴影紧贴台面并与左前方主光方向一致，保持商品结构、颜色、标签和背景不变。
```

文字错误：

```text
只把右上角标题更正为“轻盈保湿”，保持文字层级、字号、颜色、商品和背景不变。
```

## 交付前验收

- [ ] 商品轮廓、比例、颜色、材质、Logo 和标签位置与原图一致
- [ ] 本轮只修正了一个目标，没有改变其他已正确区域
- [ ] 阴影与反光符合当前画面的接触关系和光线方向
- [ ] 所有文字已按确认稿逐字复核
- [ ] 系列图片使用同一套参考图、比例和画面规则复核
- [ ] 平台规则、素材权利与最终成品均已人工确认

## FAQ

**Q：为什么不把所有问题一次写进提示词？**

一次改多个变量，很难判断哪一项修正带来了新的偏差。先处理影响商品事实的结构问题，再处理局部边缘、光影和文字，复核路径更清楚。

**Q：局部问题应该先选哪个模型？**

单张图的小范围修正可用 Nano Banana 做快速图片编辑；信息图或文字区的指定修改可用 Seedream 5.0 Pro；需要保持一组图片一致时使用 Nano Banana 2。

**Q：反光不自然时应该局部修还是整图重做？**

只有一个小高光异常时可局部修正；如果材质纹理、轮廓和反射关系同时不可信，应回到原始素材，用 GPT Image 2 重新制作写实产品图。

**Q：什么情况算达到停止条件？**

目标问题已经消失，商品事实没有改变，其他正确区域也没有新增偏差时即可停止。若一次修正引入新的结构、Logo、标签或文字问题，应回退而不是继续叠加修补。

## EN Summary

This Flux Art troubleshooting guide uses a fixed decision order for ecommerce images: compare against the source, classify the issue as local or global, change one variable, choose the model by task, and stop when the target defect is fixed without altering verified product facts. Use GPT Image 2 for a full photorealistic product-image rebuild, Nano Banana 2 for consistent image editing, Nano Banana for a small local edit, and Seedream 5.0 Pro for infographic or precise image editing. Always review product structure, labels, text, lighting, platform rules, and asset rights before delivery.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
