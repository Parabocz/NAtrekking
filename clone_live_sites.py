import requests
from bs4 import BeautifulSoup
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    "https://natrekking.com.br/kilimanjaro2026",
    "https://natrekking.com.br/kilimanjarosafari2026",
    "https://natrekking.com.br/kilimanjaro-safari-2027",
    "https://natrekking.com.br/roraimanov2026",
    # "https://natrekking.com.br/patagonia-especial", # Skip, already perfect
    "https://natrekking.com.br/ushuaia-dez26-jan27",
    "https://natrekking.com.br/patagoniachilenaespecial",
    "https://natrekking.com.br/calafate-chalten-especial",
    "https://natrekking.com.br/vulcões-do-atacama-jan-27",
    "https://natrekking.com.br/torresdelpaineo2027",
    "https://natrekking.com.br/crucedelosandes2027",
    "https://natrekking.com.br/travpicosdejaragua",
    "https://natrekking.com.br/fendacruzdepedra",
    "https://natrekking.com.br/curso-de-trekking-setembro",
    "https://natrekking.com.br/lencois-maranhenses-jul-27",
    "https://natrekking.com.br/rinoceronte",
    "https://natrekking.com.br/torredaprata",
    "https://natrekking.com.br/cantagalo",
    "https://natrekking.com.br/lencoismaranhensesagosto2026",
    "https://natrekking.com.br/curso-de-trekking-agosto",
    "https://natrekking.com.br/espraiadoxsoldados",
    "https://natrekking.com.br/travessiaaracaxcrista"
]

def clean_text(lines):
    res = []
    for l in lines:
        l = l.strip()
        if not l: continue
        if len(res) > 0 and res[-1] == l: continue
        res.append(l)
    return res

def parse_url(url):
    print(f"Fetching {url}...")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
    
    texts = []
    for p in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']):
        t = p.get_text(strip=True)
        # some wix spans are inside ps, leading to duplicates if not careful.
        # But get_text on block elements is usually better. Let's just collect all and deduplicate sequential.
        texts.append(t)
        
    lines = clean_text(texts)
    
    buckets = {
        'historia': [],
        'vibe': [],
        'specs': [],
        'cronograma': [],
        'atencao': [],
        'incluso': [],
        'nao_incluso': [],
        'investimento': [],
        'politica': [],
        'faq': []
    }
    
    state = 'intro'
    current_day = None
    
    for line in lines:
        line_lower = line.lower()
        
        # Exact match transitions for major blocks
        if line_lower == 'incluso no investimento' or line_lower == 'o que está incluso':
            state = 'incluso'
            continue
        elif line_lower == 'não incluso no investimento' or line_lower == 'não incluso no pacote' or line_lower == 'nao incluso no investimento':
            state = 'nao_incluso'
            continue
        elif line_lower == 'investimento':
            state = 'investimento'
            continue
        elif 'politica de cancelamento' in line_lower or 'política de cancelamento' in line_lower:
            state = 'politica'
            # we keep the line if we want, but let's skip the header itself
            continue
        elif line_lower in ['perguntas frequentes', 'dúvidas frequentes', 'dúvidas', 'quais documentos preciso?']:
            state = 'faq'
            if 'quais documentos' in line_lower:
                buckets['faq'].append(line)
            continue
        
        # Skip garbage
        if line_lower in ['cronograma', 'roteiro', 'dia', 'como vai rolar a trip', 'como vai rolar essa trip', 'dados da expedição']:
            continue
        
        # Timeline days transition
        if state in ['intro', 'cronograma'] and re.match(r'^(dia \d+|dia \d+ de|primeiro dia|segundo dia)', line_lower):
            state = 'cronograma'
            current_day = {"titulo": line, "descricao": []}
            buckets['cronograma'].append(current_day)
            continue
            
        # Add content based on state
        if state == 'intro':
            if 'data:' in line_lower or 'duração:' in line_lower or 'ponto de encontro:' in line_lower or 'dificuldade' in line_lower or 'elevação' in line_lower or 'distância:' in line_lower:
                buckets['specs'].append(line)
            elif 'atenção' in line_lower or 'condições do tempo' in line_lower or 'esse é um roteiro que necessita' in line_lower or 'não podemos garantir tempo' in line_lower:
                buckets['atencao'].append(line)
            elif len(line) > 60:
                buckets['vibe'].append(line)
                
        elif state == 'cronograma':
            if current_day:
                current_day['descricao'].append(line)
                
        elif state == 'incluso':
            if 'investimento' not in line_lower:
                buckets['incluso'].append(line)
                
        elif state == 'nao_incluso':
            if 'investimento' not in line_lower:
                buckets['nao_incluso'].append(line)
                
        elif state == 'investimento':
            buckets['investimento'].append(line)
            
        elif state == 'politica':
            buckets['politica'].append(line)
            
        elif state == 'faq':
            buckets['faq'].append(line)
            
    # Post processing
    for step in buckets['cronograma']:
        step['descricao'] = '\n'.join(step['descricao'])
        
    faq_list = []
    q = None
    for f in buckets['faq']:
        if '?' in f or 'quais' in f.lower() or 'como' in f.lower() or 'documentos' in f.lower():
            if q:
                faq_list.append({"pergunta": q, "resposta": ""})
            q = f
        else:
            if q:
                faq_list.append({"pergunta": q, "resposta": f})
                q = None
            else:
                if faq_list:
                    faq_list[-1]["resposta"] += "\n" + f
    if q:
        faq_list.append({"pergunta": q, "resposta": ""})
    buckets['faq'] = faq_list
    
    return buckets


with open('structured_copy.json', 'r', encoding='utf-8') as f:
    structured = json.load(f)

for url in urls:
    parsed = parse_url(url)
    if parsed:
        structured[url] = parsed
        
with open('structured_copy.json', 'w', encoding='utf-8') as f:
    json.dump(structured, f, ensure_ascii=False, indent=4)

print("Mass clone finished!")
