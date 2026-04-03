# Notion Sync

Các script trong thư mục này dùng đường dẫn tương đối theo vị trí file, nên repo có thể được clone sang máy hoặc thư mục khác mà không cần sửa hard-coded path.

## Cấu hình

1. Copy `blog/.env.example` thành `blog/.env`
2. Điền:
   - `NOTION_API_KEY`
   - `NOTION_DATABASE_ID`
   - `NOTION_SYNC_STATUSES` (ví dụ `Published,Review`)

## Lệnh thường dùng

Đẩy các bài local mới lên Notion:

```bash
cd blog
python3 sync/push_to_notion.py --since-date 2026-04-02
```

Kéo bài từ Notion về Hugo:

```bash
cd blog
python3 sync/sync_notion_to_hugo.py
```