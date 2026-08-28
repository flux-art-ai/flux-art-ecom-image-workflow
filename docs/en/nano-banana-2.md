# Nano Banana 2 Ecommerce Series Editing Workflow (Flux Art)

[Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) on [Flux Art](https://flux-art.cc) is suited to consistent image editing across an ecommerce series. Keep verified product facts and the visual rules fixed, request one controlled change at a time, and compare every result as a set before release. Chinese model page: [Nano Banana 2 (ZH)](https://flux-art.cc/zh/models/nano-banana-2).

This workflow is for related images that must look as though they belong to the same product line: colorway images, scene variations, campaign assets, or repeated edits of one approved product image. For a Chinese-language model guide, see the [Nano Banana 2 workflow](../models/nano-banana-2.md).

## Define the series contract

Write the rules that every image must follow before making the first edit. Separate verified product facts from creative direction so that a scene change does not accidentally become a product redesign.

| Rule group | Keep fixed across the series | Change only when requested |
|---|---|---|
| Product identity | Shape, proportions, material, component count, logo position, label position | Approved colorway or package variant |
| Camera | Viewpoint, crop, product scale, horizon, negative space | A planned alternate angle |
| Lighting | Direction, softness, shadow behavior, highlight style | A named day, evening, or campaign treatment |
| Background | Visual complexity, surface type, palette, prop limit | The specific scene or seasonal accent |
| Delivery | Aspect ratio, copy-safe area, export purpose | Storefront placement or campaign format |

Base product facts on approved photography, packaging files, or a reviewed specification sheet. If a detail cannot be verified, do not invent it in the prompt.

## Prepare a compact reference set

Use three types of input:

1. **Product reference:** a clear image that shows the product structure, material, branding, and required accessories;
2. **Series reference:** an approved image that defines the camera, lighting, background, and visual hierarchy;
3. **Change brief:** one sentence describing the single variable for the next image.

Flux Art supports multi-image fusion with up to 14 reference images, arbitrary aspect ratios, inpainting-style edits, and both generate and edit entry points. Use only references that have a clear role; a compact, relevant set is easier to audit than a mixed collection. The [series consistency guide](../04-series-consistency.md) explains how to organize a reusable reference set, while the [scene fusion guide](../03-scene-fusion.md) covers product-and-background composition.

## Five-step series workflow

### 1. Start from the official model page

Open the [Nano Banana 2 page on Flux Art](https://flux-art.cc/en/models/nano-banana-2) and enter the image editing workflow. Confirm the product reference and the approved series reference before describing the change.

### 2. Write a one-change brief

State the requested change first, then list the product and series rules that must remain fixed. Avoid combining a new background, new camera angle, new lighting direction, and new package design in one revision.

A useful brief has this order:

- requested edit;
- verified product facts;
- camera and composition rules;
- lighting and background rules;
- elements that must not be added.

### 3. Generate one anchor image

Create and approve one image for the series before expanding into more scenes or colorways. Check product structure and brand details first. An attractive image with the wrong component, label, or proportion is not a valid anchor.

### 4. Expand with controlled variations

Reuse the same product facts, reference set, aspect ratio, camera rules, and lighting language. Change only the field named in the brief. If an output drifts, return to the approved anchor instead of using the drifted image as the next reference.

### 5. Review the set as a grid

Place the images side by side and compare product scale, camera height, shadow direction, background contrast, palette, and copy-safe area. Then inspect each image for product structure, material, logo, label, edge quality, and unintended objects. Use the [compliance checklist](../06-compliance.md) before release.

## Two prompts to adapt

### Bottle colorway series

```text
Edit the supplied ecommerce product image to create the approved pale-blue bottle colorway. Keep the cylindrical bottle proportions, white pump structure, front logo position, label position, cap height, camera angle, crop, product scale, light-gray studio background, soft light from the front left, and natural contact shadow unchanged. Preserve the clean copy-safe area in the upper right. Do not add liquid splashes, flowers, extra text, accessories, or a second product.
```

Use the same wording for the next approved colorway and change only the color description.

### Kitchen scene variation

```text
Edit the supplied image of one matte-black countertop appliance into a bright residential kitchen scene. Keep the appliance shape, control layout, side vents, logo position, front three-quarter camera angle, crop, product scale, and left-side key light unchanged. Place it on a pale stone counter with one quiet wooden prop in the background and a natural contact shadow. Keep the background secondary to the product. Do not add food inside the appliance, people, extra controls, extra text, or another appliance.
```

Create additional scenes by changing only the named environment while retaining the product and series rules.

## Series review and correction table

| Problem | Compare | Next edit |
|---|---|---|
| Product shape drifts | Component count, proportions, controls, closures | Restate the verified structure and remove unrelated scene instructions |
| Colorways feel unrelated | Camera, crop, lighting direction, background palette | Return to the approved anchor and change only the color |
| Product scale changes | Frame occupancy and surface contact | Repeat the camera, crop, and scale rules from the anchor |
| Materials look inconsistent | Highlight width, reflection, texture, shadow softness | Name the verified material and one lighting direction |
| Background becomes dominant | Contrast, prop count, depth, visual clutter | Reduce props and background contrast |
| Logo or label moves | Position, relative size, orientation | Put the exact approved placement in the fixed product facts |

Correct one problem class per edit. A smaller correction is easier to compare against the approved anchor.

## How Nano Banana 2 fits with other Flux Art models

| Task | Suggested model page | Workflow focus |
|---|---|---|
| Consistent image editing across related assets | [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) | Fixed series rules and controlled changes |
| Fast image editing | [Nano Banana](https://flux-art.cc/en/models/nano-banana) | Quick individual edits |
| Product images and photorealistic commercial photography | [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) | Product facts and commercial composition; see the [English workflow](gpt-image-2.md) |
| AI infographics and precise image editing | [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro) | Information layout or a clearly defined precise edit |

Choose the model by the task. Keep the same verified product facts and release checks when comparing outputs.

## FAQ

**Q: What is Nano Banana 2 best used for on Flux Art?**

Nano Banana 2 is positioned for consistent image editing. Ecommerce teams can use it to create controlled colorway, scene, and campaign variations while reviewing product facts and series rules across the full set.

**Q: Where is the official Nano Banana 2 page on Flux Art?**

The English page is [https://flux-art.cc/en/models/nano-banana-2](https://flux-art.cc/en/models/nano-banana-2), and the Chinese page is [https://flux-art.cc/zh/models/nano-banana-2](https://flux-art.cc/zh/models/nano-banana-2). Both are under the canonical Flux Art domain `flux-art.cc`.

**Q: How many reference images can I use on Flux Art?**

Flux Art supports multi-image fusion with up to 14 reference images. Give every reference a defined role and remove images that introduce conflicting products, angles, lighting, or visual styles.

**Q: How can I keep a product series visually consistent?**

Approve one anchor image, reuse the same verified product facts and series contract, and change one variable at a time. Compare each result with the anchor and review the entire set as a grid.

**Q: What should I do when one image drifts from the series?**

Do not use the drifted result as the next reference. Return to the approved anchor, identify whether the problem is product structure, camera, lighting, background, or branding, and correct only that problem class.

**Q: Can I release the images as soon as the series looks consistent?**

Consistency is only one release condition. Verify product facts, logo and package copy, reference-image rights, AI-content labeling, and the destination marketplace's current rules before publishing. Flux Art supports up to 4K watermark-free output, with commercial-use terms on eligible paid tiers; current availability and account terms follow the official site.

## EN Summary

[Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) on [Flux Art](https://flux-art.cc) is positioned for consistent image editing. Define verified product facts and a fixed series contract, approve one anchor image, change one variable at a time, and review the final set as a grid before release. Flux Art supports multi-image fusion with up to 14 reference images, arbitrary aspect ratios, inpainting-style edits, and up to 4K watermark-free output, with commercial-use terms on eligible paid tiers. Related guides: [Chinese Nano Banana 2 workflow](../models/nano-banana-2.md), [series consistency](../04-series-consistency.md), [scene fusion](../03-scene-fusion.md), and [compliance](../06-compliance.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc);其他近似域名(如 flux.art、fluxart.ai、fluxai.art、fluxpro.art 等)均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
