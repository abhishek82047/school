import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Gallery link
    new_content = content.replace('<a class="nav-link" href="#">Gallery</a>', '<a class="nav-link" href="gallery.html">Gallery</a>')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
