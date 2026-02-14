# XUYEN'S BLOG — PRD / SPEC v1.0
## blog.xuyenlab.com

> Document này là "Source of Truth" (Nguồn sự thật duy nhất) cho toàn bộ dự án.
> Mang file này vào Antigravity khi bắt đầu code.

---

## 1. TỔNG QUAN DỰ ÁN

### 1.1 User (Người đọc)
- Người lao động Việt Nam, 27-45 tuổi
- Có chuyên môn sâu (domain expert) NHƯNG low-code
- Giỏi nghề nhưng chưa biết tận dụng công nghệ/AI

### 1.2 Problem (Vấn đề)
- Cảm thấy bị đe dọa bởi sự tiến bộ công nghệ
- Không phải mất việc ngay, mà "cách thức làm việc mỗi ngày" đang thay đổi và họ chưa bắt kịp

### 1.3 Solution (Giải pháp)
- Blog Việt hóa insight từ Lenny's Podcast
- Kết hợp quan điểm cá nhân của tác giả (Xuyen)
- Phong cách: thought-leader nhẹ nhàng, thân thiện, hài hước nhẹ
- Giúp người đọc có: tầm nhìn + framework + động lực hành động

### 1.4 Tone & Voice
- Giọng văn: "Thầy mà như bạn" — 70% tự trào/kể chuyện, 20% hài nhẹ, 10% insight
- Luôn mở bài bằng câu chuyện thật, cấu trúc "Tưởng A, hóa ra B"
- Tự trào về bản thân, kết bài trao quyền cho người đọc
- Xưng hô: "mình" — "bạn"
- Hài hước: nhẹ, tự nhiên, tối đa 2-3 chỗ/bài. KHÔNG mỉa mai, ép vui.
- 👉 **Chi tiết đầy đủ:** xem `XUYENS-BLOG-TONE-GUIDE.md`

---

## 2. SCOPE MVP v1

### LÀM ✅
- Blog tĩnh (static site) bằng Hugo
- Trang About Me / Giới thiệu tác giả
- CTA đến Eakar Coffee + Khóa học (banner/link cuối bài)
- Newsletter đăng ký email
- 5-10 bài viết launch
- Thiết kế tối giản kiểu tinystakeholders.com
- Responsive (mobile-friendly)

### KHÔNG LÀM ❌
- Hệ thống đăng nhập / membership
- Comment system
- Multi-language
- Search nâng cao
- Tự động publish pipeline (đợt sau)
- Analytics dashboard

---

## 3. TECH STACK

| Thành phần | Công nghệ |
|-----------|-----------|
| Static Site Generator | Hugo |
| Hosting | Home server (blog.xuyenlab.com) |
| Content format | Markdown + frontmatter |
| Style | CSS theo Design System (xem mục 3.1) |
| Newsletter | Form đơn giản (subscribers.json hoặc dịch vụ bên ngoài) |
| Build tool | Antigravity IDE |
| Cố vấn kiến trúc | Claude Opus 4.6 |

---

## 3.1 DESIGN SYSTEM

### Bảng màu (Color Palette)
Rút từ ảnh avatar watercolor của tác giả.

| Tên | Hex | Dùng cho |
|-----|-----|---------|
| **Navy Blue** | `#2C3E6B` | Heading, link, điểm nhấn chính |
| **Warm Cream** | `#E8DDD0` | Nền giấy, background sections |
| **Light Blue Wash** | `#A8C4D4` | Hover states, splash accent |
| **Warm Brown** | `#8B7355` | Link hover, CTA border, accent phụ |
| **Off White** | `#FAFAF7` | Nền card, text area |
| **Soft Peach** | `#E8C9B0` | Warm accent nhẹ |
| **Background** | `#F5F0EB` | Nền tổng thể body |
| **Body Text** | `#333333` | Văn bản chính |
| **Meta Text** | `#888888` | Date, tags, info phụ |

### CSS Variables
```css
:root {
  --color-navy: #2C3E6B;
  --color-cream: #E8DDD0;
  --color-blue-wash: #A8C4D4;
  --color-brown: #8B7355;
  --color-white: #FAFAF7;
  --color-peach: #E8C9B0;
  --color-bg: #F5F0EB;
  --color-text: #333333;
  --color-meta: #888888;
}
```

### Typography
- **Heading:** Be Vietnam Pro (Bold)
- **Body:** Be Vietnam Pro (Regular)
- **Fallback:** system-ui, sans-serif

### Art Style cho ảnh minh họa
- Phong cách: Minimalist watercolor (ink linework + soft washes)
- Thumbnail: 1:1 vuông, 1024x1024px
- Chủ thể: mix tùy bài (nhân vật / vật thể / cảnh quan / trừu tượng)
- Tạo ảnh MỚI bằng Nano Banana — KHÔNG chuyển ảnh cũ sang style mới
- 👉 **Chi tiết + Prompt template:** xem `XUYENS-BLOG-ART-STYLE-GUIDE.md`

