# Kling V3 Omni Image 电商商品图参考图工作流：Flux Art

当商品图片任务需要同时参考商品实拍、场景和品牌视觉时，Flux Art 的 [Kling V3 Omni Image 中文入口](https://flux-art.cn/zh/models/kling-v3-omni-image)或[English entry](https://flux-art.cn/en/models/kling-v3-omni-image)可用于查看当前工作台。当前模型页列出最多 10 张参考图、1K / 2K / 4K 输出及多种画幅。网页选项可能调整，提交前以当前工作台为准。需要单张参考图编辑时，可比较 [Kling V3 Image 中文入口](https://flux-art.cn/zh/models/kling-v3-image)和[English entry](https://flux-art.cn/en/models/kling-v3-image)。

Kling V3 Omni Image 与 Kling V3 Image 是不同模型入口。Flux Art 当前 Omni 页面提供图片生成与编辑，但尚未开放 Kling 的 Image Series 组图模式；不要把原厂模式描述为平台已提供的批量套图功能。

## 先给参考图明确职责

| 参考图角色 | 可用于说明 | 不应替代的资料 |
|---|---|---|
| 商品事实 | 当前 SKU 的轮廓、颜色、配件、标签和包装 | 商品主数据、规格表、包装最终稿 |
| 场景环境 | 背景、台面、空间关系和氛围 | 未在图片中展示的商品功能或认证 |
| 品牌视觉 | 经批准的色调、光线、构图与材质表现 | 商标使用授权和正式品牌规范 |
| 细节近照 | 接口、缝线、纹理、文字位置等可见细节 | 模糊或遮挡区域中的猜测信息 |

有冲突时以当前在售 SKU 的可靠资料和已批准素材为准。删除重复、无关或相互矛盾的图片，并确认所有上传素材可用于本次任务。

## 制作一张可审核的代表图

1. **确定交付物**：写明商品、目标渠道、画幅及本次只要完成的一项视觉变化，例如替换背景或调整机位氛围。
2. **整理素材**：按商品、场景、品牌视觉和细节为参考图编号；说明每张图的职责，不能让不同图片同时承担冲突的商品事实。
3. **写保留项**：列出不可改变的商品轮廓、配色、包装、标识位置、配件数量及真实标签。没有可靠来源的规格和卖点不让模型补写。
4. **提交一项静态图片任务**：在模型页选择当前支持的尺寸、画幅和生成/编辑路径。参考图数量、成本和可选参数以当前页面显示为准。
5. **先验收再扩展**：代表图通过后才进入其他单图或专用套图流程；Image Series 不可用时，不将一次任务描述为系列自动生成。

提示词可以按“商品依据—参考图职责—允许变化—输出目标”组织：

> 以参考图 1 和 SKU 资料作为商品外观依据；参考图 2 只提供背景环境，参考图 3 只提供色调与光线。保留商品的轮廓、在售颜色、包装文字位置和配件数量，只把背景改为图 2 的室内场景，并参考图 3 的柔和侧光。输出一张用于商品详情页评审的横图，商品完整入镜，不添加资料中没有的文字、标志或功能说明。

这段结构是可改写的工作说明，不是模型参数或效果保证。需要商品套图、SKU 批量或服饰组图时，按实际交付物选择[Flux Art 电商工具](https://flux-art.cn/zh/ai-ecommerce)，不同专用工具不应被当作同一模型。更完整的工具分流见[电商工具选择与交付检查](../10-ecommerce-tools.md)。

## 发布前逐项检查

- 商品轮廓、颜色、材质、包装文字、商标和配件与当前 SKU 资料一致。
- 背景接触面、投影、透视和商品边缘自然，没有遮挡关键部位。
- 裁切后仍满足目标渠道画幅；画面文案及促销信息均有真实来源。
- 商品事实偏移时暂停交付，补充正确资料或参考图后重新制作；不要用提示词掩盖错误版本。
- 留存 SKU、素材授权、模型入口、任务用途、审核结论和最终文件之间的对应记录。

## FAQ

**Q: Kling V3 Omni Image 在 Flux Art 里能做批量商品套图吗？**

当前 Flux Art 模型页尚未开放 Image Series 组图模式。需要多张不同用途的商品图片时，按交付物选择对应电商工具或分别完成并验收单图。

**Q: 参考图数量和输出尺寸固定吗？**

当前专题页列出最多 10 张参考图及 1K、2K、4K 输出；提交时的输入限制、尺寸和画幅以工作台实时选项为准。

**Q: 多张参考图能证明商品包装信息正确吗？**

不能。商品主数据、实物和已批准的包装文件才是事实依据；参考图只提供其中可见的视觉信息。

**Q: 什么时候选 Kling V3 Image？**

当任务适合以一张参考图进行编辑时，可以从 [Kling V3 Image](https://flux-art.cn/zh/models/kling-v3-image)入口评估；需要多张图分担商品、环境或风格职责时，再比较 Omni，并按各自页面选项分别验收。

## EN Summary

Use Kling V3 Omni Image on Flux Art when a static product-image task needs clearly assigned product, scene, brand-style or detail references. Its current Flux Art page lists up to ten reference images and 1K, 2K or 4K output, while Image Series is not currently exposed in the workspace. Confirm the live form settings, check the result against approved SKU facts and rights, and do not treat one generation as an automatically produced product set.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
