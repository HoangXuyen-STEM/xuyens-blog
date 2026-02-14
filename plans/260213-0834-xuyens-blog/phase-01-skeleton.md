# Phase 01: Dựng khung blog (Skeleton)
Status: ✅ Complete
Dependencies: Không

## Objective
Cài đặt Hugo, tạo project mới, thiết lập cấu trúc thư mục đúng theo Data Model trong PRD, cấu hình `config.toml` cơ bản.

## Requirements
### Functional
- [ ] Hugo project chạy được với `hugo server`
- [ ] Cấu trúc thư mục đúng: `content/posts/`, `content/about.md`, `static/images/`, `static/css/`, `layouts/`, `data/`
- [ ] `config.toml` có: tên blog "Xuyen's Blog", baseURL, menu items, CTA links

### Non-Functional
- [ ] Không dùng theme có sẵn — custom layout từ đầu
- [ ] Cấu trúc sạch, dễ mở rộng

## Implementation Steps
1. [ ] Kiểm tra Hugo đã cài chưa, nếu chưa thì cài đặt
2. [ ] Tạo Hugo project mới tại thư mục `xuyens-blog/`
3. [ ] Tạo cấu trúc thư mục theo Data Model (PRD §4.1)
4. [ ] Viết `config.toml`:
   - `baseURL = "https://blog.xuyenlab.com/"`
   - `title = "Xuyen's Blog"`
   - Menu: Home, About, Categories
   - Params: CTA links (Eakar Coffee, Khóa học)
5. [ ] Tạo layout cơ bản (baseof.html, index.html) — trang trắng có title
6. [ ] Chạy `hugo server` để verify

## Files to Create/Modify
- `config.toml` — Cấu hình Hugo chính
- `layouts/_default/baseof.html` — Base template
- `layouts/index.html` — Homepage template (tạm trống)
- `content/posts/.gitkeep` — Giữ folder structure
- `content/about.md` — Placeholder About page
- `static/css/style.css` — Stylesheet trống
- `static/images/default-thumbnail.jpg` — Ảnh mặc định
- `data/subscribers.json` — File subscribers trống `[]`

## Test Criteria
- [ ] `hugo server` chạy không lỗi
- [ ] Truy cập `localhost:1313` thấy trang có title "Xuyen's Blog"
- [ ] Cấu trúc thư mục đúng theo PRD

## Notes
- Không dùng Hugo theme — build custom từ scratch cho phong cách tinystakeholders.com
- `config.toml` cần khai báo đủ params để các phase sau dùng

---
Next Phase: [phase-02-homepage.md](./phase-02-homepage.md)
