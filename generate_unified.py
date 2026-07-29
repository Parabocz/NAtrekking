import os
import re
import json
import shutil

html_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\index.html'
template_path = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\template_expedicao.html'
expedicoes_dir = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\expedicoes'
scraped_data_path = r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\scratch\scraped_data.json'
brain_dir = r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b'
public_dir = r'C:\Users\Gustavo\.gemini\antigravity\scratch\na-trekking\public'

os.makedirs(expedicoes_dir, exist_ok=True)

try:
    with open(scraped_data_path, 'r', encoding='utf-8') as f:
        scraped_data = json.load(f)
except FileNotFoundError:
    scraped_data = {}

with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Helper function to find the exact filename of a generated image by prefix
def find_image(prefix):
    for f in os.listdir(brain_dir):
        if f.startswith(prefix) and f.endswith('.jpg'):
            # Copy it to public to be served by the web server
            shutil.copy2(os.path.join(brain_dir, f), os.path.join(public_dir, f))
            return f"public/{f}"
    return None

# Map prefixes to expeditions
hero_map = {
    "vulcoes-do-equador.html": "equador_hero",
    "kilimanjaro-2026.html": "kilimanjaro_hero",
    "kilimanjaro-safari-2026.html": "kilimanjaro_safari_hero",
    "kilimanjaro-safari-2027.html": "kilimanjaro_safari_hero",
    "monte-roraima.html": "roraima_hero",
    "patagonia-especial-reveillon.html": "patagonia_reveillon_hero",
    "ushuaia.html": "ushuaia_hero",
    "patagonia-chilena.html": "patagonia_chilena_hero",
    "patagonia-argentina.html": "patagonia_argentina_hero",
    "vulcoes-do-atacama.html": "atacama_hero",
    "cruce-de-los-andes.html": "andes_hero",
    "trekking-rinoceronte.html": "rinoceronte_hero",
    "hiking-torre-da-prata.html": "torre_prata_hero",
}

