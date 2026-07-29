import os
import re

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

data = [
    # Internacional & Montanha
    {"title": "Vulcões do Equador", "dates": "16 a 25/set/2026", "loc": "Equador", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_1.jpg", "link": None, "sort_date": "2026-09-16"},
    {"title": "Kilimanjaro 2026", "dates": "04 a 13/out/2026", "loc": "Tanzânia", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/kilimanjaro2026", "sort_date": "2026-10-04"},
    {"title": "Kilimanjaro + Safari 2026", "dates": "04 a 16/out/2026", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_3.jpg", "link": "https://natrekking.com.br/kilimanjarosafari2026", "sort_date": "2026-10-04"},
    {"title": "Kilimanjaro + Safari 2027", "dates": "04 a 16/out/2027", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_4.jpg", "link": "https://natrekking.com.br/kilimanjaro-safari-2027", "sort_date": "2027-10-04"},
    {"title": "Monte Roraima", "dates": "20 a 29/nov/2026", "loc": "Tríplice fronteira Brasil/Venezuela/Guiana", "dur": "10 dias", "cats": ["internacional"], "img": "public/agenda_internacional_5.jpg", "link": "https://natrekking.com.br/roraimanov2026", "sort_date": "2026-11-20"},
    {"title": "Patagônia Especial (Réveillon)", "dates": "27/dez/2026 a 13/jan/2027", "loc": "Argentina e Chile (Ushuaia, Punta Arenas, Puerto Natales, El Calafate, El Chaltén)", "dur": "18 dias", "cats": ["internacional"], "img": "public/agenda_internacional_6.jpg", "link": "https://natrekking.com.br/patagonia-especial", "sort_date": "2026-12-27"},
    {"title": "Ushuaia", "dates": "27/dez/2026 a 02/jan/2027", "loc": "Argentina (Ushuaia)", "dur": "7 dias/6 noites", "cats": ["internacional"], "img": "public/agenda_internacional_7.jpg", "link": "https://natrekking.com.br/ushuaia-dez26-jan27", "sort_date": "2026-12-27"},
    {"title": "Patagônia Chilena", "dates": "02 a 07/jan/2027", "loc": "Chile (Punta Arenas e Puerto Natales)", "dur": "6 dias", "cats": ["internacional"], "img": "public/agenda_internacional_8.jpg", "link": "https://natrekking.com.br/patagoniachilenaespecial", "sort_date": "2027-01-02"},
    {"title": "Patagônia Argentina", "dates": "07 a 13/jan/2027", "loc": "Argentina (El Calafate/Chaltén)", "dur": "7 dias", "cats": ["internacional"], "img": "public/agenda_internacional_9.jpg", "link": "https://natrekking.com.br/calafate-chalten-especial", "sort_date": "2027-01-07"},
    {"title": "Vulcões do Atacama", "dates": "08 a 18/jan/2027", "loc": "Chile (Deserto do Atacama/São Pedro do Atacama)", "dur": "11 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_10.jpg", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27", "sort_date": "2027-01-08"},
    {"title": "Torres del Paine", "dates": "12 a 22/mar/2027", "loc": "Chile (Puerto Natales)", "dur": "11 dias (8 de circuito)", "cats": ["internacional"], "img": "public/agenda_internacional_1.jpg", "link": "https://natrekking.com.br/torresdelpaineo2027", "sort_date": "2027-03-12"},
    {"title": "Cruce de Los Andes", "dates": "20 a 27/mar/2027", "loc": "Argentina e Chile", "dur": "8 dias", "cats": ["internacional"], "img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/crucedelosandes2027", "sort_date": "2027-03-20"},

    # Nacional & Cursos
    {"title": "Trekking Rinoceronte", "dates": "01 e 02/ago/2026", "loc": "SC (saída Curitiba/Joinville)", "dur": "2 dias", "cats": ["nacional"], "img": "public/agenda_nacional_5.jpg", "link": "https://natrekking.com.br/rinoceronte", "sort_date": "2026-08-01"},
    {"title": "Hiking Torre da Prata", "dates": "15/ago/2026", "loc": "PR (saída Joinville)", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_6.jpg", "link": "https://natrekking.com.br/torredaprata", "sort_date": "2026-08-15"},
    {"title": "Lençóis Maranhenses (ago/2026)", "dates": "15 a 21/ago/2026", "loc": "MA (saída São Luís)", "dur": "7 dias", "cats": ["nacional"], "img": "public/agenda_nacional_8.jpg", "link": "https://natrekking.com.br/lencoismaranhensesagosto2026", "sort_date": "2026-08-15"},
    {"title": "Pedra do Cantagalo", "dates": "22/ago/2026", "loc": "SC (saída Joinville)", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_7.jpg", "link": "https://natrekking.com.br/cantagalo", "sort_date": "2026-08-22"},
    {"title": "Curso de Trekking (agosto)", "dates": "29 e 30/ago/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/curso_trekking_2.jpg", "link": "https://natrekking.com.br/curso-de-trekking-agosto", "sort_date": "2026-08-29"},
    {"title": "Espraiado x Soldados", "dates": "5 a 7/set/2026", "loc": "SC (saída Curitiba/Joinville)", "dur": "3 dias", "cats": ["nacional"], "img": "public/agenda_nacional_10.jpg", "link": "https://natrekking.com.br/espraiadoxsoldados", "sort_date": "2026-09-05"},
    {"title": "Travessia Araçá x Crista", "dates": "05 a 08/set/2026", "loc": "PR e SC (saída Joinville)", "dur": "4 dias", "cats": ["nacional"], "img": "public/agenda_nacional_1.jpg", "link": "https://natrekking.com.br/travessiaaracaxcrista", "sort_date": "2026-09-05"},
    {"title": "Travessia Picos de Jaraguá", "dates": "12/set/2026", "loc": "SC (saída Curitiba/Joinville)", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_1.jpg", "link": "https://natrekking.com.br/travpicosdejaragua", "sort_date": "2026-09-12"},
    {"title": "Fenda Cruz de Pedra", "dates": "13/set/2026", "loc": "SC (saída Joinville)", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_2.jpg", "link": "https://natrekking.com.br/fendacruzdepedra", "sort_date": "2026-09-13"},
    {"title": "Curso de Trekking (setembro)", "dates": "26 e 27/set/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/curso_trekking_1.jpg", "link": "https://natrekking.com.br/curso-de-trekking-setembro", "sort_date": "2026-09-26"},
    {"title": "Lençóis Maranhenses (jul/2027)", "dates": "11 a 17/jul/2027", "loc": "MA (São Luís, Barreirinhas, Atins, Santo Amaro)", "dur": "7 dias", "cats": ["nacional"], "img": "public/agenda_nacional_4.jpg", "link": "https://natrekking.com.br/lencois-maranhenses-jul-27", "sort_date": "2027-07-11"},
]

# Sort the data by sort_date
data.sort(key=lambda x: x['sort_date'])

cards = []
for item in data:
    title = item['title']
    link = item['link']
    img = item['img']
    dates = item['dates'].upper()
    loc = item['loc'].upper()
    dur = item['dur'].upper()
    cats_str = " ".join(item['cats'])
    
    if not link:
        cta_html = f'''<span class="list-card-next">Link em breve</span>'''
    else:
        cta_html = f'''<a href="{link}" target="_blank" class="list-card-next" style="text-decoration: none; color: var(--color-accent); font-weight: 600;">Ver detalhes ↗</a>'''

    card = f'''                            <div class="list-card filterable-card" data-category="{cats_str}">
                                <div class="list-card-img" style="background-image: url('{img}');"></div>
                                <div class="list-card-content">
                                    <h4 class="list-card-title">{title}</h4>
                                    <div class="list-card-tags">
                                        <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg> <span class="tag-text">{dates}</span></span>
                                        <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> <span class="tag-text">{loc}</span></span>
                                        <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> <span class="tag-text">{dur}</span></span>
                                    </div>
                                    <p class="list-card-desc">Acesse para mais informações, roteiro completo e para garantir sua vaga.</p>
                                    <div class="list-card-footer">
                                        {cta_html}
                                    </div>
                                </div>
                            </div>'''
    cards.append(card)

unified_html = "\n".join(cards)

new_catalog = f'''<div class="catalog-container">
                    <div class="catalog-filters">
                        <select id="catalog-filter-select" class="catalog-select">
                            <option value="all">Todos</option>
                            <option value="nacional">Agenda Nacional</option>
                            <option value="internacional">Agenda Internacional</option>
                            <option value="montanha">Alta Montanha</option>
                            <option value="cursos">Cursos Trekking</option>
                        </select>
                    </div>
                    <div class="catalog-list unified-list">
{unified_html}
                    </div>
                </div>'''

# Sub no content
pattern = r'<div class="catalog-container">.*?</div>\s*</div>\s*</section>'
replacement = new_catalog + '\n            </div>\n        </section>'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done generating unified layout!")