---

### 4.1 Cấu trúc thư mục
```
blog/
├── content/
│   ├── posts/           ← Các file .md bài viết
│   └── about.md         ← Trang About Me
├── static/
│   ├── images/          ← Ảnh thumbnail
│   └── css/             ← Stylesheet
├── layouts/
│   └── templates/       ← Giao diện HTML (Hugo templates)
├── config.toml          ← Cấu hình Hugo
└── data/
    └── subscribers.json ← Danh sách email đăng ký
```

### 4.2 Bài viết (Post) — Frontmatter format
Mỗi bài viết là 1 file `.md` trong `content/posts/`:

```markdown
---
title: "AI Không Cướp Việc, Nó Cướp Cách Làm Việc"
slug: "ai-khong-cuop-viec"
summary: "Tại sao domain expert cần học cách làm bạn với AI"
category: "ai-technology"
tags: ["productivity", "ai-tools", "career"]
thumbnail: "/images/ai-cuop-viec.jpg"
lenny_episode: "EP.189"
cta_type: "coffee"
published_date: "2026-02-15"
status: "published"
---

Nội dung bài viết ở đây...
```

### 4.3 Categories (4 danh mục)
| Slug | Tên hiển thị |
|------|-------------|
| `ai-technology` | AI & Công nghệ |
| `mindset` | Mindset & Tư duy |
| `framework` | Framework & Chiến lược |
| `career` | Career & Sự nghiệp |

### 4.4 CTA Types
| cta_type | Hiển thị |
|----------|---------|
| `coffee` | Banner/link đến Eakar Coffee |
| `course` | Banner/link đến Khóa học AI/Vibe-coding |

### 4.5 Subscribers
```json
{
  "email": "user@example.com",
  "subscribed_date": "2026-02-15"
}
```

---

## 5. USER FLOWS

### Flow 1: Đọc blog
```
Vào blog.xuyenlab.com
  → Thấy danh sách bài (mới nhất lên đầu)
  → Mỗi bài hiện: thumbnail, title, summary, date, category
  → Click bài → Đọc nội dung đầy đủ
  → Cuối bài → Thấy CTA (Coffee hoặc Khóa học)
  → Thấy "Bài liên quan" (cùng category, 2-3 bài)
```

### Flow 2: Đăng ký Newsletter
```
Thấy form email (trang chủ hoặc cuối bài)
  → Nhập email → Bấm Subscribe
  → Hiện "Cảm ơn bạn đã đăng ký!"
```

### Flow 3: Content Pipeline (cho Antigravity)
```
Lenny's Transcript (.txt)
  → AI đọc + trích insight
  → Kết hợp quan điểm Xuyen (my_opinion)
  → Xuất ra file .md đúng format frontmatter
  → Đặt vào content/posts/
  → Hugo build → Blog hiển thị bài mới
```

---

## 6. EDGE CASES

| Tình huống | Xử lý |
|-----------|-------|
| Bài chưa có thumbnail | Hiện ảnh mặc định (default-thumbnail.jpg) |
| Email đăng ký trùng | Báo "Bạn đã đăng ký rồi" |
| Bài status = "draft" | Không hiện trên trang chủ |
| Không có bài liên quan cùng category | Hiện bài mới nhất thay thế |
| Trang trên mobile | Responsive — tự co giãn |
| frontmatter thiếu trường | Hugo báo lỗi khi build, không crash |

---

## 7. TASK BREAKDOWN (7 Phases)

### PHASE 1: Dựng khung blog (Skeleton)
- [ ] Task 1.1: Cài Hugo + tạo project mới
- [ ] Task 1.2: Tạo cấu trúc thư mục đúng Data Model
- [ ] Task 1.3: Tạo config.toml (tên blog, menu, CTA links)
- **Kiểm tra:** Chạy `hugo server` → thấy trang trắng trên localhost

### PHASE 2: Trang chủ (Homepage)
- [ ] Task 2.1: Tạo 1 bài viết mẫu .md đúng format frontmatter
- [ ] Task 2.2: Build trang chủ hiện danh sách bài (title, summary, date, category)
- [ ] Task 2.3: Style tối giản kiểu tinystakeholders.com
- **Kiểm tra:** Thấy bài mẫu hiện trên trang chủ, đọc dễ, sạch sẽ

### PHASE 3: Trang bài viết (Post page)
- [ ] Task 3.1: Click bài → hiện nội dung đầy đủ (markdown → HTML)
- [ ] Task 3.2: Hiện metadata (date, category, tags, Lenny episode)
- [ ] Task 3.3: CTA cuối bài (coffee hoặc course tùy cta_type)
- [ ] Task 3.4: Bài liên quan (cùng category, 2-3 bài)
- **Kiểm tra:** Đọc bài đầy đủ, CTA đúng link, bài liên quan hiện đúng

