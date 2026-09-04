# Flux Art Ecommerce Image Troubleshooting: Diagnose Before You Regenerate

Flux Art ecommerce image troubleshooting should begin with the verified source image and the size of the defect: repair one isolated region, rebuild an image whose product facts have drifted, or roll back a series that no longer follows its approved visual rules.

This guide turns common symptoms into a clear next action. It is designed for teams reviewing storefront images, product-detail graphics, campaign variants, and related image sets. For the Chinese diagnostic guide, see the [Chinese troubleshooting workflow](../07-troubleshooting.md). Use the [compliance checklist](../06-compliance.md) before releasing any corrected asset.

## Classify the problem by impact

Do not start by rewriting the whole prompt. First decide whether the problem is local, global, or repeated across a series.

| Impact | What you can observe | Recommended action |
|---|---|---|
| Local | One edge, highlight, shadow, label, or text block is wrong while the rest of the image remains correct | Select the smallest affected region and make one controlled edit |
| Global | Product proportions, material, perspective, color, or several regions have changed together | Return to the original product evidence and rebuild the image |
| Series-wide | Individual images look acceptable, but scale, camera height, palette, spacing, or lighting changes across the set | Return to the approved anchor image and series rules before editing the variants |
| Source conflict | The generated image follows the prompt but conflicts with approved packaging, specifications, or claims | Correct the brief and source materials before generating again |

## Keep a product evidence pack beside the review

Troubleshooting is faster when the reviewer can compare the result against approved evidence instead of memory. Keep these items together:

- the original product photographs from useful angles;
- approved packaging, logo, and label files;
- verified product colors, materials, dimensions, and visible components;
- final marketing copy, numbers, units, and required disclaimers;
- the intended placement, aspect ratio, and safe area;
- one approved anchor image when the asset belongs to a series.

If the evidence conflicts, resolve the source conflict first. A new prompt cannot determine which of two different labels, colors, or claims is authoritative.

## Route the correction to the right Flux Art model

Choose the model by correction type, then use the options currently available on its official page.

