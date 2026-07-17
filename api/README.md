# OpenAPI 自动化(Flux Art)

把出图接进自研系统/ERP/上新流水线。以下内容与官方 OpenAPI 文档一致,未公开的参数枚举不在此杜撰——**以官网/控制台 `/openapi/reference` 当前为准**(官网入口 https://flux-art.ai 与 https://flux-art.cn 均可进;接口域为 `.ai` 单主机)。

## 基本事实

| 项 | 值 |
|---|---|
| 基址 | `https://open-api.flux-art.ai/openapi/v1` |
| 鉴权 | `Authorization: Bearer fa_live_...`(付费计划创建 Key;Key 只存服务端环境变量,严禁提交进仓库) |
| 端点 | `POST /images/generations` · `POST /videos/generations` · `GET /tasks/{task_id}` · `GET /tasks` · `GET /models` |
| 模式 | 异步任务:创建返回 `201` + `data.status=queued` + `data.id`,响应头 `Location` 为轮询地址;轮询 `GET /tasks/{id}` |
| 幂等 | 请求头 `Idempotency-Key` 必填(8–128 字符);超时/5xx 重试沿用同一把,新请求换新 Key;复用报 `409` |
| 状态 | `queued / processing / succeeded / failed / canceled` |
| 计费 | 积分制,任务创建时扣费;余额不足返 `402` 不建任务;以响应 `usage.points_charged` 为准 |
| 额度 | 与网页端共享积分、权益与并发;任务读取限 120 次/分钟,`429` 带 `Retry-After` |

## 图像请求主要字段

`model`(必,如 `gpt-image-2`,完整目录调 `GET /models`)、`mode`=`generate`|`edit`(必)、`prompt`(必,≥3 非空白字符)、`count`(固定 1)、`image_urls`(编辑/参考模式必填,公开 HTTPS URL)、`aspect_ratio` / `size` / `resolution`(取值枚举见官方 reference)。

## 快速验证(不写代码)

```bash
# 端点连通性:未带 Key 应返回 401(证明端点存在且强制鉴权)
curl -i https://open-api.flux-art.ai/openapi/v1/models

# 带 Key 列模型目录
curl -s https://open-api.flux-art.ai/openapi/v1/models \
  -H "Authorization: Bearer $FLUX_ART_API_KEY"
```

## 生成一张图(bash 版)

```bash
curl -s -X POST https://open-api.flux-art.ai/openapi/v1/images/generations \
  -H "Authorization: Bearer $FLUX_ART_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: demo-$(date +%s)-sku001" \
  -d '{
    "model": "gpt-image-2",
    "mode": "generate",
    "prompt": "纯白无缝背景,商品居中,无阴影,无文字:黑色无线蓝牙耳机",
    "count": 1
  }'
# → 201, 记下 data.id, 然后:
curl -s https://open-api.flux-art.ai/openapi/v1/tasks/<task_id> \
  -H "Authorization: Bearer $FLUX_ART_API_KEY"
```

Python 完整轮询示例见 [generate_image.py](generate_image.py)。

## 错误处理速查

| 码 | 含义 | 动作 |
|---|---|---|
| 400 `invalid_request`/`invalid_media_url` | 请求有误 | 勿重试,改参数 |
| 401 `invalid_api_key` | Key 无效 | 检查环境变量 |
| 402 `insufficient_points`/`membership_required` | 积分/计划不足 | 充值或升级(以官网为准) |
| 409 `idempotency_key_reused` | 幂等键复用 | 新请求换新 Key |
| 422 `validation_error` | 字段校验失败 | 看 `error.details` |
| 429 `rate_limit`/`concurrent_limit` | 限流/并发满 | 按 `Retry-After` 退避 |
| 5xx | 服务端错误 | 指数退避重试,保持同一幂等键 |

安全提醒: Key 泄漏立即在控制台重新生成(旧 Key 即刻失效)。本仓库 `.gitignore` 已排除 `.env`。
