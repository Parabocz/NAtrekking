import json
import re
import os

with open(r'C:\Users\Gustavo\.gemini\antigravity\brain\f263f127-f6ed-46ad-9738-741cf821b81b\scratch\scraped_data.json', 'r', encoding='utf-8') as f:
    text_data = json.load(f)

structured_data = {}

def clean_lines(text):
    seen, result = set(), []
    for line in re.split(r'\n', text):
        line = line.strip().replace('\u200b','').replace('\xa0',' ').strip()
        if not line or len(line) < 5:
            continue
        if line in seen:
            continue
        seen.add(line)
        result.append(line)
    return result

NOISE_PHRASES = {
    'uma experiência única', 'a natureza espera por você', 'garanta seu lugar', 
    'experiências inesquecíveis', 'quem pode participar', 'ricardo tiburtius',
    'somos uma empresa do sul do brasil', 'a n.a trekking nasceu',
    '"comida boa', 'não tem o que falar', 'guia gente boa', 'nota 1000',
    'garanta seu lugar na aventura'
}

def is_noise(line):
    ll = line.lower()
    return any(n in ll for n in NOISE_PHRASES)

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
    return any(kw in line.lower() for kw in ROUTE_KEYWORDS)

WARNING_PHRASES = [
    'condições do tempo', 'não podemos garantir tempo bom', 'atenção:', 'importante:',
    'esse é um roteiro que necessita', 'os horários podem variar',
    'as expedições em grupo são', 'não se preocupe pois sempre haverá'
]
def is_warning(line):
    return any(w in line.lower() for w in WARNING_PHRASES)

FAQ_EXACT = ['políticas de cancelamento', 'política de cancelamento']
FAQ_QUESTIONS = [
    'qual o nível', 'quais custos', 'quais documentos', 'quais voos',
    'passagem aérea', 'preciso de transfer', 'que dia devo chegar',
    'bagagem', 'comunicação', 'clima', 'dividir', 'equipamento',
    'abandonar', 'quais vacinas'
]
def is_faq_trigger(line):
    ll = line.lower().strip()
    if line.endswith('?') and len(line) < 150:
        return True
    return any(q in ll for q in FAQ_QUESTIONS)

for url, raw_text in text_data.items():
    buckets = {
        'historia': [], 'vibe': [], 'specs': [], 'cronograma': [], 
        'atencao': [], 'incluso': [], 'nao_incluso': [], 
        'investimento': [], 'politica': [], 'faq': []
    }
    
    ctx = {
        'mode': 'historia',
        'tl_title': None,
        'tl_body': [],
        'faq_q': None,
        'faq_a': []
    }
    
    def flush_tl():
        if ctx['tl_title'] or ctx['tl_body']:
            t = ctx['tl_title'] if ctx['tl_title'] else "Etapa"
            buckets['cronograma'].append({"titulo": t, "detalhes": list(ctx['tl_body'])})
        ctx['tl_title'] = None
        ctx['tl_body'] = []
        
    def flush_faq():
        if ctx['faq_q']:
            buckets['faq'].append({"pergunta": ctx['faq_q'], "resposta": list(ctx['faq_a'])})
        ctx['faq_q'] = None
        ctx['faq_a'] = []
        
    all_lines = clean_lines(raw_text)
    
    for line in all_lines:
        ll = line.lower()
        if is_noise(line):
            continue
            
        if 'como vai rolar' in ll or 'o que esperar' in ll:
            flush_tl(); flush_faq()
            ctx['mode'] = 'vibe'
            continue
            
        if ll in ['incluso no investimento', 'incluso no pacote', 'o que está incluso']:
            flush_tl(); flush_faq()
            ctx['mode'] = 'incluso'
            continue
            
        if ll in ['não incluso no investimento', 'não incluso', 'nao incluso', 'não está incluso']:
            flush_tl(); flush_faq()
            ctx['mode'] = 'nao_incluso'
            continue
            
        if ll in FAQ_EXACT:
            flush_tl(); flush_faq()
            ctx['mode'] = 'politica'
            continue
            
        if is_faq_trigger(line):
            flush_tl(); flush_faq()
            ctx['mode'] = 'faq'
            ctx['faq_q'] = line
            continue
            
        if is_warning(line):
            buckets['atencao'].append(line)
            continue
            
        if re.search(r'(R\$|US\$|USD)\s*[\d\.,]+', line, re.IGNORECASE):
            buckets['investimento'].append(line)
            continue
            
        if is_timeline_trigger(line):
            flush_faq(); flush_tl()
            ctx['mode'] = 'cronograma'
            ctx['tl_title'] = line
            continue
            
        if ctx['mode'] in ['historia', 'vibe'] and META_SPEC_RE.match(line):
            buckets['specs'].append(line)
            continue

        if ctx['mode'] == 'historia':
            if len(line) > 50:
                buckets['historia'].append(line)
        elif ctx['mode'] == 'vibe':
            if len(line) > 30:
                buckets['vibe'].append(line)
        elif ctx['mode'] == 'cronograma':
            ctx['tl_body'].append(line)
        elif ctx['mode'] == 'incluso':
            if line.startswith('-') or len(line) < 120:
                buckets['incluso'].append(line.lstrip('- '))
            else:
                buckets['vibe'].append(line)
        elif ctx['mode'] == 'nao_incluso':
            if line.startswith('-') or len(line) < 120:
                buckets['nao_incluso'].append(line.lstrip('- '))
            else:
                buckets['vibe'].append(line)
        elif ctx['mode'] == 'politica':
            buckets['politica'].append(line)
        elif ctx['mode'] == 'faq':
            ctx['faq_a'].append(line)

    flush_tl()
    flush_faq()
    
    structured_data[url] = buckets

with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(structured_data, f, ensure_ascii=False, indent=4)
print("Copy estruturada gerada com sucesso em structured_copy.json!")
