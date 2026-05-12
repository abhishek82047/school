import os
import re

preloader_html = """    <!-- Preloader -->
    <div id="preloader">
        <div class="loader">
            <div class="loader-img">
                <img src="assets/images/logo.png" alt="Logo">
            </div>
            <div class="loader-line"></div>
        </div>
    </div>
"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div id="preloader">' in content:
        continue
        
    # Inject right after <body>
    new_content = re.sub(r'<body>', '<body>\n' + preloader_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Injected preloader into all HTML files.")
