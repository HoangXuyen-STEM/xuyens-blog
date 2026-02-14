# Phase 04: Các trang phụ
Status: ⬜ Pending
Dependencies: Phase 03

## Objective
Tạo trang About Me, navigation menu hoàn chỉnh, footer với social links. Hoàn thiện bộ khung giao diện.

## Requirements
### Functional
- [ ] Trang About Me: giới thiệu Xuyen — background, vision, tại sao blog này tồn tại
- [ ] Navigation menu: Home, About, 4 Categories (AI & Công nghệ, Mindset, Framework, Career)
- [ ] Footer: social links, copyright, "Powered by Hugo"

### Non-Functional
- [ ] Menu responsive (hamburger trên mobile)
- [ ] Trang About truyền cảm hứng, đúng tone thought-leader gần gũi

## Implementation Steps
1. [ ] Viết `content/about.md` — nội dung About:
   - Xuyen là ai
   - Tại sao blog này ra đời
   - Eakar Coffee connection
   - CTA đăng ký Newsletter
2. [ ] Tạo `layouts/_default/single.html` — template cho trang tĩnh (About)
3. [ ] Update `layouts/partials/nav.html`:
   - Logo/Title: "Xuyen's Blog"
   - Menu items: Home, About, dropdown/list 4 categories
   - Mobile: hamburger menu
4. [ ] Tạo `layouts/partials/footer.html`:
   - Social links (Facebook, LinkedIn, etc.)
   - Copyright © 2026 Xuyen's Blog
5. [ ] Tạo category pages — hiện bài viết theo từng category:
   - `layouts/_default/taxonomy.html` — list bài theo category
   - `layouts/_default/terms.html` — list tất cả categories

## Files to Create/Modify
- `content/about.md` — [MODIFY] Viết nội dung thật
- `layouts/_default/single.html` — [NEW] Template trang tĩnh
- `layouts/partials/nav.html` — [MODIFY] Menu hoàn chỉnh
- `layouts/partials/footer.html` — [NEW] Footer component
- `layouts/_default/taxonomy.html` — [NEW] Category listing
- `layouts/_default/terms.html` — [NEW] All categories page
- `static/css/style.css` — [MODIFY] Nav, footer, about styles
- `config.toml` — [MODIFY] Menu config, taxonomies

## Test Criteria
- [ ] Click "About" trên menu → hiện trang About Me
- [ ] Menu hoạt động: mọi link đúng destination
- [ ] Category page hiện đúng bài thuộc category đó
- [ ] Footer hiện ở mọi trang
- [ ] Mobile: hamburger menu hoạt động

## Notes
- Categories dùng Hugo taxonomies (`category` field trong frontmatter)
- Social links lấy từ `config.toml` params

---
Next Phase: [phase-05-newsletter-polish.md](./phase-05-newsletter-polish.md)
