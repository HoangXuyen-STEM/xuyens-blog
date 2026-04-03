# Runbook: Viet Bai -> Tao Anh -> Publish

Ngay cap nhat: 2026-04-03

## 1) Tong hop cong viec da lam hom nay

### Boi canh
- May tinh bi mat du lieu, repo clone lai o duong dan moi.
- 6 bai moi ngay 2026-04-02 chua duoc day len Notion va blog production.

### Su co chinh da xu ly
- Thieu pipeline Notion sau khi clone may moi.
- Script deploy phu thuoc duong dan hien tai (khong an toan khi doi path).
- Production Cloudflare Pages bi lech giua Preview va Production, gay tinh trang bai da co nhung home/list chua cap nhat.
- Thumbnail chua dung mapping theo 6 bai.

### Ket qua da dat
- Khoi phuc day du pipeline Notion:
  - `blog/sync/push_to_notion.py`
  - `blog/sync/sync_notion_to_hugo.py`
  - `blog/.env.example`
- Chuan hoa script deploy/update theo duong dan tuong doi voi vi tri script.
- Day 6 bai 2026-04-02 len Notion thanh cong.
- Dong bo va xuat ban 6 bai len production thanh cong.
- Da map thumbnail dung theo 6 slug bai viet va da thay bang bo anh moi do user cung cap.
- Production da xac nhan tra anh PNG HTTP 200 cho ca 6 bai.

### Commit lien quan (tham khao)
- `b814c68`: restore Notion pipeline + publish batch bai moi.
- `3cf4ef1`: bo sung thumbnail rieng cho 6 bai (giai doan dau).
- `6adf632`: doi frontmatter sang mapping PNG.
- `f299422`: thay bo 6 anh PNG bang bo anh moi user cung cap + xoa SVG cu.

---

## 2) Quy trinh chuan cho lan sau

Muc tieu: Moi lan xuat ban se theo dung thu tu **Viet bai -> Tao anh -> Gan thumbnail -> Day Notion -> Publish production -> Verify**.

### Buoc 0 - Kiem tra nhanh truoc khi lam
```bash
cd /home/hoang-xuyen/Projects/xuyens-blog
git pull origin master
```

Kiem tra file moi truong local (neu la may moi):
```bash
cp -n blog/.env.example blog/.env
```

Can dam bao `blog/.env` co:
- `NOTION_API_KEY`
- `NOTION_DATABASE_ID`
- `NOTION_SYNC_STATUSES` (goi y: `Published,Review` khi review; `Published` khi production nghiem ngat)

### Buoc 1 - Viet bai markdown
Tao bai moi:
```bash
cd blog
hugo new posts/ten-bai-viet.md
```

Yeu cau frontmatter toi thieu:
- `title`
- `date`
- `slug`
- `status: "published"` (neu muon len list/home)
- `thumbnail: "/images/<slug>.png"`
- `categories`, `tags` theo quy uoc noi dung

### Buoc 2 - Tao anh thumbnail
Quy uoc ten file:
- Dat dung theo slug bai viet: `blog/static/images/<slug>.png`
- Ti le khuyen nghi: 1200x630
- Format: PNG

Checklist:
- Moi bai 1 anh dung ten slug
- Khong dung khoang trang, khong ky tu la
- Duong dan frontmatter trung khop 100% voi ten file

### Buoc 3 - Day bai len Notion (neu can quy trinh Notion truoc)
```bash
cd /home/hoang-xuyen/Projects/xuyens-blog/blog
python3 sync/push_to_notion.py --since-date YYYY-MM-DD
```

Dong bo tu Notion ve Hugo (khi can):
```bash
python3 sync/sync_notion_to_hugo.py
```

### Buoc 4 - Build local de check truoc publish
```bash
cd /home/hoang-xuyen/Projects/xuyens-blog/blog
hugo --minify
```

Neu build fail thi sua xong moi publish.

### Buoc 5 - Commit va push
```bash
cd /home/hoang-xuyen/Projects/xuyens-blog
git add blog/content/posts/*.md blog/static/images/*.png
git commit -m "feat(posts): publish new posts with thumbnails"
git push origin master
```

### Buoc 6 - Deploy production
Uu tien theo CI (GitHub Actions/Pages tu dong sau khi push).

Fallback deploy gap (direct upload bang Wrangler):
```bash
cd /home/hoang-xuyen/Projects/xuyens-blog/blog
hugo --minify
cd ..
wrangler pages deploy blog/public --project-name xuyens-blog --branch master
```

### Buoc 7 - Verify production (bat buoc)
Kiem tra bai len domain:
```bash
curl -I https://blog.xuyenlab.com/
```

Kiem tra thumb cua tung bai:
```bash
curl -sI https://blog.xuyenlab.com/images/<slug>.png
```
Ky vong:
- `HTTP 200`
- `content-type: image/png`

---

## 3) Checklist rut gon (copy dung moi lan)

- [ ] Pull code moi nhat tu `master`
- [ ] Viet/hoan thien markdown bai moi
- [ ] Tao PNG dung ten slug
- [ ] Gan `thumbnail` dung duong dan `/images/<slug>.png`
- [ ] (Neu can) push Notion
- [ ] Hugo build pass
- [ ] Commit + push `master`
- [ ] Deploy production (CI hoac fallback)
- [ ] Verify URL bai + verify thumbnail HTTP 200

---

## 4) Loi thuong gap va cach xu ly nhanh

### Bai da co trong Notion nhung khong len home/list
- Kiem tra `status` trong frontmatter co phai `published` khong.
- Kiem tra deployment dang o Preview hay Production branch `master`.

### Anh co tren repo nhung production chua hien
- Kiem tra da push commit chua.
- Neu can gap, deploy truc tiep bang Wrangler nhu Buoc 6.

### Clone may moi bi mat script Notion
- Doi chieu lai 3 file: `blog/sync/push_to_notion.py`, `blog/sync/sync_notion_to_hugo.py`, `blog/.env.example`.
- Tao lai `blog/.env` va dien secret.
