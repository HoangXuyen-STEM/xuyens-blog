# PHASE 8: NOTION CMS PIPELINE (Sau Launch)
## Thiết kế sẵn — Triển khai sau khi blog.xuyenlab.com đã live

> Biến Notion thành CMS quản lý nội dung → tự động publish lên blog.
> Xuyen chỉ cần viết/edit trên Notion → blog tự cập nhật.

---

## 1. TỔNG QUAN

### Hiện tại (Phase 7 — Thủ công):
```
Viết bài .md → copy vào content/posts/ → hugo build → deploy
```

### Mục tiêu (Phase 8 — Tự động):
```
Viết/edit trên Notion → Script tự động pull → hugo build → deploy
```

### Lợi ích:
- Xuyen quản lý bài viết trực quan trên Notion (đã quen dùng)
- Edit bài = edit trên Notion, blog tự cập nhật
- Không cần mở terminal, không cần biết Hugo
- Team/cộng tác viên có thể viết bài trên Notion
- Quản lý status (Draft/Review/Published) bằng Notion database

---

## 2. KIẾN TRÚC

```
┌─────────────────────────────────────────────────┐
│                   NOTION                         │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │  Database: "Blog Posts"                   │   │
│  │  ┌─────────┬──────────┬────────────────┐ │   │
│  │  │ Title   │ Status   │ Category       │ │   │
│  │  ├─────────┼──────────┼────────────────┤ │   │
│  │  │ Bài 1   │Published │ AI & Công nghệ │ │   │
│  │  │ Bài 2   │Draft     │ Mindset        │ │   │
│  │  │ Bài 3   │Review    │ Framework      │ │   │
│  │  └─────────┴──────────┴────────────────┘ │   │
│  └──────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────┘
                     │ Notion API
                     ▼
┌─────────────────────────────────────────────────┐
│              SYNC SCRIPT (Home Server)           │
│                                                  │
│  1. Pull bài "Published" từ Notion               │
│  2. Convert Notion blocks → Hugo Markdown        │
│  3. Download ảnh → static/images/                │
│  4. Tạo frontmatter từ database properties       │
│  5. Lưu vào content/posts/                       │
│  6. Hugo build --minify                          │
│  7. Deploy (restart Nginx container)             │
└────────────────────┬────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────┐
│              BLOG (blog.xuyenlab.com)            │
│              Hugo static site                    │
└─────────────────────────────────────────────────┘
```

---

## 3. NOTION DATABASE SCHEMA

### Database: "Blog Posts"

| Property | Type | Mô tả |
|----------|------|-------|
| **Title** | Title | Tiêu đề bài viết |
| **Slug** | Rich Text | URL slug (vd: ai-khong-cuop-viec) |
| **Summary** | Rich Text | 1-2 câu tóm tắt |
| **Category** | Select | ai-technology, mindset, framework, career |
| **Tags** | Multi-select | Tags cho bài viết |
| **Lenny Episode** | Rich Text | Tên guest / episode |
| **CTA Type** | Select | coffee, course |
| **Status** | Select | Draft, Review, Published, Archived |
| **Published Date** | Date | Ngày publish |
| **Thumbnail** | Files & Media | Upload ảnh watercolor |
| **Author Notes** | Rich Text | Ghi chú nội bộ (không publish) |

### Workflow trên Notion:
```
Draft → Review → Published → (blog tự cập nhật)
                              ↓
                         Archived (ẩn khỏi blog)
```

---

## 4. SYNC SCRIPT

### Công nghệ: Python + Notion API

### File: `sync_notion_to_hugo.py`

