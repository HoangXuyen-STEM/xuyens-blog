#!/bin/bash

# ==============================================================================
# Script tự động xuất bản 6 bài viết & 6 ảnh thumbnail lên blog.xuyenlab.com
# Quy trình chuẩn: copy ảnh -> commit/push -> build -> deploy Pages -> verify
# ==============================================================================

set -euo pipefail

WORKSPACE_DIR="/home/hoang-xuyen/Projects/xuyens-blog"
STATIC_IMAGES_DIR="$WORKSPACE_DIR/blog/static/images"
BRAIN_DIR="/home/hoang-xuyen/.gemini/antigravity/brain/561c79d8-66f8-4fe3-9d32-5989db10818f"
SLUGS=(
	"tuong-thuong-hieu-la-bong-bay-hoa-ra-lai-la-loi-hua-giu-moi-ngay"
	"tuong-day-hoc-la-giao-viec-hoa-ra-la-giao-bai-toan-can-giai"
	"tuong-phai-len-giong-moi-lam-thay-hoa-ra-noi-giong-doi-thuong-moi-cham"
	"tuong-quat-mang-la-uy-quyen-hoa-ra-la-vi-so"
	"tuong-tro-luoi-bieng-hoa-ra-thay-la-ke-dong-loa"
	"tuong-day-hoc-la-truyen-kien-thuc-hoa-ra-la-tim-khoanh-khac-5-giay"
)

echo "==> Sao chép thumbnail vào blog/static/images"
mkdir -p "$STATIC_IMAGES_DIR"

cp "$BRAIN_DIR/seth_godin_thumbnail_1779270208059.png" "$STATIC_IMAGES_DIR/${SLUGS[0]}.png"
cp "$BRAIN_DIR/marty_cagan_thumbnail_1779270221397.png" "$STATIC_IMAGES_DIR/${SLUGS[1]}.png"
cp "$BRAIN_DIR/tristan_montebello_thumbnail_1779270233726.png" "$STATIC_IMAGES_DIR/${SLUGS[2]}.png"
cp "$BRAIN_DIR/carole_robin_thumbnail_1779270413982.png" "$STATIC_IMAGES_DIR/${SLUGS[3]}.png"
cp "$BRAIN_DIR/jerry_colonna_thumbnail_1779270427947.png" "$STATIC_IMAGES_DIR/${SLUGS[4]}.png"
cp "$BRAIN_DIR/matthew_dicks_thumbnail_1779270440780.png" "$STATIC_IMAGES_DIR/${SLUGS[5]}.png"

cd "$WORKSPACE_DIR"

echo "==> Commit và push source"
git add blog/content/posts blog/static/images publish_v4.sh check_live.sh docs/WRITE-IMAGE-PUBLISH-RUNBOOK.md README.md
if ! git diff --cached --quiet; then
	git commit -m "Publish 6 bài viết mới chuẩn V4 và trọn bộ 6 ảnh thumbnail màu nước"
	git push origin master
else
	echo "Khong co thay doi moi de commit."
fi

echo "==> Build Hugo production"
cd "$WORKSPACE_DIR/blog"
hugo --minify

echo "==> Deploy blog/public len Cloudflare Pages"
cd "$WORKSPACE_DIR"
wrangler pages deploy blog/public --project-name xuyens-blog --branch master

echo "==> Verify production"
"$WORKSPACE_DIR/check_live.sh" "${SLUGS[@]}"

echo "==> Hoan tat"
echo "Production: https://blog.xuyenlab.com"
