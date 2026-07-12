#!/bin/bash

set -euo pipefail

BASE_URL="https://blog.xuyenlab.com"
DEFAULT_COMMIT="HEAD"

usage() {
    echo "Usage: $0 [slug ...]"
    echo "   or: $0 --commit <commit>"
}

collect_slugs_from_commit() {
    local commit_ref="$1"
    git show "$commit_ref" --name-only --diff-filter=A \
        | grep '^blog/content/posts/.*\.md$' \
        | xargs -r -n1 basename \
        | sed 's/\.md$//'
}

if [[ "${1:-}" == "--commit" ]]; then
    if [[ $# -lt 2 ]]; then
        usage
        exit 1
    fi
    mapfile -t SLUGS < <(collect_slugs_from_commit "$2")
elif [[ $# -gt 0 ]]; then
    SLUGS=("$@")
else
    mapfile -t SLUGS < <(collect_slugs_from_commit "$DEFAULT_COMMIT")
fi

if [[ ${#SLUGS[@]} -eq 0 ]]; then
    echo "Khong tim thay slug nao de verify."
    exit 1
fi

SITEMAP_CONTENT=$(curl -fsSL "$BASE_URL/sitemap.xml")
OVERALL_OK=0

echo "| Slug | Post | Thumbnail | Sitemap | Live |"
echo "| :--- | ---: | ---: | :---: | :---: |"

for slug in "${SLUGS[@]}"; do
    POST_URL="$BASE_URL/posts/$slug/"
    IMG_URL="$BASE_URL/images/$slug.png"

    POST_STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$POST_URL")
    IMG_STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$IMG_URL")

    if grep -q "$slug" <<< "$SITEMAP_CONTENT"; then
        IN_SITEMAP="Yes"
    else
        IN_SITEMAP="No"
    fi

    if [[ "$POST_STATUS" == "200" && "$IMG_STATUS" == "200" ]]; then
        LIVE="YES"
    else
        LIVE="NO"
        OVERALL_OK=1
    fi

    echo "| $slug | $POST_STATUS | $IMG_STATUS | $IN_SITEMAP | $LIVE |"
done

exit $OVERALL_OK
