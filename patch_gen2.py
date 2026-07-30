import sys

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

injection = '''
    wix_html = ""
    if 'wix_static' in content:
        import os
        from bs4 import BeautifulSoup
        wix_path = content['wix_static']
        if os.path.exists(wix_path):
            with open(wix_path, 'r', encoding='utf-8') as wf:
                wsoup = BeautifulSoup(wf.read(), 'html.parser')
                styles = ''.join([str(s) for s in wsoup.head.find_all('style')])
                site_pages = wsoup.find(id='SITE_PAGES')
                if site_pages:
                    wix_html = styles + str(site_pages)
                else:
                    wix_html = styles + ''.join([str(c) for c in wsoup.body.children if c.name != 'script'])
    
    page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)
'''

replace_target = "page_html = page_html.replace('{{ POLITICA_CONTENT }}', politica_html)"

if replace_target in code:
    new_code = code.replace(replace_target, replace_target + '\n' + injection)
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(new_code)
    print('Patched generate_unified.py')
else:
    print('Target not found')
