import re

content = open('index.html', 'r', encoding='utf-8').read()
new_content = content.replace('style="height:36px; object-fit: contain;"', 'style="height:120px; object-fit: contain;"')

open('index.html', 'w', encoding='utf-8').write(new_content)
print('Updated logo height to 120px')
