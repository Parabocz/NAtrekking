import os
import re

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def generate_cards(items, category):
    cards = []
    for i, item in enumerate(items):
        title = item['title']
        link = item['link']
        img = item['img']
        
        if not link:
            cta_html = f'''<span class="list-card-next">Link em breve</span>'''
        else:
            cta_html = f'''<a href="{link}" target="_blank" class="list-card-next" style="text-decoration: none; color: var(--color-accent); font-weight: 600;">Ver detalhes ↗</a>'''

        card = f'''                            <div class="list-card">
                                <div class="list-card-img" style="background-image: url('{img}');"></div>
                                <div class="list-card-content">
                                    <h4 class="list-card-title">{title}</h4>
                                    <p class="list-card-duration">A DEFINIR</p>
                                    <p class="list-card-desc">Acesse para mais informações, datas disponíveis e roteiro completo.</p>
                                    <div class="list-card-footer">
                                        {cta_html}
                                    </div>
                                </div>
                            </div>'''
        cards.append(card)
    return "\n".join(cards)

internacional_items = [
    {"title": "Vulcões do Equador", "link": None, "img": "public/agenda_internacional_1.jpg"},
    {"title": "Kilimanjaro (2026)", "link": "https://natrekking.com.br/kilimanjaro2026", "img": "public/agenda_internacional_2.jpg"},
    {"title": "Kilimanjaro + Safari (2026)", "link": "https://natrekking.com.br/kilimanjarosafari2026", "img": "public/agenda_internacional_3.jpg"},
    {"title": "Kilimanjaro + Safari (2027)", "link": "https://natrekking.com.br/kilimanjaro-safari-2027", "img": "public/agenda_internacional_4.jpg"},
    {"title": "Monte Roraima", "link": "https://natrekking.com.br/roraimanov2026", "img": "public/agenda_internacional_5.jpg"},
    {"title": "Patagônia Especial (Réveillon)", "link": "https://natrekking.com.br/patagonia-especial", "img": "public/agenda_internacional_6.jpg"},
    {"title": "Ushuaia", "link": "https://natrekking.com.br/ushuaia-dez26-jan27", "img": "public/agenda_internacional_7.jpg"},
    {"title": "Patagônia Chilena", "link": "https://natrekking.com.br/patagoniachilenaespecial", "img": "public/agenda_internacional_8.jpg"},
    {"title": "Patagônia Argentina", "link": "https://natrekking.com.br/calafate-chalten-especial", "img": "public/agenda_internacional_9.jpg"},
    {"title": "Vulcões do Atacama", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27", "img": "public/agenda_internacional_10.jpg"},
    {"title": "Torres del Paine", "link": "https://natrekking.com.br/torresdelpaineo2027", "img": "public/agenda_internacional_1.jpg"},
    {"title": "Cruce de Los Andes", "link": "https://natrekking.com.br/crucedelosandes2027", "img": "public/agenda_internacional_2.jpg"}
]

nacional_items = [
    {"title": "Travessia Picos de Jaraguá", "link": "https://natrekking.com.br/travpicosdejaragua", "img": "public/agenda_nacional_1.jpg"},
    {"title": "Fenda Cruz de Pedra", "link": "https://natrekking.com.br/fendacruzdepedra", "img": "public/agenda_nacional_2.jpg"},
    {"title": "Curso de Trekking (setembro)", "link": "https://natrekking.com.br/curso-de-trekking-setembro", "img": "public/curso_trekking_1.jpg"},
    {"title": "Lençóis Maranhenses (jul/2027)", "link": "https://natrekking.com.br/lencois-maranhenses-jul-27", "img": "public/agenda_nacional_4.jpg"},
    {"title": "Trekking Rinoceronte", "link": "https://natrekking.com.br/rinoceronte", "img": "public/agenda_nacional_5.jpg"},
    {"title": "Hiking Torre da Prata", "link": "https://natrekking.com.br/torredaprata", "img": "public/agenda_nacional_6.jpg"},
    {"title": "Pedra do Cantagalo", "link": "https://natrekking.com.br/cantagalo", "img": "public/agenda_nacional_7.jpg"},
    {"title": "Lençóis Maranhenses (ago/2026)", "link": "https://natrekking.com.br/lencoismaranhensesagosto2026", "img": "public/agenda_nacional_8.jpg"},
    {"title": "Curso de Trekking (agosto)", "link": "https://natrekking.com.br/curso-de-trekking-agosto", "img": "public/curso_trekking_2.jpg"},
    {"title": "Espraiado x Soldados", "link": "https://natrekking.com.br/espraiadoxsoldados", "img": "public/agenda_nacional_10.jpg"},
    {"title": "Travessia Araça x Crista", "link": "https://natrekking.com.br/travessiaaracaxcrista", "img": "public/agenda_nacional_1.jpg"}
]

alta_montanha_items = [
    {"title": "Vulcões do Equador", "link": None, "img": "public/agenda_internacional_1.jpg"},
    {"title": "Kilimanjaro (2026)", "link": "https://natrekking.com.br/kilimanjaro2026", "img": "public/agenda_internacional_2.jpg"},
    {"title": "Kilimanjaro + Safari (2026)", "link": "https://natrekking.com.br/kilimanjarosafari2026", "img": "public/agenda_internacional_3.jpg"},
    {"title": "Vulcões do Atacama", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27", "img": "public/agenda_internacional_10.jpg"},
    {"title": "Kilimanjaro + Safari (2027)", "link": "https://natrekking.com.br/kilimanjaro-safari-2027", "img": "public/agenda_internacional_4.jpg"}
]

cursos_items = [
    {"title": "Curso de Trekking - agosto (29 e 30/08/2026)", "link": "https://natrekking.com.br/curso-de-trekking-agosto", "img": "public/curso_trekking_2.jpg"},
    {"title": "Curso de Trekking - setembro (26 e 27/09)", "link": "https://natrekking.com.br/curso-de-trekking-setembro", "img": "public/curso_trekking_1.jpg"}
]

nacional_html = generate_cards(nacional_items, "nacional")
internacional_html = generate_cards(internacional_items, "internacional")
alta_montanha_html = generate_cards(alta_montanha_items, "montanha")
cursos_html = generate_cards(cursos_items, "cursos")

# To be safe, we will just construct the entire catalog-container from scratch
# instead of relying on fragile regex matching.
# We just replace everything between <div class="catalog-container"> and the closing </div> of that container.

new_catalog = f'''<div class="catalog-container">
                    <!-- CATEGORY 1: Nacional -->
                    <div class="catalog-row" data-category="nacional">
                        <h3 class="row-title">Em Alta: Clássicos Nacionais</h3>
                        <div class="catalog-list">
{nacional_html}
                        </div>
                    </div>

                    <!-- CATEGORY 2: Internacional -->
                    <div class="catalog-row" data-category="internacional">
                        <h3 class="row-title">Fronteiras: Expedições Internacionais</h3>
                        <div class="catalog-list">
{internacional_html}
                        </div>
                    </div>

                    <!-- CATEGORY 3: Alta Montanha -->
                    <div class="catalog-row" data-category="montanha">
                        <h3 class="row-title">Lançamentos: Alta Montanha</h3>
                        <div class="catalog-list">
{alta_montanha_html}
                        </div>
                    </div>

                    <!-- CATEGORY 4: Cursos -->
                    <div class="catalog-row" data-category="cursos">
                        <h3 class="row-title">Formação: Cursos de Trekking</h3>
                        <div class="catalog-list">
{cursos_html}
                        </div>
                    </div>
                </div>'''

# Match exactly the <div class="catalog-container"> ... </div> right before </div> </section>
pattern = r'<div class="catalog-container">.*?</div>\s*</div>\s*</section>'
replacement = new_catalog + '\n            </div>\n        </section>'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done building the new structure!")
