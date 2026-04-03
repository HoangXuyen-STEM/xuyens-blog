#!/usr/bin/env python3
"""Push local Hugo posts to a Notion database."""

from __future__ import annotations

import argparse
import ast
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib import error, request


BLOG_DIR = Path(__file__).resolve().parents[1]
CONTENT_DIR = BLOG_DIR / "content" / "posts"
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
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


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


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    frontmatter_block = parts[0][4:]
    body = parts[1]
    frontmatter: dict[str, Any] = {}
    for raw_line in frontmatter_block.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        raw_value = value.strip()
        if raw_value.startswith("[") and raw_value.endswith("]"):
            frontmatter[key] = ast.literal_eval(raw_value)
        elif raw_value.startswith('"') and raw_value.endswith('"'):
            frontmatter[key] = raw_value[1:-1]
        elif raw_value.startswith("'") and raw_value.endswith("'"):
            frontmatter[key] = raw_value[1:-1]
        else:
            frontmatter[key] = raw_value
    return frontmatter, body.strip()


def markdown_to_blocks(markdown_text: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped == "***" or stripped == "---":
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            continue

        if stripped.startswith("### "):
            blocks.append(rich_text_block("heading_3", stripped[4:]))
            continue

        if stripped.startswith("## "):
            blocks.append(rich_text_block("heading_2", stripped[3:]))
            continue

        if stripped.startswith("# "):
            blocks.append(rich_text_block("heading_1", stripped[2:]))
            continue

        if stripped.startswith("> "):
            blocks.append(rich_text_block("quote", stripped[2:]))
            continue

        if stripped.startswith("- "):
            blocks.append(rich_text_block("bulleted_list_item", stripped[2:]))
            continue

        blocks.append(rich_text_block("paragraph", stripped))
    return blocks


def rich_text_block(block_type: str, text: str) -> dict[str, Any]:
    return {
        "object": "block",
        "type": block_type,
        block_type: {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": text[:2000]},
                }
            ]
        },
    }


def notion_page_exists(slug: str) -> bool:
    database_id = require_env("NOTION_DATABASE_ID")
    payload = {
        "filter": {
            "property": "Slug",
            "rich_text": {"equals": slug},
        },
        "page_size": 1,
    }
    response = notion_request(
        "POST",
        f"https://api.notion.com/v1/databases/{database_id}/query",
        payload,
    )
    return bool(response.get("results"))


def create_notion_page(frontmatter: dict[str, Any], body: str) -> str:
    database_id = require_env("NOTION_DATABASE_ID")
    title = str(frontmatter.get("title", "")).strip()
    slug = str(frontmatter.get("slug", "")).strip()
    summary = str(frontmatter.get("summary", "")).strip()
    categories = frontmatter.get("categories") or ["mindset"]
    tags = frontmatter.get("tags") or []
    lenny_episode = str(frontmatter.get("lenny_episode", "")).strip()
    cta_type = str(frontmatter.get("cta_type", "course")).strip() or "course"
    published_date = str(frontmatter.get("date", "")).strip()

    if not title or not slug:
        raise SystemExit("Each markdown file must have both title and slug in frontmatter.")

    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Title": {"title": [{"text": {"content": title[:2000]}}]},
            "Slug": {"rich_text": [{"text": {"content": slug[:2000]}}]},
            "Summary": {"rich_text": [{"text": {"content": summary[:2000]}}]},
            "Category": {"select": {"name": str(categories[0])}},
            "Tags": {"multi_select": [{"name": str(tag)} for tag in tags]},
            "Lenny Episode": {"rich_text": [{"text": {"content": lenny_episode[:2000]}}]},
            "CTA Type": {"select": {"name": cta_type}},
            "Status": {"select": {"name": "Review"}},
            "Published Date": {"date": {"start": published_date}} if published_date else {"date": None},
        },
        "children": markdown_to_blocks(body)[:100],
    }

    response = notion_request("POST", "https://api.notion.com/v1/pages", payload)
    return str(response.get("url", ""))


def discover_files(args: argparse.Namespace) -> list[Path]:
    if args.files:
        return [Path(path).resolve() for path in args.files]

    posts = sorted(CONTENT_DIR.glob("*.md"))
    selected: list[Path] = []
    for post in posts:
        frontmatter, _ = parse_frontmatter(post.read_text(encoding="utf-8"))
        post_date = str(frontmatter.get("date", "")).strip()
        post_status = str(frontmatter.get("status", "")).strip()
        if args.since_date and post_date < args.since_date:
            continue
        if args.status and post_status != args.status:
            continue
        selected.append(post)
    return selected


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Push local Hugo posts to Notion")
    parser.add_argument("files", nargs="*", help="Specific markdown files to push")
    parser.add_argument("--since-date", help="Only push posts with frontmatter date >= YYYY-MM-DD")
    parser.add_argument("--status", help="Only push posts with the exact frontmatter status")
    parser.add_argument("--skip-existing", action="store_true", default=True, help="Skip posts if the same slug already exists in Notion")
    return parser


def main() -> int:
    load_env_files()
    parser = build_parser()
    args = parser.parse_args()
    files = discover_files(args)

    if not files:
        print("No matching markdown files found.")
        return 0

    for path in files:
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        slug = str(frontmatter.get("slug", "")).strip()
        title = str(frontmatter.get("title", path.stem)).strip()

        if args.skip_existing and slug and notion_page_exists(slug):
            print(f"⏭ Skipped existing slug in Notion: {slug}")
            continue

        page_url = create_notion_page(frontmatter, body)
        print(f"✅ Pushed to Notion: {title}")
        if page_url:
            print(f"   {page_url}")

    return 0


if __name__ == "__main__":
    sys.exit(main())