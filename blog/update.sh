#!/bin/bash
# Script để cập nhật blog trên server
# Usage: ./update.sh

echo "🔨 Building Hugo site..."
hugo --minify

echo "🐳 Rebuilding Docker container..."
docker compose up -d --build

echo "✅ Blog updated!"
echo "👉 Check: https://blog.xuyenlab.com"
