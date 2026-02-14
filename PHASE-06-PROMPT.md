# PHASE 6: CONTENT PIPELINE
## Prompt cho Antigravity

> ⚠️ ĐỌC KỸ TRƯỚC KHI LÀM. Phase này tạo 5-10 bài viết launch cho blog.
> CẦN ĐỌC: XUYENS-BLOG-TONE-GUIDE.md + XUYENS-BLOG-ART-STYLE-GUIDE.md

---

## CONTEXT

- Phase 1-5 đã hoàn thành. Blog Hugo chạy được, đúng bảng màu, có newsletter.
- Phase 6 tạo nội dung thật cho blog: bài viết + thumbnail.
- Nguồn transcript: https://github.com/ChatPRD/lennys-podcast-transcripts
- Cấu trúc repo: `episodes/{guest-name}/transcript.md` (284 episodes, có YAML frontmatter)

---

## TASK 6.1: LẤY TRANSCRIPT

### Việc cần làm:
Clone repo transcript vào workspace riêng:
```bash
git clone https://github.com/ChatPRD/lennys-podcast-transcripts.git lenny-transcripts
```

### Chọn 8 episodes cho 8 bài viết launch (2 mỗi category):

| # | Category | Tìm trong episodes/ | Gợi ý guest/topic |
|---|----------|---------------------|-------------------|
| 1 | ai-technology | AI, automation, tools | Tìm episode về AI tools, AI workflow |
| 2 | ai-technology | AI, future of work | Tìm episode về AI thay đổi cách làm việc |
| 3 | mindset | growth, mindset, learning | Tìm episode về growth mindset, personal development |
| 4 | mindset | resilience, failure | Tìm episode về học từ thất bại |
| 5 | framework | strategy, product, OKR | Tìm episode về product strategy, framework |
| 6 | framework | decision making | Tìm episode về ra quyết định, prioritization |
| 7 | career | career growth, leadership | Tìm episode về career development |
| 8 | career | career pivot, change | Tìm episode về thay đổi sự nghiệp |

### Cách tìm episode phù hợp:
```bash
# Liệt kê tất cả episodes
ls lenny-transcripts/episodes/

# Tìm episode theo keyword trong title
grep -r "AI" lenny-transcripts/episodes/*/transcript.md --include="*.md" -l | head -20
grep -r "strategy" lenny-transcripts/episodes/*/transcript.md --include="*.md" -l | head -20
grep -r "career" lenny-transcripts/episodes/*/transcript.md --include="*.md" -l | head -20
```

### Kiểm tra Task 6.1:
- [ ] Repo đã clone thành công
- [ ] Đã chọn được 8 episodes (2 mỗi category)
- [ ] Liệt kê 8 episodes đã chọn: tên guest + title + category dự kiến

---

## TASK 6.2: VIẾT BÀI — CONTENT PIPELINE

### Quy trình cho MỖI bài viết:

```
Đọc transcript → Trích 3-5 insight chính
  → Chọn 1-2 insight hay nhất
  → Viết bài theo Tone Guide
  → Format đúng frontmatter
  → Lưu vào content/posts/
```

### ĐỌC TONE GUIDE TRƯỚC KHI VIẾT (XUYENS-BLOG-TONE-GUIDE.md)

Tóm tắt các quy tắc QUAN TRỌNG NHẤT:

1. **MỞ BÀI = Câu chuyện thật**, KHÔNG MỞ bằng định nghĩa/lý thuyết
2. **Cấu trúc "Tưởng A, hóa ra B"** — tạo twist bất ngờ
3. **Tự trào** — thừa nhận sai lầm, kể fail story
4. **Hài hước nhẹ** — so sánh bất ngờ, ẩn dụ đời thường (2-3 chỗ/bài)
5. **Kết bài trao quyền** — "Bạn cũng làm được"
6. **Xưng hô:** "mình" — "bạn"
7. **Ngôn ngữ:** Tiếng Việt chính, thuật ngữ Anh giữ nguyên khi phổ biến

### PROMPT TEMPLATE — Dùng cho mỗi bài viết:

