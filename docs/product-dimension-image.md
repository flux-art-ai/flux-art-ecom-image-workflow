# 商品尺寸图怎么做：本体、内腔与包装分开标注｜Flux Art

商品尺寸图要先确认量的是本体、内腔还是包装，再用同一 SKU 的已核准规格和对应角度实拍放尺寸线。在 [Flux Art 商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)（[English](https://flux-art.cn/en/ai-ecommerce/product-suite)）中可选择「规格尺寸图」起稿；数值、单位和测量端点需要另行校对。没有清楚的规格或实测记录时，不从生成图、透视照片或场景参照物估算尺寸。

## 先决定买家需要哪一种尺寸

| 买家要判断什么 | 应展示的尺寸 | 图上怎么标 |
|---|---|---|
| 收纳箱放不放得进柜格 | 商品在正常使用状态下的最大外廓 | 标出最外侧端点，核对外凸的扣件、把手或脚垫是否计入；如果还需要开盖空间，另标开启状态。 |
| 箱内放不放得进一件物品 | 内腔可用范围 | 在开盖俯视或侧视图标清内壁、底部和盖下的测量位置；箱口比底部宽时，不用箱口宽度替代底部可用宽度。 |
| 包裹能否通过取件柜或搬运通道 | 实际发货包装的外部尺寸 | 使用包装图并标「发货外箱」，不要把外箱尺寸放在商品本体照片上。 |

同一款有不同大小或附件时，逐个核对完整 SKU。没有发货包装数据，就不要从本体长宽高加一个经验值作为外箱尺寸。

## 从规格表到成品图

1. **先记录测量对象和状态。** 在规格表写明 SKU、测量对象、朝向、开合状态、两端位置、数值、单位和来源版本。尺寸以批准规格或经复核的实物测量为准；两者有冲突时先确认。
2. **按方向挑视图。** 正视图适合展示横向和高度，侧视或俯视图能更清楚地展示深度或内腔。不要把看不见的背面端点画在透视图里。若三条尺寸线会交叉，拆成两张视图。
3. **让工具做画面，把尺寸留给排版。** 用商品套图生成规格模块候选；只需无字视觉底图时，可尝试 [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)（[English](https://flux-art.cn/en/models/gpt-image-2)）或 [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)（[English](https://flux-art.cn/en/models/gpt-image-2-5)），不让模型填写数字。精确标注优先叠加在未变形、能看清两端的实物照片或核准图稿上；装饰性底图如改变轮廓，只作场景示意，不用来标尺寸。
4. **按发布后的用途复核。** 从规格表逐项对照图片上的数字、单位、对象和端点。在手机上检查箭头有没有被裁掉、读者能不能分清本体与内腔；需要比对尺寸的买家还应能在页面文字中找到这些数值。

例如，如果柜格的前口比内部空间窄，买家先要判断收纳箱是否能从前口放进去。示意图应标出箱体最宽处，不能只标箱底。若读者还要在柜中开盖，另给开盖所需空间或明确提醒核对，别让关闭状态的高度承担两种用途。

制作完整渠道页面时，继续用[详情页资料与交付清单](05-detail-page.md)。如果团队要交换零售商品与外箱的尺寸数据，可参考 [GS1 包装与商品测量标准](https://ref.gs1.org/standards/ppm/)确定各层的测量口径；它不是电商图片模板，也不替代具体渠道要求。

## FAQ

**Q: 能不能让 AI 从一张商品照片读出精确尺寸？**

不要把照片估算值当成商品规格。即使画面有手、硬币或尺子，也可能存在透视、摆放平面不同或局部遮挡。正式标注以批准规格或实物复测为准。

**Q: 图片上应写商品本体还是发货包装的尺寸？**

按读者要做的判断选。使用、摆放和兼容性写对应的商品尺寸；搬运或运输写实际发货包装尺寸。两者都需要时，分别配图并写明测量对象。

**Q: 商品套图生成的尺寸模块有一根线指错了，怎么处理？**

回到测量记录，核对端点对应的是内壁还是外壁。商品画面正确时只重排该条尺寸线和文字；如果底图已变形或端点被遮挡，换为可核验的实物视图。

## EN Summary

To make a product dimension image in [Flux Art](https://flux-art.cn), confirm whether the customer needs the object's outer dimensions, usable interior space, or the shipping package. Use approved measurements for the exact SKU and annotate a photo or approved drawing that shows both endpoints. Draft a specification module with Product Suite if useful, but add and check the actual values and units separately. A generated scene is not measurement evidence.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
