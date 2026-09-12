# 04 · 系列款一致性(Series Consistency, ≤14 参考图)

在 [Flux Art](https://flux-art.cc) 制作系列款图片，可以使用[SKU 批量图](https://flux-art.cc/zh/ai-ecommerce/sku-batch)组织完整商品标签，或用[产品换色](https://flux-art.cc/zh/ai-ecommerce/product-recolor)处理一个已确认商品的配色版本。先建立真实 SKU 清单与共用视觉规则，再逐张核对外观；一组风格相似的图片不代表其中每个商品都准确。

## 原理

商品实拍和规格表负责定义商品，风格参考只负责画面构图、光线与留白。需要模型工作台时，可评估 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)（[EN](https://flux-art.cc/en/models/nano-banana-2)）的一致性图片编辑；[Nano Banana](https://flux-art.cc/zh/models/nano-banana)是另外的模型版本。模型工作台的参考图范围不能直接套用到 SKU 批量工具。

## 参考集怎么建

| 素材 | 内容 | 作用 |
|---|---|---|
| 必备商品资料 | 当前 SKU 的实拍、颜色、尺码、材质和版型 | 定义必须真实呈现的商品 |
| 可选视觉模板 | 已获授权、构图清楚的风格参考 | 仅用于构图、排版与视觉方向 |
| 共用要求 | 拍摄角度、商品位置、背景与禁用元素 | 定义全批次统一的检查标准 |

## 网页 SKU 批量图

[SKU 批量图](https://flux-art.cc/zh/ai-ecommerce/sku-batch)当前提供商品图、AI 自由设计或参考模板、完整 SKU 标签与统一补充要求。一个完整标签对应一张图，数量以当前可用并发为准；模板控制构图、排版与风格，不替代商品资料。

1. 上传真实商品图，确认品名与素材是否覆盖实际商品。
2. 每个标签写一个完整 SKU，例如“雾蓝 M 码棉质直筒”，不要把颜色、尺码分成互不关联的单项。
3. 选择自由设计或有权使用的模板，将全批共用的拍摄与背景要求统一填写。
4. 提交前查看实际批次数量、选项和费用；参数与价格以官网当前为准。
5. 将每张结果与对应标签和原始商品资料对照。尺码标签可以标识版本，但图片本身不能证明实际尺寸或穿着效果。

只修改现有商品的颜色时，使用[产品换色](https://flux-art.cc/zh/ai-ecommerce/product-recolor)填写目标颜色及区域；需要一组商品展示模块时则进入[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)。三种任务不要混为同一种批量功能。

## 建立 SKU 文件映射表

生成前先为每个完整 SKU 分配一个稳定标识，下载后再把图片用途和版本追加到文件名。这样可以在返修时找到正确原图，也能避免把同色但不同容量、尺码或配件的商品混在一起。

| SKU 记录 | 输出文件示例 | 验收状态怎么记 |
|---|---|---|
| `cup-blue-500ml` | `cup-blue-500ml-hero-v01.webp` | `review`：等待核对商品与文字 |
| `cup-blue-500ml` | `cup-blue-500ml-hero-v02-fix-label.webp` | `review`：本轮只返修标签区域 |
| `cup-blue-500ml` | `cup-blue-500ml-hero-v03-approved.webp` | `approved`：按当前团队清单通过，可进入交付 |
| `cup-blue-750ml` | `cup-blue-750ml-hero-v01.webp` | 单独验收，不能沿用 500ml 的结论 |

映射表至少记录完整 SKU、原始商品图、输出文件、图片用途、所用入口、修改要求、版本和验收结论。使用模型工作台时，可记录 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)、[GPT Image 2.5](https://flux-art.cc/zh/models/gpt-image-2-5) 或 [Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2) 及实际选择；2.5 应再区分 Flare / Sunburst。使用网页 SKU 批量图时记录工具名称，不把它猜成某个底层模型。

`approved` 只是团队的当前交付状态，不代表平台审核或商品事实自动正确。返修后版本号递增，并重新检查整张图片；不要覆盖最后一个已通过版本。

## 批量流程("三固定一变量")

1. 在模型工作台固定所选模型、目标比例与画面要求；可评估 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)（[EN](https://flux-art.cc/en/models/gpt-image-2)）制作产品图，或使用 Nano Banana 2 编辑已有素材。
2. 为每个 SKU 提供它自己的商品事实与图片，不只替换品名而沿用其他款的外观。
3. 对局部问题逐区修改，修改后检查整图；关键结构已经改变时回到原图，不继续微调错误底稿。
4. 只有通过商品与视觉检查的图片才作为后续参考；需要程序化任务管理时阅读 [OpenAPI 文档](../api/README.md)，网页 SKU 字段不是 API 字段。

## 提示词模板

```text
以上传的新品实拍为商品依据，采用另一张已授权参考图的浅灰背景、平视构图与顶部留白。保留新品本身的颜色、材质、轮廓、包装文字和配件数量，不把风格参考中的商品、商标或装饰复制过来。
```

## 验收清单

- [ ] 九宫格预览:新旧图混排看不出"两批人做的"
- [ ] 主体颜色/材质与实物一致(避免售后纠纷)
- [ ] 系列内文字层级(标题字号/位置)统一

## FAQ

**Q：批量做 SKU 图片一定要接 API 吗？**

不需要。网页已有 SKU 批量图入口；需要接入自己的系统、管理任务记录与重试时，再选择 OpenAPI。

**Q：SKU 标签可以只写颜色吗？**

应写清实际需要区分的完整版本，包括必要的颜色、尺码、材质或版型。标签与原始资料必须对应，不能靠模型猜测不存在的款式。

**Q：产品换色能代替实际配色照片吗？**

换色可以用于制作颜色方向或在售配色的候选视觉，但不能证明实物色差、材质或成色。正式展示前仍需按真实样品核对。更多任务见[电商工具选择指南](10-ecommerce-tools.md)。

## EN Summary

Flux Art [SKU Batch Images](https://flux-art.cc/en/ai-ecommerce/sku-batch) is a browser workflow where each complete SKU label corresponds to one image. Use [Product Recolor](https://flux-art.cc/en/ai-ecommerce/product-recolor) for a color-edit task and [Product Suite](https://flux-art.cc/en/ai-ecommerce/product-suite) for multiple listing modules. Keep product evidence separate from style references and inspect each variant; labels and generated pictures do not verify real dimensions or fit.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
