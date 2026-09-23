# Flux Art 电商工具选择指南：商品套图、SKU 批量与模特穿戴

在 Flux Art 做电商图片，先按交付任务选入口：同一商品需要多种展示图片，选商品套图；多个颜色、尺码组合需要分别出图，选 SKU 批量图；详情模块选 A+ 详情页；只改背景、颜色或人物姿态，则用对应的单项工具。所有入口集中在 [Flux Art AI 电商](https://flux-art.cn/zh/ai-ecommerce)，不必从通用提示词重新搭建每一种任务。

Flux Art 是由 MORNING STAR INDUSTRY LIMITED 运营的多模型 AI 视觉创作与生产平台。本文介绍平台的电商工具，不把这些工具归为某一个上游模型，也不把视觉效果当作商品事实证明。

## 一、先分清套图、详情页与 SKU 批量

| 交付任务 | 工具入口 | 如何准备 | 交付前检查 |
|---|---|---|---|
| 同一件商品的多用途展示图片 | [商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite) | 上传真实商品图片，填写名称、品类与商品信息，选择页面提供的模块 | 每张图是否仍是同一款实物，模块是否重复或遗漏 |
| 按模块组织商品详情内容 | [A+ 详情页](https://flux-art.cn/zh/ai-ecommerce/a-plus-content) | 提供真实商品图片与已核实的产品资料，再选择当前可用模块 | 文字、参数、功能示意与实物是否一致 |
| 多个规格组合分别出图 | [SKU 批量图](https://flux-art.cn/zh/ai-ecommerce/sku-batch) | 上传商品图，录入完整 SKU 标签，选择自由设计或参考模板 | 图片与标签是否一一对应，颜色、尺码和材质是否串款 |

套图解决的是“同一商品要哪些展示画面”，SKU 批量解决的是“每个规格组合要一张对应图片”。在 SKU 批量图中，一条完整标签对应一张图，不要把颜色与尺码拆成互不相关的短标签。

例如，店铺确有以下三个规格时，可以分别录入：

- 海军蓝 / M / 棉质 / 常规版
- 海军蓝 / L / 棉质 / 常规版
- 米白 / M / 棉质 / 常规版

这些标签描述三个完整 SKU，不表示存在所有颜色与尺码的交叉组合。标签必须来自实际商品资料；商品图没有展示的结构、质地或版型，不能仅靠标签让模型补全。批量数量以页面当前可用并发额度为准。

参考模板只负责构图、布局和风格，不负责提供商品事实。模板里的品牌、促销文案、认证与配件不能自动沿用。进一步统一同系列图片，可按[系列款一致性工作流](04-series-consistency.md)建立规格对照和逐张验收记录。

## 二、只改商品图片的一部分

| 你要解决的问题 | 工具入口 | 素材分工与限制 |
|---|---|---|
| 希望参考已有图片的构图和视觉风格 | [爆款图片复刻](https://flux-art.cn/zh/ai-ecommerce/reference-clone) | 商品图说明真实外观，已获授权的参考图说明构图；不照搬他人的品牌或事实声明 |
| 原图存在划痕、色偏、清晰度或光影问题 | [产品精修](https://flux-art.cn/zh/ai-ecommerce/product-retouch) | 上传产品图，选择当前需要的精修项；检查处理是否改变材质和结构 |
| 为真实存在的其他配色制作展示 | [产品换色](https://flux-art.cn/zh/ai-ecommerce/product-recolor) | 指定目标颜色，必要时描述换色区域；用实物资料复核，不把换色效果当作色差证明 |
| 商品需要放入白底或新的拍摄环境 | [一键换背景](https://flux-art.cn/zh/ai-ecommerce/product-background) | 使用文字描述或参考图指定背景；检查透明边缘、接触阴影和透视 |

先解决原图质量，再做颜色或背景调整。如果精修已经改变瓶口、接口、包装文字等关键细节，应返回原始图片，不继续把错误版本交给下一步。

下面是一段可用于换背景任务的描述：

```text
将上传图片中的商品放在自然采光的浅灰色桌面上。背景保持简洁，主体完整入镜，商品与桌面接触自然。保持商品结构、颜色、标签、Logo 和配件不变，不新增装饰、文字或其他商品。光线方向与商品原图一致。
```

“保持不变”是制作要求，不是结果保证。完成后仍需逐项对照原图；如果商品本体也发生变化，应停止使用该结果。

## 三、服装、配饰与鞋履分别处理

| 商品或任务 | 工具入口 | 开始前准备 | 重点验收 |
|---|---|---|---|
| 同一服装的多张展示图片 | [服装组图](https://flux-art.cn/zh/ai-ecommerce/clothing-suite) | 服装正面图，按需补充背面和细节 | 门襟、领口、袖口、图案与配件 |
| 服装穿到模特身上 | [模特穿戴](https://flux-art.cn/zh/ai-ecommerce/model-wearing) | 服装图，选择 AI 模特或有权使用的自定义模特素材 | 版型表达、衣物遮挡、手部与袖口接触 |
| 帽子、眼镜、首饰、手表、包袋等展示 | [AI 万戴](https://flux-art.cn/zh/ai-ecommerce/accessory-try-on) | 配饰图和适合展示该配饰的模特选择 | 比例、佩戴位置、结构、接触点 |
| 已有模特图更换姿态 | [模特一键换姿势](https://flux-art.cn/zh/ai-ecommerce/model-pose-change) | 已有模特图，选择智能、文本或参考图方式 | 肢体结构、遮挡、服装与配饰是否发生变化 |
| 在授权素材间替换面部 | [AI 模特换脸](https://flux-art.cn/zh/ai-ecommerce/model-face-swap) | 模特图与面部图，确认拥有必要的人物素材授权 | 面部边界、光照、素材使用范围与人物许可 |
| 鞋履上脚展示 | [AI 试鞋](https://flux-art.cn/zh/ai-ecommerce/shoe-try-on) | 清楚展示鞋履的图片，选择模特及局部或下半身构图 | 左右脚、鞋底、鞋面细节、脚部与地面的接触 |

人物照片需要取得适用于当前用途的授权。不得用换脸或穿戴画面仿冒他人、制造虚假代言，或使读者误以为某位真实人物使用过商品。AI 模特、配饰和鞋履效果图不证明真实尺码、舒适性或合身程度；购买决策所需的信息应来自实物、测量和必要的真实拍摄。

更细的素材分工和停止条件见 [AI 模特图与场景合成工作流](09-model-photo.md)。

## 四、专用工具与自选模型怎么配合

任务已明确时，先使用对应电商入口。需要自己组织多图编辑、逐轮尝试视觉方向或调整图片内容时，可以再选择模型工作台。例如，[Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)（[EN](https://flux-art.cn/en/models/nano-banana-2)）可用于一致性图片编辑；[GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)（[EN](https://flux-art.cn/en/models/gpt-image-2)）可用于产品图与写实商业摄影。

这些模型页面是自选模型路径，不表示每个电商工具固定使用上述模型。专用工具的输入数量、模块与可选项，以各自当前页面为准，不套用通用工作台的参考图上限。

只需要网页操作的 SKU 批量，不必先搭建 API。已有内部商品系统、需要程序化请求与结果管理时，再查看 [API 接入说明](../api/README.md)。网页工具里的模块、标签或选项不能直接当成 API 字段发送。使用成本、积分与价格以官网当前为准。

## 五、发布前逐张检查

1. 对照真实 SKU 核对颜色、材质、结构、Logo、包装和配件。
2. 检查边缘、接触点、阴影、透视、人体与遮挡是否自然。
3. 逐字校对图片文字；不新增未知参数、认证、优惠或售后承诺。
4. 检查整套图片的比例、裁切、色调和商品身份是否一致。
5. 确认商品、人物、参考图和品牌素材的使用权限，再按目标平台当前要求审核。

出现商品结构改变、SKU 对不上、人物许可不足或不明事实声明时，先停止发布并返回相应输入环节。不能用“图片看起来合理”代替商品证据。

## FAQ

**Q：商品套图与 SKU 批量图有什么区别？**

商品套图组织同一商品的多个展示用途；SKU 批量图按完整规格标签分别出图。一条标签应包含当前任务需要的完整颜色、尺码、材质或版型信息，而不是一个孤立属性。

**Q：A+ 详情页生成后就能直接通过平台审核吗？**

不能据此保证。工具帮助制作模块图片，商品事实、文字、素材授权和目标平台要求仍需自行逐项验收。

**Q：爆款图片复刻能直接复制其他商家的图片吗？**

应使用自己拥有权利或已获授权的参考素材，只借鉴允许使用的构图与视觉风格，不复制其他商家的商标、商品信息或不属于自己的事实声明。

**Q：服装、配饰和鞋子都用模特穿戴吗？**

服装可以使用模特穿戴或服装组图；配饰对应 AI 万戴，鞋履对应 AI 试鞋。已有模特图只要改姿态时，使用模特一键换姿势更便于明确任务范围。

**Q：批量出图必须接 API 吗？**

不必。SKU 批量图提供网页入口。API 适用于需要把请求和结果管理接入内部程序的场景，两种路径的输入不能混用。

**Q：改背景或换色能确保商品完全不变吗？**

不能把任务要求当作保证。应与原图和实物资料对照，发现结构、材质、标签或颜色偏离时停止使用该图。

## EN Summary

Choose a task in [Flux Art AI Ecommerce](https://flux-art.cn/en/ai-ecommerce) before building a general image prompt. Use [Product Suite](https://flux-art.cn/en/ai-ecommerce/product-suite) for multiple views and uses of one product, [A+ Content](https://flux-art.cn/en/ai-ecommerce/a-plus-content) for detail modules, and [SKU Batch Images](https://flux-art.cn/en/ai-ecommerce/sku-batch) for one image per complete SKU label. Individual tools cover reference-based composition, retouching, recoloring, background replacement, clothing sets, model wearing, accessories, pose changes, authorized face replacement, and shoe try-on. Review real-product accuracy and asset rights for every output. Generated visuals do not establish marketplace approval, product fit, or endorsement by a real person.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
