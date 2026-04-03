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

Production nên deploy qua GitHub Actions sang Cloudflare Pages, không publish tay từ local trừ khi cần khẩn cấp.

### Thiết lập một lần trên GitHub

Thêm 2 repository secrets trong GitHub:

- `CLOUDFLARE_ACCOUNT_ID`
- `CLOUDFLARE_API_TOKEN`

API token cần quyền `Account / Cloudflare Pages / Edit`.

Workflow deploy nằm ở [.github/workflows/deploy-cloudflare-pages.yml](.github/workflows/deploy-cloudflare-pages.yml).

### Quy trình publish chuẩn

1. Sửa nội dung trong `blog/content/...`
2. Commit và push lên nhánh `master`
3. GitHub Actions tự chạy Hugo và deploy `blog/public` lên Cloudflare Pages
4. Kiểm tra production tại `https://blog.xuyenlab.com/`

### Lệnh publish cơ bản

```bash
git add blog/content/duong-dan-bai-viet.md
git commit -m "Cập nhật nội dung bài viết"
git push origin master
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
- `NOTION_SYNC_STATUSES` (ví dụ `Published,Review`)

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

Nếu GitHub Actions hoặc Git integration bị lỗi, có thể deploy tay:

```bash
cd blog
hugo --minify
```

Sau đó upload thư mục `blog/public` lên Cloudflare Pages bằng `Direct Upload`.

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
