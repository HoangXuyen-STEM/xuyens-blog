# Xuyen's Blog

Blog tĩnh cá nhân của anh Xuyen. Việt hóa insight từ Lenny's Podcast — Giúp domain expert bắt kịp thời đại AI.

## 🚀 Hướng dẫn phát triển

### 1. Cài đặt
Yêu cầu: **Hugo (Extended version)** v0.145.0 hoặc mới hơn.

### 2. Chạy Local
```bash
cd blog
hugo server --bind 0.0.0.0 --port 1313 --buildDrafts
```
Mở browser tại: `http://localhost:1313`

### 3. Tạo bài viết mới
```bash
hugo new posts/ten-bai-viet.md
```

## 🚢 Publish production

Repo hiện tại deploy production bằng `wrangler pages deploy`, không có GitHub Actions workflow trong repo này.

### Quy trình publish chuẩn

Production dùng pipeline canonical `./publish_pipeline.sh`:

1. Antigravity/AI đẩy bài lên Notion với trạng thái `Review`.
2. Xuyên duyệt và đổi trạng thái thành `Published`.
3. Cron mỗi 15 phút gọi pipeline trong repo hiện tại.
4. Pipeline chỉ sync `Published`, validate frontmatter/thumbnail, build Hugo, commit/push nếu có thay đổi, deploy Cloudflare Pages và verify production.
5. Bài `Review` không được phép vào production tree.

Chạy kiểm tra không deploy:

```bash
./publish_pipeline.sh --dry-run --skip-sync
```

Chạy production thủ công:

```bash
./publish_pipeline.sh
```

### Lệnh publish cơ bản

```bash
cd blog
hugo --minify
cd ..
git add blog/content/duong-dan-bai-viet.md blog/static/images/ten-anh.png
git commit -m "feat(posts): publish new post"
git push origin master
wrangler pages deploy blog/public --project-name xuyens-blog --branch master
```

### Verify sau deploy

```bash
./check_live.sh <slug-1> <slug-2>
```

Hoặc verify tất cả bài mới thêm trong commit gần nhất:

```bash
./check_live.sh --commit HEAD
```

## Notion Pipeline Sau Khi Clone Máy Mới

Một số file tích hợp Notion là file local nên clone máy mới xong cần kiểm tra lại cấu hình môi trường.

### File cần có

- `blog/sync/push_to_notion.py`: đẩy bài markdown local lên Notion
- `blog/sync/sync_notion_to_hugo.py`: kéo bài từ Notion về Hugo
- `blog/.env`: chứa secret local, không commit

### Khởi tạo lại cấu hình

```bash
cp blog/.env.example blog/.env
```

Điền các giá trị:

- `NOTION_API_KEY`
- `NOTION_DATABASE_ID`
- `NOTION_SYNC_STATUSES=Published` — production safety gate; không thêm `Review`

### Lệnh hữu ích

Đẩy các bài local mới từ ngày 2026-04-02 lên Notion ở trạng thái Review:

```bash
cd blog
python3 sync/push_to_notion.py --since-date 2026-04-02
```

Kéo bài từ Notion về Hugo bằng đường dẫn tương đối, không phụ thuộc repo nằm ở đâu:

```bash
cd blog
python3 sync/sync_notion_to_hugo.py
```

### Fallback khi cần deploy gấp

Nếu cần deploy tay ngay từ local:

```bash
cd blog
hugo --minify
```

Sau đó chạy:

```bash
cd ..
wrangler pages deploy blog/public --project-name xuyens-blog --branch master
```

## 🛠 Tech Stack
- **Framework**: Hugo (Extended)
- **Styling**: Vanilla CSS
- **Design Inspiration**: tinystakeholders.com
- **Hosting**: Cloudflare Pages

## 📂 Cấu trúc dự án
- `blog/`: Mã nguồn Hugo
- `docs/`: Tài liệu hướng dẫn
- `plans/`: Kế hoạch thực hiện từng phase
- `.brain/`: Lưu trữ context cho AI (AWF Framework)
