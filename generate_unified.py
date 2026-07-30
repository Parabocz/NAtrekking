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

        # ── Semantic Parser & Text Allocation (Heuristic Classifier) ────────────────────────────────────────────────
        def build_section(lines, html_tag="p"):
            return "".join(f"<{html_tag}>{l}</{html_tag}>" for l in lines)

        def build_list_items(lines):
            return "".join(f"<li>{l}</li>" for l in lines)
            
        def clean_lines(text):
            """Split on real newlines OR literal \\n, deduplicate, remove noise."""
            import re as _re
            seen, result = set(), []
            for line in _re.split(r'\\n|\n', text):
                line = line.strip().replace('\u200b','').replace('\xa0',' ').strip()
                if not line or len(line) < 5:
                    continue
                if line in seen:
                    continue
                seen.add(line)
                result.append(line)
            return result

        if not raw_text:
            intro_content    = "<p>Informações detalhadas estão sendo atualizadas para esta expedição.</p>"
            included_content = "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = "<li>Consulte nossa equipe para detalhes.</li>"
            timeline_content = """<div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content"><h3>Roteiro</h3><p>Em atualização — entre em contato para mais informações.</p></div></div>"""
            faq_content      = """<div class="accordion-item"><button class="accordion-header"><span>Tem dúvidas?</span><span class="icon">+</span></button><div class="accordion-body"><div class="accordion-content"><p>Entre em contato com nossa equipe — estamos prontos para ajudar você a planejar a expedição perfeita.</p></div></div></div>"""
        else:
            all_lines = clean_lines(raw_text)

            NOISE_PHRASES = {
                'uma experiência única', 'a natureza espera por você', 'garanta seu lugar', 
                'experiências inesquecíveis', 'como vai rolar essa trip', 'como vai rolar a trip',
                'o que esperar dessa viagem', 'quem pode participar', 'ricardo tiburtius',
                'somos uma empresa do sul do brasil', 'a n.a trekking nasceu',
                '"comida boa', 'não tem o que falar', 'guia gente boa', 'nota 1000'
            }
            
            def is_noise(line):
                ll = line.lower()
                for n in NOISE_PHRASES:
                    if n in ll:
                        return True
                return False

            META_SPEC_RE = re.compile(
                r'^(?:data:|ponto de encontro:|ganho de elevação:|perda de elevação:|'
                r'distância:|dificuldade física:|dificuldade técnica:|nível de preparação|'
                r'elevação m[íi]nima:|elevação m[áa]xima:|mudança na elevação:|'
                r'tempo de trekking:|noite média|classificamos esse|'
                r'esse roteiro acontecerá|\d{1,2}/\d{1,2}/|\d{4}\b)',
                re.IGNORECASE
            )

            TIME_RE = re.compile(r'^\d{1,2}:\d{2}\s')
            DAY_RE  = re.compile(r'^(?:dia\s+\d|d[ae]?\s*\d|\d+[°º]\s*dia)', re.IGNORECASE)
            ROUTE_ACTION_RE = re.compile(r'(?:acampamento\s+\S+\s*[>→]|portão\s+\S+\s*[>→]|acampamento\s+\w+\s*>\s*\w)', re.IGNORECASE)
            ROUTE_KEYWORDS = ['->', 'aeroporto de kilimanjaro ->']
            
            def is_timeline_trigger(line):
                if TIME_RE.match(line) or DAY_RE.match(line) or ROUTE_ACTION_RE.search(line):
                    return True
                if any(kw in line.lower() for kw in ROUTE_KEYWORDS):
                    return True
                return False

            WARNING_PHRASES = [
                'condições do tempo', 'não podemos garantir tempo bom',
                'esse é um roteiro que necessita', 'os horários podem variar',
                'as expedições em grupo são', 'não se preocupe pois sempre haverá'
            ]
            
            def is_warning(line):
                ll = line.lower()
                return any(w in ll for w in WARNING_PHRASES)

            FAQ_EXACT = ['política de cancelamento', 'politica de cancelamento', 'políticas de cancelamento']
            def is_faq_trigger(line):
                if line.endswith('?') and len(line) < 150:
                    return True
                ll = line.lower().strip()
                return any(q == ll for q in FAQ_EXACT)

            buckets = {
                'specs': [], 'intro': [], 'warnings': [],
                'timeline_data': [], 'included': [], 'excluded': [], 'faq_data': [], 'price_data': [],
            }
            
            ctx = {
                'mode': 'intro',
                'tl_title': None,
                'tl_body': [],
                'faq_q': None,
                'faq_a': []
            }
            
            def flush_tl():
                if ctx['tl_title'] or ctx['tl_body']:
                    t = ctx['tl_title'] if ctx['tl_title'] else "Etapa do roteiro"
                    buckets['timeline_data'].append((t, list(ctx['tl_body'])))
                ctx['tl_title'] = None
                ctx['tl_body'] = []
                
            def flush_faq():
                if ctx['faq_q']:
                    buckets['faq_data'].append((ctx['faq_q'], list(ctx['faq_a'])))
                ctx['faq_q'] = None
                ctx['faq_a'] = []

            for line in all_lines:
                ll = line.lower()
                if is_noise(line):
                    continue
                if re.search(r'(R\$|US\$|USD)\s*[\d\.,]+', line, re.IGNORECASE):
                    buckets['price_data'].append(line)
                    continue
                
                if ll in ['incluso no investimento', 'incluso no pacote', 'o que está incluso']:
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'included'
                    continue
                if ll in ['não incluso no investimento', 'não incluso', 'nao incluso', 'não está incluso']:
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'excluded'
                    continue
                    
                if is_faq_trigger(line):
                    flush_tl(); flush_faq()
                    ctx['mode'] = 'faq'
                    ctx['faq_q'] = line
                    continue
                    
                if is_warning(line):
                    buckets['warnings'].append(line)
                    continue
                    
                if is_timeline_trigger(line):
                    flush_faq(); flush_tl()
                    ctx['mode'] = 'timeline'
                    ctx['tl_title'] = line
                    continue
                    
                if ctx['mode'] == 'intro' and META_SPEC_RE.match(line):
                    buckets['specs'].append(line)
                    continue

                if ctx['mode'] == 'intro':
                    if len(line) > 20: 
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'timeline':
                    ctx['tl_body'].append(line)
                elif ctx['mode'] == 'included':
                    if line.startswith('-') or len(line) < 120:
                        buckets['included'].append(line.lstrip('- '))
                    else:
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'excluded':
                    if line.startswith('-') or len(line) < 120:
                        buckets['excluded'].append(line.lstrip('- '))
                    else:
                        buckets['intro'].append(line)
                elif ctx['mode'] == 'faq':
                    ctx['faq_a'].append(line)

            flush_tl()
            flush_faq()
            
            # Formatting Output
            intro_html = ""
            for p in buckets['intro'][:4]:
                intro_html += f"<p>{p}</p>"
            if not intro_html:
                intro_content = "<p>Uma aventura que transforma. Descubra paisagens únicas com segurança e apoio total da equipe NA Trekking.</p>"
                
            if buckets['specs']:
                intro_html += "<div class='expedition-specs' style='margin-top: 1.5rem; padding: 1.5rem; background: rgba(255,255,255,0.05); border-radius: 12px;'>"
                intro_html += "<h4 style='color: var(--primary-color); margin-bottom: 1rem; text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.1em;'>Especificações da Expedição</h4>"
                intro_html += "<ul style='list-style: none; padding: 0; margin: 0; display: grid; gap: 0.5rem;'>"
                for spec in buckets['specs']:
                    parts = spec.split(':', 1)
                    if len(parts) == 2:
                        intro_html += f"<li style='color: rgba(255,255,255,0.8);'><strong>{parts[0].strip()}:</strong> {parts[1].strip()}</li>"
                    else:
                        intro_html += f"<li style='color: rgba(255,255,255,0.8);'>{spec}</li>"
                intro_html += "</ul></div>"
            intro_content = intro_html

            if buckets['timeline_data']:
                timeline_content = ""
                for t_title, body_lines in buckets['timeline_data']:
                    body_html = "".join(f"<p>{l}</p>" for l in body_lines if l.strip())
                    timeline_content += f'''<div class="timeline-item">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3>{t_title}</h3>
                            {body_html}
                        </div>
                    </div>'''
            else:
                timeline_content = """<div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content"><h3>Roteiro</h3><p>Informações do roteiro serão disponibilizadas em breve.</p></div></div>"""

            included_content = build_list_items(buckets['included']) or "<li>Consulte nossa equipe para detalhes completos.</li>"
            excluded_content = build_list_items(buckets['excluded']) or "<li>Consulte nossa equipe para detalhes.</li>"

            faq_html = ""
            if buckets['warnings']:
                warnings_html = "".join(f"<p>{w}</p>" for w in buckets['warnings'])
                faq_html += f'''<div class="accordion-item">
                    <button class="accordion-header">
                        <span>Avisos Importantes</span>
                        <span class="icon">+</span>
                    </button>
                    <div class="accordion-body">
                        <div class="accordion-content">{warnings_html}</div>
                    </div>
                </div>'''

            for q, a_lines in buckets['faq_data']:
                a_text = "".join(f"<p>{l}</p>" for l in a_lines)
                if not a_text:
                    a_text = "<p>Entre em contato com nossa equipe para mais detalhes.</p>"
                faq_html += f'''<div class="accordion-item">
                    <button class="accordion-header">
                        <span>{q}</span>
                        <span class="icon">+</span>
                    </button>
                    <div class="accordion-body">
                        <div class="accordion-content">{a_text}</div>
                    </div>
                </div>'''
                

            if buckets['price_data']:
                price_content = "".join(f"<p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>{p}</p>" for p in buckets['price_data'])
                price_content += "<br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Garantir minha vaga</a>"
            else:
                price_content = "<p style='font-size: 1.1rem;'>Consulte nossa equipe para obter os valores e formas de pagamento atualizados.</p><br><a href='https://wa.me/5541999999999' class='btn btn-primary'>Consultar Valores</a>"

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
        page_html = page_html.replace('{{ INTRO_CONTENT }}', intro_content if 'intro_content' in locals() else intro_html)
        page_html = page_html.replace('{{ INCLUDED_CONTENT }}', included_content)
        page_html = page_html.replace('{{ EXCLUDED_CONTENT }}', excluded_content)
        page_html = page_html.replace('{{ TIMELINE_CONTENT }}', timeline_content)
        page_html = page_html.replace('{{ FAQ_CONTENT }}', faq_content)
        page_html = page_html.replace('{{ PRICE_CONTENT }}', price_content)
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

