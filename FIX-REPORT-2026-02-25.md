# Báo cáo fix lỗi sync Notion → Blog

Ngày thực hiện: 2026-02-25

## 1) Vấn đề ban đầu

- 7 bài gần nhất từ Antigravity đã được viết vào Notion nhưng không tự lên blog.
- Domain production có lúc hiển thị bản cũ/404 dù local đã build có bài mới.

## 2) Nguyên nhân gốc

### A. Lỗi lọc trạng thái bài viết trong script sync

- Script sync chỉ query `Status = Published`.
- Nhiều bài mới đang ở trạng thái `Review` nên bị bỏ qua.

### B. Lỗi routing/deploy tầng Cloudflare Tunnel

- Có xung đột nhiều tiến trình cloudflared (token cũ + token mới + config run).
- Một route/tunnel cũ làm domain không luôn trỏ đúng origin mới nhất.

## 3) Các thay đổi đã thực hiện

### 3.1. Thay đổi mã nguồn trong repo

#### File: `sync/sync_notion_to_hugo.py`

- Thêm cấu hình môi trường:
  - `NOTION_SYNC_STATUSES`
  - Mặc định: `Published,Review`
- Nâng cấp hàm query database:
  - Hỗ trợ 1 status hoặc nhiều status.
  - Nếu nhiều status thì dùng filter `or`.
- Cập nhật bước fetch chính:
  - Từ chỉ lấy Published → lấy theo danh sách `NOTION_SYNC_STATUSES`.

#### File: `blog/docker-compose.yml`

- Bổ sung mapping cổng:
  - `8090:80` (phục vụ theo tunnel route)
  - Giữ `2368:80` để tương thích local hiện có.

#### File: `blog/deploy.sh`

- Cập nhật output deploy để hiển thị thêm:
  - `Tunnel target: http://localhost:8090`

### 3.2. Thay đổi vận hành (runtime) trên máy host

- Cập nhật tunnel config local để dùng tunnel ID đang hoạt động.
- Tạo user service systemd:
  - `~/.config/systemd/user/cloudflared-blog.service`
- Enable + start user service cloudflared chạy từ config chuẩn.
- Tắt/cleanup các tiến trình cloudflared token cũ.
- Xác nhận system service cũ không còn active.

## 4) Kết quả sau fix

### Sync

- Trước fix: sync được 12 bài.
- Sau fix: sync được 17 bài (bao gồm nhóm bài mới trước đó bị bỏ sót).

### Build local

- Hugo build thành công.
- Thư mục `public/posts` có đầy đủ các slug bài mới.

### Production

- `https://blog.xuyenlab.com/` trả 200.
- Bài mới trả 200 (ví dụ):
  - `/posts/make-time-jake-knapp/`
  - `/posts/team-nho-lam-viec-lon-ivan-zhao/`

## 5) Trạng thái hiện tại

- Luồng hoạt động đã ổn định:
  1. Antigravity viết bài vào Notion
  2. Script sync kéo về Hugo
  3. Build + serve qua tunnel
  4. Bài mới hiển thị trên domain production

## 6) Khuyến nghị vận hành

- Giữ duy nhất một cloudflared service chuẩn để tránh xung đột route.
- Dùng `NOTION_SYNC_STATUSES` trong `.env` để điều khiển chính sách publish:
  - Production chặt chẽ: chỉ `Published`
  - Giai đoạn review nội bộ: `Published,Review`
