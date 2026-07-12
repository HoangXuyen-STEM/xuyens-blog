---
title: "Pre-Mortem: Tìm Thất Bại Trước Khi Nó Tìm Bạn"
slug: "pre-mortem-tim-that-bai-truoc"
summary: "Một PM từng làm ở Stripe, Google, Twitter chia sẻ cách tìm ra lỗi TRƯỚC khi launch — và tại sao không phải task nào cũng đáng làm tốt."
categories: ["framework"]
tags: ["pre-mortem", "prioritization", "lno-framework"]
thumbnail: "/images/default-thumbnail.jpg"
lenny_episode: "Shreyas Doshi — The Art of Product Management"
cta_type: "coffee"
date: "2026-02-13"
status: "published"
---
Mình sẽ thú nhận một chuyện.

Năm ngoái, mình tổ chức một buổi workshop cho giáo viên về AI trong giáo dục. Mình chuẩn bị slide đẹp. Nội dung chất. Demo live ấn tượng.

Nhưng mình quên một thứ: **wifi ở phòng hội trường không đủ mạnh cho 40 người kết nối cùng lúc.**

Kết quả: demo AI không chạy được. ChatGPT loading mãi. 40 giáo viên ngồi nhìn mình... và cái vòng xoay tròn trên màn hình.

Mình muốn chui xuống đất.

Buổi workshop vẫn ổn — mình nhanh trí chuyển sang dạy offline. Nhưng tối hôm đó, mình tự hỏi: *"Tại sao mình không nghĩ đến chuyện wifi trước?"*

Câu trả lời: vì mình chưa biết đến **Pre-Mortem.**

## Shreyas Doshi và 5 "Big Ideas"

Shreyas Doshi là một Product Manager huyền thoại — từng làm ở Yahoo, Google, Twitter, và Stripe. Trong Lenny's Podcast, anh chia sẻ 5 ý tưởng lớn về nghề PM. Nhưng 2 ý tưởng đầu tiên đã thay đổi cách mình làm việc.

### Big Idea #1: Pre-Mortem

Mọi người đều biết **post-mortem** — sau khi dự án fail, cả team ngồi lại phân tích: "Sao nó fail?"

Shreyas hỏi: **"Tại sao phải đợi đến khi fail?"**

Pre-mortem là *ngược lại.* Trước khi bắt đầu dự án, bạn tưởng tượng nó đã fail. Rồi hỏi: *"Nó fail vì lý do gì?"*

> **"Imagine this project has failed six months from now. Miserably failed. Now, let's work backwards and ask: what went wrong?"**

Cách làm cụ thể: bạn cho team ngồi lại và liệt kê 3 loại "mối đe dọa":

**🐯 Tiger (Hổ):** Mối đe dọa thật sự sẽ giết dự án. Ví dụ: "Server không chịu nổi traffic ngày launch."

**📄 Paper Tiger (Hổ giấy):** Thứ trông đáng sợ nhưng thật ra không nghiêm trọng. Ví dụ: "Đối thủ vừa ra feature tương tự" — có thể đáng sợ trên bề mặt nhưng thực tế không ảnh hưởng.

**🐘 Elephant (Voi):** Thứ ai cũng biết nhưng không ai nói. Elephant in the room. Ví dụ: "Mình giả định sẽ có người dùng, nhưng... mình có chắc không?"

Shreyas nói điều kỳ diệu nhất về pre-mortem không phải là tìm ra vấn đề. Đó là **tạo ra ngôn ngữ chung** để mọi người có thể nói về rủi ro mà không sợ bị coi là "tiêu cực."

Sau khi áp dụng ở Stripe, anh thấy mọi người bắt đầu nói trong các cuộc họp bình thường: *"Tôi có một tiger..."* — và ai cũng hiểu. Không ai bị coi là pessimistic. Đó chỉ là ngôn ngữ của team.

## Mình áp dụng Pre-Mortem thế nào?

Quay lại buổi workshop wifi. Nếu mình biết pre-mortem, mình sẽ tự hỏi trước 1 tuần:

*"Tưởng tượng buổi workshop đã fail. Tại sao?"*

- 🐯 Tiger: Wifi không đủ mạnh → **Chuẩn bị mobile hotspot backup**

- 🐯 Tiger: Demo AI trả lời sai → **Chuẩn bị video demo ghi sẵn**

- 📄 Paper Tiger: Giáo viên không hứng thú → Thật ra họ đã đăng ký, nên chắc OK

