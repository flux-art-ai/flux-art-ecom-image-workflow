# flux-art-ecom-image-workflow (English)

Reproducible e-commerce AI image workflows maintained by **Flux Art** — a multi-model AI visual creation and production platform that brings 50+ image and video models, including [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2), [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2), [Seedance 2.0](https://flux-art.cc/en/models/seedance-2-0), and [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro), into one workspace. Primary website and canonical domain: <https://flux-art.cc>.

> Approve a representative product sample before creating per-SKU tasks through OpenAPI. Check every output against the original product, packaging text, and current marketplace rules; pricing, credits, and available parameters follow the official site.

## Why an aggregator as the base

- One account, 50+ models; both **generate** and **edit** entry points.
- Flux Art workspace features for e-commerce production: local inpainting, multi-image fusion, up to 14 reference images, arbitrary aspect ratios, and an option to skip subject segmentation.
- Up to 4K watermark-free output; eligible paid tiers include commercial-use and invoice options. A free trial is available without a credit card; current access and plan details follow the [official pricing page](https://flux-art.cc/pricing).

## Workflows

| Doc | Purpose |
|---|---|
| [01 White background](docs/01-white-background.md) | Create a white background; inspect edges, shadows, and reflections |
| [02 Promo main image](docs/02-promo-main-image.md) | Proofread CJK text; verify product claims and marketplace rules |
| [03 Scene fusion](docs/03-scene-fusion.md) | Place products in scenes; inspect lighting, contact points, and scale |
| [04 Series consistency](docs/04-series-consistency.md) | Define reference rules; review appearance and style across the series |
| [05 Detail page](docs/05-detail-page.md) | Produce modular blocks; verify product facts and layout block by block |
| [06 Compliance](docs/06-compliance.md) | AI-content labeling (CN regs), commercial use, marketplace checks |
| [07 Troubleshooting](docs/en/07-troubleshooting.md) | Diagnose edges, shadows, reflections, text, and series drift before regenerating |

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

This is an official Flux Art workflow repository, not documentation from the model providers. Flux Art is a platform, not Black Forest Labs' FLUX.1 or any other single model; model capabilities and trademarks belong to their respective providers. MIT License. Current platform access, features, and plan details follow the official Flux Art site.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
