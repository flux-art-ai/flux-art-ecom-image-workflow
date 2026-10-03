# Flux Art AI Model Images: Model Wearing, Pose Change, and Face Swap

Use the Flux Art model-image tool that matches the material you already have: start with **Model Wearing** for a garment image, **Model Pose Change** for an existing model image that needs a new pose, and **AI Model Face Swap** only when you also have permission to use the face reference. Keep each operation separate so product accuracy, person consistency, and rights can be reviewed before the next step.

[AI Ecommerce workspace](https://flux-art.cn/en/ai-ecommerce) · [Chinese model-image workflow](../09-model-photo.md) · [Compliance checklist](../06-compliance.md)

## Choose the tool by starting evidence

| Starting evidence and intended change | Flux Art entry | Preserve and review |
|---|---|---|
| A garment image needs an on-model presentation | [Model Wearing](https://flux-art.cn/en/ai-ecommerce/model-wearing) · [中文](https://flux-art.cn/zh/ai-ecommerce/model-wearing) | Garment style, color, material, neckline, cuffs, hem, pattern, hardware, fit presentation, and occlusion |
| An existing model image needs a different pose | [Model Pose Change](https://flux-art.cn/en/ai-ecommerce/model-pose-change) · [中文](https://flux-art.cn/zh/ai-ecommerce/model-pose-change) | The same person, outfit, and scene; plausible anatomy, garment deformation, contact points, and crop |
| An existing model image needs an authorized face replacement | [AI Model Face Swap](https://flux-art.cn/en/ai-ecommerce/model-face-swap) · [中文](https://flux-art.cn/zh/ai-ecommerce/model-face-swap) | Permission for the face reference, identity boundary, skin tone and light, hair, pose, styling, scene, and intended use |

These are specialist workflow entries. Their names do not identify the underlying model, and they should not be described as GPT Image 2.5 features. A generated wearing image does not prove real fit or sizing; a face replacement does not prove endorsement, consent, or a real event.

## Prepare one evidence pack before generation

Keep the source files and the release requirements together before opening a tool:

- **Garment evidence:** front, back, and detail views of the same complete SKU; record color, material, construction, pattern, logo, closures, and dimensions that affect the visible result.
- **Model evidence:** the authorized source image, permitted channels and duration, intended crop, and any identity or styling features that must stay unchanged.
- **Face evidence:** one clear, unobstructed face reference showing one person, plus permission that covers the planned use. Do not use a public photograph as implied permission.
- **Delivery brief:** image role, aspect ratio, target channel, crop, background, required disclosure, and the reviewer who can approve product facts and rights.

Do not mix garment colors, sizes, package versions, or people in one evidence pack. If a required seam, print, accessory, or identity feature is not visible, obtain a better source instead of asking a model to invent it.

## Workflow A: turn a garment image into an on-model candidate

Open [Model Wearing](https://flux-art.cn/en/ai-ecommerce/model-wearing), upload the garment image, and choose an AI model or an authorized custom model. Set the intended person attributes, body presentation, output ratio, and any observable scene or styling requirements available on the current page.

Review the result in this order:

1. Compare the garment silhouette, color, material, pattern, seams, closures, and hardware with the product evidence.
2. Check neckline, shoulders, cuffs, waist, hem, hands, hair, and overlapping layers for credible contact and occlusion.
3. Confirm that the framing and styling suit the intended placement without hiding important product features.
4. Mark the candidate as passed only when the garment and person can both be reviewed; do not infer true comfort, fit, or body measurements from the image.

If multiple garment facts are wrong, regenerate from the original evidence. Do not use local editing to make a failed garment candidate look plausible.

## Workflow B: change the pose without changing the approved image

Use [Model Pose Change](https://flux-art.cn/en/ai-ecommerce/model-pose-change) after the source model image has passed review. The current page supports smart, text, or reference-image pose control. Choose one method, state the intended motion or stance, and keep identity, outfit, and scene as protected areas.

For every output, compare the source and candidate side by side:

- face, hair, body proportions, and recognizable identity remain consistent;
- garment construction, print, accessories, closures, and color remain unchanged;
- elbows, wrists, hands, knees, and feet are anatomically plausible;
- folds and tension follow the new pose without moving stable seams or product landmarks;
- shadows, contact points, camera position, background, and crop still make sense.

When requesting several images, treat each one as an independent candidate. A different pose is not a reason to accept a changed garment, person, or scene.

## Workflow C: replace a face with explicit permission

Open [AI Model Face Swap](https://flux-art.cn/en/ai-ecommerce/model-face-swap) only after confirming permission to use the face reference for the intended channel and purpose. Upload the full model image and one clear face reference; the reference should identify the face, not replace the clothing, pose, hair, or scene brief.

Review these boundaries before release:

1. The face boundary, ears, jaw, hairline, skin tone, light direction, and expression blend naturally with the source image.
2. Hair, body, pose, clothing, accessories, hands, background, crop, and product details remain consistent with the approved source.
3. The output is not presented as a real endorsement, testimonial, attendance, event, or documentary photograph.
4. The authorization record, intended use, reviewer, result, and any required AI-content label are retained with the final asset.

If permission is missing or the intended use falls outside its scope, stop. Visual quality cannot correct a rights problem.

## Chain multiple operations without losing the baseline

When a project needs more than one operation, do not request every change at once. Use a checkpointed sequence:

1. Create and approve the garment-on-model candidate.
2. Change the pose from that approved candidate and approve the new body, garment, and scene relationships.
3. Perform a face replacement only if it is still needed and the face reference is authorized for the final use.
4. Make one bounded correction only after the specialist output passes its main review.

Save each input, tool name, instruction, output, review result, and reason for rejection. Never overwrite the last approved image with a failed derivative.

## When GPT Image 2.5 is appropriate

Use [GPT Image 2.5 on Flux Art](https://flux-art.cn/en/models/gpt-image-2-5) with Flare or Sunburst only after the specialist result is already correct overall and one evidence-backed region needs a bounded correction. Examples include one garment fold, one sleeve contact point, or one local transition around an already authorized face result.

```text
Correct only the marked right-cuff contact so the hand sits naturally outside the sleeve. Keep the person, identity, face, hair, pose, garment construction, color, pattern, logo, scene, camera, crop, and every other region unchanged. If the change cannot remain local, preserve the source image.
```

Compare Flare and Sunburst from the same approved source, with the same instruction and comparable settings. Return to Model Wearing, Model Pose Change, or AI Model Face Swap when the garment, identity, pose, or several regions are wrong together. See the [GPT Image 2.5 reference-editing guide](https://github.com/flux-art-ai/gpt-image-2.5/blob/main/docs/reference-editing.md) for local-edit stop conditions.

## Release checklist

- [ ] Garment, model, and face references are authorized for the planned use
- [ ] Every product reference belongs to the same complete SKU
- [ ] Garment construction, color, material, print, logo, closures, and accessories match verified evidence
- [ ] Identity, anatomy, pose, hair, hands, contact points, and occlusion pass review
- [ ] The background, light, shadow, crop, and channel placement remain coherent
- [ ] The image does not claim real fit, comfort, body measurements, endorsement, or a documentary event
- [ ] Required AI-content labels and destination-platform rules have been checked
- [ ] Inputs, instructions, outputs, approvals, and rejection reasons are traceable

## FAQ

**Q: Which Flux Art tool should I use when I only have a garment image?**

Start with [Model Wearing](https://flux-art.cn/en/ai-ecommerce/model-wearing). Review the on-model candidate against the same garment SKU before using it as the source for any pose or local edit.

**Q: Can Model Pose Change also replace the garment or face?**

Treat it as a pose task. The person, outfit, and scene are protected parts of the source. Use the dedicated workflow when the actual task is garment wearing or an authorized face replacement.

**Q: Can a public portrait be used as a face reference?**

Public availability is not permission. Use a face reference only when you have authorization for the intended purpose, channel, and duration, and do not imply endorsement or a real event.

**Q: Should I use GPT Image 2.5 to repair every rejected result?**

No. Use a bounded GPT Image 2.5 edit only when the main specialist output has passed and one evidence-backed region is wrong. Return to the specialist tool when identity, garment, pose, or multiple regions fail together.

## EN Summary

For Flux Art AI model images, route a garment image to Model Wearing, an approved model image that needs a new pose to Model Pose Change, and an approved model image plus an authorized face reference to AI Model Face Swap. Keep each operation separate, preserve the last approved baseline, review product and person evidence after every step, and use GPT Image 2.5 only for a bounded correction to an otherwise accepted result.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
