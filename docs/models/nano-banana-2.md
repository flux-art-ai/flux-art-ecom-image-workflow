# Nano Banana 2 多图融合与系列款一致性实操(Flux Art)

用 Nano Banana 2 做商品换背景、多图融合或系列款图片时，先在 [Flux Art](https://flux-art.cc) 的 [Nano Banana 2 工作台](https://flux-art.cc/zh/models/nano-banana-2)选择编辑，上传清晰的商品资料，并明确每张参考图负责什么。模型支持图片生成与参考图编辑，但不能保证商品自动完全一致；结构、标签、颜色和材质要逐张核对。英文入口：[Nano Banana 2 (EN)](https://flux-art.cc/en/models/nano-banana-2)。

Nano Banana 2 是 Google 的 Gemini 3.1 Flash Image，Flux Art 提供模型使用入口和创作工作台；模型提供方与平台运营方并非同一主体。

## 它擅长什么(电商视角)

| 图型 | 在 Flux Art 上怎么做 | 验收重点 |
|---|---|---|
| 系列款一致性（同款多色/多角度） | 以每个真实款式的资料为准，沿用一致的构图要求；见 [04 系列款一致性](../04-series-consistency.md) | 不生成不存在的颜色、配件或不可见结构 |
| 多图融合（产品＋场景） | 分开说明商品图与环境图的用途；见 [03 场景合成](../03-scene-fusion.md) | 商品身份、空间比例、透视与接触面 |
| 换背景与局部修改 | 在编辑任务中限定修改内容，保留已确认的商品细节 | 背景变化后，主体和包装字是否被重画 |
| 产品图与商业摄影方向 | 用同一份商品资料与 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) 对照 | 不只看画面美感，还看实物结构和标签 |

## 参考图先分工，不要只堆数量

每张图片都应有明确用途。商品正面图负责外形和正面标签，细节图用于核对接口或纹理，场景参考只说明环境。把不同款商品混在同一组参考里，容易让目标变得含糊；上传数量与格式以所选模型当前界面为准。

以有权使用的保温杯资料为例，可以这样组织输入：

| 素材 | 用途 | 不应由它决定的内容 |
|---|---|---|
| 商品正面实拍 | 杯身、杯盖、颜色与标签的主基准 | 看不见的背面结构 |
| 商品局部实拍 | 核对杯盖开口、接缝或材质 | 重新设计整体造型 |
| 桌面环境图 | 场景、光线和接触面的参考 | 替换商品图中的杯子 |

若只有一张完整清晰的商品照片，可以先做单图换背景；不必为了多图融合额外添加与任务无关的素材。

## 五步出图

