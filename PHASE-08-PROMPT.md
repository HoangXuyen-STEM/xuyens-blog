# PHASE 8: NOTION CMS PIPELINE
## Prompt cho Antigravity — Claude Opus 4.6 (Thinking)

> Biến Notion thành CMS cho blog.xuyenlab.com.
> Xuyen viết/edit trên Notion → blog tự cập nhật.
> Blog Hugo đã live tại blog.xuyenlab.com (Docker + Nginx, port 2368).

---

## CONTEXT

- Blog Hugo đang chạy tại: `~/Documents/Dự án/xuyens-blog/blog/`
- Docker container: `xuyens-blog` trên port 2368
- Cloudflare Tunnel: blog.xuyenlab.com → localhost:2368
- Server: Ubuntu 24.04, Python 3.12.3, Docker có sẵn
- Xuyen sẽ cung cấp Notion API Key khi được hỏi
- Notion workspace: tài khoản teacher, đã dùng quen

---

## TASK 8.1: TẠO NOTION DATABASE

### Việc cần làm:
Tạo database "Blog Posts" trong Notion workspace của Xuyen (dưới page "Tạo Blog").

### Database Schema:

| Property | Type | Options/Notes |
|----------|------|---------------|
| **Title** | Title | Tiêu đề bài viết |
| **Slug** | Rich Text | URL slug, vd: `ai-khong-cuop-viec` |
| **Summary** | Rich Text | 1-2 câu tóm tắt |
| **Category** | Select | `ai-technology`, `mindset`, `framework`, `career` |
| **Tags** | Multi-select | Tự do thêm tags |
| **Lenny Episode** | Rich Text | Tên guest / episode info |
| **CTA Type** | Select | `coffee`, `course` |
| **Status** | Select | `Draft`, `Review`, `Published`, `Archived` |
| **Published Date** | Date | Ngày publish |
| **Thumbnail** | Files & Media | Upload ảnh thumbnail |

### Lưu ý:
- Hỏi Xuyen Notion API Key để tạo database qua API
- Hoặc tạo thủ công trên Notion UI — hướng dẫn Xuyen từng bước
- Database phải được share với Notion Integration (để API truy cập được)
- Parent page ID: `3060ed5fbd4780f3b563e456011168b5` (page "Tạo Blog")

### Kiểm tra:
- [ ] Database "Blog Posts" đã tạo trên Notion
- [ ] Tất cả properties đúng type
- [ ] Database đã share với Integration

---

## TASK 8.2: MIGRATE 8 BÀI HIỆN TẠI VÀO NOTION

### Việc cần làm:
Đọc 8 file .md trong `content/posts/` → tạo 8 pages trong Notion database.

### Quy trình cho mỗi bài:
1. Đọc frontmatter → điền vào database properties
2. Đọc nội dung markdown → tạo Notion page content (blocks)
3. Set Status = "Published"

### Danh sách 8 bài:
```bash
ls ~/Documents/Dự\ án/xuyens-blog/blog/content/posts/*.md
```

### Kiểm tra:
- [ ] 8 pages trong Notion database
- [ ] Properties đúng (title, slug, category, tags, status...)
- [ ] Nội dung bài hiện đúng trong Notion page
- [ ] Tất cả 8 bài Status = "Published"

---

## TASK 8.3: VIẾT SYNC SCRIPT

### Việc cần làm:
Tạo Python script: `sync_notion_to_hugo.py`
Đặt tại: `~/Documents/Dự án/xuyens-blog/sync/`

### Chức năng:
```
1. Kết nối Notion API
2. Query database → lấy tất cả bài Status = "Published"
3. Cho mỗi bài:
   a. Đọc properties → tạo frontmatter YAML
   b. Đọc page content (blocks) → convert sang Markdown
   c. Download thumbnail (nếu có) → lưu vào static/images/
   d. Tạo file .md trong content/posts/
4. Xóa bài đã "Archived" khỏi content/posts/
5. Build Hugo: hugo --minify
6. Rebuild Docker: docker compose up -d --build
```

### Cấu trúc thư mục:
```
~/Documents/Dự án/xuyens-blog/
├── blog/                    ← Hugo project (đã có)
│   ├── content/posts/       ← Bài viết (sync từ Notion)
│   ├── static/images/       ← Thumbnails (sync từ Notion)
│   └── ...
├── sync/                    ← MỚI
│   ├── sync_notion_to_hugo.py
│   ├── requirements.txt
│   └── .env                 ← NOTION_API_KEY, NOTION_DATABASE_ID
└── docker-compose.yml       ← Đã có
```

### File `.env`:
```
NOTION_API_KEY=secret_xxxxx
NOTION_DATABASE_ID=xxxxx
HUGO_CONTENT_DIR=/home/hoang-xuyen/Documents/Dự án/xuyens-blog/blog/content/posts/
HUGO_IMAGES_DIR=/home/hoang-xuyen/Documents/Dự án/xuyens-blog/blog/static/images/
HUGO_PROJECT_DIR=/home/hoang-xuyen/Documents/Dự án/xuyens-blog/blog/
```

### `requirements.txt`:
```
requests
python-dotenv
```

### Notion blocks → Markdown conversion cần hỗ trợ:
| Notion Block | Markdown Output |
|-------------|----------------|
| paragraph | `text\n\n` |
| heading_2 | `## text\n\n` |
| heading_3 | `### text\n\n` |
| bulleted_list_item | `- text\n` |
| numbered_list_item | `1. text\n` |
| quote | `> text\n\n` |
| code | ` ```lang\ncode\n``` ` |
| image | `![](url)\n\n` |
| divider | `---\n\n` |
| **bold** | `**text**` |
| *italic* | `*text*` |
| `code` | `` `text` `` |

