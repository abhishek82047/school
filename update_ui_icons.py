import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

menu_decoration = """
                        <div class="text-center mt-3 mb-2">
                            <img src="assets/images/icons/15.png" alt="Kids" style="width: 80px; margin-right: 10px;">
                            <img src="assets/images/icons/16.png" alt="Bus" style="width: 80px;">
                        </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add to mobile menu
    if 'mobile-social-links' in content and 'assets/images/icons/15.png' not in content:
        content = content.replace('<div class="mobile-social-links', menu_decoration + '                        <div class="mobile-social-links')

    # 2. Add to index.html specific places
    if file == 'index.html':
        # Replace feature icons in Pillars
        content = content.replace('<div class="feature-icon"><i class="fas fa-microscope"></i></div>',
                                  '<div class="feature-icon"><img src="assets/images/icons/12.png" style="width: 45px;"></div>')
        content = content.replace('<div class="feature-icon"><i class="fas fa-brain"></i></div>',
                                  '<div class="feature-icon"><img src="assets/images/icons/13.png" style="width: 45px;"></div>')
        content = content.replace('<div class="feature-icon"><i class="fas fa-user-shield"></i></div>',
                                  '<div class="feature-icon"><img src="assets/images/icons/3.png" style="width: 45px;"></div>')
        
        # Add chalkboard to the section title of Core Values
        content = content.replace('<h2>Unique Pillars of Schooling</h2>',
                                  '<h2>Unique Pillars of Schooling <img src="assets/images/icons/7.png" style="width: 60px; vertical-align: middle; margin-left: 10px; animation: bounce 3s infinite;"></h2>')

        # Add ABC to Toppers section
        content = content.replace('<h2>Our 2025-26 Toppers</h2>',
                                  '<h2>Our 2025-26 Toppers <img src="assets/images/icons/11.png" style="width: 50px; vertical-align: middle; margin-left: 10px;"></h2>')
        
        # Add cute sun/flower to About section title
        content = content.replace('<h2>Welcome to Time Public School</h2>',
                                  '<h2>Welcome to Time Public School <img src="assets/images/icons/8.png" style="width: 40px; vertical-align: middle; margin-left: 10px;"></h2>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files with new PNG assets.")
