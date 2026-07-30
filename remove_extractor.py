import re

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Match from wix_html = "" up to the line page_html = page_html.replace('{{ WIX_STATIC_HTML }}', wix_html)
code = re.sub(r'wix_html = "".*?page_html = page_html\.replace\(\'\{\{ WIX_STATIC_HTML \}\}\', wix_html\)', '', code, flags=re.DOTALL)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(code)
print('Semantic extractor removed')
