import os

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = "wix_html = clean_html"
if target in code:
    code = code.replace(target, target + "\n    page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)")
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed missing replace statement")
else:
    print("Target not found")
