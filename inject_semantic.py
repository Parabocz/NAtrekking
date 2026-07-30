import os
import sys
import re
from bs4 import BeautifulSoup

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

# We will completely replace the wix_html generation logic with a semantic extractor
import re
# Regex to find the block
match = re.search(r'(wix_html = "".*?)page_html = page_html\.replace\(\'\{\{ WIX_STATIC_HTML \}\}\', wix_html\)', code, re.DOTALL)

if match:
    old_logic = match.group(1)
    
    new_logic = '''wix_html = ""
    if 'wix_static' in buckets:
        import os
        from bs4 import BeautifulSoup
        wix_path = buckets['wix_static']
        if os.path.exists(wix_path):
            with open(wix_path, 'r', encoding='utf-8') as wf:
                wsoup = BeautifulSoup(wf.read(), 'html.parser')
                
                # Semantic Text Extractor
                site_pages = wsoup.find(id='SITE_PAGES')
                if not site_pages:
                    site_pages = wsoup.body
                
                blocks = []
                # Traverse and extract meaningful text
                for el in site_pages.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']):
                    text = el.get_text(strip=True)
                    if not text: continue
                    
                    # Avoid duplicated nested spans
                    if blocks and (text in blocks[-1] or blocks[-1] in text):
                        # If the new text is longer (e.g. parent p containing span), replace it
                        if len(text) > len(blocks[-1]):
                            blocks[-1] = text
                        continue
                    
                    blocks.append(text)
                
                # Render clean HTML
                clean_html = '<div class="container" style="max-width: 900px; margin: 4rem auto; padding: 0 2rem;">'
                
                for b in blocks:
                    # Very short lines might be headers or labels
                    if len(b) < 30 and b.istitle():
                        clean_html += f'<h3 style="color: var(--accent); margin-top: 2rem; margin-bottom: 0.5rem; font-size: 1.5rem;">{b}</h3>'
                    elif len(b) < 50:
                        clean_html += f'<h4 style="color: var(--text-white); margin-top: 1.5rem; margin-bottom: 0.5rem; font-size: 1.2rem; font-weight: 600;">{b}</h4>'
                    else:
                        clean_html += f'<p style="color: var(--text-gray); line-height: 1.8; margin-bottom: 1rem; font-size: 1.1rem;">{b}</p>'
                
                clean_html += '</div>'
                wix_html = clean_html
    
    '''
    
    code = code[:match.start()] + new_logic + code[match.end():]
    code = code.replace("page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)", "page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)\n")
    
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Semantic extractor injected.")
else:
    print("Could not find the block to replace.")
