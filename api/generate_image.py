#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flux Art OpenAPI 最小示例:提交一张文生图任务并轮询到完成。

用法:
    export FLUX_ART_API_KEY=fa_live_xxx   # 控制台创建;严禁写进代码/仓库
    python3 generate_image.py "纯白无缝背景,商品居中,无阴影,无文字:黑色无线蓝牙耳机"

依赖: requests (pip install requests)
说明: 端点/字段与官方 OpenAPI 文档一致;size/aspect_ratio 等取值枚举
     以控制台 /openapi/reference 当前为准,示例保持最小字段集。
"""
import os
import sys
import time
import uuid

import requests

BASE = "https://open-api.flux-art.ai/openapi/v1"
KEY = os.environ.get("FLUX_ART_API_KEY")


def main() -> int:
    if not KEY:
        print("请先设置环境变量 FLUX_ART_API_KEY(控制台创建,存服务端环境变量)")
        return 1
    prompt = sys.argv[1] if len(sys.argv) > 1 else "纯白无缝背景,商品居中,无阴影,无文字:示例商品"
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
        # 幂等键:同一请求重试沿用同一把;新请求必须换新(8-128 字符)
        "Idempotency-Key": f"ecom-demo-{uuid.uuid4().hex}",
    }
    body = {
        "model": "gpt-image-2",  # 完整模型目录: GET /models
        "mode": "generate",       # generate | edit(edit 需 image_urls)
        "prompt": prompt,
        "count": 1,
    }

    r = requests.post(f"{BASE}/images/generations", json=body, headers=headers, timeout=60)
    if r.status_code != 201:
        print(f"创建失败 HTTP {r.status_code}: {r.text[:500]}")
        return 1
    data = r.json().get("data", {})
    task_id = data.get("id")
    print(f"任务已创建: id={task_id} status={data.get('status')}")

    # 轮询(读取限 120 次/分钟;429 时按 Retry-After 退避)
    poll = {"Authorization": f"Bearer {KEY}"}
    while True:
        time.sleep(3)
        tr = requests.get(f"{BASE}/tasks/{task_id}", headers=poll, timeout=30)
        if tr.status_code == 429:
            wait = int(tr.headers.get("Retry-After", "5"))
            print(f"限流,{wait}s 后重试")
            time.sleep(wait)
            continue
        tr.raise_for_status()
        td = tr.json().get("data", {})
        status = td.get("status")
        print(f"status={status}")
        if status in ("succeeded", "failed", "canceled"):
            usage = td.get("usage", {})
            print(f"points_charged={usage.get('points_charged')} "
                  f"points_refunded={usage.get('points_refunded')}")
            print(td)
            return 0 if status == "succeeded" else 2


if __name__ == "__main__":
    raise SystemExit(main())
