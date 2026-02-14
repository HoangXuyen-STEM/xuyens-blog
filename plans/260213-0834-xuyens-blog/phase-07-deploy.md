# Phase 07: Deploy lên Server
Status: ⬜ Pending
Dependencies: Phase 06

## Objective
Build Hugo production → deploy lên home server, cấu hình domain blog.xuyenlab.com, test toàn bộ trên production.

## Requirements
### Functional
- [ ] `hugo build` tạo thư mục `public/` hoàn chỉnh
- [ ] Deploy `public/` lên home server
- [ ] Domain blog.xuyenlab.com trỏ đúng về server
- [ ] HTTPS hoạt động (Cloudflare Tunnel hoặc Let's Encrypt)

### Non-Functional
- [ ] Load time < 2s (static site nên nhanh)
- [ ] SEO basics: title tags, meta description, og:image
- [ ] Sitemap.xml tự động (Hugo built-in)

## Implementation Steps
1. [ ] Chạy `hugo build` → verify `public/` output
2. [ ] Setup deployment trên home server:
   - Copy `public/` → server web root (nginx/caddy)
   - Hoặc dùng rsync/scp script
3. [ ] Cấu hình domain:
   - DNS: blog.xuyenlab.com → home server IP
   - Hoặc Cloudflare Tunnel (nếu đã setup)
4. [ ] Cấu hình web server (nginx hoặc caddy):
   - Serve static files từ `public/`
   - HTTPS certificate
   - Caching headers cho assets
5. [ ] Test toàn bộ trên production:
   - Mọi trang load đúng
   - Mọi link hoạt động
   - Mobile responsive
   - Newsletter form hoạt động
   - SEO check (title, meta, og:image)

## Files to Create/Modify
- `scripts/deploy.sh` — [NEW] Deployment script
- `config.toml` — [MODIFY] Verify baseURL = "https://blog.xuyenlab.com/"
- Server config (nginx/caddy) — Tùy server setup

## Test Criteria
- [ ] Truy cập blog.xuyenlab.com → blog hiện đúng
- [ ] HTTPS hoạt động (khóa xanh)
- [ ] Tất cả bài viết hiện đúng
- [ ] CTA links hoạt động
- [ ] Newsletter form hoạt động trên production
- [ ] Mobile responsive trên production
- [ ] Google PageSpeed score > 90

## Notes
- Home server đã có sẵn — kiểm tra Cloudflare Tunnel nếu đã dùng trước đó
- Hugo build rất nhanh vì static site
- Dùng Claude Sonnet 4.5 (Thinking) cho server config

---
🎉 **DONE — Blog đã live!**
