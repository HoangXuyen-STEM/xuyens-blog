---
title: "ClaudePrism: Khi Nhà Khoa Học Dùng AI Mà Dữ Liệu Không Cần Lên Cloud"
slug: "claudeprism-viet-bao-offline"
summary: "Mình tưởng muốn viết báo khoa học bằng AI là phải upload hết data lên server của người ta. Hóa ra không."
categories: ["ai-technology"]
tags: ["ai-tools", "research", "productivity", "open-source"]
thumbnail: "/images/claudeprism-viet-bao-offline.jpg"
lenny_episode: "ClaudePrism — github.com/delibae/claude-prism"
cta_type: "course"
date: 2026-03-16
status: "published"
---

Mình nhớ cái buổi chiều hôm đó rất rõ.

Một người bạn làm nghiên cứu sinh ngành dược — 5 năm số liệu thí nghiệm, hàng trăm file CSV về tương tác phân tử — nhờ mình tư vấn cách dùng AI để viết báo khoa học nhanh hơn. Mình hào hứng lắm. Mở laptop, chuẩn bị giới thiệu một loạt tool.

Rồi bạn ấy hỏi một câu mình không lường trước: *"Nếu mình upload data lên đó, thì Anthropic/OpenAI có đọc không?"*

Mình im lặng.

Câu hỏi đó — đơn giản vậy thôi — đã chặn đứng cả buổi tư vấn của mình. Vì câu trả lời trung thực là: *có thể.* Dữ liệu thí nghiệm của bạn, kết quả chưa công bố, hợp chất bạn đang nghiên cứu — khi bạn paste vào ChatGPT hay Claude.ai, nó sẽ đi qua server của họ. Và chính sách lưu trữ thì... đọc xong đau đầu lắm.

Hôm đó, mình không có câu trả lời tốt cho bạn ấy.

## Tưởng phải chọn giữa "AI" và "quyền riêng tư"

Câu chuyện của bạn mình không phải ngoại lệ. Mình đã gặp khá nhiều domain expert ở Việt Nam — bác sĩ, dược sĩ, kỹ sư, nhà nghiên cứu — đều đang vướng mắc ở một chỗ giống nhau:

*Họ biết AI hữu ích. Nhưng dữ liệu của họ nhạy cảm.*

Bác sĩ có hồ sơ bệnh nhân. Kỹ sư có bản vẽ kỹ thuật nội bộ. Nhà nghiên cứu có số liệu chưa công bố. Upload tất cả lên cloud AI? Không ổn.

Vậy thì không dùng AI? Cũng không ổn — vì đối thủ của họ đang dùng.

Mình cứ tưởng đây là bài toán không có lời giải. Hóa ra có người đã giải rồi.

## ClaudePrism: AI chạy trên máy bạn, không phải trên server của ai

