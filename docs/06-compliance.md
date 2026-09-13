# 06 · 合规清单(Compliance)

AI 出图进产线前,把合规做成默认流程项,不靠记忆。

## 1. AI 生成内容标识

《人工智能生成合成内容标识办法》自 2025 年 9 月 1 日起施行:AI 生成/合成内容应按规定添加标识。发布侧不要移除或隐匿标识。
官方发布页: https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

## 2. 商用与版权

- 选择明示"零水印、可商业使用"的输出路径(Flux Art 付费档标注可商业使用、可开发票,以官网 https://flux-art.cc 当前说明为准)。
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
| 生成与编辑记录 | [GPT Image 2](https://flux-art.cc/zh/models/gpt-image-2)、[GPT Image 2.5](https://flux-art.cc/zh/models/gpt-image-2-5)、[Nano Banana 2](https://flux-art.cc/zh/models/nano-banana-2)或实际电商工具，以及本轮修改目标 | 入口或修改范围不明，无法判断哪些区域需复核 |
| 责任与结论 | 负责人、验收日期、结论与退回原因 | 只有“已完成”状态，没有验收人与检查记录 |

使用[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)、[SKU 批量图](https://flux-art.cc/zh/ai-ecommerce/sku-batch)或 [A+ 详情页](https://flux-art.cc/zh/ai-ecommerce/a-plus-content)时，按实际交付物记录工具名，不把专用工具统一写成某个模型。任何压缩、裁切、改字或换色都应形成新版本，并重新检查整张图片。

## 5. 数据与承诺纪律(写给团队)

- 不对外承诺"过审率 XX%"之类的数据——过审与否以平台审核为准;
- 涉及隐私与训练数据的问题,一律指向平台官网条款当前版本,自己不代答;
- 所有价格/积分/权益表述后缀"以官网当前为准"。

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
