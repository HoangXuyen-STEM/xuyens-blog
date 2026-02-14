# Phase 05: Newsletter + Polish
Status: ⬜ Pending
Dependencies: Phase 04

## Objective
Thêm form đăng ký Newsletter, xử lý edge cases, hoàn thiện responsive mobile.

## Requirements
### Functional
- [ ] Form email ở trang chủ và cuối mỗi bài viết
- [ ] Submit → lưu email vào `data/subscribers.json`
- [ ] Email trùng → báo "Bạn đã đăng ký rồi"
- [ ] Submit thành công → báo "Cảm ơn bạn đã đăng ký!"
- [ ] Bài chưa có thumbnail → hiện `default-thumbnail.jpg`
- [ ] Bài `status: "draft"` → không hiện trên trang chủ (đã làm Phase 2, verify lại)

### Non-Functional
- [ ] Responsive: mobile hiển thị tốt (320px → 1440px)
- [ ] Form validate email format trước khi submit
- [ ] UX mượt: feedback tức thì khi submit

## Implementation Steps
1. [ ] Tạo `layouts/partials/newsletter-form.html`:
   - Input email + button "Đăng ký"
   - JavaScript xử lý submit (fetch API hoặc form action)
2. [ ] Tạo endpoint xử lý subscribe:
   - **Option A:** Static approach — JS đọc/ghi `subscribers.json` (giới hạn: cần server-side)
   - **Option B:** Dùng Netlify Functions / Cloudflare Workers (nếu deploy home server)
   - **Option C:** Google Forms / Formspree embed (đơn giản nhất cho MVP)
   - → Chọn **Option C** cho MVP, upgrade sau
3. [ ] Thêm newsletter form vào: `index.html` (trang chủ) + `single.html` (cuối bài)
4. [ ] Xử lý edge cases:
   - Default thumbnail khi `thumbnail` trống
   - Verify draft filtering
5. [ ] Responsive CSS:
   - Mobile breakpoints: 768px, 480px
   - Nav → hamburger
   - Post cards → 1 column
   - Images → 100% width
   - Font size adjustments

## Files to Create/Modify
- `layouts/partials/newsletter-form.html` — [NEW] Newsletter form component
- `static/js/newsletter.js` — [NEW] Form handling JavaScript
- `layouts/index.html` — [MODIFY] Thêm newsletter section
- `layouts/posts/single.html` — [MODIFY] Thêm newsletter cuối bài
- `static/css/style.css` — [MODIFY] Responsive + form styles
- `layouts/partials/post-card.html` — [MODIFY] Default thumbnail fallback

## Test Criteria
- [ ] Form hiện ở trang chủ và cuối bài
- [ ] Nhập email → submit → hiện thông báo cảm ơn
- [ ] Mobile 375px: mọi thứ hiển thị tốt, không bị tràn
- [ ] Tablet 768px: layout hợp lý
- [ ] Bài không có thumbnail → hiện ảnh mặc định
- [ ] Bài draft → không hiện

## Notes
- MVP dùng 3rd party form service (Formspree/Google Forms) → đơn giản, không cần backend
- Sau này upgrade lên self-hosted nếu cần
- Test responsive bằng Chrome DevTools

---
Next Phase: [phase-06-content-pipeline.md](./phase-06-content-pipeline.md)
