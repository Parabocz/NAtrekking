import sys

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

if 'import re' not in code:
    code = 'import re\n' + code

broken1 = "wix_html = styles + str(site_pages)"
fixed1 = "wix_html = styles + str(site_pages)\n                    wix_html = re.sub(r'--alpha\\s+-', '--alpha-', wix_html)"

broken2 = "wix_html = styles + ''.join([str(c) for c in wsoup.body.children if c.name != 'script'])"
fixed2 = "wix_html = styles + ''.join([str(c) for c in wsoup.body.children if c.name != 'script'])\n                    wix_html = re.sub(r'--alpha\\s+-', '--alpha-', wix_html)"

code = code.replace(broken1, fixed1)
code = code.replace(broken2, fixed2)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed CSS regex in generator")
