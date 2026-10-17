import re

content = open('index.html', 'r', encoding='utf-8').read()

old_classes = "bg-[rgba(255,255,255,0.03)] backdrop-blur-xl border border-[rgba(255,255,255,0.08)] shadow-[0_8px_32px_0_rgba(0,0,0,0.3)] rounded-xl p-5 hover:border-[rgba(255,51,51,0.4)] hover:bg-[rgba(255,255,255,0.06)]"

new_classes = "bg-white/10 backdrop-blur-md border border-white/20 shadow-[inset_0_1px_1px_rgba(255,255,255,0.3),0_8px_32px_0_rgba(0,0,0,0.3)] rounded-2xl p-6 hover:border-white/40 hover:bg-white/20"

new_content = content.replace(old_classes, new_classes)

open('index.html', 'w', encoding='utf-8').write(new_content)
print('Updated review boxes!')
