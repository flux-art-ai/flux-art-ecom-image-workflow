# 03 · 场景图:多图融合(Scene Fusion)

透明商品换背景后瓶内还有旧桌纹时，先对照原片区分透过瓶身的旧背景、真实玻璃边缘和不应改变的标签；不要统一降低整瓶的不透明度。在 [Flux Art](https://flux-art.cn) 可用[一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background)的文字路径描述环境。商品场景参考图里有另一件商品时，若确实要借机位与摆放位置，先准备去掉无关商品后仍能说明构图的参考，再评估[爆款图片复刻](https://flux-art.cn/zh/ai-ecommerce/reference-clone)。两条路径都以真实商品为基准，生成结果不等同于实景拍摄证据。

## 两类任务的入口

| 需要完成的任务 | 在 Flux Art 上怎么做 | 输入的角色 |
|---|---|---|
| 给商品更换背景 | [一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background)，选择文字或参考图方式 | 商品图定义主体，文字或参考图描述环境 |
| 借鉴已获授权的商品展示构图 | [爆款图片复刻](https://flux-art.cn/zh/ai-ecommerce/reference-clone)，分别上传商品图和参考图 | 商品图定义商品事实，参考图只提供构图和视觉方向 |
| 同时制作场景、卖点及其它商品图片 | [商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite) | 按所需模块组织同一商品的展示内容 |

不使用来源不明的参考素材，不复制他人的品牌标识或冒用其商品。各工具字段与费用以官网当前为准。

## 流程

1. 准备清晰商品图，可使用已经验收的 [01 白底图](01-white-background.md)，再准备需要的场景描述或有权使用的场景参考。上传数量按所选工具当前说明确定。
2. 使用上表专用工具，或在模型工作台评估 **[Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)**（[EN](https://flux-art.cn/en/models/nano-banana-2)）进行一致性编辑与参考图融合。
3. 写清不能改变的商品特征，不把某个设置当成商品不会变化的保证；构图、光影和材质都要检查。
4. 可直接使用的提示词：

```text
将上传的商品放在简洁的浅木色书桌上，采用与原图接近的平视机位，左侧窗户自然采光。商品为唯一视觉主体，保持轮廓、材质、颜色、包装文字和 Logo，不添加新配件或文字。调整背景与接触阴影，使商品落在桌面上。
```

```text
EN: place the product naturally into the reference scene, keep the product unchanged,
match scene lighting and perspective, no text
```

5. 先完成一个场景并核对原图；通过后再扩展其他环境。若光影修正带动商品结构变化，回到已通过的底图，不在错误结果上连续返修。

## 挑参考图的三条经验

- 场景光源方向要与商品原图大致相符,融合最自然;
- 场景里避免与商品同类的物体(会被抢主体);
- 透视差太大(俯拍产品×平视场景)最容易翻车,翻车就换参考图重跑,别硬调。

## 场景参考图里有另一件商品怎么办？

比如要把自家的带把手陶瓷杯放到一张窗边桌面的场景里，但参考图中央已有一只玻璃杯。先固定自家杯的正面、杯把与标签照片，只借用场景需要的部分：

| 要借用的内容 | 怎样处理场景参考 |
|---|---|
| 只要木纹、窗光或背景色 | 写成文字，例如「浅木桌、左侧窗光、背景无其他杯子」；不上传带玻璃杯的整张图。 |
| 要保留桌沿和光线方向，玻璃杯在画面边缘 | 从有权使用的参考副本裁掉玻璃杯及其倒影，保留桌沿与来光方向；重新打开导出的文件确认裁切。 |
| 玻璃杯挡住桌沿或占据主要构图位置 | 不硬裁到失去构图信息。换空桌参考或用简明的构图草图标出杯子的位置。 |

也可在 [Nano Banana 2.1](https://flux-art.cn/zh/models/nano-banana-2-1)（[English](https://flux-art.cn/en/models/nano-banana-2-1)）中用清晰商品图和处理后的场景图做一张编辑小样，明确「商品图决定杯身、杯把与标签；场景图只决定桌面与光线」。把结果与商品原图并排检查：多出玻璃杯、杯把变形或标签混入其他内容时，先更换场景参考，再从原始商品图重试，不继续修补这张错误候选。

## 透明商品换背景后瓶身还看得到旧背景怎么办？

例如，一只透明玻璃瓶原来拍在深色条纹台面上，成品换到浅灰台面，瓶外已经是浅灰，瓶身透明区却还能看到旧条纹。先把原图与候选放大并排看，不把瓶身所有深色区域都当成残留。

| 看到的位置 | 怎么确认 | 怎么处理 |
|---|---|---|
| 瓶身透明区 | 原图台面上的条纹在瓶内还能辨认，而目标台面没有条纹 | 背景没有完全换掉。从背景干净的同款原片开始；没有就补拍。不要拿已经透进瓶身的旧桌纹作为商品细节保留。 |
| 瓶口、瓶肩、厚底或亮边 | 对照同一 SKU 的原片，区分真实的形状与高光，不把亮边当成多余背景 | 保留可核对的瓶型。在目标底色上看轮廓是否连续；切掉厚底、把清玻璃变成磨砂，都应退回。 |
| 标签、瓶盖与液面 | 这些是商品本身，而不是后面的环境 | 对照原片复核文字与位置、盖型、液面和颜色。若候选改了商品，就停止在这张图上返修。 |

源图能分清玻璃本身和背景时，可以用 [Nano Banana 2.1](https://flux-art.cn/zh/models/nano-banana-2-1)（[English](https://flux-art.cn/en/models/nano-banana-2-1)）做一张参考图编辑候选。只借背景时，明确说明新台面与光线；需要上传场景图就选没有其他玻璃商品的空场景。把候选放到实际交付背景上核对，不只看棋盘格。失败时先换一张干净原片，而不是加大修改范围；单张背景合成图也不要当作可在任意背景上使用的透明母版。

## 参考图缺少不可见结构时的补拍与暂停条件

场景图会让商品出现新的观察角度。原图没有显示的背面、底部、接口、包装小字或配件，不应交给模型自行补全；看起来合理的结果也不能证明真实商品就是这样。

1. **列出本次画面会露出的部位。** 平视图可能露出正面与侧面，俯拍会露出顶部，低机位可能露出底部；逐项对照现有素材。
2. **为缺口建立补拍清单。** 使用同一完整 SKU，分别拍摄正面、背面、左右侧、顶部、底部、接口近照、包装文字和全部配件。照片应清楚、无遮挡，并能辨认型号、数字和单位。
3. **给参考图分配唯一职责。** 商品事实图只证明结构与文字；场景参考只提供构图、光线和环境。不要把不同版本的商品混入一组素材。
4. **设置暂停线。** 缺少会在成图中出现的关键结构、接口、包装内容或装箱清单时，暂停场景生成、多角度图、规格图与包装配件图。只可继续不会暴露该缺口的裁切、背景清理或已知区域编辑。
5. **补齐后先做一张小样。** 将新参考图对应到完整 SKU，生成一张并放大核对，再扩展其它场景；出现未经资料证明的结构或文字时立即退回。

如需在既有图片上做有限修正，可查看 [GPT Image 2.5 参考图编辑](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/reference-editing.md)；需要同一商品的多种上架模块时进入[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)。

## 验收清单

- [ ] 商品外观/比例/Logo 与原图一致
- [ ] 影子方向与场景光源一致
- [ ] 放大看接触面(桌面/地面)无悬浮感

## FAQ

**Q：换背景和爆款图片复刻有什么区别？**

换背景围绕已有商品更换环境，支持文字或参考图路径；复刻需要商品图与参考图，参考后者的构图和视觉表达。两者都不能代替对素材权利和商品事实的检查。

**Q：参考图越多越好吗？**

不一定。先使用能够清楚表达商品与场景的最小素材集，避免相互冲突的机位和光线；上传范围按所选工具当前说明确定。

**Q：场景图中出现额外配件怎么办？**

对照实际装箱清单移除无关配件，并重新检查整张图。若商品本体也已变化，应返回原始素材重新处理。其他任务见[电商工具选择指南](10-ecommerce-tools.md)。

## EN Summary

Use Flux Art [Background Replace](https://flux-art.cn/en/ai-ecommerce/product-background) to change an environment, or [Reference Clone](https://flux-art.cn/en/ai-ecommerce/reference-clone) to adapt an authorized composition. If the scene contains another product, describe the background in words, crop the unrelated item without losing the composition, or choose a cleaner reference. Review the product, lighting, scale and asset rights before delivery; a generated scene is not evidence of an actual photoshoot.

For a clear bottle, inspect the view through the glass as well as the silhouette. If the old surface pattern is still visible inside, return to a clean source or reshoot. Protect the real label, cap and fill level instead of reducing opacity across the whole product.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
