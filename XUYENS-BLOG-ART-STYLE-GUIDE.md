# ART STYLE GUIDE — XUYEN'S BLOG
## blog.xuyenlab.com

> File này là "Source of Truth" cho toàn bộ hình ảnh trên blog.
> Dùng kèm prompt template khi tạo ảnh bằng Nano Banana.

---

## 1. STYLE: WATERCOLOR ILLUSTRATION

### Mô tả tổng quát
Minimalist watercolor illustration kết hợp ink linework với soft watercolor washes.
Gợi cảm giác: contemplative, warm, professional nhưng gần gũi.
Giống phong cách ảnh avatar của tác giả.

### Đặc trưng kỹ thuật
- **Linework:** Ink pen hoặc fine liner, loose và sketchy, không quá chi tiết
- **Màu nước:** Soft washes, edges tan dần vào nền (không viền cứng)
- **Nền:** Off-white (giấy watercolor texture), KHÔNG nền trắng tinh
- **Splashes:** Soft watercolor splashes/blooms ở rìa hoặc phía sau chủ thể
- **White space:** Nhiều khoảng trống, thoáng, không chật
- **Paper texture:** Visible — giống giấy vẽ thật

### KHÔNG BAO GIỜ
- ❌ Ảnh chụp thật hoặc photorealistic
- ❌ Vector/flat illustration
- ❌ Nền màu đặc hoặc gradient digital
- ❌ Quá nhiều chi tiết hoặc quá sặc sỡ
- ❌ Chuyển ảnh cũ sang style mới (luôn tạo MỚI)

---

## 2. BẢNG MÀU (COLOR PALETTE)

Rút từ ảnh avatar tác giả — dùng cho cả ảnh thumbnail VÀ CSS blog.

### Màu chính
| Tên | Hex | Dùng cho |
|-----|-----|---------|
| **Navy Blue** | `#2C3E6B` | Điểm nhấn chính, heading, accent |
| **Warm Cream** | `#E8DDD0` | Nền giấy, background blog |
| **Light Blue Wash** | `#A8C4D4` | Splash nền, hover states |
| **Warm Brown** | `#8B7355` | Accent phụ, links, CTA |
| **White** | `#FAFAF7` | Nền card, text area |

### Màu phụ (dùng ít)
| Tên | Hex | Dùng cho |
|-----|-----|---------|
| **Soft Peach** | `#E8C9B0` | Warm splash accent |
| **Dark Gray** | `#333333` | Body text |
| **Medium Gray** | `#888888` | Meta text (date, tags) |

### Quy tắc phối màu trong ảnh
- Mỗi ảnh dùng tối đa **3-4 màu** từ palette
- Navy Blue luôn là điểm nhấn chính
- Warm Cream/White làm nền
- Light Blue Wash + Soft Peach làm splash phụ
- KHÔNG dùng màu ngoài palette (giữ consistency)

---

## 3. THUMBNAIL SPECIFICATIONS

### Format
- **Tỉ lệ:** 1:1 (vuông)
- **Kích thước:** 1024x1024px (Nano Banana output)
- **Resize cho blog:** 600x600px (web) + 300x300px (mobile)

### Chủ thể — Mix tùy bài viết
| Loại | Khi nào dùng | Ví dụ |
|------|-------------|-------|
| **Nhân vật** | Bài về con người, career, mindset | Người ngồi cafe suy tư, người đi làm nhìn ra cửa sổ |
| **Vật thể/Biểu tượng** | Bài về công cụ, framework | Ly cà phê + laptop, cuốn sách mở, bàn cờ |
| **Cảnh quan** | Bài về tầm nhìn, thay đổi lớn | Con đường rẽ nhánh, ngọn hải đăng, cầu nối |
| **Trừu tượng** | Bài về AI, công nghệ | Mạng lưới kết nối, gears + bàn tay |

### Composition
- Chủ thể ở trung tâm hoặc lệch 1/3
- Watercolor splash từ chủ thể lan ra rìa
- Rìa ảnh tan dần vào nền cream
- Không text trên ảnh thumbnail

