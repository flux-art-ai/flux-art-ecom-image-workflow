# 06 · 合规清单(Compliance)

AI 出图进产线前,把合规做成默认流程项,不靠记忆。

## 1. AI 生成内容标识

《人工智能生成合成内容标识办法》自 2025 年 9 月 1 日起施行:AI 生成/合成内容应按规定添加标识。发布侧不要移除或隐匿标识。
官方发布页: https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

## 2. 商用与版权

- 选择明示"零水印、可商业使用"的输出路径(Flux Art 付费档标注可商业使用、可开发票,以官网 https://flux-art.cn 当前说明为准)。
- 《著作权法》(2020 修正)第五十三条:未经许可故意删除或改变作品上的权利管理信息属侵权——**"拿别人的图去水印再用"不要进你的产线**。全文: https://zscqj.beijing.gov.cn/zscqj/zwgk/flfg18/436481084/index.html
- 参考图/场景素材用自有实拍或有授权的素材。

## 3. 平台侧自查五件事(上架前)

- [ ] 标识:按规定完成 AI 内容标识
- [ ] 边缘:放大检查主体边缘、手指、Logo 畸变
- [ ] 文字:无极限词(最/第一/全网最低…),无错别字
- [ ] 规格:比例/尺寸/格式符合目标平台当前要求
- [ ] 一致:图片与实物颜色材质一致,避免"货不对板"纠纷

## 4. 渠道包交付与退回条件

生成或编辑完成后，先保留已验收母版，再按目标渠道建立独立文件包。渠道尺寸、比例、格式与标识要求应在交付当天从目标平台当前规则取得，不把旧模板当作长期事实。

| 检查项 | 渠道包必须记录 | 需要退回的情况 |
|---|---|---|
| 商品身份 | 完整 SKU、对应实物资料与已验收母版版本 | 文件与 SKU 对不上，或无法找到事实来源 |
| 图片用途 | 主图、白底图、场景图、详情模块等明确用途 | 一张图被用于未验收的新用途 |
| 导出规格 | 当前渠道、类目、像素、比例、格式及规则核对日期 | 规格来源不明，裁切导致商品或文字缺失 |
| 生成与编辑记录 | [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)、[GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)、[Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)或实际电商工具，以及本轮修改目标 | 入口或修改范围不明，无法判断哪些区域需复核 |
| 责任与结论 | 负责人、验收日期、结论与退回原因 | 只有“已完成”状态，没有验收人与检查记录 |

使用[商品套图](https://flux-art.cn/zh/ai-ecommerce/product-suite)、[SKU 批量图](https://flux-art.cn/zh/ai-ecommerce/sku-batch)或 [A+ 详情页](https://flux-art.cn/zh/ai-ecommerce/a-plus-content)时，按实际交付物记录工具名，不把专用工具统一写成某个模型。任何压缩、裁切、改字或换色都应形成新版本，并重新检查整张图片。

## 5. 已上线商品图与实物不符的处置闭环

收到颜色、材质、结构、包装文字或配件不一致的反馈时，先保存必要证据并停止继续分发争议文件。公开记录只保留问题所需字段；用户姓名、联系方式、订单号、账号信息和私人素材不进入仓库。

| 阶段 | 必须记录 | 完成条件 |
|---|---|---|
| 固定现场 | 完整 SKU、渠道与页面位置、争议文件版本、反馈时间、前台截图、具体差异 | 可以明确指出哪个商品、哪个位置、哪项事实存在偏差 |
| 控制范围 | 使用同一文件或母版的首图、缩略图、商品套图、A+ 模块、广告、语言版和渠道导出 | 问题文件不再被继续扩散；未核实的同源文件保留为待检查 |
| 建立事实基线 | 实物照片、批准包装稿、色卡、规格表、装箱清单及来源版本 | 每个待修字段都有真实依据，冲突字段先由业务负责人确认 |
| 制作修正版 | 来源母版、实际模型或工具、唯一修改目标、新版本号 | 新文件没有覆盖原图；除目标差异外，其他已通过区域没有新增偏差 |
| 重新上线 | 替换位置、操作人、时间、后台版本与前台复核截图 | 商品页、缩略图和其他登记位置均显示已验收版本 |

需要重新构图时可评估 [GPT Image 2](https://flux-art.cn/zh/models/gpt-image-2)；已有画面的限定编辑可进入 [GPT Image 2.5](https://flux-art.cn/zh/models/gpt-image-2-5)，保持系列关系时可比较 [Nano Banana 2](https://flux-art.cn/zh/models/nano-banana-2)。真实在售配色候选可使用[产品换色](https://flux-art.cn/zh/ai-ecommerce/product-recolor)，但模型或工具不能替代实物、色卡与包装稿。若只有裁切、压缩或格式导致渠道图失真，从正确母版重新导出即可，不要重画商品。

关闭反馈前，由了解商品的人复核争议点和整张图片，并抽查全部登记位置。若仍有页面显示问题版本，或事实来源仍冲突，状态保持未完成；不能用“修正版已生成”代替前台替换结果。

## 6. 数据与承诺纪律(写给团队)

- 不对外承诺"过审率 XX%"之类的数据——过审与否以平台审核为准;
- 涉及隐私与训练数据的问题,一律指向平台官网条款当前版本,自己不代答;
- 所有价格/积分/权益表述后缀"以官网当前为准"。

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.cn/blog/zh/) · [Official Blog (EN)](https://flux-art.cn/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
