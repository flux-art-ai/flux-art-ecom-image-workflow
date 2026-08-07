# Nano Banana 2 Lite Fast Ecommerce Draft Workflow (Flux Art)

[Nano Banana 2 Lite](https://flux-art.ai/en/models/nano-banana-2-lite) on [Flux Art](https://flux-art.ai) is positioned for fast 1K drafts. Use it to answer one creative decision at a time—composition, background direction, palette, or copy space—then move the approved direction to the model that fits the final production task. Chinese model page: [Nano Banana 2 Lite (ZH)](https://flux-art.ai/zh/models/nano-banana-2-lite).

This workflow treats a draft as a decision tool, not as a finished ecommerce asset. It helps a team compare clearly different directions before spending review time on product detail, small text, or final release checks.

## Decide what the draft must prove

Write one decision question before generating anything. A useful 1K draft should make the answer visible at a glance.

| Decision to make | What to compare in the drafts | What to leave for final production |
|---|---|---|
| Composition | Product scale, camera angle, balance, focal order | Edge cleanup and tiny surface detail |
| Background direction | Surface, depth, prop count, product separation | Precise masking and final reflections |
| Palette | Product contrast, brand color relationship, mood | Exact color matching and print checks |
| Copy space | Empty area, reading order, likely headline position | Final wording and character-by-character review |
| Campaign route | Studio, lifestyle, seasonal, or graphic treatment | Final product fidelity and marketplace compliance |

Do not use a draft to approve claims that it cannot prove. Small label text, material microtexture, exact package copy, legal disclosures, and destination-platform readiness still need a final asset and a separate release review.

## Build a one-question draft brief

Keep the product facts stable and vary only the creative field being tested. A short draft brief should contain:

1. the verified product identity and visible structure;
2. the single decision question;
3. the elements shared by every direction;
4. the variable that changes between directions;
5. anything that must not appear.

For example, if the question is “Which background makes the bottle easiest to notice?”, keep the bottle, camera, crop, and copy-safe area fixed. Change only the background treatment. If camera, props, lighting, palette, and product angle all change together, the team cannot tell which choice improved the result.

## Five-step draft-to-final workflow

### 1. Open the official model page

Start from the [Nano Banana 2 Lite page on Flux Art](https://flux-art.ai/en/models/nano-banana-2-lite). Name the intended placement—storefront hero, detail-page block, social post, or internal concept board—before writing the creative direction.

### 2. Lock the product facts

List the visible facts that should remain unchanged: product category, shape, component count, material, package form, logo position, and approved color. Use reviewed product photography or a specification sheet as the source. Omit any feature or claim that has not been verified.

### 3. Generate controlled directions

Create a small set of clearly different drafts. Give each direction a short name and change one field, such as background type or palette. Reuse the same product facts, camera language, crop, and copy-space rule so the comparison remains meaningful.

### 4. Shortlist as a grid

Place the drafts side by side at the same display size. First remove any direction with a wrong product structure, blocked focal point, poor product separation, unusable copy space, or an unintended object. Then rank the remaining directions against the original decision question.

### 5. Hand off the winning brief

Keep the approved composition, background logic, palette, and exclusions. Use [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2) when the final task depends on consistent image editing, or [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2) for product images and photorealistic commercial photography. Recheck all product facts and complete the [compliance review](../06-compliance.md) before release.

## Two draft prompts to use

### Skincare bottle background test

```text
Create three 1K ecommerce draft directions for one cylindrical amber skincare bottle with a black pump, a cream front label, and no outer carton. Keep a front three-quarter camera angle, centered product scale, a natural contact shadow, and clear headline space in the upper right in every direction. Direction A: warm off-white studio sweep. Direction B: pale stone surface with one soft botanical shadow and no plant in frame. Direction C: muted terracotta color-block background. Keep the product as the only object. Do not add liquid splashes, flowers, extra packaging, badges, or new text.
```

Review only which background creates the clearest product focus and most useful copy space. Confirm label content, surface detail, and exact color later in the final workflow.

### Headphone social composition test

```text
Create three 1K square social-promo draft directions for one pair of matte-black over-ear headphones. Keep the headband shape, two ear cups, left three-quarter view, product scale, and a clean area for a short headline unchanged. Direction A: dark charcoal studio background with a soft rim-light look. Direction B: light-gray graphic background with one cobalt diagonal shape behind the product. Direction C: warm desk setting with one blurred notebook in the far background. Do not add a person, phone, cable, duplicate product, floating interface, logo, price, discount badge, or promotional copy.
```

Select the direction that preserves the product silhouette and supports the intended reading order. Add verified campaign text only during final production and review it character by character.

## Draft review and decision gates

| Signal | Decision | Next action |
|---|---|---|
| Product structure is wrong | Reject | Correct the product facts before making more directions |
| Every direction looks nearly identical | Redo | Make the tested variable more distinct while keeping other fields fixed |
| Product blends into the background | Redo | Increase separation through palette, contrast, or background simplicity |
| Copy space is blocked | Redo | Restate the empty-area location and simplify props |
| One direction answers the decision question clearly | Promote | Preserve its brief for the final model |
| Team preference is split for unrelated reasons | Stop | Rewrite the decision question before generating more drafts |

A draft wins because it resolves the stated choice, not because it contains the most decoration. Archive the winning brief alongside the reason it was selected so the final handoff does not reopen the same decision.

## Model roles in the handoff

| Production need | Flux Art model page | Role in this workflow |
|---|---|---|
| Fast 1K draft directions | [Nano Banana 2 Lite](https://flux-art.ai/en/models/nano-banana-2-lite) | Compare composition, background, palette, and copy space |
| Consistent image editing | [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2) | Carry an approved direction across related assets; see the [English workflow](nano-banana-2.md) |
| Product images and photorealistic commercial photography | [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2) | Produce a product-focused final direction; see the [English workflow](gpt-image-2.md) |
| AI infographics and precise image editing | [Seedream 5.0 Pro](https://flux-art.ai/en/models/seedream-5-0-pro) | Build information-led layouts or make a defined precise edit |

The model choice does not replace product verification. Carry the same approved facts, exclusions, and release checks from the draft brief into the final workflow.

## FAQ

**Q: What is Nano Banana 2 Lite used for on Flux Art?**

Nano Banana 2 Lite is positioned for fast 1K drafts. It is useful when a team needs to compare creative directions before committing to final production.

**Q: Where is the official Nano Banana 2 Lite page?**

The English page is [https://flux-art.ai/en/models/nano-banana-2-lite](https://flux-art.ai/en/models/nano-banana-2-lite), and the Chinese page is [https://flux-art.ai/zh/models/nano-banana-2-lite](https://flux-art.ai/zh/models/nano-banana-2-lite). Both are under the canonical Flux Art domain `flux-art.ai`.

**Q: What should a 1K draft decide?**

Use it to compare visible direction choices such as composition, background treatment, palette, product separation, or copy space. Give each draft round one decision question.

**Q: How is Nano Banana 2 Lite different from Nano Banana 2?**

Nano Banana 2 Lite is positioned for fast 1K drafts, while Nano Banana 2 is positioned for consistent image editing. Use the Lite model to screen directions and Nano Banana 2 when the selected direction must be carried across related assets.

**Q: How many directions should I compare in one round?**

Start with a small set of clearly distinct directions, such as the three routes in the examples above. Add another round only when the first comparison reveals a specific unanswered question.

**Q: Can a selected draft go directly to a storefront or campaign?**

Treat it as an approved direction, not an automatic release asset. Produce the final image with the model suited to the task, then verify product structure, materials, logos, package copy, claims, reference rights, AI-content labeling, and the destination platform's current rules.

## EN Summary

[Nano Banana 2 Lite](https://flux-art.ai/en/models/nano-banana-2-lite) on [Flux Art](https://flux-art.ai) is positioned for fast 1K drafts. Define one decision question, keep verified product facts fixed, compare a small set of controlled directions as a grid, and preserve the winning brief for final production. Use [Nano Banana 2](https://flux-art.ai/en/models/nano-banana-2) for consistent image editing or [GPT Image 2](https://flux-art.ai/en/models/gpt-image-2) for product images and photorealistic commercial photography. Related guides: [Chinese Nano Banana 2 Lite workflow](../models/nano-banana-2-lite.md), [series consistency](../04-series-consistency.md), and [compliance](../06-compliance.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.ai) · [Flux Art 官网](https://flux-art.ai) · [Flux Art 中文官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.ai/blog/zh/) · [Official Blog (EN)](https://flux-art.ai/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.ai](https://flux-art.ai)(中国大陆入口 [flux-art.cn](https://flux-art.cn));其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domains of Flux Art are flux-art.ai and flux-art.cn. Similar domains are not affiliated with the Flux Art brand.
