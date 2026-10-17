import re
import sys

def replace_logos():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()
    
    matches = re.findall(r'src="data:image/[^"]+"', text)
    print(f"Found {len(matches)} base64 images")
    
    # We only want to replace them if there are exactly 2 (as seen in the About section) or a few that we are sure are logos.
    # The logos are inside the about section. Let's just do a blanket replace if we confirm they are the only ones, or limit to the about section.
    
    # The About section starts with "<!-- About Hero / Intro -->" and ends somewhere.
    # We can just replace all for now if there are only 2.
    if len(matches) > 0:
        new_text = re.sub(r'src="data:image/[^"]+"', 'src="our_logo.png"', text)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Replaced successfully.")

if __name__ == '__main__':
    replace_logos()
