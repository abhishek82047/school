import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove sticky-top from navbar
    new_content = content.replace('navbar-expand-lg sticky-top', 'navbar-expand-lg')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated all navbars to be floating.")
