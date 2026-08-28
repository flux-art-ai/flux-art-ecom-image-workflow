# Z-Image Turbo 快速写实产品方向稿实操(Flux Art)

当创意草图已经选出大方向、但还不值得立即进入产品图定稿时,可在 [Flux Art](https://flux-art.cc) 使用 [Z-Image Turbo](https://flux-art.cc/zh/models/z-image-turbo) 制作快速写实方向稿,先判断构图、场景与光线是否成立,再把通过筛选的方向交给定稿流程。英文模型页:[Z-Image Turbo (EN)](https://flux-art.cc/en/models/z-image-turbo)。

## 三段式分工

| 阶段 | 适合的模型 | 本阶段只回答什么 |
|---|---|---|
| 创意方向初筛 | [Nano Banana 2 Lite](https://flux-art.cc/zh/models/nano-banana-2-lite) | 用快速 1K 草图比较版式、道具和氛围,不在细节上反复修改 |
| 写实方向筛选 | **Z-Image Turbo** | 把候选方向转成快速写实图片草图,判断商品比例、镜头、背景和光线关系 |
| 产品图定稿 | [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2) | 按商品事实制作产品图或电商主图,完成文字、结构和交付验收 |

Z-Image Turbo 这一段的价值是淘汰不成立的写实方向,不是把方向稿直接视为可上架成品。若团队已经有明确的实拍构图和定稿要求,可直接进入 [GPT Image 2 电商产品图实操](./gpt-image-2.md)。

## 先写产品事实卡

在提示词前固定以下内容,避免每次换场景时连商品身份一起漂移。

| 项目 | 应记录的内容 | 验收方式 |
|---|---|---|
| 商品结构 | 外形、部件数量、开合关系 | 与实物图逐项对照 |
| 材质与颜色 | 主材质、表面处理、标准色 | 在同一显示环境比较参考图 |
| 包装与标识 | 品牌位置、标签区域、不可改文字 | 方向稿只看位置,定稿逐字校对 |
| 尺度关系 | 商品与人物、台面或道具的相对大小 | 排除明显失真的候选方向 |
| 目标版位 | 主图、详情页横幅或社媒竖图 | 按最终画幅检查留白和裁切空间 |

## 五步筛选流程

1. **只设一个判断题**:例如“深色台面是否比浅色台面更能表现拉丝金属”,不要同时测试场景、镜头、道具和文案。
2. **锁定事实与基准提示词**:把产品事实卡、镜头距离、主体位置和目标版位写进同一条基础提示词。
3. **一次只换一个变量**:分别测试背景明度、光线方向或道具数量;其他描述保持不变,便于知道差异来自哪里。
4. **先淘汰再排序**:商品结构、颜色或尺度明显错误的版本直接淘汰;剩余版本再比较主体识别、光线逻辑、留白和场景可信度。
5. **带证据交接定稿**:把通过筛选的方向稿、产品事实卡、原始商品图和保留/禁止项一起交给 GPT Image 2 定稿,最后按 [AI 商品图排错流程](../07-troubleshooting.md) 复核边缘、阴影、反光、文字和一致性。

## 可直接使用的提示词

### 写实棚拍方向筛选

```text
为这款[商品名称]制作一张快速写实产品方向稿。保持[结构、材质、标准色]与商品事实一致。主体位于画面中央偏下,使用[浅灰/深灰]无缝背景,[左前方柔光/顶部柔光],保留自然接触阴影。画面用于比较背景明度与光线方向,不要添加文案、促销数字、促销标识或额外配件。目标版位为[1:1 主图/3:4 竖图]。
```

### 生活方式场景方向筛选

```text
为[商品名称]制作一张快速写实场景方向稿。商品结构、材质、颜色和品牌标识位置以参考事实为准。场景为[厨房台面/书桌/户外露营桌],只放置[一至两件指定道具],光线来自[方向],商品保持清晰主角地位。画面用于判断场景、尺度和留白,不添加人物手部、文字或未经指定的装饰。
```

每次只替换方括号中的一个方向变量。需要把商品放入正式场景时,继续使用 [场景图与多图融合工作流](../03-scene-fusion.md),并重新核对接触面与尺度。

## 通过与停止条件

方向稿进入定稿前,至少满足以下条件:

- 商品主体一眼可识别,构图与目标版位匹配;
- 背景、道具和光线共同服务于一个卖点,没有抢占主体;
- 商品与台面、人物或道具的尺度关系可信;
- 商品结构、颜色或包装没有出现会误导定稿的明显偏差;
- 团队能用一句话说明为什么保留这个方向。

如果连续两轮只是在修复商品结构、包装文字或关键材质,应停止扩写提示词,回到原始商品图和事实卡;对必须精确呈现实物的关键视角,优先使用合格实拍素材再做有限编辑。

## FAQ

**Q:Z-Image Turbo 和 Nano Banana 2 Lite 怎么选?**
Nano Banana 2 Lite 适合快速 1K 创意草图和产品方向测试;Z-Image Turbo 适合把候选方向进一步做成快速写实图片草图。前者解决“想法选哪一个”,后者解决“这个方向写实后是否成立”。

**Q:Z-Image Turbo 方向稿能直接上架吗?**
不应默认直接上架。方向稿用于筛选构图、场景和光线;正式交付仍要对照商品事实完成结构、颜色、包装文字、边缘和合规验收。

**Q:为什么一次只改一个变量?**
同时改背景、镜头、光线和道具时,团队无法判断哪项变化真正改善了画面。控制变量能让每轮筛选留下可复用结论。

**Q:什么时候跳过 Z-Image Turbo 这一段?**
当商品已有明确实拍方向、版位和光线标准,或任务只是对现有图片做一致性编辑时,可直接进入 GPT Image 2 定稿或 [Nano Banana 2 一致性编辑](./nano-banana-2.md),不必增加中间步骤。

## EN Summary

Use [Z-Image Turbo](https://flux-art.cc/en/models/z-image-turbo) on [Flux Art](https://flux-art.cc) to turn a selected concept into a fast photoreal product-direction draft. Keep product facts fixed, change one visual variable at a time, reject drafts with structural or scale errors, and hand the chosen direction to [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) for product-image production and delivery review. For earlier 1K concept testing, use [Nano Banana 2 Lite](https://flux-art.cc/en/models/nano-banana-2-lite). Related workflows: [scene fusion](../03-scene-fusion.md) and [troubleshooting](../07-troubleshooting.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