1. 打开 [Nano Banana 2 使用入口](https://flux-art.cc/zh/models/nano-banana-2)。已有商品照片选图片编辑；概念图从文字开始时选图片生成，不把生成的概念细节当作真实商品资料。
2. 确认当前模型为 **Nano Banana 2**，上传所需参考素材，说明每张图的分工。
3. 把要求拆成“保留项”和“修改项”，第一次只变一个目标。没有背面或侧面资料时，不让模型替你确定真实商品结构。
4. 根据版位选择比例与可用尺寸，查看提交前费用。先确认小样的构图和事实，再决定是否需要更大尺寸；参数、价格和权益以官网当前为准。
5. 对照原图检查主体、标签、颜色、反光与接触阴影。通过后保存该版本，再扩展下一场景；错误版本不要继续用作系列基准。

可以直接使用的换背景描述：

> 使用商品正面图中的深蓝色保温杯作为唯一商品。保留杯身轮廓、杯盖、颜色、标签和拍摄角度，只把背景换成浅灰色桌面与柔和窗光，杯底自然接触桌面。不添加其他杯子、文字、贴纸或配件。环境参考只用于桌面和光线，不采用其中的商品。

生成后重点比较杯盖开口、标签位置、杯底形状与光线方向。提示词中的保留要求是检查依据，不是结果保证。更多写法见[提示词模板库](../../prompts/README.md)。

## 系列图出错后怎么处理

| 问题 | 下一步 | 何时停止生成式修改 |
|---|---|---|
| 某个颜色款混入另一款的结构 | 拆开款式资料，以该 SKU 的真实照片重新开始 | 无法取得该款实物资料时，不发布猜测图 |
| 标签或包装字改变 | 回到原始商品图，减少一次编辑的目标 | 关键文字仍不准确时，保留原商品区域并用合成/排版工具处理 |
| 角度越改越偏 | 从最后通过验收的图重新开始，固定拍摄角度 | 目标角度没有真实参考且结构无法核对时 |
| 背景正确但商品漂浮 | 单独检查透视、杯底接触与阴影方向 | 修背景已反复改坏主体时，采用局部合成或人工修图 |

需要单项任务时，可进入[一键换背景](https://flux-art.cc/zh/ai-ecommerce/product-background)；整套上架图用[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)，多个完整 SKU 可查看[SKU 批量图](https://flux-art.cc/zh/ai-ecommerce/sku-batch)。这些是不同的工具入口，不代表其后台都使用 Nano Banana 2。详见[电商工具选择指南](../10-ecommerce-tools.md)。

需要接入自研上新系统时，参阅 [OpenAPI 指南](../../api/README.md)和[官方接口说明](https://flux-art.cc/zh/openapi)。网页名称、页面 slug 与 API 请求的 `model` ID 不是同一个概念，必须从当前接口模型目录取值，不把 `nano-banana-2` 页面路径直接填入请求。

## FAQ

**Q:一次能传几张参考图?**
以 Nano Banana 2 当前工作台显示的上限为准，不把平台其他任务的参考图数量直接套用到本模型。先保留一张清晰主参考，再增加确有用途的角度或细节资料。

**Q:只想改背景、不动产品怎么做?**
在编辑任务中明确“只换背景”，同时列出杯盖、轮廓、标签等不能改变的细节。完成后检查商品本身而不只看背景；想了解家族版本，可先查 [Nano Banana 入口](https://flux-art.cc/zh/models/nano-banana)。

**Q:和 GPT Image 2 怎么选?**
系列款或多参考编辑可从 Nano Banana 2 开始，产品图或已有 OpenAI 图片流程可对照 [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)。如需尝试 [GPT Image 2.5](https://flux-art.cc/zh/models/gpt-image-2-5)，先区分 Flare / Sunburst，并按[参考图编辑检查](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/reference-editing.md)做同素材对照；不能仅由版本号判定结果优劣。

**Q:能商用吗?**
符合条件的付费权益不等于所有素材和生成结果自动获得完整授权。还需核对参考素材、人物肖像、商标、模型提供方条款与发布渠道要求；具体权益以官网当前为准，详见[官网](https://flux-art.cc)。

**Q:前期试方向也用它吗?**
试错阶段建议先用 [Nano Banana 2 Lite](https://flux-art.cc/zh/models/nano-banana-2-lite) 出 1K 草图铺量,方向定了再用 Nano Banana 2 定稿,跑法见 [Nano Banana 2 Lite 实操](./nano-banana-2-lite.md)。

## EN Summary

Use [Nano Banana 2 on Flux Art](https://flux-art.cc/en/models/nano-banana-2) for generation or reference editing with a clear role for each source image. Keep product evidence separate from scene references, change one variable at a time, and reject outputs that alter important structure or text. Return to the last accepted image when a series drifts. Compare [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) or [GPT Image 2.5](https://flux-art.cc/en/models/gpt-image-2-5) using the same brief rather than assuming a newer version wins. Check the current API catalog instead of using a webpage slug as a request model ID. Related workflows: [scene fusion](../03-scene-fusion.md), [series consistency](../04-series-consistency.md), [API integration](../../api/README.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