```python
"""
Notion → Hugo Sync Script
Chạy mỗi 15 phút hoặc khi có webhook trigger.
"""

import os
import requests
from datetime import datetime

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")
HUGO_CONTENT_DIR = "/path/to/xuyens-blog/content/posts/"
HUGO_IMAGES_DIR = "/path/to/xuyens-blog/static/images/"

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_published_posts():
    """Lấy tất cả bài Status = Published từ Notion"""
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "Status",
            "select": {"equals": "Published"}
        },
        "sorts": [
            {"property": "Published Date", "direction": "descending"}
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()["results"]

def get_page_content(page_id):
    """Lấy nội dung blocks của 1 page"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    response = requests.get(url, headers=HEADERS)
    return response.json()["results"]

def notion_blocks_to_markdown(blocks):
    """Convert Notion blocks → Hugo Markdown"""
    md = ""
    for block in blocks:
        btype = block["type"]
        
        if btype == "paragraph":
            text = extract_rich_text(block["paragraph"]["rich_text"])
            md += f"{text}\n\n"
        
        elif btype == "heading_2":
            text = extract_rich_text(block["heading_2"]["rich_text"])
            md += f"## {text}\n\n"
        
        elif btype == "heading_3":
            text = extract_rich_text(block["heading_3"]["rich_text"])
            md += f"### {text}\n\n"
        
        elif btype == "bulleted_list_item":
            text = extract_rich_text(block["bulleted_list_item"]["rich_text"])
            md += f"- {text}\n"
        
        elif btype == "quote":
            text = extract_rich_text(block["quote"]["rich_text"])
            md += f"> {text}\n\n"
        
        elif btype == "image":
            url = block["image"].get("file", {}).get("url", "")
            if not url:
                url = block["image"].get("external", {}).get("url", "")
            md += f"![]({url})\n\n"
        
        elif btype == "divider":
            md += "---\n\n"
    
    return md

def extract_rich_text(rich_text_array):
    """Extract text từ Notion rich text array"""
    result = ""
    for rt in rich_text_array:
        text = rt["plain_text"]
        annotations = rt.get("annotations", {})
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("code"):
            text = f"`{text}`"
        result += text
    return result

def create_hugo_post(page, content_md):
    """Tạo file .md cho Hugo từ Notion page"""
    props = page["properties"]
    
    title = props["Title"]["title"][0]["plain_text"]
    slug = props["Slug"]["rich_text"][0]["plain_text"] if props["Slug"]["rich_text"] else title.lower().replace(" ", "-")
    summary = props["Summary"]["rich_text"][0]["plain_text"] if props["Summary"]["rich_text"] else ""
    category = props["Category"]["select"]["name"] if props["Category"]["select"] else "mindset"
    tags = [t["name"] for t in props["Tags"]["multi_select"]] if props["Tags"]["multi_select"] else []
    lenny_ep = props["Lenny Episode"]["rich_text"][0]["plain_text"] if props["Lenny Episode"]["rich_text"] else ""
    cta_type = props["CTA Type"]["select"]["name"] if props["CTA Type"]["select"] else "coffee"
    pub_date = props["Published Date"]["date"]["start"] if props["Published Date"]["date"] else datetime.now().strftime("%Y-%m-%d")
    
    # Download thumbnail nếu có
    thumbnail_path = f"/images/{slug}.jpg"
    if props["Thumbnail"]["files"]:
        img_url = props["Thumbnail"]["files"][0]["file"]["url"]
        download_image(img_url, f"{HUGO_IMAGES_DIR}{slug}.jpg")
    else:
        thumbnail_path = "/images/default-thumbnail.svg"
    
    # Tạo frontmatter
    frontmatter = f"""---
title: "{title}"
slug: "{slug}"
summary: "{summary}"
category: "{category}"
tags: {tags}
thumbnail: "{thumbnail_path}"
lenny_episode: "{lenny_ep}"
cta_type: "{cta_type}"
published_date: "{pub_date}"
status: "published"
---

"""
    
    # Lưu file
    filepath = f"{HUGO_CONTENT_DIR}{slug}.md"
    with open(filepath, "w") as f:
        f.write(frontmatter + content_md)
    
    print(f"✅ Created: {filepath}")

def download_image(url, filepath):
    """Download ảnh từ Notion"""
    response = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(response.content)

def build_and_deploy():
    """Build Hugo và deploy"""
    os.system("cd /path/to/xuyens-blog && hugo --minify")
    os.system("docker-compose -f /path/to/xuyens-blog/docker-compose.yml up -d --build")
    print("🚀 Blog deployed!")

def main():
    print(f"🔄 Syncing Notion → Hugo... ({datetime.now()})")
    
    posts = get_published_posts()
    print(f"📝 Found {len(posts)} published posts")
    
    for page in posts:
        page_id = page["id"]
        blocks = get_page_content(page_id)
        content_md = notion_blocks_to_markdown(blocks)
        create_hugo_post(page, content_md)
    
    build_and_deploy()
    print("✅ Sync complete!")

if __name__ == "__main__":
    main()
```

