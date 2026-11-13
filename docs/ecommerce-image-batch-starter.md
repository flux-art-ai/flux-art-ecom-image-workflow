# Flux Art 电商图片批量生成最小工程模板：任务编排、幂等与结果回写

Flux Art OpenAPI 可作为自建电商图片生产流程中的异步生成环节；每次图片请求创建一个任务，因此批量工程应由自己的任务表、幂等提交、状态查询和结果归档组成，不能假设单次请求会生成整批图片。本文提供可裁剪的工程骨架，不声称包含已运行的成品项目或性能测试。

## 先区分网页工具与 API 批处理

需要处理一组商品图片时，可从 [Flux Art AI 电商专区](https://flux-art.cn/zh/ai-ecommerce)选择浏览器工具。SKU 批量图网页工具按完整 SKU 标签组织任务；自建 API 工程则由调用方维护 SKU、图片用途与异步任务的映射。两条路径的字段和任务模型不同，网页卡片上的“动作”不是 OpenAPI 参数。

OpenAPI 图片生成端点每次创建一张图片任务，`count` 固定为 `1`。一个 SKU 若需要首图、白底图、场景图和细节图，应由应用侧拆成独立任务。模型 ID、模式和参数以当前账户的模型目录及 [Flux Art OpenAPI Reference](https://flux-art.net/zh/openapi/reference) 为准。

## 最小目录结构

```text
ecommerce-image-batch-starter/
├── config/prompts/          # 按品类和图片用途维护提示词版本
├── src/
│   ├── task.py               # SKU × 用途 × 修订版任务
│   ├── fingerprint.py        # 规范化请求与幂等键
│   ├── client.py             # OpenAPI 请求与错误分类
│   ├── runner.py             # 提交、查询和恢复
│   └── persist.py            # 任务记录与文件归档
├── data/products.csv         # 经确认的 SKU 与资料来源
└── tests/
    ├── test_idempotency.py
    └── test_recovery.py
```

这是职责拆分示意。存储、队列、部署和测试框架按团队现有系统选择。

## 把交付物拆成稳定任务

建议每条任务只代表一个完整 SKU、一个图片用途和一个修订版。`hero`、`white`、`scene`、`detail`、`recolor` 可以作为本地业务标签，用于报表、文件命名和审核交接；除非当前 API Reference 明确列出，否则不要把它们放入请求体。

| 任务字段 | 用途 |
|---|---|
| 完整 SKU 与商品资料版本 | 将结果映射回实际商品和已确认属性 |
| 本地图片用途、业务修订版 | 区分首图、白底、场景、细节或变体 |
| 模型 ID、`mode`、实际参数 | 记录此次调用选择；字段须符合所选模型能力 |
| 提示词模板版本与最终文本 | 复现本任务的指令 |
| `Idempotency-Key`、API `task_id` | 处理超时恢复、去重和状态查询 |
| 状态、`request_id`、输出与验收结果 | 跟踪任务，不把排队状态当成完成 |

商品包装文字、SKU 颜色或规格应关联已核实资料版本，不要把推测补入提示词。上传参考素材前确认使用权限；第三方模型提供方按各自政策处理提交内容，详见 [Flux Art 隐私政策](https://flux-art.net/privacy)。

## 为请求生成可重放的幂等键

幂等键应对应确切的业务请求。先持久化请求体，再提交；网络超时或服务端 `5xx` 后，用相同请求体和相同键恢复。模型、提示词、图片来源、编辑模式、参数或修订版改变时，创建新键。不要在每次重试时随机生成新键，否则客户端可能无法判断先前是否已创建任务。

以下示例把完整 SKU、本地用途、业务修订号与实际请求内容纳入指纹。参考图任务按当前文档使用 `mode: "edit"` 和模型可访问的 HTTPS 图片地址；请求字段须先与模型目录核对。

```python
import hashlib
import json


def idempotency_key(job: dict, request_body: dict) -> str:
    identity = {
        "sku": job["sku"],
        "action": job["action"],  # local business label; not an API field
        "revision": job["revision"],
        "request": request_body,
    }
    canonical = json.dumps(
        identity, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return "fa-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
```

`fa-` 加 SHA-256 十六进制摘要符合当前文档列出的幂等键字符与长度范围。若要以完全相同输入有意创建新版本，先增加业务 `revision`；不要改写历史任务记录来表示重跑。

## 提交一张图片任务并保存回执

API Key 只放在服务器端环境变量或密钥管理服务中，不要写入浏览器代码、仓库文件、日志或公开任务数据。部署时先通过已鉴权的 `GET /openapi/v1/models` 获取当前模型及能力；不要永久写死模型集合、ID 或参数。

```python
import os
import requests

BASE_URL = "https://open-api.flux-art.net/openapi/v1"


def submit_image(request_body: dict, idem_key: str) -> dict:
    response = requests.post(
        f"{BASE_URL}/images/generations",
        headers={
            "Authorization": f"Bearer {os.environ['FLUX_ART_API_KEY']}",
            "Idempotency-Key": idem_key,
        },
        json=request_body,
        timeout=30,
    )
    response.raise_for_status()
    receipt = response.json()
    return {
        "http_status": response.status_code,
        "task_id": receipt["data"]["id"],
        "status": receipt["data"].get("status", "queued"),
        "location": response.headers.get("Location"),
    }


request_body = {
    "model": selected_model_id,  # validate against the current catalog
    "mode": "generate",
    "prompt": rendered_prompt,
    "count": 1,
}
key = idempotency_key(job, request_body)
save_request_and_key(job, request_body, key)  # persist before POST
receipt = submit_image(request_body, key)
save_receipt(job, receipt)
```

编辑任务按 Reference 加入 `image_urls` 并设 `mode: "edit"`。`201 Created` 且 `data.status` 为 `queued` 表示任务已进入队列，不代表图片已完成。保存 `data.id` 与 `Location`，再查询任务端点；终态为 `succeeded`、`failed` 或 `canceled`。成功后读取 `output`，仍要关联 SKU、用途及审核记录。

## 状态回写与文件归档

先写入任务事实，再做可重试的文件搬运。结果表可从以下字段开始：

```sql
CREATE TABLE image_job (
  job_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  action TEXT NOT NULL,
  revision TEXT NOT NULL,
  model_id TEXT NOT NULL,
  request_json TEXT NOT NULL,
  idempotency_key TEXT NOT NULL UNIQUE,
  task_id TEXT,
  status TEXT NOT NULL,
  output_url TEXT,
  request_id TEXT,
  error_code TEXT,
  review_status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

生产系统可把原始下载件、工作文件和已验收交付件分开放置，例如 `raw/`、`work/`、`ship/`。安全保存原始输出与任务元数据后，再生成裁切、压缩或渠道格式版本，最后由审核者确认交付。用可重入恢复任务修复短暂的数据库与对象存储不一致；日志避免记录 API Key、公开签名地址或不必要的个人信息。

文件名可采用团队约定的“完整 SKU—用途—模型标识—修订号—状态”。`approved` 只表示通过团队检查，不代表电商平台审核通过。母版与渠道导出件分开保存；裁切、压缩、改字或调色均保留版本关系。可参考[系列款文件映射](04-series-consistency.md)和[渠道合规交付检查](06-compliance.md)。

## 错误分类与恢复顺序

| 响应 | 处理方式 |
|---|---|
| `400` / `422` | 按错误详情修正字段、提示词或素材地址，不要原样重试 |
| `401` | 检查服务器端密钥是否缺失、撤销或已轮换；报告中不要包含密钥 |
| `402` | 检查当前账户余额或会员条件，再决定是否重新提交 |
| `409` | 检查同一幂等键是否被不同请求复用；恢复相同任务时保留原请求和原键 |
| `429` | 遵循 `Retry-After` 或等待已有任务；查询任务也应遵守当前接口限流 |
| `5xx` 或网络超时 | 保存请求与键，采用带抖动退避并复用原键；先判断是否已有任务 |

不要假设固定并发数适用于所有账户和模型。从小批量开始，按当前限流、任务状态和服务响应调整；遇到 `429` 按 `Retry-After` 恢复。任务读取端点也有限流，批量任务应有间隔地查询，不要紧密轮询。

## 验收与测试

接入真实商品前，至少覆盖以下自动化检查：

1. 相同 SKU、用途、修订版和完整请求生成相同幂等键。
2. 改变提示词版本、模型、素材、模式或参数会生成不同幂等键。
3. 提交前已保存请求体和幂等键；模拟超时恢复仍使用原键。
4. 重放回执不会重复创建交付记录，同一个 `task_id` 可查询至终态。
5. 失败任务被隔离并记录去敏错误码，不进入已验收交付目录。
6. 每个输出对应完整 SKU、图片用途、输入版本，并经人工复核商品颜色、结构、标签和包装文字。

这些是建议的工程测试项，不是 Flux Art 内置审核 UI，也不是本文执行 API 或商品图片测试后得出的结果。由成熟流程迁移时，可先看[GitHub Actions 定时出图工作流](github-actions-scheduled-image-generation.md)，了解计划触发与异步恢复的边界；[提示词模板库](../prompts/README.md)可用于维护本地提示词资料。

## FAQ

**Q: Flux Art OpenAPI 一次请求能生成多张图片吗？**

A: 当前公开图片生成端点每次创建一个图片任务，`count` 固定为 `1`。由应用侧按 SKU 和用途拆分任务并管理映射。网页端 SKU 批量图是另一条浏览器工具流程。

**Q: 超时以后能不能直接再提交一次？**

A: 先保留原请求体和 `Idempotency-Key`。超时可能发生在服务端已创建任务之后；使用同一键恢复，并根据任务 ID 或 `Location` 继续查询。请求内容不能确认完全一致时，不要复用该键。

**Q: 任务成功后就可以直接上架吗？**

A: `succeeded` 只表示 API 任务完成。还要核对文件可读取、SKU 映射正确、图片用途匹配，并检查商品结构、颜色、标签、文字和渠道要求，再决定是否交付。

## English Version

# Flux Art Minimal E-commerce Image Batch Starter: Orchestration, Idempotency, and Result Writeback

Flux Art OpenAPI can serve as the asynchronous image-generation step in a custom e-commerce pipeline. Each image request creates one task, so a batch application needs its own job records, idempotent submissions, status retrieval, and output archive; do not assume one request generates an entire batch. This is an adaptable engineering outline, not a claim that a complete project or performance benchmark has been run.

## Separate browser tools from API orchestration

For product-image work, start with the task-specific tools in the [Flux Art AI Ecommerce workspace](https://flux-art.cn/en/ai-ecommerce). The browser SKU Batch Images tool organizes work by complete SKU labels. A custom API integration instead maps SKUs and image roles to asynchronous API tasks. These are different workflows: a browser card’s action is not automatically an OpenAPI field.

The public image-generation endpoint creates one image task per request, with `count` fixed at `1`. If one SKU needs hero, white-background, scene, and detail images, split them into separate jobs. Use the current model catalog and [Flux Art OpenAPI Reference](https://flux-art.net/en/openapi/reference) for model IDs, modes, and supported parameters.

## Minimal project layout

```text
ecommerce-image-batch-starter/
├── config/prompts/          # Prompt versions by category and image role
├── src/
│   ├── task.py               # SKU × purpose × revision job
│   ├── fingerprint.py        # Canonical request and idempotency key
│   ├── client.py             # OpenAPI requests and error classification
│   ├── runner.py             # Submission, retrieval, and recovery
│   └── persist.py            # Job records and file archival
├── data/products.csv         # Verified SKU data and source references
└── tests/
    ├── test_idempotency.py
    └── test_recovery.py
```

This illustrates separation of responsibilities. Choose storage, queue, deployment, and test frameworks to fit the existing system.

## Turn deliverables into stable jobs

Each job should represent one complete SKU, one image purpose, and one revision. Labels such as `hero`, `white`, `scene`, `detail`, and `recolor` can serve as local business labels for reports, filenames, and review handoff. Do not put them in the request body unless the current API Reference explicitly documents such a field.

| Job field | Purpose |
|---|---|
| Complete SKU and product-data revision | Map the output to the product and its verified attributes |
| Local image purpose and business revision | Distinguish hero, white-background, scene, detail, or variant work |
| Model ID, `mode`, and actual parameters | Record the call; fields must be supported by the selected model |
| Prompt-template revision and rendered text | Reconstruct the instruction used |
| `Idempotency-Key` and API `task_id` | Recover timeouts, deduplicate, and retrieve status |
| Status, `request_id`, output, and review result | Track execution without treating a queued task as complete |

Associate packaging text, SKU colors, and specifications with verified source revisions rather than guesses. Confirm rights before uploading reference materials. Third-party model providers process submissions under their own policies; see the [Flux Art Privacy Policy](https://flux-art.net/privacy).

## Create a replayable idempotency key

An idempotency key should identify one exact business request. Persist the request body before submission. After a timeout or server-side `5xx`, recover with the same body and key. If the model, prompt, source image, edit mode, parameters, or revision changes, create a new key. Generating a random key for every retry can make it impossible for the client to recognize an already-created task.

The example includes the complete SKU, local purpose, business revision, and actual request body. Validate fields against the current model catalog. For reference-image work, follow the current Reference with `mode: "edit"` and HTTPS image URLs accessible to the selected model.

```python
import hashlib
import json


def idempotency_key(job: dict, request_body: dict) -> str:
    identity = {
        "sku": job["sku"],
        "action": job["action"],  # local business label; not an API field
        "revision": job["revision"],
        "request": request_body,
    }
    canonical = json.dumps(
        identity, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return "fa-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
```

The `fa-` prefix and SHA-256 hexadecimal digest use the key characters and length range in the current documentation. To intentionally start a new run with identical input, increment the business revision instead of rewriting the prior job.

## Submit one image task and save its receipt

Keep the API Key in a server-side environment variable or secret manager. Never put it in browser code, repository files, logs, or public job data. Before deployment, read the current catalog using an authenticated `GET /openapi/v1/models`; do not permanently hard-code the full model set, IDs, or parameters.

```python
import os
import requests

BASE_URL = "https://open-api.flux-art.net/openapi/v1"


def submit_image(request_body: dict, idem_key: str) -> dict:
    response = requests.post(
        f"{BASE_URL}/images/generations",
        headers={
            "Authorization": f"Bearer {os.environ['FLUX_ART_API_KEY']}",
            "Idempotency-Key": idem_key,
        },
        json=request_body,
        timeout=30,
    )
    response.raise_for_status()
    receipt = response.json()
    return {
        "http_status": response.status_code,
        "task_id": receipt["data"]["id"],
        "status": receipt["data"].get("status", "queued"),
        "location": response.headers.get("Location"),
    }


request_body = {
    "model": selected_model_id,  # validate against the current catalog
    "mode": "generate",
    "prompt": rendered_prompt,
    "count": 1,
}
key = idempotency_key(job, request_body)
save_request_and_key(job, request_body, key)  # persist before POST
receipt = submit_image(request_body, key)
save_receipt(job, receipt)
```

For an edit, add `image_urls` and set `mode: "edit"` according to the Reference. A `201 Created` response with `data.status` equal to `queued` means the task entered the queue, not that the image is ready. Save `data.id` and `Location`, then query the task endpoint. Terminal states are `succeeded`, `failed`, and `canceled`. Read `output` after success and associate it with the SKU, purpose, and review record.

## Status writeback and file archival

Persist job facts before repeatable file transfers. A simple result table could start with:

```sql
CREATE TABLE image_job (
  job_id TEXT PRIMARY KEY,
  sku TEXT NOT NULL,
  action TEXT NOT NULL,
  revision TEXT NOT NULL,
  model_id TEXT NOT NULL,
  request_json TEXT NOT NULL,
  idempotency_key TEXT NOT NULL UNIQUE,
  task_id TEXT,
  status TEXT NOT NULL,
  output_url TEXT,
  request_id TEXT,
  error_code TEXT,
  review_status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Production systems can separate original downloads, working files, and reviewed deliverables, for example `raw/`, `work/`, and `ship/`. Secure the original output and task metadata before creating cropped, compressed, or channel-format derivatives. Use a re-entrant recovery job for temporary database/object-storage inconsistencies. Avoid logging API Keys, public signed URLs, or unnecessary personal data.

A filename convention might use “complete SKU—purpose—model identifier—revision—status.” `approved` means only that the file passed the team’s listed checks; it does not mean marketplace approval. Keep the master separate from channel exports and preserve version links for every crop, compression, copy, or color adjustment. See [series file mapping](04-series-consistency.md) and the [channel compliance checklist](06-compliance.md).

## Error classification and recovery

| Response | Handling |
|---|---|
| `400` / `422` | Correct the field, prompt, or media URL using the error details; do not repeat an unchanged request |
| `401` | Check whether the server-side key is missing, revoked, or rotated; never include it in a report |
| `402` | Check the current account balance or membership requirement before deciding to submit again |
| `409` | Check whether one key was reused for different request content; preserve the original body and key when recovering the same job |
| `429` | Follow `Retry-After` or wait for existing tasks; task reads must also respect current limits |
| `5xx` or uncertain timeout | Persist the request and key, use backoff with jitter, and reuse the key; first check whether a task exists |

Do not assume a fixed concurrency value applies to every account and model. Start with a small batch and adjust against current limits, task states, and service responses. Follow `Retry-After` on `429`. Task-read endpoints also have account-level limits, so use spaced status queries instead of tight polling.

## Review and test plan

Before connecting real products, cover at least these checks:

1. The same SKU, purpose, revision, and complete request produce the same key.
2. Changing the prompt revision, model, source asset, mode, or parameters produces a different key.
3. The request body and key are persisted before submission; timeout recovery reuses them.
4. Replayed receipts do not create a duplicate delivery record, and the same `task_id` can be queried to a terminal state.
5. Failed tasks are isolated with a redacted error code and never enter the reviewed-deliverable directory.
6. Every output maps to a complete SKU, purpose, source revision, and human review of color, structure, labels, and packaging text.

These are suggested engineering tests, not a built-in Flux Art review UI and not results from API calls or product-image tests performed for this article. For an existing workflow, see the [GitHub Actions scheduled image-generation guide](github-actions-scheduled-image-generation.md) for the boundary between scheduled triggers and asynchronous recovery. The [prompt-template library](../prompts/README.md) can organize local prompt materials.

## FAQ

**Q: Can one Flux Art OpenAPI request generate multiple images?**

A: The current public image endpoint creates one image task per request, with `count` fixed at `1`. The application splits work by SKU and purpose. Browser-based SKU Batch Images is a separate workflow.

**Q: Can I submit again immediately after a timeout?**

A: Retain the original request body and `Idempotency-Key`. A timeout can happen after task creation. Recover with the same key and continue using the task ID or `Location`. Do not reuse the key unless the request content is identical.

**Q: Is a successful task ready to publish?**

A: `succeeded` means the API task completed. Confirm the file is readable, mapped to the right SKU and purpose, and reviewed for product structure, color, labels, text, and channel requirements.

## EN Summary

This bilingual starter shows how to orchestrate e-commerce image jobs with Flux Art OpenAPI: split deliverables into individual image tasks, derive idempotency keys from the exact request and business revision, persist requests before submission, recover asynchronous tasks with the original key, classify errors, and review each file against its SKU sources. It distinguishes custom API orchestration from the browser-based SKU Batch Images tool and makes no performance or benchmark claims.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
