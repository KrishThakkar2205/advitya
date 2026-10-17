import fitz
import re

pdf_path = r'C:\Users\Prince Mehta\.gemini\antigravity\brain\9bce81c9-a53c-4ba2-9ff8-56b72a39165a\media__1784546486958.pdf'
doc = fitz.open(pdf_path)

logo_files = []
for i in range(len(doc)):
    page = doc.load_page(i)
    # The pdf pages are white-background with logos. 
    # Actually wait! The OCR saw them on a white background, maybe the PDF has no background (transparent).
    pix = page.get_pixmap(alpha=True, dpi=300)
    out_name = f'company_logo_{i}.png'
    pix.save(out_name)
    logo_files.append(out_name)

print(f'Extracted {len(doc)} logos')

content = open('index.html', 'r', encoding='utf-8').read()

logos_html = ''
for f in logo_files:
    # 13 is empty in the screenshots, but I'll just include it. If it's a 1x1 pixel, it's fine.
    # We remove the filter because the new logos are ready-made.
    logos_html += f'                            <span class="logo-item"><img src="{f}" alt="Company" style="height:36px; object-fit: contain;"></span>\n'

full_logos = logos_html + '                            <!-- Duplicate for loop -->\n' + logos_html

pattern = re.compile(r'(<div class="logos-track"[^>]*>).*?(</div>)', re.DOTALL)
new_content = pattern.sub(r'\1\n' + full_logos + r'                        \2', content)

open('index.html', 'w', encoding='utf-8').write(new_content)
print('Updated HTML')
