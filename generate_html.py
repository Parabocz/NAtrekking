import os
import re

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def generate_cards(category_prefix, count):
    cards = []
    for i in range(1, count + 1):
        image_name = f"{category_prefix}_{i}.jpg"
        card = f'''        <div class="list-card">
            <div class="list-card-img" style="background-image: url('public/{image_name}');">
                <div class="list-card-badge">{i}</div>
            </div>
            <div class="list-card-content">
                <h3 class="list-card-title">Expedição {category_prefix.replace("_", " ").title()} {i}</h3>
                <p class="list-card-duration">Duração: X DIAS</p>
                <p class="list-card-desc">Descrição da expedição {category_prefix} {i}. Preencha com os dados reais da agenda.</p>
                <div class="list-card-footer">
                    <span>Próxima turma: <strong>A definir</strong></span>
                    <a href="#" class="list-card-next">Ver detalhes ↗</a>
                </div>
            </div>
        </div>'''
        cards.append(card)
    return "\n".join(cards)

nacional_html = generate_cards("agenda_nacional", 10)
internacional_html = generate_cards("agenda_internacional", 10)
alta_montanha_html = generate_cards("alta_montanha", 10)
cursos_html = generate_cards("curso_trekking", 2)

# We need to replace the contents inside each <div class="catalog-list" id="X">
content = re.sub(r'(<div class="catalog-list" id="nacionais">).*?(</div>\s*<!-- \.catalog-list -->)', r'\1\n' + nacional_html + r'\n\2', content, flags=re.DOTALL)
content = re.sub(r'(<div class="catalog-list" id="internacionais" style="display: none;">).*?(</div>\s*<!-- \.catalog-list -->)', r'\1\n' + internacional_html + r'\n\2', content, flags=re.DOTALL)
content = re.sub(r'(<div class="catalog-list" id="alta-montanha" style="display: none;">).*?(</div>\s*<!-- \.catalog-list -->)', r'\1\n' + alta_montanha_html + r'\n\2', content, flags=re.DOTALL)

# Add the 4th category section. Let's find where the buttons are to add the 4th button.
btn_html = r'<button class="catalog-tab" data-target="cursos">Cursos de Trekking</button>\n            </div>'
content = re.sub(r'</div>\s*<!-- End Tabs -->', btn_html + '\n        <!-- End Tabs -->', content)

# And add the container for the 4th category after the Alta Montanha container
curso_container = f'''
        <div class="catalog-list" id="cursos" style="display: none;">
{cursos_html}
        </div>
        <!-- .catalog-list -->
'''
content = re.sub(r'(<div class="catalog-list" id="alta-montanha" style="display: none;">.*?</div>\s*<!-- \.catalog-list -->)', r'\1' + curso_container, content, flags=re.DOTALL)


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