```
Bạn là Xuyen — giáo viên 25+ năm kinh nghiệm, đang viết blog cho người đi làm Việt Nam 27-45 tuổi.

GIỌNG VĂN:
- "Thầy mà như bạn" — kể chuyện ngang hàng, không lên lớp
- 70% tự trào/kể chuyện cá nhân + 20% hài hước nhẹ + 10% insight sắc bén
- Mở bài bằng câu chuyện thật hoặc tình huống cụ thể
- Có twist "Tưởng A, hóa ra B" 
- Hài hước từ sự thật, không ép vui (so sánh bất ngờ, ẩn dụ đời thường)
- Kết bài trao quyền: câu hỏi gợi mở + khuyến khích hành động
- Xưng hô: "mình" — "bạn"
- Tiếng Việt là chính, thuật ngữ Anh giữ nguyên

CẤU TRÚC BÀI:
1. [MỞ BÀI] Câu chuyện thật / tình huống — hook người đọc (2-3 đoạn)
2. [THÂN BÀI] 3-5 phần — Insight từ Lenny + quan điểm cá nhân "mình" + ẩn dụ + hài (1-2 chỗ)
3. [KẾT BÀI] Tóm tắt ngắn + câu hỏi gợi mở + "Bạn cũng làm được" (1-2 đoạn)

TRANSCRIPT LENNY'S PODCAST:
[DÁN TRANSCRIPT Ở ĐÂY]

YÊU CẦU:
- Trích 2-3 insight hay nhất từ transcript
- Kết hợp quan điểm cá nhân của "mình" (Xuyen — giáo viên dạy hóa, làm AI educator, chủ Eakar Coffee)
- Viết 800-1200 từ
- KHÔNG viết giống sách giáo khoa
- KHÔNG liệt kê bullet points dài dòng
- Test: đọc to lên phải nghe tự nhiên như đang nói chuyện

OUTPUT FORMAT (Hugo Markdown):
---
title: "[Tiêu đề hấp dẫn tiếng Việt]"
slug: "[url-slug-khong-dau]"
summary: "[1-2 câu tóm tắt]"
category: "[ai-technology|mindset|framework|career]"
tags: ["tag1", "tag2", "tag3"]
thumbnail: "/images/[ten-file].jpg"
lenny_episode: "[Tên guest]"
cta_type: "[coffee|course]"
published_date: "[YYYY-MM-DD]"
status: "published"
---

[Nội dung bài viết]
```

### VÍ DỤ OUTPUT ĐÚNG TONE:

```markdown
---
title: "AI Không Cướp Việc, Nó Cướp Cách Làm Việc"
slug: "ai-khong-cuop-viec"
summary: "Tại sao domain expert cần học cách làm bạn với AI — trước khi AI làm bạn với người khác"
category: "ai-technology"
tags: ["ai-tools", "productivity", "career"]
thumbnail: "/images/ai-khong-cuop-viec.jpg"
lenny_episode: "Ami Vora"
cta_type: "coffee"
published_date: "2026-02-15"
status: "published"
---

Năm ngoái, mình hỏi một anh bạn kế toán 15 năm kinh nghiệm: "Anh có lo AI thay thế không?"

Anh ấy cười: "Lo gì, Excel mình còn chưa giỏi."

Mình cũng cười. Rồi im lặng.

Vì thật ra, câu trả lời đó mới đáng lo hơn cả AI...

[tiếp tục bài viết]
```

### QUY TẮC ĐẶT TÊN FILE:
```
content/posts/ai-khong-cuop-viec.md
content/posts/tu-duy-product-thinking.md
content/posts/framework-giai-nguoc.md
```
Slug = tên file (không dấu, gạch nối).

---

## TASK 6.3: TẠO THUMBNAIL PROMPT

Cho mỗi bài viết, tạo 1 prompt cho Nano Banana theo Art Style Guide.

### Base prompt (COPY CHÍNH XÁC cho mọi ảnh):
```
A minimalist watercolor illustration on off-white textured paper. 
Loose ink linework with soft watercolor washes. 
Color palette: navy blue (#2C3E6B), warm cream, light blue washes, warm brown accents. 
Edges dissolve softly into the paper background. 
Visible paper texture and subtle paint blooms. 
Plenty of white space. Square format 1:1.
```

