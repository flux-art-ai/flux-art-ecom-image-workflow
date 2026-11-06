# Flux Art 电商作图提示词结构：四段写法与中英模板

Flux Art 电商作图提示词可以按“主体、保留、可变、输出”四段组织：先说明要呈现的商品，再列出不能随意改动的事实，接着描述本次创作变化，最后写目标画幅与构图要求。这是一种便于沟通、检查和复用的写法，不是模型规则或结果保证；不同模型和工作台对提示词及输出选项的处理可能不同。

**快速结构：** 主体事实 → 商品保留项 → 场景变化 → 输出要求。

## 四段分别写什么

### 1. 主体：让商品可辨认

写可观察、可核对的商品信息，优先使用商品资料或已批准的图片，不用“高级”“惊艳”“很酷”等主观形容词代替商品特征。

| 太宽泛 | 更可核对的写法 |
|---|---|
| 一款好看的杯子 | 500 ml 直筒保温杯，哑光深蓝杯身，银色旋盖 |
| 一件高级感上衣 | 浅杏色翻领针织衫，单排三粒扣，下摆至大腿中部 |
| 一双很酷的鞋 | 白灰拼色低帮板鞋，橡胶大底，鞋舌有黑色标识 |

这些是提示词写法示例。实际商品的容量、尺寸、颜色、结构和标识必须以对应 SKU 的真实资料为准；没有资料支持的细节不要猜。

### 2. 保留：列出本次不希望改变的商品事实

把容易被改动或影响购买判断的细节逐项列出，而不是只写“保持商品不变”。可按商品选择颜色、形状比例、材质质感、标识位置与文字、扣件数量、接口排布、包装与配件等项目。与本次任务无关的项目可以省略。

例如：

```text
保留：深蓝哑光杯身、直筒比例、银色旋盖结构，以及杯身中下部白色竖排标识的位置和已核对文字。不要添加未提供的配件或功能信息。
```

### 3. 可变：明确本次交给画面创作的部分

把允许变化的内容和范围说清楚，避免背景、商品和构图的修改目标混在一起。常见可变项包括：

- 场景与背景：室内或户外、桌面材质、环境元素、背景虚化程度；
- 光线：光线方向、软硬、色温与阴影表现；
- 构图：拍摄角度、主体位置、留白方向与画面裁切；
- 视觉氛围：简洁、温暖、冷调或其他与品牌相符的方向。

若只想换背景，应直接写“只调整背景和环境，商品外观与位置尽量沿用参考图”，并在生成后检查边缘、透视、接触面和商品细节。提示词表达的是目标，不代表模型一定能完全按要求处理。

### 4. 输出：描述交付画面，而不是猜测参数

写图片用途、工作台当前支持的画幅选项、主体在画面中的位置、需要的留白和是否包含文字。若工作台提供分辨率或其他输出设置，请按界面可选项选择，不要把某种比例、分辨率或参数写成所有模型都支持的固定值。

若画面需要促销文字，先核对实际文案和商品事实；生成后逐字校对，并检查文字是否遮挡商品。若文案不必直接出现在图片中，可要求预留排版区域，再用设计工具添加经过审核的文字。

## 可直接改写的电商提示词

### 白底商品图

```text
【主体】[商品名称与 SKU]；商品资料确认的颜色、材质和结构为：[填写已核对事实]。
【保留】[列出本次必须呈现的商品细节、标识和包装文字]；不添加资料中没有的配件或功能信息。
【可变】背景为纯白无缝背景；画面中不加入道具。商品与背景交界处保持自然，具体阴影按上架要求处理。
【输出】用途：[商品详情页首图/其他用途]；画幅：[选择工作台支持的比例]；商品居中，四周留白均匀；不添加额外文字。
```

### 场景图

```text
【主体】[沿用已核对的商品资料与 SKU]。
【保留】[颜色、比例、材质、结构、标识与配件等本次需要核对的事实]。
【可变】把商品呈现在[具体环境]中；主光从[方向]照入，色温偏[暖/中性/冷]；背景包含[必要元素]，其余保持简洁。
【输出】用途：[生活方式场景图/广告构图]；画幅：[选择工作台支持的比例]；商品放在[画面位置]，在[左侧/右侧/上方]留出排版空间；不生成未经核对的卖点文字。
```

### 服饰穿戴图

```text
【主体】[服装款式、颜色、面料和已核对的版型信息]。
【保留】领型、袖长、扣子数量与位置、图案、下摆长度及面料外观以参考资料为准，不自行添加装饰。
【可变】由已获授权的成年模特穿着，姿势为[姿势]，背景为[环境]，光线为[方向与质感]。
【输出】用途：[商品穿戴展示]；画幅：[选择工作台支持的比例]；展示范围为[半身/全身]，确保关键服装细节处于画面内。
```