[ClaudePrism](https://github.com/delibae/claude-prism) là một desktop app mã nguồn mở — hoàn toàn miễn phí — được thiết kế cho một mục đích cụ thể: **viết báo khoa học với AI, mà dữ liệu nằm trên ổ cứng của bạn.**

Không phải cloud. Không phải server ai đó. Ổ cứng của *bạn*.

Cụ thể nó làm được gì?

**LaTeX offline.** Nếu bạn làm nghiên cứu, bạn biết LaTeX — định dạng tiêu chuẩn cho báo khoa học. Nhưng cài LaTeX truyền thống thì phức tạp kinh khủng. ClaudePrism dùng Tectonic — một engine LaTeX nhúng thẳng vào app, compile offline không cần cài thêm gì. Lần đầu tải package, lần sau dùng không cần internet.

**Python một click.** Click "Install uv" → click "Create venv" → Python environment sẵn sàng. Claude tự dùng môi trường đó để chạy code phân tích, vẽ biểu đồ, xử lý data — ngay trong editor. Không cần mở terminal. Không cần biết `pip install` là gì.

**100+ scientific skills.** Đây là phần mình thấy ấn tượng nhất. ClaudePrism có một thư viện skill chuyên ngành: bioinformatics, cheminformatics, machine learning, clinical research, multi-omics... Mỗi skill là một bộ prompt + tool configuration giúp Claude hiểu sâu vào lĩnh vực đó. Bạn nghiên cứu RDKit? Có skill RDKit. Bạn dùng Scanpy? Có skill Scanpy.

**Claude AI trực tiếp trong editor.** Chat với Claude, chọn model (Opus, Sonnet, Haiku), dùng slash commands, xem proposed changes dạng diff — chấp nhận hoặc từ chối từng chunk. Giống như có một cộng sự ngồi bên cạnh, không phải một chatbot trả lời xong là quên.

> 💡 **Lưu ý quan trọng:** Khi bạn dùng tính năng AI của ClaudePrism, nội dung bạn đưa vào *vẫn được gửi đến Anthropic API* để Claude xử lý. ClaudePrism offline ở chỗ: *file không lưu trên server*, compile LaTeX không cần internet, Python chạy local. Nhưng inference của AI thì vẫn qua cloud. Điều này khác hoàn toàn với các tool lưu hết mọi thứ lên server của họ.

## Mình — một người không phải nhà nghiên cứu — thấy gì?

Phải thú thật: mình không làm nghiên cứu khoa học. Mình là giáo viên. LaTeX với mình trước đây giống như đọc tờ hướng dẫn lắp đồ IKEA bằng tiếng Thụy Điển.

Nhưng khi thử ClaudePrism, mình nhận ra một điều: *đây không chỉ là tool cho nhà khoa học.*

Nguyên tắc nó dùng — **local-first, AI-assisted, open source** — áp dụng được cho bất kỳ ai cần viết tài liệu kỹ thuật mà cần privacy. Kỹ sư viết spec. Bác sĩ soạn protocol. Luật sư soạn hợp đồng.

Câu hỏi không phải là "tôi có phải nhà khoa học không?" Câu hỏi là: "Tôi có dữ liệu nhạy cảm cần xử lý với AI không?"

Nếu có — ClaudePrism đáng để thử.

## So với OpenAI Prism: Tại sao mã nguồn mở thắng?

OpenAI vừa ra [OpenAI Prism](https://openai.com/prism/) — một workspace LaTeX trên cloud. ClaudePrism được sinh ra như một sự đối chiếu trực tiếp. Hãy nhìn nhanh:

| | OpenAI Prism | ClaudePrism |
|---|---|---|
| **Dữ liệu** | Lưu trên server OpenAI | Lưu trên máy bạn |
| **LaTeX** | Cloud compile | Offline (Tectonic) |
| **Python** | Không có | Có (uv + venv) |
| **Giá** | Trả phí | Miễn phí |
| **Mã nguồn** | Đóng | Mở (MIT) |

Không phải OpenAI Prism tệ. Nó tiện nếu bạn không quan tâm data đi đâu. Nhưng nếu bạn *quan tâm* — và nhiều domain expert Việt Nam đang ngày càng quan tâm hơn — ClaudePrism cho bạn lựa chọn.

## Bài học rộng hơn: "Offline-first" sẽ là xu hướng tiếp theo

Mình có một dự đoán nho nhỏ.

Giai đoạn đầu của AI (2022-2024): mọi người hào hứng upload mọi thứ lên cloud AI. *Nhanh, tiện, không suy nghĩ nhiều.*

Giai đoạn tiếp theo (2025 trở đi): domain expert bắt đầu hỏi *"dữ liệu của mình đi đâu?"* — và đòi hỏi nhiều hơn về quyền kiểm soát.

ClaudePrism không phải tool duy nhất theo hướng này. Nhưng nó là một trong số ít tool đủ hoàn chỉnh để domain expert thật sự dùng được — không cần biết cách cài TeX Live, không cần biết cách tạo virtualenv bằng tay.

Và điều đó mới quan trọng. Không phải công nghệ đằng sau — mà là *ai có thể dùng được.*

---

*Nếu bạn làm nghiên cứu, viết báo, hoặc xử lý dữ liệu nhạy cảm — hãy thử ClaudePrism. Miễn phí, mã nguồn mở, chạy trên Windows/macOS/Linux. Đường link ở đây: [github.com/delibae/claude-prism](https://github.com/delibae/claude-prism)*

*Còn bạn đang dùng tool gì để viết tài liệu kỹ thuật hiện tại? Mình tò mò lắm.* ☕