### Thêm chủ thể cụ thể cho mỗi bài:

| Bài | Chủ thể gợi ý |
|-----|---------------|
| AI & Công nghệ #1 | Subject: A person at a desk looking at a glowing laptop, with a friendly robot silhouette sitting beside them. Warm, collaborative mood. |
| AI & Công nghệ #2 | Subject: Two hands — one human, one robotic — reaching toward each other, with soft watercolor light between them. |
| Mindset #1 | Subject: A person climbing a mountain path, pausing to look at the view. Contemplative, not exhausted. Growth journey. |
| Mindset #2 | Subject: A broken pot repaired with gold lines (kintsugi style). Beauty in imperfection. |
| Framework #1 | Subject: A compass resting on an open notebook with sketched diagrams. Navigation and strategy feeling. |
| Framework #2 | Subject: A chess board mid-game, viewed from above, with watercolor pieces. Strategic thinking. |
| Career #1 | Subject: A person at a crossroads — two paths in a watercolor forest. Curious, not afraid. |
| Career #2 | Subject: Seeds being planted in soil, with small green sprouts emerging. New beginnings, growth. |

### Output:
Tạo file `THUMBNAIL-PROMPTS.md` chứa 8 prompts đầy đủ (base + subject).
Xuyen sẽ dùng file này để tạo ảnh bằng Nano Banana riêng.

---

## TASK 6.4: REVIEW CHẤT LƯỢNG

Sau khi viết xong 8 bài, tự review theo checklist Tone Guide:

### Checklist cho MỖI bài:
- [ ] Mở bài bằng câu chuyện thật / tình huống cụ thể? (KHÔNG lý thuyết)
- [ ] Có twist "Tưởng A, hóa ra B"?
- [ ] Có tự trào / thừa nhận sai lầm?
- [ ] Có 1-2 chỗ hài hước tự nhiên? (không gượng)
- [ ] Kết bài trao quyền? (câu hỏi hoặc checklist hành động)
- [ ] Đọc to nghe tự nhiên?
- [ ] Xưng hô "mình" — "bạn" nhất quán?
- [ ] 800-1200 từ?
- [ ] Frontmatter đầy đủ các trường?
- [ ] Slug = tên file?

### Nếu bài nào FAIL checklist:
→ Viết lại phần fail, KHÔNG viết lại toàn bộ bài.

---

## TASK 6.5: BUILD VÀ VERIFY

```bash
# Build blog với bài mới
hugo server

# Kiểm tra
# - 8 bài mới hiện trên trang chủ
# - Mỗi bài click vào đọc được
# - Category đúng
# - Lenny episode tag hiện đúng
# - CTA cuối bài đúng type
# - Related posts hoạt động
# - Không có lỗi build
```

### Kiểm tra tổng:
- [ ] 8 bài hiện trên trang chủ (mới nhất lên đầu)
- [ ] Mỗi bài: title, summary, category tag, lenny tag đúng
- [ ] Click → nội dung đầy đủ, CTA đúng
- [ ] Related posts cùng category hiện đúng
- [ ] `hugo build` → 0 errors
- [ ] File THUMBNAIL-PROMPTS.md đã tạo

**Pass hết → báo lại → chuyển Phase 7 (Deploy).**

---

## TÓM TẮT 5 TASKS

| Task | Việc | Output |
|------|------|--------|
| 6.1 | Clone repo, chọn 8 episodes | Danh sách 8 episodes |
| 6.2 | Viết 8 bài đúng Tone Guide | 8 file .md trong content/posts/ |
| 6.3 | Tạo thumbnail prompts | THUMBNAIL-PROMPTS.md |
| 6.4 | Review checklist | 8/8 bài pass |
| 6.5 | Build & verify | Blog hiện 8 bài, 0 errors |

---

*Phase 6 Prompt v1.0 — Dùng với model: Claude Opus 4.6 (Thinking)*
*Đây là phase cần xử lý ngôn ngữ Việt → PHẢI dùng Claude, KHÔNG dùng Gemini.*
