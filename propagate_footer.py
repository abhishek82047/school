import os
import re

# Read the new footer area from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Match from multi-waves-container to the end of footer
footer_pattern = r'<!-- Shared Footer Area with Multi-Waves -->.*?</footer>'
footer_match = re.search(footer_pattern, index_content, re.DOTALL)

if not footer_match:
    print("Could not find footer in index.html")
    exit(1)

new_footer_block = footer_match.group(0)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    if file == 'index.html': continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing footer structures
    # It might have the old wave-footer-top or the new multi-waves-container
    content = re.sub(r'<!-- (Shared Footer|Footer).*?</footer>', new_footer_block, content, flags=re.DOTALL)
    
    # If the above didn't work (no comments), try raw footer tags
    if 'footer-new' not in content:
        content = re.sub(r'<div class="wave-footer-top"></div>.*?<footer.*?</footer>', new_footer_block, content, flags=re.DOTALL)
        content = re.sub(r'<footer.*?</footer>', new_footer_block, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Successfully propagated the premium multi-wave footer to all panels.")