---

## 4. PROMPT TEMPLATE CHO NANO BANANA

### Base prompt (dùng cho MỌI ảnh)
```
A minimalist watercolor illustration on off-white textured paper. 
Loose ink linework with soft watercolor washes. 
Color palette: navy blue (#2C3E6B), warm cream, light blue washes, warm brown accents. 
Edges dissolve softly into the paper background. 
Visible paper texture and subtle paint blooms. 
Plenty of white space. Square format 1:1.
[CHỦ THỂ CỤ THỂ Ở ĐÂY]
```

### Ví dụ prompt theo loại bài:

**Bài "AI Không Cướp Việc, Nó Cướp Cách Làm Việc"** (category: AI & Công nghệ)
```
A minimalist watercolor illustration on off-white textured paper. 
Loose ink linework with soft watercolor washes. 
Color palette: navy blue, warm cream, light blue washes, warm brown accents. 
Edges dissolve softly into the paper background. 
Visible paper texture and subtle paint blooms. Plenty of white space. Square format 1:1.
Subject: A person sitting at a desk, looking thoughtfully at a glowing laptop screen. 
A subtle, friendly robot silhouette sits beside them like a colleague. 
Warm and contemplative mood, not threatening.
```

**Bài "Tư Duy Product Thinking Cho Người Đi Làm"** (category: Mindset)
```
...same base prompt...
Subject: A hand-drawn lightbulb with watercolor glow, surrounded by small sketches 
of everyday objects — a coffee cup, a notebook, a phone. 
Suggesting ideas emerging from daily life.
```

**Bài "Framework Giải Ngược"** (category: Framework & Chiến lược)
```
...same base prompt...
Subject: A winding path viewed from above, starting from a clear destination point 
and tracing backwards through soft watercolor landscape. 
A compass or lighthouse at the destination. Working backwards concept.
```

**Bài "Career Pivot ở Tuổi 35"** (category: Career)
```
...same base prompt...
Subject: A person standing at a crossroads — two paths diverging in a 
watercolor forest. One path is well-worn, the other is fresh and bright. 
The person looks curious, not afraid. Hopeful mood.
```

---

## 5. ÁP DỤNG CHO BLOG CSS

### Typography (đề xuất)
- **Heading:** Be Vietnam Pro (Bold) — clean, Vietnamese-friendly
- **Body:** Be Vietnam Pro (Regular) — dễ đọc
- **Fallback:** system-ui, sans-serif

### CSS Color Variables
```css
:root {
  --color-navy: #2C3E6B;
  --color-cream: #E8DDD0;
  --color-blue-wash: #A8C4D4;
  --color-brown: #8B7355;
  --color-white: #FAFAF7;
  --color-peach: #E8C9B0;
  --color-text: #333333;
  --color-meta: #888888;
  --color-bg: #F5F0EB;
}

body {
  background-color: var(--color-bg);
  color: var(--color-text);
  font-family: 'Be Vietnam Pro', system-ui, sans-serif;
}

a { color: var(--color-navy); }
a:hover { color: var(--color-brown); }

.post-card {
  background: var(--color-white);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.category-tag {
  color: var(--color-navy);
  background: rgba(44, 62, 107, 0.08);
}

.cta-banner {
  background: var(--color-cream);
  border-left: 4px solid var(--color-brown);
}
```

---

## 6. QUY TRÌNH TẠO ẢNH CHO BÀI VIẾT MỚI

```
1. Đọc bài viết → Xác định concept/mood
2. Chọn loại chủ thể (nhân vật / vật thể / cảnh quan / trừu tượng)
3. Ghép vào base prompt + mô tả chủ thể cụ thể
4. Tạo ảnh bằng Nano Banana
5. Review: đúng palette? đúng style? đủ white space?
6. Resize → đặt vào static/images/
7. Cập nhật frontmatter: thumbnail: "/images/ten-file.jpg"
```

---

*Art Style Guide v1.0 — 2026-02-13*
*Dùng cùng PRD + Tone Guide trong workspace xuyens-blog/*