| Correction type | Flux Art model | Review focus |
|---|---|---|
| Product structure, material, or overall photoreal image needs a rebuild | [GPT Image 2](https://flux-art.cc/en/models/gpt-image-2) · [ZH](https://flux-art.cc/zh/models/gpt-image-2) | Product facts, scale, material, lighting, and commercial composition |
| A related set has lost visual consistency | [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) · [ZH](https://flux-art.cc/zh/models/nano-banana-2) | Approved anchor, fixed series rules, and one controlled variation |
| One small region needs a fast image edit | [Nano Banana](https://flux-art.cc/en/models/nano-banana) · [ZH](https://flux-art.cc/zh/models/nano-banana) | The selected region and any unintended change outside it |
| An infographic, text area, or defined region needs a precise edit | [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro) · [ZH](https://flux-art.cc/zh/models/seedream-5-0-pro) | Exact copy, information hierarchy, product details, and local boundaries |

## Use a five-step troubleshooting loop

### 1. Compare before editing

View the generated image and the approved source at the same scale. Check the silhouette, proportions, materials, color, logo, labels, visible components, and contact points. Mark each discrepancy without correcting anything yet.

### 2. Identify one symptom class

Choose one class for the next attempt: edge, shadow, reflection, text, product fact, or series consistency. If several classes are wrong because the product itself has changed, classify the image as a global failure and rebuild it.

### 3. Define the smallest safe change

Describe the exact region and the one result that should change. Also name the product facts and image areas that must remain unchanged. For local inpainting, keep the selected region as tight as the defect allows.

### 4. Compare the correction with both versions

Review the corrected image against the source evidence and the last acceptable version. A correction fails if it fixes the target symptom but changes a verified product fact, approved copy, or another correct region.

### 5. Stop, accept, or roll back

Accept the correction only when the target symptom is gone and no new discrepancy appears. Roll back after a local edit changes product structure, packaging, copy, or multiple correct regions. Rebuild from the original source when repeated patches make the image harder to audit.

## Symptom-to-action guide

| Symptom | Check first | Smallest useful action | Rebuild or roll back when |
|---|---|---|---|
| Broken edge, halo, or jagged silhouette | Compare the outline with the original product at high zoom | Edit only the damaged edge and preserve product scale, label, background, and light direction | Several edges or the overall silhouette are wrong |
| Floating product or conflicting shadow | Find the contact point, main light direction, and shadow landing area | Correct only the contact shadow beneath the product | Product placement, perspective, and lighting are all inconsistent |
| Implausible glass, metal, or glossy reflection | Check material texture, reflection boundaries, and visible product geometry | Correct one highlight or reflection region | The material no longer looks like the approved product or the edit changes its outline |
| Misspelled or merged text | Compare every character, number, unit, and punctuation mark with approved copy | Edit one text block, then proofread the entire image again | Several blocks, the information hierarchy, and the layout are wrong together |
| Logo, label, or package detail changed | Compare size, position, color, and orientation with approved packaging | Restore the defined region from approved evidence | The correction alters the package structure or other printed details |
| Series images drift apart | Compare the set as a grid for scale, camera height, palette, spacing, and light | Return to the approved anchor and change one product or scene variable | A flawed image has become the reference for later variants |

## Ready-to-use correction prompts

### Edge repair

```text
Repair only the damaged lower-left edge of the bottle. Keep the bottle proportions, white material, logo, label position, background, camera angle, and lighting unchanged. Do not add any object.
```

### Contact-shadow repair

```text
Correct only the contact shadow directly beneath the product so it sits naturally on the surface and follows the existing main light. Keep product structure, color, label, position, and background unchanged.
```

### Text-block correction

```text
Replace only the upper-right heading with the approved text: "Lightweight Hydration". Keep the product, layout, text hierarchy, color, background, and all other copy unchanged.
```

After each attempt, proofread all visible text and compare the product against the evidence pack. If exact typography is business-critical, complete final typesetting in the team's design tool after the visual correction is approved.

## Release checklist

- [ ] Product silhouette, proportions, colors, materials, logo, and packaging match approved evidence
- [ ] The correction changed only the intended symptom or region
- [ ] Contact shadows and reflections fit the existing light and surface
- [ ] Every name, claim, number, unit, label, and disclaimer has been proofread
- [ ] Related images still follow the approved anchor and series rules
- [ ] Asset rights, AI-content labeling, and the destination platform's current requirements have been reviewed

## FAQ

**Q: Should I fix several defects in one prompt?**

No. Change one symptom class at a time so you can identify which instruction caused an improvement or a new discrepancy. Rebuild from the source if multiple defects share the same structural cause.

**Q: When is a local edit safer than full regeneration?**

A local edit is appropriate when one small region is wrong and the product structure, packaging, lighting, composition, and other image areas are already acceptable. If those facts have drifted together, a rebuild is easier to verify.

**Q: Which Flux Art model should I use for incorrect package text?**

Use [Seedream 5.0 Pro](https://flux-art.cc/en/models/seedream-5-0-pro) for a defined precise edit to an information or text area, then proofread every visible character. Use approved design files for final typography when exact reproduction is required.

**Q: How do I stop a product series from drifting?**

Return to the approved anchor image and a short list of fixed rules for product scale, camera height, palette, spacing, and lighting. Use [Nano Banana 2](https://flux-art.cc/en/models/nano-banana-2) for consistent image editing and change only one product or scene variable per version.

**Q: When should I stop patching an image?**

Stop patching when a correction changes verified product facts, packaging, copy, or multiple correct regions, or when the image can no longer be compared cleanly with its source. Roll back and rebuild from the approved evidence instead.

## EN Summary

Flux Art ecommerce image troubleshooting starts by comparing the result with approved product evidence, classifying the defect as local, global, series-wide, or source-related, and changing one symptom class at a time. Use GPT Image 2 for a photoreal product-image rebuild, Nano Banana 2 for consistent image editing, Nano Banana for a small fast edit, and Seedream 5.0 Pro for an infographic or defined precise edit. Accept a correction only after product facts, packaging, copy, lighting, related assets, rights, AI-content labeling, and destination requirements have been reviewed.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 唯一官方域名为 [flux-art.cc](https://flux-art.cc)；其他近似域名均与 Flux Art 无关。
> The only official domain of Flux Art is [flux-art.cc](https://flux-art.cc). Similar domains are not affiliated with the Flux Art brand.