### SKU 系列图

```text
【主体】本次商品为 SKU [编号]，版本差异为[颜色/尺寸/配件等已核对差异]。
【保留】沿用系列共用的版型、镜头角度、背景和光线；本 SKU 的差异只按商品资料呈现。
【可变】仅调整[明确列出的 SKU 差异]，其他画面元素尽量保持一致。
【输出】用途：[系列商品图]；画幅：[选择工作台支持的比例]；主体位置、留白和裁切沿用已验收样张。
```

更多按图型整理的中英提示词见[电商提示词模板库](../prompts/README.md)；场景图的参考素材分工与验收见[场景融合工作流](03-scene-fusion.md)，带文案主图可参考[促销主图工作流](02-promo-main-image.md)。

## 参考图、迭代与验收

1. 先判断任务是从零构思、改背景、调整构图还是制作 SKU 变体，再选择当前工作台支持的输入方式。
2. 使用有权用于该商品和渠道的图片。若提供多张参考图，为每张图指定单一用途，例如商品外观、场景、材质细节或构图方向；只提供与当前任务有关的素材。
3. 首轮只调整主要可变项。若结果不理想，记录问题所在，再修改一个具体要求，避免一次同时改变商品、场景、镜头和文案。
4. 用相同的商品资料核对主体形状、颜色、结构、标识、包装文字、配件、透视、光线、边缘和画幅。参考图与提示词不一致时，先回到商品资料确认，而不是把生成结果当作商品事实。
5. 对用于上架的文字、规格、功效表述和平台要求进行人工复核。关键商品事实无法确认时暂停使用该图。

可以在团队自己的记录中保存 SKU、提示词版本、参考素材来源、所改变量、输出文件和验收结论。平台是否提供相应的历史记录或素材管理功能，以当前工作台页面为准。

## FAQ

**Q: 四段的顺序必须固定吗？**

A: 不必把它当成模型硬性规则。先写主体和需要检查的商品事实，再写画面变化与输出要求，主要是方便阅读、交接和逐项验收。

**Q: 每张商品图都要上传正面、侧面和细节图吗？**

A: 不需要一概如此。按任务需要和工作台支持的输入方式准备有权使用的素材；如果角度、结构或包装文字会影响本次验收，再补充相应参考资料。

**Q: 提示词能保证商品细节不变化吗？**

A: 不能。提示词只能表达目标，输出仍需与真实商品资料逐项比对；发现结构、标识或文字错误时，不应直接用于上架。

**Q: 图片里的促销文案可以直接交给模型生成吗？**

A: 可以在提示词中说明文案和布局需求，但输出后仍需逐字校对并确认商品事实、促销条件及渠道规则。对精确文案要求高时，可先生成留白画面，再用设计工具排字。

## EN Summary

Organize an e-commerce image prompt into four readable parts: the product, the facts to preserve, the scene or composition that may change, and the requested output. Treat this as a planning and review aid, not a model rule or a guarantee. Use verified product data, authorized references, the options currently available in the chosen interface, and a human review before publishing.

## English Version

Flux Art e-commerce image prompts can be organized into four parts: the product, the product facts to preserve, the visual elements that may change, and the requested output. This structure makes a brief easier to review and reuse; it is not a model rule or a guarantee. Prompt interpretation and available output options vary by model and interface.

**Quick structure:** product facts → details to preserve → scene changes → output requirements.

### 1. Product: describe what can be checked

Use observable product information from the relevant SKU data or approved images. Replace vague mood words such as “beautiful” or “premium” with details that identify the actual item.

| Vague | More checkable |
|---|---|
| A nice-looking cup | A 500 ml straight-sided insulated cup, matte navy body, silver screw lid |
| A premium top | A light beige knitted top, folded collar, three-button placket, hem at mid-thigh |
| A cool sneaker | A low-top white-and-gray sneaker, rubber outsole, black mark on the tongue |

These are writing examples, not product specifications. Confirm capacity, dimensions, color, construction, and marks against the actual SKU. Do not guess missing details.

### 2. Preserve: list product facts that should remain

Name the details that affect product identification or a purchase decision instead of writing only “keep the product unchanged.” Depending on the task, list color, proportions, material appearance, logo position and wording, fasteners, ports, packaging, or included accessories.

```text
Preserve: the matte navy body, straight-sided proportions, silver screw lid, and the position and verified wording of the white vertical mark on the lower-middle part of the cup. Do not add accessories or features that are not in the supplied product information.
```

### 3. Change: define the creative choices

