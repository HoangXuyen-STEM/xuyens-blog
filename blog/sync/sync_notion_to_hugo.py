#!/usr/bin/env python3
"""Sync Notion posts into Hugo content with path-safe relative directories."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib import error, request


BLOG_DIR = Path(__file__).resolve().parents[1]
CONTENT_DIR = BLOG_DIR / "content" / "posts"
IMAGES_DIR = BLOG_DIR / "static" / "images"
ENV_PATHS = [BLOG_DIR / ".env", Path(__file__).resolve().parent / ".env"]
NOTION_VERSION = "2022-06-28"


def load_env_files() -> None:
    for env_path in ENV_PATHS:
        if not env_path.exists():
            continue
        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if value:
        return value
    raise SystemExit(
        f"Missing {name}. Copy {BLOG_DIR / '.env.example'} to {BLOG_DIR / '.env'} and fill the value."
    )


def notion_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {require_env('NOTION_API_KEY')}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_request(method: str, url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers=notion_headers(), method=method)
    try:
        with request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Notion API error {exc.code}: {body}") from exc


def sync_statuses() -> list[str]:
    """Return statuses allowed to enter the production Hugo tree.

    Production defaults to Published only. Review content must never become a
    published Hugo post unless an operator explicitly overrides the environment
    for a non-production preview workflow.
    """
    raw_value = os.environ.get("NOTION_SYNC_STATUSES", "Published")
    statuses = [item.strip() for item in raw_value.split(",") if item.strip()]
    if not statuses:
        raise SystemExit("NOTION_SYNC_STATUSES must contain at least one status.")
    return statuses


def database_filter(statuses: list[str]) -> dict[str, Any]:
    if len(statuses) == 1:
        return {"property": "Status", "select": {"equals": statuses[0]}}
    return {
        "or": [
            {"property": "Status", "select": {"equals": status}}
            for status in statuses
        ]
    }


def query_posts() -> list[dict[str, Any]]:
    database_id = require_env("NOTION_DATABASE_ID")
    payload = {
        "filter": database_filter(sync_statuses()),
        "sorts": [{"property": "Published Date", "direction": "descending"}],
        "page_size": 100,
    }
    response = notion_request(
        "POST",
        f"https://api.notion.com/v1/databases/{database_id}/query",
        payload,
    )
    return list(response.get("results", []))


def fetch_blocks(page_id: str) -> list[dict[str, Any]]:
    response = notion_request(
        "GET",
        f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100",
    )
    return list(response.get("results", []))


def rich_text_to_markdown(items: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for item in items:
        text = item.get("plain_text", "")
        annotations = item.get("annotations", {})
        href = item.get("href")
        if href:
            text = f"[{text}]({href})"
        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        parts.append(text)
    return "".join(parts)


def blocks_to_markdown(blocks: list[dict[str, Any]]) -> str:
    output: list[str] = []
    for block in blocks:
        block_type = block.get("type")
        block_data = block.get(block_type or "", {})
        rich_text = rich_text_to_markdown(block_data.get("rich_text", []))

        if block_type == "paragraph":
            output.append(rich_text)
        elif block_type == "heading_1":
            output.append(f"# {rich_text}")
        elif block_type == "heading_2":
            output.append(f"## {rich_text}")
        elif block_type == "heading_3":
            output.append(f"### {rich_text}")
        elif block_type == "bulleted_list_item":
            output.append(f"- {rich_text}")
        elif block_type == "numbered_list_item":
            output.append(f"1. {rich_text}")
        elif block_type == "quote":
            output.append(f"> {rich_text}")
        elif block_type == "divider":
            output.append("---")
        elif block_type == "image":
            image_url = block_data.get("external", {}).get("url") or block_data.get("file", {}).get("url")
            if image_url:
                output.append(f"![]({image_url})")

    return "\n\n".join(line for line in output if line).strip() + "\n"


def prop_title(page: dict[str, Any], name: str) -> str:
    items = page["properties"].get(name, {}).get("title", [])
    return "".join(item.get("plain_text", "") for item in items).strip()


def prop_rich_text(page: dict[str, Any], name: str) -> str:
    items = page["properties"].get(name, {}).get("rich_text", [])
    return "".join(item.get("plain_text", "") for item in items).strip()


def prop_select(page: dict[str, Any], name: str) -> str:
    select = page["properties"].get(name, {}).get("select")
    return "" if not select else str(select.get("name", "")).strip()


def prop_multi_select(page: dict[str, Any], name: str) -> list[str]:
    items = page["properties"].get(name, {}).get("multi_select", [])
    return [str(item.get("name", "")).strip() for item in items if item.get("name")]


def prop_date(page: dict[str, Any], name: str) -> str:
    date_obj = page["properties"].get(name, {}).get("date")
    return "" if not date_obj else str(date_obj.get("start", "")).strip()


def prop_thumbnail(page: dict[str, Any]) -> str:
    files = page["properties"].get("Thumbnail", {}).get("files", [])
    if not files:
        return "/images/default-thumbnail.jpg"
    first = files[0]
    file_url = first.get("file", {}).get("url") or first.get("external", {}).get("url")
    if not file_url:
        return "/images/default-thumbnail.jpg"
    slug = prop_rich_text(page, "Slug") or prop_title(page, "Title").lower().replace(" ", "-")
    image_path = IMAGES_DIR / f"{slug}.jpg"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    with request.urlopen(file_url) as response:
        image_path.write_bytes(response.read())
    return f"/images/{slug}.jpg"


def write_post(page: dict[str, Any], markdown_body: str) -> Path:
    notion_status = prop_select(page, "Status")
    allowed_statuses = sync_statuses()
    if notion_status not in allowed_statuses:
        raise SystemExit(
            f"Refusing to publish Notion status {notion_status!r}; allowed: {', '.join(allowed_statuses)}"
        )

    title = prop_title(page, "Title")
    slug = prop_rich_text(page, "Slug") or title.lower().replace(" ", "-")
    summary = prop_rich_text(page, "Summary")
    category = prop_select(page, "Category") or "mindset"
    tags = prop_multi_select(page, "Tags")
    lenny_episode = prop_rich_text(page, "Lenny Episode")
    cta_type = prop_select(page, "CTA Type") or "course"
    published_date = prop_date(page, "Published Date")
    thumbnail = prop_thumbnail(page)

    frontmatter = [
        "---",
        f'title: "{title.replace("\"", "\\\"")}"',
        f'slug: "{slug}"',
        f'summary: "{summary.replace("\"", "\\\"")}"',
        f'categories: ["{category}"]',
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
        f'thumbnail: "{thumbnail}"',
        f'lenny_episode: "{lenny_episode.replace("\"", "\\\"")}"',
        f'cta_type: "{cta_type}"',
        f'date: "{published_date}"',
        'status: "published"',
        "---",
        "",
    ]

    post_path = CONTENT_DIR / f"{slug}.md"
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    post_path.write_text("\n".join(frontmatter) + markdown_body, encoding="utf-8")
    return post_path


def main() -> int:
    load_env_files()
    pages = query_posts()
    print(f"Found {len(pages)} page(s) in Notion matching {', '.join(sync_statuses())}.")
    for page in pages:
        markdown_body = blocks_to_markdown(fetch_blocks(page["id"]))
        post_path = write_post(page, markdown_body)
        print(f"✅ Synced {post_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())