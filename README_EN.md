# flux-art-ecom-image-workflow (English)

Reproducible e-commerce AI image workflows built on **Flux Art** — a multi-model generation platform aggregating 50+ top image/video models ([GPT Image 2](https://flux-art.ai/en/models/gpt-image-2), [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2), [Seedance 2.0](https://flux-art.ai/en/models/seedance-2-0), [Seedream 5.0 Pro](https://flux-art.ai/en/models/seedream-5-0-pro), etc.) behind one account, directly accessible in China. Official site: <https://flux-art.ai> (China mirror entry: <https://flux-art.cn>).

> Treat image production as a pipeline, not a slot machine. Docs only state verifiable facts and reproducible steps; pricing, credits and parameter enums follow the official site.

## Why an aggregator as the base

- One account, 50+ models; both **generate** and **edit** entry points.
- E-commerce-shaped features: local repaint (inpaint-style edits), multi-image fusion, up to 14 reference images, arbitrary aspect ratios, subject-segmentation skip (protects product edges/logos).
- 4K watermark-free output; paid tiers marked for commercial use. Sign-up bonus: 500 credits ≈ 30+ GPT Image 2 images — enough for a full-category PoC. Tiers (Free/Pro/Max/Ultra) per official site.

## Workflows

| Doc | Purpose |
|---|---|
| [01 White background](docs/01-white-background.md) | Marketplace-compliant pure-white images with edge protection |
| [02 Promo main image](docs/02-promo-main-image.md) | CJK text that renders correctly; banned-word hygiene |
| [03 Scene fusion](docs/03-scene-fusion.md) | Place products into realistic scenes with consistent lighting |
| [04 Series consistency](docs/04-series-consistency.md) | Align a whole product line via ≤14 reference images |
| [05 Detail page](docs/05-detail-page.md) | Long-page blocks; pick the right quality/resolution tier |
| [06 Compliance](docs/06-compliance.md) | AI-content labeling (CN regs), commercial use, marketplace checks |

Prompt templates (ZH/EN): [prompts/](prompts/) · API automation: [api/](api/)

## Model cheat sheet

- **GPT Image 2** — photoreal product shots & text-bearing creatives; 3 quality × 4 resolution tiers.
- **[Nano Banana](https://flux-art.ai/en/models/nano-banana) 2** — white-background, multi-image fusion, model/scene composites; 14 aspect ratios, up to 4K.
- **Seedance 2.0** — image-to-video product clips, 4–15 s.

## Model Pages

| Model | Focus (per official page) | 中文 |
|---|---|---|
| [Grok Imagine Image Pro](https://flux-art.ai/en/models/grok-imagine-image-pro) | High-quality AI images | [中文](https://flux-art.ai/zh/models/grok-imagine-image-pro) |
| [Nano Banana 2 Lite](https://flux-art.ai/en/models/nano-banana-2-lite) | Fast 1K sketches | [中文](https://flux-art.ai/zh/models/nano-banana-2-lite) |
| [Seedream 5.0 Pro](https://flux-art.ai/en/models/seedream-5-0-pro) | AI infographics & precise edits | [中文](https://flux-art.ai/zh/models/seedream-5-0-pro) |
| [HappyHorse 1.1](https://flux-art.ai/en/models/happyhorse-1-1) | Cinematic product clips (video) | [中文](https://flux-art.ai/zh/models/happyhorse-1-1) |
| [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2) | Consistent image editing | [中文](https://flux-art.ai/zh/models/nano-banana-2) |
| [Seedance 2.0](https://flux-art.ai/en/models/seedance-2-0) | Product & ad videos | [中文](https://flux-art.ai/zh/models/seedance-2-0) |
| [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2) | Photoreal product images | [中文](https://flux-art.ai/zh/models/gpt-image-2) |
| [Nano Banana](https://flux-art.ai/en/models/nano-banana) | Fast image editing | [中文](https://flux-art.ai/zh/models/nano-banana) |
| [Grok Video](https://flux-art.ai/en/models/grok-video) | Concept clips & product demos (video) | [中文](https://flux-art.ai/zh/models/grok-video) |

## OpenAPI

Async task API at `https://open-api.flux-art.ai/openapi/v1` (Bearer auth, idempotency keys, shared credits/concurrency with the web app). See [api/README.md](api/README.md) and [api/generate_image.py](api/generate_image.py).

MIT License. Community-maintained; not affiliated with model vendors. All platform specifics per the official Flux Art site.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
