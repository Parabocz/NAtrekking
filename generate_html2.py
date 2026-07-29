import os
import re

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def generate_cards(category_prefix, count):
    cards = []
    for i in range(1, count + 1):
        image_name = f"{category_prefix}_{i}.jpg"
        card = f'''                            <div class="list-card">
                                <div class="list-card-img" style="background-image: url('public/{image_name}');"></div>
                                <div class="list-card-content">
                                    <h4 class="list-card-title">Expedição {category_prefix.replace("_", " ").title()} {i}</h4>
                                    <p class="list-card-duration">X DIAS</p>
                                    <p class="list-card-desc">Descrição temporária. Preencha com os dados reais.</p>
                                    <div class="list-card-footer">
                                        <span class="list-card-next">Próxima: <strong>A definir</strong></span>
                                    </div>
                                </div>
                            </div>'''
        cards.append(card)
    return "\n".join(cards)

nacional_html = generate_cards("agenda_nacional", 10)
internacional_html = generate_cards("agenda_internacional", 10)
alta_montanha_html = generate_cards("alta_montanha", 10)
cursos_html = generate_cards("curso_trekking", 2)

# Replace contents of Nacional
content = re.sub(
    r'(<div class="catalog-row" data-category="nacional">\s*<h3 class="row-title">[^<]+</h3>\s*<div class="catalog-list">).*?(</div>\s*</div>)',
    r'\1\n' + nacional_html + r'\n\2',
    content,
    flags=re.DOTALL
)

# Replace contents of Internacional
content = re.sub(
    r'(<div class="catalog-row" data-category="internacional">\s*<h3 class="row-title">[^<]+</h3>\s*<div class="catalog-list">).*?(</div>\s*</div>)',
    r'\1\n' + internacional_html + r'\n\2',
    content,
    flags=re.DOTALL
)

# Replace contents of Alta Montanha
content = re.sub(
    r'(<div class="catalog-row" data-category="montanha">\s*<h3 class="row-title">[^<]+</h3>\s*<div class="catalog-list">).*?(</div>\s*</div>)',
    r'\1\n' + alta_montanha_html + r'\n\2',
    content,
    flags=re.DOTALL
)

# Add Cursos right after Alta Montanha
curso_section = f'''

                    <!-- CATEGORY 4 -->
                    <div class="catalog-row" data-category="cursos">
                        <h3 class="row-title">Formação: Cursos de Trekking</h3>
                        <div class="catalog-list">
{cursos_html}
                        </div>
                    </div>
'''
content = re.sub(
    r'(<div class="catalog-row" data-category="montanha">.*?</div>\s*</div>)',
    r'\1' + curso_section,
    content,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