- 🐘 Elephant: Mình có đủ kiến thức AI để trả lời câu hỏi chuyên sâu không? → **Chuẩn bị danh sách "tôi không biết, nhưng sẽ tìm hiểu"**

5 phút suy nghĩ. Tiết kiệm 40 phút xấu hổ.

### Big Idea #2: LNO Framework — Không phải việc nào cũng đáng làm tốt

Đây là idea thay đổi cách mình *sử dụng thời gian.*

Shreyas kể: khi mới vào Google, anh làm việc 12-14 tiếng/ngày. Mệt. Stress. To-do list không bao giờ ngắn lại. Anh về nhà phàn nàn với vợ mỗi tối.

Rồi anh phát hiện ra: **tất cả task không giống nhau.** Có 3 loại:

**L (Leverage):** Task mà nỗ lực bạn bỏ ra cho 10X-100X kết quả. Ví dụ: viết chiến lược sản phẩm, quyết định hướng đi.

**N (Neutral):** Task cho kết quả tương đương nỗ lực. Bỏ 1 → được 1. Ví dụ: meeting cập nhật tiến độ, email thông thường.

**O (Overhead):** Task hành chính, bỏ nhiều nỗ lực nhưng không tạo thêm giá trị. Ví dụ: báo cáo chi tiêu, điền form.

Vấn đề: **anh đối xử với mọi task như nhau.** Viết email thông thường cũng kỹ như viết PRD chiến lược. Report chi tiêu cũng chỉn chu như proposal cho CEO.

Khi anh ngừng perfection ở N và O tasks, anh có thêm thời gian cho L tasks. Và impact tăng lên *đáng kể.*

> 💡 **Insight:** Bạn không cần làm TẤT CẢ mọi thứ tốt. Bạn cần biết TASK NÀO đáng làm tốt — và dồn năng lượng vào đó.

## Mình áp dụng LNO vào dạy học

Khi mình nhìn công việc qua lens LNO:

**L tasks (dồn năng lượng):**

- Thiết kế bài giảng mới cho chủ đề khó

- Viết feedback chi tiết cho học sinh có học lực yếu

- Chuẩn bị bài phát biểu trước phụ huynh

**N tasks (làm vừa đủ):**

- Chấm bài tập thông thường

- Email trao đổi với đồng nghiệp

- Meeting hàng tuần

**O tasks (làm nhanh nhất có thể):**

- Điền sổ đầu bài

- Báo cáo hành chính

- Nhập điểm vào hệ thống

Trước đây, mình dành 30 phút cho mỗi bản báo cáo hành chính. Giờ: 10 phút. Nó là O task — không ai đọc kỹ nó cả.

Thời gian giải phóng? Mình dùng để viết feedback dài 1 trang cho một học sinh đang struggle. Đó là L task — nó có thể thay đổi hướng đi của em đó.

## Framework: Pre-Mortem + LNO trong 5 phút

Bạn có thể dùng cả 2 framework cùng lúc:

**Bước 1: Trước khi bắt đầu dự án/tuần mới, làm Pre-Mortem mini**

- Liệt kê 1-2 Tiger (rủi ro thật)

- Xác định Elephant (thứ mình đang tránh)

- Chuẩn bị plan B cho tigers

**Bước 2: Nhìn to-do list qua lens LNO**

- Đánh dấu L/N/O cho mỗi task

- Dồn năng lượng cho L tasks

- Làm nhanh O tasks — *tệ cũng được*

**Bước 3: Kiểm tra cuối tuần**

- Tuần này mình có dành đủ thời gian cho L tasks không?

- Có tiger nào xuất hiện mà mình chưa xử lý không?

## "Great PMs" vs "Busy PMs"

Shreyas nói một câu mình ghi lại:

> **"Great PMs implicitly know what their L tasks are. They're the tasks that bother them the most — because they're not doing them."**

Đọc lại: L tasks là những task mà bạn *biết* bạn nên làm, nhưng bạn cứ trì hoãn. Viết chiến lược? Có đó. Nhưng mình bận chấm bài (N task). Chuẩn bị bài giảng mới? Có đó. Nhưng mình bận điền form (O task).

Busy ≠ productive. Và mình — sau 25 năm — mới hiểu ra điều này.

Tốt hơn muộn còn hơn... ờ, không biết 😅

---

*Thử nhìn lại to-do list hôm nay và đánh dấu L/N/O cho mỗi task. Bạn sẽ ngạc nhiên khi biết mình đang dành bao nhiêu thời gian cho O tasks. Và bao ít thời gian cho L tasks.* ☕
