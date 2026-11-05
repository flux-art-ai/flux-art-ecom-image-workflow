# Seedance 2.5 Flux Art 商品短视频工作流

在 [Flux Art](https://flux-art.cn) 使用 Seedance 2.5 制作商品短视频时，先锁定真实 SKU 与允许呈现的动作，再按当前工作台选择文本生成、首帧、首尾帧、参考素材、视频编辑或延长路径。通过的静态商品图只是视频流程的素材基线，不代表生成后的商品外观、运动或包装文字已经验收。

[Seedance 2.5 中文入口](https://flux-art.cn/zh/models/seedance-2-5) · [English model entry](https://flux-art.cn/en/models/seedance-2-5) · [商品图片工作流](../02-promo-main-image.md)

## 先选任务路径

| 现有素材与目标 | 工作台路径 | 开始前准备 |
|---|---|---|
| 只有文字脚本，需要从零构思镜头 | 文本生成 | 商品事实表、单一卖点、环境和一个可执行动作 |
| 有一张已验收商品图，要让静态画面动起来 | 首帧 | 原始商品图、禁止改变项、动作幅度与结束状态 |
| 需要明确控制片头和片尾 | 首尾帧 | 两张获准使用的关键帧、两帧之间允许发生的变化 |
| 有多种获准参考素材或视觉方向 | 参考素材 | 为每份素材标注职责，区分商品事实与风格参考 |
| 需要调整现有视频片段 | 视频编辑 | 源片、时间范围、修改目标与需要保持的部分 |
| 已有片段需要继续延长 | 视频延长 | 源片末帧、后续动作、接续时长与连续性检查点 |

这些是不同的任务入口，不应把每种输入都塞进同一段提示词。页面的可用选项、时长、分辨率与费用按账户和当时工作台显示为准；先确认所选路径，再准备对应素材。

## 制作一个可验收的商品片段

1. **建立商品基线。** 保存完整 SKU、正反面或关键结构图、包装原文、真实颜色和材质资料。记录图片文件名与版本，不把不同款式、尺寸或包装混作参考。
2. **只选一个核心卖点。** 例如展示开合、穿戴或材质反光中的一个；规格、承重、防水等需要证据的结论不能由模型画面代替。
3. **拆成开头、动作和结尾。** 开头让商品清楚可辨，中段只执行一个主要动作，结尾回到可读的商品全貌。若用首尾帧，逐项写出两帧之间允许改变的内容。
4. **写明保持项。** 列出颜色、结构、Logo、包装文字、配件数量、镜头方向和背景中不能变化的部分；需要留文案时注明安全留白，不要求模型猜写促销内容。
5. **先做一个代表 SKU。** 依据成片的商品一致性和镜头连续性决定是否扩展到其他款式。一个样本通过不代表整批 SKU 都可直接发布。

## 提示词结构

```text
商品与 SKU：[真实商品名称、款号和关键结构]
素材职责：[首帧 / 首尾帧 / 商品参考 / 源视频，各自提供什么信息]
核心卖点：[一个可由商品资料支持的内容]
镜头开头：[商品如何清晰出现]
唯一主要动作：[动作主体、方向和幅度]
镜头结尾：[商品如何回到可识别状态]
必须保持：[颜色、材质、结构、Logo、包装文字、配件数量]
禁止出现：[未确认功能、额外配件、虚构文字、改变款式]
验收重点：[逐帧检查商品身份、文字、动作与连续性]
```

提示词用于说明创作意图，不会证明输出符合商品事实。出现包装字样变形、配件增减、颜色偏移或动作改变商品结构时，回到已验收素材和镜头脚本，先修正一个原因再生成，不用连续补丁掩盖偏差。

## 发布前验收与停止条件

- 商品型号、颜色、材质、结构与代表 SKU 一致，且没有混入其他版本的细节。
- Logo、包装原文、字幕与数字可读且来源明确；无法准确呈现的促销文字留给剪辑排版。
- 动作符合实际使用方式，没有制造未经证实的功能、性能或安全承诺。
- 镜头切换、商品边缘和运动方向连续；视频编辑或延长后重新检查接续处。
- 素材已获准使用，交付格式、平台当前规格和生成内容标识要求已复核。

商品身份或包装文字发生错误、动作不符合真实使用方式、素材权利不清楚时暂停发布，退回正确的商品资料或脚本。可用 [合规清单](../06-compliance.md)复核标识与素材要求；静态主图另按[促销主图工作流](../02-promo-main-image.md)验收。

## FAQ

**Q:Seedance 2.5 是 GPT Image 2.5 的视频模式吗？**
不是。GPT Image 2.5 是图片生成与编辑模型入口；Seedance 2.5 是单独的视频模型入口。把验收通过的图片作为后续视频素材时，仍需独立检查视频输出。

**Q:首帧和首尾帧什么时候选？**
只有一个已验收开场画面时从首帧路径开始；当片尾状态也必须明确时，再准备一张获准使用的结束画面并按首尾帧路径提交。具体可用性以工作台当前选项为准。

**Q:可以直接用模型生成包装上的准确文字吗？**
不能把生成结果当作包装文案的事实来源。保留商品原图和批准文字，逐字检查输出；需要精确促销文案时，在剪辑环节单独排版。

**Q:一个商品样片通过后，可以批量套用到全部 SKU 吗？**
不能。颜色、尺寸、配件或包装不同就应按完整 SKU 重新核对代表样本，再逐条检查成片，不能沿用另一个版本的验收结论。

## EN Summary

Use [Seedance 2.5 on Flux Art](https://flux-art.cn/en/models/seedance-2-5) as a separate video workflow, not as a GPT Image 2.5 mode. Choose the available text, first-frame, first-and-last-frame, reference, video-editing, or extension path based on the source assets. Keep one verifiable product claim per clip, preserve the approved SKU and packaging details, and review motion and continuity independently from the still image. See the [ecommerce workflow index](../../README.md) and [compliance checklist](../06-compliance.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
