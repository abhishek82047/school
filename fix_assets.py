import os
import re

file = 'index.html'

with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the inline images from h2
content = content.replace('<h2>Unique Pillars of Schooling <img src="assets/images/icons/7.png" style="width: 60px; vertical-align: middle; margin-left: 10px; animation: bounce 3s infinite;"></h2>',
                          '<h2>Unique Pillars of Schooling</h2>')

content = content.replace('<h2>Our 2025-26 Toppers <img src="assets/images/icons/11.png" style="width: 50px; vertical-align: middle; margin-left: 10px;"></h2>',
                          '<h2>Our 2025-26 Toppers</h2>')

content = content.replace('<h2>Welcome to Time Public School <img src="assets/images/icons/8.png" style="width: 40px; vertical-align: middle; margin-left: 10px;"></h2>',
                          '<h2>Welcome to Time Public School</h2>')

# 2. Add floating assets to sections
# For "Our Latest Events" section (around line 335 usually)
# Let's find: <section class="section-padding pt-5" style="background-color: var(--bg-tint);">
# and add position-relative
content = content.replace('<section class="section-padding pt-5" style="background-color: var(--bg-tint);">\n        <div class="container">',
                          '<section class="section-padding pt-5 position-relative overflow-hidden" style="background-color: var(--bg-tint);">\n        <img src="assets/images/icons/7.png" class="d-none d-lg-block position-absolute" style="top: 50px; right: 5%; width: 150px; opacity: 0.8; animation: float 4s infinite;">\n        <img src="assets/images/icons/12.png" class="d-none d-lg-block position-absolute" style="bottom: 50px; left: 5%; width: 120px; opacity: 0.8; animation: float 5s infinite; animation-delay: 1s;">\n        <div class="container position-relative z-1">')

# For "Core Values / Pillars" section
content = content.replace('<h2>Unique Pillars of Schooling</h2>',
                          '<h2>Unique Pillars of Schooling</h2>\n                <img src="assets/images/icons/10.png" class="position-absolute" style="top: -20px; left: -20px; width: 120px; opacity: 0.5; z-index: 0;">')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed HTML assets.")
