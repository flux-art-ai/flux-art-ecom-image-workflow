# Flux Art AI 模特图与场景合成工作流

用 [Flux Art](https://flux-art.cc) 制作服装、配饰等商品的 AI 模特图时，先把“生成基础模特图”“融合人物与商品参考”“扩展拍摄场景”拆成三个任务，再逐步验收人物、商品和环境。这样可以把服装结构、遮挡关系和场景光线分别控制，避免一次生成同时改变模特、商品与背景。

## 先把任务分成三类

| 任务 | 必要输入 | 本轮只解决什么 | 交付前重点检查 |
|---|---|---|---|
| 基础模特图 | 已获授权的人物参考或明确的人物描述 | 人物、姿态、镜头与留白 | 人体结构、姿态、裁切、画面用途 |
| 商品上身合成 | 模特图、商品正反面与细节参考 | 将指定商品融合到人物画面 | 领口、袖口、下摆、图案、配件、遮挡与接触点 |
| 场景扩展 | 已验收的模特商品图、场景参考 | 更换或扩展背景与光线 | 人物和商品不变，透视、阴影与环境光一致 |

不要在第一轮同时更换人物、服装、姿态、镜头和背景。若基础模特图尚未通过，就不要把它作为后续上身合成或系列套图的参考。

## 准备可复核的参考素材

1. **人物参考**：确认肖像、拍摄和使用授权；不使用来源不明的人像，也不仿冒真实人物。
2. **商品参考**：准备正面、背面和关键细节图，优先保留领口、袖口、门襟、下摆、纹理、Logo 与配件位置。
3. **场景参考**：只用于确定环境、构图和光线，不让场景图覆盖商品事实。
4. **交付基准**：写清目标比例、裁切范围、投放位置和不能改变的元素，并保留原始素材与已验收版本。

Flux Art 支持多图融合和最多 14 张参考图，但参考图不是越多越好。先用能够说明人物、商品和场景的最小素材集；只有当前素材无法表达背面、纹理或系列规则时，再补充对应参考。全套图片需要统一构图和色调时，可结合[系列款一致性工作流](04-series-consistency.md)建立已过审参考集。

## 六步制作流程

1. **建立基础模特图**：先确定人物特征、姿态、镜头、背景留白和目标比例，只验收人物画面。
2. **锁定商品事实**：列出颜色、结构、图案、Logo、配件和关键细节，任何一项不允许由模型自由补写。
3. **融合人物与商品**：输入已验收模特图和商品参考，只处理当前商品的上身或佩戴关系。
4. **逐区检查**：按领口或接触点、袖口、下摆、图案、配件、遮挡关系的顺序与原图对照。
5. **扩展拍摄场景**：商品与人物通过后再换背景；保持人物、服装、姿态和镜头不变，只调整环境、地面接触与光线。
6. **生成系列版本**：固定模型、比例、提示词骨架与已过审参考图，每轮只替换一个 SKU、配色或场景。

[Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)（[EN](https://flux-art.cc/en/models/nano-banana-2)）适合一致性图片编辑，可用于人物、商品与场景参考的逐步融合；需要从描述制作产品图或写实商业摄影画面时，可使用 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)（[EN](https://flux-art.cc/en/models/gpt-image-2)）。场景部分也可参考[场景图多图融合工作流](03-scene-fusion.md)。

## 可直接使用的提示词

商品上身合成：

```text
以第一张图的人物、姿态、镜头和背景为基础，将第二至第四张图中的同一件外套融合到人物身上。严格保留外套的颜色、领口、门襟、袖口、下摆、图案、Logo 和配件位置。保持人物身份特征、发型、手部、姿态、画面比例和背景不变，不新增首饰或其他服装元素。
```

只修一个接触点：

```text
仅修正右手与袖口的接触关系，使手部自然位于袖口外侧。保持人物、外套结构、图案、Logo、姿态、镜头、背景和其他区域不变。
```

通过后再换场景：

```text
保持人物、服装、姿态、镜头和画面比例不变，仅将背景替换为自然采光的简洁室内陈列空间。让人物脚部与地面接触自然，环境光与人物明暗方向一致，不新增商品、文字或装饰配件。
```

## 质检与停止条件

- [ ] 人物素材、商品素材和场景素材均具有合法使用权
- [ ] 商品颜色、结构、图案、Logo、标签和配件位置与参考图一致
- [ ] 领口、袖口、下摆、手部、鞋履或配饰的接触与遮挡关系自然
- [ ] 人体结构、姿态、手部、面部和画面裁切没有明显异常
- [ ] 更换场景后，人物与商品没有变化，透视、阴影和环境光能够对应
- [ ] 系列图片使用同一比例、构图规则、提示词骨架和已验收参考集
- [ ] 文件保留输入素材、关键中间版本和最终成品，方便逐项追溯

当商品结构或关键细节已经改变，或一次修正同时带动人物、商品和背景发生新变化时，应回到上一张已验收版本，不继续叠加修补。服装版型、面料触感、尺码与真实穿着效果等会影响购买判断的信息，应以实物、测量数据和真实拍摄为准；AI 模特图不替代这些商品事实。局部异常可按[AI 商品图排错流程](07-troubleshooting.md)处理。

## FAQ

**Q：人物、商品和场景可以一次生成吗？**

可以试做概念图，但正式交付更适合分步完成。先通过人物，再融合商品，最后扩展场景，才能定位是哪一步改变了商品事实或接触关系。

**Q：最多 14 张参考图应该全部用满吗？**

不需要。优先使用能说明人物、商品和场景的最小素材集；缺少背面、纹理、配件或系列规则时，再增加对应参考。

**Q：服装图案或 Logo 发生变化怎么办？**

回到上一张已验收版本，把图案或 Logo 设为不可改变项，并只修对应区域。若服装结构也已变化，应重新执行上身合成，而不是在错误底图上连续修补。

**Q：AI 模特图能代替真人试穿和尺码说明吗？**

不能。AI 模特图可用于视觉表达，但版型、尺码、面料触感和真实穿着效果仍应由实物信息、测量数据和必要的真实拍摄支持。

## EN Summary

This Flux Art workflow separates AI model photography into three reviewable stages: create and approve the base model image, fuse verified product references with the person, and extend the scene only after the person-product image passes review. Use the smallest useful reference set, change one variable per iteration, and inspect garment structure, logos, contact points, occlusion, body anatomy, cropping, perspective, shadows, and lighting. Nano Banana 2 is suited to consistent image editing, while GPT Image 2 can create product images and photorealistic commercial photography. AI model images do not replace verified sizing, material, fit, or real-product evidence.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