---

## 5. TỰ ĐỘNG HÓA

### Cách 1: Cron job (Đơn giản)
```bash
# Chạy mỗi 15 phút
*/15 * * * * cd /path/to/xuyens-blog && python3 sync_notion_to_hugo.py >> /var/log/blog-sync.log 2>&1
```

### Cách 2: Notion Webhook (Real-time hơn)
- Dùng Notion API webhook (nếu có)
- Hoặc dùng service như Pipedream/Make.com trigger khi Notion database thay đổi

### Cách 3: Docker container riêng
```yaml
# Thêm vào docker-compose.yml
services:
  blog-sync:
    build: ./sync
    container_name: blog-sync
    restart: unless-stopped
    environment:
      - NOTION_API_KEY=${NOTION_API_KEY}
      - NOTION_DATABASE_ID=${NOTION_DATABASE_ID}
    volumes:
      - ./content:/app/content
      - ./static/images:/app/images
    # Chạy mỗi 15 phút
    command: >
      sh -c "while true; do python sync_notion_to_hugo.py; sleep 900; done"
```

---

## 6. WORKFLOW SAU KHI CÓ NOTION CMS

### Viết bài mới:
```
1. Mở Notion → Database "Blog Posts"
2. Tạo page mới → Viết nội dung
3. Điền properties (category, tags, slug, thumbnail...)
4. Set Status = "Published"
5. Đợi 15 phút (hoặc trigger thủ công)
6. Blog tự cập nhật! ✅
```

### Edit bài cũ:
```
1. Mở bài trên Notion → sửa nội dung
2. Đợi sync cycle
3. Blog tự cập nhật! ✅
```

### Ẩn bài:
```
1. Đổi Status → "Archived"
2. Sync cycle → bài biến mất khỏi blog ✅
```

### Antigravity viết bài:
```
1. Antigravity viết bài → output Notion page (dùng Notion MCP)
2. Xuyen review trên Notion
3. Set Status = "Published"
4. Blog tự đăng! ✅
```

---

## 7. TASK BREAKDOWN — PHASE 8

| Task | Việc | Effort |
|------|------|--------|
| 8.1 | Tạo Notion Database "Blog Posts" đúng schema | 30 phút |
| 8.2 | Migrate 8 bài hiện tại vào Notion database | 1 giờ |
| 8.3 | Code sync script (Python + Notion API) | 2-3 giờ |
| 8.4 | Setup cron job / Docker container | 30 phút |
| 8.5 | Test end-to-end: edit trên Notion → blog cập nhật | 30 phút |
| 8.6 | Tạo workflow cho Antigravity viết bài → Notion | 1 giờ |

**Tổng:** ~5-6 giờ

### Model allocation:
- Task 8.1-8.2: Gemini 3 Flash (việc đơn giản)
- Task 8.3: Claude Opus 4.6 (logic phức tạp, API)
- Task 8.4-8.5: Claude Sonnet 4.5 (server config)
- Task 8.6: Claude Opus 4.6 (workflow design)

---

## 8. PREREQUISITES

Trước khi làm Phase 8, Xuyen cần:
- [ ] Notion API Key (tạo integration tại https://www.notion.so/my-integrations)
- [ ] Share database với integration
- [ ] Blog đã live (Phase 7 done)
- [ ] Python 3 + pip trên home server

---

*Phase 8 Spec v1.0 — 2026-02-13*
*Triển khai sau khi blog.xuyenlab.com đã live*
