import os
import re

def update_phone_numbers(directory):
    patterns = [
        (r'9993538999', '8962720522'),
        (r'99935 38999', '89627 20522'),
    ]
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                for pattern, replacement in patterns:
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file_path}")

if __name__ == "__main__":
    update_phone_numbers('.')
