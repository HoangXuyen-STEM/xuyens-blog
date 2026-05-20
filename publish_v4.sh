#!/bin/bash

# ==============================================================================
# Script tự động xuất bản 6 bài viết & 6 ảnh Thumbnail màu nước lên blog.xuyenlab.com
# ==============================================================================

# Định nghĩa đường dẫn
WORKSPACE_DIR="/home/hoang-xuyen/Projects/xuyens-blog"
STATIC_IMAGES_DIR="$WORKSPACE_DIR/blog/static/images"
BRAIN_DIR="/home/hoang-xuyen/.gemini/antigravity/brain/561c79d8-66f8-4fe3-9d32-5989db10818f"

echo "🎨 Đang sao chép các ảnh thumbnail màu nước từ thư mục Brain sang Hugo Static..."

# Đảm bảo thư mục đích tồn tại
mkdir -p "$STATIC_IMAGES_DIR"

# Copy các ảnh thumbnail của Batch mới
cp "$BRAIN_DIR/seth_godin_thumbnail_1779270208059.png" "$STATIC_IMAGES_DIR/tuong-thuong-hieu-la-bong-bay-hoa-ra-lai-la-loi-hua-giu-moi-ngay.png"
cp "$BRAIN_DIR/marty_cagan_thumbnail_1779270221397.png" "$STATIC_IMAGES_DIR/tuong-day-hoc-la-giao-viec-hoa-ra-la-giao-bai-toan-can-giai.png"
cp "$BRAIN_DIR/tristan_montebello_thumbnail_1779270233726.png" "$STATIC_IMAGES_DIR/tuong-phai-len-giong-moi-lam-thay-hoa-ra-noi-giong-doi-thuong-moi-cham.png"

# Copy các ảnh thumbnail của Batch trước
cp "$BRAIN_DIR/carole_robin_thumbnail_1779270413982.png" "$STATIC_IMAGES_DIR/tuong-quat-mang-la-uy-quyen-hoa-ra-la-vi-so.png"
cp "$BRAIN_DIR/jerry_colonna_thumbnail_1779270427947.png" "$STATIC_IMAGES_DIR/tuong-tro-luoi-bieng-hoa-ra-thay-la-ke-dong-loa.png"
cp "$BRAIN_DIR/matthew_dicks_thumbnail_1779270440780.png" "$STATIC_IMAGES_DIR/tuong-day-hoc-la-truyen-kien-thuc-hoa-ra-la-tim-khoanh-khac-5-giay.png"

echo "✅ Đã sao chép thành công 6 ảnh thumbnail vào thư mục tĩnh của Hugo!"
echo ""

# Tiến hành commit và push lên master để kích hoạt Cloudflare Pages Deploy
echo "🚀 Đang thực hiện Git commit và push để publish lên blog.xuyenlab.com..."
cd "$WORKSPACE_DIR"

git add .
git commit -m "Publish 6 bài viết mới chuẩn V4 và trọn bộ 6 ảnh thumbnail màu nước"
git push origin master

echo "🎉 QUÁ TRÌNH HOÀN TẤT! Cloudflare Pages sẽ tự động deploy sau 1-2 phút."
echo "🔗 Anh có thể kiểm tra trực tiếp tại: https://blog.xuyenlab.com"
