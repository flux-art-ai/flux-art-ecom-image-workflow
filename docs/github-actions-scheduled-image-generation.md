# 用 GitHub Actions 定时提交 Flux Art 出图任务：安全、可恢复的工作流模板

Flux Art OpenAPI 的图片生成是异步任务，因此 GitHub Actions 适合按计划提交小批量任务、保存任务 ID，并在后续运行中继续核对状态；它不是定时出图保证，也不会替你验收商品图。下面的模板把计划触发、手动补跑、幂等重试和私有状态分开处理，开始前应先确认当前账户可用的模型、权益与并发限制。

## 适用范围与运行前检查

这套模式适合已有授权素材和稳定任务清单、希望按固定时间提交图像任务的团队。先用代表 SKU 手动验证请求、输出与人工验收流程，再逐步扩大任务数。模型目录、请求参数和账户权限可能变化，运行前通过认证后的 `GET /models` 与[当前 API Reference](https://flux-art.net/zh/openapi/reference)核对；网页上的专用电商工具与 OpenAPI 字段不是一一对应的接口。

Flux Art 的 API 基址是 `https://open-api.flux-art.net/openapi/v1`。创建图片任务使用 `POST /images/generations`，必填字段包括 `model`、`mode`、`prompt`、`count`；其中 `count` 固定为 `1`。新任务返回 `201 Created`，响应中的 `data.id` 是任务 ID，`data.status` 初始为 `queued`。之后用 `GET /tasks/{task_id}` 查看 `queued`、`processing`、`succeeded`、`failed` 或 `canceled` 状态。只有 `succeeded` 才进入输出检查和交付。

开始前逐项确认：

1. 用一项低风险任务走通认证、创建、查询和人工验收；API 任务会按账户规则消耗资源，不是 dry run。
2. 将 API Key 保存为仓库 Secret `FLUX_ART_API_KEY`，只在服务端工作流中读取；不要写进文件、命令行参数、日志或输出工件。
3. 调度仓库设为私有。若选择把待处理任务状态提交回仓库，任务提示词、SKU 标识、任务 ID 和输出地址也必须按敏感数据处理；只保存恢复任务所需的最少字段。
4. 从当前账户的 `GET /models` 选择实际可用的 `model` 值，并核对模型要求的 `size`、`resolution` 或 `aspect_ratio` 等可选字段。不要从网页标题推造 API ID。
5. 先设小批次。提交速率、账户并发和计划权益以当前账户与 API 返回为准；遇到 `429` 按 `Retry-After` 等待，不要靠增加并发来绕过限制。

API Key 的安全边界和 OpenAPI 的异步调用细节见[API 接入说明](../api/README.md)。只希望在浏览器里制作电商图片时，可先从[电商工具选择指南](10-ecommerce-tools.md)选择网页工具，不必为了“自动化”而改走 API。

## GitHub Actions 工作流

把下面文件保存为私有调度仓库的 `.github/workflows/flux-art-image-jobs.yml`。`timezone` 使用 IANA 时区；这里安排在北京时间每天 10:17，避开整点常见的调度拥挤时段。`workflow_dispatch` 保留手动入口。GitHub Actions 的计划运行可能延迟或在高负载时被跳过，所以不要将它当成准点或恰好一次执行的服务；脚本必须能安全重跑。

```yaml
name: Flux Art scheduled image jobs

on:
  schedule:
    - cron: "17 10 * * *"
      timezone: "Asia/Shanghai"
  workflow_dispatch:

concurrency:
  group: flux-art-image-jobs
  cancel-in-progress: false

jobs:
  submit-and-reconcile:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Submit new jobs and reconcile pending tasks
        env:
          FLUX_ART_API_KEY: ${{ secrets.FLUX_ART_API_KEY }}
        run: python scripts/run_flux_art_jobs.py
      - name: Save private recovery state
        if: always()
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add state/tasks.json
          if ! git diff --cached --quiet; then
            git commit -m "chore: save private image task state"
            git push
          fi
```

GitHub 的 `schedule` 只在默认分支上的工作流文件生效，计划任务以默认分支最新提交运行。公开仓库中的计划工作流在长期无活动后可能被自动停用；对含有商品资料、提示词和状态的任务调度仓库，使用私有仓库并定期检查 Actions 状态更合适。GitHub 的触发规则见[官方工作流事件文档](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)。

## 任务清单与状态恢复

将新任务清单放在私有仓库的 `tasks/daily.json`。每项用团队自定义且稳定的 `key` 标识，不要把消费者姓名、订单号或其他不必要的个人信息放进 key。

```json
[
  {
    "key": "sku-042-main-image",
    "model": "gpt-image-2",
    "mode": "generate",
    "prompt": "经授权的商品资料与构图要求；不要包含不必要的个人信息"
  }
]
```

上面的模型值仅用于说明字段格式；真实运行前必须在当前账户的 `GET /models` 中确认它仍可用。提示词使用虚构商品，不代表真实商品资料。脚本应为每项任务构造稳定的 `Idempotency-Key`，并在发送请求前持久化该键与完全相同的请求体。API 要求幂等键为 8–128 个允许字符；同一请求超时或遇到服务端 `5xx` 时，使用同一个键和同一请求体重试。不要在响应不确定时生成新键，否则可能创建第二个计费任务；确认输入错误并修正请求后，再用新任务 key 作为独立请求提交。

建议将状态拆成两类：

| 状态 | 最少保存内容 | 下次运行的动作 |
|---|---|---|
| 尚未提交 | 任务 key、请求体、幂等键 | 用原请求体和原键创建任务；先保存恢复信息，再发请求 |
| 已创建、未完成 | `data.id`、幂等键、请求体校验摘要、最近状态 | 查询原任务 ID；不要创建替代任务 |
| 已完成或失败 | 任务 ID、最终状态、必要的去敏验收记录 | 成功时人工检查 `output`；失败时检查错误和账户 `usage`，再决定是否发起新任务 |

本模板通过 `GITHUB_TOKEN` 将 `state/tasks.json` 提交回私有仓库，因此工作流声明了 `contents: write`。若改用受控的私有外部状态存储，应将权限降为 `contents: read`。不要为了写状态而给其他 job 更宽权限。状态中不应包含 API Key、完整日志、无关客户资料或不必要的输出 URL。

## 提交、轮询与重试规则

将下面脚本保存为 `scripts/run_flux_art_jobs.py`。它按北京时间日期和任务 key 构造稳定幂等键，发送前先写入状态文件；后续运行查询未完成任务，不在一次 Action 中无限轮询。脚本假设任务清单、状态文件都位于私有仓库。

```python
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

BASE = "https://open-api.flux-art.net/openapi/v1"
API_KEY = os.environ.get("FLUX_ART_API_KEY")
MANIFEST = Path("tasks/daily.json")
STATE = Path("state/tasks.json")
if not API_KEY:
    raise SystemExit("FLUX_ART_API_KEY is not set")


def call(method, path, body=None, idem=None):
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
    payload = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        payload = json.dumps(body, ensure_ascii=False, separators=(",", ":")).encode()
    if idem:
        headers["Idempotency-Key"] = idem
    req = Request(BASE + path, data=payload, headers=headers, method=method)
    try:
        with urlopen(req, timeout=45) as response:
            return response.status, json.loads(response.read())
    except HTTPError as exc:
        if exc.code == 429:
            print("Rate limited; resume after Retry-After on a later run.", file=sys.stderr)
        elif exc.code >= 500:
            print("Server error; preserve the saved request and idempotency key.", file=sys.stderr)
        else:
            print(f"Request needs attention: HTTP {exc.code}.", file=sys.stderr)
        raise RuntimeError(f"API returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise RuntimeError("Network outcome is uncertain; retry with saved state.") from exc


def save(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=STATE.parent, delete=False) as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")
        temp = f.name
    os.replace(temp, STATE)


tasks = json.loads(MANIFEST.read_text(encoding="utf-8"))
state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
day = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y%m%d")
failed = False

for task in tasks:
    task_key = task.get("key", "")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,80}", task_key):
        print("Each task needs a stable, non-personal key.", file=sys.stderr)
        failed = True
        continue
    terminal = {"succeeded", "failed", "canceled"}
    record = next((item for item in state.values()
                   if item.get("task_key") == task_key and item.get("status") not in terminal), None)
    idem = record["idempotency_key"] if record else (
        "fa-" + day + "-" + hashlib.sha256(task_key.encode()).hexdigest()[:24]
    )
    record = record or state.get(idem)
    if record is None:
        body = {name: task[name] for name in ("model", "mode", "prompt")}
        body["count"] = 1
        record = {"task_key": task_key, "idempotency_key": idem, "request": body}
        state[idem] = record
        save(state)  # Persist before POST; a retry can reuse the exact body and key.
        try:
            status, result = call("POST", "/images/generations", body, idem)
            record["task_id"] = result["data"]["id"]
            record["status"] = result["data"].get("status", "queued")
            record["created_http_status"] = status
            save(state)
        except Exception as exc:
            print(f"{task_key}: creation is unconfirmed; saved request will be retried safely ({exc})", file=sys.stderr)
            failed = True
            continue

    if record.get("task_id") and record.get("status") not in {"succeeded", "failed", "canceled"}:
        try:
            _, result = call("GET", "/tasks/" + record["task_id"])
            data = result["data"]
            record["status"] = data.get("status", "unknown")
            if record["status"] == "succeeded":
                record["output"] = data.get("output")
            elif record["status"] in {"failed", "canceled"}:
                record["error"] = data.get("error")
                record["usage"] = data.get("usage")
            save(state)
        except Exception as exc:
            print(f"{task_key}: status is unconfirmed; keep the task ID for the next run ({exc})", file=sys.stderr)
            failed = True
            continue
    print(f"{task_key}: {record.get('status', 'submission pending')}")

if failed:
    raise SystemExit(1)
```

这段脚本不会打印 API Key 或响应体。`state/tasks.json` 仍会包含请求提示词、任务 ID 和成功任务的 `output`，必须保存在私有仓库并按团队策略清理。请求超时或遇到 `5xx` 时，下次运行使用已保存的请求体和幂等键；遇到 `429` 则按响应头 `Retry-After` 等待，不在同一轮立即循环。只有人工检查输出后才能交付。

状态提交可放在工作流脚本步骤之后：

上面的工作流已包含状态提交步骤。不要把这个写状态步骤用于公开仓库。GitHub 关于 Secret、最小权限和日志风险的说明见[安全使用文档](https://docs.github.com/en/actions/reference/security/secure-use)。

## 上线前验收

- 在默认分支检查 workflow 文件已经存在，并在 Actions 页面确认计划触发器启用。
- 先用 `workflow_dispatch` 和一项测试任务验证 Secret、模型目录、请求字段、异步状态恢复及费用记录。
- 手动中断一次测试运行，确认下一次能够以同一幂等键恢复原任务，而不是重复创建。
- 检查 `queued`、`processing`、`succeeded`、`failed` 与 `canceled` 的分支；成功图片需由人验收后才能交付。
- 查看 Actions 日志和状态文件，确认其中没有 API Key、无关个人资料或不应公开的输出地址。
- 仅在小批次稳定后逐步增加任务；任何时候以实际 API 响应和账户规则为准。

## FAQ

**Q: 定时触发能保证每天准时运行吗？**

A: 不能。GitHub 说明计划事件可能延迟或被跳过；保留手动触发，并让状态可恢复。

**Q: 请求超时后可以换一个幂等键再试吗？**

A: 对同一逻辑请求不要换。使用相同请求体和原幂等键重试，避免不确定结果造成重复任务。

**Q: Action 显示成功就能直接发布图片吗？**

A: 不能。任务成功只表示 API 返回了输出；商品细节、素材授权、文字与渠道要求仍需逐张人工验收。

## EN Summary

Use GitHub Actions to submit a small, scheduled batch and reconcile asynchronous Flux Art tasks—not to promise exact run times or automatic approval. Keep the API key in a GitHub Secret, preserve the same request body and idempotency key when retrying, store only the minimum recovery state in a private location, and review every successful output before delivery.

## English Version

### Schedule Flux Art Image Jobs with GitHub Actions: A Recoverable Workflow

Flux Art image generation through the OpenAPI is asynchronous, so GitHub Actions can submit a small scheduled batch, save task IDs, and reconcile them in later runs. It cannot guarantee an exact execution time or review product images for you. Confirm the models, fields, account entitlements, and concurrency rules currently available to your account before expanding a batch.

## Scope and prerequisites

This pattern is for teams with authorized source material and a stable task list. First validate one low-risk SKU end to end, including authentication, task creation, status lookup, and human review. Check the authenticated `GET /models` response and the [current API Reference](https://flux-art.net/en/openapi/reference) before each integration change. Web-based e-commerce tools and OpenAPI request fields are separate interfaces.

The API base is `https://open-api.flux-art.net/openapi/v1`. Create an image task with `POST /images/generations`, using `model`, `mode`, `prompt`, and `count`; `count` is fixed at `1`. A new task returns `201 Created`, with its task ID in `data.id` and an initial `queued` status. Query `GET /tasks/{task_id}` for `queued`, `processing`, `succeeded`, `failed`, or `canceled`. Only `succeeded` proceeds to output review and delivery.

Before running:

1. Test one low-risk request. A real API task follows your account's usage rules; it is not a dry run.
2. Store the API key as the repository Secret `FLUX_ART_API_KEY`. Read it only in the server-side workflow; never put it in files, command-line arguments, logs, or artifacts.
3. Use a private scheduling repository. Treat prompts, SKU identifiers, task IDs, and output URLs as sensitive if they are persisted. Save only the minimum state needed for recovery.
4. Select a `model` value returned by the current authenticated `GET /models` endpoint. Verify optional fields such as `size`, `resolution`, or `aspect_ratio` against the selected model. Do not infer an API ID from a web-page title.
5. Start with a small batch. Follow the current account and API limits; on `429`, wait according to `Retry-After` instead of increasing concurrency to bypass a limit.

See the [OpenAPI integration guide](../api/README.md) for authentication and asynchronous task handling. If you only need browser-based product imagery, choose a tool from the [e-commerce workflow guide](10-ecommerce-tools.md) rather than adding an API integration unnecessarily.

## GitHub Actions workflow

Save this as `.github/workflows/flux-art-image-jobs.yml` in a private scheduling repository. The IANA time zone schedules this example for 10:17 a.m. China Standard Time, away from the top of the hour. `workflow_dispatch` provides a manual run. GitHub may delay or drop scheduled runs under high load, so do not treat the schedule as an exact-time or exactly-once service; the script must be safe to rerun.

```yaml
name: Flux Art scheduled image jobs

on:
  schedule:
    - cron: "17 10 * * *"
      timezone: "Asia/Shanghai"
  workflow_dispatch:

concurrency:
  group: flux-art-image-jobs
  cancel-in-progress: false

jobs:
  submit-and-reconcile:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Submit new jobs and reconcile pending tasks
        env:
          FLUX_ART_API_KEY: ${{ secrets.FLUX_ART_API_KEY }}
        run: python scripts/run_flux_art_jobs.py
      - name: Save private recovery state
        if: always()
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add state/tasks.json
          if ! git diff --cached --quiet; then
            git commit -m "chore: save private image task state"
            git push
          fi
```

GitHub runs a scheduled workflow from the latest commit on the default branch, and the workflow file must be on that branch. Scheduled workflows in public repositories may be disabled after a long period without activity. For scheduling behavior, see [GitHub's workflow events documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

## Task manifest and recovery state

Store new work in `tasks/daily.json` in the private repository. Give every item a stable, team-defined `key`; avoid putting customer names, order IDs, or other unnecessary personal data in that key.

```json
[
  {
    "key": "sku-042-main-image",
    "model": "a model ID selected from the current GET /models response",
    "mode": "generate",
    "prompt": "Authorized product facts and composition requirements; omit unnecessary personal data"
  }
]
```

The model value only illustrates the field format; confirm it remains available in your account's current `GET /models` response before running. The prompt describes a fictional product, not real product data. For each logical task, create a stable `Idempotency-Key` and persist it with the exact request body before sending. The API requires 8–128 allowed characters. If the same request times out or receives a server-side `5xx`, retry with the same key and body. Do not create a new key while the outcome is uncertain, or you may create another billable task.

Keep state in separate stages:

| Stage | Minimum state | Next run |
|---|---|---|
| Not submitted | Task key, request body, idempotency key | Create the task with the saved body and key; persist recovery data before sending |
| Created, unfinished | `data.id`, idempotency key, request-body digest, latest status | Query the existing task ID; do not create a replacement |
| Finished or failed | Task ID, final status, minimal redacted review record | Review `output` on success; inspect the error and account `usage` on failure before deciding whether to submit a new task |

The job needs `contents: write` only because it commits state to this private repository. If you use controlled private storage outside Git history, remove that job permission and keep the default read access. State must not contain the API key, full logs, unrelated customer data, or unnecessary output URLs.

## Submission, polling, and retry rules

The language-neutral Python example in the Chinese section is the implementation for this workflow too: persist the exact body and daily idempotency key before POST, save `data.id`, and query unfinished tasks once per run. It resumes an unfinished task from a previous day before creating a new daily task. `201` means a new task; an idempotent replay may return `200`. Correct `400`/`422` inputs before making a new task; check the Secret for `401`, account entitlement for `402`, and the same-account task ID for `404`. For `409`, check key/body consistency; for `429`, follow `Retry-After`; for `5xx`, retry with the original body and key. Human review is still required before delivery. If a confirmed input error requires changing the request, update the task key as well so the corrected request gets a distinct idempotency key.

Set a maximum total runtime in Actions so a run cannot occupy a runner indefinitely. Never print secrets, full request bodies, or raw customer data to logs. See GitHub's [secure-use documentation](https://docs.github.com/en/actions/reference/security/secure-use) for secrets, least privilege, and logging risks.

## Pre-release checklist

- Confirm the workflow file exists on the default branch and the scheduled trigger is enabled in the Actions interface.
- Use `workflow_dispatch` and one test task to validate the Secret, model directory, request fields, asynchronous recovery, and usage records.
- Interrupt a test run and verify that the next run resumes with the same idempotency key instead of creating a duplicate.
- Handle `queued`, `processing`, `succeeded`, `failed`, and `canceled`; require human review before delivering a successful image.
- Check logs and state for API keys, unnecessary personal data, or output URLs that should not be exposed.
- Increase batch size only after a small batch is stable; always follow current API responses and account rules.

## FAQ

**Does a scheduled trigger guarantee an exact daily run time?**

No. GitHub notes that scheduled runs may be delayed or dropped. Keep a manual trigger and make task state recoverable.

**Can I use a new idempotency key after a timeout?**

Not for the same logical request. Retry with the original body and key so an uncertain response does not create a duplicate task.

**Can I publish an image as soon as the Action succeeds?**

No. Success means the API returned output; product details, source rights, text, and channel requirements still need human review.

## EN Summary

GitHub Actions can schedule small Flux Art image batches and reconcile asynchronous tasks, but it cannot guarantee exact run times or approve images. Store the API key in a GitHub Secret, preserve the same request body and idempotency key when retrying, keep minimum recovery state in a private location, and have a person review every successful output before delivery.

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cn) · [Flux Art 官网](https://flux-art.cn) · [Flux Art 官方博客](https://flux-art.net/blog/zh/) · [Official Blog (EN)](https://flux-art.net/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的固定官方访问入口是 [flux-art.cn](https://flux-art.cn)。公开引用、收藏与分享统一使用这一地址。
> Flux Art’s permanent official entry is [flux-art.cn](https://flux-art.cn). Use this address for public references, bookmarks and sharing.
