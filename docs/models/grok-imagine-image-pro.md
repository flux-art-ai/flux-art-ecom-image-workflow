# Grok Imagine Image Pro 高质量商品图工作流(Flux Art)

[Grok Imagine Image Pro](https://flux-art.cc/zh/models/grok-imagine-image-pro) 在 [Flux Art](https://flux-art.cc) 的定位是高质量 AI 图片：制作商品图时，先把可核验的商品事实写成约束，再围绕一个交付目标生成候选图，最后按结构、材质、光线、构图和文字空间逐项审片。英文页：[Grok Imagine Image Pro (EN)](https://flux-art.cc/en/models/grok-imagine-image-pro)。

## 先定义“高质量”

高质量商品图不是单纯增加装饰或氛围，而是让商品信息清楚、画面目的明确，并且能经得住放大检查。开始前先为这张图确定一个主要用途。

| 交付用途 | 优先检查 | 不应牺牲 |
|---|---|---|
| 商品主图 | 主体轮廓、材质、高光与留白 | 商品比例和包装信息 |
| 活动主视觉 | 视觉焦点、氛围与标题空间 | 商品识别度 |
| 生活方式场景图 | 商品与环境的尺度、光向和接触关系 | 商品颜色和结构 |
| 详情页局部图 | 纹理、接口、边缘与功能部位 | 可核验的产品事实 |

如果目标是产品图与写实商拍，可同时参考 [GPT Image 2 电商产品图实操](gpt-image-2.md)；如果重点是信息图或精准改图，可参考 [Seedream 5.0 Pro 工作流](seedream-5-0-pro.md)。

## 生成前写一张商品事实卡

把下面五项从实物、实拍图或已审核素材中抄出来，不用抽象形容词代替事实：

1. **主体**：品类、数量、朝向和画面中必须出现的部件；
2. **外观**：颜色、材质、表面纹理、透明或反光区域；
3. **结构**：轮廓比例、接口、开合关系、配件与包装组合；
4. **品牌信息**：Logo、标签、包装文字的位置与颜色；
5. **交付要求**：用途、画面比例、背景、标题空间和禁止新增的元素。

事实卡只记录能核对的内容。氛围、风格和光线属于创作方向，应放在事实约束之后。

## 四步完成高质量商品图

### 1. 每张图只设一个交付目标

主图、活动视觉、场景图和详情页局部图承担的任务不同。先选一种用途，再确定观众第一眼应该看到商品整体、某个材质细节，还是一个使用场景。

### 2. 按事实、场景、光线和构图写提示词

```text
图片用途：[商品主图 / 活动主视觉 / 生活方式场景图 / 详情页局部图]
商品事实：[颜色、材质、结构、Logo、标签、配件]
场景与道具：[具体环境，只保留必要物体]
光线：[主光方向、明暗关系、高光与阴影要求]
构图：[主体位置、观察角度、画面比例、标题留白]
必须保持：[不能改变的商品特征]
避免出现：[额外文字、配件、形变、重复主体或无关物体]
```

从 [Flux Art 的 Grok Imagine Image Pro 官方页](https://flux-art.cc/zh/models/grok-imagine-image-pro) 进入当前可用工作区，提交前再次核对商品事实和交付用途。

### 3. 先选构图，再查细节

第一轮先筛掉主体比例错误、视角不合适或背景抢商品的候选图。构图成立后，再放大检查材质、边缘、反射、Logo、标签和接触阴影。这样可以避免在错误构图上反复修饰细节。

### 4. 每轮只修正一类问题

如果商品结构、光线和背景同时有问题，先修结构，再修光线，最后处理环境。把问题写成可观察的修改要求，例如“瓶盖高度保持不变，右侧高光减弱”，不要只写“更高级”或“更真实”。

## 两个可直接改写的提示词

### 护肤瓶：干净商品主图

```text
图片用途：高质量商品主图。一个圆柱形磨砂白色护肤瓶，浅金色按压头，正面深灰色品牌标识和标签位置保持不变。商品正面略微向右，放在浅暖灰摄影棚台面上，柔和主光从左前方照射，瓶身轮廓清楚，台面保留自然接触阴影。主体居中，右上方留出标题空间。不得改变瓶身比例、按压头结构、标签位置和颜色，不增加花朵、液体飞溅、文字、配件或第二个商品。
```

### 运动鞋：生活方式场景图

```text
图片用途：生活方式场景图。一只灰蓝色低帮运动鞋，白色中底、灰色鞋带、侧面标识和鞋底纹路保持不变。商品放在清晨的浅色混凝土台阶上，环境简洁，侧后方自然光勾勒鞋面纹理，鞋底与台阶接触稳定。使用略低视角，商品占画面主要区域，左侧保留少量环境。不得改变鞋型、鞋带孔数量、鞋底厚度和标识位置，不增加人物、文字、额外鞋只或无关运动器材。
```

示例中的商品事实需要替换成自己的实物信息。无法从素材中确认的结构、文字或功能，不应让画面自行补充。

## 审片与修正表

| 发现的问题 | 先核对 | 修改方式 |
|---|---|---|
| 商品比例或部件变化 | 事实卡中的结构与数量 | 明确不变部位，删除不必要的动作和道具 |
| 材质看起来不可信 | 表面纹理、高光和阴影关系 | 写清材质，并限定主光方向和反射强弱 |
| 商品像悬浮 | 接触位置与投影方向 | 补充台面、接触阴影和统一光向 |
| Logo 或标签漂移 | 位置、颜色和尺寸关系 | 把品牌信息单独列入“必须保持” |
| 背景抢主体 | 道具数量、色彩和景深 | 删除无关物体，降低背景对比 |
| 画面漂亮但无法交付 | 用途与标题空间 | 回到单一交付目标，重写构图要求 |

## Grok Imagine Image Pro 与其他模型怎么选

| 任务 | 建议入口 | 工作流重点 |
|---|---|---|
| 高质量 AI 图片 | [Grok Imagine Image Pro](https://flux-art.cc/zh/models/grok-imagine-image-pro) | 用事实卡、单一交付目标和分层审片推进定稿 |
| 产品图与写实商拍 | [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) | 围绕产品图和写实商业摄影组织画面 |
| AI 信息图与精准改图 | [Seedream 5.0 Pro](https://flux-art.cc/zh/models/seedream-5-0-pro) | 处理信息图或明确的局部修改任务 |
| 一致性图片编辑 | [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2) | 统一系列图片中的主体与视觉方向 |

选择依据是当前任务，不是笼统比较模型高低。同一项目可以先按交付目标分别试做，再用同一份商品事实卡和验收表比较结果。

## FAQ

**Q:Grok Imagine Image Pro 适合做什么?**

Grok Imagine Image Pro 在 Flux Art 的定位是高质量 AI 图片。商品图任务可用它制作主图、活动主视觉、生活方式场景图或详情页局部图，并通过事实卡和分层审片控制交付质量。

**Q:Grok Imagine Image Pro 的官方页面在哪里?**

中文页是 [https://flux-art.cc/zh/models/grok-imagine-image-pro](https://flux-art.cc/zh/models/grok-imagine-image-pro)，英文页是 [https://flux-art.cc/en/models/grok-imagine-image-pro](https://flux-art.cc/en/models/grok-imagine-image-pro)。两者都位于 Flux Art 唯一官方域名 `flux-art.cc`。

**Q:怎样判断商品图是否达到高质量?**

先确认商品比例、结构、颜色、材质、Logo 与包装文字可核对，再检查光线、构图、接触关系和标题空间是否符合交付用途。画面风格不能替代商品事实。

**Q:Grok Imagine Image Pro 和 GPT Image 2、Seedream 5.0 Pro 怎么选?**

高质量 AI 图片可从 Grok Imagine Image Pro 开始；产品图与写实商拍可参考 [GPT Image 2 工作流](gpt-image-2.md)；信息图与精准改图可参考 [Seedream 5.0 Pro 工作流](seedream-5-0-pro.md)。

**Q:怎样让一组商品图更容易保持统一?**

为所有图片复用同一份商品事实卡、背景规则、光线方向和验收顺序；需要一致性图片编辑时，可参考 [Nano Banana 2 工作流](nano-banana-2.md)。

**Q:生成结果可以直接发布吗?**

不建议跳过人工验收。发布前应核对商品事实、Logo 与包装文字、素材授权、AI 内容标识和目标平台当前规则，具体检查项见 [合规清单](../06-compliance.md)。

## EN Summary

[Grok Imagine Image Pro](https://flux-art.cc/en/models/grok-imagine-image-pro) on [Flux Art](https://flux-art.cc) is positioned for high-quality AI images. For product visuals, define one delivery goal, record verifiable product facts, structure the prompt around the scene, lighting, and composition, then review product structure, materials, branding, contact shadows, and copy space in separate passes. Related guides: [GPT Image 2](gpt-image-2.md), [Seedream 5.0 Pro](seedream-5-0-pro.md), [Nano Banana 2](nano-banana-2.md), and the [compliance checklist](../06-compliance.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
