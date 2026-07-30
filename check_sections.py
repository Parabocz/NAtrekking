import re
with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section class="(.*?)"', text)
print('SECTIONS:', sections)
