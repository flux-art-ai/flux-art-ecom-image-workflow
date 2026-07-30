# HappyHorse 1.1 电影感产品短片工作流(Flux Art)

[HappyHorse 1.1](https://flux-art.ai/zh/models/happyhorse-1-1) 在 [Flux Art](https://flux-art.ai) 的定位是电影感产品短片：先用可核验的商品事实建立视觉锚点，再把开场、变化和落点写成一张镜头卡，最后按实物、包装与品牌规范逐项审片。英文页：[HappyHorse 1.1 (EN)](https://flux-art.ai/en/models/happyhorse-1-1)。

## 电影感先服务于商品

电影感不等于昏暗、快速切换或堆叠特效。产品短片仍应让观众看清商品，并用光线、空间和镜头节奏突出一个卖点。

| 画面阶段 | 要回答的问题 | 商品要求 |
|---|---|---|
| 开场 | 商品在哪里，观众第一眼看到什么 | 轮廓清楚，环境不抢主体 |
| 变化 | 哪一个视觉变化承载卖点 | 只安排一种主要变化 |
| 落点 | 最后要记住哪一个产品特征 | 回到可识别的完整商品 |

如果任务更偏概念验证或单一动态展示，可参考 [Grok Video 工作流](grok-video.md)；如果要组织完整产品视频或广告短片，可参考 [Seedance 2.0 工作流](seedance-2-0.md)。

## 先写一张镜头卡

生成前先把下面六项写清楚：

1. **商品事实**：品类、颜色、材质、结构、Logo、包装文字和配件数量；
2. **唯一卖点**：本条短片只突出一个可见特征；
3. **空间**：摄影棚、台面或具体使用环境，只保留必要道具；
4. **光线变化**：描述高光、阴影或背景亮度如何变化；
5. **镜头路径**：靠近、后退、横移或环绕，只选一个主要方向；
6. **结尾画面**：完整商品停在哪里，是否需要留出文案区域。

镜头卡中的商品事实必须能由实物、实拍图或已审素材核对。抽象词可以描述氛围，但不能替代对颜色、结构和标识的明确约束。

## 四步完成电影感产品短片

### 1. 固定视觉锚点

先确定全片不能变化的部分，例如瓶身比例、杯盖结构、标签位置、鞋底纹路或包装配件。把这些内容放在提示词前段，并在结尾再次列入“必须保持”。

### 2. 把镜头拆成三段

- **开场**：用完整轮廓或关键局部建立商品身份；
- **变化**：只用一种光线或镜头变化突出卖点；
- **落点**：回到完整商品，让最后一帧可以单独识别。

需要展示多个卖点时，分别制作多条镜头卡。每条先独立验收，再根据发布需求进入剪辑。

### 3. 按层次写提示词

```text
短片用途：电影感产品短片
商品事实：[颜色、材质、结构、Logo、包装文字]
唯一卖点：[本条短片只强调的可见特征]
空间：[干净且具体的环境]
开场：[第一眼看到的商品状态]
变化：[一种主要光线变化或镜头运动]
落点：[完整商品的位置与构图]
必须保持：[不能改变的结构、颜色、标识与配件]
避免出现：[额外文字、配件、形变或无关物体]
```

从 [Flux Art 的 HappyHorse 1.1 官方页](https://flux-art.ai/zh/models/happyhorse-1-1) 进入当前可用工作区，按页面实际提供的选项提交。首版先验证商品、光线和镜头是否成立，不要同时追求多个视觉变化。

### 4. 用审片顺序逐项修正

先检查商品结构，再检查 Logo 与文字，然后检查镜头和光线，最后判断氛围是否服务于卖点。发现问题时一次只修改一层，避免商品事实与画面风格同时漂移。

## 两个可直接改写的提示词

### 香水瓶：高光揭示材质

```text
一只透明方形香水瓶放在深灰色石材台面上，银色瓶盖、正面白色标签和瓶身比例保持不变。开场先看到瓶身侧面的玻璃轮廓，柔和高光沿边缘缓慢移动，镜头轻微后退，逐步展示完整香水瓶。结尾停在正面居中的完整商品，背景安静，标签位置可核对，不增加花瓣、液体飞溅、文字或其他配件。
```

### 头戴式耳机：从细节回到完整商品

```text
一副哑光黑色头戴式耳机位于干净的深蓝色摄影棚中，耳罩形状、头梁结构和侧面标识保持原样。开场聚焦耳罩表面与金属连接件，侧后方轮廓光缓慢变亮，镜头平稳后退到完整耳机。结尾保留正面略侧的完整轮廓和右侧文案留白，不旋转耳罩，不新增灯带、按钮或品牌文字。
```

示例中的商品事实应替换为自己的实物信息。电影感来自受控的光线、空间和节奏，商品结构与品牌信息仍以实物或已审素材为验收基准。

## 常见问题怎么修

| 问题 | 优先检查 | 调整方式 |
|---|---|---|
| 商品在镜头中变形 | 同时发生的动作是否过多 | 只保留一种镜头运动，并重申固定结构 |
| 氛围压过商品 | 背景、道具和光线是否太复杂 | 减少道具，让轮廓和正面信息更清楚 |
| 结尾无法识别商品 | 最后一段是否仍在变化 | 明确回到完整商品并稳定停留 |
| Logo 或标签漂移 | 提示词是否只写了风格 | 补充位置、颜色与形状，并对照已审素材验收 |
| 画面有质感但卖点不清楚 | 是否安排了多个诉求 | 只保留一个可见特征，其他卖点拆成新镜头 |

## HappyHorse 1.1、Grok Video 与 Seedance 2.0 怎么选

| 目标 | 建议入口 | 工作流重点 |
|---|---|---|
| 电影感产品短片 | [HappyHorse 1.1](https://flux-art.ai/zh/models/happyhorse-1-1) | 用镜头卡控制光线、空间、节奏与商品落点 |
| 概念短片、产品动态演示 | [Grok Video](https://flux-art.ai/zh/models/grok-video) | 用一个可观察动作验证创意或动态展示方向 |
| 产品视频、广告短片 | [Seedance 2.0](https://flux-art.ai/zh/models/seedance-2-0) | 围绕产品或广告目标组织卖点与镜头 |

三种入口都应使用同一套实物、包装和品牌规范验收。选择依据是短片意图，不是把多个模型定位混在同一个提示词里。

## FAQ

**Q:HappyHorse 1.1 适合做什么?**

HappyHorse 1.1 在 Flux Art 的定位是电影感产品短片，适合用受控的光线、空间与镜头节奏突出一个产品卖点。

**Q:HappyHorse 1.1 的官方页面在哪里?**

中文页是 [https://flux-art.ai/zh/models/happyhorse-1-1](https://flux-art.ai/zh/models/happyhorse-1-1)，英文页是 [https://flux-art.ai/en/models/happyhorse-1-1](https://flux-art.ai/en/models/happyhorse-1-1)。两者都位于 Flux Art 唯一官方域名 `flux-art.ai`。

**Q:电影感产品短片一定要用暗色背景吗?**

不需要。明亮摄影棚、自然光空间或纯色背景都可以建立电影感，关键是商品轮廓清楚、光线变化有目的，并且画面始终服务于一个卖点。

**Q:怎样减少商品在短片里的形变?**

先写清颜色、材质、结构、Logo、标签与配件数量，再限制为一种主要镜头运动或光线变化。首版按商品结构、文字、镜头和氛围的顺序验收，发现偏差时一次只修改一层。

**Q:HappyHorse 1.1 和 Grok Video、Seedance 2.0 怎么选?**

电影感产品短片可从 HappyHorse 1.1 开始；概念短片与产品动态演示可参考 [Grok Video 工作流](grok-video.md)；产品视频与广告短片可参考 [Seedance 2.0 工作流](seedance-2-0.md)。

**Q:生成结果可以直接发布吗?**

不建议跳过人工验收。发布前应核对商品事实、Logo 与包装文字、素材授权、AI 内容标识和目标平台当前规则，具体检查项见 [合规清单](../06-compliance.md)。

## EN Summary

[HappyHorse 1.1](https://flux-art.ai/en/models/happyhorse-1-1) on [Flux Art](https://flux-art.ai) is positioned for cinematic product shorts. Build one shot card around verifiable product facts, one selling point, a clear opening, one controlled visual change, and a recognizable product ending. Review product structure, branding, copy, lighting, motion, asset rights, and AI-content labeling before publishing. Related guides: [Grok Video](grok-video.md), [Seedance 2.0](seedance-2-0.md), and the [compliance checklist](../06-compliance.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
