import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add back sticky-top to navbar
    if 'navbar-expand-lg sticky-top' not in content:
        new_content = content.replace('navbar navbar-expand-lg', 'navbar navbar-expand-lg sticky-top')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Reverted all navbars to sticky-top.")
