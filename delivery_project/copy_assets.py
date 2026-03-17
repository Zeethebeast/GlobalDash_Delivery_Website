import os
import shutil
import glob

brain_dir = r"C:\Users\ZEE NATION\.gemini\antigravity\brain\7e9237f2-4b56-4900-bd29-95afaa40f501"
static_img_dir = r"C:\Users\ZEE NATION\.gemini\antigravity\scratch\delivery_project\static\images"

os.makedirs(static_img_dir, exist_ok=True)
for f in glob.glob(os.path.join(brain_dir, "*.png")):
    fname = os.path.basename(f)
    # create generic names for easy template usage
    if "truck" in fname.lower():
        dest = os.path.join(static_img_dir, "truck.png")
    elif "driver" in fname.lower():
        dest = os.path.join(static_img_dir, "driver.png")
    elif "map" in fname.lower():
        dest = os.path.join(static_img_dir, "map.png")
    elif "carousel_warehouse" in fname.lower():
        dest = os.path.join(static_img_dir, "carousel_warehouse.png")
    elif "carousel_fleet" in fname.lower():
        dest = os.path.join(static_img_dir, "carousel_fleet.png")
    elif "carousel_delivery" in fname.lower():
        dest = os.path.join(static_img_dir, "carousel_delivery.png")
    elif "promo_speed" in fname.lower():
        dest = os.path.join(static_img_dir, "promo_speed.png")
    elif "promo_global" in fname.lower():
        dest = os.path.join(static_img_dir, "promo_global.png")
    else:
        dest = os.path.join(static_img_dir, fname)
    shutil.copy(f, dest)
    print(f"Copied {f} to {dest}")
