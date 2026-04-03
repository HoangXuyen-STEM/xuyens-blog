#!/bin/bash
# Script để cập nhật blog trên server
# Usage: ./update.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🔨 Building Hugo site..."
hugo --minify

echo "🐳 Rebuilding Docker container..."
docker compose up -d --build

echo "✅ Blog updated!"
echo "👉 Check: https://blog.xuyenlab.com"
