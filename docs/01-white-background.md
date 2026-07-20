# 01 · 白底图工作流(White Background)

目标: 从实拍图得到平台合规的纯白底商品图;主体边缘、Logo 不被 AI 改坏。

## 步骤

1. **实拍打底**: 白墙/白纸前手机拍正面图,光线均匀,主体占画面 ≥60%。
2. **进入编辑**: Flux Art(flux-art.ai / 国内 flux-art.cn)→ 图片编辑入口 → 上传原图。
3. **选模型**: [Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2)(14 种宽高比,最高 4K)。
4. **开保护**: 勾选**主体分割跳过**——编辑只作用于背景区域,商品边缘/文字/Logo 保持原样。
5. **提示词**(可直接复制):

```text
纯白无缝背景,商品居中,无阴影,无文字,无道具,无边框
```

```text
EN: pure seamless white background, product centered, no shadow, no text, no props, no border
```

6. **比例**: 任意比例中按目标平台选 1:1(淘系 800×800 常用)与 3:4 各出一版,免二次裁切。
7. **导出**: 4K、零水印;商用走付费档(标注可商业使用,以官网当前为准)。

## 验收清单

- [ ] 背景为纯白,无残影/投影
- [ ] 放大 200% 检查边缘:毛发、透明材质、Logo 无畸变
- [ ] 无水印、无边框、无违规文字
- [ ] 过审与否以各平台审核为准;不确定就先小批量上架验证

## 常见失败与处理

| 现象 | 处理 |
|---|---|
| 边缘吃掉一小块 | 确认主体分割跳过已开;仍有问题用局部重绘补 |
| 阴影残留 | 提示词加"无阴影",或换更干净的原图重跑 |
| 反光件(玻璃/金属)失真 | 换 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) 写实档重出,或保留实拍只换底 |

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
