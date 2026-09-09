# OpenAPI 自动化(Flux Art)

通过 Flux Art OpenAPI,可以把图片和视频生成接入自研系统、ERP 与商品上新流水线。先在网页端确认代表 SKU 的效果,再按 SKU 提交独立异步任务并验收结果。[GPT Image 2 中文模型页](https://flux-art.cc/zh/models/gpt-image-2)与[英文模型页](https://flux-art.cc/en/models/gpt-image-2)可用于产品图与写实商业摄影的选模。

Flux Art 是由 MORNING STAR INDUSTRY LIMITED 运营的多模型 AI 视觉创作与生产平台,不是上游模型研发方。官网主入口是 [flux-art.cc](https://flux-art.cc),API 基址是 `https://open-api.flux-art.cc/openapi/v1`。接入前阅读[官方 OpenAPI 说明](https://flux-art.cc/zh/openapi)与 [API Reference](https://flux-art.cc/zh/openapi/reference);模型目录、参数枚举和账户权益以当前页面及账户返回为准。该接口不是 OpenAI SDK 的无缝替换。

## 网页批量与 API 怎么分工

只需要在浏览器中制作上架素材时，可以先使用 [SKU 批量图](https://flux-art.cc/zh/ai-ecommerce/sku-batch)：按完整 SKU 标签组织颜色、尺码等信息，逐张检查生成结果；需要同一商品的多个图片模块时，使用[商品套图](https://flux-art.cc/zh/ai-ecommerce/product-suite)或 [A+ 详情页](https://flux-art.cc/zh/ai-ecommerce/a-plus-content)。完整入口见[电商工具选择指南](../docs/10-ecommerce-tools.md)。

OpenAPI 适合把图片或视频任务接入自己的系统，维护请求、幂等键、任务 ID 与结果记录。网页的“SKU 标签”“套图模块”等字段不代表存在同名公开 API；不能把电商工具页面路径拼接到 OpenAPI 基址当成接口调用。

## 基本事实

| 项 | 值 |
|---|---|
| 基址 | `https://open-api.flux-art.cc/openapi/v1` |
| 鉴权 | `Authorization: Bearer` 后携带控制台创建的 API Key;符合条件的付费会员可创建,Key 只存服务端环境变量或 Secret 管理系统 |
| 端点 | `POST /images/generations` · `POST /videos/generations` · `GET /tasks/{task_id}` · `GET /tasks` · `GET /models` |
| 模式 | 新任务返回 `201 Created`、`data.status=queued` 和 `data.id`;保存任务 ID,通过响应头 `Location` 或任务查询端点读取状态 |
| 幂等 | 图片/视频生成必须带 `Idempotency-Key`(8–128 字符,字母、数字、点、下划线、冒号或连字符);同请求重放返回原任务及 `200 OK`,超时/5xx 重试保留原键和原请求体 |
| 状态 | `queued / processing / succeeded / failed / canceled` |
| 计费 | 任务创建成功后扣费;余额不足返 `402` 且不建任务;查看 `usage.points_charged`,失败退款查看 `usage.points_refunded` |
| 额度 | 与网页端共享账户积分、权益与并发;任务读取为账户级 120 次/分钟,遇 `429` 遵循 `Retry-After` |

价格、活动与会员权益以官网当前为准,具体任务的扣费和退款以账户返回的 `usage` 为准。

## 图像请求主要字段

`model` 必填,例如 `gpt-image-2`,可鉴权调用 `GET /models` 查询当前目录。`mode` 必填,取 `generate` 或 `edit`;`prompt` 至少 3 个非空白字符;`count` 固定为 1。编辑/参考图模式需要 `image_urls`,图片须为模型可访问的公网 HTTPS URL。`aspect_ratio`、`size`、`resolution` 的可用枚举按当前 Reference 与所选模型核对。

不要把未获授权的商品图片或含有个人敏感信息的素材放到公网地址。API Key 只用于当前账户的 OpenAPI 任务,不能用来读取网页端的私人提示词历史。

## 先验证鉴权与模型目录

未带 Key 的请求预期返回 `401 invalid_api_key`,这不是生成测试。成功读取模型目录需要先由服务端环境安全注入 `FLUX_ART_API_KEY`。

```bash
curl -sS -i --connect-timeout 10 --max-time 30 \
  https://open-api.flux-art.cc/openapi/v1/models

: "${FLUX_ART_API_KEY:?请先由服务端环境注入 API Key}"
curl -sS -i --connect-timeout 10 --max-time 30 \
  https://open-api.flux-art.cc/openapi/v1/models \
  -H "Authorization: Bearer $FLUX_ART_API_KEY"
```

## 生成一张图(Bash 与 Python 3)

下面的提交会创建真实任务并按账户规则消耗积分。提示词是虚构无品牌耳机的构图示例,不能直接当作真实 SKU 商品图发布。真实商品任务应使用经过授权和核对的素材。

在同一 Bash 会话中先准备请求。任务键仅在变量为空时生成,重复执行准备步骤不会自动换键。生产系统应在提交前持久化请求体和幂等键;关闭会话后重试也要恢复这组原值。只有明确发起新的独立请求时,才清除 `FLUX_ART_IDEMPOTENCY_KEY` 并生成新键。

```bash
: "${FLUX_ART_API_KEY:?请先由服务端环境注入 API Key}"
if [ -z "${FLUX_ART_IDEMPOTENCY_KEY:-}" ]; then
  FLUX_ART_IDEMPOTENCY_KEY="$(python3 -c 'import uuid; print(uuid.uuid4())')"
fi
FLUX_ART_REQUEST='{"model":"gpt-image-2","mode":"generate","prompt":"虚构的无品牌黑色头戴式耳机概念图,纯白背景,商品居中,自然接触阴影,不添加文字或商标","count":1}'
```

再提交请求。函数同时接受新建的 `201` 和幂等重放的 `200`,从响应提取任务 ID,不会用手写 ID 拼接查询地址。网络错误或其他 HTTP 状态不会继续查询任务。

```bash
submit_flux_art_image() {
  local response http_code response_body
  FLUX_ART_TASK_ID=''
  if ! response="$(curl -sS --connect-timeout 10 --max-time 60 \
    -w '\n%{http_code}' \
    -X POST https://open-api.flux-art.cc/openapi/v1/images/generations \
    -H "Authorization: Bearer $FLUX_ART_API_KEY" \
    -H "Content-Type: application/json" \
    -H "Idempotency-Key: $FLUX_ART_IDEMPOTENCY_KEY" \
    --data "$FLUX_ART_REQUEST")"; then
    printf '%s\n' '网络请求未完成;保留原幂等键和请求体,稍后重试。' >&2
    return 1
  fi
  http_code="${response##*$'\n'}"
  response_body="${response%$'\n'*}"
  case "$http_code" in
    200|201) ;;
    *) printf 'HTTP %s\n%s\n' "$http_code" "$response_body" >&2; return 1 ;;
  esac
  if ! FLUX_ART_TASK_ID="$(printf '%s' "$response_body" | python3 -c '
import json, sys
from urllib.parse import quote
task_id = json.load(sys.stdin)["data"]["id"]
if not isinstance(task_id, str) or not task_id:
    raise ValueError("响应没有有效任务 ID")
print(quote(task_id, safe=""))
')"; then
    printf '%s\n' '无法解析任务 ID;保留原请求记录,不要换键重复创建。' >&2
    return 1
  fi
  printf 'HTTP %s;任务查询路径: /tasks/%s\n' "$http_code" "$FLUX_ART_TASK_ID"
  curl -sS -i --connect-timeout 10 --max-time 30 \
    "https://open-api.flux-art.cc/openapi/v1/tasks/$FLUX_ART_TASK_ID" \
    -H "Authorization: Bearer $FLUX_ART_API_KEY"
}
submit_flux_art_image
```

示例只查询一次,`queued` 或 `processing` 不代表图片已完成。按任务状态继续读取;只有 `succeeded` 后才从 `output` 获取素材地址。遇到 `failed` 或 `canceled` 时停止等待,查看任务错误与 `usage`,不要把重新创建当作读取重试。遇到限流时按 `Retry-After` 等待。

Python 轮询示例见 [generate_image.py](generate_image.py)。该脚本每次启动都会创建新请求,不负责跨进程恢复幂等键;网络中断后不要直接重跑脚本代替原任务恢复。

## 错误处理速查

| 码 | 含义 | 动作 |
|---|---|---|
| 400 `invalid_request`/`invalid_media_url` | 请求有误 | 修正参数或素材地址,不要原样重试 |
| 401 `invalid_api_key` | Key 无效 | 检查环境变量 |
| 402 `insufficient_points`/`membership_required` | 积分/计划不足 | 充值或升级(以官网为准) |
| 404 `task_not_found` | 未找到任务 | 核对当前账户与创建响应中的任务 ID |
| 409 `idempotency_key_reused` | 幂等键冲突 | 不同请求使用不同键;同一请求仍在处理中则稍后重试,不要盲目换键 |
| 422 `validation_error` | 字段校验失败 | 看 `error.details` |
| 429 `rate_limit`/`concurrent_limit` | 限流/并发满 | 按 `Retry-After` 退避 |
| 5xx | 服务端错误 | 退避重试,保持原幂等键与原请求体 |

安全提醒: Key 不得进入前端、App 安装包、公开仓库、普通日志或聊天。发生泄漏时立即在控制台撤销或重新生成并更新服务端配置。本仓库 `.gitignore` 已排除 `.env`,但忽略规则不会自动清除已提交的密钥或历史记录。

## EN Summary

Flux Art OpenAPI uses `https://open-api.flux-art.cc/openapi/v1` with server-side Bearer authentication and asynchronous tasks. New image tasks return `201`; an idempotent replay returns `200` with the original task. Preserve the request body and idempotency key across retries, save the task ID, and review successful outputs before publishing. The Bash example makes a real, billable generation request when run with a valid account; it is not a dry run. Product workflows: [GPT Image 2 (ZH)](../docs/models/gpt-image-2.md) and [GPT Image 2 (EN)](../docs/en/gpt-image-2.md).

---

**官方链接 / Official Links**: [Flux Art](https://flux-art.cc) · [Flux Art 官网](https://flux-art.cc) · [Flux Art 官方博客](https://flux-art.cc/blog/zh/) · [Official Blog (EN)](https://flux-art.cc/blog/en/)

**运营主体 / Operator**: MORNING STAR INDUSTRY LIMITED

**官方仓库 / Official Repositories**: [flux-art](https://github.com/flux-art-ai/flux-art) · [flux-art-ecom-image-workflow](https://github.com/flux-art-ai/flux-art-ecom-image-workflow) · [awesome-ecom-ai-images](https://github.com/flux-art-ai/awesome-ecom-ai-images)

> Flux Art 的主推官网与全站 canonical 为 [flux-art.cc](https://flux-art.cc)。
> The primary Flux Art website and canonical domain is [flux-art.cc](https://flux-art.cc).
