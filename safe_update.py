import os
import re

def update_files(directory):
    replacements = [
        (r'fa-phone-alt', 'fa-phone-volume'),
        (r'07652-452027', ''),
    ]
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                for pattern, replacement in replacements:
                    content = re.sub(pattern, replacement, content)
                
                # Special case for the hero pagination in index.html
                if file == 'index.html':
                    content = re.sub(r'<!-- Vertical Pagination Dots -->\s+<div class="hero-pagination-vertical">.*?</div>', '', content, flags=re.DOTALL)
                
                # Clean up <br> tags left after phone removal
                content = content.replace('<br></span>', '</span>')
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file_path}")

if __name__ == "__main__":
    update_files('.')
