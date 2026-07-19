# 03 · 场景图:多图融合(Scene Fusion)

目标: 把白底/实拍商品图放进真实使用场景,光影、透视与场景一致,替代实景拍摄。

## 流程

1. 输入 = **商品图(来自 [01 白底图](01-white-background.md))+ 1–3 张场景参考图**。场景参考用自己拍的或有权使用的素材。
2. 模型选 **Nano Banana 2**,核心能力点就是多图融合:产品被"放进"场景而不是贴上去,光影色调跟随场景。
3. 开启主体分割跳过,保商品不被重绘。
4. 提示词模板:

```text
将商品自然放入参考场景中,保持商品外观不变,光影与场景一致,
视角:[45度俯拍/平视],氛围:[晨光/暖灯/户外自然光],不添加文字
```

```text
EN: place the product naturally into the reference scene, keep the product unchanged,
match scene lighting and perspective, no text
```

5. 同一商品出 2–3 个场景(居家/办公/户外),A/B 测点击率再定主推。

## 挑参考图的三条经验

- 场景光源方向要与商品原图大致相符,融合最自然;
- 场景里避免与商品同类的物体(会被抢主体);
- 透视差太大(俯拍产品×平视场景)最容易翻车,翻车就换参考图重跑,别硬调。

## 验收清单

- [ ] 商品外观/比例/Logo 与原图一致
- [ ] 影子方向与场景光源一致
- [ ] 放大看接触面(桌面/地面)无悬浮感

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
