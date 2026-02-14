# Changelog

Tất cả các thay đổi quan trọng của dự án sẽ được ghi nhận tại đây.

## [2026-02-13] - Phát triển bộ khung Core

### Added
- [Phase 1] Khởi tạo project Hugo, cấu trúc folder và config chuẩn.
- [Phase 2] Trang chủ với layout 1 cột, post-card hiện thumbnail và category.
- [Phase 3] Template bài viết (single post) với:
    - Typography chuẩn SEO.
    - CTA Banner linh hoạt (Coffee vs Course).
    - Related posts grid với logic fallback (bài mới nhất).
- [Phase 4] Các trang phụ và điều hướng:
    - Trang About Me (nội dung thực).
    - Landing page cho từng danh mục (Category pages).
    - Trang 404 tùy chỉnh.
    - Mobile Navigation với hamburger menu (Vanilla JS).
    - Footer với social links.

### Fixed
- Lỗi syntax CSS làm vỡ layout footer.
- Logic lọc bài draft trên trang chủ.
- Responsive cho post card trên màn hình nhỏ.
