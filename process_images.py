
import os
import glob
from PIL import Image

ARTIFACT_DIR = "/home/hoang-xuyen/.gemini/antigravity/brain/8d833a3d-fdcd-4d4c-993f-d73575d01b86"
TARGET_DIR = "/home/hoang-xuyen/Documents/Dự án/xuyens-blog/blog/static/images"

# Ensure target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# Mapping of source prefix (in artifact dir, using underscores) to target filename (using hyphens)
mapping = {
    "ai_khong_cuop_viec": "ai-khong-cuop-viec.jpg",
    "dung_duoi_theo_ai": "dung-duoi-theo-ai.jpg",
    "prototype_truoc_ke_hoach_sau": "prototype-truoc-ke-hoach-sau.jpg",
    "thoat_khoi_che_do_tu_dong": "thoat-khoi-che-do-tu-dong.jpg",
    "nghi_nhu_nguoi_choi_poker": "nghi-nhu-nguoi-choi-poker.jpg",
    "pre_mortem_tim_that_bai_truoc": "pre-mortem-tim-that-bai-truoc.jpg",
    "ngung_hop_nhieu_quyet_dinh_tot_hon": "ngung-hop-nhieu-quyet-dinh-tot-hon.jpg",
    "su_nghiep_khong_phai_cuoc_dua": "su-nghiep-khong-phai-cuoc-dua.jpg",
    "con_duong_khong_loi_mon": "con-duong-khong-loi-mon.jpg",
    "tu_duy_product_thinking": "tu-duy-product-thinking.jpg"
}

print(f"Processing images from {ARTIFACT_DIR} to {TARGET_DIR}...")

for src_prefix, target_name in mapping.items():
    # Find the source file
    pattern = os.path.join(ARTIFACT_DIR, f"{src_prefix}*.png")
    files = glob.glob(pattern)
    
    if not files:
        print(f"WARNING: No source file found for {src_prefix}")
        continue
        
    # Use the most recent file if multiple exist (though unlikely with just one generation run)
    files.sort(key=os.path.getmtime, reverse=True)
    src_file = files[0]
    target_path = os.path.join(TARGET_DIR, target_name)
    
    try:
        with Image.open(src_file) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(target_path, "JPEG", quality=90)
        print(f"Successfully processed: {target_name}")
    except Exception as e:
        print(f"ERROR convertng {src_prefix}: {e}")

print("Done.")
