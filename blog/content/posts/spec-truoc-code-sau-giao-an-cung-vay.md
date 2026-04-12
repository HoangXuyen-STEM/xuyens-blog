---
title: "Spec Trước, Code Sau — Giáo Án Cũng Vậy"
slug: "spec-truoc-code-sau-giao-an-cung-vay"
summary: "Hồi mới đi dạy, mình không soạn giáo án. 45 phút loạn. Thầy hiệu phó nhìn vào — không nói gì. 25 năm sau, mình hiểu: giáo án là spec."
categories: ["framework"]
tags: ["spec", "vibe-coding", "giáo án", "FIDS", "Simon Willison"]
thumbnail: "/images/spec-truoc-code-sau-giao-an-cung-vay.png"
lenny_episode: "Simon Willison — Agentic Engineering Patterns"
cta_type: "course"
date: "2026-04-11"
status: "published"
---

Hồi mới đi dạy, mình không soạn giáo án. Nghĩ trong đầu là dạy được. Giỏi mà, Hóa học là sở trường mà — cần gì giáo án.

Kết quả: 45 phút loạn. Mình nói một đằng, viết bảng một nẻo. Học sinh ngơ ngác. Mình mồ hôi đầm đìa. Thầy hiệu phó đi ngang nhìn vào — không nói gì.

Cái nhìn đó đáng giá hơn mọi lời khiển trách. Mình nhớ đến giờ.

## 25 năm sau, mình gọi giáo án bằng tên khác: spec

Spec — specification — là bản mô tả chi tiết trước khi bắt tay làm. Trong coding, spec là tài liệu ghi rõ: sản phẩm sẽ làm gì, cho ai, kết quả ra sao.

Giáo án cũng y chang.

Ai dạy? Dạy cho ai? Sau 45 phút, học sinh phải biết cái gì? Bằng cách nào? Nếu tụi nó không hiểu thì làm sao? Đó là spec.

Không có spec, giờ dạy loạn. Không có spec, code cũng loạn. Mình đã chứng minh cả hai bằng kinh nghiệm bản thân.

## Simon Willison và bước ngoặt AI coding

Mình nghe tập Lenny's Podcast phỏng vấn Simon Willison — một trong những người viết nhiều nhất về AI coding. Ông nói tháng 11/2025 là bước ngoặt — AI coding đã đủ giỏi để thay đổi cách mọi người viết phần mềm.

Nhưng — và đây là phần hay — ông không nói AI thay thế developer. Ông nói AI cần PATTERN. Cần cấu trúc. Cần spec.

3 pattern agentic engineering ông đề xuất:

**Red/Green TDD** — viết test trước, code sau. Giống viết đề thi trước, rồi soạn bài dạy sao cho học sinh làm được đề đó. Không phải dạy xong mới nghĩ đề.

**Templates** — không bắt đầu từ zero. Dùng khuôn mẫu có sẵn. Giống giáo viên kinh nghiệm có "giáo án khung" — mỗi bài chỉ cần điều chỉnh, không viết lại từ đầu.

**Hoarding** — tích lũy patterns. Mỗi lần dạy xong, ghi lại cái gì hiệu quả, cái gì thất bại. Lần sau dùng lại. Giống developer lưu lại code snippets hay dùng.

Cả 3 pattern có một điểm chung: SPEC RÕ RÀNG trước khi bắt tay làm.

## FIDS — spec cho giáo viên

Mình dùng framework FIDS khi soạn giáo án:

**Feel** — Hiểu vấn đề. Học sinh đang ở đâu? Tụi nó biết gì rồi? Tụi nó sợ gì?

**Imagine** — Hình dung giải pháp. Sau 45 phút, mình muốn tụi nó đạt được gì? Bằng cách nào?

**Do** — Thử làm. Dạy thử. Cho bài tập. Xem phản ứng.

**Share** — Chia sẻ. Tụi nó trình bày lại. Mình nghe. Sửa. Ghi nhận.

Vibe-coding cũng y chang. Mình viết spec (prompt chi tiết) → AI sinh code → mình test → sửa lại spec → AI code lại.

Giáo án theo FIDS. Vibe-coding theo spec. Cùng một tư duy: biết mình muốn gì TRƯỚC khi bắt đầu.

## Mình từng nghĩ giỏi là không cần chuẩn bị

25 năm trước mình nghĩ vậy. Giỏi là lên lớp dạy không cần nhìn giáo án. Giỏi là xuất khẩu thành bài.

Sai. Hoàn toàn sai.

Giỏi là chuẩn bị kỹ đến mức lên lớp trông nhẹ nhàng. Giống nhạc sĩ jazz — nghe tưởng ngẫu hứng, nhưng đằng sau là hàng ngàn giờ luyện. Cái "tự nhiên" đó đến từ spec trong đầu rõ ràng đến mức không cần nhìn giấy.

Simon Willison nói: *"AI giỏi hơn rồi nhưng không có spec thì nó vẫn code bậy."* Mình thêm: "Giáo viên giỏi mấy mà không có spec thì cũng dạy bậy."

## Bắt đầu bằng câu hỏi

Dù bạn đang soạn giáo án, viết prompt, hay lên kế hoạch kinh doanh — bắt đầu bằng một câu hỏi:

*"Mình muốn kết quả cuối cùng là gì?"*

Đó là spec. Không cần phức tạp. Không cần 10 trang. Chỉ cần một câu trả lời rõ ràng cho câu hỏi đó — rồi mọi thứ khác sẽ theo sau.

---

💡 **Lấy cảm hứng từ:** Simon Willison — Agentic Engineering Patterns, Lenny's Podcast

Buổi đầu tiên trong khóa AI của mình, mình không dạy prompt. Mình dạy cách viết spec — không phải spec kỹ thuật, mà spec cho CÁCH BẠN NGHĨ. Vì nếu bạn không biết mình muốn gì, thì prompt hay mấy cũng vô nghĩa.
