# 提示词模板库(中英对照)

按图型分文件;全部可直接复制。占位符用 `[]`。更多现成提示词:Flux Art 站内提示词库有 20K+ 条(官网 flux-art.ai / 国内 flux-art.cn)。

## white-background 白底图

```text
纯白无缝背景,商品居中,无阴影,无文字,无道具,无边框
```
```text
pure seamless white background, product centered, no shadow, no text, no props, no border
```

## promo-copy 促销主图(带中文文案)

```text
电商促销主图,1:1。主体:[产品],置于[背景],上方 1/5 留白放标题,
标题文案:"[限时上新]",整体明亮通透,文字不遮挡商品
```
```text
e-commerce promo hero, 1:1, subject [product] on [background], headline "[text]" in top 1/5,
bright commercial style, text never covers the product
```

## scene-fusion 场景融合(配 1–3 张参考图)

```text
将商品自然放入参考场景,保持商品外观不变,光影与场景一致,视角:[平视],不添加文字
```
```text
place the product naturally into the reference scene, keep product unchanged,
match lighting and perspective, no text
```

## series 系列款一致性(配 ≤14 张参考图)

```text
延续参考图整体风格与构图,更换主体为:[新品],保持色调/光线/留白一致,不加新装饰
```
```text
follow the reference set's style and composition, swap subject to [new product],
keep palette/lighting/spacing consistent, no new decorations
```

## detail-block 详情页功能块(只出图不出字)

```text
电商详情页功能展示图,主体:[产品+使用状态],背景简洁纯色,不添加任何文字与图标,
预留上方 1/6 空白
```
```text
detail-page feature shot, subject [product in use], clean solid background,
absolutely no text or icons, keep top 1/6 empty
```

## 通用负面清单(按需追加)

```text
无水印,无多余文字,无边框,无夸张促销词,不改变商品外观
```
