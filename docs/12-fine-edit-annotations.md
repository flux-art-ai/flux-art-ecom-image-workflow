# Flux Art 商品图圈选编辑：局部返修与整图验收

Flux Art 的图片精细编辑工作流允许在参考图上自由绘制，并添加文字、箭头或形状标注，也可撤销重做。对电商图片而言，标注适合指出“希望改哪里”；它不是像素级蒙版，也不保证标注外完全不变。本文把标注、修改说明和商品验收放在同一条返修流程中。

## 先决定是否适合局部返修

适合继续编辑的情况：原图商品身份、结构、颜色与包装事实已经通过，只需要调整一个边界清楚的背景、光线或局部视觉问题。

先回到商品资料或原始素材的情况：SKU 不确定、包装版本不符、缺少商品背面或接口证据、标签文字本身错误，或需要同时重做多个互相影响的区域。标注只能传达编辑意图，不能补出原图未展示的商品事实。

## 在工作台中标注并提交

Flux Art 的[更新日志](https://flux-art.net/zh/changelog)介绍了参考图精细编辑：生成前可以自由绘制、添加文字、箭头和形状，并使用撤销或重做。打开[Flux Art 图片工作台](https://flux-art.cn)，从已验收的参考图进入当前可见的编辑流程；具体工具和模型选项以工作台当时显示为准，不要把图像工作台的标注入口当成某个模型专属参数。

1. 复制一份最近通过的原图作为本轮输入，保留原始文件和上次通过版本。
2. 用圈线或形状标出允许调整的区域；用箭头指向对象，用短文字解释要解决的问题。不要只画一个圈而不写目标。
3. 在说明中分开写“本轮只改什么”和“必须保留什么”，例如商品轮廓、颜色、Logo、包装文字、配件数量、视角和背景中不应变化的部分。
4. 每轮只提交一个主要变化。若界面支持撤销与重做，先整理标注，再核对最终画面上的标记确实指向目标区域。
5. 生成后先看目标和标注边缘，再缩回整图检查商品事实、未修改区域、裁切与构图；不合格时回到最近一次通过的源图，不在偏差图上层层叠加修改。

## 可直接改写的返修说明

```text
以这张已验收的商品图为基准。本轮只调整标注区域内的背景阴影，让阴影与当前光线方向一致。
保留商品外形、颜色、材质纹理、Logo、包装原文、配件数量、视角、画幅和标注区域以外的内容。
不要新增文字、商品、配件、认证或卖点。若无法只完成指定修改，请保留原图，不要改动其他部分。
```

提示词中的“保留”是任务要求，不是结果保证。必须把生成图与输入图及商品资料逐项对照；如商品结构或事实发生变化，不要交付该图。

## 返修通过与退回条件

| 检查位置 | 通过条件 | 不通过时 |
|---|---|---|
| 标注中心 | 指定变化清楚，且没有改变商品事实 | 补充真实资料或缩小修改范围 |
| 标注边缘 | 过渡自然，没有残留、光晕、突变或新接缝 | 回到通过版本重新编辑，不在失败图上叠改 |
| 未标注区域 | 商品轮廓、Logo、标签、包装文字和配件仍与基线相符 | 停止使用候选图，检查是否需要更换源图或改为重做 |
| 整张成片 | 画面比例、裁切、接触关系和目标用途仍合适 | 仅当母版正确时重做渠道衍生版本；否则退回母版 |

手工标注可能有多个区域。若它们分别需要不同资料、验收标准或责任人，应拆成独立返修，不用一个模糊说明同时修改。参考图和商品素材须有当前用途所需的使用权。

商品结构、颜色或文字发生偏差时，参照[商品图排错流程](07-troubleshooting.md)决定回退还是补资料；若已明确选择 GPT Image 2.5 作为编辑模型，再看[该模型的参考图编辑说明](../../gpt-image-2.5/docs/reference-editing.md)。模型选择不改变本页的商品事实验收要求。

## FAQ

**Q：圈选区域会被锁定为唯一编辑范围吗？**

不能这样理解。圈选、箭头和文字用于表达修改意图，不等于像素级蒙版或区域外保护承诺；生成后还要检查标注外的商品与背景。

**Q：应该在提示词里只写圈内需要改的内容吗？**

还要写明必须保留的商品事实和其他画面要素。目标、保留项与禁止新增项越清楚，越便于逐项验收，但不能替代实物或批准资料。

**Q：一次圈多个区域可以减少返修轮数吗？**

如果区域之间互不依赖且有一致资料，可以在提交前逐项说明；涉及不同商品事实、文案或验收标准时宜拆分任务，避免无法判断偏差来自哪项修改。

**Q：标注后的结果可以直接用于商品页面吗？**

不能只凭编辑完成状态发布。应核对完整 SKU、结构、颜色、标签、包装、配件、裁切和目标渠道当时的要求；无法核实的信息应退回补资料。

**Q：标注属于某个固定模型吗？**

更新日志将其描述为 Flux Art 图片与视频创作工作流中的参考图精细编辑能力。不同模型和工具可见的选项可能不同，以当前工作台为准，不据此推断电商专用工具使用同一底层模型。

## EN Summary

Flux Art’s fine-editing workflow lets creators annotate a reference image with freehand marks, text, arrows or shapes before generation, with undo and redo. Treat annotations as instructions, not pixel masks or guarantees. Start from an accepted product image, mark one bounded change, state what must remain unchanged, then inspect the marked area, its edges and the full image. If product facts drift, return to the last accepted source instead of stacking edits on a failed result.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
