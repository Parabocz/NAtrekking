import re

with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

if '{{ ATENCAO_CONTENT }}' not in text:
    text = text.replace('{{ TIMELINE_CONTENT }}', '{{ ATENCAO_CONTENT }}\n                    {{ TIMELINE_CONTENT }}')
    with open('template_expedicao.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('ATENCAO_CONTENT added to template')

with open('generate_unified.py', 'r', encoding='utf-8') as f:
    code = f.read()

if 'atencao_content = buckets.get' not in code:
    replacement = '''
    atencao_content = buckets.get('atencao', '')
    if isinstance(atencao_content, list):
        atencao_content = "".join(f"<p>{p}</p>" for p in atencao_content)
    
    page_html = page_html.replace('{{ ATENCAO_CONTENT }}', atencao_content)
    page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_html)
    '''
    code = code.replace("page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_html)", replacement)
    
    with open('generate_unified.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print('atencao replace added to generator')