data = [
    # Internacional & Montanha
    {"title": "Vulcões do Equador", "dates": "16 a 25/set/2026", "loc": "Equador", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_1.jpg", "link": None, "sort_date": "2026-09-16", "elevation": "5.897m", "difficulty": "Alta", "filename": "vulcoes-do-equador.html", "url": None},
    {"title": "Kilimanjaro 2026", "dates": "04 a 13/out/2026", "loc": "Tanzânia", "dur": "10 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/kilimanjaro2026", "sort_date": "2026-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-2026.html", "url": "https://natrekking.com.br/kilimanjaro2026"},
    {"title": "Kilimanjaro + Safari 2026", "dates": "04 a 16/out/2026", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_3.jpg", "link": "https://natrekking.com.br/kilimanjarosafari2026", "sort_date": "2026-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-safari-2026.html", "url": "https://natrekking.com.br/kilimanjarosafari2026"},
    {"title": "Kilimanjaro + Safari 2027", "dates": "04 a 16/out/2027", "loc": "Tanzânia", "dur": "13 dias", "cats": ["internacional", "montanha"], "img": "public/alta_montanha_10.jpg", "link": "https://natrekking.com.br/kilimanjaro-safari-2027", "sort_date": "2027-10-04", "elevation": "5.895m", "difficulty": "Muito Alta", "filename": "kilimanjaro-safari-2027.html", "url": "https://natrekking.com.br/kilimanjaro-safari-2027"},
    {"title": "Monte Roraima", "dates": "20 a 29/nov/2026", "loc": "Tríplice fronteira Brasil/Venezuela/Guiana", "dur": "10 dias", "cats": ["internacional"], "img": "public/agenda_internacional_4.jpg", "link": "https://natrekking.com.br/roraimanov2026", "sort_date": "2026-11-20", "elevation": "2.810m", "difficulty": "Alta", "filename": "monte-roraima.html", "url": "https://natrekking.com.br/roraimanov2026"},
    {"title": "Patagônia Especial (Réveillon)", "dates": "27/dez/2026 a 13/jan/2027", "loc": "Argentina e Chile", "dur": "18 dias", "cats": ["internacional"], "img": "public/agenda_internacional_5.jpg", "link": "https://natrekking.com.br/patagonia-especial", "sort_date": "2026-12-27", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-especial-reveillon.html", "url": "https://natrekking.com.br/patagonia-especial"},
    {"title": "Ushuaia", "dates": "27/dez/2026 a 02/jan/2027", "loc": "Argentina (Ushuaia)", "dur": "7 dias", "cats": ["internacional"], "img": "public/agenda_internacional_6.jpg", "link": "https://natrekking.com.br/ushuaia-dez26-jan27", "sort_date": "2026-12-27", "elevation": "Consultar", "difficulty": "Moderada", "filename": "ushuaia.html", "url": "https://natrekking.com.br/ushuaia-dez26-jan27"},
    {"title": "Patagônia Chilena", "dates": "02 a 07/jan/2027", "loc": "Chile (Punta Arenas e Puerto Natales)", "dur": "6 dias", "cats": ["internacional"], "img": "public/agenda_internacional_7.jpg", "link": "https://natrekking.com.br/patagoniachilenaespecial", "sort_date": "2027-01-02", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-chilena.html", "url": "https://natrekking.com.br/patagoniachilenaespecial"},
    {"title": "Patagônia Argentina", "dates": "07 a 13/jan/2027", "loc": "Argentina (El Calafate/Chaltén)", "dur": "7 dias", "cats": ["internacional"], "img": "public/agenda_internacional_8.jpg", "link": "https://natrekking.com.br/calafate-chalten-especial", "sort_date": "2027-01-07", "elevation": "Consultar", "difficulty": "Moderada", "filename": "patagonia-argentina.html", "url": "https://natrekking.com.br/calafate-chalten-especial"},
    {"title": "Vulcões do Atacama", "dates": "08 a 18/jan/2027", "loc": "Chile (Deserto do Atacama)", "dur": "11 dias", "cats": ["internacional", "montanha"], "img": "public/agenda_internacional_9.jpg", "link": "https://natrekking.com.br/vulcões-do-atacama-jan-27", "sort_date": "2027-01-08", "elevation": "5.920m", "difficulty": "Muito Alta", "filename": "vulcoes-do-atacama.html", "url": "https://natrekking.com.br/vulcões-do-atacama-jan-27"},
    {"title": "Torres del Paine", "dates": "12 a 22/mar/2027", "loc": "Chile (Puerto Natales)", "dur": "11 dias", "cats": ["internacional"], "img": "public/agenda_internacional_10.jpg", "link": "https://natrekking.com.br/torresdelpaineo2027", "sort_date": "2027-03-12", "elevation": "Consultar", "difficulty": "Alta", "filename": "torres-del-paine.html", "url": "https://natrekking.com.br/torresdelpaineo2027"},
    {"title": "Cruce de Los Andes", "dates": "20 a 27/mar/2027", "loc": "Argentina e Chile", "dur": "8 dias", "cats": ["internacional"], "img": "public/agenda_internacional_2.jpg", "link": "https://natrekking.com.br/crucedelosandes2027", "sort_date": "2027-03-20", "elevation": "Consultar", "difficulty": "Moderada", "filename": "cruce-de-los-andes.html", "url": "https://natrekking.com.br/crucedelosandes2027"},

    # Nacional & Cursos
    {"title": "Trekking Rinoceronte", "dates": "01 e 02/ago/2026", "loc": "SC", "dur": "2 dias", "cats": ["nacional"], "img": "public/agenda_nacional_1.jpg", "link": "https://natrekking.com.br/rinoceronte", "sort_date": "2026-08-01", "elevation": "Consultar", "difficulty": "Moderada", "filename": "trekking-rinoceronte.html", "url": "https://natrekking.com.br/rinoceronte"},
    {"title": "Hiking Torre da Prata", "dates": "15/ago/2026", "loc": "PR", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_2.jpg", "link": "https://natrekking.com.br/torredaprata", "sort_date": "2026-08-15", "elevation": "Consultar", "difficulty": "Moderada", "filename": "hiking-torre-da-prata.html", "url": "https://natrekking.com.br/torredaprata"},
    {"title": "Lençóis Maranhenses (ago/2026)", "dates": "15 a 21/ago/2026", "loc": "MA", "dur": "7 dias", "cats": ["nacional"], "img": "public/agenda_nacional_4.jpg", "link": "https://natrekking.com.br/lencoismaranhensesagosto2026", "sort_date": "2026-08-15", "elevation": "N/A", "difficulty": "Baixa/Moderada", "filename": "lencois-maranhenses-ago-2026.html", "url": "https://natrekking.com.br/lencoismaranhensesagosto2026"},
    {"title": "Pedra do Cantagalo", "dates": "22/ago/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_3.jpg", "link": "https://natrekking.com.br/cantagalo", "sort_date": "2026-08-22", "elevation": "Consultar", "difficulty": "Moderada", "filename": "pedra-do-cantagalo.html", "url": "https://natrekking.com.br/cantagalo"},
    {"title": "Curso de Trekking (agosto)", "dates": "29 e 30/ago/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/agenda_nacional_5.jpg", "link": "https://natrekking.com.br/curso-de-trekking-agosto", "sort_date": "2026-08-29", "elevation": "N/A", "difficulty": "Iniciante", "filename": "curso-trekking-agosto.html", "url": "https://natrekking.com.br/curso-de-trekking-agosto"},
    {"title": "Espraiado x Soldados", "dates": "5 a 7/set/2026", "loc": "SC", "dur": "3 dias", "cats": ["nacional"], "img": "public/agenda_nacional_6.jpg", "link": "https://natrekking.com.br/espraiadoxsoldados", "sort_date": "2026-09-05", "elevation": "Consultar", "difficulty": "Alta", "filename": "espraiado-x-soldados.html", "url": "https://natrekking.com.br/espraiadoxsoldados"},
    {"title": "Travessia Araçá x Crista", "dates": "05 a 08/set/2026", "loc": "PR e SC", "dur": "4 dias", "cats": ["nacional"], "img": "public/agenda_nacional_7.jpg", "link": "https://natrekking.com.br/travessiaaracaxcrista", "sort_date": "2026-09-05", "elevation": "Consultar", "difficulty": "Alta", "filename": "travessia-araca-x-crista.html", "url": "https://natrekking.com.br/travessiaaracaxcrista"},
    {"title": "Travessia Picos de Jaraguá", "dates": "12/set/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_8.jpg", "link": "https://natrekking.com.br/travpicosdejaragua", "sort_date": "2026-09-12", "elevation": "Consultar", "difficulty": "Alta", "filename": "travessia-picos-de-jaragua.html", "url": "https://natrekking.com.br/travpicosdejaragua"},
    {"title": "Fenda Cruz de Pedra", "dates": "13/set/2026", "loc": "SC", "dur": "1 dia", "cats": ["nacional"], "img": "public/agenda_nacional_9.jpg", "link": "https://natrekking.com.br/fendacruzdepedra", "sort_date": "2026-09-13", "elevation": "Consultar", "difficulty": "Moderada", "filename": "fenda-cruz-de-pedra.html", "url": "https://natrekking.com.br/fendacruzdepedra"},
    {"title": "Curso de Trekking (setembro)", "dates": "26 e 27/set/2026", "loc": "Rio dos Cedros/SC", "dur": "2 dias", "cats": ["cursos"], "img": "public/agenda_nacional_10.jpg", "link": "https://natrekking.com.br/curso-de-trekking-setembro", "sort_date": "2026-09-26", "elevation": "N/A", "difficulty": "Iniciante", "filename": "curso-trekking-setembro.html", "url": "https://natrekking.com.br/curso-de-trekking-setembro"},
    {"title": "Lençóis Maranhenses (jul/2027)", "dates": "11 a 17/jul/2027", "loc": "MA", "dur": "7 dias", "cats": ["nacional"], "img": "public/agenda_nacional_11.png", "link": "https://natrekking.com.br/lencois-maranhenses-jul-27", "sort_date": "2027-07-11", "elevation": "N/A", "difficulty": "Baixa/Moderada", "filename": "lencois-maranhenses-jul-2027.html", "url": "https://natrekking.com.br/lencois-maranhenses-jul-27"},
]

data.sort(key=lambda x: x['sort_date'])
cards = []
generated = set()

for item in data:
    title = item['title']
    dates = item['dates'].upper()
    loc = item['loc'].upper()
    dur = item['dur'].upper()
    cats_str = " ".join(item['cats'])
    elevation = item.get('elevation', 'Consultar')
    difficulty = item.get('difficulty', 'Consultar')
    filename = item['filename']
    url = item.get('url')
    
    # 1. Determine hero image (Generated or Fallback)
    prefix = hero_map.get(filename)
    hero_image = None
    if prefix:
        hero_image = find_image(prefix)
    
    # Fallback to high-res generic hero if generation failed/quota hit
    if not hero_image:
        hero_image = "public/fallback_hero.jpg"

    if filename not in generated:
        generated.add(filename)
        
        raw_text = scraped_data.get(url, "") if url else ""

        # ── Semantic Parser ────────────────────────────────────────────────
        def clean_lines(text):
            """Split on real newlines OR literal \\n, deduplicate, remove noise."""
            import re as _re
            seen, result = set(), []
            for line in _re.split(r'\n', text):
                # strip zero-width spaces and non-breaking spaces
                line = line.strip().replace('\u200b','').replace('\xa0',' ').strip()
                if not line or len(line) < 9:
                    continue
                if line in seen:
                    continue
                seen.add(line)
                result.append(line)
            return result

        def build_section(lines, html_tag="p"):
            return "".join(f"<{html_tag}>{l}</{html_tag}>" for l in lines)

        def build_list_items(lines):
            return "".join(f"<li>{l}</li>" for l in lines if len(l) > 10)

        if not raw_text:
            if url is None:
                intro_content    = "<p>Em breve, as informações completas serão disponibilizadas aqui. Fique ligado!</p>"
                included_content = "<li>Informações em breve</li>"
                excluded_content = "<li>Informações em breve</li>"
                timeline_items_data = [("Em Breve", ["Detalhes do roteiro serão divulgados em breve."])]
                faq_pairs        = []
            else:
                intro_content    = "<p>Informações detalhadas estão sendo atualizadas para esta expedição.</p>"
                included_content = "<li>Consulte nossa equipe para detalhes completos.</li>"
                excluded_content = "<li>Consulte nossa equipe para detalhes.</li>"
                timeline_items_data = [("Roteiro", ["Em atualização — entre em contato para mais informações."])]
                faq_pairs        = []
        else:
            all_lines = clean_lines(raw_text)

            # ── Section boundary patterns ──────────────────────────────────
            NOISE_EXACT = {
                'uma experiência única', 'a natureza espera por você',
                'garanta seu lugar nessa aventura.', 'garanta seu lugar na aventura dos sonhos: kilimanjaro te espera!',
                'experiências inesquecíveis', 'como vai rolar essa trip', 'como vai rolar a trip',
                'o que esperar dessa viagem?', 'quem pode participar?',
                'somos uma empresa do sul do brasil com sede em joinville- sc, mas operamos em diversos estados e em mais 6 países promovendo expedições de todos os níveis.',
                'a n.a trekking nasceu através do adriano knopik (@adriknopik), guia e fundador, com intuito de mostrar as pessoas um novo estilo de vida, onde a simplicidade e a superação estão diariamente presentes.',
                'incluso no investimento', 'não incluso no investimento',
                'o que esperar dessa viagem', 'quem pode participar',
            }

            def is_noise(line):
                ll = line.lower().strip()
                if ll in NOISE_EXACT:
                    return True
                if ll.startswith('garanta seu lugar') and len(ll) < 80:
                    return True
                if 'ricardo tiburtius' in ll or 'expedição monte roraima' in ll.lower():
                    return True
                # repeated testimonial fragments
                if ll in {'"comida boa todo dia, equipe atenciosa', 'não tem o que falar. foi muito bom.',
                          'guia gente boa!', 'nota 1000! obrigado!"', 'não tem o que falar. foi muito bom.'}:
                    return True
                return False

            INCLUDED_TRIGGERS  = {'incluso no investimento', 'incluso no pacote', 'o que está incluso'}
            EXCLUDED_TRIGGERS  = {'não incluso no investimento', 'não incluso', 'nao incluso'}
            FAQ_STARTS         = [
                'qual o nível de experiência', 'quais custos a mais', 'quais documentos',
                'quais voos', 'a passagem aérea', 'preciso de transfer', 'que dia devo chegar',
                'nossa bagagem', 'haverá comunicação', 'o que esperar do clima',
                'tenho que dividir', 'quanto equipamento', 'e se eu abandonar',
                'política de cancelamento', 'politica de cancelamento',
                'condições do tempo:'
            ]
            # Route section starts with "como vai rolar" block or time-stamped schedule
            ROUTE_TRIGGERS     = [
                'como vai rolar', 'cronograma', 'rota lemosho', 'escalada do kilimanjaro',
                'aeroporto de kilimanjaro', 'ponto de encontro:'
            ]
            # Time-pattern: lines starting with HH:MM or "Dia N" or "Acampamento X > Y"
            TIME_RE = re.compile(r'^\d{1,2}:\d{2}\s')
            DAY_RE  = re.compile(
                r'^(?:dia\s+\d|d[ae]?\s*\d|\d+[°º]\s*dia|'
                r'acampamento\s+\S+\s*[>→]|portão\s+\S+\s*[>→]|'
                r'acampamento\s+\w+\s*>\s*\w)',
                re.IGNORECASE
            )

            intro_lines    = []
            included_lines = []
            excluded_lines = []
            route_lines    = []
            faq_pairs      = []

            mode      = 'intro'
            cur_faq   = [None, []]  # [question, answer_lines]

            def flush_faq():
                if cur_faq[0]:
                    faq_pairs.append((cur_faq[0], list(cur_faq[1])))
                cur_faq[0] = None
                cur_faq[1] = []

            # Descriptive sentences only for intro (no metadata lines)
            META_SKIP = re.compile(
                r'^(?:data:|ponto de encontro:|ganho de elevação:|perda de elevação:|'
                r'distância:|dificuldade física:|dificuldade técnica:|nível de preparação|'
                r'elevação m[íi]nima:|elevação m[áa]xima:|mudança na elevação:|'
                r'tempo de trekking:|noite média|distância:|classificamos esse|'
                r'esse roteiro acontecerá|\d{1,2}/\d{1,2}/|\d{4}\b)',
                re.IGNORECASE
            )

            for line in all_lines:
                ll = line.lower()

                if is_noise(line):
                    continue

                # Section switches
                if ll in INCLUDED_TRIGGERS:
                    mode = 'included'
                    continue
                if ll in EXCLUDED_TRIGGERS:
                    mode = 'excluded'
                    continue
                if any(ll.startswith(t) for t in FAQ_STARTS) or any(t in ll for t in FAQ_STARTS[:6]):
                    flush_faq()
                    cur_faq[0] = line
                    cur_faq[1] = []
                    mode = 'faq'
                    continue
                if mode == 'intro' and any(t in ll for t in ROUTE_TRIGGERS):
                    mode = 'route'
                    continue
                if mode == 'intro' and (TIME_RE.match(line) or DAY_RE.match(line)):
                    mode = 'route'

                if mode == 'intro':
                    if not META_SKIP.match(line) and len(line) > 30:
                        intro_lines.append(line)
                elif mode == 'included':
                    included_lines.append(line)
                elif mode == 'excluded':
                    excluded_lines.append(line)
                elif mode == 'route':
                    route_lines.append(line)
                elif mode == 'faq':
                    if line.endswith('?') and len(line) < 150:
                        flush_faq()
                        cur_faq[0] = line
                        cur_faq[1] = []
                    else:
                        cur_faq[1].append(line)
            flush_faq()

            # ── Build Intro ────────────────────────────────────────────────
            intro_content = build_section(intro_lines[:5])
            if not intro_content.strip():
                intro_content = "<p>Uma aventura que transforma. Descubra paisagens únicas com segurança e apoio total da equipe NA Trekking.</p>"

            # ── Included / Excluded ────────────────────────────────────────
            included_content = build_list_items(included_lines) or "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = build_list_items(excluded_lines) or "<li>Consulte nossa equipe para detalhes.</li>"

            # ── Timeline ───────────────────────────────────────────────────
            # Each entry starts when we see a time-stamp or day marker
            timeline_items_data = []
            cur_tl = [None, []]  # [title, body_lines]

            def flush_tl():
                if cur_tl[0] or cur_tl[1]:
                    timeline_items_data.append((cur_tl[0] or 'Etapa', list(cur_tl[1])))
                cur_tl[0] = None
                cur_tl[1] = []

            for line in route_lines:
                if TIME_RE.match(line) or DAY_RE.match(line) or (len(line) < 80 and '->' in line) or (len(line) < 80 and '>' in line and 'acampamento' in line.lower()):
                    flush_tl()
                    cur_tl[0] = line
                else:
                    cur_tl[1].append(line)
            flush_tl()

            # Fallback: chunk into labeled groups
            if not timeline_items_data and route_lines:
                chunk = max(3, len(route_lines) // 5)
                for idx in range(0, len(route_lines), chunk):
                    timeline_items_data.append((f"Etapa {idx//chunk+1}", route_lines[idx:idx+chunk]))

            if not timeline_items_data:
                timeline_items_data = [("Roteiro", ["Informações do roteiro serão disponibilizadas em breve."])]

            # Cancellation policy as last FAQ
            cancel = [l for l in all_lines if 'cancelamento' in l.lower() and len(l) > 40]
            if cancel and not any('cancelamento' in (q or '').lower() for q, _ in faq_pairs):
                faq_pairs.append(("Política de Cancelamento", cancel[:6]))

        # ── Build Timeline HTML ────────────────────────────────────────────
        def build_timeline(items):
            html = ""
            for title, body_lines in items:
                body_html = "".join(f"<p>{l}</p>" for l in body_lines if l.strip())
                html += f"""<div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <h3>{title}</h3>
                        {body_html}
                    </div>
                </div>\n"""
            return html

        timeline_content = build_timeline(timeline_items_data)

        # ── Build FAQ HTML ─────────────────────────────────────────────────
        faq_html = ""
        for q, a_lines in faq_pairs:
            if not q:
                continue
            a_text = " ".join(a_lines[:8]).strip()
            if not a_text:
                a_text = "Entre em contato com nossa equipe para mais detalhes."
            faq_html += f"""<div class="accordion-item">
                <button class="accordion-header">
                    <span>{q}</span>
                    <span class="icon">+</span>
                </button>
                <div class="accordion-body">
                    <div class="accordion-content"><p>{a_text}</p></div>
                </div>
            </div>\n"""
        faq_content = faq_html or """<div class="accordion-item">
            <button class="accordion-header"><span>Tem dúvidas?</span><span class="icon">+</span></button>
            <div class="accordion-body"><div class="accordion-content"><p>Entre em contato com nossa equipe — estamos prontos para ajudar você a planejar a expedição perfeita.</p></div></div>
        </div>"""

        # ── Inject into template ───────────────────────────────────────────
        page_html = template_html.replace('{{ TITLE }}', title)
        page_html = page_html.replace('{{ BACKGROUND_IMG }}', hero_image)
        page_html = page_html.replace('{{ DATES }}', dates)
        page_html = page_html.replace('{{ LOC }}', loc)
        page_html = page_html.replace('{{ DUR }}', dur)
        page_html = page_html.replace('{{ DIFFICULTY }}', difficulty)
        page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content)
        page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_content)
        page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_content)
        page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_content)
        page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_content)
        page_html = page_html.replace('{{ ORIGINAL_LINK }}', url or '#')

        def build_section(lines, html_tag="p"):
            parts = []
            for l in lines:
                parts.append(f"<{html_tag}>{l}</{html_tag}>")
            return "".join(parts)

        def build_list_items(lines):
            return "".join(f"<li>{l}</li>" for l in lines if len(l) > 10)

        if not raw_text:
            pass  # handled above
        else:
            all_lines = clean_lines(raw_text)

            # ── Detect section boundaries ──────────────────────────────────
            INCLUDED_TRIGGERS  = ['incluso no investimento', 'incluso no pacote', 'o que está incluso']
            EXCLUDED_TRIGGERS  = ['não incluso', 'nao incluso', 'não está incluso']
            FAQ_TRIGGERS       = ['política de cancelamento', 'politica de cancelamento',
                                  'qual o nível', 'quais documentos', 'quais voos',
                                  'haverá comunicação', 'condições do tempo', 'o que esperar do clima',
                                  'tenho que dividir', 'quanto equipamento', 'e se eu abandonar',
                                  'a passagem aérea', 'preciso de transfer', 'nossa bagagem']
            ROUTE_TRIGGERS     = ['como vai rolar', 'roteiro', 'cronograma', 'rota lemosho',
                                  'dia 1', 'dia 2', 'dia 3', 'aeroporto de kilimanjaro',
                                  'ponto de encontro', 'escalada do kilimanjaro', 'dia ->', '->',
                                  'acampamento', 'camp ', 'portão']
            EXCLUDE_NOISE      = ['experiências inesquecíveis', 'uma experiência única',
                                  'a natureza espera por você', 'garanta seu lugar',
                                  'somos uma empresa', 'a n.a trekking nasceu',
                                  'quem pode participar', 'o que esperar dessa viagem',
                                  'como vai rolar essa trip', 'incluso no investimento',
                                  'não incluso no investimento', 'qual o nível de experiência',
                                  'política de cancelamento', 'politica de cancelamento']

            intro_lines    = []
            included_lines = []
            excluded_lines = []
            route_lines    = []
            faq_pairs      = []   # list of (question, answer_lines)

            mode = 'intro'
            cur_faq_q  = None
            cur_faq_a  = []

            def flush_faq():
                if cur_faq_q and (cur_faq_a or cur_faq_q):
                    faq_pairs.append((cur_faq_q, list(cur_faq_a)))

            for line in all_lines:
                ll = line.lower()

                # noise skip
                if any(noise in ll for noise in EXCLUDE_NOISE):
                    if any(t in ll for t in FAQ_TRIGGERS):
                        flush_faq()
                        cur_faq_q = line
                        cur_faq_a = []
                        mode = 'faq'
                    continue

                # mode switches
                if any(t in ll for t in INCLUDED_TRIGGERS):
                    mode = 'included'
                    continue
                if any(t in ll for t in EXCLUDED_TRIGGERS):
                    mode = 'excluded'
                    continue
                if any(t in ll for t in FAQ_TRIGGERS):
                    flush_faq()
                    cur_faq_q = line
                    cur_faq_a = []
                    mode = 'faq'
                    continue
                # detect route section (stays in route once we enter)
                if mode == 'intro' and any(t in ll for t in ROUTE_TRIGGERS):
                    mode = 'route'

                # accumulate
                if mode == 'intro':
                    intro_lines.append(line)
                elif mode == 'included':
                    included_lines.append(line)
                elif mode == 'excluded':
                    excluded_lines.append(line)
                elif mode == 'route':
                    route_lines.append(line)
                elif mode == 'faq':
                    # If looks like a new question (ends with ?)
                    if line.endswith('?') or (len(line) < 120 and ll.endswith('?')):
                        flush_faq()
                        cur_faq_q = line
                        cur_faq_a = []
                    else:
                        cur_faq_a.append(line)
            flush_faq()

            # ── Build Intro ────────────────────────────────────────────────
            # Keep first meaningful 4 sentences max
            intro_content = build_section(intro_lines[:6])
            if not intro_content.strip():
                intro_content = "<p>Uma experiência transformadora que conecta pessoas à natureza.</p>"

            # ── Build Included / Excluded ──────────────────────────────────
            included_content = build_list_items(included_lines) or "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = build_list_items(excluded_lines) or "<li>Consulte nossa equipe para detalhes.</li>"

            # ── Build Timeline ─────────────────────────────────────────────
            # Try to detect day-by-day entries first
            day_pattern = re.compile(
                r'^(?:dia\s+\d+|d[ae]?\s*\d|day\s+\d|\d+[°º]\s*dia|'
                r'acampamento\s+\w+\s*[>→]\s*\w|portão\s+\w+\s*[>→])',
                re.IGNORECASE
            )

            timeline_items = []
            current_title  = None
            current_body   = []

            def flush_timeline():
                if current_title or current_body:
                    timeline_items.append((current_title or "Etapa", list(current_body)))

            for line in route_lines:
                if day_pattern.match(line) or (len(line) < 80 and '->' in line) or (len(line) < 80 and '→' in line):
                    flush_timeline()
                    current_title = line
                    current_body  = []
                else:
                    current_body.append(line)
            flush_timeline()

            # If no structured days found, chunk the route_lines into artificial segments
            if not timeline_items and route_lines:
                chunk_size = max(3, len(route_lines) // 5)
                for i in range(0, len(route_lines), chunk_size):
                    chunk = route_lines[i:i+chunk_size]
                    label = f"Etapa {i//chunk_size + 1}"
                    timeline_items.append((label, chunk))

            if not timeline_items:
                timeline_items = [("Roteiro", ["Informações do roteiro serão disponibilizadas em breve."])]

            def build_timeline(items):
                html = ""
                for i, item in enumerate(items):
                    if isinstance(item, tuple):
                        title, body_lines = item
                    else:
                        title = f"Etapa {i+1}"
                        body_lines = [item]
                    body_html = "".join(f"<p>{l}</p>" for l in body_lines if l.strip())
                    html += f"""<div class=\"timeline-item\">
                        <div class=\"timeline-dot\"></div>
                        <div class=\"timeline-content\">
                            <h3>{title}</h3>
                            {body_html}
                        </div>
                    </div>\n"""
                return html

            timeline_content = build_timeline(timeline_items)

            # ── Build FAQ Accordion ────────────────────────────────────────
            # Add Cancellation policy as last FAQ item if present
            cancel_lines = [l for l in all_lines if 'cancelamento' in l.lower() and len(l) > 30]
            if cancel_lines and not any('cancelamento' in q.lower() for q, _ in faq_pairs):
                faq_pairs.append(("Política de Cancelamento", cancel_lines[:8]))

            faq_html = ""
            for q, a_lines in faq_pairs:
                a_text = " ".join(a_lines[:6])
                if not a_text.strip():
                    continue
                faq_html += f"""<div class=\"accordion-item\">
                    <button class=\"accordion-header\">
                        <span>{q}</span>
                        <span class=\"icon\">+</span>
                    </button>
                    <div class=\"accordion-body\">
                        <div class=\"accordion-content\"><p>{a_text}</p></div>
                    </div>
                </div>\n"""
            faq_content = faq_html or "<div class=\"accordion-item\"><button class=\"accordion-header\"><span>Dúvidas?</span><span class=\"icon\">+</span></button><div class=\"accordion-body\"><div class=\"accordion-content\"><p>Entre em contato com nossa equipe para mais informações.</p></div></div></div>"

        # ── Inject into template ───────────────────────────────────────────
        page_html = template_html.replace('{{ TITLE }}', title)
        page_html = page_html.replace('{{ BACKGROUND_IMG }}', hero_image)
        page_html = page_html.replace('{{ DATES }}', dates)
        page_html = page_html.replace('{{ LOC }}', loc)
        page_html = page_html.replace('{{ DUR }}', dur)
        page_html = page_html.replace('{{ DIFFICULTY }}', difficulty)
        page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content)
        page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_content)
        page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_content)
        page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_content)
        page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_content)
        page_html = page_html.replace('{{ ORIGINAL_LINK }}', url or '#')
        
        # 3. Conditional Elevation
        elevation_html = f'''<div class="meta-item">
                        <span class="meta-label">Elevação Máx</span>
                        <span class="meta-value">{elevation}</span>
                    </div>'''
        if 'montanha' in item['cats']:
            page_html = page_html.replace('{{ ELEVATION_BLOCK }}', elevation_html)
        else:
            page_html = page_html.replace('{{ ELEVATION_BLOCK }}', '')
        
        page_path = os.path.join(expedicoes_dir, filename)
        with open(page_path, 'w', encoding='utf-8') as pf:
            pf.write(page_html)

    # Card keeps original catalog image
    target_link = f"expedicoes/{filename}"
    card = f'''                            <a href="{target_link}" class="list-card-link">
                                <div class="list-card filterable-card" data-category="{cats_str}">
                                    <div class="list-card-img" style="background-image: url('{item['img']}');"></div>
                                    <div class="list-card-content">
                                        <h4 class="list-card-title">{title}</h4>
                                        <div class="list-card-tags">
                                            <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg> <span class="tag-text">{dates}</span></span>
                                            <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> <span class="tag-text">{loc}</span></span>
                                            <span class="list-card-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> <span class="tag-text">{dur}</span></span>
                                        </div>
                                    </div>
                                </div>
                            </a>'''
    cards.append(card)

unified_html = "\\n".join(cards)

# Lemos novamente o index original e substituímos
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_catalog = f'''<div class="catalog-container">
                    <div class="catalog-filters">
                        <div class="custom-dropdown" id="catalog-filter-dropdown">
                            <div class="dropdown-header">
                                <span class="dropdown-selected">Todos</span>
                                <svg class="dropdown-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                            <ul class="dropdown-list">
                                <li class="dropdown-item active" data-value="all">Todos</li>
                                <li class="dropdown-item" data-value="nacional">Agenda Nacional</li>
                                <li class="dropdown-item" data-value="internacional">Agenda Internacional</li>
                                <li class="dropdown-item" data-value="montanha">Alta Montanha</li>
                                <li class="dropdown-item" data-value="cursos">Cursos Trekking</li>
                            </ul>
                        </div>
                    </div>
                    <div class="catalog-list unified-list">
{unified_html}
                    </div>
                </div>'''

pattern = r'<div class="catalog-container">.*?</div>\s*</div>\s*</section>'
replacement = new_catalog + '\n            </div>\n        </section>'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Geradas {len(generated)} paginas unicas de expedicoes!")
print("Index.html atualizado!")

