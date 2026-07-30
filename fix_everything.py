import json
import re

# 1. Fix structured_copy.json for Ushuaia Investimento
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

u = data['https://natrekking.com.br/ushuaia-dez26-jan27']
u['investimento'] = [
    "Desconto para pagamento a vista via Wise fica 2.124,57 dólares",
    "Desconto para pagamento parcelado via Wise fica 2.368,26 dólares em 1+5 de 394,71 dólares",
    "Desconto para pagamento a vista no Pix fica R$ 11.520,97",
    "Desconto para pagamento parcelado no Pix fica R$ 12.431,35 em 1+5 de R$ 2.071,89",
    "Fica R$ 13.010,68 em até 12 vezes sem juros",
    "(12 de R$ 1.084,22 aprox)"
]

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# 2. Fix style.css timeline opacity
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make timeline items visible by default just in case GSAP fails
css = css.replace('opacity: 0;\n\n    transform: translateY(20px);', 'opacity: 1;\n\n    transform: translateY(0);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 3. Fix generate_unified.py hero tags
with open('generate_unified.py', 'r', encoding='utf-8') as f:
    gen = f.read()

gen = gen.replace("page_html = page_html.replace('{{ HERO_IMAGE }}', img_path)", 
                  "page_html = page_html.replace('{{ BACKGROUND_IMG }}', img_path)\n    page_html = page_html.replace('..//public', '..') # safety")
gen = gen.replace("page_html = page_html.replace('{{ LOCATION }}', exp.get('loc', ''))",
                  "page_html = page_html.replace('{{ LOC }}', exp.get('loc', ''))")
gen = gen.replace("page_html = page_html.replace('{{ DURATION }}', exp.get('dur', ''))",
                  "page_html = page_html.replace('{{ DUR }}', exp.get('dur', ''))")

# For elevation, the template has {{ ELEVATION_BLOCK }}. Let's generate it properly.
old_elevation = "page_html = page_html.replace('{{ ELEVATION }}', exp.get('elevation', ''))"
new_elevation = """elevation_val = exp.get('elevation', 'Consultar')
    if elevation_val and elevation_val != 'N/A' and elevation_val != 'Consultar':
        elevation_html = f'''<div class="meta-item">
            <span class="meta-label">Elevação</span>
            <span class="meta-value">{elevation_val}</span>
        </div>'''
    else:
        elevation_html = ''
    page_html = page_html.replace('{{ ELEVATION_BLOCK }}', elevation_html)"""

gen = gen.replace(old_elevation, new_elevation)

with open('generate_unified.py', 'w', encoding='utf-8') as f:
    f.write(gen)

print("Everything fixed in scripts!")
