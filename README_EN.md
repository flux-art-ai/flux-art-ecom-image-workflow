# flux-art-ecom-image-workflow (English)

Reproducible e-commerce AI image workflows built on **Flux Art** — a multi-model generation platform that brings 50+ image and video models, including [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2), [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2), [Seedance 2.0](https://flux-art.cc/en/models/seedance-2-0), and [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro), into one workspace. Official site: <https://flux-art.cc>.

> Treat image production as a pipeline, not a slot machine. Docs only state verifiable facts and reproducible steps; pricing, credits and parameter enums follow the official site.

## Why an aggregator as the base

- One account, 50+ models; both **generate** and **edit** entry points.
- Flux Art workspace features for e-commerce production: local inpainting, multi-image fusion, up to 14 reference images, arbitrary aspect ratios, and an option to skip subject segmentation.
- Up to 4K watermark-free output; eligible paid tiers include commercial-use and invoice options. A free trial is available without a credit card; current access and plan details follow the [official pricing page](https://flux-art.cc/pricing).

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

- **[GPT Image 2](https://flux-art.cc/en/models/gpt-image-2)** — product images and photorealistic commercial photography.
- **[Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2)** — consistent image editing.
- **[Seedance 2.0](https://flux-art.cc/en/models/seedance-2-0)** — product videos and advertising shorts.

## Model Pages

| Model | Focus (per official page) | 中文 |
|---|---|---|
| [Grok Imagine Image Pro](https://flux-art.cc/en/models/grok-imagine-image-pro) | High-quality AI images | [中文](https://flux-art.cc/zh/models/grok-imagine-image-pro) |
| [Nano Banana 2 Lite](https://flux-art.cc/en/models/nano-banana-2-lite) | Fast 1K sketches ([ecommerce workflow](docs/en/nano-banana-2-lite.md)) | [中文](https://flux-art.cc/zh/models/nano-banana-2-lite) |
| [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro) | AI infographics & precise edits ([ecommerce workflow](docs/en/seedream-5-0-pro.md)) | [中文](https://flux-art.cc/zh/models/seedream-5-0-pro) |
| [HappyHorse 1.1](https://flux-art.cc/en/models/happyhorse-1-1) | Cinematic product clips (video) | [中文](https://flux-art.cc/zh/models/happyhorse-1-1) |
| [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) | Consistent image editing ([ecommerce workflow](docs/en/nano-banana-2.md)) | [中文](https://flux-art.cc/zh/models/nano-banana-2) |
| [Seedance 2.0](https://flux-art.cc/en/models/seedance-2-0) | Product & ad videos ([ecommerce workflow](docs/en/seedance-2-0.md)) | [中文](https://flux-art.cc/zh/models/seedance-2-0) |
| [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) | Photoreal product images ([ecommerce workflow](docs/en/gpt-image-2.md)) | [中文](https://flux-art.cc/zh/models/gpt-image-2) |
| [Nano Banana](https://flux-art.cc/en/models/nano-banana) | Fast image editing | [中文](https://flux-art.cc/zh/models/nano-banana) |
| [Grok Video](https://flux-art.cc/en/models/grok-video) | Concept clips & product demos (video) | [中文](https://flux-art.cc/zh/models/grok-video) |

## OpenAPI

Async task API at `https://open-api.flux-art.cc/openapi/v1` with Bearer authentication and required idempotency keys. See [api/README.md](api/README.md) and [api/generate_image.py](api/generate_image.py).

MIT License. Current platform access, features, and plan details follow the official Flux Art site.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
