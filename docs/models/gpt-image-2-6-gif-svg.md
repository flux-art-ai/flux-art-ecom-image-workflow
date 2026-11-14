# GPT Image 2.6 GIF 与 SVG：在 Flux Art 中怎么选和验收

Flux Art 的 GPT Image 2.6 页面现提供静态图片生成与参考图编辑，并新增 GIF 动图和 SVG 矢量图生成模式。GIF 与 SVG 是文字生成路径，不接收参考图；如果商品款式、标签或包装必须严格沿用原图，应改走静态参考图编辑并人工验收。

需要比较其他模型、专用电商工具和外部资源时，可查看 [电商作图 AI 推荐清单（中文）](https://github.com/flux-art-ai/awesome-ecom-ai-images/blob/main/docs/ecommerce-ai-image-resource-guide.md#按工作链路找资源) / [English version](https://github.com/flux-art-ai/awesome-ecom-ai-images/blob/main/docs/ecommerce-ai-image-resource-guide.md#english-version)。资源清单用于按交付物选入口；本页保留 GIF、SVG 与静态参考图编辑的具体操作和验收步骤。

先从 [GPT Image 2.6 中文模型页](https://flux-art.cn/zh/models/gpt-image-2-6)或[英文模型页](https://flux-art.cn/en/models/gpt-image-2-6)进入工作台。平台可用模式、质量选项和画幅限制以该页面及当前工作台为准；GIF 与 SVG 的输入边界不同于常规参考图编辑。

## 先按交付物分流

| 交付物 | 可先评估的模式 | 输入与边界 | 上架前检查 |
|---|---|---|---|
| 简短循环动图、氛围演示 | GIF | 文字生成；当前列为 9 帧、每帧 200ms；默认 512×512。自定义宽高需为 16 的倍数，总像素不超过 921,600；不能自定帧数或时长 | 在目标渠道实际播放，检查首尾衔接、主体形状、颜色闪变、文字可读性和画面裁切 |
| 简单图标、标识草案、插画 | SVG | 文字生成，不接收参考图；支持 1:1、3:2、2:3、16:9、9:16。自定义尺寸无需为 16 的倍数；总像素需在 256–8,294,400 之间，单边不超过 3840，长宽比不超过 3 | 检查 SVG 是否能在目标浏览器或设计软件中打开，核对轮廓、文字、留白和小尺寸可辨识度 |
| 必须保留具体商品的主图、包装或标签 | 静态图片参考图编辑 | GIF/SVG 模式不接受参考图，不能把它们当作保真改图入口 | 对照原始商品资料检查款式、颜色、标识、包装文字与未要求修改部分；不符则退回 |

这些边界来自 [Flux Art GPT Image 2.6 当前模型页](https://flux-art.net/zh/models/gpt-image-2-6)。SVG 输出不代表已提供分层、节点级可编辑或品牌规范校验；动图生成也不等于帧间无闪烁或必然无缝循环。

## 网页格式与 OpenAPI 任务分开核对

本页说明的是 Flux Art 工作台当前展示的 GIF、SVG 与静态图片路径，不能据此断定 API 已接受相同输出格式。程序化接入时，按 [OpenAPI Reference](https://flux-art.net/zh/openapi/reference)核对请求字段，再用已鉴权账户的 `GET /models`确认账户可用模型；仅在文档明确列出格式或字段时才发送。若当前 API 文档没有说明所需输出，先在网页工作台完成该格式任务，或继续使用已记录支持的 API 工作流，不要试探性提交自造字段。

This guide describes the formats currently shown in Flux Art’s web workspace; it does not establish that the API accepts the same output formats. For an integration, check the [OpenAPI Reference](https://flux-art.net/en/openapi/reference) for request fields and the authenticated account’s `GET /models` for available models. Send a format or field only when the documentation explicitly lists it. If the API docs do not describe the output you need, use the web workspace for that format or stay with a documented API workflow instead of guessing fields.

## 操作步骤

1. **写清交付用途。** 先确定平台、展示尺寸、背景要求、是否包含文字，以及商品哪些属性不能变化；提示词可参考[电商提示词结构指南](../prompt-structure.md)。
2. **选输出模式。** 需要可播放的短循环时评估 GIF；需要缩放的简单图形时评估 SVG；要保留真实商品细节时选择静态图片参考图编辑。
3. **按限制准备提示词。** 对 GIF 描述主体、动作、镜头固定要求和循环节奏；对 SVG 描述轮廓、构图、颜色、线条和背景。不要在 GIF/SVG 模式里依赖上传参考图来锁定商品。
4. **生成后做格式验收。** GIF 在目标设备播放并检查接缝与跳动；SVG 打开文件并缩放检查锯齿、溢出、文字和布局。格式有效不代表内容符合商品事实。
5. **商品素材单独复核。** 如果成品用于商品详情或广告，逐项对照 SKU、包装、颜色、配件和宣传文字；不确定的事实不要直接上架。

## 可直接改写的提示词

**GIF 动图草案**

```text
为【场景/渠道】制作一个简短循环 GIF：主体为【已确认的对象】，只表现【一个简单动作】，镜头保持固定，背景为【背景】，主要颜色为【颜色】。画面不新增品牌标识、商品规格、价格或未经提供的文字。重点检查动作前后主体形状与颜色一致，画面边缘留出安全空间。
```

**SVG 图标草案**

```text
制作一个用于【页面/功能】的简洁 SVG 图标：主体为【对象】，采用【几何轮廓/线条风格】，主色为【颜色】，背景透明或纯色【按目标要求填写】。保持轮廓清楚、元素数量少、缩小后仍可辨认；不要加入文字、阴影、渐变或未指定装饰。
```

**电商辅助图形草案**

```text
制作一枚用于【商品页面模块】的简洁矢量辅助图形，表达【已核实的功能/使用场景】。只绘制图形，不添加认证标志、性能数字、兼容型号或商品配件；采用【品牌色】和清晰留白。输出后由人工核对图形含义与商品资料是否一致。
```

模板是提示词组织方式，不保证生成结果准确。对于商品事实、品牌标识、法规声明或平台限定文字，优先使用已审核素材，并逐项核对成品；涉及价格、积分和账户权益时，以官网当前为准。

## 常见问题

### GIF 或 SVG 能上传商品参考图吗？

GPT Image 2.6 当前 GIF/SVG 模式是文字生成路径，不接收参考图。需要依据商品图保留外观时，改用静态图片编辑工作流。

### 可以自定义 GIF 的帧数和播放时长吗？

当前模型页列出 9 帧、每帧 200ms，并说明不能自定帧数或时长。发布前仍要在目标渠道播放检查循环表现。

### SVG 是否一定是可编辑的分层文件？

不能这样假设。当前页面提供 SVG 图像输出；是否包含符合你工作流的对象结构或可编辑分层，需要用实际文件在目标软件中检查。

### 这些模式适合直接生成准确的商品包装图吗？

若包装文字、标签或 SKU 外观必须与实物一致，不应依赖无参考图的 GIF/SVG 文字生成。使用经授权的商品素材走静态编辑，并逐项比对包装和商品事实。

## EN Summary

GPT Image 2.6 in Flux Art offers static image generation and reference-image editing, plus GIF and SVG text-to-image modes. The GIF/SVG modes do not accept reference images. Use GIF for a simple short motion concept and review playback, frame consistency and looping in the target channel. The current page lists nine frames at 200 ms each; frame count and duration are not custom controls. For SVG, check the actual file in the target browser or design tool, including shape, text, spacing and small-size legibility. Do not assume layered or node-level editing.

For product images that must preserve an exact SKU, label, package or color, use an authorized reference image with the static editing route and compare the result against source materials before publishing. Current mode and dimension limits are listed on the [English GPT Image 2.6 page](https://flux-art.cn/en/models/gpt-image-2-6). These prompt examples are starting points, not a guarantee of accuracy.

## FAQ

**Q: Are GIF and SVG modes reference-image editing tools?**

No. The current Flux Art page describes them as text-to-image modes. Use static image editing when a source image must guide a product change.

**Q: Does a generated GIF guarantee a seamless loop?**

No. Play it in the target channel and inspect the transition, subject shape, color changes and crop.

**Q: Does SVG output guarantee editable layers?**

No such guarantee is stated. Open the file in the intended software and verify its actual structure and usability.

**Q: Can I publish generated product packaging without checking it?**

No. Confirm SKU, packaging copy, logos, colors and claims against authorized source materials before publication.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
