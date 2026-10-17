import re

content = open('index.html', 'r', encoding='utf-8').read()

companies = {
    'FedEx': 'fedex.com',
    'Disney': 'disney.com',
    'Dropbox': 'dropbox.com',
    'Claude': 'anthropic.com',
    'Reddit': 'reddit.com',
    'J.P. Morgan': 'jpmorgan.com',
    'Ryanair': 'ryanair.com',
    'American Airlines': 'aa.com',
    'Care.com': 'care.com',
    'Intel': 'intel.com'
}

for name, domain in companies.items():
    content = re.sub(
        rf'<span class="logo-item"><img src="our_logo\.png" alt="{name}" title="{name}" style="height:(\d+)px;"></span>',
        f'<span class="logo-item"><img src="https://logo.clearbit.com/{domain}" alt="{name}" title="{name}" style="height:\\1px; filter: brightness(0) invert(1); opacity: 0.8; object-fit: contain;"></span>',
        content
    )

open('index.html', 'w', encoding='utf-8').write(content)
print('Fixed marquee logos!')
