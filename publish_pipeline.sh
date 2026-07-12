#!/usr/bin/env bash
# Canonical production pipeline for Xuyen's Blog.
# Notion Published → Hugo → Git → Cloudflare Pages → live verification.

set -Eeuo pipefail

# Cron has a minimal PATH; include Snap because Hugo is installed there.
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$REPO_DIR/blog"
LOG_DIR="$REPO_DIR/.ops-logs"
LOCK_FILE="/tmp/xuyens-blog-publish.lock"
DRY_RUN=0
FORCE_DEPLOY=0
SKIP_SYNC=0

usage() {
  cat <<'EOF'
Usage: ./publish_pipeline.sh [--dry-run] [--force-deploy] [--skip-sync]

  --dry-run      Validate sync/build plan without Git push or Cloudflare deploy.
  --force-deploy Deploy current Hugo build even when sync produced no source changes.
  --skip-sync    Do not call Notion; validate/build the current local source only.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --force-deploy) FORCE_DEPLOY=1 ;;
    --skip-sync) SKIP_SYNC=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/publish-$(date +%F).log"
exec > >(tee -a "$LOG_FILE") 2>&1

log() { printf '[%s] %s\n' "$(date '+%F %T')" "$*"; }
fail() { log "ERROR: $*"; exit 1; }
trap 'fail "Pipeline stopped at line $LINENO"' ERR

command -v flock >/dev/null || fail "flock is required"
exec 9>"$LOCK_FILE"
flock -n 9 || fail "Another publish pipeline is already running"

cd "$REPO_DIR"
[[ "$(git branch --show-current)" == "master" ]] || fail "Pipeline must run on master"

# Never mix an automated publish with unfinished human work.
if [[ $DRY_RUN -eq 0 ]] && [[ -n "$(git status --porcelain)" ]]; then
  fail "Git workspace is not clean; refusing automated publish"
fi

log "Starting pipeline (dry_run=$DRY_RUN, skip_sync=$SKIP_SYNC, force_deploy=$FORCE_DEPLOY)"

if [[ $SKIP_SYNC -eq 0 ]]; then
  log "Syncing approved Notion posts (Published only)"
  NOTION_SYNC_STATUSES=Published /usr/bin/python3 "$BLOG_DIR/sync/sync_notion_to_hugo.py"
fi

log "Validating post frontmatter and local thumbnails"
/usr/bin/python3 - "$BLOG_DIR" <<'PY'
import re
import sys
from pathlib import Path

blog = Path(sys.argv[1])
errors = []
for post in sorted((blog / "content" / "posts").glob("*.md")):
    text = post.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text:
        errors.append(f"{post.name}: invalid YAML frontmatter")
        continue
    fm = text.split("\n---\n", 1)[0]
    fields = {}
    for line in fm.splitlines()[1:]:
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key.strip()] = value
    def field(name):
        return fields.get(name, "").strip()
    status = field("status").lower()
    # Draft/review files may remain in the repository, but Hugo excludes them.
    # Validate the complete production contract only for published posts.
    if status == "published":
        for required in ("title", "slug", "date", "status", "thumbnail"):
            if not field(required):
                errors.append(f"{post.name}: missing {required}")
        thumbnail = field("thumbnail")
        if thumbnail.startswith("/images/"):
            image = blog / "static" / thumbnail.lstrip("/")
            if not image.exists():
                errors.append(f"{post.name}: missing thumbnail {thumbnail}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Validation passed")
PY

log "Building Hugo"
(
  cd "$BLOG_DIR"
  hugo --minify --gc
)

SOURCE_CHANGED=0
if [[ -n "$(git status --porcelain -- blog/content blog/static/images)" ]]; then
  SOURCE_CHANGED=1
fi

if [[ $DRY_RUN -eq 1 ]]; then
  log "Dry-run passed; source_changed=$SOURCE_CHANGED. No commit, push or deploy performed."
  exit 0
fi

if [[ $SOURCE_CHANGED -eq 1 ]]; then
  log "Committing synchronized content"
  git add blog/content blog/static/images
  git commit -m "chore(content): publish approved Notion posts"
  git push origin master
else
  log "No approved content changes detected"
fi

if [[ $SOURCE_CHANGED -eq 0 && $FORCE_DEPLOY -eq 0 ]]; then
  log "Nothing to deploy; exiting successfully"
  exit 0
fi

log "Deploying Hugo public directory to Cloudflare Pages"
wrangler pages deploy "$BLOG_DIR/public" --project-name xuyens-blog --branch master

log "Verifying production homepage and sitemap"
for url in "https://blog.xuyenlab.com/" "https://blog.xuyenlab.com/sitemap.xml"; do
  status="$(curl -L -sS -o /dev/null -w '%{http_code}' "$url")"
  [[ "$status" == "200" ]] || fail "Verification failed: $url returned $status"
done

if [[ $SOURCE_CHANGED -eq 1 ]]; then
  log "Verifying newly committed posts"
  "$REPO_DIR/check_live.sh" --commit HEAD
fi

log "Pipeline completed successfully"
