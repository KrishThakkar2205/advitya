from PIL import Image
import glob
import re

# Trim transparent pixels from all logos
for img_path in glob.glob('company_logo_*.png'):
    im = Image.open(img_path)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    
    bbox = im.getbbox()
    if bbox:
        trimmed = im.crop(bbox)
        trimmed.save(img_path)
        print(f"Trimmed {img_path}")
    else:
        print(f"Empty image: {img_path}")

# Update the HTML to have a smaller, more consistent height now that the padding is gone
content = open('index.html', 'r', encoding='utf-8').read()
new_content = content.replace('style="height:120px; object-fit: contain;"', 'style="height:44px; object-fit: contain;"')
open('index.html', 'w', encoding='utf-8').write(new_content)
print("Updated HTML with consistent 44px height.")
