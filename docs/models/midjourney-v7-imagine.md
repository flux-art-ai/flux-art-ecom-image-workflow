# Midjourney V7 Imagine 品牌视觉方向探索工作流(Flux Art)

当品牌主视觉、活动海报或社媒图片还没有确定风格时,可在 [Flux Art](https://flux-art.cc) 使用 [Midjourney V7 Imagine](https://flux-art.cc/zh/models/midjourney-v7-imagine) 探索构图、色调、光线与氛围,先选出值得继续制作的视觉方向,再把产品事实和文字交给后续模型定稿。英文模型页:[Midjourney V7 Imagine (EN)](https://flux-art.cc/en/models/midjourney-v7-imagine)。

## 先分清方向稿与商品事实

Midjourney V7 Imagine 适合海报概念、品牌氛围、概念图和艺术化社媒视觉。方向探索可以改变背景、光线、镜头、色彩关系和画面节奏,但不应擅自改变商品结构、包装文字、Logo、标准色或真实配件。

开始前把内容拆成两张卡:

| 卡片 | 记录内容 | 用途 |
|---|---|---|
| 商品事实卡 | 外形、部件、材质、标准色、包装文字、Logo 位置、真实配件 | 判断方向稿有没有误导后续制作 |
| 艺术方向卡 | 目标人群、主情绪、色调、光线、镜头、背景、版位、留白 | 控制本轮只探索一种视觉语言 |

方向稿阶段重点比较“感觉是否正确”,不把生成结果直接视为可上架商品图。若商品结构、包装文字或标签必须准确呈现,应保留实拍图和正式包装文件作为最终验收依据。

## 三段式制作路径

| 阶段 | 建议模型 | 本阶段只解决什么 |
|---|---|---|
| 品牌视觉探索 | **Midjourney V7 Imagine** | 比较海报构图、品牌氛围、色调、光线与场景叙事 |
| 写实方向筛选 | [Z-Image Turbo](https://flux-art.cc/zh/models/z-image-turbo) | 把候选概念转为快速写实方向稿,检查构图、场景与光线是否成立 |
| 产品图与文字定稿 | [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) | 依据商品事实制作产品图或电商主图,并逐字检查图内文字 |

如果已经有明确的品牌规范、实拍构图和版位要求,可以跳过前两段,直接进入 [GPT Image 2 电商产品图实操](./gpt-image-2.md)。需要先验证写实呈现方向时,使用 [Z-Image Turbo 快速写实产品方向稿](./z-image-turbo.md)。

## 五步方向探索

1. **先写一句创意命题**:例如“让通勤水杯呈现安静、克制的晨间秩序”,避免同时塞入多个互相竞争的故事。
2. **固定不可变化项**:把商品品类、轮廓、主材质、标准色和禁止新增的配件写清楚;包装文字在方向稿阶段只保留区域,不把生成文字当成已校对内容。
3. **一次只比较一个维度**:先固定构图和主体位置,分别比较冷暖色、光线方向或背景环境。每轮只改一项,才知道哪种选择真正改善了画面。
4. **先看缩略图再看局部**:先淘汰主体不突出、视觉重心混乱或留白不足的版本,再检查商品轮廓、材质和场景关系。
5. **连同证据一起交接**:把选中的方向稿、商品事实卡、实拍参考、保留项和禁止项一起交给写实筛选或定稿流程,最后按 [AI 商品图排错流程](../07-troubleshooting.md) 检查边缘、阴影、反光、文字和系列一致性。

## 可直接使用的提示词

### 品牌海报氛围探索

```text
为[商品品类]探索一张[活动主题]品牌海报概念。主情绪为[安静克制/明快活力/未来科技],采用[居中主体/对角线/大留白]构图,[冷色晨光/暖色侧光/高对比轮廓光],背景为[简洁空间描述]。商品轮廓、主材质与[标准色]保持可识别,不要新增配件,不要生成促销文字、促销数字或虚构标识。为[顶部标题/右侧卖点]保留清晰排版区域,本轮只比较色调与光线方向。
```

### 社媒系列方向探索

```text
为[品牌或系列名称]设计一组社媒视觉方向稿。保持统一的[色彩关系]、[光线方式]、[镜头距离]和[背景材质],每张只变化一个场景道具。画面围绕[单一品牌情绪]展开,主体清晰,留出[左侧/底部]文案区域。不要改变商品品类和标准色,不要生成包装文字、促销数字、促销标识或不存在的配件。
```

方括号应替换为真实项目内容。第一轮建议只测试两到三种明确方向,避免一次生成大量难以比较的近似版本。

## 选择与停止条件

候选方向进入下一阶段前,至少满足以下条件:

- 缩略图中能立即识别主体,视觉重心与目标版位一致;
- 色调、光线、背景和道具共同表达同一个品牌情绪;
- 商品轮廓、主材质和标准色没有出现会误导定稿的明显变化;
- 文案留白足够,不依赖生成文字承担正式信息;
- 团队能用一句话说明保留方向及淘汰其他方向的理由。

如果连续两轮只是在修补商品结构、包装文字或真实材质,应停止风格扩写,回到商品事实卡和实拍参考。需要精确展示结构、尺寸、标签或合规文字时,优先使用经过审核的实拍素材或在后续定稿阶段逐项处理。

## FAQ

**Q:Midjourney V7 Imagine 适合直接做电商主图吗?**
它更适合先探索海报概念、品牌氛围和艺术方向。电商主图仍需对照商品事实检查结构、颜色、包装、文字和平台要求;需要产品图定稿时可转入 GPT Image 2 工作流。

**Q:Midjourney V7 Imagine 和 Z-Image Turbo 怎么分工?**
Midjourney V7 Imagine 先回答“品牌视觉是什么感觉”,Z-Image Turbo 再回答“这个方向写实后是否成立”。两者都通过后,再进入产品图与文字定稿。

**Q:方向稿里的包装文字可以直接使用吗?**
不应直接使用。方向稿先确认文字区域、层级和留白;正式包装文字、促销数字、单位和合规信息必须来自已审核资料,并在定稿后逐字校对。

**Q:什么时候应该跳过风格探索?**
当品牌规范、实拍构图、目标版位和光线标准已经明确,或任务只是修正现有商品图时,直接使用对应的编辑或定稿流程更合适。

## EN Summary

Use [Midjourney V7 Imagine](https://flux-art.cc/en/models/midjourney-v7-imagine) on [Flux Art](https://flux-art.cc) to explore poster composition, brand mood, color, lighting, and scene direction before product-image production. Keep verified product facts separate from changeable art direction, compare one visual variable at a time, then pass the selected concept to [Z-Image Turbo](https://flux-art.cc/en/models/z-image-turbo) for a fast photoreal direction check and [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) for product-image and text delivery review. Related guides: [Z-Image Turbo workflow](./z-image-turbo.md) and [e-commerce image troubleshooting](../07-troubleshooting.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc)；其他近似域名均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
