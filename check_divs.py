import re
with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    text = f.read()

divs = re.findall(r'<div class="(.*?)"', text)
print('DIV CLASSES:')
for d in list(dict.fromkeys(divs)):
    print('-', d)
