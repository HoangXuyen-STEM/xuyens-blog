#!/bin/bash

# Xuyen's Blog - Automated Deployment Script
# Usage: ./deploy.sh

set -e  # Exit on error

echo "🔨 Building Hugo site..."
hugo --minify

if [ $? -ne 0 ]; then
    echo "❌ Hugo build failed!"
    exit 1
fi

echo "📊 Build statistics:"
echo "   HTML files: $(find public/ -name "*.html" | wc -l)"
echo "   Total size: $(du -sh public/ | cut -f1)"

echo ""
echo "🐳 Building and deploying Docker container..."
docker compose up -d --build

if [ $? -ne 0 ]; then
    echo "❌ Docker deployment failed!"
    exit 1
fi

echo ""
echo "⏳ Waiting for container to be healthy..."
sleep 3

echo ""
echo "🔍 Container status:"
docker ps | grep xuyens-blog

echo ""
echo "📝 Recent logs:"
docker logs --tail 10 xuyens-blog

echo ""
echo "✅ Deployment complete!"
echo "🌐 Local: http://localhost:2368"
echo "🌐 Tunnel target: http://localhost:8090"
echo "🌐 Production: https://blog.xuyenlab.com"
echo ""
echo "💡 To view logs: docker logs -f xuyens-blog"
echo "💡 To restart: docker compose restart"
echo "💡 To stop: docker compose down"
