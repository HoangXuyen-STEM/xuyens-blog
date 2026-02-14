# Phase 03: Trang bài viết (Post Page)
Status: ⬜ Pending
Dependencies: Phase 02

## Objective
Tạo template cho trang bài viết đầy đủ: nội dung markdown → HTML, metadata, CTA cuối bài, bài liên quan.

## Requirements
### Functional
- [ ] Hiển thị nội dung bài viết (markdown → HTML) đầy đủ
- [ ] Hiện metadata: published_date, category, tags, lenny_episode
- [ ] CTA cuối bài: tùy theo `cta_type` (coffee → Eakar Coffee, course → Khóa học)
- [ ] Bài liên quan: 2-3 bài cùng category
- [ ] Nếu không có bài cùng category → hiện bài mới nhất

### Non-Functional
- [ ] Reading experience tốt — line-height, font-size, max-width thoải mái
- [ ] Code blocks, lists, blockquotes render đẹp
- [ ] CTA nổi bật nhưng không phản cảm

## Implementation Steps
1. [ ] Tạo `layouts/posts/single.html` — template bài viết:
   - Header: title, date, category badge, tags
   - Body: `.Content` (Hugo render markdown)
   - Lenny episode reference (nếu có)
2. [ ] Tạo `layouts/partials/cta-banner.html`:
   - If `cta_type == "coffee"` → Banner Eakar Coffee với link
   - If `cta_type == "course"` → Banner Khóa học với link
3. [ ] Tạo `layouts/partials/related-posts.html`:
   - Query: bài cùng `category`, exclude bài hiện tại, limit 3
   - Fallback: nếu < 2 bài cùng category → bổ sung bài mới nhất
4. [ ] Update CSS: typography cho article content, CTA styles, related posts grid

## Files to Create/Modify
- `layouts/posts/single.html` — [NEW] Template bài viết
- `layouts/partials/cta-banner.html` — [NEW] CTA component
- `layouts/partials/related-posts.html` — [NEW] Related posts component
- `static/css/style.css` — [MODIFY] Thêm styles cho post page
- `content/posts/` — Thêm 2-3 bài mẫu nữa (để test related posts)

## Test Criteria
- [ ] Click bài từ trang chủ → hiện nội dung đầy đủ
- [ ] Metadata hiện đúng (date, category, tags)
- [ ] CTA cuối bài đúng loại theo `cta_type`
- [ ] Bài liên quan hiện 2-3 bài cùng category
- [ ] Bài không có bài liên quan cùng category → hiện bài mới nhất
- [ ] Markdown render đẹp (headings, bold, italic, code, lists, quotes)

## Notes
- CTA links lấy từ `config.toml` params (đã set ở Phase 1)
- `lenny_episode` hiện dạng: "💡 Insight từ Lenny's Podcast EP.189"

---
Next Phase: [phase-04-secondary-pages.md](./phase-04-secondary-pages.md)
