# Phase 02: Trang chủ (Homepage)
Status: ⬜ Pending
Dependencies: Phase 01

## Objective
Build trang chủ hiện danh sách bài viết (mới nhất lên đầu), style tối giản kiểu tinystakeholders.com. Tạo bài viết mẫu để test.

## Requirements
### Functional
- [ ] Danh sách bài viết hiện: thumbnail, title, summary, date, category
- [ ] Sắp xếp: bài mới nhất lên đầu
- [ ] Chỉ hiện bài có `status: "published"` (ẩn draft)
- [ ] Click bài → đến trang bài viết

### Non-Functional
- [ ] Style tối giản, sạch sẽ, dễ đọc
- [ ] Typography tốt — font dễ đọc cho tiếng Việt
- [ ] Load nhanh (static site)

## Implementation Steps
1. [ ] Tạo 1 bài viết mẫu `.md` đúng frontmatter format (PRD §4.2)
2. [ ] Build `layouts/index.html` — hiện danh sách bài:
   - Loop qua `content/posts/`
   - Filter: chỉ `status = "published"`
   - Sort: `published_date` descending
   - Hiện: thumbnail, title, summary, date, category badge
3. [ ] Viết `static/css/style.css`:
   - Color scheme: trắng/đen tối giản
   - Typography: Google Fonts (Inter hoặc Noto Sans Vietnamese)
   - Card layout cho mỗi bài
   - Spacing, line-height thoáng

## Files to Create/Modify
- `content/posts/ai-khong-cuop-viec.md` — Bài mẫu
- `layouts/index.html` — Homepage template
- `layouts/_default/baseof.html` — Update base template (head, nav, footer)
- `static/css/style.css` — Main stylesheet
- `layouts/partials/post-card.html` — Partial cho 1 card bài viết

## Test Criteria
- [ ] Trang chủ hiện bài mẫu với đầy đủ: thumbnail, title, summary, date, category
- [ ] Bài draft không hiện trên trang chủ
- [ ] Style sạch sẽ, typography rõ ràng
- [ ] Click vào bài → chuyển đến URL bài viết

## Notes
- Tham khảo tinystakeholders.com: layout 1 cột, typography lớn, spacing thoáng
- Font cần hỗ trợ tiếng Việt tốt (có dấu)

---
Next Phase: [phase-03-post-page.md](./phase-03-post-page.md)