### Frontmatter output format:
```yaml
---
title: "Tiêu đề"
slug: "slug-khong-dau"
summary: "Tóm tắt"
category: "ai-technology"
tags: ["tag1", "tag2"]
thumbnail: "/images/slug.jpg"
lenny_episode: "Guest Name"
cta_type: "coffee"
published_date: "2026-02-15"
status: "published"
---
```

### Kiểm tra:
- [ ] Script chạy không lỗi: `python3 sync_notion_to_hugo.py`
- [ ] File .md được tạo đúng trong content/posts/
- [ ] Frontmatter đúng format
- [ ] Markdown content đúng (heading, bold, italic, list...)
- [ ] Thumbnail download đúng
- [ ] Hugo build thành công sau sync
- [ ] Blog hiển thị đúng sau rebuild

---

## TASK 8.4: TẠO AUTO-SYNC

### Việc cần làm:
Setup cron job chạy sync script mỗi 15 phút.

### Cron job:
```bash
crontab -e

# Thêm dòng:
*/15 * * * * cd /home/hoang-xuyen/Documents/Dự\ án/xuyens-blog/sync && /usr/bin/python3 sync_notion_to_hugo.py >> /var/log/blog-sync.log 2>&1
```

### Hoặc tạo systemd timer (ổn định hơn):

File: `/etc/systemd/system/blog-sync.service`
```ini
[Unit]
Description=Sync Notion to Hugo Blog

[Service]
Type=oneshot
User=hoang-xuyen
WorkingDirectory=/home/hoang-xuyen/Documents/Dự án/xuyens-blog/sync
ExecStart=/usr/bin/python3 sync_notion_to_hugo.py
Environment=HOME=/home/hoang-xuyen
```

File: `/etc/systemd/system/blog-sync.timer`
```ini
[Unit]
Description=Run blog sync every 15 minutes

[Timer]
OnBootSec=2min
OnUnitActiveSec=15min

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable blog-sync.timer
sudo systemctl start blog-sync.timer
```

### Kiểm tra:
- [ ] Cron/timer đã cài đặt
- [ ] Đợi 15 phút → kiểm tra log: `tail -f /var/log/blog-sync.log`
- [ ] Sửa 1 bài trên Notion → đợi sync → blog cập nhật

---

## TASK 8.5: TEST END-TO-END

### Test 1: Sửa bài trên Notion
1. Mở 1 bài trong Notion → sửa tiêu đề hoặc nội dung
2. Đợi sync cycle (hoặc chạy thủ công: `python3 sync_notion_to_hugo.py`)
3. Kiểm tra blog.xuyenlab.com → bài đã cập nhật

### Test 2: Tạo bài mới trên Notion
1. Tạo page mới trong database → điền properties
2. Viết nội dung → Set Status = "Published"
3. Đợi sync → kiểm tra blog hiện bài mới

### Test 3: Ẩn bài
1. Đổi Status → "Archived"
2. Đợi sync → bài biến mất khỏi blog

### Test 4: Draft không hiện
1. Tạo bài mới → Status = "Draft"
2. Đợi sync → bài KHÔNG hiện trên blog

### Kiểm tra:
- [ ] Test 1: Sửa bài → blog cập nhật ✅
- [ ] Test 2: Bài mới → blog hiện ✅
- [ ] Test 3: Archived → blog ẩn ✅
- [ ] Test 4: Draft → không hiện ✅

---

## TASK 8.6: TẠO SCRIPT MANUAL SYNC

Để Xuyen có thể trigger sync ngay (không đợi 15 phút):

File: `~/Documents/Dự án/xuyens-blog/sync/sync-now.sh`
```bash
#!/bin/bash
echo "🔄 Syncing Notion → Blog..."
cd /home/hoang-xuyen/Documents/Dự\ án/xuyens-blog/sync
python3 sync_notion_to_hugo.py
echo "✅ Done! Check https://blog.xuyenlab.com"
```

```bash
chmod +x sync-now.sh
```

Xuyen chỉ cần chạy: `./sync-now.sh` khi muốn cập nhật ngay.

---

## TÓM TẮT WORKFLOW SAU PHASE 8

### Viết bài mới:
```
Notion → Tạo page → Viết nội dung → Status = "Published" → Đợi 15 phút → Blog live!
```

### Sửa bài:
```
Notion → Edit page → Đợi 15 phút → Blog cập nhật!
```

### Cập nhật ngay:
```
SSH vào server → ./sync-now.sh → Blog cập nhật ngay!
```

### Ẩn bài:
```
Notion → Status = "Archived" → Đợi 15 phút → Bài biến mất!
```

---

## TỔNG KIỂM TRA PHASE 8

- [ ] Notion database "Blog Posts" có đủ 8 bài
- [ ] Sync script chạy không lỗi
- [ ] Auto-sync (cron/timer) hoạt động mỗi 15 phút
- [ ] Sửa trên Notion → blog cập nhật
- [ ] Tạo bài mới → blog hiện
- [ ] Archived → blog ẩn
- [ ] Manual sync script hoạt động
- [ ] Logs ghi nhận đúng

**Pass hết → Phase 8 hoàn thành! 🎉**

---

*Phase 8 Prompt v1.0 — Dùng với model: Claude Opus 4.6 (Thinking)*
*Hỏi Xuyen Notion API Key khi cần.*
