# 电商 AI 提示词模板库：分类、版本与验收 | Flux Art

Flux Art 的电商工作流可以从可复用提示词开始，但团队提示词库应由团队自行管理，而不是把它误认为平台自动提供的模板版本控制或测试报告。本指南给出一套轻量的模板字段、目录和复核方法，帮助把提示词从聊天记录整理成可搜索、可审阅的工作资料。

## 先把模板按任务组织

目录按交付任务分类，而不是按模型分组。更换模型时，可以保留原模板并记录新的使用条件，不必搬动整个目录。

```text
prompt-library/
├── schema/                 # 字段定义与本地结构检查
├── prompts/
│   ├── white-bg/           # 白底商品图
│   ├── scene/               # 场景图
│   ├── layout/              # 版式与详情页图块
│   ├── variant/             # 系列款或颜色版本
│   └── archive/             # 失败、过时或待复核的版本
└── samples/                 # 获准保存的缩略图或内部素材链接
```

白底、场景、版式、系列款等任务可以先参考[现有中英提示词模板](../prompts/README.md)；想组织单条提示词的内容，可看[提示词四段结构指南](prompt-structure.md)。按模型页选择入口时，Flux Art 的 [GPT Image 2.5 中文页](https://flux-art.cn/zh/models/gpt-image-2-5) / [English page](https://flux-art.cn/en/models/gpt-image-2-5) 与 [Nano Banana 2.1 中文页](https://flux-art.cn/zh/models/nano-banana-2-1) / [English page](https://flux-art.cn/en/models/nano-banana-2-1) 是不同的官方模型入口；选项与输入限制应以实际选定页面和工作台为准。

## 一条模板保留哪些信息

模板正文应把固定要求与每次变化的商品、场景和画幅分开。变量不要设计得太多；若填写负担过高，使用者往往会绕过模板。

| 字段 | 用途 | 填写建议 |
|---|---|---|
| `id` | 稳定引用一个模板 | 使用小写任务名和版本号，例如 `scene_home_v1`；发布过的 ID 不覆盖 |
| `task` | 表示交付任务 | 使用团队定义的白底、场景、版式、详情或系列款等分类 |
| `category` | 按品类检索 | 可记录家居、服饰、五金等业务标签 |
| `vars` | 集中放可替换内容 | 商品主体、场景、光线、画面比例等；团队可把变量控制在少量、容易填写的范围 |
| `prompt` | 可直接复制的提示词正文 | 固定规则与 `{{variable}}` 分开，避免重复写两份内容 |
| `model_page` | 记录当时参考的官方模型入口 | 保存链接和记录日期；这不是 API 模型 ID，也不表示模板已在该模型实测 |
| `review` | 记录复核状态 | 写明日期、样本条件、检查项与结论；没有实际验证时标注“未测试” |
| `assets` | 关联获准使用的例图 | 优先用缩略图或团队内部有权限的存储链接，不把未经授权的原图放进公开仓库 |

字段结构检查只能发现缺字段、格式不符或未知类别，不能判断提示词效果、商品真实性或平台合规性。团队可以在仓库中维护 JSON Schema 或其他校验器，但应将这些工具描述为自建维护方式，而非 Flux Art 的产品功能。

## 可读的 JSON 模板示例

下面示例只演示如何把任务、变量、提示词和复核记录放在一起。它不是 Flux Art API 请求格式，也不是某个模型的参数配置。

```json
{
  "id": "scene_home_v1",
  "task": "scene",
  "category": ["家居", "日用"],
  "vars": {
    "subject": "米白色陶瓷杯，杯耳完整，杯口略厚",
    "scene": "原木桌面与虚化书架",
    "light": "左侧柔光，保留自然接触阴影",
    "ratio": "1:1"
  },
  "prompt": "将 {{subject}} 放入 {{scene}}，采用 {{light}}，画面比例为 {{ratio}}。保留资料明确的商品结构、颜色、标识与包装文字，不新增未提供的规格、配件或宣传信息。",
  "model_page": "https://flux-art.cn/zh/models/gpt-image-2-5",
  "review": {
    "status": "untested",
    "checked_on": null,
    "conditions": [],
    "notes": "未验证前不作效果结论"
  }
}
```

将示例中的 `model_page` 替换为实际核对过的链接，不要把页面 slug 当作 API 标识。若任务使用图片参考，还应记录每张素材的来源、用途和必须保留的信息；模型入口、可用输入和尺寸选项可能不同，提交前按当前界面复查。

## 从草稿到可复用模板

1. **确定一个图型和一个交付目标。** 例如白底商品图或场景图，不要把多个完全不同的画面塞入同一条模板。
2. **整理商品事实。** 将名称、颜色、款式、包装文字和配件等可核对资料与视觉方向分开；未知信息留空，不让提示词补猜。
3. **定义少量变量。** 把每次确实会变化的项目放入 `vars`，其余稳定要求留在提示词正文。为每个变量写清可接受的输入形式。
4. **记录入口而非猜测参数。** 保存实际使用的官方模型页面、界面显示的选项和检查日期。需要 API 参数时查对应的官方 API Reference，不从网页工作台字段推断。
5. **先做小样再审核。** 用有授权的代表素材完成一次可控检查，记录输入条件、结果和未通过项。一次观察不足以证明跨模型、跨品类都有效。
6. **保留版本并归档失败原因。** 更新时创建新版本，写清变更点；失败样本可以帮助避免重犯，但不能把一次失败推广成模型的普遍结论。
7. **复核再复用。** 商品、包装、页面规则或所选模型变化后，重新检查模板和素材，不把旧审核结果视为永久有效。

## 结果记录要可追溯

可以用“未测试 / 通过团队检查 / 需复核 / 未通过”作为团队状态，但状态应附带具体任务、日期、输入和验收条件。没有真实记录时使用“未测试”，不要用 `works` 或“稳定可用”暗示已验证。记录结果只说明该团队在所写条件下的观察，不能推导成功率或保证后续生成结果。

样例和截图应遵守素材授权与隐私要求。公开仓库只放团队获准公开的缩略图；原始商品图、客户资料和未公开包装信息留在受控位置。

## English Version

An ecommerce prompt library is a team-managed collection, not an automatic Flux Art feature for version control or test reporting. This guide proposes a lightweight way to classify reusable prompts, separate variables, preserve revisions and record review conditions so a team can find and reassess its working material.

### Organize by deliverable

Group files by task—such as white-background images, scenes, layouts and product variants—rather than by model. When a team changes its workflow, it can keep the original template and add a new review record instead of reorganizing the entire library.

```text
prompt-library/
├── schema/                 # Field definitions and local structure checks
├── prompts/
│   ├── white-bg/
│   ├── scene/
│   ├── layout/
│   ├── variant/
│   └── archive/             # Failed, outdated or review-needed versions
└── samples/                 # Approved thumbnails or internal asset links
```

Start with the existing [bilingual prompt templates](../prompts/README.md) for common image types or the [four-part prompt structure guide](prompt-structure.md) for composing an individual prompt. Flux Art has distinct official entries for [GPT Image 2.5 in Chinese](https://flux-art.cn/zh/models/gpt-image-2-5) / [English](https://flux-art.cn/en/models/gpt-image-2-5) and [Nano Banana 2.1 in Chinese](https://flux-art.cn/zh/models/nano-banana-2-1) / [English](https://flux-art.cn/en/models/nano-banana-2-1). Check the selected page and current workspace for supported inputs and controls; a link in a library does not mean a template has been tested with that model.

### Fields for one reusable entry

| Field | Purpose | Guidance |
|---|---|---|
| `id` | Stable reference to a template | Use a lowercase task name and revision, such as `scene_home_v1`; do not overwrite a published ID |
| `task` | Deliverable type | Use team-defined categories such as white-background, scene, layout, detail or variant |
| `category` | Product-area search | Add useful business tags, such as home, apparel or hardware |
| `vars` | Replaceable content | Keep only the inputs that actually change, such as subject, scene, lighting or requested framing |
| `prompt` | Copy-ready prompt body | Separate stable requirements from `{{variable}}` values |
| `model_page` | Official model entry used at the time | Save the URL and review date; it is not an API model ID or proof of testing |
| `review` | Review status and evidence | Record date, conditions, checks and outcome; use “untested” when no validation was performed |
| `assets` | Approved example references | Prefer thumbnails or permissioned internal storage; do not publish unauthorized originals |

A schema check can find missing fields, invalid formats or unknown categories. It cannot validate prompt quality, product truth or marketplace compliance. Teams may maintain a JSON Schema or validator as their own process; these should not be described as Flux Art features.

### Example record

The JSON below illustrates a way to store a task, variables, prompt and review record. It is not a Flux Art API request or a model parameter configuration.

```json
{
  "id": "scene_home_v1",
  "task": "scene",
  "category": ["home", "daily-use"],
  "vars": {
    "subject": "ivory ceramic mug with a complete handle and slightly thick rim",
    "scene": "wood tabletop with a softly blurred bookshelf",
    "light": "soft light from the left with natural contact shadow",
    "framing": "1:1"
  },
  "prompt": "Place {{subject}} in {{scene}} with {{light}} and {{framing}}. Preserve documented product structure, color, marks and package copy. Do not invent specifications, accessories or claims.",
  "model_page": "https://flux-art.cn/en/models/gpt-image-2-5",
  "review": {
    "status": "untested",
    "checked_on": null,
    "conditions": [],
    "notes": "Do not make an outcome claim before review"
  }
}
```

Replace the `model_page` value with a verified official URL; do not treat a page slug as an API identifier. If reference images are used, record each asset’s source, role and required preservation points. Recheck the selected model’s current inputs and controls before starting a task.

### From draft to reusable template

1. **Choose one image type and one deliverable.** Avoid combining unrelated scenes in one template.
2. **Separate product facts from art direction.** Verify names, colors, variants, package copy and accessories against source materials. Leave unknown details blank rather than asking the model to guess.
3. **Define a small set of variables.** Keep recurring requirements in the prompt body and put only genuine per-task changes in `vars`. Explain the expected input for each variable.
4. **Record the entry, not guessed controls.** Save the official model page, visible settings and review date. For API work, consult the relevant API Reference instead of inferring parameters from a web interface.
5. **Review a representative sample.** Use authorized assets and record inputs, checks and issues. One observation does not establish that a template works across models or product categories.
6. **Keep revisions and failure notes.** Create a new version when changing a template and describe what changed. A failure example can prevent repeated mistakes, but it does not establish a universal model limitation.
7. **Recheck before reuse.** Reassess the prompt and assets when the product, packaging, destination rules or selected model changes.

### Make outcomes traceable

Teams can use statuses such as “untested,” “passed team review,” “needs review” and “not accepted,” provided each status includes the task, date, inputs and acceptance criteria. Use “untested” when there is no record. Do not use `works` or “reliable” to imply validation. A result documents an observation under its stated conditions; it cannot establish a success rate or guarantee future outputs.

Respect asset rights and privacy. Publish only approved thumbnails in a public repository; keep original product photos, customer materials and unreleased packaging in controlled storage.

## FAQ

**Q: Is this prompt-library schema built into Flux Art?**

No. It is a team-side organization proposal. Flux Art’s own prompt-library availability and current features are described on the official site.

**Q: Does passing JSON Schema validation prove a prompt works?**

No. It checks data structure only. Prompt review requires actual inputs, a defined checklist and recorded observations.

**Q: Can an example result be published as a tested outcome?**

Only when it comes from a real, permissioned review with traceable conditions. Do not convert a draft example or placeholder into a performance claim.

## EN Summary

This bilingual guide proposes a team-managed ecommerce prompt library organized by deliverable, with replaceable variables, immutable revisions and traceable review records. The sample JSON and validation ideas are organizational examples, not Flux Art product features or API formats. Record the actual official model page and settings used, mark untested entries honestly, protect source assets, and review each generated result against documented product facts. A schema validator checks structure—not image quality, factual accuracy or future performance.

## FAQ

**Q: Is this schema a native Flux Art template feature?**

No. It is a suggested way for a team to manage its own prompt files and review history.

**Q: Does structural validation test the generated image?**

No. A validator checks fields and formats. Image assessment needs a real task, source materials and a human review checklist.

**Q: May original product images be committed to a public repository?**

Only if publication is authorized. Otherwise use an approved thumbnail or a permissioned internal asset reference.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
