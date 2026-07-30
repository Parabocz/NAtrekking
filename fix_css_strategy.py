import os
import sys
import re
from bs4 import BeautifulSoup

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

# We need to find the block where wix_html is built
# and change it to save styles to public/wix_{filename}.css
# Then inject <link rel="stylesheet" href="/wix_{filename}.css">

# Let's write a script that completely replaces the wix block
old_block = '''    wix_html = ""
    if 'wix_static' in buckets:
        import os
        from bs4 import BeautifulSoup
        wix_path = buckets['wix_static']
        if os.path.exists(wix_path):
            with open(wix_path, 'r', encoding='utf-8') as wf:
                wsoup = BeautifulSoup(wf.read(), 'html.parser')
                styles = ''.join([str(s) for s in wsoup.head.find_all('style')])
                site_pages = wsoup.find(id='SITE_PAGES')
                if site_pages:
                    wix_html = styles + str(site_pages)
                    wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)
                    wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)
                else:
                    wix_html = styles + ''.join([str(c) for c in wsoup.body.children if c.name != 'script'])
                    wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)
                    wix_html = re.sub(r'--([a-zA-Z0-9_]+)\s*-\s*([a-zA-Z0-9_]+)', r'--\1-\2', wix_html)
    
    page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)'''

new_block = '''    wix_html = ""
    if 'wix_static' in buckets:
        import os
        from bs4 import BeautifulSoup
        wix_path = buckets['wix_static']
        if os.path.exists(wix_path):
            with open(wix_path, 'r', encoding='utf-8') as wf:
                wsoup = BeautifulSoup(wf.read(), 'html.parser')
                
                # Extract all styles
                style_tags = wsoup.head.find_all('style')
                styles_content = ""
                for s in style_tags:
                    styles_content += s.string if s.string else ""
                
                # Save styles to public directory to bypass Vite processing
                os.makedirs('public/wix', exist_ok=True)
                css_filename = f"wix_{exp['filename'].replace('.html', '.css')}"
                css_path = os.path.join('public', 'wix', css_filename)
                
                with open(css_path, 'w', encoding='utf-8') as cssf:
                    cssf.write(styles_content)
                
                # Inject a link tag instead of inline styles
                link_tag = f'<link rel="stylesheet" href="/wix/{css_filename}">'
                
                site_pages = wsoup.find(id='SITE_PAGES')
                if site_pages:
                    wix_html = link_tag + str(site_pages)
                else:
                    wix_html = link_tag + ''.join([str(c) for c in wsoup.body.children if c.name != 'script'])
    
    page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)'''

if old_block in code:
    code = code.replace(old_block, new_block)
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully updated generator to use public CSS files.")
else:
    print("Old block not found!")
    # Let's try a regex fallback just in case spaces don't match
    import re
    match = re.search(r'wix_html = "".*?page_html = page_html\.replace\(\'\{\{ WIX_STATIC_HTML \}\}\', wix_html\)', code, re.DOTALL)
    if match:
        code = code[:match.start()] + new_block + code[match.end():]
        with open('generate_unified.py', 'w', encoding='utf-8') as f:
            f.write(code)
        print("Successfully updated generator to use public CSS files using regex fallback.")
    else:
        print("Fallback failed too.")
