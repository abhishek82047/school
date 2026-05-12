import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    if file == 'disclosure.html': continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the empty link for Mandatory Disclosure
    content = content.replace('<a class="nav-link" href="#">Mandatory Disclosure</a>', 
                             '<a class="nav-link" href="disclosure.html">Mandatory Disclosure</a>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links to Mandatory Disclosure in all files.")
