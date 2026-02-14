# Phase 06: Content Pipeline
Status: ⬜ Pending
Dependencies: Phase 05

## Objective
Tạo pipeline AI biến Lenny's Podcast transcript → bài viết tiếng Việt đúng format, đúng tone. Batch tạo 5-10 bài launch.

## Requirements
### Functional
- [ ] Script/prompt nhận transcript (.txt) → xuất file `.md` đúng frontmatter format
- [ ] Output có: title Việt hóa hấp dẫn, summary, category, tags, nội dung bài
- [ ] Kết hợp "quan điểm Xuyen" (my_opinion section)
- [ ] 5-10 bài viết sẵn sàng cho launch

### Non-Functional
- [ ] Tone: thought-leader nhẹ nhàng, thân thiện, hài hước nhẹ
- [ ] Không "AI味" — đọc tự nhiên như người Việt viết
- [ ] Mỗi bài 800-1500 từ
- [ ] Headings, bullet points, quotes — dễ scan

## Implementation Steps
1. [ ] Tạo prompt template cho AI:
   - Input: transcript text + episode number
   - Output: file `.md` đúng frontmatter format
   - Rules: tone, length, structure, Việt hóa
2. [ ] Tạo script `scripts/create-post.sh`:
   - Nhận tham số: transcript file, episode number, category
   - Gọi AI (hoặc manual flow) → tạo `.md` file
   - Đặt vào `content/posts/` với slug từ title
3. [ ] Batch tạo 5-10 bài đầu tiên:
   - Đa dạng 4 categories
   - Mỗi category ít nhất 1 bài
   - Có cả `cta_type: "coffee"` và `"course"`
4. [ ] Review + chỉnh sửa bài:
   - Xuyen review tone, accuracy
   - Sửa câu cú "AI味"
   - Thêm my_opinion sections

## Files to Create/Modify
- `scripts/create-post.sh` — [NEW] Post creation script
- `scripts/prompt-template.md` — [NEW] AI prompt template
- `content/posts/*.md` — [NEW] 5-10 bài viết launch
- `static/images/*.jpg` — [NEW] Thumbnails cho bài viết

## Test Criteria
- [ ] Mỗi bài `.md` có đủ frontmatter fields
- [ ] `hugo build` không lỗi với tất cả bài viết
- [ ] Trang chủ hiện đúng tất cả bài published
- [ ] Mỗi bài đọc tự nhiên, đúng tone
- [ ] CTA cuối bài đúng loại

## Notes
- Phase này cần Xuyen review nội dung — KHÔNG tự động publish
- Dùng Claude Opus 4.6 (Thinking) cho content pipeline vì xử lý tiếng Việt
- Thumbnail có thể dùng AI generate (Antigravity generate_image tool)

---
Next Phase: [phase-07-deploy.md](./phase-07-deploy.md)
