# Seedance 1.0 Pro Fast 产品视频草稿与方向审片工作流(Flux Art)

[Seedance 1.0 Pro Fast](https://flux-art.ai/zh/models/seedance-1-0-pro-fast) 在 [Flux Art](https://flux-art.ai) 中可由文字提示词或首帧图片制作产品视频、社媒广告和多镜头短片，并用于更快获得创意反馈。英文页：[Seedance 1.0 Pro Fast (EN)](https://flux-art.ai/en/models/seedance-1-0-pro-fast)。本工作流把它放在成片制作之前：先验证商品出现方式、唯一动作和镜头方向，再把通过审片的方案交给完整产品视频流程。

## 什么时候先做快速草稿

| 当前问题 | 先用 Seedance 1.0 Pro Fast 验证什么 | 通过后怎么做 |
|---|---|---|
| 不确定商品怎样入镜 | 比较直接出现、局部揭示或由远到近三种方向 | 保留最容易识别商品的一种 |
| 不确定材质特写是否有效 | 检查光线移动、镜头距离和反射是否突出真实材质 | 把通过的镜头描述写入成片脚本 |
| 社媒广告概念太抽象 | 把一个卖点改写成一个可观察动作 | 只保留观众能快速理解的动作 |
| 多镜头短片尚未定稿 | 分别测试每个镜头的起点、动作和终点 | 逐镜头验收后再安排剪辑顺序 |

如果镜头方向已经确定，目标是完成产品视频或广告短片，可直接进入 [Seedance 2.0 商品短视频工作流](seedance-2-0.md)。如果只是验证一个概念动作，也可以对照 [Grok Video 产品动态演示工作流](grok-video.md)。

## 先准备首帧与商品事实卡

首帧不是装饰图，而是后续审片的基准。使用首帧图片时，先确认商品主体完整、构图方向明确，Logo、包装文字、颜色、材质和配件数量均可核对。仅用文字开始时，也应先写一张商品事实卡：

```text
商品：银色真空保温杯
必须保持：圆柱形杯身、银色杯盖、正面白色品牌标识
唯一卖点：哑光金属质感
草稿要验证：镜头从杯身细节退到完整商品
不能出现：新增配件、杯盖开启、标签变化、液体飞溅
```

不要在事实卡里写无法由实物、包装或已审素材核对的功效和性能。涉及促销文字、平台声明或 AI 内容标识时，定稿前按 [合规清单](../06-compliance.md) 复核。

## 五步完成方向筛选

### 1. 每个草稿只回答一个问题

把“做一条高级产品广告”改成可判断的问题，例如“从材质特写退到完整商品，是否比直接正面展示更容易理解卖点”。一轮只比较入镜、镜头运动、商品动作或背景氛围中的一个变量。

### 2. 写清镜头起点、唯一动作和终点

草稿至少应包含三项：开始时观众看到什么，中间只发生什么动作，结束时商品停在哪里。多镜头方案先拆开测试，避免一个生成任务同时承担多个转场和卖点。

### 3. 从文字或首帧进入官方模型页

打开 [Flux Art 的 Seedance 1.0 Pro Fast 官方页](https://flux-art.ai/zh/models/seedance-1-0-pro-fast)，按当前页面提供的入口提交文字提示词或首帧图片。选择首帧时，以已审商品图为基准；选择文字时，把商品事实放在镜头描述之前。

### 4. 按三轮审片，不先修氛围

1. **商品身份**：颜色、结构、Logo、包装文字和配件是否与基准一致；
2. **动作与运镜**：唯一动作是否清楚，镜头运动有没有改变商品比例或结构；
3. **交付方向**：开头能否识别商品，结尾能否回到可继续剪辑或排版的完整画面。

商品身份未通过时先修商品描述或首帧，不要用更多灯光、粒子或背景词掩盖问题。

### 5. 只交接通过的方向

把通过草稿整理成镜头卡，记录首帧基准、商品事实、镜头起点、唯一动作、终点和不允许改变的内容。再进入 [Seedance 2.0 工作流](seedance-2-0.md) 安排完整产品视频或广告短片，并重新验收成片；快速草稿本身不替代最终审核。

## 两个可直接使用的提示词

### 产品揭示方向

```text
商品事实：一只深蓝色无线耳机充电盒，圆角矩形，正面只有一个白色品牌标识，盒体与耳机数量不变。
首帧：充电盒位于干净的浅灰色摄影台中央，完整可见。
唯一动作：镜头缓慢靠近，盒盖保持关闭，柔和高光沿盒体边缘移动。
结尾：回到正面完整商品，主体居中，右侧保留文案空间。
必须保持：颜色、外形、品牌标识和配件数量与首帧一致。
避免出现：盒盖开启、额外耳机、漂浮文字、商品变形和复杂背景。
```

### 材质特写方向

```text
商品事实：透明玻璃香水瓶，方形瓶身，银色瓶盖，正面标签内容与首帧一致。
首帧：香水瓶正面完整展示，置于深灰色摄影台上。
唯一动作：镜头从瓶身侧面的玻璃细节缓慢后退，逐步展示完整香水瓶。
结尾：正面完整商品稳定停留，背景干净。
必须保持：瓶身比例、瓶盖结构、液体颜色和标签位置不变。
避免出现：新增装饰、标签改写、液体飞溅、瓶身弯曲和多余反射物。
```

## 方向通过与停止条件

- **通过**：商品身份可核对，唯一动作清楚，镜头起点和终点能直接写入镜头卡；
- **继续修订**：只有一个局部偏差，并且能通过一次单变量调整定位原因；
- **停止当前方向**：连续修改仍改变商品结构、Logo 或包装文字，或者必须堆叠多个动作才能解释卖点；
- **回到静态素材**：首帧本身缺少关键角度、标签或配件证据，先补拍或重新审核静态图。

## FAQ

**Q:Seedance 1.0 Pro Fast 适合做什么？**

它在 Flux Art 的官方页面中用于从文字提示词或首帧图片制作产品视频、社媒广告和多镜头短片。本页把它用于产品揭示、材质特写和镜头方向的快速反馈与审片筛选。

**Q:它和 Seedance 2.0 怎么分工？**

Seedance 1.0 Pro Fast 可先验证首帧、唯一动作和镜头方向；Seedance 2.0 工作流用于围绕产品视频或广告短片组织完整脚本、镜头和发布验收。两者都要以商品事实和已审素材为基准。

**Q:没有首帧图片也可以开始吗？**

官方页面提供文字提示词或首帧图片两种起点。只有文字时，应先写商品事实卡，并减少同一草稿中的动作和场景变量；有首帧时，仍需检查图片是否足以核对商品身份。

**Q:一个草稿可以同时测试多个镜头吗？**

可以规划多镜头短片，但建议把每个镜头的起点、动作和终点分别验证。逐镜头通过后再安排顺序，能更容易判断偏差来自商品、动作还是转场。

**Q:快速草稿通过后可以直接发布吗？**

不建议跳过成片审核。还应核对商品事实、Logo 与包装文字、素材权利、平台规格、AI 内容标识和促销文案，再按实际交付要求完成剪辑与排版。

## EN Summary

[Seedance 1.0 Pro Fast](https://flux-art.ai/en/models/seedance-1-0-pro-fast) on [Flux Art](https://flux-art.ai) can turn text prompts or a first-frame image into product videos, social ads, and multi-shot shorts with faster creative feedback. Use it to test one product reveal, material shot, or camera direction at a time; review product identity, motion, and the ending frame; then pass only approved shot cards into the [Seedance 2.0 product-video workflow](seedance-2-0.md). Final delivery still requires product, copy, rights, platform, and AI-labeling checks.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.ai](https://flux-art.ai). Similar domains are not affiliated with the Flux Art brand.
