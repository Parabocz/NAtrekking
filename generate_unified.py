import os
import json

data = [
# Internacional & Montanha
{"title": "Vulcões do Equador", "dates": "16 a 25/set/2026", "loc": "Equador", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/equador_hero_1785360532710.jpg", "link": None, "sort_date": "2026-09-16", "elevation": "5.897m", "difficulty": "Alta", "filename": "vulcoes-do-equador.html", "url": None},
{"title": "Kilimanjaro 2026", "dates": "04 a 13/out/2026", "loc": "Tanzânia", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/kilimanjaro_hero_1785360543579.jpg", "link": "https://natrekking.com.br/kilimanjaro2026", "sort_date": "2026-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-2026.html", "url": "https://natrekking.com.br/kilimanjaro2026"},
{"title": "Kilimanjaro + Safari 2026", "dates": "04 a 16/out/2026", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/kilimanjaro_safari_hero_1785360555337.jpg", "link": "https://natrekking.com.br/kilimanjarosafari2026", "sort_date": "2026-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-safari-2026.html", "url": "https://natrekking.com.br/kilimanjarosafari2026"},
{"title": "Kilimanjaro + Safari 2027", "dates": "04 a 16/out/2027", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/alta_montanha_10.jpg", "link": "https://natrekking.com.br/kilimanjaro-safari-2027", "sort_date": "2027-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-safari-2027.html", "url": "https://natrekking.com.br/kilimanjaro-safari-2027"},
{"title": "Monte Roraima", "dates": "20 a 29/nov/2026", "loc": "Tríplice fronteira Brasil/Venezuela/Guiana", "dur": "10 dias", "cats": ["internacional"], "img": "public/roraima_hero_1785360565465.jpg", "link": "https://natrekking.com.br/roraimanov2026", "sort_date": "2026-11-20", "elevation": "2.810m", "difficulty": "Alta", "filename": "monte-roraima.html", "url": "https://natrekking.com.br/roraimanov2026"},
{"title": "Patagônia Especial (Réveillon)", "dates": "27/dez/2026 a 13/jan/2027", "loc": "Argentina e Chile", "dur": "18 dias", "cats": ["internacional"], "img": "public/patagonia_reveillon_hero_1785360574602.jpg", "link": "https://natrekking.com.br/patagonia-especial", "sort_date": "2026-12-27", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-especial-reveillon.html", "url": "https://natrekking.com.br/patagonia-especial"},
{"title": "Ushuaia", "dates": "27/dez/2026 a 02/jan/2027", "loc": "Argentina (Ushuaia)", "dur": "7 dias", "cats": ["internacional"], "img": "public/ushuaia_hero_1785360593447.jpg", "link": "https://natrekking.com.br/ushuaia-dez26-jan27", "sort_date": "2026-12-27", "elevation": "Consultar", "difficulty": "Moderada", "filename": "ushuaia.html", "url": "https://natrekking.com.br/ushuaia-dez26-jan27"},
{"title": "Patagônia Chilena", "dates": "02 a 07/jan/2027", "loc": "Chile (Punta Arenas e Puerto Natales)", "dur": "6 dias", "cats": ["internacional"], "img": "public/patagonia_chilena_hero_1785360603284.jpg", "link": "https://natrekking.com.br/patagoniachilenaespecial", "sort_date": "2027-01-02", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-chilena.html", "url": "https://natrekking.com.br/patagoniachilenaespecial"},
{"title": "Patagônia Argentina", "dates": "07 a 13/jan/2027", "loc": "Argentina (El Calafate/Chaltén)", "dur": "7 dias", "cats": ["internacional"], "img": "public/patagonia_argentina_hero_1785360613356.jpg", "link": "https://natrekking.com.br/calafate-chalten-especial", "sort_date": "2027-01-07", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-argentina.html", "url": "https://natrekking.com.br/calafate-chalten-especial"},
{"title": "Vulcões do Atacama", "dates": "08 a 18/jan/2027", "loc": "Chile (Deserto do Atacama)", "dur": "11 dias", "cats": ["internacional", "montanha"], "img": "public/atacama_hero_1785360644849.jpg", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27", "sort_date": "2027-01-08", "elevation": "5.920m", "difficulty": "Muito Alta", "filename": "vulcoes-do-atacama.html", "url": "https://natrekking.com.br/vulcões-do-atacama-jan-27"},
{"title": "Torres del Paine", "dates": "12 a 22/mar/2027", "loc": "Chile (Puerto Natales)", "dur": "11 dias", "cats": ["internacional"], "img": "public/torres_paine_hero_1785360623634.jpg", "link": "https://natrekking.com.br/torresdelpaineo2027", "sort_date": "2027-03-12", "elevation": "Consultar", "difficulty": "Alta", "filename": "torres-del-paine.html", "url": "https://natrekking.com.br/torresdelpaineo2027"},
{"title": "Cruce de Los Andes", "dates": "20 a 27/mar/2027", "loc": "Argentina e Chile", "dur": "8 dias", "cats": ["internacional"], "img": "public/andes_hero_1785360668799.jpg", "link": "https://natrekking.com.br/crucedelosandes2027", "sort_date": "2027-03-20", "elevation": "Consultar", "difficulty": "Moderada", "filename": "cruce-de-los-andes.html", "url": "https://natrekking.com.br/crucedelosandes2027"},

# Nacional & Cursos
{"title": "Trekking Rinoceronte", "dates": "01 e 02/ago/2026", "loc": "SC", "dur": "2 dias", "cats": ["nacional"], "img": "public/agenda_nacional_1.jpg", "link": "https://natrekking.com.br/rinoceronte", "sort_date": "2026-08-01", "elevation": "Consultar", "difficulty": "Moderada", "filename": "trekking-rinoceronte.html", "url": "https://natrekking.com.br/rinoceronte"},
{"title": "Hiking Torre da Prata", "dates": "15/ago/2026", "loc": "PR", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_2.jpg", "link": "https://natrekking.com.br/torredaprata", "sort_date": "2026-08-15", "elevation": "Consultar", "difficulty": "Moderada", "filename": "hiking-torre-da-prata.html", "url": "https://natrekking.com.br/torredaprata"},
{"title": "Lençóis Maranhenses (ago/2026)", "dates": "15 a 21/ago/2026", "loc": "MA", "dur": "7 dias", "cats": ["nacional"], "img": "public/agenda_nacional_4.jpg", "link": "https://natrekking.com.br/lencoismaranhensesagosto2026", "sort_date": "2026-08-15", "elevation": "N/A", "difficulty": "Baixa/Moderada", "filename": "lencois-maranhenses-ago-2026.html", "url": "https://natrekking.com.br/lencoismaranhensesagosto2026"},
{"title": "Pedra do Cantagalo", "dates": "22/ago/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_3.jpg", "link": "https://natrekking.com.br/cantagalo", "sort_date": "2026-08-22", "elevation": "Consultar", "difficulty": "Moderada", "filename": "pedra-do-cantagalo.html", "url": "https://natrekking.com.br/cantagalo"},
{"title": "Curso de Trekking (agosto)", "dates": "29 e 30/ago/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/agenda_nacional_5.jpg", "link": "https://natrekking.com.br/curso-de-trekking-agosto", "sort_date": "2026-08-29", "elevation": "N/A", "difficulty": "Iniciante", "filename": "curso-trekking-agosto.html", "url": "https://natrekking.com.br/curso-de-trekking-agosto"},
{"title": "Espraiado x Soldados", "dates": "5 a 7/set/2026", "loc": "SC", "dur": "3 dias", "cats": ["nacional"], "img": "public/agenda_nacional_6.jpg", "link": "https://natrekking.com.br/espraiadoxsoldados", "sort_date": "2026-09-05", "elevation": "Consultar", "difficulty": "Alta", "filename": "espraiado-x-soldados.html", "url": "https://natrekking.com.br/espraiadoxsoldados"},
{"title": "Travessia Araça x Crista", "dates": "05 a 08/set/2026", "loc": "PR e SC", "dur": "4 dias", "cats": ["nacional"], "img": "public/agenda_nacional_7.jpg", "link": "https://natrekking.com.br/travessiaaracaxcrista", "sort_date": "2026-09-05", "elevation": "Consultar", "difficulty": "Alta", "filename": "travessia-araca-x-crista.html", "url": "https://natrekking.com.br/travessiaaracaxcrista"},
{"title": "Travessia Picos de Jaraguá", "dates": "12/set/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_8.jpg", "link": "https://natrekking.com.br/travpicosdejaragua", "sort_date": "2026-09-12", "elevation": "Consultar", "difficulty": "Alta", "filename": "travessia-picos-de-jaragua.html", "url": "https://natrekking.com.br/travpicosdejaragua"},
{"title": "Fenda Cruz de Pedra", "dates": "13/set/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_9.jpg", "link": "https://natrekking.com.br/fendacruzdepedra", "sort_date": "2026-09-13", "elevation": "Consultar", "difficulty": "Moderada", "filename": "fenda-cruz-de-pedra.html", "url": "https://natrekking.com.br/fendacruzdepedra"},
{"title": "Curso de Trekking (setembro)", "dates": "26 e 27/set/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/agenda_nacional_10.jpg", "link": "https://natrekking.com.br/curso-de-trekking-setembro", "sort_date": "2026-09-26", "elevation": "N/A", "difficulty": "Iniciante", "filename": "curso-trekking-setembro.html", "url": "https://natrekking.com.br/curso-de-trekking-setembro"},
{"title": "Lençóis Maranhenses (jul/2027)", "dates": "10 a 16/jul/2027", "loc": "MA", "dur": "7 dias", "cats": ["nacional"], "img": "public/nacional_1.jpg", "link": "https://natrekking.com.br/lencois-maranhenses-jul-27", "sort_date": "2027-07-10", "elevation": "N/A", "difficulty": "Baixa/Moderada", "filename": "lencois-maranhenses-jul-2027.html", "url": "https://natrekking.com.br/lencois-maranhenses-jul-27"}
]

# ==========================================
# 2. LOAD STRUCTURED COPY JSON
# ==========================================
with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured_copy = json.load(f)

# ==========================================
# 3. LOAD TEMPLATES
# ==========================================
with open('template_expedicao.html', 'r', encoding='utf-8') as f:
    template = f.read()

os.makedirs('expedicoes', exist_ok=True)

# ==========================================
# 4. GENERATOR LOOP
# ==========================================
for exp in data:
    if not exp.get("filename"):
        continue

    url = exp.get('url')
    buckets = structured_copy.get(url, {
        'historia': [], 'vibe': [], 'specs': [], 'cronograma': [],
        'atencao': [], 'incluso': [], 'nao_incluso': [],
        'investimento': [], 'politica': [], 'faq': []
    })

    historia_content = "".join(f"<p style='margin-bottom: 1rem;'>{p}</p>" for p in buckets['historia']) if buckets['historia'] else "<p>Detalhes completos em breve.</p>"
    vibe_content = "".join(f"<p style='margin-bottom: 1rem;'>{p}</p>" for p in buckets['vibe']) if buckets['vibe'] else ""
    
    if buckets['atencao']:
        atencao_content = f"""<div style='background: rgba(244,67,54,0.1); border-left: 4px solid #F44336; padding: 1.5rem; margin-bottom: 3rem; border-radius: 4px;'>
            <h3 style='color: #F44336; margin-bottom: 1rem;'><i class='fas fa-exclamation-triangle'></i> Atenção</h3>
            {"".join(f"<p style='margin-bottom:0.5rem; color:#ddd;'>{p}</p>" for p in buckets['atencao'])}
        </div>"""
    else:
        atencao_content = ""

    timeline_html = ""
    for step in buckets['cronograma']:
        step_title = step.get('titulo', 'Passo')
        step_details = step.get('detalhes', [])
        details_html = "".join(f"<li>{d}</li>" for d in step_details)
        timeline_html += f"""
        <div class="timeline-item">
            <div class="timeline-content">
                <h3 class="timeline-title">{step_title}</h3>
                <ul class="timeline-details">
                    {details_html}
                </ul>
            </div>
        </div>
        """
    if not timeline_html:
        timeline_html = "<p>Roteiro detalhado em breve.</p>"

    included_html = "".join(f"<li><i class='fas fa-check'></i> {item}</li>" for item in buckets['incluso']) if buckets['incluso'] else "<li>Consultar equipe</li>"
    excluded_html = "".join(f"<li><i class='fas fa-times'></i> {item}</li>" for item in buckets['nao_incluso']) if buckets['nao_incluso'] else "<li>Consultar equipe</li>"

    if buckets['investimento']:
        price_content = "".join(f"<p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>{p}</p>" for p in buckets['investimento'])
        price_content += "<br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Garantir minha vaga</a>"
    else:
        price_content = "<p style='font-size: 1.1rem;'>Consulte nossa equipe para obter os valores e formas de pagamento atualizados.</p><br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Consultar Valores</a>"

    faq_html = ""
    for faq in buckets['faq']:
        q = faq.get('pergunta', '')
        a_list = faq.get('resposta', [])
        a_html = "".join(f"<p>{ans}</p>" for ans in a_list)
        faq_html += f"""
        <div class="accordion-item">
            <button class="accordion-header">
                {q}
                <i class="fas fa-chevron-down"></i>
            </button>
            <div class="accordion-content">
                {a_html}
            </div>
        </div>
        """

    politica_html = ""
    if buckets['politica']:
        p_html = "".join(f"<p style='margin-bottom: 0.5rem;'>{p}</p>" for p in buckets['politica'])
        politica_html = f"""
        <div class="accordion-item">
            <button class="accordion-header" style="color: #F44336;">
                Política de Cancelamento
                <i class="fas fa-chevron-down"></i>
            </button>
            <div class="accordion-content">
                {p_html}
            </div>
        </div>
        """

    page_html = template.replace('{{ TITLE }}', exp.get('title', 'Expedição'))
    img_path = exp.get('img', 'public/hero_mountain_bg_1785256610841.jpg').replace('public/', '/')
    page_html = page_html.replace('{{ BACKGROUND_IMG }}', img_path)
    page_html = page_html.replace('..//public', '..') # safety
    page_html = page_html.replace('{{ DATES }}', exp.get('dates', ''))
    page_html = page_html.replace('{{ DUR }}', exp.get('dur', ''))
    page_html = page_html.replace('{{ LOC }}', exp.get('loc', ''))
    page_html = page_html.replace('{{ DIFFICULTY }}', exp.get('difficulty', ''))
    elevation_val = exp.get('elevation', 'Consultar')
    if elevation_val and elevation_val != 'N/A' and elevation_val != 'Consultar':
        elevation_html = f'''<div class="meta-item">
            <span class="meta-label">Elevação</span>
            <span class="meta-value">{elevation_val}</span>
        </div>'''
    else:
        elevation_html = ''
    page_html = page_html.replace('{{ ELEVATION_BLOCK }}', elevation_html)
    
    page_html = page_html.replace('{{ HISTORIA_CONTENT }}', historia_content)
    page_html = page_html.replace('{{ VIBE_CONTENT }}', vibe_content)
    page_html = page_html.replace('{{ ATENCAO_CONTENT }}', atencao_content)
    page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_html)
    page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_html)
    page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_html)
    page_html = page_html.replace('{{ PRICE_CONTENT }}', price_content)
    page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_html)
    page_html = page_html.replace('{{ POLITICA_CONTENT }}', politica_html)

    out_path = os.path.join('expedicoes', exp['filename'])
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(page_html)

print("Geradas 23 páginas com a nova arquitetura baseada em JSON!")
