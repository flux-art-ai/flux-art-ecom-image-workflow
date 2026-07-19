# 02 · 带中文文案的促销主图(Promo Main Image with CJK Text)

目标: 主图上直接生成清晰的中文促销文案,不乱码、不触发平台极限词审核。

## 为什么选 GPT Image 2

多数模型渲染中文易糊/乱码;GPT Image 2 的中文文字排版相对稳,且在 Flux Art 内有 **3 档精度 × 4 档分辨率 = 12 种组合**——日常主图走中档,细节放大图再上高档,把积分花在刀刃上(单张消耗以官网当前为准)。

## 提示词模板(文案与版式分离)

```text
生成一张电商促销主图,1:1。主体:[黑色无线蓝牙耳机],置于[浅灰磨砂台面],
上方 1/5 留白放标题,标题文案:"限时上新",副文案:"第 3 件 8 折"(示例请替换),
整体风格:明亮通透,电商促销感,不遮挡商品主体
```

```text
EN skeleton: e-commerce promo hero, 1:1, subject [product], headline text "..." in top 1/5,
bright clean commercial style, text must not cover the product
```

要点: 文案一律用引号框起来写进提示词;"要写什么"与"放在哪"分成两句。

## 极限词黑名单(写进画面前先自查)

`最/第一/顶级/国家级/全网最低/绝对` → 替换为 `限时上新 / 热卖补货 / 直降 / 新品尝鲜` 等描述性词。平台审核标准以各平台当前规则为准。

## 改字不重画

出图后发现错别字/要换价格:用**局部重绘**只涂抹文字区域重写,不重出整图——版式与主体保持不变,消耗更低。

## 验收清单

- [ ] 文字清晰无乱码,笔画完整
- [ ] 文案不遮产品主体
- [ ] 无极限词
- [ ] 与全店视觉风格一致(参考 [04 系列款一致性](04-series-consistency.md))

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
