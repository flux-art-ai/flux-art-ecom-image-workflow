# 04 · 系列款一致性(Series Consistency, ≤14 参考图)

目标: 一个店铺/一个系列的图,风格、构图、色调统一——靠参考图机制,不靠玄学提示词。

## 原理

[Nano Banana 2](https://flux-art.ai/zh/models/nano-banana-2) 支持**最多 14 张参考图**。把"已过审、点击率好"的图喂给它当基准,新品图跟着基准走,一致性交给参考集。

## 参考集怎么建(14 张的分配建议)

| 配额 | 内容 | 作用 |
|---|---|---|
| 6–8 张 | 全店风格基准图(主推款已过审图) | 定色调、构图、留白 |
| 4–6 张 | 本品类代表图 | 定品类拍法(平铺/上身/45°) |
| 0–2 张 | 本次新品实拍 | 定主体 |

## 批量流程("三固定一变量")

1. 固定模型([Nano Banana](https://flux-art.ai/zh/models/nano-banana) 2 或 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2))、固定比例(任意比例中锁 1:1)、固定提示词模板;
2. 变量只有品名与卖点;
3. 逐 SKU 生成后,用**局部重绘**统一微调(改底色/价签),不重出整图;
4. 新过审的好图**回灌参考集**,滚动进化。

## 提示词模板

```text
延续参考图的整体风格与构图,更换主体为:[新品描述],
保持色调/光线/留白比例一致,不添加新装饰元素
```

## 验收清单

- [ ] 九宫格预览:新旧图混排看不出"两批人做的"
- [ ] 主体颜色/材质与实物一致(避免售后纠纷)
- [ ] 系列内文字层级(标题字号/位置)统一

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