State what may change and how. Common variables include the setting and background, light direction and softness, camera angle, subject placement, negative space, crop, and overall visual mood. If the task is a background change only, say so explicitly and review edges, perspective, contact surfaces, and product details afterward. A prompt states an intent; it does not ensure that every detail will be followed.

### 4. Output: describe the deliverable without assuming controls

State the intended placement, an aspect-ratio option currently offered in the interface, the subject’s position, required negative space, and whether text should appear in the image. If the selected tool offers resolution or other output controls, choose from the options actually shown. Do not assume every model supports the same ratio, resolution, or parameter.

For promotional text, verify the wording and product claims first. Proofread generated text character by character and make sure it does not obscure the product. When exact copy matters, request clear space and add reviewed text in a design tool.

### Reusable prompt templates

#### White-background product image

```text
[PRODUCT] [name and SKU]; verified color, material, and construction: [facts from the product record].
[PRESERVE] [details, marks, and packaging wording that must be checked]; do not add accessories or features absent from the source information.
[CHANGE] Use a seamless white background and no props. Keep the product-background transition natural; handle shadows according to the intended listing use.
[OUTPUT] Placement: [listing lead image / other use]; aspect ratio: [choose an option available in the interface]; center the product with even margins; add no extra text.
```

#### Lifestyle scene

```text
[PRODUCT] Use the verified product information and SKU [SKU].
[PRESERVE] [list the facts that matter for this image].
[CHANGE] Place the product in [specific setting]. Light comes from [direction] with a [warm / neutral / cool] tone. Include [necessary elements] and keep the rest of the background simple.
[OUTPUT] Use: [lifestyle image / campaign composition]; aspect ratio: [available option]; place the product at [position] and leave copy space on [side / top]. Do not create unverified selling-point text.
```

#### Apparel-on-model image

```text
[PRODUCT] [garment type, color, material, and verified fit details].
[PRESERVE] Keep the collar, sleeve length, button count and placement, pattern, hem length, and fabric appearance consistent with the reference information; do not add decoration.
[CHANGE] Show the garment on an authorized adult model, in [pose], against [setting], with [light direction and quality].
[OUTPUT] Use: [apparel product display]; aspect ratio: [available option]; show [half-body / full-body] framing and keep the key garment details in view.
```

#### SKU series

```text
[PRODUCT] This is SKU [ID]. The verified variant difference is [color / size / included part].
[PRESERVE] Keep the shared product construction, camera angle, background, and lighting consistent with the approved series reference.
[CHANGE] Change only [listed SKU differences]; keep other visual elements as close to the approved reference as practical.
[OUTPUT] Use: [series listing images]; aspect ratio: [available option]; follow the approved sample for subject position, spacing, and crop.
```

See the [bilingual e-commerce prompt library](../prompts/README.md) for more image-type templates. For reference-image roles and review points, see the [scene-fusion workflow](03-scene-fusion.md); for a hero image with copy, see the [promotional main-image workflow](02-promo-main-image.md).

### References, iteration, and review

1. Identify whether the task is a new concept, a background change, a composition adjustment, or a SKU variant, then use an input method supported by the current interface.
2. Use images you are authorized to use. When supplying multiple references, assign each one a single role—such as product appearance, setting, material detail, or composition—and include only what the task needs.
3. Change the main visual variable first. If the result misses the brief, record the specific issue and revise one requirement at a time instead of changing the product, scene, camera, and copy all at once.
4. Compare the output with the verified product record: shape, color, construction, marks, package wording, accessories, perspective, light, edges, and framing. If the prompt, reference, and product record conflict, confirm the source information before continuing.
5. Manually review copy, specifications, benefit statements, and channel rules before using an image in a listing. Pause when a material product fact cannot be verified.

Your team can keep its own record of the SKU, prompt version, reference-source permissions, changed variables, output file, and review decision. Availability of platform history or asset-management features depends on the current interface.

### Frequently Asked Questions

**Question: Must the four parts always stay in this exact order?**

Answer: No. Treat the sequence as a readable brief, not a model constraint. Putting product facts and review criteria first helps people hand off and check the task.

**Question: Do I always need front, side, and detail photos?**

Answer: No. Provide authorized references that are relevant to the task and accepted by the current interface. Add an angle or detail when it is needed to verify the product.

**Question: Can a prompt guarantee that product details will remain unchanged?**

Answer: No. A prompt communicates the goal, but the output still needs to be checked against the product record before publication.

**Question: Can I ask the image model to render promotional copy?**

Answer: You can describe the wording and layout, but proofread the result and verify every claim and channel requirement. For exact copy, generate an image with clear space and add reviewed text in a design tool.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
