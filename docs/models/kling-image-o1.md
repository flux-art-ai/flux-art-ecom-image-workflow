# Kling Image O1 多参考图商品视觉工作流｜Flux Art

当一张商品图需要组合多张来源各异的参考图时，Flux Art 的 Kling Image O1 页面可作为生成或编辑入口：先给每张图片分配明确职责，再写保留项、变化范围与目标画面。当前专题页显示最多 10 张参考图及 1K / 2K 输出；实际可用项以提交时工作台为准。

## 什么时候用多参考图

适合把不同视觉信息拆开管理的任务，例如：商品外观来自实拍，场景来自获准使用的环境图，风格来自品牌视觉样张，细节来自包装或材质近照。若任务只需改动已验收图片中的一个局部，可先查看 [GPT Image 2.5 参考图编辑流程](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/reference-editing.md)；若重点是扩展已定稿系列的相似构图，可比较 [Nano Banana 2 系列款流程](nano-banana-2.md)。这些路线是任务分流，不是效果排名。

Kling Image O1 的 [中文入口](https://flux-art.cn/zh/models/kling-image-o1)与[英文入口](https://flux-art.cn/en/models/kling-image-o1)均可从 Flux Art 模型页面进入。模型由其提供方开发，Flux Art 提供统一的使用工作台；当前模型页显示的输入和输出选项可能随页面调整。

## 先给每张图片分配职责

| 参考图角色 | 从图中提取什么 | 商品任务中的例子 |
|---|---|---|
| 商品主体 | 轮廓、颜色、包装与标识位置 | 当前在售 SKU 的正面实拍 |
| 场景环境 | 背景、台面、空间关系 | 有权使用的厨房台面或户外场景 |
| 风格光线 | 色调、光比、材质表现 | 已批准的品牌视觉样张 |
| 细节依据 | 纹理、接口、缝线或包装局部 | 标签、拉链、接缝的清晰近照 |
| 构图参考 | 景别、主体位置与留白 | 已获准参考的版式或拍摄构图 |

不要让同一张图同时承担互相冲突的要求。若不同参考图在商品颜色、包装、商标或构图上不一致，先回到 SKU 主数据和已批准素材，确定哪张是商品事实依据，哪张只提供视觉方向。

## 五步完成一次可复核的小样

1. **选一项交付任务**：明确是商品主图、场景图、细节呈现还是品牌视觉探索；不要一次要求模型重做所有模块。
2. **整理参考图**：按主体、场景、风格和细节排序，删除无关或相互矛盾的图片，并确认素材使用权限。
3. **写清保留与变化**：列出商品轮廓、颜色、标签和包装文字等必须对照保留的事实，再单独说明允许替换的背景或氛围。
4. **设置画面**：在工作台选择当前可用的输出档位和比例。Kling Image O1 专题页当前列出 1K / 2K；不要把其他模型的规格套用到本页。价格和积分以官网当前为准。
5. **验收后再扩展**：先检查单张代表图中的商品几何、文字、数量、边缘与光线，再决定是否用同一 Brief 制作变体。

## 可直接改写的提示词结构

> 图 1 作为商品外观与包装事实依据；图 2 只提供场景环境；图 3 只提供光线与色调；图 4 用于查看材质细节。保留商品轮廓、颜色、标签位置和包装文字，只将背景替换为图 2 的环境。构图参考图 5 的主体位置，但不要复制其中的商标、文字或其他商品。生成一张用于商品页面评审的横幅候选图，留出安全裁切空间。

提示词不能替代商品资料。没有出现在可靠商品图或已批准资料里的尺寸、成分、认证、功能与包装内容，不应要求模型补写。

## 输出检查与返修

放大检查商品轮廓、材质、标签、配件数量与边缘；再查看背景接触关系、投影、画面文字和目标比例。如果商品事实不一致，先更换或补齐对应参考图；如果只需改一个明确区域，可转到 [GPT Image 2.5 参考图编辑指南](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/reference-editing.md)，以已验收原图作为新基线。最终发布前还要核对完整 SKU、素材授权和渠道规格。

## FAQ

**Q: Kling Image O1 在 Flux Art 里最多能上传多少张参考图？**

当前模型专题页列出最多 10 张参考图。具体输入限制以提交时该模型工作台的显示为准。

**Q: 每张参考图都要在提示词中说明用途吗？**

建议说明。把商品、场景、风格或细节分别指向对应图片，有助于团队复核输入是否齐全，也让后续返修更容易定位。

**Q: 多参考图可以证明商品包装或尺寸真实吗？**

不可以。商品主数据、实物和已批准的包装文件才是事实依据；参考图只提供可见信息，不能替代规格核验。

**Q: Kling Image O1 适合只修改一个小区域吗？**

可以按当前页面评估生成或编辑入口；若目标是对一张已验收图片做范围明确的局部返修，也可比较 GPT Image 2.5 的编辑流程，并用同一原图验收。

**Q: 多参考图都能用于商品广告吗？**

提交前要确认图片、品牌元素、人物和场景素材均可用于当前交付。参考图中的受保护元素不应因模型能够读取就直接复制到成品。

## EN Summary

Use Kling Image O1 on Flux Art when a visual brief assigns different roles to multiple references, such as product facts, scene, lighting, style and detail. The current Flux Art topic page lists up to ten reference images and 1K / 2K output. Review product attributes, labels, rights and the final crop against approved sources before delivery.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