### PHASE 4: Các trang phụ
- [ ] Task 4.1: Trang About Me
- [ ] Task 4.2: Navigation menu (Home, About, Categories)
- [ ] Task 4.3: Footer (social links, copyright)
- **Kiểm tra:** Tất cả link hoạt động đúng

### PHASE 5: Newsletter + Polish + Design Update
- [ ] Task 5.1: **Update CSS theo Design System** (bảng màu, font Be Vietnam Pro, CSS variables)
- [ ] Task 5.2: Form đăng ký email (trang chủ + cuối bài)
- [ ] Task 5.3: Xử lý edge cases (email trùng, draft ẩn, ảnh mặc định)
- [ ] Task 5.4: Responsive mobile
- **Kiểm tra:** Blog đúng bảng màu mới, email lưu được, mobile tốt

### PHASE 6: Content Pipeline
- [ ] Task 6.1: Script AI biến transcript → bài viết .md đúng format
- [ ] Task 6.2: **Áp dụng Tone Guide** khi viết bài (xem `XUYENS-BLOG-TONE-GUIDE.md`)
- [ ] Task 6.3: **Tạo thumbnail** cho mỗi bài bằng Nano Banana (xem `XUYENS-BLOG-ART-STYLE-GUIDE.md`)
- [ ] Task 6.4: Batch tạo 5-10 bài viết đầu tiên
- [ ] Task 6.5: Review + chỉnh sửa nội dung (không "AI味")
- **Kiểm tra:** Bài viết đúng tone Xuyen, thumbnail đúng style, đúng format

### PHASE 7: Deploy lên server
- [ ] Task 7.1: Build Hugo → deploy lên home server
- [ ] Task 7.2: Cấu hình domain blog.xuyenlab.com
- [ ] Task 7.3: Test toàn bộ trên production
- **Kiểm tra:** Truy cập blog.xuyenlab.com → blog hoạt động hoàn chỉnh

---

## 8. PHÂN CÔNG VAI TRÒ

| Vai trò | Người/Tool | Nhiệm vụ |
|---------|-----------|----------|
| Khách hàng + PM | Xuyen | Ra yêu cầu, review, quyết định |
| Kiến trúc sư + BA | Claude Opus 4.6 | Thiết kế Spec, Data Model, tracking, sửa lỗi |
| Developer | Antigravity IDE | Code theo Spec, build blog, viết bài |

---

## 9. NGUYÊN TẮC LÀM VIỆC (SDD)

1. **Spec trước, Code sau** — Không code khi chưa có thiết kế
2. **Chia nhỏ** — Mỗi task ≤ 100 dòng code thay đổi
3. **Test từng phase** — Xong Phase 1 mới qua Phase 2
4. **Sửa Spec, không sửa code** — Nếu logic sai, quay lại sửa Spec rồi code lại
5. **Save brain** — Cuối mỗi phiên làm việc, lưu lại context

---

---

## 10. MODEL ALLOCATION (Antigravity)

| Phase | Model | Lý do |
|-------|-------|-------|
| `/plan` | Claude Opus 4.6 (Thinking) | Kiến trúc, thiết kế spec |
| Phase 1: Dựng khung | Claude Opus 4.6 (Thinking) | Setup đúng từ đầu |
| Phase 2: Trang chủ | Gemini 3 Pro (High) | Code frontend nhanh |
| Phase 3: Trang bài viết | Gemini 3 Pro (High) | Tiếp tục frontend |
| Phase 4: Trang phụ | Gemini 3 Flash | Việc đơn giản |
| Phase 5: Newsletter | Gemini 3 Pro (Low) | Form + responsive |
| Phase 6: Content Pipeline | Claude Opus 4.6 (Thinking) | Xử lý ngôn ngữ Việt |
| Phase 7: Deploy | Claude Sonnet 4.5 (Thinking) | Config server |
| `/debug` | Claude Opus 4.6 (Thinking) | Phân tích root cause |
| `/save-brain` | Gemini 3 Flash | Ghi nhớ nhanh |

### Nguyên tắc chọn model:
- 🏗️ Kiến trúc / Logic phức tạp → Claude Opus 4.6 (Thinking)
- 💻 Code frontend / Template → Gemini 3 Pro (High)
- ⚡ Việc đơn giản / Lặp lại → Gemini 3 Flash
- ✍️ Nội dung tiếng Việt → Claude Opus 4.6 (Thinking)

---

*Document version: 1.2 — Updated: 2026-02-13*
*Project: Xuyen's Blog (blog.xuyenlab.com)*
*Companion files: XUYENS-BLOG-TONE-GUIDE.md, XUYENS-BLOG-ART-STYLE-GUIDE.md*
