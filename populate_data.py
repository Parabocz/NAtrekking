import os
import re

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def get_image(category, index):
    return f"public/agenda_{category}_{((index-1) % 10) + 1}.jpg"

def generate_cards(items, category):
    cards = []
    for i, item in enumerate(items):
        title = item['title']
        link = item['link']
        img = item.get('img', get_image(category, i + 1))
        
        # Link / CTA
        if not link:
            cta_html = f'''<span class="list-card-next">Link em breve</span>'''
            link_wrapper_start = ""
            link_wrapper_end = ""
        else:
            cta_html = f'''<a href="{link}" target="_blank" class="list-card-next">Ver detalhes ↗</a>'''
            # If we want the whole card clickable, but usually CTA is enough. Let's make the CTA link.

        card = f'''                            <div class="list-card">
                                <div class="list-card-img" style="background-image: url('{img}');"></div>
                                <div class="list-card-content">
                                    <h4 class="list-card-title">{title}</h4>
                                    <p class="list-card-duration">A DEFINIR</p>
                                    <p class="list-card-desc">Mais informações na página oficial.</p>
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

# Replace contents of Cursos
content = re.sub(
    r'(<div class="catalog-row" data-category="cursos">\s*<h3 class="row-title">[^<]+</h3>\s*<div class="catalog-list">).*?(</div>\s*</div>)',
    r'\1\n' + cursos_html + r'\n\2',
    content,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done generating actual data!")
