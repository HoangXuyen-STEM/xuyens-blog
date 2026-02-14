# PHASE 7: DEPLOY LÊN HOME SERVER
## Prompt cho Antigravity

> Phase cuối cùng. Blog đã có 8 bài, design đúng, newsletter hoạt động.
> Giờ deploy lên home server để blog.xuyenlab.com live.

---

## CONTEXT

- Blog Hugo đã hoàn chỉnh trên localhost (Phase 1-6 done)
- Home server: Ubuntu, đã có Docker + Cloudflare Tunnel
- Domain: blog.xuyenlab.com (qua Cloudflare)
- Build: `hugo build` → 90 pages, 0 errors

---

## TASK 7.1: BUILD PRODUCTION

### Việc cần làm:

1. Cập nhật `config.toml`:
```toml
baseURL = "https://blog.xuyenlab.com"
```

2. Build production:
```bash
hugo --minify
```
Output sẽ nằm trong thư mục `public/`.

3. Verify build:
```bash
# Kiểm tra số file
find public/ -name "*.html" | wc -l

# Kiểm tra không có lỗi
# Mở public/index.html xem có nội dung đúng
```

### Kiểm tra Task 7.1:
- [ ] `baseURL` đã đổi sang https://blog.xuyenlab.com
- [ ] `hugo --minify` → 0 errors
- [ ] Thư mục `public/` có đầy đủ HTML, CSS, JS, images

---

## TASK 7.2: DEPLOY LÊN HOME SERVER

### Cách 1: Docker + Nginx (Khuyến nghị)

Tạo `Dockerfile`:
```dockerfile
FROM nginx:alpine
COPY public/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

Tạo `nginx.conf`:
```nginx
server {
    listen 80;
    server_name blog.xuyenlab.com;
    root /usr/share/nginx/html;
    index index.html;

    # Gzip compression
    gzip on;
    gzip_types text/css application/javascript text/html application/json;
    gzip_min_length 1000;

    # Cache static assets
    location ~* \.(css|js|jpg|jpeg|png|gif|svg|ico|woff|woff2)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Hugo clean URLs
    location / {
        try_files $uri $uri/ $uri.html =404;
    }

    # Custom 404
    error_page 404 /404.html;
}
```

Tạo `docker-compose.yml`:
```yaml
version: '3'
services:
  blog:
    build: .
    container_name: xuyens-blog
    restart: unless-stopped
    ports:
      - "8090:80"
    volumes:
      - ./public:/usr/share/nginx/html:ro
```

Deploy:
```bash
# Build và chạy
docker-compose up -d --build

# Kiểm tra
curl http://localhost:8090
```

### Cách 2: Copy trực tiếp (Đơn giản hơn)

Nếu server đã có Nginx/Caddy:
```bash
# Copy public/ lên server
rsync -avz public/ user@server:/var/www/blog.xuyenlab.com/

# Hoặc nếu làm trên server luôn
cp -r public/* /var/www/blog.xuyenlab.com/
```

### Kiểm tra Task 7.2:
- [ ] Container/service chạy không lỗi
- [ ] `curl http://localhost:8090` → trả về HTML trang chủ
- [ ] Logs không có error

---

## TASK 7.3: CẤU HÌNH CLOUDFLARE TUNNEL

Nếu Xuyen đã có Cloudflare Tunnel cho các service khác:

```bash
# Thêm route cho blog vào config tunnel
# File: ~/.cloudflared/config.yml

ingress:
  - hostname: blog.xuyenlab.com
    service: http://localhost:8090
  # ... các service khác
  - service: http_status:404

# Restart tunnel
sudo systemctl restart cloudflared
```

Nếu chưa có tunnel → Xuyen sẽ tự cấu hình (đã có kinh nghiệm).

### Kiểm tra Task 7.3:
- [ ] Truy cập https://blog.xuyenlab.com → blog hiển thị
- [ ] HTTPS hoạt động (Cloudflare tự cấp cert)
- [ ] Tất cả trang load đúng (homepage, posts, about, categories)

---

## TASK 7.4: TEST PRODUCTION

Checklist test toàn diện:

### Trang chủ
- [ ] 8 bài viết hiện đầy đủ
- [ ] Thumbnail hiện đúng (hoặc default)
- [ ] Category tag đúng
- [ ] Lenny episode tag đúng
- [ ] Click bài → đến trang bài viết

### Trang bài viết
- [ ] Nội dung đầy đủ, format đẹp
- [ ] CTA cuối bài hiện đúng
- [ ] Related posts hoạt động
- [ ] Newsletter form hiện

### Trang phụ
- [ ] About Me → nội dung đúng
- [ ] Navigation → tất cả link hoạt động
- [ ] Category pages → filter đúng
- [ ] Footer → social links đúng

### Newsletter
- [ ] Nhập email → "Cảm ơn bạn"
- [ ] Nhập trùng → "Đã đăng ký rồi"

### Mobile
- [ ] Mở trên điện thoại → responsive tốt
- [ ] Newsletter form → input + button xếp dọc

### Performance
- [ ] Trang load < 3 giây
- [ ] Không có lỗi console (F12)
- [ ] Không có broken links

**Pass hết → 🎉 BLOG LIVE!**

---

## SCRIPT CẬP NHẬT BÀI MỚI (dùng sau này)

Khi Xuyen viết bài mới, quy trình:
```bash
# 1. Thêm file .md vào content/posts/
# 2. Thêm thumbnail vào static/images/
# 3. Build lại
hugo --minify

# 4. Deploy lại (nếu dùng Docker)
docker-compose up -d --build

# Hoặc (nếu dùng rsync)
rsync -avz public/ user@server:/var/www/blog.xuyenlab.com/
```

Có thể tạo script `deploy.sh` cho nhanh:
```bash
#!/bin/bash
echo "🔨 Building blog..."
hugo --minify
echo "🚀 Deploying..."
docker-compose up -d --build
echo "✅ Done! Check https://blog.xuyenlab.com"
```

---

*Phase 7 Prompt v1.0 — Dùng với model: Claude Sonnet 4.5 (Thinking)*
