# 05 · 详情页长图(Detail Page)

目标: 详情页按"分块生成→拼接"的方式产出;用 [GPT Image 2](https://flux-art.ai/zh/models/gpt-image-2) 的档位组合控制积分成本。

## 档位策略(3 精度 × 4 分辨率 = 12 组合)

| 图型 | 建议档位 | 理由 |
|---|---|---|
| 头图/氛围块 | 中精度·中分辨率 | 观感优先,成本可控 |
| 功能点小图 | 低-中档 | 数量多,单张成本敏感 |
| 材质/细节放大块 | 高精度·高分辨率 | 决定转化的信任块 |

单张积分消耗与档位枚举以官网/控制台当前为准——原则是"缩略低档、主图中档、细节高档"。

## 分块生成流程

1. 先写详情页大纲(痛点块/功能块×3/细节块/规格块/售后块);
2. 每块单独生成:**功能块让 AI 只出图不出字**,文字后期排版加——多语言站点尤其如此,规避错字;
3. 规格块/对比块用表格排版工具做,不强求 AI 生成;
4. 统一改色改字用局部重绘;
5. 拼接导出长图,压缩后检查文字仍可读。

## 提示词模板(功能块)

```text
电商详情页功能展示图,主体:[产品+使用状态],构图居中,背景简洁纯色,
不添加任何文字与图标,预留上方 1/6 空白(后期排字用)
```

## 与视频的衔接

详情页头部要动图/短视频时,用 [Seedance 2.0](https://flux-art.ai/zh/models/seedance-2-0)(图/视频/音频多输入,4–15 秒),静态套图完成后再做,素材可直接复用。

## 验收清单

- [ ] 全页色调统一(块与块之间无跳色)
- [ ] 文字均为后期排版,无 AI 生成错字
- [ ] 手机端预览:细节块文字可读、加载不糊

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
